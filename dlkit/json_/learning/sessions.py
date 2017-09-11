"""JSON implementations of learning sessions."""

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
from ..id.objects import IdList
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import DateTime
from ..primitives import Id
from ..primitives import Type
from ..types import Relationship
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from ..utilities import overlap
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.learning import sessions as abc_learning_sessions
from dlkit.abstract_osid.learning.objects import ActivityForm as ABCActivityForm
from dlkit.abstract_osid.learning.objects import ObjectiveBankForm as ABCObjectiveBankForm
from dlkit.abstract_osid.learning.objects import ObjectiveForm as ABCObjectiveForm
from dlkit.abstract_osid.learning.objects import ProficiencyForm as ABCProficiencyForm
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


class ObjectiveLookupSession(abc_learning_sessions.ObjectiveLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Objective`` s."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objectives(self):
        """Tests if this user can perform ``Objective`` lookups.

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

    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_objective_view(self):
        """A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_objective(self, objective_id):
        """Gets the ``Objective`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Objective`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Objective`` and retained
        for compatibility.

        arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        return: (osid.learning.Objective) - the objective
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(objective_id, 'learning').get_identifier())},
                 **self._view_filter()))
        return objects.Objective(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_objectives_by_ids(self, objective_ids):
        """Gets an ``ObjectiveList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        objectives specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Objectives`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    objective_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``objective_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        object_id_list = []
        for i in objective_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'learning').get_identifier()))
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
        return objects.ObjectiveList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_objectives_by_genus_type(self, objective_genus_type):
        """Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` which does not include objectives of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        arg:    objective_genus_type (osid.type.Type): an objective
                genus type
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NullArgument - ``objective_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(objective_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.ObjectiveList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_objectives_by_parent_genus_type(self, objective_genus_type):
        """Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` and include any additional objective with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session

        arg:    objective_genus_type (osid.type.Type): an objective
                genus type
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NullArgument - ``objective_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ObjectiveList([])

    @utilities.arguments_not_none
    def get_objectives_by_record_type(self, objective_record_type):
        """Gets an ``ObjectiveList`` containing the given objective record ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        arg:    objective_record_type (osid.type.Type): an objective
                record type
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NullArgument - ``objective_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ObjectiveList([])

    def get_objectives(self):
        """Gets all ``Objectives``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        return: (osid.learning.ObjectiveList) - an ``ObjectiveList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.ObjectiveList(result, runtime=self._runtime, proxy=self._proxy)

    objectives = property(fget=get_objectives)


class ObjectiveQuerySession(abc_learning_sessions.ObjectiveQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching ``Objective`` objects.

    The search query is constructed using the ``ObjectiveQuery``. The
    objective record ``Type`` also specifies the record for the
    objective query.

    This session defines views that offer differing behaviors for
    searching.

      * federated objective bank view: searches include objectives in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      * isolated objective bank view: searches are restricted to
        objectives in this objective bank


    Objectives may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``ObjectiveQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_search_objectives(self):
        """Tests if this user can perform ``Objectives`` searches.

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

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_objective_query(self):
        """Gets an objective query.

        return: (osid.learning.ObjectiveQuery) - the objective query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.ObjectiveQuery(runtime=self._runtime)

    objective_query = property(fget=get_objective_query)

    @utilities.arguments_not_none
    def get_objectives_by_query(self, objective_query):
        """Gets a list of ``Objectives`` matching the given objective query.

        arg:    objective_query (osid.learning.ObjectiveQuery): the
                objective query
        return: (osid.learning.ObjectiveList) - the returned
                ``ObjectiveList``
        raise:  NullArgument - ``objective_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``objective_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in objective_query._query_terms:
            if '$in' in objective_query._query_terms[term] and '$nin' in objective_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': objective_query._query_terms[term]['$in']}},
                             {term: {'$nin': objective_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: objective_query._query_terms[term]})
        for term in objective_query._keyword_terms:
            or_list.append({term: objective_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('learning',
                                             collection='Objective',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.ObjectiveList(result, runtime=self._runtime, proxy=self._proxy)


class ObjectiveAdminSession(abc_learning_sessions.ObjectiveAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Objectives``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Objective,`` a ``ObjectiveForm`` is requested using
    ``get_objective_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ObjectiveForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ObjectiveForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ObjectiveForm``
    corresponds to an attempted transaction.

    For updates, ``ObjectiveForms`` are requested to the ``Objective``
    ``Id`` that is to be updated using ``getObjectiveFormForUpdate()``.
    Similarly, the ``ObjectiveForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``ObjectiveForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Objectives``. To unmap an
    ``Objective`` from the current ``ObjectiveBank,`` the
    ``ObjectiveObjectiveBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Objective`` itself thus
    removing it from all known ``ObjectiveBank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_create_objectives(self):
        """Tests if this user can create ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Objective
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Objective`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_objective_with_record_types(self, objective_record_types):
        """Tests if this user can create a single ``Objective`` using the desired record types.

        While ``LearningManager.getObjectiveRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Objective``.
        Providing an empty array tests if an ``Objective`` can be
        created with no records.

        arg:    objective_record_types (osid.type.Type[]): array of
                objective record types
        return: (boolean) - ``true`` if ``Objective`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``objective_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_objective_form_for_create(self, objective_record_types):
        """Gets the objective form for creating new objectives.

        A new form should be requested for each create transaction.

        arg:    objective_record_types (osid.type.Type[]): array of
                objective record types
        return: (osid.learning.ObjectiveForm) - the objective form
        raise:  NullArgument - ``objective_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_create_template
        for arg in objective_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if objective_record_types == []:
            obj_form = objects.ObjectiveForm(
                objective_bank_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        else:
            obj_form = objects.ObjectiveForm(
                objective_bank_id=self._catalog_id,
                record_types=objective_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_objective(self, objective_form):
        """Creates a new ``Objective``.

        arg:    objective_form (osid.learning.ObjectiveForm): the form
                for this ``Objective``
        return: (osid.learning.Objective) - the new ``Objective``
        raise:  IllegalState - ``objective_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``objective_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``objective_form`` did not originate from
                ``get_objective_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        if not isinstance(objective_form, ABCObjectiveForm):
            raise errors.InvalidArgument('argument type is not an ObjectiveForm')
        if objective_form.is_for_update():
            raise errors.InvalidArgument('the ObjectiveForm is for update only, not create')
        try:
            if self._forms[objective_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('objective_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('objective_form did not originate from this session')
        if not objective_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(objective_form._my_map)

        self._forms[objective_form.get_id().get_identifier()] = CREATED
        result = objects.Objective(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_objectives(self):
        """Tests if this user can update ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if objective modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_objective_form_for_update(self, objective_id):
        """Gets the objective form for updating an existing objective.

        A new objective form should be requested for each update
        transaction.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        return: (osid.learning.ObjectiveForm) - the objective form
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        if not isinstance(objective_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (objective_id.get_identifier_namespace() != 'learning.Objective' or
                objective_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(objective_id.get_identifier())})

        obj_form = objects.ObjectiveForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_objective(self, objective_form):
        """Updates an existing objective.

        arg:    objective_form (osid.learning.ObjectiveForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``objective_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``objective_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``objective_form`` did not originate from
                ``get_objective_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        if not isinstance(objective_form, ABCObjectiveForm):
            raise errors.InvalidArgument('argument type is not an ObjectiveForm')
        if not objective_form.is_for_update():
            raise errors.InvalidArgument('the ObjectiveForm is for update only, not create')
        try:
            if self._forms[objective_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('objective_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('objective_form did not originate from this session')
        if not objective_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(objective_form._my_map)

        self._forms[objective_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Objective(
            osid_object_map=objective_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_objectives(self):
        """Tests if this user can delete ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Objective`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_objective(self, objective_id):
        """Deletes the ``Objective`` identified by the given ``Id``.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective`` to delete
        raise:  NotFound - an ``Objective`` was not found identified by
                the given ``Id``
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ObjectiveAdminSession.delete_objective_template

        if not isinstance(objective_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        if collection.find({'objectiveId': str(objective_id)}).count() != 0:
            raise errors.IllegalState('there are still Activitys associated with this Objective')

        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        collection.delete_one({'_id': ObjectId(objective_id.get_identifier())})

    def can_manage_objective_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Objective`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_objective(self, objective_id, alias_id):
        """Adds an ``Id`` to an ``Objective`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Objective`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective, it is
        reassigned to the given objective ``Id``.

        arg:    objective_id (osid.id.Id): the ``Id`` of an
                ``Objective``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=objective_id, equivalent_id=alias_id)


class ObjectiveHierarchySession(abc_learning_sessions.ObjectiveHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Objective`` objects.

    Each node in the hierarchy is a unique ``Objective that contains its
    child objectives``. The hierarchy may be traversed recursively to
    establish the tree structure through ``get_parent_objectives()`` and
    ``getChildObjectives()``. To relate these ``Ids`` to another OSID,
    ``get_objective_nodes()`` can be used for retrievals that can be
    used for bulk lookups in other OSIDs. Any ``Objective`` available in
    the Learning OSID is known to this hierarchy but does not appear in
    the hierarchy traversal until added as a root node or a child of
    another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_objectives()`` or ``get_child_objectives()``
    in lieu of a ``PermissionDenied`` error that may disrupt the
    traversal through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: objective elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, *args, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Objective
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()
        self._kwargs = kwargs
        hierarchy_mgr = self._get_provider_manager('HIERARCHY')
        self._hierarchy_session = hierarchy_mgr.get_hierarchy_traversal_session_for_hierarchy(
            Id(authority='LEARNING',
               namespace='CATALOG',
               identifier='OBJECTIVE'),
            proxy=self._proxy
        )

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_access_objective_hierarchy(self):
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
        raise errors.Unimplemented()

    def use_comparative_objective_view(self):
        """The returns from the objective methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_objective_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def get_root_objective_ids(self):
        """Gets the root objective ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root objective ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    root_objective_ids = property(fget=get_root_objective_ids)

    def get_root_objectives(self):
        """Gets the root objective in this objective hierarchy.

        return: (osid.learning.ObjectiveList) - the root objective
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchySession.get_root_subjects_template
        root_ids = self._hierarchy_session.get_roots()
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'_id': {'$in': [ObjectId(root_id.get_identifier()) for root_id in root_ids]}},
                 **self._view_filter()))
        return objects.ObjectiveList(
            result,
            runtime=self._runtime,
            proxy=self._proxy)

    root_objectives = property(fget=get_root_objectives)

    @utilities.arguments_not_none
    def has_parent_objectives(self, objective_id):
        """Tests if the ``Objective`` has any parents.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (boolean) - ``true`` if the objective has parents,
                ``false`` otherwise
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def is_parent_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is a direct parent of an objective.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``objective_id,``  ``false`` otherwise
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_parent_objective_ids(self, objective_id):
        """Gets the parent ``Ids`` of the given objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (osid.id.IdList) - the parent ``Ids`` of the objective
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_parent_objectives(self, objective_id):
        """Gets the parents of the given objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (osid.learning.ObjectiveList) - the parents of the
                objective
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def is_ancestor_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is an ancestor of an objective.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``objective_id,``  ``false`` otherwise
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def has_child_objectives(self, objective_id):
        """Tests if an objective has any children.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (boolean) - ``true`` if the ``objective_id`` has
                children, ``false`` otherwise
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def is_child_of_objective(self, id_, objective_id):
        """Tests if an objective is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``objective_id,``  ``false`` otherwise
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_child_objective_ids(self, objective_id):
        """Gets the child ``Ids`` of the given objective.

        arg:    objective_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the objective
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_child_objectives(self, objective_id):
        """Gets the children of the given objective.

        arg:    objective_id (osid.id.Id): the ``Id`` to query
        return: (osid.learning.ObjectiveList) - the children of the
                objective
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchySession.get_child_subjects_template
        if self._hierarchy_session.has_children(objective_id):
            child_ids = self._hierarchy_session.get_children(objective_id)
            collection = JSONClientValidated('learning',
                                             collection='Objective',
                                             runtime=self._runtime)
            result = collection.find(
                dict({'_id': {'$in': [ObjectId(child_id.get_identifier()) for child_id in child_ids]}},
                     **self._view_filter()))
            return objects.ObjectiveList(
                result,
                runtime=self._runtime,
                proxy=self._proxy)
        raise errors.IllegalState('no children')

    @utilities.arguments_not_none
    def is_descendant_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is a descendant of an objective.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``objective_id,`` ``false`` otherwise
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_objective_node_ids(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective.

        arg:    objective_id (osid.id.Id): the ``Id`` to query
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
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_objective_nodes(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective.

        arg:    objective_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.learning.ObjectiveNode) - an objective node
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ObjectiveHierarchyDesignSession(abc_learning_sessions.ObjectiveHierarchyDesignSession, osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Objective`` objects.

    Each node in the hierarchy is a unique ``Objective``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, *args, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Objective
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()
        self._kwargs = kwargs
        hierarchy_mgr = self._get_provider_manager('HIERARCHY')
        self._hierarchy_session = hierarchy_mgr.get_hierarchy_design_session_for_hierarchy(
            Id(authority='LEARNING',
               namespace='CATALOG',
               identifier='OBJECTIVE'),
            proxy=self._proxy
        )

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_modify_objective_hierarchy(self):
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
        # osid.ontology.SubjectHierarchyDesignSession.can_modify_subject_hierarchy_template
        return True

    @utilities.arguments_not_none
    def add_root_objective(self, objective_id):
        """Adds a root objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        raise:  AlreadyExists - ``objective_id`` is already in hierarchy
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchyDesignSession.add_root_subject_template
        return self._hierarchy_session.add_root(id_=objective_id)

    @utilities.arguments_not_none
    def remove_root_objective(self, objective_id):
        """Removes a root objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchyDesignSession.remove_root_subject_template
        return self._hierarchy_session.remove_root(id_=objective_id)

    @utilities.arguments_not_none
    def add_child_objective(self, objective_id, child_id):
        """Adds a child to an objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``objective_id`` is already a parent of
                ``child_id``
        raise:  NotFound - ``objective_id`` or ``child_id`` not found
        raise:  NullArgument - ``objective_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchyDesignSession.add_child_subject_template
        return self._hierarchy_session.add_child(id_=objective_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_objective(self, objective_id, child_id):
        """Removes a child from an objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  NotFound - ``objective_id`` not a parent of ``child_id``
        raise:  NullArgument - ``objective_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchyDesignSession.remove_child_subject_template
        return self._hierarchy_session.remove_child(id_=objective_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_objectives(self, objective_id):
        """Removes all children from an objective.

        arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.ontology.SubjectHierarchyDesignSession.remove_child_subjects_template
        return self._hierarchy_session.remove_children(id_=objective_id)


class ObjectiveSequencingSession(abc_learning_sessions.ObjectiveSequencingSession, osid_sessions.OsidSession):
    """This session provides methods to sequence the objectives in the objective hierarchy."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        self._catalog_class = objects.Objective
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()

    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    objective_hierarchy = property(fget=get_objective_hierarchy)

    def can_sequence_objectives(self):
        """Tests if this user can sequence objectives.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        return: (boolean) - ``false`` if sequencing objectives is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def move_objective_ahead(self, parent_objective_id, reference_objective_id, objective_id):
        """Moves an objective ahead of a refrence objective under the given parent.

        arg:    parent_objective_id (osid.id.Id): the ``Id`` of the
                parent objective
        arg:    reference_objective_id (osid.id.Id): the ``Id`` of the
                objective
        arg:    objective_id (osid.id.Id): the ``Id`` of the objective
                to move ahead of ``reference_objective_id``
        raise:  NotFound - ``parent_objective_id,
                reference_objective_id,`` or ``objective_id`` not found,
                or ``reference_objective_id`` or ``objective_id`` is not
                a child of ``parent_objective_id``
        raise:  NullArgument - ``parent_objective_id,
                reference_objective_id,`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def move_objective_behind(self, parent_objective_id, reference_objective_id, objective_id):
        """Moves an objective behind a refrence objective under the given parent.

        arg:    parent_objective_id (osid.id.Id): the ``Id`` of the
                parent objective
        arg:    reference_objective_id (osid.id.Id): the ``Id`` of the
                objective
        arg:    objective_id (osid.id.Id): the ``Id`` of the objective
                to move behind ``reference_objective_id``
        raise:  NotFound - ``parent_objective_id,
                reference_objective_id,`` or ``objective_id`` not found,
                or ``reference_objective_id`` or ``objective_id`` is not
                a child of ``parent_objective_id``
        raise:  NullArgument - ``parent_objective_id,
                reference_objective_id,`` or ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def sequence_objectives(self, parent_objective_id, objective_ids):
        """Sequences a set of objectives under a parent.

        arg:    parent_objective_id (osid.id.Id): the ``Id`` of the
                parent objective
        arg:    objective_ids (osid.id.Id[]): the ``Id`` of the
                objectives
        raise:  NotFound - ``parent_id`` or an ``objective_id`` not
                found, or an ``objective_id`` is not a child of
                ``parent_objective_id``
        raise:  NullArgument - ``paren_objectivet_id`` or
                ``objective_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ObjectiveObjectiveBankSession(abc_learning_sessions.ObjectiveObjectiveBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Objective`` to ``ObjectiveBank`` mappings.

    An ``Objective`` may appear in multiple ``ObjectiveBanks``. Each
    ``ObjectiveBank`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'learning.ObjectiveObjectiveBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_objective_objective_bank_mappings(self):
        """Tests if this user can perform lookups of objective/objective bank mappings.

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

    def use_comparative_objective_bank_view(self):
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

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

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
    def get_objective_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        return: (osid.id.IdList) - list of related objectives
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for objective in self.get_objectives_by_objective_bank(objective_bank_id):
            id_list.append(objective.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_objectives_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ObjectiveList) - list of related
                objective ``Ids``
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_lookup_session_for_objective_bank(objective_bank_id, proxy=self._proxy)
        lookup_session.use_isolated_objective_bank_view()
        return lookup_session.get_objectives()

    @utilities.arguments_not_none
    def get_objective_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        return: (osid.id.IdList) - list of objective ``Ids``
        raise:  NullArgument - ``objective_bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for objective in self.get_objectives_by_objective_banks(objective_bank_ids):
            id_list.append(objective.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_objectives_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        return: (osid.learning.ObjectiveList) - list of objectives
        raise:  NullArgument - ``objective_bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        objective_list = []
        for objective_bank_id in objective_bank_ids:
            objective_list += list(
                self.get_objectives_by_objective_bank(objective_bank_id))
        return objects.ObjectiveList(objective_list)

    @utilities.arguments_not_none
    def get_objective_bank_ids_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        arg:    objective_id (osid.id.Id): ``Id`` of an ``Objective``
        return: (osid.id.IdList) - list of objective bank ``Ids``
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_objective_bank_view()
        objective = lookup_session.get_objective(objective_id)
        id_list = []
        for idstr in objective._my_map['assignedObjectiveBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_objective_banks_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        arg:    objective_id (osid.id.Id): ``Id`` of an ``Objective``
        return: (osid.learning.ObjectiveBankList) - list of objective
                banks
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_objective_banks_by_ids(
            self.get_objective_bank_ids_by_objective(objective_id))


class ObjectiveObjectiveBankAssignmentSession(abc_learning_sessions.ObjectiveObjectiveBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Objectives`` to ``ObjectiveBanks``.

    An ``Objective`` may map to multiple ``ObjectiveBanks`` and removing
    the last reference to an ``Objective`` is the equivalent of deleting
    it. Each ``ObjectiveBank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``Objective`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    _session_namespace = 'learning.ObjectiveObjectiveBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'ObjectiveBank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_objectives(self):
        """Tests if this user can alter objective/objective bank mappings.

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
    def can_assign_objectives_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if objective_bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any objective can be assigned.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        objective_banks = lookup_session.get_objective_banks()
        id_list = []
        for objective_bank in objective_banks:
            id_list.append(objective_bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_objective_bank_ids_for_objective(self, objective_bank_id, objective_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific objective can be assigned.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        raise:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_objective_bank_ids(objective_bank_id)

    @utilities.arguments_not_none
    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        """Adds an existing ``Objective`` to an ``ObjectiveBank``.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        raise:  AlreadyExists - ``objective_id`` already mapped to
                ``objective_bank_id``
        raise:  NotFound - ``objective_id`` or ``objective_bank_id`` not
                found
        raise:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_objective_bank(objective_bank_id)  # to raise NotFound
        self._assign_object_to_catalog(objective_id, objective_bank_id)

    @utilities.arguments_not_none
    def unassign_objective_from_objective_bank(self, objective_id, objective_bank_id):
        """Removes an ``Objective`` from an ``ObjectiveBank``.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        raise:  NotFound - ``objective_id`` or ``objective_bank_id`` not
                found or ``objective_id`` not mapped to
                ``objective_bank_id``
        raise:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_objective_bank(objective_bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(objective_id, objective_bank_id)

    @utilities.arguments_not_none
    def reassign_proficiency_to_objective_bank(self, objective_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        raise:  NotFound - ``objective_id, from_objective_bank_id,`` or
                ``to_objective_bank_id`` not found or ``objective_id``
                not mapped to ``from_objective_bank_id``
        raise:  NullArgument - ``objective_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.reassign_resource_to_bin
        self.assign_objective_to_objective_bank(objective_id, to_objective_bank_id)
        try:
            self.unassign_objective_from_objective_bank(objective_id, from_objective_bank_id)
        except:  # something went wrong, roll back assignment to to_objective_bank_id
            self.unassign_objective_from_objective_bank(objective_id, to_objective_bank_id)
            raise


class ObjectiveRequisiteSession(abc_learning_sessions.ObjectiveRequisiteSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving objective requisites.

    A requisite is a set of ``Objectives`` that should be achieved
    before another ``Objective`` is attempted.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * isolated objective bank view: All objective methods in this
        session operate, retrieve and pertain to objectives defined
        explicitly in the current objective bank. Using an isolated view
        is useful for managing objectives with the
        ``ObjectiveAdminSession.``
      * federated objective bank view: All objective methods in this
        session operate, retrieve and pertain to all objectives defined
        in this objective bank and any other objective banks implicitly
        available in this objective bank through objective bank
        inheritence.


    Objectives may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Objective``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        self._catalog_class = objects.Objective
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_objective_prerequisites(self):
        """Tests if this user can perform ``Objective`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_objective_view(self):
        """A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_requisite_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are the immediate requisites for the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        return: (osid.learning.ObjectiveList) - the returned requisite
                ``Objectives``
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ObjectiveRequisiteSession.get_requisite_objectives_template
        # NOTE: This implementation currently ignores plenary view
        requisite_type = Type(**Relationship().get_type_data('OBJECTIVE.REQUISITE'))
        relm = self._get_provider_manager('RELATIONSHIP')
        rls = relm.get_relationship_lookup_session(proxy=self._proxy)
        rls.use_federated_family_view()
        requisite_relationships = rls.get_relationships_by_genus_type_for_source(objective_id,
                                                                                 requisite_type)
        destination_ids = [ObjectId(r.get_destination_id().identifier)
                           for r in requisite_relationships]
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': destination_ids}})
        return objects.ObjectiveList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_all_requisite_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are the requisites for the given ``Objective`` including the requistes of the requisites, and so on.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_dependent_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that require the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ObjectiveRequisiteSession.get_dependent_objectives_template
        # NOTE: This implementation currently ignores plenary view
        requisite_type = Type(**Relationship().get_type_data('OBJECTIVE.REQUISITE'))
        relm = self._get_provider_manager('RELATIONSHIP')
        rls = relm.get_relationship_lookup_session(proxy=self._proxy)
        rls.use_federated_family_view()
        requisite_relationships = rls.get_relationships_by_genus_type_for_destination(objective_id,
                                                                                      requisite_type)
        source_ids = [ObjectId(r.get_source_id().identifier)
                      for r in requisite_relationships]
        collection = JSONClientValidated('learning',
                                         collection='Objective',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': source_ids}})
        return objects.ObjectiveList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def is_objective_required(self, objective_id, required_objective_id):
        """Tests if an objective is required before proceeding with an objective.

        One objective may indirectly depend on another objective by way
        of one or more other objectives.

        arg:    objective_id (osid.id.Id): ``Id`` of the dependent
                ``Objective``
        arg:    required_objective_id (osid.id.Id): ``Id`` of the
                required ``Objective``
        return: (boolean) - ``true`` if ``objective_id`` depends on
                ``required_objective_id,`` ``false`` otherwise
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_equivalent_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are equivalent to the given ``Objective`` for the purpose of requisites.

        An equivalent objective can satisfy the given objective. In
        plenary mode, the returned list contains all of the equivalent
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ObjectiveRequisiteAssignmentSession(abc_learning_sessions.ObjectiveRequisiteAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to manage requisites.

    Each ``ObjectiveBank`` may have its own authorizations governing who
    is allowed to operate on it.

    Moving or adding a reference of an ``Objective`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None):
        self._catalog_class = objects.Objective
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_assign_requisites(self):
        """Tests if this user can manage objective requisites.

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
    def assign_objective_requisite(self, objective_id, requisite_objective_id):
        """Creates a requirement dependency between two ``Objectives``.

        arg:    objective_id (osid.id.Id): the ``Id`` of the dependent
                ``Objective``
        arg:    requisite_objective_id (osid.id.Id): the ``Id`` of the
                required ``Objective``
        raise:  AlreadyExists - ``objective_id`` already mapped to
                ``requisite_objective_id``
        raise:  NotFound - ``objective_id`` or
                ``requisite_objective_id`` not found
        raise:  NullArgument - ``objective_id`` or
                ``requisite_objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        requisite_type = Type(**Relationship().get_type_data('OBJECTIVE.REQUISITE'))

        ras = self._get_provider_manager(
            'RELATIONSHIP').get_relationship_admin_session_for_family(
            self.get_objective_bank_id(), proxy=self._proxy)
        rfc = ras.get_relationship_form_for_create(objective_id, requisite_objective_id, [])
        rfc.set_display_name('Objective Requisite')
        rfc.set_description('An Objective Requisite created by the ObjectiveRequisiteAssignmentSession')
        rfc.set_genus_type(requisite_type)
        ras.create_relationship(rfc)

    @utilities.arguments_not_none
    def unassign_objective_requisite(self, objective_id, requisite_objective_id):
        """Removes an ``Objective`` requisite from an ``Objective``.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        arg:    requisite_objective_id (osid.id.Id): the ``Id`` of the
                required ``Objective``
        raise:  NotFound - ``objective_id`` or
                ``requisite_objective_id`` not found or ``objective_id``
                not mapped to ``requisite_objective_id``
        raise:  NullArgument - ``objective_id`` or
                ``requisite_objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        requisite_type = Type(**Relationship().get_type_data('OBJECTIVE.REQUISITE'))
        rls = self._get_provider_manager(
            'RELATIONSHIP').get_relationship_lookup_session_for_family(
            self.get_objective_bank_id(), proxy=self._proxy)
        ras = self._get_provider_manager(
            'RELATIONSHIP').get_relationship_admin_session_for_family(
            self.get_objective_bank_id(), proxy=self._proxy)
        rls.use_federated_family_view()
        relationships = rls.get_relationships_by_genus_type_for_source(objective_id, requisite_type)
        if relationships.available() == 0:
            raise errors.IllegalState('no Objective found')
        for relationship in relationships:
            if str(relationship.get_destination_id()) == str(requisite_objective_id):
                ras.delete_relationship(relationship.ident)

    @utilities.arguments_not_none
    def assign_equivalent_objective(self, objective_id, equivalent_objective_id):
        """Makes an objective equivalent to another objective for the purposes of satisfying a requisite.

        arg:    objective_id (osid.id.Id): the ``Id`` of the principal
                ``Objective``
        arg:    equivalent_objective_id (osid.id.Id): the ``Id`` of the
                equivalent ``Objective``
        raise:  AlreadyExists - ``objective_id`` already mapped to
                ``equiavelnt_objective_id``
        raise:  NotFound - ``objective_id`` or
                ``equivalent_objective_id`` not found
        raise:  NullArgument - ``objective_id`` or
                ``equivalent_objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def unassign_equivalent_objective(self, objective_id, equivalent_objective_id):
        """Removes an ``Objective`` requisite from an ``Objective``.

        arg:    objective_id (osid.id.Id): the ``Id`` of the principal
                ``Objective``
        arg:    equivalent_objective_id (osid.id.Id): the ``Id`` of the
                equivalent ``Objective``
        raise:  NotFound - ``objective_id`` or
                ``equivalent_objective_id`` not found or
                ``objective_id`` is already equivalent to
                ``equivalent_objective_id``
        raise:  NullArgument - ``objective_id`` or
                ``equivalent_objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()


class ActivityLookupSession(abc_learning_sessions.ActivityLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Activity`` objects.

    The ``Activity`` represents something to perform in order to achieve
    a learning objective.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * isolated objective bank view: All activity methods in this
        session operate, retrieve and pertain to activities defined
        explicitly in the current objective bank. Using an isolated view
        is useful for managing activities with the
        ``ActivityAdminSession.``
      * federated objective bank view: All activity methods in this
        session operate, retrieve and pertain to all activities defined
        in this objective bank and any other objective banks implicitly
        available in this objective bank through objective bank
        inheritence.


    Activities may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Activity``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_activities(self):
        """Tests if this user can perform ``Activity`` lookups.

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

    def use_comparative_activity_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_activity_view(self):
        """A complete view of the ``Activity`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_activity(self, activity_id):
        """Gets the ``Activity`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Activity`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Activity`` and retained for
        compatibility.

        arg:    activity_id (osid.id.Id): ``Id`` of the ``Activity``
        return: (osid.learning.Activity) - the activity
        raise:  NotFound - ``activity_id`` not found
        raise:  NullArgument - ``activity_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(activity_id, 'learning').get_identifier())},
                 **self._view_filter()))
        return objects.Activity(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_activities_by_ids(self, activity_ids):
        """Gets an ``ActivityList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        activities specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Activities`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        arg:    activity_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``activity_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        object_id_list = []
        for i in activity_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'learning').get_identifier()))
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
        return objects.ActivityList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_activities_by_genus_type(self, activity_genus_type):
        """Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` which does not include activities of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        arg:    activity_genus_type (osid.type.Type): an activity genus
                type
        return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        raise:  NullArgument - ``activity_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(activity_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.ActivityList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_activities_by_parent_genus_type(self, activity_genus_type):
        """Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` and include any additional activity with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        arg:    activity_genus_type (osid.type.Type): an activity genus
                type
        return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        raise:  NullArgument - ``activity_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ActivityList([])

    @utilities.arguments_not_none
    def get_activities_by_record_type(self, activity_record_type):
        """Gets a ``ActivityList`` containing the given activity record ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        arg:    activity_record_type (osid.type.Type): an activity
                record type
        return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        raise:  NullArgument - ``activity_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ActivityList([])

    @utilities.arguments_not_none
    def get_activities_for_objective(self, objective_id):
        """Gets the activities for the given objective.

        In plenary mode, the returned list contains all of the
        activities mapped to the objective ``Id`` or an error results if
        an Id in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        return: (osid.learning.ActivityList) - list of enrollments
        raise:  NotFound - ``objective_id`` not found
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'objectiveId': str(objective_id)},
                 **self._view_filter()))
        return objects.ActivityList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_activities_for_objectives(self, objective_ids):
        """Gets the activities for the given objectives.

        In plenary mode, the returned list contains all of the
        activities specified in the objective ``Id`` list, in the order
        of the list, including duplicates, or an error results if a
        course offering ``Id`` in the supplied list is not found or
        inaccessible. Otherwise, inaccessible ``Activities`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        arg:    objective_ids (osid.id.IdList): list of objective
                ``Ids``
        return: (osid.learning.ActivityList) - list of activities
        raise:  NotFound - an ``objective_id`` not found
        raise:  NullArgument - ``objective_id_list`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_activities_by_asset(self, asset_id):
        """Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        arg:    asset_id (osid.id.Id): ``Id`` of an ``Asset``
        return: (osid.learning.ActivityList) - list of activities
        raise:  NotFound - ``asset_id`` not found
        raise:  NullArgument - ``asset_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_activities_by_assets(self, asset_ids):
        """Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        arg:    asset_ids (osid.id.IdList): ``Ids`` of ``Assets``
        return: (osid.learning.ActivityList) - list of activities
        raise:  NotFound - an ``asset_id`` not found
        raise:  NullArgument - ``asset_id_list`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        raise errors.Unimplemented()

    def get_activities(self):
        """Gets all ``Activities``.

        In plenary mode, the returned list contains all known activites
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        return: (osid.learning.ActivityList) - a ``ActivityList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.ActivityList(result, runtime=self._runtime, proxy=self._proxy)

    activities = property(fget=get_activities)


class ActivityQuerySession(abc_learning_sessions.ActivityQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching ``Activity`` objects.

    The search query is constructed using the ``ActivityQuery``. The
    activity record ``Type`` also specifies the record for the activity
    query.

    This session defines views that offer differing behaviors for
    searching.

      * federated objective bank view: searches include activities in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      * isolated objective bank view: searches are restricted to
        activities in this objective bank


    Activities may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``ActivityQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_search_activities(self):
        """Tests if this user can perform ``Activity`` searches.

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

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_activity_query(self):
        """Gets an activity query.

        return: (osid.learning.ActivityQuery) - the activity query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.ActivityQuery(runtime=self._runtime)

    activity_query = property(fget=get_activity_query)

    @utilities.arguments_not_none
    def get_activities_by_query(self, activity_query):
        """Gets a list of ``Activities`` matching the given activity query.

        arg:    activity_query (osid.learning.ActivityQuery): the
                activity query
        return: (osid.learning.ActivityList) - the returned
                ``ActivityList``
        raise:  NullArgument - ``activity_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``activity_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in activity_query._query_terms:
            if '$in' in activity_query._query_terms[term] and '$nin' in activity_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': activity_query._query_terms[term]['$in']}},
                             {term: {'$nin': activity_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: activity_query._query_terms[term]})
        for term in activity_query._keyword_terms:
            or_list.append({term: activity_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('learning',
                                             collection='Activity',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.ActivityList(result, runtime=self._runtime, proxy=self._proxy)


class ActivityAdminSession(abc_learning_sessions.ActivityAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Activities``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Activity,`` an ``ActivityForm`` is requested using
    ``get_activity_form_for_create()`` specifying the desired objective
    and record ``Types`` or none if no record ``Types`` are needed. The
    returned ``ActivityForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``ActivityForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each ``ActivityForm``
    corresponds to an attempted transaction.

    For updates, ``ActivityForms`` are requested to the ``Activity``
    ``Id`` that is to be updated using ``getActivityFormForUpdate()``.
    Similarly, the ``ActivityForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``ActivityForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Activities``. To unmap an
    ``Activity`` from the current ``ObjectiveBank,`` the
    ``ActivityObjectiveBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Activity`` itself thus
    removing it from all known ``ObjectiveBank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_create_activities(self):
        """Tests if this user can create ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Activity`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_activity_with_record_types(self, activity_record_types):
        """Tests if this user can create a single ``Activity`` using the desired record types.

        While ``LearningManager.getActivityRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Activity``.
        Providing an empty array tests if an ``Activity`` can be created
        with no records.

        arg:    activity_record_types (osid.type.Type[]): array of
                activity record types
        return: (boolean) - ``true`` if ``Activity`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``activity_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_activity_form_for_create(self, objective_id, activity_record_types):
        """Gets the activity form for creating new activities.

        A new form should be requested for each create transaction.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        arg:    activity_record_types (osid.type.Type[]): array of
                activity record types
        return: (osid.learning.ActivityForm) - the activity form
        raise:  NotFound - ``objective_id`` is not found
        raise:  NullArgument - ``objective_id`` or
                ``activity_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template

        if not isinstance(objective_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in activity_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if activity_record_types == []:
            # WHY are we passing objective_bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.ActivityForm(
                objective_bank_id=self._catalog_id,
                objective_id=objective_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.ActivityForm(
                objective_bank_id=self._catalog_id,
                record_types=activity_record_types,
                objective_id=objective_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_activity(self, activity_form):
        """Creates a new ``Activity``.

        arg:    activity_form (osid.learning.ActivityForm): the form for
                this ``Activity``
        return: (osid.learning.Activity) - the new ``Activity``
        raise:  IllegalState - ``activity_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``activity_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``activity_form`` did not originate from
                ``get_activity_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        if not isinstance(activity_form, ABCActivityForm):
            raise errors.InvalidArgument('argument type is not an ActivityForm')
        if activity_form.is_for_update():
            raise errors.InvalidArgument('the ActivityForm is for update only, not create')
        try:
            if self._forms[activity_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('activity_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('activity_form did not originate from this session')
        if not activity_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(activity_form._my_map)

        self._forms[activity_form.get_id().get_identifier()] = CREATED
        result = objects.Activity(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_activities(self):
        """Tests if this user can update ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if activity modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_activity_form_for_update(self, activity_id):
        """Gets the activity form for updating an existing activity.

        A new activity form should be requested for each update
        transaction.

        arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        return: (osid.learning.ActivityForm) - the activity form
        raise:  NotFound - ``activity_id`` is not found
        raise:  NullArgument - ``activity_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        if not isinstance(activity_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (activity_id.get_identifier_namespace() != 'learning.Activity' or
                activity_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(activity_id.get_identifier())})

        obj_form = objects.ActivityForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_activity(self, activity_form):
        """Updates an existing activity,.

        arg:    activity_form (osid.learning.ActivityForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``activity_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``activity_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``activity_form`` did not originate from
                ``get_activity_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        if not isinstance(activity_form, ABCActivityForm):
            raise errors.InvalidArgument('argument type is not an ActivityForm')
        if not activity_form.is_for_update():
            raise errors.InvalidArgument('the ActivityForm is for update only, not create')
        try:
            if self._forms[activity_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('activity_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('activity_form did not originate from this session')
        if not activity_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(activity_form._my_map)

        self._forms[activity_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Activity(
            osid_object_map=activity_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_activities(self):
        """Tests if this user can delete ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Activity`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_activity(self, activity_id):
        """Deletes the ``Activity`` identified by the given ``Id``.

        arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
                to delete
        raise:  NotFound - an ``Activity`` was not found identified by
                the given ``Id``
        raise:  NullArgument - ``activity_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Activity',
                                         runtime=self._runtime)
        if not isinstance(activity_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        activity_map = collection.find_one(
            dict({'_id': ObjectId(activity_id.get_identifier())},
                 **self._view_filter()))

        objects.Activity(osid_object_map=activity_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(activity_id.get_identifier())})

    def can_manage_activity_aliases(self):
        """Tests if this user can manage ``Id`` aliases for activities.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Activity`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_activity(self, activity_id, alias_id):
        """Adds an ``Id`` to an ``Activity`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Activity`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another activity, it is
        reassigned to the given activity ``Id``.

        arg:    activity_id (osid.id.Id): the ``Id`` of an ``Activity``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``activity_id`` not found
        raise:  NullArgument - ``activity_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=activity_id, equivalent_id=alias_id)


class ActivityObjectiveBankSession(abc_learning_sessions.ActivityObjectiveBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Activity`` to ``ObjectiveBank`` mappings.

    An ``Activity`` may appear in multiple ``ObjectiveBanks``. Each
    ``ObjectiveBank`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'learning.ActivityObjectiveBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_activity_objective_bank_mappings(self):
        """Tests if this user can perform lookups of activity/objective bank mappings.

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

    def use_comparative_objective_bank_view(self):
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

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

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
    def get_activity_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        return: (osid.id.IdList) - list of related activity ``Ids``
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for activity in self.get_activities_by_objective_bank(objective_bank_id):
            id_list.append(activity.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_activities_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ActivityList) - list of related
                activities
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_activity_lookup_session_for_objective_bank(objective_bank_id, proxy=self._proxy)
        lookup_session.use_isolated_objective_bank_view()
        return lookup_session.get_activities()

    @utilities.arguments_not_none
    def get_activity_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        return: (osid.id.IdList) - list of activity ``Ids``
        raise:  NullArgument - ``objective_bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for activity in self.get_activities_by_objective_banks(objective_bank_ids):
            id_list.append(activity.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_activities_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        return: (osid.learning.ActivityList) - list of activities
        raise:  NullArgument - ``objective_bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        activity_list = []
        for objective_bank_id in objective_bank_ids:
            activity_list += list(
                self.get_activities_by_objective_bank(objective_bank_id))
        return objects.ActivityList(activity_list)

    @utilities.arguments_not_none
    def get_objective_bank_ids_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        arg:    activity_id (osid.id.Id): ``Id`` of a ``Activity``
        return: (osid.id.IdList) - list of objective bank ``Ids``
        raise:  NotFound - ``activity_id`` is not found
        raise:  NullArgument - ``activity_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_activity_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_objective_bank_view()
        activity = lookup_session.get_activity(activity_id)
        id_list = []
        for idstr in activity._my_map['assignedObjectiveBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_objective_banks_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        arg:    activity_id (osid.id.Id): ``Id`` of a ``Activity``
        return: (osid.learning.ObjectiveBankList) - list of objective
                bank ``Ids``
        raise:  NotFound - ``activity_id`` is not found
        raise:  NullArgument - ``activity_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bins_by_resource
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_objective_banks_by_ids(
            self.get_objective_bank_ids_by_activity(activity_id))


class ActivityObjectiveBankAssignmentSession(abc_learning_sessions.ActivityObjectiveBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Activities`` to ``ObjectiveBanks``.

    An ``Activity`` may map to multiple ``ObjectiveBanks`` and removing
    the last reference to a ``Activity`` is the equivalent of deleting
    it. Each ``ObjectiveBank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``Activity`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    _session_namespace = 'learning.ActivityObjectiveBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'ObjectiveBank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_activities(self):
        """Tests if this user can alter activity/objective bank mappings.

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
    def can_assign_activities_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if objective_bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any activity can be assigned.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        objective_banks = lookup_session.get_objective_banks()
        id_list = []
        for objective_bank in objective_banks:
            id_list.append(objective_bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_objective_bank_ids_for_activity(self, objective_bank_id, activity_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific activity can be assigned.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        raise:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_objective_bank_ids(objective_bank_id)

    @utilities.arguments_not_none
    def assign_activity_to_objective_bank(self, activity_id, objective_bank_id):
        """Adds an existing ``Activity`` to a ``ObjectiveBank``.

        arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        raise:  AlreadyExists - ``activity_id`` already mapped to
                ``objective_bank_id``
        raise:  NotFound - ``activity_id`` or ``objective_bank_id`` not
                found
        raise:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_objective_bank(objective_bank_id)  # to raise NotFound
        self._assign_object_to_catalog(activity_id, objective_bank_id)

    @utilities.arguments_not_none
    def unassign_activity_from_objective_bank(self, activity_id, objective_bank_id):
        """Removes a ``Activity`` from a ``ObjectiveBank``.

        arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        raise:  NotFound - ``activity_id`` or ``objective_bank_id`` not
                found or ``activity_id`` not mapped to
                ``objective_bank_id``
        raise:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_objective_bank(objective_bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(activity_id, objective_bank_id)

    @utilities.arguments_not_none
    def reassign_activity_to_objective_bank(self, activity_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        raise:  NotFound - ``activity_id, from_objective_bank_id,`` or
                ``to_objective_bank_id`` not found or ``activity_id``
                not mapped to ``from_objective_bank_id``
        raise:  NullArgument - ``activity_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.reassign_resource_to_bin
        self.assign_activity_to_objective_bank(activity_id, to_objective_bank_id)
        try:
            self.unassign_activity_from_objective_bank(activity_id, from_objective_bank_id)
        except:  # something went wrong, roll back assignment to to_objective_bank_id
            self.unassign_activity_from_objective_bank(activity_id, to_objective_bank_id)
            raise


class ProficiencyLookupSession(abc_learning_sessions.ProficiencyLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving proficiencies."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the obective bank
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_lookup_proficiencies(self):
        """Tests if this user can perform ``Proficiency`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.can_lookup_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_proficiency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_proficiency_view(self):
        """A complete view of the ``Proficiency`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this objective bank
        only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_effective_proficiency_view(self):
        """Only proficiencies whose effective dates are current are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_effective_relationship_view
        self._use_effective_view()

    def use_any_effective_proficiency_view(self):
        """All proficienies of any effective dates are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.use_any_effective_relationship_view
        self._use_any_effective_view()

    @utilities.arguments_not_none
    def get_proficiency(self, proficiency_id):
        """Gets the ``Proficiency`` specified by its ``Id``.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency`` to retrieve
        return: (osid.learning.Proficiency) - the returned
                ``Proficiency``
        raise:  NotFound - no ``Proficiency`` found with the given
                ``Id``
        raise:  NullArgument - ``proficiency_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(proficiency_id, 'learning').get_identifier())},
                 **self._view_filter()))
        return objects.Proficiency(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_proficiencies_by_ids(self, proficiency_ids):
        """Gets a ``ProficiencyList`` corresponding to the given ``IdList``.

        arg:    proficiency_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NotFound - an ``Id`` was not found
        raise:  NullArgument - ``proficiency_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        object_id_list = []
        for i in proficiency_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'learning').get_identifier()))
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
        return objects.ProficiencyList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type(self, proficiency_genus_type):
        """Gets a ``ProficiencyList`` corresponding to the given proficiency genus ``Type`` which does not include proficiencies of types derived from the specified ``Type``.

        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``proficiency_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(proficiency_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_proficiencies_by_parent_genus_type(self, proficiency_genus_type):
        """Gets a ``ProficiencyList`` corresponding to the given proficiency genus ``Type`` and include any additional proficiencies with genus types derived from the specified ``Type``.

        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``proficiency_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ProficiencyList([])

    @utilities.arguments_not_none
    def get_proficiencies_by_record_type(self, proficiency_record_type):
        """Gets a ``ProficiencyList`` containing the given proficiency record ``Type``.

        arg:    proficiency_record_type (osid.type.Type): a proficiency
                record type
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``proficiency_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.ProficiencyList([])

    @utilities.arguments_not_none
    def get_proficiencies_on_date(self, from_, to):
        """Gets a ``ProficiencyList`` effecyive during the entire given date range inclusive but not confined to the date range.

        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_on_date
        proficiency_list = []
        for proficiency in self.get_proficiencies():
            if overlap(from_, to, proficiency.start_date, proficiency.end_date):
                proficiency_list.append(proficiency)
        return objects.ProficiencyList(proficiency_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_on_date(self, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given proficiency genus type effective during the entire given date range inclusive but not confined to the date range.

        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``proficiency_genus_type, from,`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_proficiencies_for_objective(self, objective_id):
        """Gets a ``ProficiencyList`` relating to the given objective.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``objective_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_destination
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'objectiveId': str(objective_id)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_for_objective_on_date(self, objective_id, from_, to):
        """Gets a ``ProficiencyList`` relating to the given objective effective during the entire given date range inclusive but not confined to the date range.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``objective_id, from`` or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_destination_on_date
        proficiency_list = []
        for proficiency in self.get_proficiencies_for_objective():
            if overlap(from_, to, proficiency.start_date, proficiency.end_date):
                proficiency_list.append(proficiency)
        return objects.ProficiencyList(proficiency_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_for_objective(self, objective_id, proficiency_genus_type):
        """Gets a ``ProficiencyList`` relating to the given objective and proficiency genus ``Type``.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``objective_id`` or
                ``proficiency_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_destination
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'objectiveId': str(objective_id),
                  'genusTypeId': str(proficiency_genus_type)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_for_objective_on_date(self, objective_id, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given proficiency genus type relating to the given objective effective during the entire given date range inclusive but not confined to the date range.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``objective_id, proficiency_genus_type,
                from,`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_proficiencies_for_objectives(self, objective_ids):
        """Gets a ``ProficiencyList`` relating to the given objectives.

        arg:    objective_ids (osid.id.IdList): the objective ``Ids``
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``objective_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_destination
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'objectiveId': str(objective_ids)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_for_resource(self, resource_id):
        """Gets a ``ProficiencyList`` relating to the given resource.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'resourceId': str(resource_id)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``ProficiencyList`` relating to the given resource effective during the entire given date range inclusive but not confined to the date range.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, from`` or ``to`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date
        proficiency_list = []
        for proficiency in self.get_proficiencies_for_resource(resource_id):
            if overlap(from_, to, proficiency.start_date, proficiency.end_date):
                proficiency_list.append(proficiency)
        return objects.ProficiencyList(proficiency_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_for_resource(self, resource_id, proficiency_genus_type):
        """Gets a ``ProficiencyList`` relating to the given resource and proficiency genus ``Type``.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``resource_id`` or
                ``proficiency_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_source
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'resourceId': str(resource_id),
                  'genusTypeId': str(proficiency_genus_type)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_for_resource_on_date(self, resource_id, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given proficiency genus type relating to the given resource effective during the entire given date range inclusive but not confined to the date range.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``resource_id, proficiency_genus_type,
                from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date
        proficiency_list = []
        for proficiency in self.get_proficiencies_by_genus_type_for_resource():
            if overlap(from_, to, proficiency.start_date, proficiency.end_date):
                proficiency_list.append(proficiency)
        return objects.ProficiencyList(proficiency_list, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_for_resources(self, resource_ids):
        """Gets a ``ProficiencyList`` relating to the given resources.

        arg:    resource_ids (osid.id.IdList): the resource ``Ids``
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``resource_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'resourceId': str(resource_ids)},
                 **self._view_filter())).sort('_sort_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_for_objective_and_resource(self, objective_id, resource_id):
        """Gets a ``ProficiencyList`` relating to the given objective and resource ````.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``objective_id`` or ``resource_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'resourceId': str(objective_id),
                  'objectiveId': str(resource_id)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_for_objective_and_resource_on_date(self, objective_id, resource_id, from_, to):
        """Gets a ``ProficiencyList`` relating to the given resource and objective effective during the entire given date range inclusive but not confined to the date range.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``objective_id, resource_id, from`` or
                ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_for_objective_and_resource(self, objective_id, resource_id, proficiency_genus_type):
        """Gets a ``ProficiencyList`` of the given genus type relating to the given objective and resource ````.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  NullArgument - ``objective_id, resource_id`` or
                ``proficiency_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipLookupSession.get_relationships_by_genus_type_for_peers
        # NOTE: This implementation currently ignores plenary and effective views
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'resourceId': str(objective_id),
                  'objectiveId': str(resource_id),
                  'genusTypeId': str(proficiency_genus_type)},
                 **self._view_filter())).sort('_id', ASCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self, objective_id, resource_id, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given genus type relating to the given resource and objective effective during the entire given date range inclusive but not confined to the date range.

        arg:    objective_id (osid.id.Id): an objective ``Id``
        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    proficiency_genus_type (osid.type.Type): a proficiency
                genus type
        arg:    from (osid.calendaring.DateTime): starting date
        arg:    to (osid.calendaring.DateTime): ending date
        return: (osid.learning.ProficiencyList) - the returned
                ``Proficiency`` list
        raise:  InvalidArgument - ``from`` is greater than ``to``
        raise:  NullArgument - ``objective_id, resource_id,
                proficiency_genus_type, from`` or ``to`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_proficiencies(self):
        """Gets all ``Proficiencies``.

        return: (osid.learning.ProficiencyList) - a list of
                ``Proficiencies``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.ProficiencyList(result, runtime=self._runtime, proxy=self._proxy)

    proficiencies = property(fget=get_proficiencies)


class ProficiencyQuerySession(abc_learning_sessions.ProficiencyQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``Proficiency`` objects.

    The search query is constructed using the ``ProficiencyQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated objective bank view: searches include proficiencies in
        objective banks of which this objective bank is an ancestor in
        the obective bank hierarchy
      * isolated objective bank view: searches are restricted to
        proficiencies in this objective bank


    Proficiencies may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``ProficiencyQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the obective bank
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_search_proficiencies(self):
        """Tests if this user can perform ``Proficiency`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.can_search_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def get_proficiency_query(self):
        """Gets a proficiency query.

        return: (osid.learning.ProficiencyQuery) - the proficiency query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.ProficiencyQuery(runtime=self._runtime)

    proficiency_query = property(fget=get_proficiency_query)

    @utilities.arguments_not_none
    def get_proficiencies_by_query(self, proficiency_query):
        """Gets a list of ``Proficiencies`` matching the given proficiency query.

        arg:    proficiency_query (osid.learning.ProficiencyQuery): the
                proficiency query
        return: (osid.learning.ProficiencyList) - the returned
                ``ProficiencyList``
        raise:  NullArgument - ``proficiency_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``proficiency_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in proficiency_query._query_terms:
            if '$in' in proficiency_query._query_terms[term] and '$nin' in proficiency_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': proficiency_query._query_terms[term]['$in']}},
                             {term: {'$nin': proficiency_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: proficiency_query._query_terms[term]})
        for term in proficiency_query._keyword_terms:
            or_list.append({term: proficiency_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('learning',
                                             collection='Proficiency',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.ProficiencyList(result, runtime=self._runtime, proxy=self._proxy)


class ProficiencyAdminSession(abc_learning_sessions.ProficiencyAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Proficiencies``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Proficiency,`` a ``ProficiencyForm`` is requested using
    ``get_proficiency_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``ProficiencyForm`` will indicate
    that it is to be used with a create operation and can be used to
    examine metdata or validate data prior to creation. Once the
    ``ProficiencyForm`` is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ``ProficiencyForm`` corresponds to an attempted
    transaction.

    For updates, ``ProficiencyForms`` are requested to the
    ``Proficiency``  ``Id`` that is to be updated using
    ``getProficiencyFormForUpdate()``. Similarly, the
    ``ProficiencyForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``ProficiencyForm`` can only be used once for a successful update
    and cannot be reused.

    The delete operations delete ``Proficiencies``. To unmap a
    ``Proficiency`` from the current ``ObjectiveBank,`` the
    ``ProficiencyObjectiveBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Proficiency`` itself thus
    removing it from all known ``ObjectiveBank`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.ObjectiveBank
        self._catalog_name = 'ObjectiveBank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='learning',
            cat_name='ObjectiveBank',
            cat_class=objects.ObjectiveBank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    objective_bank_id = property(fget=get_objective_bank_id)

    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        return: (osid.learning.ObjectiveBank) - the obective bank
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    objective_bank = property(fget=get_objective_bank)

    def can_create_proficiencies(self):
        """Tests if this user can create ``Proficiencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Proficiency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Proficiency`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_proficiency_with_record_types(self, proficiency_record_types):
        """Tests if this user can create a single ``Proficiency`` using the desired record types.

        While ``LearningManager.getProficiencyRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Proficiency``. Providing an empty array tests if a
        ``Proficiency`` can be created with no records.

        arg:    proficiency_record_types (osid.type.Type[]): array of
                proficiency record types
        return: (boolean) - ``true`` if ``Proficiency`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``proficiency_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_proficiency_form_for_create(self, objective_id, resource_id, proficiency_record_types):
        """Gets the proficiency form for creating new proficiencies.

        A new form should be requested for each create transaction.

        arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        arg:    proficiency_record_types (osid.type.Type[]): array of
                proficiency record types
        return: (osid.learning.ProficiencyForm) - the proficiency form
        raise:  NotFound - ``objective_id`` or ``resource_id`` is not
                found
        raise:  NullArgument - ``objective_id, resource_id,`` or
                ``proficieny_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create
        # These really need to be in module imports:
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        from dlkit.abstract_osid.type.primitives import Type as ABCType
        if not isinstance(objective_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        if not isinstance(resource_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in proficiency_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if proficiency_record_types == []:
            # WHY are we passing objective_bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.ProficiencyForm(
                objective_bank_id=self._catalog_id,
                objective_id=objective_id,
                resource_id=resource_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.ProficiencyForm(
                objective_bank_id=self._catalog_id,
                record_types=proficiency_record_types,
                objective_id=objective_id,
                resource_id=resource_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_proficiency(self, proficiency_form):
        """Creates a new ``Proficiency``.

        A new form should be requested for each create transaction.

        arg:    proficiency_form (osid.learning.ProficiencyForm): the
                form for this ``Proficiency``
        return: (osid.learning.Proficiency) - the new ``Proficiency``
        raise:  IllegalState - ``proficiency_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``proficiency_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``proficiency_form`` did not originate
                from ``get_proficiency_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        if not isinstance(proficiency_form, ABCProficiencyForm):
            raise errors.InvalidArgument('argument type is not an ProficiencyForm')
        if proficiency_form.is_for_update():
            raise errors.InvalidArgument('the ProficiencyForm is for update only, not create')
        try:
            if self._forms[proficiency_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('proficiency_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('proficiency_form did not originate from this session')
        if not proficiency_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(proficiency_form._my_map)

        self._forms[proficiency_form.get_id().get_identifier()] = CREATED
        result = objects.Proficiency(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_proficiencies(self):
        """Tests if this user can update ``Proficiencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Proficiency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Proficiency`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_proficiency_form_for_update(self, proficiency_id):
        """Gets the proficiency form for updating an existing proficiency.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency``
        return: (osid.learning.ProficiencyForm) - the proficiency form
        raise:  NotFound - ``proficiency_id`` is not found
        raise:  NullArgument - ``proficiency_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        if not isinstance(proficiency_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (proficiency_id.get_identifier_namespace() != 'learning.Proficiency' or
                proficiency_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(proficiency_id.get_identifier())})

        obj_form = objects.ProficiencyForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_proficiency(self, proficiency_form):
        """Updates an existing proficiency.

        arg:    proficiency_form (osid.learning.ProficiencyForm): the
                form containing the elements to be updated
        raise:  IllegalState - ``proficiency_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``proficiency_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``proficiency_form`` did not originate
                from ``get_proficiency_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        if not isinstance(proficiency_form, ABCProficiencyForm):
            raise errors.InvalidArgument('argument type is not an ProficiencyForm')
        if not proficiency_form.is_for_update():
            raise errors.InvalidArgument('the ProficiencyForm is for update only, not create')
        try:
            if self._forms[proficiency_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('proficiency_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('proficiency_form did not originate from this session')
        if not proficiency_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(proficiency_form._my_map)

        self._forms[proficiency_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.Proficiency(
            osid_object_map=proficiency_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_proficiencies(self):
        """Tests if this user can delete ``Proficiencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Proficiency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Proficiency`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_proficiency(self, proficiency_id):
        """Deletes a ``Proficiency``.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency`` to remove
        raise:  NotFound - ``proficiency_id`` not found
        raise:  NullArgument - ``proficiency_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('learning',
                                         collection='Proficiency',
                                         runtime=self._runtime)
        if not isinstance(proficiency_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        proficiency_map = collection.find_one(
            dict({'_id': ObjectId(proficiency_id.get_identifier())},
                 **self._view_filter()))

        objects.Proficiency(osid_object_map=proficiency_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(proficiency_id.get_identifier())})

    def delete_proficiencies(self):
        """Deletes all proficiencies in this ``ObjectiveBank``.

        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def can_manage_proficiency_aliases(self):
        """Tests if this user can manage ``Id`` aliases for proficiency entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``Proficiency`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_proficiency(self, proficiency_id, alias_id):
        """Adds an ``Id`` to a ``Proficiency`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Proficiency`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another proficiency, it is
        reassigned to the given proficiency ``Id``.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of a
                ``Proficiency``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``proficiency_id`` not found
        raise:  NullArgument - ``proficiency_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=proficiency_id, equivalent_id=alias_id)


class ProficiencyObjectiveBankAssignmentSession(abc_learning_sessions.ProficiencyObjectiveBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Proficiencies`` to ``ObjectiveBank`` objects.

    A ``Proficiency`` may appear in multiple ``ObjectiveBank`` objects
    and removing the last reference to a ``Proficiency`` is the
    equivalent of deleting it. Each ``ObjectiveBank`` may have its own
    authorizations governing who is allowed to operate on it.

    Adding a reference of a ``Proficiency`` to another ``ObjectiveBank``
    is not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'learning.ProficiencyObjectiveBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'ObjectiveBank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_proficiencies(self):
        """Tests if this user can alter proficiency/objective bank mappings.

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
    def can_assign_proficiencies_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter proficiency/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if objective_bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank proficiency in which any proficiency can be assigned.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.id.IdList) - list of assignable objectiveBank
                ``Ids``
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        objective_banks = lookup_session.get_objective_banks()
        id_list = []
        for objective_bank in objective_banks:
            id_list.append(objective_bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_objective_bank_ids_for_proficiency(self, objective_bank_id, proficiency_id):
        """Gets a list of objective banks including and under the given objective bank proficiency in which a specific proficiency can be assigned.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency``
        return: (osid.id.IdList) - list of assignable objectiveBank
                ``Ids``
        raise:  NullArgument - ``objective_bank_id`` or
                ``proficiency_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_objective_bank_ids(objective_bank_id)

    @utilities.arguments_not_none
    def assign_proficiency_to_objective_bank(self, proficiency_id, objective_bank_id):
        """Adds an existing ``Proficiency`` to a ``ObjectiveBank``.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        raise:  AlreadyExists - ``proficiency_id`` is already mapped to
                ``objective_bank_id``
        raise:  NotFound - ``proficiency_id`` or ``objective_bank_id``
                not found
        raise:  NullArgument - ``proficiency_id`` or
                ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_objective_bank(objective_bank_id)  # to raise NotFound
        self._assign_object_to_catalog(proficiency_id, objective_bank_id)

    @utilities.arguments_not_none
    def unassign_proficiency_from_objective_bank(self, proficiency_id, objective_bank_id):
        """Removes a ``Proficiency`` from a ``ObjectiveBank``.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        raise:  NotFound - ``proficiency_id`` or ``objective_bank_id``
                not found or ``proficiency_id`` not mapped to
                ``objective_bank_id``
        raise:  NullArgument - ``proficiency_id`` or
                ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        mgr = self._get_provider_manager('LEARNING', local=True)
        lookup_session = mgr.get_objective_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_objective_bank(objective_bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(proficiency_id, objective_bank_id)

    @utilities.arguments_not_none
    def reassign_proficiency_to_objective_bank(self, proficiency_id, from_objective_bank_id, to_objective_bank_id):
        """Moves a ``Proficiency`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        arg:    proficiency_id (osid.id.Id): the ``Id`` of the
                ``Proficiency``
        arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        raise:  NotFound - ``proficiency_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` not found or
                ``proficiency_id`` not mapped to
                ``from_objective_bank_id``
        raise:  NullArgument - ``proficiency_id,
                from_objective_bank_id,`` or ``to_objective_bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.reassign_resource_to_bin
        self.assign_proficiency_to_objective_bank(proficiency_id, to_objective_bank_id)
        try:
            self.unassign_proficiency_from_objective_bank(proficiency_id, from_objective_bank_id)
        except:  # something went wrong, roll back assignment to to_objective_bank_id
            self.unassign_proficiency_from_objective_bank(proficiency_id, to_objective_bank_id)
            raise


class ObjectiveBankLookupSession(abc_learning_sessions.ObjectiveBankLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``ObjectiveBank`` objects.

    The ``ObjectiveBank`` represents a collection of ``Objectives
    Activities`` , and ``Proficiencies``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``ObjectiveBanks`` it can access, without breaking
    execution. However, an administrative application may require all
    ``ObjectiveBank`` elements to be available.

    ``ObjectiveBanks`` may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``ObjectiveBank``.

    """
    _session_namespace = 'learning.ObjectiveBankLookupSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_lookup_session()
            self._catalog_session.use_comparative_catalog_view()
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_objective_banks(self):
        """Tests if this user can perform ``ObjectiveBank`` lookups.

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

    def use_comparative_objective_bank_view(self):
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

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``ObjectiveBank`` returns is desired.

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
    def get_objective_bank(self, objective_bank_id):
        """Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ObjectiveBank) - the objective bank
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bin
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog(catalog_id=objective_bank_id)
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        # Need to consider how to best deal with the "phantom root" catalog issue
        if objective_bank_id.get_identifier() == PHANTOM_ROOT_IDENTIFIER:
            return self._get_phantom_root_catalog(cat_class=objects.ObjectiveBank, cat_name='ObjectiveBank')
        try:
            result = collection.find_one({'_id': ObjectId(self._get_id(objective_bank_id, 'learning').get_identifier())})
        except errors.NotFound:
            # Try creating an orchestrated ObjectiveBank.  Let it raise errors.NotFound()
            result = self._create_orchestrated_cat(objective_bank_id, 'learning', 'ObjectiveBank')

        return objects.ObjectiveBank(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_objective_banks_by_ids(self, objective_bank_ids):
        """Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        arg:    objective_bank_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``objective_bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        # NOTE: This implementation currently ignores plenary view
        # Also, this should be implemented to use get_ObjectiveBank() instead of direct to database
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_ids(catalog_ids=objective_bank_ids)
        catalog_id_list = []
        for i in objective_bank_ids:
            catalog_id_list.append(ObjectId(i.get_identifier()))
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        result = collection.find({'_id': {'$in': catalog_id_list}}).sort('_id', DESCENDING)

        return objects.ObjectiveBankList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_objective_banks_by_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which does not include objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        arg:    objective_bank_genus_type (osid.type.Type): an objective
                bank genus type
        return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        raise:  NullArgument - ``objective_bank_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_by_genus_type_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs_by_genus_type(catalog_genus_type=objective_bank_genus_type)
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        result = collection.find({"genusTypeId": str(objective_bank_genus_type)}).sort('_id', DESCENDING)

        return objects.ObjectiveBankList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and include any additional objective banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        arg:    objective_bank_genus_type (osid.type.Type): an objective
                bank genus type
        return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        raise:  NullArgument - ``objective_bank_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_objective_banks_by_record_type(self, objective_bank_record_type):
        """Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        arg:    objective_bank_record_type (osid.type.Type): an
                objective bank record type
        return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        raise:  NullArgument - ``objective_bank_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_objective_banks_by_provider(self, resource_id):
        """Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    def get_objective_banks(self):
        """Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        return: (osid.learning.ObjectiveBankList) - a
                ``ObjectiveBankList``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.get_bins_template
        # NOTE: This implementation currently ignores plenary view
        if self._catalog_session is not None:
            return self._catalog_session.get_catalogs()
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        result = collection.find().sort('_id', DESCENDING)

        return objects.ObjectiveBankList(result, runtime=self._runtime, proxy=self._proxy)

    objective_banks = property(fget=get_objective_banks)


class ObjectiveBankAdminSession(abc_learning_sessions.ObjectiveBankAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``ObjectiveBanks``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``ObjectiveBank,`` an ``ObjectiveBankForm`` is requested using
    ``get_objective_bank_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``ObjectiveBankForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``ObjectiveBankForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``ObjectiveBankForm`` corresponds to an attempted transaction.

    For updates, ``ObjectiveBankForms`` are requested to the
    ``ObjectiveBank``  ``Id`` that is to be updated using
    ``getObjectiveBankFormForUpdate()``. Similarly, the
    ``ObjectiveBankForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``ObjectiveBankForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``ObjectiveBanks``. It is safer to
    remove all mappings to the ``ObjectiveBank`` catalogs before
    deletion.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    _session_namespace = 'learning.ObjectiveBankAdminSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        OsidSession._init_catalog(self, proxy, runtime)
        if self._cataloging_manager is not None:
            self._catalog_session = self._cataloging_manager.get_catalog_admin_session()
        self._forms = dict()
        self._kwargs = kwargs

    def can_create_objective_banks(self):
        """Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``ObjectiveBank`` creation is
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
    def can_create_objective_bank_with_record_types(self, objective_bank_record_types):
        """Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        arg:    objective_bank_record_types (osid.type.Type[]): array of
                objective bank record types
        return: (boolean) - ``true`` if ``ObjectiveBank`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``objective_bank_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if self._catalog_session is not None:
            return self._catalog_session.can_create_catalog_with_record_types(catalog_record_types=objective_bank_record_types)
        return True

    @utilities.arguments_not_none
    def get_objective_bank_form_for_create(self, objective_bank_record_types):
        """Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        arg:    objective_bank_record_types (osid.type.Type[]): array of
                objective bank record types
        return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        raise:  NullArgument - ``objective_bank_record_types`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types.
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_create(catalog_record_types=objective_bank_record_types)
        for arg in objective_bank_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if objective_bank_record_types == []:
            result = objects.ObjectiveBankForm(
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        else:
            result = objects.ObjectiveBankForm(
                record_types=objective_bank_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy)  # Probably don't need effective agent id now that we have proxy in form.
        self._forms[result.get_id().get_identifier()] = not CREATED
        return result

    @utilities.arguments_not_none
    def create_objective_bank(self, objective_bank_form):
        """Creates a new ``ObjectiveBank``.

        arg:    objective_bank_form (osid.learning.ObjectiveBankForm):
                the form for this ``ObjectiveBank``
        return: (osid.learning.ObjectiveBank) - the new
                ``ObjectiveBank``
        raise:  IllegalState - ``objective_bank_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``objective_bank_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``objective_bank_form`` did not originate
                from ``get_objective_bank_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.create_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.create_catalog(catalog_form=objective_bank_form)
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        if not isinstance(objective_bank_form, ABCObjectiveBankForm):
            raise errors.InvalidArgument('argument type is not an ObjectiveBankForm')
        if objective_bank_form.is_for_update():
            raise errors.InvalidArgument('the ObjectiveBankForm is for update only, not create')
        try:
            if self._forms[objective_bank_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('objective_bank_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('objective_bank_form did not originate from this session')
        if not objective_bank_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(objective_bank_form._my_map)

        self._forms[objective_bank_form.get_id().get_identifier()] = CREATED
        result = objects.ObjectiveBank(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_objective_banks(self):
        """Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        return: (boolean) - ``false`` if ``ObjectiveBank`` modification
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
    def get_objective_bank_form_for_update(self, objective_bank_id):
        """Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_form_for_update(catalog_id=objective_bank_id)
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        if not isinstance(objective_bank_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        result = collection.find_one({'_id': ObjectId(objective_bank_id.get_identifier())})

        cat_form = objects.ObjectiveBankForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[cat_form.get_id().get_identifier()] = not UPDATED

        return cat_form

    @utilities.arguments_not_none
    def update_objective_bank(self, objective_bank_form):
        """Updates an existing objective bank.

        arg:    objective_bank_form (osid.learning.ObjectiveBankForm):
                the form containing the elements to be updated
        raise:  IllegalState - ``objective_bank_form`` already used in
                an update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``objective_bank_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``objective_bank_form did not originate
                from get_objective_bank_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.update_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.update_catalog(catalog_form=objective_bank_form)
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        if not isinstance(objective_bank_form, ABCObjectiveBankForm):
            raise errors.InvalidArgument('argument type is not an ObjectiveBankForm')
        if not objective_bank_form.is_for_update():
            raise errors.InvalidArgument('the ObjectiveBankForm is for update only, not create')
        try:
            if self._forms[objective_bank_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('objective_bank_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('objective_bank_form did not originate from this session')
        if not objective_bank_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(objective_bank_form._my_map)  # save is deprecated - change to replace_one

        self._forms[objective_bank_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned
        return objects.ObjectiveBank(osid_object_map=objective_bank_form._my_map, runtime=self._runtime, proxy=self._proxy)

    def can_delete_objective_banks(self):
        """Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        return: (boolean) - ``false`` if ``ObjectiveBank`` deletion is
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
    def delete_objective_bank(self, objective_bank_id):
        """Deletes an ``ObjectiveBank``.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank`` to remove
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinAdminSession.delete_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.delete_catalog(catalog_id=objective_bank_id)
        collection = JSONClientValidated('learning',
                                         collection='ObjectiveBank',
                                         runtime=self._runtime)
        if not isinstance(objective_bank_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        for object_catalog in ['Objective', 'Activity', 'Proficiency', 'ObjectiveBank']:
            obj_collection = JSONClientValidated('learning',
                                                 collection=object_catalog,
                                                 runtime=self._runtime)
            if obj_collection.find({'assignedObjectiveBankIds': {'$in': [str(objective_bank_id)]}}).count() != 0:
                raise errors.IllegalState('catalog is not empty')
        collection.delete_one({'_id': ObjectId(objective_bank_id.get_identifier())})

    def can_manage_objective_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``ObjectiveBank`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_objective_bank(self, objective_bank_id, alias_id):
        """Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                ``ObjectiveBank``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.alias_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.alias_catalog(catalog_id=objective_bank_id, alias_id=alias_id)
        self._alias_id(primary_id=objective_bank_id, equivalent_id=alias_id)


class ObjectiveBankHierarchySession(abc_learning_sessions.ObjectiveBankHierarchySession, osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``ObjectiveBank`` objects.

    Each node in the hierarchy is a unique ``ObjectiveBank``. The
    hierarchy may be traversed recursively to establish the tree
    structure through ``get_parent_objective_banks()`` and
    ``getChildObjectiveBanks()``. To relate these ``Ids`` to another
    OSID, ``get_objective_bank_nodes()`` can be used for retrievals that
    can be used for bulk lookups in other OSIDs. Any ``ObjectiveBank``
    available in the ObjectiveBanking OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_objective_banks()`` or
    ``get_child_objective_banks()`` in lieu of a ``PermissionDenied``
    error that may disrupt the traversal through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: objective bank elements may be silently
        omitted or re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    _session_namespace = 'learning.ObjectiveBankHierarchySession'

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
                Id(authority='LEARNING',
                   namespace='CATALOG',
                   identifier='OBJECTIVEBANK'),
                proxy=self._proxy)

    def get_objective_bank_hierarchy_id(self):
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

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
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

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_access_objective_bank_hierarchy(self):
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

    def use_comparative_objective_bank_view(self):
        """The returns from the objective bank methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinLookupSession.use_comparative_bin_view
        self._catalog_view = COMPARATIVE
        if self._catalog_session is not None:
            self._catalog_session.use_comparative_catalog_view()

    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

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

    def get_root_objective_bank_ids(self):
        """Gets the root objective bank ``Ids`` in this hierarchy.

        return: (osid.id.IdList) - the root objective bank ``Ids``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalog_ids()
        return self._hierarchy_session.get_roots()

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    def get_root_objective_banks(self):
        """Gets the root objective banks in this objective bank hierarchy.

        return: (osid.learning.ObjectiveBankList) - the root objective
                banks
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_root_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_root_catalogs()
        return ObjectiveBankLookupSession(
            self._proxy,
            self._runtime).get_objective_banks_by_ids(list(self.get_root_objective_bank_ids()))

    root_objective_banks = property(fget=get_root_objective_banks)

    @utilities.arguments_not_none
    def has_parent_objective_banks(self, objective_bank_id):
        """Tests if the ``ObjectiveBank`` has any parents.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (boolean) - ``true`` if the objective bank has parents,
                ``false`` otherwise
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_parent_catalogs(catalog_id=objective_bank_id)
        return self._hierarchy_session.has_parents(id_=objective_bank_id)

    @utilities.arguments_not_none
    def is_parent_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a direct parent of an objective bank.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (boolean) - ``true`` if this ``id`` is a parent of
                ``objective_bank_id,``  ``false`` otherwise
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_parent_of_catalog(id_=id_, catalog_id=objective_bank_id)
        return self._hierarchy_session.is_parent(id_=objective_bank_id, parent_id=id_)

    @utilities.arguments_not_none
    def get_parent_objective_bank_ids(self, objective_bank_id):
        """Gets the parent ``Ids`` of the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (osid.id.IdList) - the parent ``Ids`` of the objective
                bank
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalog_ids(catalog_id=objective_bank_id)
        return self._hierarchy_session.get_parents(id_=objective_bank_id)

    @utilities.arguments_not_none
    def get_parent_objective_banks(self, objective_bank_id):
        """Gets the parents of the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (osid.learning.ObjectiveBankList) - the parents of the
                objective bank
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_parent_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_parent_catalogs(catalog_id=objective_bank_id)
        return ObjectiveBankLookupSession(
            self._proxy,
            self._runtime).get_objective_banks_by_ids(
                list(self.get_parent_objective_bank_ids(objective_bank_id)))

    @utilities.arguments_not_none
    def is_ancestor_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is an ancestor of an objective bank.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``objective_bank_id,`` ``false`` otherwise
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_ancestor_of_catalog(id_=id_, catalog_id=objective_bank_id)
        return self._hierarchy_session.is_ancestor(id_=id_, ancestor_id=objective_bank_id)

    @utilities.arguments_not_none
    def has_child_objective_banks(self, objective_bank_id):
        """Tests if an objective bank has any children.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (boolean) - ``true`` if the ``objective_bank_id`` has
                children, ``false`` otherwise
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.has_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.has_child_catalogs(catalog_id=objective_bank_id)
        return self._hierarchy_session.has_children(id_=objective_bank_id)

    @utilities.arguments_not_none
    def is_child_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an objective bank is a direct child of another.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (boolean) - ``true`` if the ``id`` is a child of
                ``objective_bank_id,``  ``false`` otherwise
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_child_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_child_of_catalog(id_=id_, catalog_id=objective_bank_id)
        return self._hierarchy_session.is_child(id_=objective_bank_id, child_id=id_)

    @utilities.arguments_not_none
    def get_child_objective_bank_ids(self, objective_bank_id):
        """Gets the child ``Ids`` of the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the objective bank
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalog_ids(catalog_id=objective_bank_id)
        return self._hierarchy_session.get_children(id_=objective_bank_id)

    @utilities.arguments_not_none
    def get_child_objective_banks(self, objective_bank_id):
        """Gets the children of the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        return: (osid.learning.ObjectiveBankList) - the children of the
                objective bank
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_child_bins
        if self._catalog_session is not None:
            return self._catalog_session.get_child_catalogs(catalog_id=objective_bank_id)
        return ObjectiveBankLookupSession(
            self._proxy,
            self._runtime).get_objective_banks_by_ids(
                list(self.get_child_objective_bank_ids(objective_bank_id)))

    @utilities.arguments_not_none
    def is_descendant_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a descendant of an objective bank.

        arg:    id (osid.id.Id): an ``Id``
        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``objective_bank_id,`` ``false`` otherwise
        raise:  NotFound - ``objective_bank_id`` is not found
        raise:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if self._catalog_session is not None:
            return self._catalog_session.is_descendant_of_catalog(id_=id_, catalog_id=objective_bank_id)
        return self._hierarchy_session.is_descendant(id_=id_, descendant_id=objective_bank_id)

    @utilities.arguments_not_none
    def get_objective_bank_node_ids(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
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
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if self._catalog_session is not None:
            return self._catalog_session.get_catalog_node_ids(
                catalog_id=objective_bank_id,
                ancestor_levels=ancestor_levels,
                descendant_levels=descendant_levels,
                include_siblings=include_siblings)
        return self._hierarchy_session.get_nodes(
            id_=objective_bank_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)

    @utilities.arguments_not_none
    def get_objective_bank_nodes(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.learning.ObjectiveBankNode) - an objective bank
                node
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchySession.get_bin_nodes
        return objects.ObjectiveBankNode(self.get_objective_bank_node_ids(
            objective_bank_id=objective_bank_id,
            ancestor_levels=ancestor_levels,
            descendant_levels=descendant_levels,
            include_siblings=include_siblings)._my_map, runtime=self._runtime, proxy=self._proxy)


class ObjectiveBankHierarchyDesignSession(abc_learning_sessions.ObjectiveBankHierarchyDesignSession, osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``ObjectiveBank`` objects.

    Each node in the hierarchy is a unique ``ObjectiveBank``.

    """
    _session_namespace = 'learning.ObjectiveBankHierarchyDesignSession'

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
                Id(authority='LEARNING',
                   namespace='CATALOG',
                   identifier='OBJECTIVEBANK'),
                proxy=self._proxy)

    def get_objective_bank_hierarchy_id(self):
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

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    def get_objective_bank_hierarchy(self):
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

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    def can_modify_objective_bank_hierarchy(self):
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
    def add_root_objective_bank(self, objective_bank_id):
        """Adds a root objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        raise:  AlreadyExists - ``objective_bank_id`` is already in
                hierarchy
        raise:  NotFound - ``objective_bank_id`` not found
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_root_catalog(catalog_id=objective_bank_id)
        return self._hierarchy_session.add_root(id_=objective_bank_id)

    @utilities.arguments_not_none
    def remove_root_objective_bank(self, objective_bank_id):
        """Removes a root objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        raise:  NotFound - ``objective_bank_id`` is not a root
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_root_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_root_catalog(catalog_id=objective_bank_id)
        return self._hierarchy_session.remove_root(id_=objective_bank_id)

    @utilities.arguments_not_none
    def add_child_objective_bank(self, objective_bank_id, child_id):
        """Adds a child to an objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``objective_bank_id`` is already a
                parent of ``child_id``
        raise:  NotFound - ``objective_bank_id`` or ``child_id`` not
                found
        raise:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.add_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.add_child_catalog(catalog_id=objective_bank_id, child_id=child_id)
        return self._hierarchy_session.add_child(id_=objective_bank_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_objective_bank(self, objective_bank_id, child_id):
        """Removes a child from an objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        arg:    child_id (osid.id.Id): the ``Id`` of the child
        raise:  NotFound - ``objective_bank_id`` not a parent of
                ``child_id``
        raise:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalog(catalog_id=objective_bank_id, child_id=child_id)
        return self._hierarchy_session.remove_child(id_=objective_bank_id, child_id=child_id)

    @utilities.arguments_not_none
    def remove_child_objective_banks(self, objective_bank_id):
        """Removes all children from an objective bank.

        arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        raise:  NotFound - ``objective_bank_id`` not in hierarchy
        raise:  NullArgument - ``objective_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.BinHierarchyDesignSession.remove_child_bin_template
        if self._catalog_session is not None:
            return self._catalog_session.remove_child_catalogs(catalog_id=objective_bank_id)
        return self._hierarchy_session.remove_children(id_=objective_bank_id)
