"""JSON implementations of cataloging sessions."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from bson.objectid import ObjectId


from . import objects
from . import queries
from .. import utilities
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from dlkit.abstract_osid.cataloging import sessions as abc_cataloging_sessions
from dlkit.abstract_osid.cataloging.objects import CatalogForm as ABCCatalogForm
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.primitives import Type as ABCType


DESCENDING = -1
ASCENDING = 1
COMPARATIVE = 0
PLENARY = 1
CREATED = True
UPDATED = True
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')


class CatalogLookupSession(abc_cataloging_sessions.CatalogLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Catalog`` objects.

    The ``Catalog`` represents a collection of OSID ``Ids``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Catalogs`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Catalogs``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.

    """
    _session_namespace = 'cataloging.CatalogLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_catalogs(self):
        """Tests if this user can perform ``Catalog`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.can_lookup_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_lookup_catalogs()
        return True

    def use_comparative_catalog_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_catalog_view(self):
        """A complete view of the ``Catalog`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    @utilities.arguments_not_none
    def get_catalog(self, catalog_id):
        """Gets the ``Catalog`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Catalog`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Catalog`` and retained for
        compatibility.

        arg:    catalog_id (osid.id.Id): ``Id`` of the ``Catalog``
        return: (osid.cataloging.Catalog) - the catalog
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=catalog_id)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if catalog_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.Catalog, cat_name='Catalog')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(catalog_id, 'cataloging').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Catalog.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(catalog_id, 'cataloging', 'Catalog')

        return objects.Catalog(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_catalogs_by_ids(self, catalog_ids):
        """Gets a ``CatalogList`` corresponding to the given catalog ``IdList``.

        In plenary mode, the returned list contains all of the catalogs
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Catalogs`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    catalog_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.cataloging.CatalogList) - the returned ``Catalog
                list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``catalog_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Catalog() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=catalog_ids)
        catalog_id_list = []
        for i in catalog_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.CatalogList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_catalogs_by_genus_type(self, catalog_genus_type):
        """Gets a ``CatalogList`` corresponding to the given catalog genus ``Type`` which does not include catalogs of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known catalogs
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        arg:    catalog_genus_type (osid.type.Type): a catalog genus
                type
        return: (osid.cataloging.CatalogList) - the returned ``Catalog
                list``
        raise:  NullArgument - ``catalog_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=catalog_genus_type)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(catalog_genus_type)}).sort('_id', DESCENDING)

        return objects.CatalogList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_catalogs_by_parent_genus_type(self, catalog_genus_type):
        """Gets a ``CatalogList`` corresponding to the given catalog genus ``Type`` and include any additional catalogs with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known catalogs
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        arg:    catalog_genus_type (osid.type.Type): a catalog genus
                type
        return: (osid.cataloging.CatalogList) - the returned ``Catalog
                list``
        raise:  NullArgument - ``catalog_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_catalogs_by_record_type(self, catalog_record_type):
        """Gets a ``CatalogList`` containing the given subject record ``Type``.

        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        arg:    catalog_record_type (osid.type.Type): a catalog record
                type
        return: (osid.cataloging.CatalogList) - the returned ``Catalog
                list``
        raise:  NullArgument - ``catalog_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_catalogs_by_provider(self, resource_id):
        """Gets a ``CatalogList`` from the given provider.

        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.cataloging.CatalogList) - the returned ``Catalog
                list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_catalogs(self):
        """Gets all ``Catalogs``.

        In plenary mode, the returned list contains all known catalogs
        or an error results. Otherwise, the returned list may contain
        only those catalogs that are accessible through this session.

        return: (osid.cataloging.CatalogList) - a list of ``Catalogs``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.CatalogList(result, runtime=self._runtime, proxy=self._proxy)

    catalogs = property(fget=get_catalogs)


class CatalogQuerySession(abc_cataloging_sessions.CatalogQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching ``Catalog`` objects.

    The search query is constructed using the ``CatalogQuery``. The
    catalog record ``Type`` also specifies the record for the catalog
    query.

    Catalogs may have a query record indicated by their respective
    record types. The query record is accessed via the ``CatalogQuery``.

    """
    _session_namespace = 'cataloging.CatalogQuerySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_query_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_search_catalogs(self):
        """Tests if this user can perform ``Catalog`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.can_search_bins_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def get_catalog_query(self):
        """Gets a catalog query.

        The returned query will not have an extension query.

        return: (osid.cataloging.CatalogQuery) - the catalog query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.get_bin_query_template
        return queries.CatalogQuery(runtime=self._runtime)

    catalog_query = property(fget=get_catalog_query)

    @utilities.arguments_not_none
    def get_catalogs_by_query(self, catalog_query):
        """Gets a list of ``Catalogs`` matching the given catalog query.

        arg:    catalog_query (osid.cataloging.CatalogQuery): the
                catalog query
        return: (osid.cataloging.CatalogList) - the returned
                ``CatalogList``
        raise:  NullArgument - ``catalog_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``catalog_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_query(catalog_query)
        query_terms = dict(catalog_query._query_terms)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        result = collection.find(query_terms).sort('_id', DESCENDING)

        return objects.CatalogList(result, runtime=self._runtime)


class CatalogAdminSession(abc_cataloging_sessions.CatalogAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Catalogs``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Catalog,`` a ``CatalogForm`` is requested using
    ``get_catalog_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``CatalogForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``CatalogForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``CatalogForm``
    corresponds to an attempted transaction.

    For updates, ``CatalogForms`` are requested to the ``Catalog``
    ``Id`` that is to be updated using ``getCatalogFormForUpdate()``.
    Similarly, the ``CatalogForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``CatalogForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Catalogs``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    _session_namespace = 'cataloging.CatalogAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_catalogs(self):
        """Tests if this user can create ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Catalog`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``Catalog`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs()
        return True

    @utilities.arguments_not_none
    def can_create_catalog_with_record_types(self, catalog_record_types):
        """Tests if this user can create a single ``Catalog`` using the desired record types.

        While ``CatalogingManager.getCatalogRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Catalog``.
        Providing an empty array tests if a ``Catalog`` can be created
        with no records.

        arg:    catalog_record_types (osid.type.Type[]): array of
                catalog record types
        return: (boolean) - ``true`` if ``Catalog`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``catalog_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=catalog_record_types)
        return True

    @utilities.arguments_not_none
    def get_catalog_form_for_create(self, catalog_record_types):
        """Gets the catalog form for creating new catalogs.

        A new form should be requested for each create transaction.

        arg:    catalog_record_types (osid.type.Type[]): array of
                catalog record types
        return: (osid.cataloging.CatalogForm) - the catalog form
        raise:  NullArgument - ``catalog_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=catalog_record_types)
        for arg in catalog_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if catalog_record_types == []:
            result = objects.CatalogForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.CatalogForm(
                record_types=catalog_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_catalog(self, catalog_form):
        """Creates a new ``Catalog``.

        arg:    catalog_form (osid.cataloging.CatalogForm): the form for
                this ``Catalog``
        return: (osid.cataloging.Catalog) - the new ``Catalog``
        raise:  IllegalState - ``catalog_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``catalog_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``catalog_form`` did not originate from
                ``get_catalog_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=catalog_form)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        if not isinstance(catalog_form, ABCCatalogForm):
            raise errors.InvalidArgument('argument type is not an CatalogForm')
        if catalog_form.is_for_update():
            raise errors.InvalidArgument('the CatalogForm is for update only, not create')
        try:
            if self._forms[catalog_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('catalog_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('catalog_form did not originate from this session')
        if not catalog_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(catalog_form._my_map)

        self._forms[catalog_form.get_id().get_identifier()] = CREATED
        result = objects.Catalog(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_catalogs(self):
        """Tests if this user can update ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Catalog`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        return: (boolean) - ``false`` if ``Catalog`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_update_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_update_catalogs()
        return True

    @utilities.arguments_not_none
    def get_catalog_form_for_update(self, catalog_id):
        """Gets the catalog form for updating an existing catalog.

        A new catalog form should be requested for each update
        transaction.

        arg:    catalog_id (osid.id.Id): the ``Id`` of the ``Catalog``
        return: (osid.cataloging.CatalogForm) - the catalog form
        raise:  NotFound - ``catalog_id`` is not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=catalog_id)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        if not isinstance(catalog_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(catalog_id.get_identifier())})

        cat_form = objects.CatalogForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_catalog(self, catalog_form):
        """Updates an existing catalog.

        arg:    catalog_form (osid.cataloging.CatalogForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``catalog_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``catalog_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``catalog_form`` did not originate from
                ``get_catalog_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=catalog_form)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        if not isinstance(catalog_form, ABCCatalogForm):
            raise errors.InvalidArgument('argument type is not an CatalogForm')
        if not catalog_form.is_for_update():
            raise errors.InvalidArgument('the CatalogForm is for update only, not create')
        try:
            if self._forms[catalog_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('catalog_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('catalog_form did not originate from this session')
        if not catalog_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(catalog_form._my_map)  # save is deprecated - change to replace_one

        self._forms[catalog_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Catalog(osid_object_map=catalog_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_catalogs(self):
        """Tests if this user can delete ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Catalog`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``Catalog`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_delete_bins
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_delete_catalogs()
        return True

    @utilities.arguments_not_none
    def delete_catalog(self, catalog_id):
        """Deletes a ``Catalog``.

        arg:    catalog_id (osid.id.Id): the ``Id`` of the ``Catalog``
                to remove
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=bin_id)
        collection = JSONClientValidated('cataloging',
                                         collection='Catalog',
                                         runtime=self._runtime)
        if not isinstance(catalog_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection.delete_one({'_id': ObjectId(catalog_id.get_identifier())})

    def can_manage_catalog_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Catalogs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Catalog`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_catalog(self, catalog_id, alias_id):
        """Adds an ``Id`` to a ``Catalog`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Catalog`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another catalog, it is
        reassigned to the given catalog ``Id``.

        arg:    catalog_id (osid.id.Id): the ``Id`` of a ``Catalog``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=catalog_id, alias_id=alias_id)
        self._alias_id(primary_id=catalog_id, equivalent_id=alias_id)


class CatalogHierarchySession(abc_cataloging_sessions.CatalogHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Catalog`` objects.

    Each node in the hierarchy is a unique ``Catalog``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_catalogs()`` and ``getChildCatalogs()``. To relate
    these ``Ids`` to another OSID, ``get_catalog_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Catalog`` available in the Catalog OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_catalogs()`` or ``get_child_catalogs()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: catalog elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    _session_namespace = 'cataloging.CatalogHierarchySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchySession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_traversal_session_for_hierarchy(
                Id(authority='CATALOGING',
                   namespace='CATALOG',
                   identifier='CATALOG'),
                proxy=self._proxy)

    def get_catalog_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    def get_catalog_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    def can_access_catalog_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_access_catalog_hierarchy()
        return True

    def use_comparative_catalog_view(self):
        """The returns from the catalog methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_catalog_view(self):
        """A complete view of the ``Catalog`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_plenary_bin_view
        self._catalog_view = PLENARY
        if self._catalog_session is not None:
            self._catalog_session.use_plenary_catalog_view()

    def get_root_catalog_ids(self):
        """Gets the root catalog ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root catalog ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalog_ids()
        return self._hierarchy_session.get_roots()

    root_catalog_ids = property(fget=get_root_catalog_ids)

    def get_root_catalogs(self):
        """Gets the root catalogs in the catalog hierarchy.

        A node with no parents is an orphan. While all catalog ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        return: (osid.cataloging.CatalogList) - the root catalogs
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalogs()
        return CatalogLookupSession(
            self._proxy,
            self._runtime).get_catalogs_by_ids(list(self.get_root_catalog_ids()))

    root_catalogs = property(fget=get_root_catalogs)

    @utilities.arguments_not_none
    def has_parent_catalogs(self, catalog_id):
        """Tests if the ``Catalog`` has any parents.

        arg:    catalog_id (osid.id.Id): a catalog ``Id``
        return: (boolean) - ``true`` if the catalog has parents,
                ``false`` otherwise
        raise:  NotFound - ``catalog_id`` is not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_parent_catalogs(catalog_id=catalog_id)
        return self._hierarchy_session.has_parents(id_=catalog_id)

    @utilities.arguments_not_none
    def is_parent_of_catalog(self, id_, catalog_id):
        """Tests if an ``Id`` is a direct parent of a catalog.

        arg:    id (osid.id.Id): an ``Id``
        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``catalog_id,``  ``false`` otherwise
        raise:  NotFound - ``catalog_id`` is not found
        raise:  NullArgument - ``id`` or ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_parent_of_catalog(id_=id_, catalog_id=catalog_id)
        return self._hierarchy_session.is_parent(id_=catalog_id, parent_id=id_)

    @utilities.arguments_not_none
    def get_parent_catalog_ids(self, catalog_id):
        """Gets the parent ``Ids`` of the given catalog.

        arg:    catalog_id (osid.id.Id): a catalog ``Id``
        return: (osid.id.IdList) - the parent ``Ids`` of the catalog
        raise:  NotFound - ``catalog_id`` is not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalog_ids(catalog_id=catalog_id)
        return self._hierarchy_session.get_parents(id_=catalog_id)

    @utilities.arguments_not_none
    def get_parent_catalogs(self, catalog_id):
        """Gets the parent catalogs of the given ``id``.

        arg:    catalog_id (osid.id.Id): the ``Id`` of the ``Catalog``
                to query
        return: (osid.cataloging.CatalogList) - the parent catalogs of
                the ``id``
        raise:  NotFound - a ``Catalog`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalogs(catalog_id=catalog_id)
        return CatalogLookupSession(
            self._proxy,
            self._runtime).get_catalogs_by_ids(
                list(self.get_parent_catalog_ids(catalog_id)))

    @utilities.arguments_not_none
    def is_ancestor_of_catalog(self, id_, catalog_id):
        """Tests if an ``Id`` is an ancestor of a catalog.

        arg:    id (osid.id.Id): an ``Id``
        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``catalogId``.  ``false`` otherwise
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_ancestor_of_catalog(id_=id_, catalog_id=catalog_id)
        return self._hierarchy_session.is_ancestor(id_=id_, ancestor_id=catalog_id)

    @utilities.arguments_not_none
    def has_child_catalogs(self, catalog_id):
        """Tests if a catalog has any children.

        arg:    catalog_id (osid.id.Id): a ``catalog_id``
        return: (boolean) - ``true`` if the ``catalog_id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``catalog_id`` is not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_child_catalogs(catalog_id=catalog_id)
        return self._hierarchy_session.has_children(id_=catalog_id)

    @utilities.arguments_not_none
    def is_child_of_catalog(self, id_, catalog_id):
        """Tests if a catalog is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``catalog_id,``  ``false`` otherwise
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_child_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_child_of_catalog(id_=id_, catalog_id=catalog_id)
        return self._hierarchy_session.is_child(id_=catalog_id, child_id=id_)

    @utilities.arguments_not_none
    def get_child_catalog_ids(self, catalog_id):
        """Gets the child ``Ids`` of the given catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the catalog
        raise:  NotFound - ``catalog_id`` is not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalog_ids(catalog_id=catalog_id)
        return self._hierarchy_session.get_children(id_=catalog_id)

    @utilities.arguments_not_none
    def get_child_catalogs(self, catalog_id):
        """Gets the child catalogs of the given ``id``.

        arg:    catalog_id (osid.id.Id): the ``Id`` of the ``Catalog``
                to query
        return: (osid.cataloging.CatalogList) - the child catalogs of
                the ``id``
        raise:  NotFound - a ``Catalog`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalogs(catalog_id=catalog_id)
        return CatalogLookupSession(
            self._proxy,
            self._runtime).get_catalogs_by_ids(
                list(self.get_child_catalog_ids(catalog_id)))

    @utilities.arguments_not_none
    def is_descendant_of_catalog(self, id_, catalog_id):
        """Tests if an ``Id`` is a descendant of a catalog.

        arg:    id (osid.id.Id): an ``Id``
        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``catalog_id,``  ``false`` otherwise
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_descendant_of_catalog(id_=id_, catalog_id=catalog_id)
        return self._hierarchy_session.is_descendant(id_=id_, descendant_id=catalog_id)

    @utilities.arguments_not_none
    def get_catalog_node_ids(self, catalog_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a catalog node
        raise:  NotFound - a ``Catalog`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_node_ids(
                catalog_id=catalog_id,
                ancestor_levels=ancestor_levels,
                descendant_levels=descendant_levels,
                include_siblings=include_siblings)
        return self._hierarchy_session.get_nodes(
            id_=catalog_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)

    @utilities.arguments_not_none
    def get_catalog_nodes(self, catalog_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.cataloging.CatalogNode) - a catalog node
        raise:  NotFound - a ``Catalog`` identified by ``Id is`` not
                found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_nodes
        return objects.CatalogNode(self.get_catalog_node_ids(
            catalog_id=catalog_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)._my_map, runtime=self._runtime, proxy=self._proxy)


class CatalogHierarchyDesignSession(abc_cataloging_sessions.CatalogHierarchyDesignSession, osid_sessions.OsidSession):
    """This session manages a hierarchy of catalogs.

    ``Catalogs`` may be organized into a hierarchy for organizing or
    federating. A parent ``Catalog`` includes all of the Ids of its
    children such that a single root node contains all of the ``Ids`` of
    the federation.

    """
    _session_namespace = 'cataloging.CatalogHierarchyDesignSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.init_template
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        self._forms = dict()
        self._kwargs = kwargs
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_hierarchy_design_session()
        else:
            hierarchy_mgr = self._get_provider_manager('HIERARCHY')
            self._hierarchy_session = hierarchy_mgr.get_hierarchy_design_session_for_hierarchy(
                Id(authority='CATALOGING',
                   namespace='CATALOG',
                   identifier='CATALOG'),
                proxy=self._proxy)

    def get_catalog_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy_id()
        return self._hierarchy_session.get_hierarchy_id()

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    def get_catalog_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - assessment failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_hierarchy()
        return self._hierarchy_session.get_hierarchy()

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    def can_modify_catalog_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_modify_catalog_hierarchy()
        return True

    @utilities.arguments_not_none
    def add_root_catalog(self, catalog_id):
        """Adds a root catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        raise:  AlreadyExists - ``catalog_id`` is already in hierarchy
        raise:  NotFound - ``catalog_id`` not found
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_root_catalog(catalog_id=catalog_id)
        return self._hierarchy_session.add_root(id_=catalog_id)

    @utilities.arguments_not_none
    def remove_root_catalog(self, catalog_id):
        """Removes a root catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        raise:  NotFound - ``catalog_id`` is not a root
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_root_catalog(catalog_id=catalog_id)
        return self._hierarchy_session.remove_root(id_=catalog_id)

    @utilities.arguments_not_none
    def add_child_catalog(self, catalog_id, child_id):
        """Adds a child to a catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``catalog_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``catalog_id`` or ``child_id`` not found
        raise:  NullArgument - ``catalog_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_child_catalog(catalog_id=catalog_id, child_id=child_id)
        return self._hierarchy_session.add_child(id_=catalog_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_catalog(self, catalog_id, child_id):
        """Removes a child from a catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``catalog_id`` is not a parent of
                ``child_id``
        raise:  NullArgument - ``catalog_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalog(catalog_id=catalog_id, child_id=child_id)
        return self._hierarchy_session.remove_child(id_=catalog_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_catalogs(self, catalog_id):
        """Removes all children from a catalog.

        arg:    catalog_id (osid.id.Id): the ``Id`` of a catalog
        raise:  NotFound - ``catalog_id`` is not in hierarchy
        raise:  NullArgument - ``catalog_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalogs(catalog_id=catalog_id)
        return self._hierarchy_session.remove_children(id_=catalog_id)
