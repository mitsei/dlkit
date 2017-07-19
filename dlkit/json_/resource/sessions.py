"""JSON implementations of resource sessions."""

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
from . import searches
from .. import MONGO_LISTENER
from .. import utilities
from ..authentication.objects import AgentList
from ..id.objects import IdList
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from .simple_agent import Agent
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.resource import sessions as abc_resource_sessions
from dlkit.abstract_osid.resource.objects import BinForm as ABCBinForm
from dlkit.abstract_osid.resource.objects import ResourceForm as ABCResourceForm
from dlkit.abstract_osid.type.primitives import Type as ABCType


DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')
COMPARATIVE = 0
PLENARY = 1


class ResourceLookupSession(abc_resource_sessions.ResourceLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving resources.

    A ``Resource`` is an arbitrary entity that may represent a person,
    place or thing used to identify an object used in various services.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated bin view: All resource methods in this session operate,
        retrieve and pertain to resources defined explicitly in the
        current bin. Using an isolated view is useful for managing
        ``Resources`` with the ``ResourceAdminSession.``
      * federated bin view: All resource methods in this session
        operate, retrieve and pertain to all resources defined in this
        bin and any other resources implicitly available in this bin
        through bin inheritence.


    The methods ``use_federated_bin_view()`` and
    ``use_isolated_bin_view()`` behave as a radio group and one should
    be selected before invoking any lookup methods.

    Resources may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Resource``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bin
        self._catalog_name = 'Bin'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='resource',
            cat_name='Bin',
            cat_class=objects.Bin)
        self._kwargs = kwargs

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bin = property(fget=get_bin)

    def can_lookup_resources(self):
        """Tests if this user can perform ``Resource`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_resource_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_resource_view(self):
        """A complete view of the ``Resource`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_resource(self, resource_id):
        """Gets the ``Resource`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Resource`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Resource`` and retained for
        compatibility.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to retrieve
        return: (osid.resource.Resource) - the returned ``Resource``
        raise:  NotFound - no ``Resource`` found with the given ``Id``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(resource_id, 'resource').get_identifier())},
                 **self._view_filter()))
        return objects.Resource(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_resources_by_ids(self, resource_ids):
        """Gets a ``ResourceList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the resources
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Resources`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    resource_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``resource_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        object_id_list = []
        for i in resource_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'resource').get_identifier()))
        result = collection.find(
            dict({'_id': {'$in': object_id_list}},
                 **self._view_filter()))
        result = list(result)
        sorted_result = []
        for object_id in object_id_list:
            for object_map in result:
                if object_map['_id'] == object_id:
                    sorted_result.append(object_map)
                    break
        return objects.ResourceList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_resources_by_genus_type(self, resource_genus_type):
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` which does not include resources of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        arg:    resource_genus_type (osid.type.Type): a resource genus
                type
        return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        raise:  NullArgument - ``resource_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(resource_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.ResourceList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_resources_by_parent_genus_type(self, resource_genus_type):
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` and include any additional resources with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        arg:    resource_genus_type (osid.type.Type): a resource genus
                type
        return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        raise:  NullArgument - ``resource_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ResourceList([])

    @utilities.arguments_not_none
    def get_resources_by_record_type(self, resource_record_type):
        """Gets a ``ResourceList`` containing the given resource record ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        arg:    resource_record_type (osid.type.Type): a resource record
                type
        return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        raise:  NullArgument - ``resource_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ResourceList([])

    def get_resources(self):
        """Gets all ``Resources``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        return: (osid.resource.ResourceList) - a list of ``Resources``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.ResourceList(result, runtime=self._runtime, proxy=self._proxy)

    resources = property(fget=get_resources)


class ResourceQuerySession(abc_resource_sessions.ResourceQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Resource`` objects.

    The search query is constructed using the ``ResourceQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bin view: searches include resources in bins of which
        this bin is a ancestor in the bin hierarchy
      * isolated bin view: searches are restricted to resources in this
        bin


    Resources may have a resource record indicated by their respective
    record types. The resource query record is accessed via the
    ``ResourceQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bin
        self._catalog_name = 'Bin'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='resource',
            cat_name='Bin',
            cat_class=objects.Bin)
        self._kwargs = kwargs

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bin = property(fget=get_bin)

    def can_search_resources(self):
        """Tests if this user can perform ``Resource`` searches.

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
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_resource_query(self):
        """Gets a resource query.

        The returned query will not have an extension query.

        return: (osid.resource.ResourceQuery) - the resource query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.ResourceQuery(runtime=self._runtime)

    resource_query = property(fget=get_resource_query)

    @utilities.arguments_not_none
    def get_resources_by_query(self, resource_query):
        """Gets a list of ``Resources`` matching the given resource query.

        arg:    resource_query (osid.resource.ResourceQuery): the
                resource query
        return: (osid.resource.ResourceList) - the returned
                ``ResourceList``
        raise:  NullArgument - ``resource_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``resource_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in resource_query._query_terms:
            if '$in' in resource_query._query_terms[term] and '$nin' in resource_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': resource_query._query_terms[term]['$in']}},
                             {term: {'$nin': resource_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: resource_query._query_terms[term]})
        for term in resource_query._keyword_terms:
            or_list.append({term: resource_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('resource',
                                             collection='Resource',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.ResourceList(result, runtime=self._runtime, proxy=self._proxy)


class ResourceSearchSession(abc_resource_sessions.ResourceSearchSession, ResourceQuerySession):
    """This session provides methods for searching among ``Resource`` objects.

    The search query is constructed using the ``ResourceQuery``.

    ``get_resources_by_query()`` is the basic search method and returns
    a list of ``Resources``. A more advanced search may be performed
    with ``getResourcesBySearch()``. It accepts an ``ResourceSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_resources_by_search()`` returns an ``ResourceSearchResults``
    that can be used to access the resulting ``ResourceList`` or be used
    to perform a search within the result set through ``ResourceList``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bin view: searches include resources in bins of which
        this bin is a ancestor in the bin hierarchy
      * isolated bin view: searches are restricted to resources in this
        bin


    Resources may have a resource query record indicated by their
    respective record types. The resource query record is accessed via
    the ``ResourceQuery``.

    """

    def get_resource_search(self):
        """Gets a resource search.

        return: (osid.resource.ResourceSearch) - the resource search
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceSearchSession.get_resource_search_template
        return searches.ResourceSearch(runtime=self._runtime)

    resource_search = property(fget=get_resource_search)

    def get_resource_search_order(self):
        """Gets a resource search order.

        The ``ResourceSearchOrder`` is supplied to a ``ResourceSearch``
        to specify the ordering of results.

        return: (osid.resource.ResourceSearchOrder) - the resource
                search order
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    resource_search_order = property(fget=get_resource_search_order)

    @utilities.arguments_not_none
    def get_resources_by_search(self, resource_query, resource_search):
        """Gets the search results matching the given search query using the given search.

        arg:    resource_query (osid.resource.ResourceQuery): the
                resource query
        arg:    resource_search (osid.resource.ResourceSearch): the
                resource search
        return: (osid.resource.ResourceSearchResults) - the resource
                search results
        raise:  NullArgument - ``resource_query`` or ``resource_search``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``resource_query`` or ``resource_search``
                is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        # Copied from osid.resource.ResourceQuerySession.get_resources_by_query_template
        and_list = list()
        or_list = list()
        for term in resource_query._query_terms:
            and_list.append({term: resource_query._query_terms[term]})
        for term in resource_query._keyword_terms:
            or_list.append({term: resource_query._keyword_terms[term]})
        if resource_search._id_list is not None:
            identifiers = [ObjectId(i.identifier) for i in resource_search._id_list]
            and_list.append({'_id': {'$in': identifiers}})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        if resource_search.start is not None and resource_search.end is not None:
            result = collection.find(query_terms)[resource_search.start:resource_search.end]
        else:
            result = collection.find(query_terms)
        return searches.ResourceSearchResults(result, dict(resource_query._query_terms), runtime=self._runtime)

    @utilities.arguments_not_none
    def get_resource_query_from_inspector(self, resource_query_inspector):
        """Gets a resource query from an inspector.

        The inspector is available from a ``ResourceSearchResults``.

        arg:    resource_query_inspector
                (osid.resource.ResourceQueryInspector): a resource query
                inspector
        return: (osid.resource.ResourceQuery) - the resource query
        raise:  NullArgument - ``resource_query_inspector`` is ``null``
        raise:  Unsupported - ``resource_query_inspector`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ResourceAdminSession(abc_resource_sessions.ResourceAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Resources``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Resource,`` a ``ResourceForm`` is requested using
    ``get_resource_form_for_create()`` specifying desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ResourceForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ResourceForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ResourceForm``
    corresponds to an attempted transaction.

    For updates, ``ResourceForms`` are requested to the ``Resource``
    ``Id`` that is to be updated using ``getResourceFormForUpdate()``.
    Similarly, the ``ResourceForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``ResourceForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Resources``. To unmap a ``Resource``
    from the current ``Bin,`` the ``ResourceBinAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Resource`` itself thus removing it from all known ``Bin``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bin
        self._catalog_name = 'Bin'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='resource',
            cat_name='Bin',
            cat_class=objects.Bin)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bin = property(fget=get_bin)

    def can_create_resources(self):
        """Tests if this user can create ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Resource`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_resource_with_record_types(self, resource_record_types):
        """Tests if this user can create a single ``Resource`` using the desired record types.

        While ``ResourceManager.getResourceRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Resource``.
        Providing an empty array tests if a ``Resource`` can be created
        with no records.

        arg:    resource_record_types (osid.type.Type[]): array of
                resource record types
        return: (boolean) - ``true`` if ``Resource`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``resource_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_resource_form_for_create(self, resource_record_types):
        """Gets the resource form for creating new resources.

        A new form should be requested for each create transaction.

        arg:    resource_record_types (osid.type.Type[]): array of
                resource record types
        return: (osid.resource.ResourceForm) - the resource form
        raise:  NullArgument - ``resource_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in resource_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if resource_record_types == []:
            obj_form = objects.ResourceForm(
                bin_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.ResourceForm(
                bin_id=self._catalog_id,
                record_types=resource_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_resource(self, resource_form):
        """Creates a new ``Resource``.

        arg:    resource_form (osid.resource.ResourceForm): the form for
                this ``Resource``
        return: (osid.resource.Resource) - the new ``Resource``
        raise:  IllegalState - ``resource_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``resource_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``resource_form`` did not originate from
                ``get_resource_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        if not isinstance(resource_form, ABCResourceForm):
            raise errors.InvalidArgument('argument type is not an ResourceForm')
        if resource_form.is_for_update():
            raise errors.InvalidArgument('the ResourceForm is for update only, not create')
        try:
            if self._forms[resource_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('resource_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('resource_form did not originate from this session')
        if not resource_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(resource_form._my_map)

        self._forms[resource_form.get_id().get_identifier()] = CREATED
        result = objects.Resource(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_resources(self):
        """Tests if this user can update ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Resource`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_resource_form_for_update(self, resource_id):
        """Gets the resource form for updating an existing resource.

        A new resource form should be requested for each update
        transaction.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        return: (osid.resource.ResourceForm) - the resource form
        raise:  NotFound - ``resource_id`` is not found
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        if not isinstance(resource_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (resource_id.get_identifier_namespace() != 'resource.Resource' or
                resource_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(resource_id.get_identifier())})

        obj_form = objects.ResourceForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_resource(self, resource_form):
        """Updates an existing resource.

        arg:    resource_form (osid.resource.ResourceForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``resource_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``resource_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``resource_form`` did not originate from
                ``get_resource_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        if not isinstance(resource_form, ABCResourceForm):
            raise errors.InvalidArgument('argument type is not an ResourceForm')
        if not resource_form.is_for_update():
            raise errors.InvalidArgument('the ResourceForm is for update only, not create')
        try:
            if self._forms[resource_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('resource_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('resource_form did not originate from this session')
        if not resource_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(resource_form._my_map)

        self._forms[resource_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Resource(
            osid_object_map=resource_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_resources(self):
        """Tests if this user can delete ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Resource`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_resource(self, resource_id):
        """Deletes a ``Resource``.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to remove
        raise:  NotFound - ``resource_id`` not found
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        if not isinstance(resource_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        resource_map = collection.find_one(
            dict({'_id': ObjectId(resource_id.get_identifier())},
                 **self._view_filter()))

        objects.Resource(osid_object_map=resource_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(resource_id.get_identifier())})

    def can_manage_resource_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Resource`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_resource(self, resource_id, alias_id):
        """Adds an ``Id`` to a ``Resource`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Resource`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another resource it is
        reassigned to the given resource ``Id``.

        arg:    resource_id (osid.id.Id): the ``Id`` of a ``Resource``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``resource_id`` not found
        raise:  NullArgument - ``alias_id`` or ``resource_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=resource_id, equivalent_id=alias_id)


class ResourceNotificationSession(abc_resource_sessions.ResourceNotificationSession, osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Resource`` objects in this ``Bin``.

    This also includes existing resources that may appear or disappear
    due to changes in the ``Bin`` hierarchy, This session is intended
    for consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.

    The two views defined in this session correspond to the views in the
    ``ResourceLookupSession``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bin
        self._catalog_name = 'Bin'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='resource',
            cat_name='Bin',
            cat_class=objects.Bin)

        if not MONGO_LISTENER.is_alive():
            MONGO_LISTENER.initialize(runtime)
            MONGO_LISTENER.start()

        self._receiver = kwargs['receiver']
        db_prefix = ''
        try:
            db_prefix_param_id = Id('parameter:mongoDBNamePrefix@mongo')
            db_prefix = runtime.get_configuration().get_value_by_parameter(db_prefix_param_id).get_string_value()
        except (AttributeError, KeyError, errors.NotFound):
            pass
        self._ns = '{0}resource.Resource'.format(db_prefix)

        if self._ns not in MONGO_LISTENER.receivers:
            MONGO_LISTENER.receivers[self._ns] = dict()
        MONGO_LISTENER.receivers[self._ns][self._receiver] = {
            'authority': self._authority,
            'obj_name_plural': 'resources',
            'i': False,
            'u': False,
            'd': False,
            'reliable': False,
        }

    def __del__(self):
        """Make sure the receiver is removed from the listener"""
        del MONGO_LISTENER.receivers[self._ns][self._receiver]
        super(ResourceNotificationSession, self).__del__()

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bin = property(fget=get_bin)

    def can_register_for_resource_notifications(self):
        """Tests if this user can register for ``Resource`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this bin only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def register_for_new_resources(self):
        """Register for notifications of new resources.

        ``ResourceReceiver.newResources()`` is invoked when a new
        ``Resource`` is appears in this bin.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        MONGO_LISTENER.receivers[self._ns][self._receiver]['i'] = True

    def register_for_changed_resources(self):
        """Registers for notification of updated resources.

        ``ResourceReceiver.changedResources()`` is invoked when a
        resource in this bin is changed.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        MONGO_LISTENER.receivers[self._ns][self._receiver]['u'] = True

    @utilities.arguments_not_none
    def register_for_changed_resource(self, resource_id):
        """Registers for notification of an updated resource.

        ``ResourceReceiver.changedResources()`` is invoked when the
        specified resource in this bin is changed.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to monitor
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not MONGO_LISTENER.receivers[self._ns][self._receiver]['u']:
            MONGO_LISTENER.receivers[self._ns][self._receiver]['u'] = []
        if isinstance(MONGO_LISTENER.receivers[self._ns][self._receiver]['u'], list):
            MONGO_LISTENER.receivers[self._ns][self._receiver]['u'].append(resource_id.get_identifier())

    def register_for_deleted_resources(self):
        """Registers for notification of deleted resources.

        ``ResourceReceiver.deletedResources()`` is invoked when a
        resource is deleted or removed from this bin.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        MONGO_LISTENER.receivers[self._ns][self._receiver]['d'] = True

    @utilities.arguments_not_none
    def register_for_deleted_resource(self, resource_id):
        """Registers for notification of a deleted resource.

        ``ResourceReceiver.deletedResources()`` is invoked when the
        specified resource is deleted or removed from this bin.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to monitor
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not MONGO_LISTENER.receivers[self._ns][self._receiver]['d']:
            MONGO_LISTENER.receivers[self._ns][self._receiver]['d'] = []
        if isinstance(MONGO_LISTENER.receivers[self._ns][self._receiver]['d'], list):
            MONGO_LISTENER.receivers[self._ns][self._receiver]['d'].append(resource_id.get_identifier())

    def reliable_resource_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.reliable_resource_notifications
        MONGO_LISTENER.receivers[self._ns][self._receiver]['reliable'] = True

    def unreliable_resource_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceNotificationSession.unreliable_resource_notifications
        MONGO_LISTENER.receivers[self._ns][self._receiver]['reliable'] = False

    @utilities.arguments_not_none
    def acknowledge_resource_notification(self, notification_id):
        """Acknowledge an resource notification.

        arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ResourceBinSession(abc_resource_sessions.ResourceBinSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Resource`` to ``Bin`` mappings.

    A ``Resource`` may appear in multiple ``Bins``. Each ``Bin`` may
    have its own authorizations governing who is allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'resource.ResourceBinSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def use_comparative_bin_view(self):
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

    def use_plenary_bin_view(self):
        """A complete view of the ``Resource`` and ``Bin`` returns is desired.

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

    def can_lookup_resource_bin_mappings(self):
        """Tests if this user can perform lookups of resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_resource_ids_by_bin(self, bin_id):
        """Gets the list of ``Resource``  ``Ids`` associated with a ``Bin``.

        arg:    bin_id (osid.id.Id): ``Id`` of a ``Bin``
        return: (osid.id.IdList) - list of related resource ``Ids``
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for resource in self.get_resources_by_bin(bin_id):
            id_list.append(resource.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_resources_by_bin(self, bin_id):
        """Gets the list of ``Resources`` associated with a ``Bin``.

        arg:    bin_id (osid.id.Id): ``Id`` of a ``Bin``
        return: (osid.resource.ResourceList) - list of related resources
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('RESOURCE', local=True)
        lookup_session = mgr.get_resource_lookup_session_for_bin(bin_id, proxy=self._proxy)
        lookup_session.use_isolated_bin_view()
        return lookup_session.get_resources()

    @utilities.arguments_not_none
    def get_resource_ids_by_bins(self, bin_ids):
        """Gets the list of ``Resource Ids`` corresponding to a list of ``Bin`` objects.

        arg:    bin_ids (osid.id.IdList): list of bin ``Ids``
        return: (osid.id.IdList) - list of resource ``Ids``
        raise:  NullArgument - ``bin_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for resource in self.get_resources_by_bins(bin_ids):
            id_list.append(resource.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_resources_by_bins(self, bin_ids):
        """Gets the list of ``Resources`` corresponding to a list of ``Bins``.

        arg:    bin_ids (osid.id.IdList): list of bin ``Ids``
        return: (osid.resource.ResourceList) - list of resources
        raise:  NullArgument - ``bin_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        resource_list = []
        for bin_id in bin_ids:
            resource_list += list(
                self.get_resources_by_bin(bin_id))
        return objects.ResourceList(resource_list)

    @utilities.arguments_not_none
    def get_bin_ids_by_resource(self, resource_id):
        """Gets the list of ``Bin``  ``Ids`` mapped to a ``Resource``.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        return: (osid.id.IdList) - list of bin ``Ids``
        raise:  NotFound - ``resource_id`` is not found
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('RESOURCE', local=True)
        lookup_session = mgr.get_resource_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bin_view()
        resource = lookup_session.get_resource(resource_id)
        id_list = []
        for idstr in resource._my_map['assignedBinIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_bins_by_resource(self, resource_id):
        """Gets the list of ``Bin`` objects mapped to a ``Resource``.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        return: (osid.resource.BinList) - list of bins
        raise:  NotFound - ``resource_id`` is not found
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('RESOURCE', local=True)
        lookup_session = mgr.get_bin_lookup_session(proxy=self._proxy)
        return lookup_session.get_bins_by_ids(
            self.get_bin_ids_by_resource(resource_id))


class ResourceBinAssignmentSession(abc_resource_sessions.ResourceBinAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Resources`` to ``Bins``.

    A ``Resource`` may map to multiple ``Bin`` objects and removing the
    last reference to a ``Resource`` is the equivalent of deleting it.
    Each ``Bin`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of a ``Resource`` to another ``Bin`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'resource.ResourceBinAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Bin'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_resources(self):
        """Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_assign_resources_to_bin(self, bin_id):
        """Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``bin_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if bin_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_bin_ids(self, bin_id):
        """Gets a list of bins including and under the given bin node in which any resource can be assigned.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.id.IdList) - list of assignable bin ``Ids``
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('RESOURCE', local=True)
        lookup_session = mgr.get_bin_lookup_session(proxy=self._proxy)
        bins = lookup_session.get_bins()
        id_list = []
        for bin in bins:
            id_list.append(bin.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_bin_ids_for_resource(self, bin_id, resource_id):
        """Gets a list of bins including and under the given bin node in which a specific resource can be assigned.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        return: (osid.id.IdList) - list of assignable bin ``Ids``
        raise:  NullArgument - ``bin_id`` or ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_bin_ids(bin_id)

    @utilities.arguments_not_none
    def assign_resource_to_bin(self, resource_id, bin_id):
        """Adds an existing ``Resource`` to a ``Bin``.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        raise:  AlreadyExists - ``resource_id`` is already assigned to
                ``bin_id``
        raise:  NotFound - ``resource_id`` or ``bin_id`` not found
        raise:  NullArgument - ``resource_id`` or ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('RESOURCE', local=True)
        lookup_session = mgr.get_bin_lookup_session(proxy=self._proxy)
        lookup_session.get_bin(bin_id)  # to raise NotFound
        self._assign_object_to_catalog(resource_id, bin_id)

    @utilities.arguments_not_none
    def unassign_resource_from_bin(self, resource_id, bin_id):
        """Removes a ``Resource`` from a ``Bin``.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        raise:  NotFound - ``resource_id`` or ``bin_id`` not found or
                ``resource_id`` not assigned to ``bin_id``
        raise:  NullArgument - ``resource_id`` or ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('RESOURCE', local=True)
        lookup_session = mgr.get_bin_lookup_session(proxy=self._proxy)
        lookup_session.get_bin(bin_id)  # to raise NotFound
        self._unassign_object_from_catalog(resource_id, bin_id)


class ResourceAgentSession(abc_resource_sessions.ResourceAgentSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Resource`` to ``Agent`` mappings.

    An ``Agent`` may map to only one ``Resource`` while a ``Resource``
    may map to multiple ``Agents``.

    This lookup session defines several views

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'resource.ResourceAgentSession'

    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bin
        self._catalog_name = 'Bin'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='resource',
            cat_name='Bin',
            cat_class=objects.Bin)
        self._forms = dict()

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bin = property(fget=get_bin)

    def can_lookup_resource_agent_mappings(self):
        """Tests if this user can perform lookups of resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_resource_id_by_agent(self, agent_id):
        """Gets the ``Resource``  ``Id`` associated with the given agent.

        arg:    agent_id (osid.id.Id): ``Id`` of the ``Agent``
        return: (osid.id.Id) - associated resource
        raise:  NotFound - ``agent_id`` is not found
        raise:  NullArgument - ``agent_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_resource_by_agent(agent_id).get_id()

    @utilities.arguments_not_none
    def get_resource_by_agent(self, agent_id):
        """Gets the ``Resource`` associated with the given agent.

        arg:    agent_id (osid.id.Id): ``Id`` of the ``Agent``
        return: (osid.resource.Resource) - associated resource
        raise:  NotFound - ``agent_id`` is not found
        raise:  NullArgument - ``agent_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'agentIds': {'$in': [str(agent_id)]}},
                 **self._view_filter()))
        return objects.Resource(
            osid_object_map=result,
            runtime=self._runtime,
            proxy=self._proxy)

    @utilities.arguments_not_none
    def get_agent_ids_by_resource(self, resource_id):
        """Gets the list of ``Agent``  ``Ids`` mapped to a ``Resource``.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        return: (osid.id.IdList) - list of agent ``Ids``
        raise:  NotFound - ``resource_id`` is not found
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        resource = collection.find_one(
            dict({'_id': ObjectId(resource_id.get_identifier())},
                 **self._view_filter()))
        if 'agentIds' not in resource:
            result = IdList([])
        else:
            result = IdList(resource['agentIds'])
        return result

    @utilities.arguments_not_none
    def get_agents_by_resource(self, resource_id):
        """Gets the list of ``Agents`` mapped to a ``Resource``.

        arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        return: (osid.authentication.AgentList) - list of agents
        raise:  NotFound - ``resource_id`` is not found
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        agent_list = []
        for agent_id in self.get_agent_ids_by_resource(resource_id):
            agent_list.append(Agent(agent_id))
        return AgentList(agent_list)


class ResourceAgentAssignmentSession(abc_resource_sessions.ResourceAgentAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Resource`` to ``Agents``.

    A ``Resource`` may be associated with multiple ``Agents``. An
    ``Agent`` may map to only one ``Resource``.

    """
    _session_namespace = 'resource.ResourceAgentAssignmentSession'

    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bin
        self._catalog_name = 'Bin'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='resource',
            cat_name='Bin',
            cat_class=objects.Bin)
        self._forms = dict()

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bin = property(fget=get_bin)

    def can_assign_agents(self):
        """Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def can_assign_agents_to_resource(self, resource_id):
        """Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def assign_agent_to_resource(self, agent_id, resource_id):
        """Adds an existing ``Agent`` to a ``Resource``.

        arg:    agent_id (osid.id.Id): the ``Id`` of the ``Agent``
        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        raise:  AlreadyExists - ``agent_id`` is already assigned to
                ``resource_id``
        raise:  NotFound - ``agent_id`` or ``resource_id`` not found
        raise:  NullArgument - ``agent_id`` or ``resource_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Should check for existence of Agent? We may mever manage them.
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        resource = collection.find_one({'_id': ObjectId(resource_id.get_identifier())})

        try:
            ResourceAgentSession(
                self._catalog_id, self._proxy, self._runtime).get_resource_by_agent(agent_id)
        except errors.NotFound:
            pass
        else:
            raise errors.AlreadyExists()
        if 'agentIds' not in resource:
            resource['agentIds'] = [str(agent_id)]
        else:
            resource['agentIds'].append(str(agent_id))
        collection.save(resource)

    @utilities.arguments_not_none
    def unassign_agent_from_resource(self, agent_id, resource_id):
        """Removes an ``Agent`` from a ``Resource``.

        arg:    agent_id (osid.id.Id): the ``Id`` of the ``Agent``
        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        raise:  NotFound - ``agent_id`` or ``resource_id`` not found or
                ``agent_id`` not assigned to ``resource_id``
        raise:  NullArgument - ``agent_id`` or ``resource_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('resource',
                                         collection='Resource',
                                         runtime=self._runtime)
        resource = collection.find_one({'_id': ObjectId(resource_id.get_identifier())})

        try:
            resource['agentIds'].remove(str(agent_id))
        except (KeyError, ValueError):
            raise errors.NotFound('agent_id not assigned to resource')
        collection.save(resource)


class BinLookupSession(abc_resource_sessions.BinLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Bin`` objects.

    The ``Bin`` represents a collection resources.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Bins`` it can access, without breaking execution.
    However, an administrative application may require all ``Bin``
    elements to be available.

    Bins may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Bin``.

    """
    _session_namespace = 'resource.BinLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_bins(self):
        """Tests if this user can perform ``Bin`` lookups.

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

    def use_comparative_bin_view(self):
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

    def use_plenary_bin_view(self):
        """A complete view of the ``Bin`` returns is desired.

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
    def get_bin(self, bin_id):
        """Gets the ``Bin`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bin`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bin`` and retained for compatibility.

        arg:    bin_id (osid.id.Id): ``Id`` of the ``Bin``
        return: (osid.resource.Bin) - the bin
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=bin_id)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if bin_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.Bin, cat_name='Bin')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(bin_id, 'resource').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Bin.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(bin_id, 'resource', 'Bin')

        return objects.Bin(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_bins_by_ids(self, bin_ids):
        """Gets a ``BinList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the bins
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bins`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    bin_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.resource.BinList) - the returned ``Bin list``
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``bin_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Bin() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=bin_ids)
        catalog_id_list = []
        for i in bin_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.BinList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_bins_by_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        arg:    bin_genus_type (osid.type.Type): a bin genus type
        return: (osid.resource.BinList) - the returned ``Bin list``
        raise:  NullArgument - ``bin_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=bin_genus_type)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(bin_genus_type)}).sort('_id', DESCENDING)

        return objects.BinList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_bins_by_parent_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        arg:    bin_genus_type (osid.type.Type): a bin genus type
        return: (osid.resource.BinList) - the returned ``Bin list``
        raise:  NullArgument - ``bin_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_bins_by_record_type(self, bin_record_type):
        """Gets a ``BinList`` containing the given bin record ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        arg:    bin_record_type (osid.type.Type): a bin record type
        return: (osid.resource.BinList) - the returned ``Bin list``
        raise:  NullArgument - ``bin_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_bins_by_provider(self, resource_id):
        """Gets a ``BinList`` from the given provider.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.resource.BinList) - the returned ``Bin list``
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_bins(self):
        """Gets all ``Bins``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        return: (osid.resource.BinList) - a list of ``Bins``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.BinList(result, runtime=self._runtime, proxy=self._proxy)

    bins = property(fget=get_bins)


class BinQuerySession(abc_resource_sessions.BinQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Bin`` objects.

    The search query is constructed using the ``BinQuery``.

    Bins may have a bin query record indicated by their respective
    record types. The bin query record is accessed via the ``BinQuery``.

    """
    _session_namespace = 'resource.BinQuerySession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_query_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_search_bins(self):
        """Tests if this user can perform ``Bin`` searches.

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

    def get_bin_query(self):
        """Gets a bin query.

        The returned query will not have an extension query.

        return: (osid.resource.BinQuery) - the bin query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.get_bin_query_template
        return queries.BinQuery(runtime=self._runtime)

    bin_query = property(fget=get_bin_query)

    @utilities.arguments_not_none
    def get_bins_by_query(self, bin_query):
        """Gets a list of ``Bins`` matching the given bin query.

        arg:    bin_query (osid.resource.BinQuery): the bin query
        return: (osid.resource.BinList) - the returned ``BinList``
        raise:  NullArgument - ``bin_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - a ``bin_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_query(bin_query)
        query_terms = dict(bin_query._query_terms)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        result = collection.find(query_terms).sort('_id', DESCENDING)

        return objects.BinList(result, runtime=self._runtime)


class BinAdminSession(abc_resource_sessions.BinAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Bins``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Bin,`` a ``BinForm`` is requested using
    ``get_bin_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BinForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BinForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BinForm`` corresponds
    to an attempted transaction.

    For updates, ``BinForms`` are requested to the ``Bin``  ``Id`` that
    is to be updated using ``getBinFormForUpdate()``. Similarly, the
    ``BinForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``BinForm``
    can only be used once for a successful update and cannot be reused.

    The delete operations delete ``Bins``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    _session_namespace = 'resource.BinAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_bins(self):
        """Tests if this user can create ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Bin`` creation is not
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
    def can_create_bin_with_record_types(self, bin_record_types):
        """Tests if this user can create a single ``Bin`` using the desired record types.

        While ``ResourceManager.getBinRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bin``.
        Providing an empty array tests if a ``Bin`` can be created with
        no records.

        arg:    bin_record_types (osid.type.Type[]): array of bin record
                types
        return: (boolean) - ``true`` if ``Bin`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``bin_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=bin_record_types)
        return True

    @utilities.arguments_not_none
    def get_bin_form_for_create(self, bin_record_types):
        """Gets the bin form for creating new bins.

        arg:    bin_record_types (osid.type.Type[]): array of bin record
                types
        return: (osid.resource.BinForm) - the bin form
        raise:  NullArgument - ``bin_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=bin_record_types)
        for arg in bin_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if bin_record_types == []:
            result = objects.BinForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.BinForm(
                record_types=bin_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_bin(self, bin_form):
        """Creates a new ``Bin``.

        arg:    bin_form (osid.resource.BinForm): the form for this
                ``Bin``
        return: (osid.resource.Bin) - the new ``Bin``
        raise:  IllegalState - ``bin_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``bin_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``bin_form`` did not originate from
                ``get_bin_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=bin_form)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        if not isinstance(bin_form, ABCBinForm):
            raise errors.InvalidArgument('argument type is not an BinForm')
        if bin_form.is_for_update():
            raise errors.InvalidArgument('the BinForm is for update only, not create')
        try:
            if self._forms[bin_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('bin_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('bin_form did not originate from this session')
        if not bin_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(bin_form._my_map)

        self._forms[bin_form.get_id().get_identifier()] = CREATED
        result = objects.Bin(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_bins(self):
        """Tests if this user can update ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Bin`` modification is not
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
    def get_bin_form_for_update(self, bin_id):
        """Gets the bin form for updating an existing bin.

        A new bin form should be requested for each update transaction.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        return: (osid.resource.BinForm) - the bin form
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=bin_id)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        if not isinstance(bin_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(bin_id.get_identifier())})

        cat_form = objects.BinForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_bin(self, bin_form):
        """Updates an existing bin.

        arg:    bin_form (osid.resource.BinForm): the form containing
                the elements to be updated
        raise:  IllegalState - ``bin_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``bin_id`` or ``bin_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``bin_form`` did not originate from
                ``get_bin_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=bin_form)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        if not isinstance(bin_form, ABCBinForm):
            raise errors.InvalidArgument('argument type is not an BinForm')
        if not bin_form.is_for_update():
            raise errors.InvalidArgument('the BinForm is for update only, not create')
        try:
            if self._forms[bin_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('bin_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('bin_form did not originate from this session')
        if not bin_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(bin_form._my_map)  # save is deprecated - change to replace_one

        self._forms[bin_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Bin(osid_object_map=bin_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_bins(self):
        """Tests if this user can delete ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        return: (boolean) - ``false`` if ``Bin`` deletion is not
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
    def delete_bin(self, bin_id):
        """Deletes a ``Bin``.

        arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin`` to remove
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=bin_id)
        collection = JSONClientValidated('resource',
                                         collection='Bin',
                                         runtime=self._runtime)
        if not isinstance(bin_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['Resource', 'ResourceRelationship', 'Bin']:
            obj_collection = JSONClientValidated('resource',
                                                 collection=object_catalog,
                                                 runtime=self._runtime)
            if obj_collection.find({'assignedBinIds': {'$in': [str(bin_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(bin_id.get_identifier())})

    def can_manage_bin_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Bin`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_bin(self, bin_id, alias_id):
        """Adds an ``Id`` to a ``Bin`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bin`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another bin, it is reassigned to the
        given bin ``Id``.

        arg:    bin_id (osid.id.Id): the ``Id`` of a ``Bin``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=bin_id, alias_id=alias_id)
        self._alias_id(primary_id=bin_id, equivalent_id=alias_id)


class BinHierarchySession(abc_resource_sessions.BinHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Bin`` objects.

    Each node in the hierarchy is a unique ``Bin``. The hierarchy may be
    traversed recursively to establish the tree structure through
    ``get_parent_bins()`` and ``getChildBins()``. To relate these
    ``Ids`` to another OSID, ``get_bin_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Bin`` available in the Resource OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_bins()`` or ``get_child_bins()`` in lieu of
    a ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: bin elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    _session_namespace = 'resource.BinHierarchySession'

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
                Id(authority='RESOURCE',
                   namespace='CATALOG',
                   identifier='BIN'),
                proxy=self._proxy)

    def get_bin_hierarchy_id(self):
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

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
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

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

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

    def use_comparative_bin_view(self):
        """The returns from the bin methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_bin_view(self):
        """A complete view of the ``Bin`` returns is desired.

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

    def get_root_bin_ids(self):
        """Gets the root bin ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root bin ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalog_ids()
        return self._hierarchy_session.get_roots()

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        """Gets the root bins in the bin hierarchy.

        A node with no parents is an orphan. While all bin ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        return: (osid.resource.BinList) - the root bins
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalogs()
        return BinLookupSession(
            self._proxy,
            self._runtime).get_bins_by_ids(list(self.get_root_bin_ids()))

    root_bins = property(fget=get_root_bins)

    @utilities.arguments_not_none
    def has_parent_bins(self, bin_id):
        """Tests if the ``Bin`` has any parents.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (boolean) - ``true`` if the bin has parents, ``false``
                otherwise
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_parent_catalogs(catalog_id=bin_id)
        return self._hierarchy_session.has_parents(id_=bin_id)

    @utilities.arguments_not_none
    def is_parent_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a direct parent of a bin.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``bin_id,``  ``false`` otherwise
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``id`` or ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_parent_of_catalog(id_=id_, catalog_id=bin_id)
        return self._hierarchy_session.is_parent(id_=bin_id, parent_id=id_)

    @utilities.arguments_not_none
    def get_parent_bin_ids(self, bin_id):
        """Gets the parent ``Ids`` of the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (osid.id.IdList) - the parent ``Ids`` of the bin
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalog_ids(catalog_id=bin_id)
        return self._hierarchy_session.get_parents(id_=bin_id)

    @utilities.arguments_not_none
    def get_parent_bins(self, bin_id):
        """Gets the parents of the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` to query
        return: (osid.resource.BinList) - the parents of the bin
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalogs(catalog_id=bin_id)
        return BinLookupSession(
            self._proxy,
            self._runtime).get_bins_by_ids(
                list(self.get_parent_bin_ids(bin_id)))

    @utilities.arguments_not_none
    def is_ancestor_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is an ancestor of a bin.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``bin_id,``  ``false`` otherwise
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``id`` or ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_ancestor_of_catalog(id_=id_, catalog_id=bin_id)
        return self._hierarchy_session.is_ancestor(id_=id_, ancestor_id=bin_id)

    @utilities.arguments_not_none
    def has_child_bins(self, bin_id):
        """Tests if a bin has any children.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (boolean) - ``true`` if the ``bin_id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_child_catalogs(catalog_id=bin_id)
        return self._hierarchy_session.has_children(id_=bin_id)

    @utilities.arguments_not_none
    def is_child_of_bin(self, id_, bin_id):
        """Tests if a bin is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``bin_id,``  ``false`` otherwise
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``id`` or ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_child_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_child_of_catalog(id_=id_, catalog_id=bin_id)
        return self._hierarchy_session.is_child(id_=bin_id, child_id=id_)

    @utilities.arguments_not_none
    def get_child_bin_ids(self, bin_id):
        """Gets the child ``Ids`` of the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the bin
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalog_ids(catalog_id=bin_id)
        return self._hierarchy_session.get_children(id_=bin_id)

    @utilities.arguments_not_none
    def get_child_bins(self, bin_id):
        """Gets the children of the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` to query
        return: (osid.resource.BinList) - the children of the bin
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalogs(catalog_id=bin_id)
        return BinLookupSession(
            self._proxy,
            self._runtime).get_bins_by_ids(
                list(self.get_child_bin_ids(bin_id)))

    @utilities.arguments_not_none
    def is_descendant_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a descendant of a bin.

        arg:    id (osid.id.Id): an ``Id``
        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``bin_id,``  ``false`` otherwise
        raise:  NotFound - ``bin_id`` is not found
        raise:  NullArgument - ``id`` or ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_descendant_of_catalog(id_=id_, catalog_id=bin_id)
        return self._hierarchy_session.is_descendant(id_=id_, descendant_id=bin_id)

    @utilities.arguments_not_none
    def get_bin_node_ids(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a bin node
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_node_ids(
                catalog_id=bin_id,
                ancestor_levels=ancestor_levels,
                descendant_levels=descendant_levels,
                include_siblings=include_siblings)
        return self._hierarchy_session.get_nodes(
            id_=bin_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)

    @utilities.arguments_not_none
    def get_bin_nodes(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        arg:    bin_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.resource.BinNode) - a bin node
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_nodes
        return objects.BinNode(self.get_bin_node_ids(
            bin_id=bin_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)._my_map, runtime=self._runtime, proxy=self._proxy)


class BinHierarchyDesignSession(abc_resource_sessions.BinHierarchyDesignSession, osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Bin`` objects.

    Each node in the hierarchy is a unique ``Bin``.

    """
    _session_namespace = 'resource.BinHierarchyDesignSession'

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
                Id(authority='RESOURCE',
                   namespace='CATALOG',
                   identifier='BIN'),
                proxy=self._proxy)

    def get_bin_hierarchy_id(self):
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

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
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

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_modify_bin_hierarchy(self):
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
    def add_root_bin(self, bin_id):
        """Adds a root bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        raise:  AlreadyExists - ``bin_id`` is already in hierarchy
        raise:  NotFound - ``bin_id`` not found
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_root_catalog(catalog_id=bin_id)
        return self._hierarchy_session.add_root(id_=bin_id)

    @utilities.arguments_not_none
    def remove_root_bin(self, bin_id):
        """Removes a root bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        raise:  NotFound - ``bin_id`` not a root
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_root_catalog(catalog_id=bin_id)
        return self._hierarchy_session.remove_root(id_=bin_id)

    @utilities.arguments_not_none
    def add_child_bin(self, bin_id, child_id):
        """Adds a child to a bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``bin_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``bin_id`` or ``child_id`` not found
        raise:  NullArgument - ``bin_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_child_catalog(catalog_id=bin_id, child_id=child_id)
        return self._hierarchy_session.add_child(id_=bin_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_bin(self, bin_id, child_id):
        """Removes a child from a bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``bin_id`` not a parent of ``child_id``
        raise:  NullArgument - ``bin_id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalog(catalog_id=bin_id, child_id=child_id)
        return self._hierarchy_session.remove_child(id_=bin_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_bins(self, bin_id):
        """Removes all children from a bin.

        arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        raise:  NotFound - ``bin_id`` not in hierarchy
        raise:  NullArgument - ``bin_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalogs(catalog_id=bin_id)
        return self._hierarchy_session.remove_children(id_=bin_id)
