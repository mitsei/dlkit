"""JSON implementations of osid sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# import inflection


import datetime
import socket


from bson.objectid import ObjectId
from importlib import import_module


from .. import types
from .. import utilities
from ..cataloging.objects import Catalog
from ..locale.objects import Locale
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from ..utilities import camel_to_under
from ..utilities import get_authenticated_agent_id_with_proxy
from ..utilities import get_authenticated_agent_with_proxy
from ..utilities import get_effective_agent_id_with_proxy
from ..utilities import get_effective_agent_with_proxy
from ..utilities import get_locale_with_proxy
from ..utilities import get_provider_manager
from ..utilities import is_authenticated_with_proxy
from ..utilities import make_catalog_map
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid import sessions as abc_osid_sessions


COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
EFFECTIVE = 0
ANY_EFFECTIVE = 1
CREATED = True
UPDATED = True


class OsidSession(abc_osid_sessions.OsidSession):
    """The ``OsidSession`` is the top level interface for all OSID sessions.

    An ``OsidSession`` is created through its corresponding
    ``OsidManager``. A new ``OsidSession`` should be created for each
    user of a service and for each processing thread. A session
    maintains a single authenticated user and is not required to ensure
    thread-protection. A typical OSID session defines a set of service
    methods corresponding to some compliance level as defined by the
    service and is generally responsible for the management and
    retrieval of ``OsidObjects``.

    ``OsidSession`` defines a set of common methods used throughout all
    OSID sessions. An OSID session may optionally support transactions
    through the transaction interface.

    """
    def __init__(self):
        self._proxy = None
        self._runtime = None
        self._catalog_identifier = None
        self._my_catalog_map = None
        self._catalog_id = None
        self._catalog = None
        self._forms = None
        self._object_view = COMPARATIVE
        self._catalog_view = ISOLATED
        self._effective_view = ANY_EFFECTIVE
        self._authority = 'ODL.MIT.EDU'
        self._cataloging_manager = None
        self._catalog_session = None

    def _init_proxy_and_runtime(self, proxy, runtime):
        self._proxy = proxy
        self._runtime = runtime
        if runtime is not None:
            try:
                authority_param_id = Id('parameter:authority@mongo')
                self._authority = runtime.get_configuration().get_value_by_parameter(
                    authority_param_id).get_string_value()
            except (KeyError, errors.NotFound):
                self._authority = 'ODL.MIT.EDU'

    def _init_catalog(self, proxy=None, runtime=None):
        """Initialize this session as an OsidCatalog based session."""
        self._init_proxy_and_runtime(proxy, runtime)
        osid_name = self._session_namespace.split('.')[0]
        try:
            config = self._runtime.get_configuration()
            parameter_id = Id('parameter:' + osid_name + 'CatalogingProviderImpl@mongo')
            provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
            self._cataloging_manager = self._runtime.get_manager('CATALOGING', provider_impl)  # need to add version argument
        except (AttributeError, KeyError, errors.NotFound):
            pass

    def _init_object(self, catalog_id, proxy, runtime, db_name, cat_name, cat_class):
        """Initialize this session an OsidObject based session."""
        self._catalog_identifier = None
        self._init_proxy_and_runtime(proxy, runtime)

        uses_cataloging = False
        if catalog_id is not None and catalog_id.get_identifier() != PHANTOM_ROOT_IDENTIFIER:
            self._catalog_identifier = catalog_id.get_identifier()

            config = self._runtime.get_configuration()
            parameter_id = Id('parameter:' + db_name + 'CatalogingProviderImpl@mongo')

            try:
                provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
            except (AttributeError, KeyError, errors.NotFound):
                collection = JSONClientValidated(db_name,
                                                 collection=cat_name,
                                                 runtime=self._runtime)
                try:
                    self._my_catalog_map = collection.find_one({'_id': ObjectId(self._catalog_identifier)})
                except errors.NotFound:
                    if catalog_id.get_identifier_namespace() != db_name + '.' + cat_name:
                        self._my_catalog_map = self._create_orchestrated_cat(catalog_id, db_name, cat_name)
                    else:
                        raise errors.NotFound('could not find catalog identifier ' + catalog_id.get_identifier() + cat_name)
            else:
                uses_cataloging = True
                cataloging_manager = self._runtime.get_manager('CATALOGING',
                                                               provider_impl)  # need to add version argument
                lookup_session = cataloging_manager.get_catalog_lookup_session()
                # self._my_catalog_map = lookup_session.get_catalog(catalog_id)._my_map
                # self._catalog = Catalog(osid_object_map=self._my_catalog_map, runtime=self._runtime,
                #                         proxy=self._proxy)
                self._catalog = lookup_session.get_catalog(catalog_id)
        else:
            self._catalog_identifier = PHANTOM_ROOT_IDENTIFIER
            self._my_catalog_map = make_catalog_map(cat_name, identifier=self._catalog_identifier)

        if not uses_cataloging:
            self._catalog = cat_class(osid_object_map=self._my_catalog_map, runtime=self._runtime, proxy=self._proxy)

        self._catalog._authority = self._authority  # there should be a better way...
        self._catalog_id = self._catalog.get_id()
        self._forms = dict()

    def _get_phantom_root_catalog(self, cat_name, cat_class):
        """Get's the catalog id corresponding to the root of all implementation catalogs."""
        catalog_map = make_catalog_map(cat_name, identifier=PHANTOM_ROOT_IDENTIFIER)
        return cat_class(osid_object_map=catalog_map, runtime=self._runtime, proxy=self._proxy)

    def _create_orchestrated_cat(self, foreign_catalog_id, db_name, cat_name):
        """Creates a catalog in the current service orchestrated with a foreign service Id."""
        if (foreign_catalog_id.identifier_namespace == db_name + '.' + cat_name and
                foreign_catalog_id.authority == self._authority):
            raise errors.NotFound()  # This is not a foreign catalog
        foreign_service_name = foreign_catalog_id.get_identifier_namespace().split('.')[0]
        # foreign_cat_name = inflection.underscore(foreign_catalog_id.namespace.split('.')[1])
        # catalog_name = foreign_cat_name.lower()
        catalog_name = camel_to_under(foreign_catalog_id.namespace.split('.')[1])
        manager = self._get_provider_manager(foreign_service_name.upper())
        lookup_session = getattr(manager, 'get_{0}_lookup_session'.format(catalog_name))(proxy=self._proxy)
        getattr(lookup_session, 'get_{0}'.format(catalog_name))(foreign_catalog_id)  # Raises NotFound
        collection = JSONClientValidated(db_name,
                                         collection=cat_name,
                                         runtime=self._runtime)
        foreign_identifier = ObjectId(foreign_catalog_id.get_identifier())
        default_text = 'Orchestrated ' + foreign_service_name
        catalog_map = make_catalog_map(cat_name, identifier=foreign_identifier, default_text=default_text)
        collection.insert_one(catalog_map)
        alias_id = Id(identifier=foreign_catalog_id.identifier,
                      namespace=db_name + '.' + cat_name,
                      authority=self._authority)
        try:
            admin_session = getattr(manager, 'get_{0}_admin_session'.format(catalog_name))(proxy=self._proxy)
            getattr(admin_session, 'alias_{0}'.format(catalog_name))(foreign_catalog_id, alias_id)
        except (errors.Unimplemented, AttributeError):
            pass
        return catalog_map

    def _get_provider_manager(self, osid, local=False):
        """Gets the most appropriate provider manager depending on config."""
        return get_provider_manager(osid, runtime=self._runtime, proxy=self._proxy, local=local)

    def _get_id(self, id_, pkg_name):
        """
        Returns the primary id given an alias.

        If the id provided is not in the alias table, it will simply be
        returned as is.

        Only looks within the Id Alias namespace for the session package

        """
        collection = JSONClientValidated('id',
                                         collection=pkg_name + 'Ids',
                                         runtime=self._runtime)
        try:
            result = collection.find_one({'aliasIds': {'$in': [str(id_)]}})
        except errors.NotFound:
            return id_
        else:
            return Id(result['_id'])

    def _alias_id(self, primary_id, equivalent_id):
        """Adds the given equivalent_id as an alias for primary_id if possible"""
        pkg_name = primary_id.get_identifier_namespace().split('.')[0]
        obj_name = primary_id.get_identifier_namespace().split('.')[1]
        collection = JSONClientValidated(pkg_name,
                                         collection=obj_name,
                                         runtime=self._runtime)
        collection.find_one({'_id': ObjectId(primary_id.get_identifier())})  # to raise NotFound
        collection = JSONClientValidated('id',
                                         collection=pkg_name + 'Ids',
                                         runtime=self._runtime)
        try:
            result = collection.find_one({'aliasIds': {'$in': [str(equivalent_id)]}})
        except errors.NotFound:
            pass
        else:
            result['aliasIds'].remove(str(equivalent_id))
            collection.save(result)
        try:
            id_map = collection.find_one({'_id': str(primary_id)})
        except errors.NotFound:
            collection.insert_one({'_id': str(primary_id), 'aliasIds': [str(equivalent_id)]})
        else:
            id_map['aliasIds'].append(str(equivalent_id))
            collection.save(id_map)

    def _get_catalog_idstrs(self):
        """Returns the proper list of catalog idstrs based on catalog view"""
        if self._catalog_view == ISOLATED:
            return [str(self._catalog_id)]
        else:
            return self._get_descendent_cat_idstrs(self._catalog_id)

    def _get_descendent_cat_idstrs(self, cat_id, hierarchy_session=None):
        """Recursively returns a list of all descendent catalog ids, inclusive"""
        def get_descendent_ids(h_session):
            idstr_list = [str(cat_id)]
            if h_session is None:
                pkg_name = cat_id.get_identifier_namespace().split('.')[0]
                cat_name = cat_id.get_identifier_namespace().split('.')[1]
                try:
                    mgr = self._get_provider_manager('HIERARCHY')
                    h_session = mgr.get_hierarchy_traversal_session_for_hierarchy(
                        Id(authority=pkg_name.upper(),
                           namespace='CATALOG',
                           identifier=cat_name.upper()),
                        proxy=self._proxy)
                except (errors.OperationFailed, errors.Unsupported):
                    return idstr_list  # there is no hierarchy
            if h_session.has_children(cat_id):
                for child_id in h_session.get_children(cat_id):
                    idstr_list += self._get_descendent_cat_idstrs(child_id, h_session)
            return list(set(idstr_list))

        use_caching = False
        try:
            config = self._runtime.get_configuration()
            parameter_id = Id('parameter:useCachingForQualifierIds@json')
            if config.get_value_by_parameter(parameter_id).get_boolean_value():
                use_caching = True
            else:
                pass
        except (AttributeError, KeyError, errors.NotFound):
            pass
        if use_caching:
            key = 'descendent-catalog-ids-{0}'.format(str(cat_id))

            # If configured to use memcache as the caching engine, use it.
            # Otherwise default to diskcache
            caching_engine = 'diskcache'

            try:
                config = self._runtime.get_configuration()
                parameter_id = Id('parameter:cachingEngine@json')
                caching_engine = config.get_value_by_parameter(parameter_id).get_string_value()
            except (AttributeError, KeyError, errors.NotFound):
                pass

            if caching_engine == 'memcache':
                import memcache
                caching_host = '127.0.0.1:11211'
                try:
                    config = self._runtime.get_configuration()
                    parameter_id = Id('parameter:cachingHostURI@json')
                    caching_host = config.get_value_by_parameter(parameter_id).get_string_value()
                except (AttributeError, KeyError, errors.NotFound):
                    pass

                mc = memcache.Client([caching_host], debug=0)

                catalog_ids = mc.get(key)
                if catalog_ids is None:
                    catalog_ids = get_descendent_ids(hierarchy_session)
                    mc.set(key, catalog_ids)
            elif caching_engine == 'diskcache':
                import diskcache
                with diskcache.Cache('/tmp/dlkit_cache') as cache:
                    # A little bit non-DRY, since it's almost the same as for memcache above.
                    # However, for diskcache.Cache, we have to call ".close()" or use a
                    #   ``with`` statement to safeguard calling ".close()", so we keep this
                    #   separate from the memcache implementation.
                    catalog_ids = cache.get(key)
                    if catalog_ids is None:
                        catalog_ids = get_descendent_ids(hierarchy_session)
                        cache.set(key, catalog_ids)
            else:
                raise errors.NotFound('The {0} caching engine was not found.'.format(caching_engine))
        else:
            catalog_ids = get_descendent_ids(hierarchy_session)
        return catalog_ids

    def _is_phantom_root_federated(self):
        return (self._catalog_view == FEDERATED and
                self._catalog_id.get_identifier() == '000000000000000000000000')

    def _use_comparative_object_view(self):
        self._object_view = COMPARATIVE

    def _use_plenary_object_view(self):
        self._object_view = PLENARY

    def _use_federated_catalog_view(self):
        self._catalog_view = FEDERATED

    def _use_isolated_catalog_view(self):
        self._catalog_view = ISOLATED

    def _use_effective_view(self):
        self._effective_view = EFFECTIVE

    def _use_any_effective_view(self):
        self._effective_view = ANY_EFFECTIVE

    def _effective_view_filter(self):
        """Returns the mongodb relationship filter for effective views"""
        if self._effective_view == EFFECTIVE:
            now = datetime.datetime.utcnow()
            return {'startDate': {'$$lte': now}, 'endDate': {'$$gte': now}}
        return {}

    def _view_filter(self):
        """
        Returns the mongodb catalog filter for isolated or federated views.

        This also searches across all underlying catalogs in federated
        catalog views. Real authz for controlling access to underlying
        catalogs will need to be managed in an adapter above the
        pay grade of this implementation.

        """
        if self._is_phantom_root_federated():
            return {}
        idstr_list = self._get_catalog_idstrs()
        return {'assigned' + self._catalog_name + 'Ids': {'$in': idstr_list}}
        # return {'assigned' + utilities.format_catalog(self._catalog_name) + 'Ids': {'$in': idstr_list}}

    def _assign_object_to_catalog(self, obj_id, cat_id):
        pkg_name = obj_id.get_identifier_namespace().split('.')[0]
        obj_name = obj_id.get_identifier_namespace().split('.')[1]
        catalog_key = 'assigned' + self._catalog_name + 'Ids'
        collection = JSONClientValidated(pkg_name,
                                         collection=obj_name,
                                         runtime=self._runtime)
        obj_map = collection.find_one({'_id': ObjectId(obj_id.get_identifier())})
        if catalog_key in obj_map:
            if str(cat_id) in obj_map[catalog_key]:
                raise errors.AlreadyExists()
            else:
                obj_map[catalog_key].append(str(cat_id))
        else:
            obj_map[catalog_key] = [str(cat_id)]
        collection.save(obj_map)

    def _unassign_object_from_catalog(self, obj_id, cat_id):
        pkg_name = obj_id.get_identifier_namespace().split('.')[0]
        obj_name = obj_id.get_identifier_namespace().split('.')[1]
        catalog_key = 'assigned' + self._catalog_name + 'Ids'
        collection = JSONClientValidated(pkg_name,
                                         collection=obj_name,
                                         runtime=self._runtime)
        obj_map = collection.find_one({'_id': ObjectId(obj_id.get_identifier())})
        if obj_map[catalog_key] == [str(cat_id)]:
            raise errors.OperationFailed('unassigning object from ${cat_name_under} would leave it unattached')
        try:
            obj_map[catalog_key].remove(str(cat_id))
        except (KeyError, ValueError):
            raise errors.NotFound()
        collection.save(obj_map)

    def get_locale(self):
        """Gets the locale indicating the localization preferences in effect for this session.

        return: (osid.locale.Locale) - the locale
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_locale_with_proxy(self._proxy)

    locale = property(fget=get_locale)

    def is_authenticated(self):
        """Tests if an agent is authenticated to this session.

        return: (boolean) - ``true`` if valid authentication credentials
                exist, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return is_authenticate_with_proxy(self._proxy)

    def get_authenticated_agent_id(self):
        """Gets the ``Id`` of the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        return: (osid.id.Id) - the authenticated agent ``Id``
        raise:  IllegalState - ``is_authenticated()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_authenticated_agent_id_with_proxy(self._proxy)

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        """Gets the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        return: (osid.authentication.Agent) - the authenticated agent
        raise:  IllegalState - ``is_authenticated()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_authenticated_agent_with_proxy(self._proxy)

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        """Gets the ``Id`` of the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        return: (osid.id.Id) - the effective agent
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_effective_agent_id_with_proxy(self._proxy)

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        """Gets the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        return: (osid.authentication.Agent) - the effective agent
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return get_effective_agent_id_with_proxy(self._proxy)  # Currently raises Unimplemented

    effective_agent = property(fget=get_effective_agent)

    def get_date(self):
        """Gets the service date which may be the current date or the effective date in which this session exists.

        return: (timestamp) - the service date
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    date = property(fget=get_date)

    def get_clock_rate(self):
        """Gets the rate of the service clock.

        return: (decimal) - the clock rate
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    clock_rate = property(fget=get_clock_rate)

    def get_format_type(self):
        """Gets the ``DisplayText`` format ``Type`` preference in effect for this session.

        return: (osid.type.Type) - the effective ``DisplayText`` format
                ``Type``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    format_type = property(fget=get_format_type)

    def supports_transactions(self):
        """Tests for the availability of transactions.

        return: (boolean) - ``true`` if transaction methods are
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def start_transaction(self):
        """Starts a new transaction for this sesson.

        Transactions are a means for an OSID to provide an all-or-
        nothing set of operations within a session and may be used to
        coordinate this service from an external transaction manager. A
        session supports one transaction at a time. Starting a second
        transaction before the previous has been committed or aborted
        results in an ``IllegalState`` error.

        return: (osid.transaction.Transaction) - a new transaction
        raise:  IllegalState - a transaction is already open
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - transactions not supported
        *compliance: optional -- This method must be implemented if
        ``supports_transactions()`` is true.*
        *implementation notes*: Ideally, a provider that supports
        transactions should guarantee atomicity, consistency, isolation
        and durability in a 2 phase commit process. This is not always
        possible in distributed systems and a transaction provider may
        simply allow for a means of processing bulk updates.  To
        maximize interoperability, providers should honor the one-
        transaction-at-a-time rule.

        """
        raise errors.Unimplemented()
