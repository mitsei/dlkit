"""JSON implementations of grading sessions."""

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
from ..primitives import DateTime
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from ..utilities import overlap
from .objects import GradebookColumnSummary
from dlkit.abstract_osid.grading import sessions as abc_grading_sessions
from dlkit.abstract_osid.grading.objects import GradeEntryForm as ABCGradeEntryForm
from dlkit.abstract_osid.grading.objects import GradeSystemForm as ABCGradeSystemForm
from dlkit.abstract_osid.grading.objects import GradebookColumnForm as ABCGradebookColumnForm
from dlkit.abstract_osid.grading.objects import GradebookForm as ABCGradebookForm
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
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


class GradeSystemLookupSession(abc_grading_sessions.GradeSystemLookupSession, osid_sessions.OsidSession):
    """The session defines methods for retrieving ``Grades`` and ``GradeSystems``.

    A Grade represents a qualified ranking defined in some grade system.

    Two views are defined in this session:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * federated gradebook view: lookups include grade systems from
        this gradebook and other gradebooks which are children of this
        gradebook in the gradebook hierarchy
      * isolated gradebook view: lookups include only those grade
        systems defined in this gradebook


    Grades and grade systems may have an additional records indicated by
    their respective record types. The record may not be accessed
    through a cast of the object.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``GradeSystem``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``GradeSystem Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` lookups.

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
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_grade_system_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_grade_system_view(self):
        """A complete view of the ``GradeSystem`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_grade_system(self, grade_system_id):
        """Gets the ``GradeSystem`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradeSystem`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradeSystem`` and retained
        for compatibility.

        arg:    grade_system_id (osid.id.Id): ``Id`` of the
                ``GradeSystem``
        return: (osid.grading.GradeSystem) - the grade system
        raise:  NotFound - ``grade_system_id`` not found
        raise:  NullArgument - ``grade_system_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(grade_system_id, 'grading').get_identifier())},
                 **self._view_filter()))
        return objects.GradeSystem(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_grade_system_by_grade(self, grade_id):
        """Gets the ``GradeSystem`` by a ``Grade``  ``Id``.

        arg:    grade_id (osid.id.Id): ``Id`` of a ``Grade``
        return: (osid.grading.GradeSystem) - the grade system
        raise:  NotFound - ``grade_id`` not found
        raise:  NullArgument - ``grade_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_grade_systems_by_ids(self, grade_system_ids):
        """Gets a ``GradeSystemList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the systems
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``GradeSystems`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        arg:    grade_system_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``grade_system_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        object_id_list = []
        for i in grade_system_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'grading').get_identifier()))
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
        return objects.GradeSystemList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_grade_systems_by_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` which does not include systems of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        arg:    grade_system_genus_type (osid.type.Type): a grade system
                genus type
        return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        raise:  NullArgument - ``grade_system_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(grade_system_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.GradeSystemList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_grade_systems_by_parent_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` and include any additional systems with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        arg:    grade_system_genus_type (osid.type.Type): a grade system
                genus type
        return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        raise:  NullArgument - ``grade_system_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.GradeSystemList([])

    @utilities.arguments_not_none
    def get_grade_systems_by_record_type(self, grade_system_record_type):
        """Gets a ``GradeSystemList`` containing the given grade record ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        arg:    grade_system_record_type (osid.type.Type): a grade
                system record type
        return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        raise:  NullArgument - ``grade_system_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.GradeSystemList([])

    def get_grade_systems(self):
        """Gets all ``GradeSystems``.

        In plenary mode, the returned list contains all known grade
        systems or an error results. Otherwise, the returned list may
        contain only those grade systems that are accessible through
        this session.

        return: (osid.grading.GradeSystemList) - a ``GradeSystemList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.GradeSystemList(result, runtime=self._runtime, proxy=self._proxy)

    grade_systems = property(fget=get_grade_systems)


class GradeSystemQuerySession(abc_grading_sessions.GradeSystemQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``GradeSystems``.

    The search query is constructed using the ``GradeSystemQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated gradebook view: searches include grade systems in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        systems in this gradebook


    Grade systems may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeSystemQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_search_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` searches.

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

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grades in gradebooks which are
        children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_grade_system_query(self):
        """Gets a grade system query.

        return: (osid.grading.GradeSystemQuery) - a grade system query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.GradeSystemQuery(runtime=self._runtime)

    grade_system_query = property(fget=get_grade_system_query)

    @utilities.arguments_not_none
    def get_grade_systems_by_query(self, grade_system_query):
        """Gets a list of ``GradeSystem`` objects matching the given grade system query.

        arg:    grade_system_query (osid.grading.GradeSystemQuery): the
                grade system query
        return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystemList``
        raise:  NullArgument - ``grade_system_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_system_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in grade_system_query._query_terms:
            if '$in' in grade_system_query._query_terms[term] and '$nin' in grade_system_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': grade_system_query._query_terms[term]['$in']}},
                             {term: {'$nin': grade_system_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: grade_system_query._query_terms[term]})
        for term in grade_system_query._keyword_terms:
            or_list.append({term: grade_system_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        result = collection.find(query_terms).sort('_id', DESCENDING)
        return objects.GradeSystemList(result, runtime=self._runtime, proxy=self._proxy)


class GradeSystemAdminSession(abc_grading_sessions.GradeSystemAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``GradeSystems``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``GradeSystem,`` a ``GradeSystemForm`` is requested using
    ``get_grade_system_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradeSystemForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``GradeSystemForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each
    ``GradeSystemForm`` corresponds to an attempted transaction.

    For updates, ``GradeSystemForms`` are requested to the
    ``GradeSystem``  ``Id`` that is to be updated using
    ``getGradeSystemFormForUpdate()``. Similarly, the
    ``GradeSystemForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``GradeSystemForm`` can only be used once for a successful update
    and cannot be reused.

    The delete operations delete ``GradeSystems`` To unmap a
    ``GradeSystem`` from the current ``Gradebook,`` the
    ``GradeSystemGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradeSystem`` itself thus
    removing it from all known ``Gradebook`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._forms = dict()
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_create_grade_systems(self):
        """Tests if this user can create ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``GradeSystem`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_grade_system_with_record_types(self, grade_system_record_types):
        """Tests if this user can create a single ``GradeSystem`` using the desired record types.

        While ``GradingManager.getGradeSystemRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeSystem``.
        Providing an empty array tests if a ``GradeSystem`` can be
        created with no records.

        arg:    grade_system_record_types (osid.type.Type[]): array of
                grade system types
        return: (boolean) - ``true`` if ``GradeSystem`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``grade_system_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_grade_system_form_for_create(self, grade_system_record_types):
        """Gets the grade system form for creating new grade systems.

        A new form should be requested for each create transaction.

        arg:    grade_system_record_types (osid.type.Type[]): array of
                grade system types
        return: (osid.grading.GradeSystemForm) - the grade system form
        raise:  NullArgument - ``grade_system_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in grade_system_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if grade_system_record_types == []:
            obj_form = objects.GradeSystemForm(
                gradebook_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.GradeSystemForm(
                gradebook_id=self._catalog_id,
                record_types=grade_system_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_grade_system(self, grade_system_form):
        """Creates a new ``GradeSystem``.

        arg:    grade_system_form (osid.grading.GradeSystemForm): the
                form for this ``GradeSystem``
        return: (osid.grading.GradeSystem) - the new ``GradeSystem``
        raise:  IllegalState - ``grade_system_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``grade_system_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_system_form`` did not originate
                from ``get_grade_system_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_system_form, ABCGradeSystemForm):
            raise errors.InvalidArgument('argument type is not an GradeSystemForm')
        if grade_system_form.is_for_update():
            raise errors.InvalidArgument('the GradeSystemForm is for update only, not create')
        try:
            if self._forms[grade_system_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('grade_system_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('grade_system_form did not originate from this session')
        if not grade_system_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(grade_system_form._my_map)

        self._forms[grade_system_form.get_id().get_identifier()] = CREATED
        result = objects.GradeSystem(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_grade_systems(self):
        """Tests if this user can update ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        return: (boolean) - ``false`` if ``GradeSystem`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_grade_system_form_for_update(self, grade_system_id):
        """Gets the grade system form for updating an existing grade system.

        A new grade system form should be requested for each update
        transaction.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of the
                ``GradeSystem``
        return: (osid.grading.GradeSystemForm) - the grade system form
        raise:  NotFound - ``grade_system_id`` is not found
        raise:  NullArgument - ``grade_system_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_system_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if grade_system_id.get_identifier_namespace() != 'grading.GradeSystem':
            if grade_system_id.get_authority() != self._authority:
                raise errors.InvalidArgument()
            else:
                grade_system_id = self._get_grade_system_id_with_enclosure(grade_system_id)
        result = collection.find_one({'_id': ObjectId(grade_system_id.get_identifier())})

        obj_form = objects.GradeSystemForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    def _get_grade_system_id_with_enclosure(self, enclosure_id):
        """Create an GradeSystem with an enclosed foreign object.

        return: (osid.id.Id) - the id of the new GradeSystem

        """
        mgr = self._get_provider_manager('GRADING')
        query_session = mgr.get_grade_system_query_session_for_gradebook(self._catalog_id, proxy=self._proxy)
        query_form = query_session.get_grade_system_query()
        query_form.match_enclosed_object_id(enclosure_id)
        query_result = query_session.get_grade_systems_by_query(query_form)
        if query_result.available() > 0:
            grade_system_id = query_result.next().get_id()
        else:
            create_form = self.get_grade_system_form_for_create([ENCLOSURE_RECORD_TYPE])
            create_form.set_enclosed_object(enclosure_id)
            grade_system_id = self.create_grade_system(create_form).get_id()
        return grade_system_id

    @utilities.arguments_not_none
    def duplicate_grade_system(self, grade_system_id):
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        mgr = self._get_provider_manager('GRADING')
        lookup_session = mgr.get_grade_system_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_gradebook_view()
        try:
            lookup_session.use_unsequestered_grade_system_view()
        except AttributeError:
            pass
        grade_system_map = dict(lookup_session.get_grade_system(grade_system_id)._my_map)
        del grade_system_map['_id']
        if 'gradebookId' in grade_system_map:
            grade_system_map['gradebookId'] = str(self._catalog_id)
        if 'assignedGradebookIds' in grade_system_map:
            grade_system_map['assignedGradebookIds'] = [str(self._catalog_id)]
        insert_result = collection.insert_one(grade_system_map)
        result = objects.GradeSystem(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)
        return result

    @utilities.arguments_not_none
    def update_grade_system(self, grade_system_form):
        """Updates an existing grade system.

        arg:    grade_system_form (osid.grading.GradeSystemForm): the
                form containing the elements to be updated
        raise:  IllegalState - ``grade_system_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``grade_system_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_system_form`` did not originate
                from ``get_grade_system_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_system_form, ABCGradeSystemForm):
            raise errors.InvalidArgument('argument type is not an GradeSystemForm')
        if not grade_system_form.is_for_update():
            raise errors.InvalidArgument('the GradeSystemForm is for update only, not create')
        try:
            if self._forms[grade_system_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('grade_system_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('grade_system_form did not originate from this session')
        if not grade_system_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(grade_system_form._my_map)

        self._forms[grade_system_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.GradeSystem(
            osid_object_map=grade_system_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_grade_systems(self):
        """Tests if this user can delete grade systems.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``GradeSystem`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_grade_system(self, grade_system_id):
        """Deletes a ``GradeSystem``.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of the
                ``GradeSystem`` to remove
        raise:  NotFound - ``grade_system_id`` not found
        raise:  NullArgument - ``grade_system_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_system_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        grade_system_map = collection.find_one({'_id': ObjectId(grade_system_id.get_identifier())})

        # check if has columns first
        if self._has_columns(grade_system_id):
            raise errors.InvalidArgument('Grade system being used by gradebook columns. ' +
                                         'Cannot delete it.')

        objects.GradeSystem(osid_object_map=grade_system_map,
                            runtime=self._runtime,
                            proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(grade_system_id.get_identifier())})

    def can_manage_grade_system_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradeSystem`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_grade_system(self, grade_system_id, alias_id):
        """Adds an ``Id`` to a ``GradeSystem`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradeSystem`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade system, it is
        reassigned to the given grade system ``Id``.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``grade_system_id`` not found
        raise:  NullArgument - ``grade_system_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=grade_system_id, equivalent_id=alias_id)

    @utilities.arguments_not_none
    def can_create_grades(self, grade_system_id):
        """Tests if this user can create ``Grade`` s for a ``GradeSystem``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        return: (boolean) - ``false`` if ``Grade`` creation is not
                authorized, ``true`` otherwise
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_grade_with_record_types(self, grade_system_id, grade_record_types):
        """Tests if this user can create a single ``Grade`` using the desired record types.

        While ``GradingManager.getGradeRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Grade``.
        Providing an empty array tests if a ``Grade`` can be created
        with no records.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        arg:    grade_record_types (osid.type.Type[]): array of grade
                recod types
        return: (boolean) - ``true`` if ``Grade`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``grade_system_id`` or
                ``grade_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_grade_form_for_create(self, grade_system_id, grade_record_types):
        """Gets the grade form for creating new grades.

        A new form should be requested for each create transaction.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        arg:    grade_record_types (osid.type.Type[]): array of grade
                recod types
        return: (osid.grading.GradeForm) - the grade form
        raise:  NotFound - ``grade_system_id`` is not found
        raise:  NullArgument - ``grade_system_id`` or
                ``grade_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template

        if not isinstance(grade_system_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in grade_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if grade_record_types == []:
            # WHY are we passing gradebook_id = self._catalog_id below, seems redundant:
            obj_form = objects.GradeForm(
                gradebook_id=self._catalog_id,
                grade_system_id=grade_system_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.GradeForm(
                gradebook_id=self._catalog_id,
                record_types=grade_record_types,
                grade_system_id=grade_system_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_grade(self, grade_form):
        """Creates a new ``Grade``.

        arg:    grade_form (osid.grading.GradeForm): the form for this
                ``Grade``
        return: (osid.grading.Grade) - the new ``Grade``
        raise:  IllegalState - ``grade_form`` already used in a create
                transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``grade_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_form`` did not originate from
                ``get_grade_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.create_asset_content_template
        from dlkit.abstract_osid.grading.objects import GradeForm as ABCGradeForm
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_form, ABCGradeForm):
            raise errors.InvalidArgument('argument type is not an GradeForm')
        if grade_form.is_for_update():
            raise errors.InvalidArgument('the GradeForm is for update only, not create')
        try:
            if self._forms[grade_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('grade_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('grade_form did not originate from this session')
        if not grade_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        grade_form._my_map['_id'] = ObjectId()
        grade_system_id = Id(grade_form._my_map['gradeSystemId']).get_identifier()
        grade_system = collection.find_one(
            {'$and': [{'_id': ObjectId(grade_system_id)},
                      {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]})
        grade_system['grades'].append(grade_form._my_map)
        result = collection.save(grade_system)

        self._forms[grade_form.get_id().get_identifier()] = CREATED
        from .objects import Grade
        return Grade(
            osid_object_map=grade_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    @utilities.arguments_not_none
    def can_update_grades(self, grade_system_id):
        """Tests if this user can update ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        return: (boolean) - ``false`` if ``Grade`` modification is not
                authorized, ``true`` otherwise
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_grade_form_for_update(self, grade_id):
        """Gets the grade form for updating an existing grade.

        A new grade form should be requested for each update
        transaction.

        arg:    grade_id (osid.id.Id): the ``Id`` of the ``Grade``
        return: (osid.grading.GradeForm) - the grade form
        raise:  NotFound - ``grade_id`` is not found
        raise:  NullArgument - ``grade_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        from .objects import GradeForm
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        document = collection.find_one({'grades._id': ObjectId(grade_id.get_identifier())})
        for sub_doc in document['grades']:  # There may be a MongoDB shortcut for this
            if sub_doc['_id'] == ObjectId(grade_id.get_identifier()):
                result = sub_doc
        obj_form = GradeForm(
            osid_object_map=result,
            runtime=self._runtime,
            proxy=self._proxy)
        obj_form._for_update = True
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED
        return obj_form

    @utilities.arguments_not_none
    def update_grade(self, grade_form):
        """Updates an existing grade.

        arg:    grade_form (osid.grading.GradeForm): the form containing
                the elements to be updated
        raise:  IllegalState - ``grade_form`` already used in an update
                transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``grade_id`` or ``grade_form`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_form`` did not originate from
                ``get_grade_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.update_asset_content_template
        from dlkit.abstract_osid.grading.objects import GradeForm as ABCGradeForm
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_form, ABCGradeForm):
            raise errors.InvalidArgument('argument type is not an GradeForm')
        if not grade_form.is_for_update():
            raise errors.InvalidArgument('the GradeForm is for update only, not create')
        try:
            if self._forms[grade_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('grade_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('grade_form did not originate from this session')
        if not grade_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        grade_system_id = Id(grade_form._my_map['grade_systemId']).get_identifier()
        grade_system = collection.find_one(
            {'$and': [{'_id': ObjectId(grade_system_id)},
                      {'assigned' + self._catalog_name + 'Ids': {'$in': [str(self._catalog_id)]}}]})
        index = 0
        found = False
        for i in grade_system['grades']:
            if i['_id'] == ObjectId(grade_form._my_map['_id']):
                grade_system['grades'].pop(index)
                grade_system['grades'].insert(index, grade_form._my_map)
                found = True
                break
            index += 1
        if not found:
            raise errors.NotFound()
        try:
            collection.save(grade_system)
        except:  # what exceptions does mongodb save raise?
            raise errors.OperationFailed()
        self._forms[grade_form.get_id().get_identifier()] = UPDATED
        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        from .objects import Grade

        return Grade(
            osid_object_map=grade_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    @utilities.arguments_not_none
    def can_delete_grades(self, grade_system_id):
        """Tests if this user can delete grades.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        return: (boolean) - ``false`` if ``Grade`` deletion is not
                authorized, ``true`` otherwise
        raise:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_grade(self, grade_id):
        """Deletes a ``Grade``.

        arg:    grade_id (osid.id.Id): the ``Id`` of the ``Grade`` to
                remove
        raise:  NotFound - ``grade_id`` not found
        raise:  NullArgument - ``grade_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetAdminSession.delete_asset_content_template
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        from .objects import Grade
        collection = JSONClientValidated('grading',
                                         collection='GradeSystem',
                                         runtime=self._runtime)
        if not isinstance(grade_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        grade_system = collection.find_one({'grades._id': ObjectId(grade_id.get_identifier())})

        index = 0
        found = False
        for i in grade_system['grades']:
            if i['_id'] == ObjectId(grade_id.get_identifier()):
                grade_map = grade_system['grades'].pop(index)
            index += 1
            found = True
        if not found:
            raise errors.OperationFailed()
        Grade(
            osid_object_map=grade_map,
            runtime=self._runtime,
            proxy=self._proxy)._delete()
        collection.save(grade_system)

    def can_manage_grade_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Grade`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_grade(self, grade_id, alias_id):
        """Adds an ``Id`` to a ``Grade`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Grade`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade, it is
        reassigned to the given grade ``Id``.

        arg:    grade_id (osid.id.Id): the ``Id`` of a ``Grade``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``grade_id`` not found
        raise:  NullArgument - ``grade_id`` or ``alias_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def _has_columns(self, grade_system_id):
        grading_manager = self._get_provider_manager('GRADING')
        gcqs = grading_manager.get_gradebook_column_query_session(proxy=self._proxy)
        gcqs.use_federated_gradebook_view()
        querier = gcqs.get_gradebook_column_query()
        querier.match_grade_system_id(grade_system_id, match=True)
        columns = gcqs.get_gradebook_columns_by_query(querier)
        return columns.available() > 0


class GradeEntryLookupSession(abc_grading_sessions.GradeEntryLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``GradeEntrie`` s."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` lookups.

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
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_grade_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_grade_entry_view(self):
        """A complete view of the ``GradeEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_effective_grade_entry_view(self):
        """Only grade entries whose effective dates are current are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_effective_relationship_view
        self._use_effective_view()

    def use_any_effective_grade_entry_view(self):
        """All grade entries of any effective dates are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_any_effective_relationship_view
        self._use_any_effective_view()

    @utilities.arguments_not_none
    def get_grade_entry(self, grade_entry_id):
        """Gets the ``GradeEntry`` specified by its ``Id``.

        arg:    grade_entry_id (osid.id.Id): ``Id`` of the
                ``GradeEntry``
        return: (osid.grading.GradeEntry) - the grade entry
        raise:  NotFound - ``grade_entry_id`` not found
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(grade_entry_id, 'grading').get_identifier())},
                 **self._view_filter()))
        return objects.GradeEntry(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_grade_entries_by_ids(self, grade_entry_ids):
        """Gets a ``GradeEntryList`` corresponding to the given ``IdList``.

        arg:    grade_entry_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``grade_entry_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        object_id_list = []
        for i in grade_entry_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'grading').get_identifier()))
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
        return objects.GradeEntryList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_grade_entries_by_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` which does not include grade entries of genus types derived from the specified ``Type``.

        arg:    grade_entry_genus_type (osid.type.Type): a grade entry
                genus type
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``grade_entry_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(grade_entry_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.GradeEntryList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_grade_entries_by_parent_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` and include any additional grade entry with genus types derived from the specified ``Type``.

        arg:    grade_entry_genus_type (osid.type.Type): a grade entry
                genus type
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``grade_entry_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.GradeEntryList([])

    @utilities.arguments_not_none
    def get_grade_entries_by_record_type(self, grade_entry_record_type):
        """Gets a ``GradeEntryList`` containing the given grade entry record ``Type``.

        arg:    grade_entry_record_type (osid.type.Type): a grade entry
                record type
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``grade_entry_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.GradeEntryList([])

    @utilities.arguments_not_none
    def get_grade_entries_on_date(self, from_, to):
        """Gets a ``GradeEntryList`` effective during the entire given date range inclusive but not confined to the date range.

        arg:    from (osid.calendaring.DateTime): start of date range
        arg:    to (osid.calendaring.DateTime): end of date range
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``from or to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_on_date
        grade_entry_list = []
        for grade_entry in self.get_grade_entries():
            if overlap(from_, to, grade_entry.start_date, grade_entry.end_date):
                grade_entry_list.append(grade_entry)
        return objects.GradeEntryList(grade_entry_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entries_for_gradebook_column(self, gradebook_column_id):
        """Gets a ``GradeEntryList`` for the gradebook column.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'gradebookColumnId': str(gradebook_column_id)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.GradeEntryList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entries_for_gradebook_column_on_date(self, gradebook_column_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column and effective during the entire given date range inclusive but not confined to the date range.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        arg:    from (osid.calendaring.DateTime): start of date range
        arg:    to (osid.calendaring.DateTime): end of date range
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``gradebook_column_id, from, or to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date
        grade_entry_list = []
        for grade_entry in self.get_grade_entries_for_gradebook_column(gradebook_column_id):
            if overlap(from_, to, grade_entry.start_date, grade_entry.end_date):
                grade_entry_list.append(grade_entry)
        return objects.GradeEntryList(grade_entry_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entries_for_resource(self, resource_id):
        """Gets a ``GradeEntryList`` for the given key key resource.

        arg:    resource_id (osid.id.Id): a key resource ``Id``
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_grade_entries_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given key resource and effective during the entire given date range inclusive but not confined to the date range.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    from (osid.calendaring.DateTime): start of date range
        arg:    to (osid.calendaring.DateTime): end of date range
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, from, or to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_grade_entries_for_gradebook_column_and_resource(self, gradebook_column_id, resource_id):
        """Gets a ``GradeEntryList`` for the gradebook column and key resource.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        arg:    resource_id (osid.id.Id): a key resource ``Id``
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``gradebook_column_id`` or
                ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'gradebookColumnId': str(gradebook_column_id),
                  'keyResourceId': str(resource_id)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.GradeEntryList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, gradebook_column_id, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column, resource, and effective during the entire given date range inclusive but not confined to the date range.

        arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        arg:    resource_id (osid.id.Id): a key resource ``Id``
        arg:    from (osid.calendaring.DateTime): start of date range
        arg:    to (osid.calendaring.DateTime): end of date range
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``gradebook_column_id, resource, from, or
                to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_grade_entries_by_grader(self, resource_id):
        """Gets a ``GradeEntryList`` for the given grader.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_grade_entries(self):
        """Gets all grade entries.

        return: (osid.grading.GradeEntryList) - a ``GradeEntryList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.GradeEntryList(result, runtime=self._runtime, proxy=self._proxy)

    grade_entries = property(fget=get_grade_entries)


class GradeEntryQuerySession(abc_grading_sessions.GradeEntryQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching ``GradeEntry`` objects.

    The search query is constructed using the ``GradeEntryQuery``. The
    grade entry record ``Type`` also specifies the record interface for
    the grade entry query.

    This session defines views that offer differing behaviors for
    searching.

      * federated gradebook view: searches include grade entries in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        entries in this gradebook


    Grade entries may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeEntryQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_search_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` searches.

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

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_grade_entry_query(self):
        """Gets a grade entry query.

        return: (osid.grading.GradeEntryQuery) - the grade entry query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.GradeEntryQuery(runtime=self._runtime)

    grade_entry_query = property(fget=get_grade_entry_query)

    @utilities.arguments_not_none
    def get_grade_entries_by_query(self, grade_entry_query):
        """Gets a list of entries matching the given grade entry query.

        arg:    grade_entry_query (osid.grading.GradeEntryQuery): the
                grade entry query
        return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntryList``
        raise:  NullArgument - ``grade_entry_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_entry_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in grade_entry_query._query_terms:
            if '$in' in grade_entry_query._query_terms[term] and '$nin' in grade_entry_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': grade_entry_query._query_terms[term]['$in']}},
                             {term: {'$nin': grade_entry_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: grade_entry_query._query_terms[term]})
        for term in grade_entry_query._keyword_terms:
            or_list.append({term: grade_entry_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        result = collection.find(query_terms).sort('_id', DESCENDING)
        return objects.GradeEntryList(result, runtime=self._runtime, proxy=self._proxy)


class GradeEntryAdminSession(abc_grading_sessions.GradeEntryAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``GradeEntries``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``GradeEntry,`` a ``GradeEntryForm`` is requested using
    ``get_grade_entry_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradeEntryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``GradeEntryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``GradeEntryForm``
    corresponds to an attempted transaction.

    For updates, ``GradeEntryForms`` are requested to the ``GradeEntry``
    ``Id`` that is to be updated using ``getGradeEntryFormForUpdate()``.
    Similarly, the ``GradeEntryForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``GradeEntryForm`` can only be used once for a
    successful update and cannot be reused.

    The delete operations delete ``GradeEntries``. To unmap a
    ``GradeEntry`` from the current ``Gradebook,`` the
    ``GradeEntryGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradeEntry`` itself thus
    removing it from all known ``Gradebook`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._forms = dict()
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_create_grade_entries(self):
        """Tests if this user can create grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradeEntry`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_grade_entry_with_record_types(self, grade_entry_record_types):
        """Tests if this user can create a single ``GradeEntry`` using the desired record types.

        While ``GradingManager.getGradeEntryRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeEntry``.
        Providing an empty array tests if a ``GradeEntry`` can be
        created with no records.

        arg:    grade_entry_record_types (osid.type.Type[]): array of
                grade entry record types
        return: (boolean) - ``true`` if ``GradeEntry`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``grade_entry_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_grade_entry_form_for_create(self, gradebook_column_id, resource_id, grade_entry_record_types):
        """Gets the grade entry form for creating new grade entries.

        A new form should be requested for each create transaction.

        arg:    gradebook_column_id (osid.id.Id): the gradebook column
        arg:    resource_id (osid.id.Id): the key resource
        arg:    grade_entry_record_types (osid.type.Type[]): array of
                grade entry record types
        return: (osid.grading.GradeEntryForm) - the grade entry form
        raise:  NotFound - ``gradebook_column_id or resource_id`` not
                found
        raise:  NullArgument - ``gradebook_column_id, resource_id,`` or
                ``grade_entry_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(gradebook_column_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(resource_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        # Add code for checking Id and getting gradebook_column enclosure
        for arg in grade_entry_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if grade_entry_record_types == []:
            # WHY are we passing gradebook_id = self._catalog_id below, seems redundant:
            # Probably don't need effective agent id since form can now get that from proxy.
            obj_form = objects.GradeEntryForm(
                gradebook_id=self._catalog_id,
                gradebook_column_id=gradebook_column_id,
                resource_id=resource_id,
                effective_agent_id=str(self.get_effective_agent_id()),
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.GradeEntryForm(
                gradebook_id=self._catalog_id,
                record_types=grade_entry_record_types,
                gradebook_column_id=gradebook_column_id,
                resource_id=resource_id,
                effective_agent_id=str(self.get_effective_agent_id()),
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_grade_entry(self, grade_entry_form):
        """Creates a new ``GradeEntry``.

        arg:    grade_entry_form (osid.grading.GradeEntryForm): the form
                for this ``GradeEntry``
        return: (osid.grading.GradeEntry) - the new ``GradeEntry``
        raise:  IllegalState - ``grade_entry_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``grade_entry_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_entry_form`` did not originate
                from ``get_grade_entry_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        if not isinstance(grade_entry_form, ABCGradeEntryForm):
            raise errors.InvalidArgument('argument type is not an GradeEntryForm')
        if grade_entry_form.is_for_update():
            raise errors.InvalidArgument('the GradeEntryForm is for update only, not create')
        try:
            if self._forms[grade_entry_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('grade_entry_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('grade_entry_form did not originate from this session')
        if not grade_entry_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(grade_entry_form._my_map)

        self._forms[grade_entry_form.get_id().get_identifier()] = CREATED
        result = objects.GradeEntry(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_overridecalculated_grade_entries(self):
        """Tests if this user can override grade entries calculated from another.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradeEntry`` override is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_grade_entry_form_for_override(self, grade_entry_id, grade_entry_record_types):
        """Gets the grade entry form for overriding calculated grade entries.

        A new form should be requested for each create transaction.

        arg:    grade_entry_id (osid.id.Id): the ``Id`` of the grade
                entry to be overridden
        arg:    grade_entry_record_types (osid.type.Type[]): array of
                grade entry record types
        return: (osid.grading.GradeEntryForm) - the grade entry form
        raise:  AlreadyExists - ``grade_entry_id`` is already overridden
        raise:  NotFound - ``grade_entry_id`` not found or
                ``grade_entry_id`` is not a calculated entry
        raise:  NullArgument - ``grade_entry_id`` or
                ``grade_entry_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def override_calculated_grade_entry(self, grade_entry_form):
        """Creates a new overriding ``GradeEntry``.

        arg:    grade_entry_form (osid.grading.GradeEntryForm): the form
                for this ``GradeEntry``
        return: (osid.grading.GradeEntry) - the new ``GradeEntry``
        raise:  IllegalState - ``grade_entry_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``grade_entry_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_entry_form`` did not originate
                from ``get_grade_entry_form_for_override()``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def can_update_grade_entries(self):
        """Tests if this user can update grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if grade entry modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_grade_entry_form_for_update(self, grade_entry_id):
        """Gets the grade entry form for updating an existing entry.

        A new grade entry form should be requested for each update
        transaction.

        arg:    grade_entry_id (osid.id.Id): the ``Id`` of the
                ``GradeEntry``
        return: (osid.grading.GradeEntryForm) - the grade entry form
        raise:  NotFound - ``grade_entry_id`` is not found
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        if not isinstance(grade_entry_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if grade_entry_id.get_identifier_namespace() != 'grading.GradeEntry':
            if grade_entry_id.get_authority() != self._authority:
                raise errors.InvalidArgument()
            else:
                grade_entry_id = self._get_grade_entry_id_with_enclosure(grade_entry_id)
        result = collection.find_one({'_id': ObjectId(grade_entry_id.get_identifier())})

        obj_form = objects.GradeEntryForm(
            osid_object_map=result,
            effective_agent_id=str(self.get_effective_agent_id()),
            runtime=self._runtime,
            proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_grade_entry(self, grade_entry_form):
        """Updates an existing grade entry.

        arg:    grade_entry_form (osid.grading.GradeEntryForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``grade_entry_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``grade_entry_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``grade_entry_form`` did not originate
                from ``get_grade_entry_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        if not isinstance(grade_entry_form, ABCGradeEntryForm):
            raise errors.InvalidArgument('argument type is not an GradeEntryForm')
        if not grade_entry_form.is_for_update():
            raise errors.InvalidArgument('the GradeEntryForm is for update only, not create')
        try:
            if self._forms[grade_entry_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('grade_entry_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('grade_entry_form did not originate from this session')
        if not grade_entry_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(grade_entry_form._my_map)

        self._forms[grade_entry_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.GradeEntry(
            osid_object_map=grade_entry_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_grade_entries(self):
        """Tests if this user can delete grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradeEntry`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_grade_entry(self, grade_entry_id):
        """Deletes the ``GradeEntry`` identified by the given ``Id``.

        arg:    grade_entry_id (osid.id.Id): the ``Id`` of the
                ``GradeEntry`` to delete
        raise:  NotFound - a ``GradeEntry`` was not found identified by
                the given ``Id``
        raise:  NullArgument - ``grade_entry_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('grading',
                                         collection='GradeEntry',
                                         runtime=self._runtime)
        if not isinstance(grade_entry_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        grade_entry_map = collection.find_one(
            dict({'_id': ObjectId(grade_entry_id.get_identifier())},
                 **self._view_filter()))

        objects.GradeEntry(osid_object_map=grade_entry_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(grade_entry_id.get_identifier())})

    def can_manage_grade_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeEntries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradeEntry`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_grade_entry(self, grade_entry_id, alias_id):
        """Adds an ``Id`` to a ``GradeEntry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradeEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade entry, it is
        reassigned to the given grade entry ``Id``.

        arg:    grade_entry_id (osid.id.Id): the ``Id`` of a
                ``GradeEntry``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``grade_entry_id`` not found
        raise:  NullArgument - ``grade_entry_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=grade_entry_id, equivalent_id=alias_id)


class GradebookColumnLookupSession(abc_grading_sessions.GradebookColumnLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``GradebookColumns``."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_lookup_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` lookups.

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

    def use_comparative_gradebook_column_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_gradebook_column_view(self):
        """A complete view of the ``GradebookColumn`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_gradebook_column(self, gradebook_column_id):
        """Gets the ``GradebookColumn`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradebookColumn`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradebookColumn`` and
        retained for compatibility.

        arg:    gradebook_column_id (osid.id.Id): ``Id`` of the
                ``GradebookColumn``
        return: (osid.grading.GradebookColumn) - the gradebook column
        raise:  NotFound - ``gradebook_column_id`` not found
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(gradebook_column_id, 'grading').get_identifier())},
                 **self._view_filter()))
        return objects.GradebookColumn(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_gradebook_columns_by_ids(self, gradebook_column_ids):
        """Gets a ``GradebookColumnList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the gradebook
        columns specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if a ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible gradeboook columns may be omitted from the list.

        arg:    gradebook_column_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``grade_book_column_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        object_id_list = []
        for i in gradebook_column_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'grading').get_identifier()))
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
        return objects.GradebookColumnList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_gradebook_columns_by_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` which does not include gradebook columns of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        arg:    gradebook_column_genus_type (osid.type.Type): a
                gradebook column genus type
        return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        raise:  NullArgument - ``gradebook_column_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(gradebook_column_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.GradebookColumnList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_gradebook_columns_by_parent_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` and include any additional columns with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        arg:    gradebook_column_genus_type (osid.type.Type): a
                gradebook column genus type
        return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        raise:  NullArgument - ``gradebook_column_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.GradebookColumnList([])

    @utilities.arguments_not_none
    def get_gradebook_columns_by_record_type(self, gradebook_column_record_type):
        """Gets a ``GradebookColumnList`` containing the given gradebook column record ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        arg:    gradebook_column_record_type (osid.type.Type): a
                gradebook column record type
        return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        raise:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.GradebookColumnList([])

    def get_gradebook_columns(self):
        """Gets all gradebook columns.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        return: (osid.grading.GradebookColumnList) - a
                ``GradebookColumn``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.GradebookColumnList(result, runtime=self._runtime, proxy=self._proxy)

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        """Tests if a summary entry is available.

        return: (boolean) - ``true`` if a summary entry is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Not yet:
        return False

    @utilities.arguments_not_none
    def get_gradebook_column_summary(self, gradebook_column_id):
        """Gets the ``GradebookColumnSummary`` for summary results.

        arg:    gradebook_column_id (osid.id.Id): ``Id`` of the
                ``GradebookColumn``
        return: (osid.grading.GradebookColumnSummary) - the gradebook
                column summary
        raise:  NotFound - ``gradebook_column_id`` is not found
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unimplemented - ``has_summary()`` is ``false``
        *compliance: mandatory -- This method is must be implemented.*

        """
        gradebook_column = self.get_gradebook_column(gradebook_column_id)
        summary_map = gradebook_column._my_map
        summary_map['gradebookColumnId'] = str(gradebook_column.ident)
        return GradebookColumnSummary(osid_object_map=summary_map,
                                      runtime=self._runtime,
                                      proxy=self._proxy)


class GradebookColumnQuerySession(abc_grading_sessions.GradebookColumnQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching ``GradebookColumn`` objects.

    The search query is constructed using the ``GradebookColumnQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated gradebook view: searches include columns in gradebooks
        of which this gradebook is a ancestor in the gradebook hierarchy
      * isolated gradebook view: searches are restricted to columns in
        this gradebook


    Gradebook columns may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``GradebookColumnQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_search_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` searches.

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

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_gradebook_column_query(self):
        """Gets a gradebook column query.

        return: (osid.grading.GradebookColumnQuery) - the gradebook
                column
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.GradebookColumnQuery(runtime=self._runtime)

    gradebook_column_query = property(fget=get_gradebook_column_query)

    @utilities.arguments_not_none
    def get_gradebook_columns_by_query(self, gradebook_column_query):
        """Gets a list of gradebook columns matching the given query.

        arg:    gradebook_column_query
                (osid.grading.GradebookColumnQuery): the gradebook
                column query
        return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumnList``
        raise:  NullArgument - ``gradebook_column_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``gradebook_column_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in gradebook_column_query._query_terms:
            if '$in' in gradebook_column_query._query_terms[term] and '$nin' in gradebook_column_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': gradebook_column_query._query_terms[term]['$in']}},
                             {term: {'$nin': gradebook_column_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: gradebook_column_query._query_terms[term]})
        for term in gradebook_column_query._keyword_terms:
            or_list.append({term: gradebook_column_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        result = collection.find(query_terms).sort('_id', DESCENDING)
        return objects.GradebookColumnList(result, runtime=self._runtime, proxy=self._proxy)


class GradebookColumnAdminSession(abc_grading_sessions.GradebookColumnAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``GradebookColumns``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``GradebookColumn,`` a ``GradebookColumnForm`` is requested using
    ``get_gradebook_column_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``GradebookColumnForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``GradebookColumnForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``GradebookColumnForm`` corresponds to an attempted transaction.

    For updates, ``GradebookColumnForms`` are requested to the
    ``GradebookColumn``  ``Id`` that is to be updated using
    ``getGradebookColumnFormForUpdate()``. Similarly, the
    ``GradebookColumnForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``GradebookColumnForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``GradebookColumns`` To unmap a
    ``GradebookColumn`` from the current ``Gradebook,`` the
    ``GradebookColumnGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradebookColumnForm``
    itself thus removing it from all known ``Gradebook`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Gradebook
        self._catalog_name = 'Gradebook'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='grading',
            cat_name='Gradebook',
            cat_class=objects.Gradebook)
        self._forms = dict()
        self._kwargs = kwargs

    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    gradebook = property(fget=get_gradebook)

    def can_create_gradebook_columns(self):
        """Tests if this user can create gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a gradebook
        column will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradebookColumn`` creation is
                not authorized, ``true`` otherwise
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
    def can_create_gradebook_column_with_record_types(self, gradebook_column_record_types):
        """Tests if this user can create a single ``GradebookColumn`` using the desired record types.

        While ``GradingManager.getGradebookColumnRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``GradebookColumn``. Providing an empty array tests if a
        ``GradebookColumn`` can be created with no records.

        arg:    gradebook_column_record_types (osid.type.Type[]): array
                of gradebook column record types
        return: (boolean) - ``true`` if ``GradebookColumn`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``gradebook_column_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs_with_record_types(catalog_record_types=gradebook_column_record_types)
        return True

    @utilities.arguments_not_none
    def get_gradebook_column_form_for_create(self, gradebook_column_record_types):
        """Gets the gradebook column form for creating new gradebook columns.

        A new form should be requested for each create transaction.

        arg:    gradebook_column_record_types (osid.type.Type[]): array
                of gradebook column record types
        return: (osid.grading.GradebookColumnForm) - the gradebook
                column form
        raise:  NullArgument - ``gradebook_column_record_types`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in gradebook_column_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if gradebook_column_record_types == []:
            obj_form = objects.GradebookColumnForm(
                gradebook_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.GradebookColumnForm(
                gradebook_id=self._catalog_id,
                record_types=gradebook_column_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_gradebook_column(self, gradebook_column_form):
        """Creates a new ``GradebookColumn``.

        arg:    gradebook_column_form
                (osid.grading.GradebookColumnForm): the form for this
                ``GradebookColumn``
        return: (osid.grading.GradebookColumn) - the new
                ``GradebookColumn``
        raise:  IllegalState - ``gradebook_column_form`` already used in
                a create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``gradebook_column_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``gradebook_column_form`` did not
                originate from
                ``get_gradebook_column_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        if not isinstance(gradebook_column_form, ABCGradebookColumnForm):
            raise errors.InvalidArgument('argument type is not an GradebookColumnForm')
        if gradebook_column_form.is_for_update():
            raise errors.InvalidArgument('the GradebookColumnForm is for update only, not create')
        try:
            if self._forms[gradebook_column_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('gradebook_column_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('gradebook_column_form did not originate from this session')
        if not gradebook_column_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(gradebook_column_form._my_map)

        self._forms[gradebook_column_form.get_id().get_identifier()] = CREATED
        result = objects.GradebookColumn(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_gradebook_columns(self):
        """Tests if this user can update gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        return: (boolean) - ``false`` if gradebook column modification
                is not authorized, ``true`` otherwise
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
    def get_gradebook_column_form_for_update(self, gradebook_column_id):
        """Gets the gradebook column form for updating an existing gradebook column.

        A new gradebook column form should be requested for each update
        transaction.

        arg:    gradebook_column_id (osid.id.Id): the ``Id`` of the
                ``GradebookColumn``
        return: (osid.grading.GradebookColumnForm) - the gradebook
                column form
        raise:  NotFound - ``gradebook_column_id`` is not found
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        if not isinstance(gradebook_column_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if gradebook_column_id.get_identifier_namespace() != 'grading.GradebookColumn':
            if gradebook_column_id.get_authority() != self._authority:
                raise errors.InvalidArgument()
            else:
                gradebook_column_id = self._get_gradebook_column_id_with_enclosure(gradebook_column_id)
        result = collection.find_one({'_id': ObjectId(gradebook_column_id.get_identifier())})

        obj_form = objects.GradebookColumnForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    def _get_gradebook_column_id_with_enclosure(self, enclosure_id):
        """Create an GradebookColumn with an enclosed foreign object.

        return: (osid.id.Id) - the id of the new GradebookColumn

        """
        mgr = self._get_provider_manager('GRADING')
        query_session = mgr.get_gradebook_column_query_session_for_gradebook(self._catalog_id, proxy=self._proxy)
        query_form = query_session.get_gradebook_column_query()
        query_form.match_enclosed_object_id(enclosure_id)
        query_result = query_session.get_gradebook_columns_by_query(query_form)
        if query_result.available() > 0:
            gradebook_column_id = query_result.next().get_id()
        else:
            create_form = self.get_gradebook_column_form_for_create([ENCLOSURE_RECORD_TYPE])
            create_form.set_enclosed_object(enclosure_id)
            gradebook_column_id = self.create_gradebook_column(create_form).get_id()
        return gradebook_column_id

    @utilities.arguments_not_none
    def duplicate_gradebook_column(self, gradebook_column_id):
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        mgr = self._get_provider_manager('GRADING')
        lookup_session = mgr.get_gradebook_column_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_gradebook_view()
        try:
            lookup_session.use_unsequestered_gradebook_column_view()
        except AttributeError:
            pass
        gradebook_column_map = dict(lookup_session.get_gradebook_column(gradebook_column_id)._my_map)
        del gradebook_column_map['_id']
        if 'gradebookId' in gradebook_column_map:
            gradebook_column_map['gradebookId'] = str(self._catalog_id)
        if 'assignedGradebookIds' in gradebook_column_map:
            gradebook_column_map['assignedGradebookIds'] = [str(self._catalog_id)]
        insert_result = collection.insert_one(gradebook_column_map)
        result = objects.GradebookColumn(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)
        return result

    @utilities.arguments_not_none
    def update_gradebook_column(self, gradebook_column_form):
        """Updates an existing gradebook column.

        arg:    gradebook_column_form
                (osid.grading.GradebookColumnForm): the form containing
                the elements to be updated
        raise:  IllegalState - ``gradebook_column_form`` already used in
                an update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``gradebook_column_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``gradebook_column_form`` did not
                originate from
                ``get_gradebook_column_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)
        if not isinstance(gradebook_column_form, ABCGradebookColumnForm):
            raise errors.InvalidArgument('argument type is not an GradebookColumnForm')
        if not gradebook_column_form.is_for_update():
            raise errors.InvalidArgument('the GradebookColumnForm is for update only, not create')
        try:
            if self._forms[gradebook_column_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('gradebook_column_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('gradebook_column_form did not originate from this session')
        if not gradebook_column_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')

        # check that there are no entries, if updating the gradeSystemId
        old_column = collection.find_one({"_id": gradebook_column_form._my_map['_id']})
        if old_column['gradeSystemId'] != gradebook_column_form._my_map['gradeSystemId']:
            if self._has_entries(gradebook_column_form.id_):
                raise errors.IllegalState('Entries exist in this gradebook column. ' +
                                          'Cannot change the grade system.')

        collection.save(gradebook_column_form._my_map)

        self._forms[gradebook_column_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.GradebookColumn(
            osid_object_map=gradebook_column_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    @utilities.arguments_not_none
    def sequence_gradebook_columns(self, gradebook_column_ids):
        """Resequences the gradebook columns.

        arg:    gradebook_column_ids (osid.id.IdList): the ``Ids`` of
                the ``GradebookColumns``
        raise:  NullArgument - ``gradebook_column_id_list`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def move_gradebook_column(self, front_gradebook_column_id, back_gradebook_column_id):
        """Moves a gradebook column in front of another.

        arg:    front_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        arg:    back_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        raise:  NotFound - ``front_gradebook_column_id or
                back_gradebook_column_id`` is not found
        raise:  NullArgument - ``front_gradebook_column_id or
                back_gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def copy_gradebook_column_entries(self, source_gradebook_column_id, target_gradebook_column_id):
        """Copies gradebook column entries from one column to another.

        If the target grade column grade system differs from the source,
        the grades in the entries are transformed to the new grade
        system.

        arg:    source_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        arg:    target_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        raise:  NotFound - ``source_gradebook_column_id
                ortarget_gradebook_column_id`` is not found
        raise:  NullArgument - ``source_gradebook_column_id
                target_gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def can_delete_gradebook_columns(self):
        """Tests if this user can delete gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradebookColumn`` deletion is
                not authorized, ``true`` otherwise
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
    def delete_gradebook_column(self, gradebook_column_id):
        """Deletes the ``GradebookColumn`` identified by the given ``Id``.

        arg:    gradebook_column_id (osid.id.Id): the ``Id`` of the
                ``GradebookColumn`` to delete
        raise:  NotFound - a ``GradebookColumn`` was not found
                identified by the given ``Id``
        raise:  NullArgument - ``gradebook_column_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(gradebook_column_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')

        # check that no entries already exist for this gradebook column
        grading_manager = self._get_provider_manager('GRADING')
        gels = grading_manager.get_grade_entry_lookup_session(proxy=getattr(self, "_proxy", None))
        gels.use_federated_gradebook_view()
        entries = gels.get_grade_entries_for_gradebook_column(gradebook_column_id)
        if self._has_entries(gradebook_column_id):
            raise errors.IllegalState('Entries exist in this gradebook column. Cannot delete it.')

        collection = JSONClientValidated('grading',
                                         collection='GradebookColumn',
                                         runtime=self._runtime)

        gradebook_column_map = collection.find_one({'_id': ObjectId(gradebook_column_id.get_identifier())})

        objects.GradebookColumn(osid_object_map=gradebook_column_map,
                                runtime=self._runtime,
                                proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(gradebook_column_id.get_identifier())})

    def can_manage_gradebook_column_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradebookColumns``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``GradebookColumn`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_gradebook_column(self, gradebook_column_id, alias_id):
        """Adds an ``Id`` to a ``GradebookColumn`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradebookColumn`` is determined by
        the provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another gradebook column,
        it is reassigned to the given gradebook column ``Id``.

        arg:    gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``gradebook_column_id`` not found
        raise:  NullArgument - ``gradebook_column_id`` or ``alias_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=gradebook_column_id, equivalent_id=alias_id)

    def _has_entries(self, gradebook_column_id):
        grading_manager = self._get_provider_manager('GRADING')
        gels = grading_manager.get_grade_entry_lookup_session(proxy=getattr(self, "_proxy", None))
        gels.use_federated_gradebook_view()
        entries = gels.get_grade_entries_for_gradebook_column(gradebook_column_id)
        return entries.available() > 0


class GradebookLookupSession(abc_grading_sessions.GradebookLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Gradebook`` objects.

    The ``Gradebook`` represents a collection of grade systems, entries,
    and gradebook columns.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Gradebooks`` it can access, without breaking
    execution. However, an administrative application may require all
    ``Gradebook`` elements to be available.

    Gradebooks may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Gradebook``.

    """
    _session_namespace = 'grading.GradebookLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_gradebooks(self):
        """Tests if this user can perform ``Gradebook`` lookups.

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

    def use_comparative_gradebook_view(self):
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

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Gradebook`` returns is desired.

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
    def get_gradebook(self, gradebook_id):
        """Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        arg:    gradebook_id (osid.id.Id): ``Id`` of the ``Gradebook``
        return: (osid.grading.Gradebook) - the gradebook
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=gradebook_id)
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if gradebook_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.Gradebook, cat_name='Gradebook')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(gradebook_id, 'grading').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated Gradebook.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(gradebook_id, 'grading', 'Gradebook')

        return objects.Gradebook(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_gradebooks_by_ids(self, gradebook_ids):
        """Gets a ``GradebookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        gradebooks specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Gradebook`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        arg:    gradebook_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``gradebook_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_Gradebook() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=gradebook_ids)
        catalog_id_list = []
        for i in gradebook_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.GradebookList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include gradebooks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        arg:    gradebook_genus_type (osid.type.Type): a gradebook genus
                type
        return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        raise:  NullArgument - ``gradebook_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=gradebook_genus_type)
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(gradebook_genus_type)}).sort('_id', DESCENDING)

        return objects.GradebookList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional gradebooks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        arg:    gradebook_genus_type (osid.type.Type): a gradebook genus
                type
        return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        raise:  NullArgument - ``gradebook_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_gradebooks_by_record_type(self, gradebook_record_type):
        """Gets a ``GradebookList`` containing the given gradebook record ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        arg:    gradebook_record_type (osid.type.Type): a gradebook
                record type
        return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        raise:  NullArgument - ``gradebook_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_gradebooks_by_provider(self, resource_id):
        """Gets a ``GradebookList`` for the given provider ````.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_gradebooks(self):
        """Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        return: (osid.grading.GradebookList) - a ``GradebookList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.GradebookList(result, runtime=self._runtime, proxy=self._proxy)

    gradebooks = property(fget=get_gradebooks)


class GradebookAdminSession(abc_grading_sessions.GradebookAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Gradebooks``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Gradebook,`` a ``GradebookForm`` is requested using
    ``get_gradebook_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradebookForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``GradebookForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``GradebookForm``
    corresponds to an attempted transaction.

    For updates, ``GradebookForms`` are requested to the ``Gradebook``
    ``Id`` that is to be updated using ``getGradebookFormForUpdate()``.
    Similarly, the ``GradebookForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``GradebookForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Gradebooks``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    _session_namespace = 'grading.GradebookAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_gradebooks(self):
        """Tests if this user can create ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``Gradebook`` creation is not
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
    def can_create_gradebook_with_record_types(self, gradebook_record_types):
        """Tests if this user can create a single ``Gradebook`` using the desired record types.

        While ``GradingManager.getGradebookRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Gradebook``.
        Providing an empty array tests if a ``Gradebook`` can be created
        with no records.

        arg:    gradebook_record_types (osid.type.Type[]): array of
                gradebook record types
        return: (boolean) - ``true`` if ``Gradebook`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``gradebook_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalogs_with_record_types(catalog_record_types=gradebook_record_types)
        return True

    @utilities.arguments_not_none
    def get_gradebook_form_for_create(self, gradebook_record_types):
        """Gets the gradebook form for creating new gradebooks.

        A new form should be requested for each create transaction.

        arg:    gradebook_record_types (osid.type.Type[]): array of
                gradebook record types
        return: (osid.grading.GradebookForm) - the gradebook form
        raise:  NullArgument - ``gradebook_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=gradebook_record_types)
        for arg in gradebook_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if gradebook_record_types == []:
            result = objects.GradebookForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.GradebookForm(
                record_types=gradebook_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_gradebook(self, gradebook_form):
        """Creates a new ``Gradebook``.

        arg:    gradebook_form (osid.grading.GradebookForm): the form
                for this ``Gradebook``
        return: (osid.grading.Gradebook) - the new ``Gradebook``
        raise:  IllegalState - ``gradebook_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``gradebook_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``gradebook_form`` did not originate from
                ``get_gradebook_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=gradebook_form)
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        if not isinstance(gradebook_form, ABCGradebookForm):
            raise errors.InvalidArgument('argument type is not an GradebookForm')
        if gradebook_form.is_for_update():
            raise errors.InvalidArgument('the GradebookForm is for update only, not create')
        try:
            if self._forms[gradebook_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('gradebook_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('gradebook_form did not originate from this session')
        if not gradebook_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(gradebook_form._my_map)

        self._forms[gradebook_form.get_id().get_identifier()] = CREATED
        result = objects.Gradebook(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_gradebooks(self):
        """Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        return: (boolean) - ``false`` if ``Gradebook`` modification is
                not authorized, ``true`` otherwise
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
    def get_gradebook_form_for_update(self, gradebook_id):
        """Gets the gradebook form for updating an existing gradebook.

        A new gradebook form should be requested for each update
        transaction.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the
                ``Gradebook``
        return: (osid.grading.GradebookForm) - the gradebook form
        raise:  NotFound - ``gradebook_id`` is not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=gradebook_id)
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        if not isinstance(gradebook_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(gradebook_id.get_identifier())})

        cat_form = objects.GradebookForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_gradebook(self, gradebook_form):
        """Updates an existing gradebook.

        arg:    gradebook_form (osid.grading.GradebookForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``gradebook_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``gradebook_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``gradebook_form did not originate from
                get_gradebook_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=gradebook_form)
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        if not isinstance(gradebook_form, ABCGradebookForm):
            raise errors.InvalidArgument('argument type is not an GradebookForm')
        if not gradebook_form.is_for_update():
            raise errors.InvalidArgument('the GradebookForm is for update only, not create')
        try:
            if self._forms[gradebook_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('gradebook_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('gradebook_form did not originate from this session')
        if not gradebook_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(gradebook_form._my_map)  # save is deprecated - change to replace_one

        self._forms[gradebook_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.Gradebook(osid_object_map=gradebook_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_gradebooks(self):
        """Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``Gradebook`` deletion is not
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
    def delete_gradebook(self, gradebook_id):
        """Deletes a ``Gradebook``.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of the
                ``Gradebook`` to remove
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=gradebook_id)
        collection = JSONClientValidated('grading',
                                         collection='Gradebook',
                                         runtime=self._runtime)
        if not isinstance(gradebook_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['GradeSystem', 'GradeEntry', 'GradebookColumn', 'Gradebook']:
            obj_collection = JSONClientValidated('grading',
                                                 collection=object_catalog,
                                                 runtime=self._runtime)
            if obj_collection.find({'assignedGradebookIds': {'$in': [str(gradebook_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(gradebook_id.get_identifier())})

    def can_manage_gradebook_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Gradebook`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_gradebook(self, gradebook_id, alias_id):
        """Adds an ``Id`` to a ``Gradebook`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Gradebook`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another gradebook, it is
        reassigned to the given gradebook ``Id``.

        arg:    gradebook_id (osid.id.Id): the ``Id`` of a ``Gradebook``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``gradebook_id`` not found
        raise:  NullArgument - ``gradebook_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=gradebook_id, alias_id=osid.id.Id)
        self._alias_id(primary_id=gradebook_id, equivalent_id=alias_id)
