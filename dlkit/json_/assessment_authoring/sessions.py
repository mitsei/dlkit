"""JSON implementations of assessment.authoring sessions."""

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
from ..list_utilities import move_id_ahead, move_id_behind, order_ids
from ..osid import sessions as osid_sessions
from ..osid.sessions import OsidSession
from ..primitives import Id
from ..primitives import Type
from ..utilities import JSONClientValidated
from ..utilities import PHANTOM_ROOT_IDENTIFIER
from dlkit.abstract_osid.assessment_authoring import sessions as abc_assessment_authoring_sessions
from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartForm as ABCAssessmentPartForm
from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleForm as ABCSequenceRuleForm
from dlkit.abstract_osid.id.primitives import Id as ABCId
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.primitives import Type as ABCType
from dlkit.json_.assessment.assessment_utilities import get_assessment_part_lookup_session
from dlkit.primordium.id.primitives import Id


DESCENDING = -1
ASCENDING = 1
CREATED = True
UPDATED = True
ACTIVE = 0
ANY_STATUS = 1
SEQUESTERED = 0
UNSEQUESTERED = 1
ENCLOSURE_RECORD_TYPE = Type(
    identifier='enclosure',
    namespace='osid-object',
    authority='ODL.MIT.EDU')
COMPARATIVE = 0
PLENARY = 1
ISOLATED = 1


class AssessmentPartLookupSession(abc_assessment_authoring_sessions.AssessmentPartLookupSession, osid_sessions.OsidSession):
    """This session defines methods for retrieving assessment parts."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs
        self._status_view = ACTIVE
        self._sequestered_view = SEQUESTERED

    def _view_filter(self):
        """
        Overrides OsidSession._view_filter to add sequestering filter.

        """
        view_filter = OsidSession._view_filter(self)
        if self._sequestered_view == SEQUESTERED:
            view_filter['sequestered'] = False
        return view_filter

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_lookup_assessment_parts(self):
        """Tests if this user can perform ``AssessmentPart`` lookups.

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

    def use_comparative_assessment_part_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_assessment_part_view(self):
        """A complete view of the ``AssessmentPart`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment parts in catalogs which
        are children of this catalog in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_active_assessment_part_view(self):
        """Only active assessment parts are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_active_composition_view_template
        self._status_view = ACTIVE

    def use_any_status_assessment_part_view(self):
        """All active and inactive assessment parts are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_any_status_composition_view_template
        self._status_view = ANY_STATUS

    def use_sequestered_assessment_part_view(self):
        """The methods in this session omit sequestered assessment parts.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_sequestered_composition_view_template
        self._sequestered_view = SEQUESTERED

    def use_unsequestered_assessment_part_view(self):
        """The methods in this session return all assessment parts, including sequestered assessment parts.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_unsequestered_composition_view_template
        self._sequestered_view = UNSEQUESTERED

    @utilities.arguments_not_none
    def get_assessment_part(self, assessment_part_id):
        """Gets the ``AssessmentPart`` specified by its ``Id``.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart`` to retrieve
        return: (osid.assessment.authoring.AssessmentPart) - the
                returned ``AssessmentPart``
        raise:  NotFound - no ``AssessmentPart`` found with the given
                ``Id``
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(assessment_part_id, 'assessment_authoring').get_identifier())},
                 **self._view_filter()))
        return objects.AssessmentPart(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessment_parts_by_ids(self, assessment_part_ids):
        """Gets an ``AssessmentPartList`` corresponding to the given ``IdList``.

        arg:    assessment_part_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``assessment_part_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        object_id_list = []
        for i in assessment_part_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'assessment_authoring').get_identifier()))
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
        return objects.AssessmentPartList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessment_parts_by_genus_type(self, assessment_part_genus_type):
        """Gets an ``AssessmentPartList`` corresponding to the given assessment part genus ``Type`` which does not include assessment parts of types derived from the specified ``Type``.

        arg:    assessment_part_genus_type (osid.type.Type): an
                assessment part genus type
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NullArgument - ``assessment_part_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(assessment_part_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentPartList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_assessment_parts_by_parent_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentPartList`` corresponding to the given assessment part genus ``Type`` and include any additional assessment parts with genus types derived from the specified ``Type``.

        arg:    assessment_genus_type (osid.type.Type): an assessment
                part genus type
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NullArgument - ``assessment_part_genus_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentPartList([])

    @utilities.arguments_not_none
    def get_assessment_parts_by_record_type(self, assessment_part_record_type):
        """Gets an ``AssessmentPart`` containing the given assessment part record ``Type``.

        arg:    assessment_part_record_type (osid.type.Type): an
                assessment part record type
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NullArgument - ``assessment_part_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.AssessmentPartList([])

    @utilities.arguments_not_none
    def get_assessment_parts_for_assessment(self, assessment_id):
        """Gets an ``AssessmentPart`` for the given assessment.

        arg:    assessment_id (osid.id.Id): an assessment ``Id``
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentId': str(assessment_id)},
                 **self._view_filter()))
        return objects.AssessmentPartList(result, runtime=self._runtime)

    def get_assessment_parts(self):
        """Gets all ``AssessmentParts``.

        return: (osid.assessment.authoring.AssessmentPartList) - a list
                of ``AssessmentParts``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.AssessmentPartList(result, runtime=self._runtime, proxy=self._proxy)

    assessment_parts = property(fget=get_assessment_parts)

    @utilities.arguments_not_none
    def get_assessment_parts_for_assessment_part(self, assessment_part_id):
        """Gets an ``AssessmentPart`` for the given assessment part.

        arg:    assessment_part_id (osid.id.Id): an assessment part ``Id``
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOT IN SPEC - Implemented from
        # osid.assessment_authoring.AssessmentPartLookupSession.additional_methods
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentPartId': str(assessment_part_id)},
                 **self._view_filter()))
        return objects.AssessmentPartList(result, runtime=self._runtime)


class AssessmentPartQuerySession(abc_assessment_authoring_sessions.AssessmentPartQuerySession, osid_sessions.OsidSession):
    """This session provides methods for searching among ``AssessmentPart`` objects.

    The search query is constructed using the ``AssessmentPartQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessment parts in bank
        of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessment parts
        in this bank
      * sequestered assessment part viiew: All assessment part methods
        suppress sequestered assessment parts.
      * unsequestered assessment part view: All assessment part methods
        return all assessment parts.


    Assessment parts may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``AssessmentPartQuery``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs
        self._status_view = ACTIVE
        self._sequestered_view = SEQUESTERED

    def _view_filter(self):
        """
        Overrides OsidSession._view_filter to add sequestering filter.

        """
        view_filter = OsidSession._view_filter(self)
        if self._sequestered_view == SEQUESTERED:
            view_filter['sequestered'] = False
        return view_filter

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the bank
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_search_assessment_parts(self):
        """Tests if this user can perform ``AssessmentPart`` lookups.

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

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment part in banks which are
        children of this step in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_sequestered_assessment_part_view(self):
        """The methods in this session omit sequestered assessment parts.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_sequestered_composition_view_template
        self._sequestered_view = SEQUESTERED

    def use_unsequestered_assessment_part_view(self):
        """The methods in this session return all assessment parts, including sequestered assessment parts.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_unsequestered_composition_view_template
        self._sequestered_view = UNSEQUESTERED

    def get_assessment_part_query(self):
        """Gets an assessment part query.

        return: (osid.assessment.authoring.AssessmentPartQuery) - the
                assessment part query
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resource_query_template
        return queries.AssessmentPartQuery(runtime=self._runtime)

    assessment_part_query = property(fget=get_assessment_part_query)

    @utilities.arguments_not_none
    def get_assessment_parts_by_query(self, assessment_part_query):
        """Gets a list of ``AssessmentParts`` matching the given assessment part query.

        arg:    assessment_part_query
                (osid.assessment.authoring.AssessmentPartQuery): the
                assessment part query
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPartList``
        raise:  NullArgument - ``assessment_part_query`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``assessment_part_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceQuerySession.get_resources_by_query
        and_list = list()
        or_list = list()
        for term in assessment_part_query._query_terms:
            if '$in' in assessment_part_query._query_terms[term] and '$nin' in assessment_part_query._query_terms[term]:
                and_list.append(
                    {'$or': [{term: {'$in': assessment_part_query._query_terms[term]['$in']}},
                             {term: {'$nin': assessment_part_query._query_terms[term]['$nin']}}]})
            else:
                and_list.append({term: assessment_part_query._query_terms[term]})
        for term in assessment_part_query._keyword_terms:
            or_list.append({term: assessment_part_query._keyword_terms[term]})
        if or_list:
            and_list.append({'$or': or_list})
        view_filter = self._view_filter()
        if view_filter:
            and_list.append(view_filter)
        if and_list:
            query_terms = {'$and': and_list}
            collection = JSONClientValidated('assessment_authoring',
                                             collection='AssessmentPart',
                                             runtime=self._runtime)
            result = collection.find(query_terms).sort('_id', DESCENDING)
        else:
            result = []
        return objects.AssessmentPartList(result, runtime=self._runtime, proxy=self._proxy)


class AssessmentPartAdminSession(abc_assessment_authoring_sessions.AssessmentPartAdminSession, osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``AssessmentParts``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``AssessmentPart,`` an ``AssessmentPartForm`` is requested using
    ``get_assessment_part_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``AssessmentPartForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``AssessmentPartForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``AssessmentPartForm`` corresponds to an attempted transaction.

    For updates, ``AssessmentPartForms`` are requested to the
    ``AssessmentPart``  ``Id`` that is to be updated using
    ``getAssessmentPartFormForUpdate()``. Similarly, the
    ``AssessmentPartForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AssessmentPartForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``AssessmentParts``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_create_assessment_parts(self):
        """Tests if this user can create assessment parts.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to unauthorized users.

        return: (boolean) - ``false`` if ``AssessmentPart`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_assessment_part_with_record_types(self, assessment_part_record_types):
        """Tests if this user can create a single ``AssessmentPart`` using the desired record types.

        While
        ``AssessmentAuthoringManager.getAssessmentPartRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentPart``. Providing an empty array tests if an
        ``AssessmentPart`` can be created with no records.

        arg:    assessment_part_record_types (osid.type.Type[]): array
                of assessment part record types
        return: (boolean) - ``true`` if ``AssessmentPart`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``assessment_part_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_part_form_for_create_for_assessment(self, assessment_id, assessment_part_record_types):
        """Gets the assessment part form for creating new assessment parts for an assessment.

        A new form should be requested for each create transaction.

        arg:    assessment_id (osid.id.Id): an assessment ``Id``
        arg:    assessment_part_record_types (osid.type.Type[]): array
                of assessment part record types to be included in the
                create operation or an empty list if none
        return: (osid.assessment.authoring.AssessmentPartForm) - the
                assessment part form
        raise:  NotFound - ``assessment_id`` is not found
        raise:  NullArgument - ``assessment_id`` or
                ``assessment_part_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template

        if not isinstance(assessment_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in assessment_part_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if assessment_part_record_types == []:
            # WHY are we passing bank_id = self._catalog_id below, seems redundant:
            obj_form = objects.AssessmentPartForm(
                bank_id=self._catalog_id,
                assessment_id=assessment_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        else:
            obj_form = objects.AssessmentPartForm(
                bank_id=self._catalog_id,
                record_types=assessment_part_record_types,
                assessment_id=assessment_id,
                catalog_id=self._catalog_id,
                runtime=self._runtime,
                proxy=self._proxy)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    @utilities.handle_simple_sequencing
    def create_assessment_part_for_assessment(self, assessment_part_form):
        """Creates a new assessment part.

        arg:    assessment_part_form
                (osid.assessment.authoring.AssessmentPartForm):
                assessment part form
        return: (osid.assessment.authoring.AssessmentPart) - the new
                part
        raise:  IllegalState - ``assessment_part_form`` already used in
                a create transaction
        raise:  InvalidArgument - ``assessment_part_form`` is invalid
        raise:  NullArgument - ``assessment_part_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_part_form`` did not originate
                from
                ``get_assessment_part_form_for_create_for_assessment()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if not isinstance(assessment_part_form, ABCAssessmentPartForm):
            raise errors.InvalidArgument('argument type is not an AssessmentPartForm')
        if assessment_part_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentPartForm is for update only, not create')
        try:
            if self._forms[assessment_part_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('assessment_part_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('assessment_part_form did not originate from this session')
        if not assessment_part_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(assessment_part_form._my_map)

        self._forms[assessment_part_form.get_id().get_identifier()] = CREATED
        result = objects.AssessmentPart(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    @utilities.arguments_not_none
    def get_assessment_part_form_for_create_for_assessment_part(self, assessment_part_id, assessment_part_record_types):
        """Gets the assessment part form for creating new assessment parts under another assessment part.

        A new form should be requested for each create transaction.

        arg:    assessment_part_id (osid.id.Id): an assessment part
                ``Id``
        arg:    assessment_part_record_types (osid.type.Type[]): array
                of assessment part record types to be included in the
                create operation or an empty list if none
        return: (osid.assessment.authoring.AssessmentPartForm) - the
                assessment part form
        raise:  NotFound - ``assessment_part_id`` is not found
        raise:  NullArgument - ``assessment_part_id`` or
                ``assessment_part_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(assessment_part_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in assessment_part_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if assessment_part_record_types == []:
            assessment_part_record_types = None
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session_for_bank(self._catalog_id, proxy=self._proxy)
        child_parts = lookup_session.get_assessment_parts_for_assessment_part(assessment_part_id)
        mdata = {}
        # Check for underlying Parts, whether Sections and set appropriate mdata overrides:
        if child_parts.available == 0:
            pass
        else:
            mdata['sequestered'] = {}
            mdata['sequestered']['is_read_only'] = True
            mdata['sequestered']['is_required'] = True
            if child_parts.available() > 0 and child_parts.next().is_section():
                mdata['sequestered']['default_boolean_values'] = [False]
            else:
                mdata['sequestered']['default_boolean_values'] = [True]
        # WHY are we passing bank_id = self._catalog_id below, seems redundant:
        obj_form = objects.AssessmentPartForm(
            bank_id=self._catalog_id,
            record_types=assessment_part_record_types,
            assessment_part_id=assessment_part_id,
            catalog_id=self._catalog_id,
            runtime=self._runtime,
            mdata=mdata)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    @utilities.handle_simple_sequencing
    def create_assessment_part_for_assessment_part(self, assessment_part_form):
        """Creates a new assessment part.

        arg:    assessment_part_form
                (osid.assessment.authoring.AssessmentPartForm):
                assessment part form
        return: (osid.assessment.authoring.AssessmentPart) - the new
                part
        raise:  IllegalState - ``assessment_part_form`` already used in
                a create transaction
        raise:  InvalidArgument - ``assessment_part_form`` is invalid
        raise:  NullArgument - ``assessment_part_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_part_form`` did not originate
                from ``get_assessment_part_form_for_create_for_assessmen
                t_part()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if not isinstance(assessment_part_form, ABCAssessmentPartForm):
            raise errors.InvalidArgument('argument type is not an AssessmentPartForm')
        if assessment_part_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentPartForm is for update only, not create')
        try:
            if self._forms[assessment_part_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('assessment_part_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('assessment_part_form did not originate from this session')
        if not assessment_part_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(assessment_part_form._my_map)

        self._forms[assessment_part_form.get_id().get_identifier()] = CREATED
        result = objects.AssessmentPart(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_assessment_parts(self):
        """Tests if this user can update ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentPart`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        return: (boolean) - ``false`` if assessment part modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_assessment_part_form_for_update(self, assessment_part_id):
        """Gets the assessment part form for updating an existing assessment part.

        A new assessment part form should be requested for each update
        transaction.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        return: (osid.assessment.authoring.AssessmentPartForm) - the
                assessment part form
        raise:  NotFound - ``assessment_part_id`` is not found
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if not isinstance(assessment_part_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart' or
                assessment_part_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(assessment_part_id.get_identifier())})

        mdata = {}
        if not result['assessmentPartId']:
            pass
        else:
            parent_part_id = Id(result['assessmentPartId'])
            mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
            lookup_session = mgr.get_assessment_part_lookup_session_for_bank(self._catalog_id, proxy=self._proxy)
            if lookup_session.get_assessment_parts_for_assessment_part(parent_part_id).available() > 1:
                mdata['sequestered']['is_read_only'] = True
                mdata['sequestered']['is_required'] = True
        obj_form = objects.AssessmentPartForm(osid_object_map=result,
                                              runtime=self._runtime,
                                              proxy=self._proxy,
                                              mdata=mdata)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_assessment_part(self, assessment_part_id, assessment_part_form):
        """Updates an existing assessment part.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        arg:    assessment_part_form
                (osid.assessment.authoring.AssessmentPartForm): part
                form
        raise:  NotFound - ``assessment_part_id`` not found
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        raise:  Unsupported - ``assessment_part_form`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if not isinstance(assessment_part_form, ABCAssessmentPartForm):
            raise errors.InvalidArgument('argument type is not an AssessmentPartForm')
        if not assessment_part_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentPartForm is for update only, not create')
        try:
            if self._forms[assessment_part_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('assessment_part_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('assessment_part_form did not originate from this session')
        if not assessment_part_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(assessment_part_form._my_map)

        self._forms[assessment_part_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.AssessmentPart(
            osid_object_map=assessment_part_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_assessment_parts(self):
        """Tests if this user can delete ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentPart`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentPart`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    @utilities.handle_simple_sequencing
    def delete_assessment_part(self, assessment_part_id):
        """Removes an asessment part and all mapped items.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        raise:  NotFound - ``assessment_part_id`` not found
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure occurred
        *compliance: mandatory -- This method must be implemented.*

        """
        # Should be implemented from template for
        # osid.learning.ObjectiveAdminSession.delete_objective_template
        # but need to handle magic part delete ...

        if not isinstance(assessment_part_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if collection.find({'assessmentPartId': str(assessment_part_id)}).count() != 0:
            raise errors.IllegalState('there are still AssessmentParts associated with this AssessmentPart')

        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        try:
            apls = get_assessment_part_lookup_session(runtime=self._runtime,
                                                      proxy=self._proxy)
            apls.use_unsequestered_assessment_part_view()
            apls.use_federated_bank_view()
            part = apls.get_assessment_part(assessment_part_id)
            part.delete()
        except AttributeError:
            collection.delete_one({'_id': ObjectId(assessment_part_id.get_identifier())})

    def can_manage_assessment_part_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``AssessmentPart`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_assessment_part(self, assessment_part_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentPart`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentPart`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment part, it is
        reassigned to the given assessment part ``Id``.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of an
                ``AssessmentPart``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        raise:  NotFound - ``assessment_part_id`` not found
        raise:  NullArgument - ``assessment_part_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=assessment_part_id, equivalent_id=alias_id)


class AssessmentPartBankSession(abc_assessment_authoring_sessions.AssessmentPartBankSession, osid_sessions.OsidSession):
    """This session provides methods to retrieve ``AssessmentPart`` to ``Bank`` mappings.

    an ``AssessmentPart`` may appear in multiple ``Bank`` objects. Each
    bank may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    _session_namespace = 'assessment_authoring.AssessmentPartBankSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_view = COMPARATIVE
        self._kwargs = kwargs

    def can_lookup_assessment_part_bank_mappings(self):
        """Tests if this user can perform lookups of assessment part/bank mappings.

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

    def use_comparative_assessment_part_bank_view(self):
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

    def use_plenary_assessment_part_bank_view(self):
        """A complete view of the ``AssessmentPart`` and ``Bank`` returns is desired.

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
    def get_assessment_part_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentPartIds`` associated with an ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of related assessment part
                ``Ids``
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        id_list = []
        for assessment_part in self.get_assessment_parts_by_bank(bank_id):
            id_list.append(assessment_part.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessment_parts_by_bank(self, bank_id):
        """Gets the list of assessment parts associated with an ``Bank``.

        arg:    bank_id (osid.id.Id): ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartList) - list of
                related assessment parts
        raise:  NotFound - ``bank_id`` is not found
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bin
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session_for_bank(bank_id, proxy=self._proxy)
        lookup_session.use_isolated_bank_view()
        return lookup_session.get_assessment_parts()

    @utilities.arguments_not_none
    def get_assessment_part_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentPart Ids`` corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.id.IdList) - list of assessment part ``Ids``
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        id_list = []
        for assessment_part in self.get_assessment_parts_by_banks(bank_ids):
            id_list.append(assessment_part.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assessment_parts_by_banks(self, bank_ids):
        """Gets the list of assessment part corresponding to a list of ``Banks``.

        arg:    bank_ids (osid.id.IdList): list of bank ``Ids``
        return: (osid.assessment.authoring.AssessmentPartList) - list of
                assessment parts
        raise:  NullArgument - ``bank_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_resources_by_bins
        assessment_part_list = []
        for bank_id in bank_ids:
            assessment_part_list += list(
                self.get_assessment_parts_by_bank(bank_id))
        return objects.AssessmentPartList(assessment_part_list)

    @utilities.arguments_not_none
    def get_bank_ids_by_assessment_part(self, assessment_part_id):
        """Gets the ``Bank``  ``Ids`` mapped to an ``AssessmentPart``.

        arg:    assessment_part_id (osid.id.Id): ``Id`` of an
                ``AssessmentPart``
        return: (osid.id.IdList) - list of banks
        raise:  NotFound - ``assessment_part_id`` is not found
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        assessment_part = lookup_session.get_assessment_part(assessment_part_id)
        id_list = []
        for idstr in assessment_part._my_map['assignedBankIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_banks_by_assessment_part(self, assessment_part_id):
        """Gets the ``Banks`` mapped to an ``AssessmentPart``.

        arg:    assessment_part_id (osid.id.Id): ``Id`` of an
                ``AssessmentPart``
        return: (osid.assessment.BankList) - list of banks
        raise:  NotFound - ``assessment_part_id`` is not found
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        return lookup_session.get_banks_by_ids(
            self.get_bank_ids_by_assessment_part(assessment_part_id))


class AssessmentPartBankAssignmentSession(abc_assessment_authoring_sessions.AssessmentPartBankAssignmentSession, osid_sessions.OsidSession):
    """This session provides methods to re-assign ``AssessmentPart`` to ``Bank`` mappings.

    An ``AssessmentPart`` may appear in multiple ``Bank`` objects and
    removing the last reference to an ``AssessmentPart`` is the
    equivalent of deleting it. Each ``Bank`` may have its own
    authorizations governing who is allowed to operate on it.

    Adding a reference of an ``AssessmentPart`` to another ``Bank`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    _session_namespace = 'assessment_authoring.AssessmentPartBankAssignmentSession'

    def __init__(self, proxy=None, runtime=None, **kwargs):
        OsidSession._init_catalog(self, proxy, runtime)
        self._catalog_name = 'Bank'
        self._forms = dict()
        self._kwargs = kwargs

    def can_assign_assessment_parts(self):
        """Tests if this user can alter assessment part/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

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
    def can_assign_assessment_parts_to_bank(self, bank_id):
        """Tests if this user can alter assessment part/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        raise:  NullArgument - ``bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        if bank_id.get_identifier() == '000000000000000000000000':
            return False
        return True

    @utilities.arguments_not_none
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of bank including and under the given bank node in which any assessment part can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # This will likely be overridden by an authorization adapter
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        banks = lookup_session.get_banks()
        id_list = []
        for bank in banks:
            id_list.append(bank.get_id())
        return IdList(id_list)

    @utilities.arguments_not_none
    def get_assignable_bank_ids_for_assessment_part(self, bank_id, assessment_part_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment part can be assigned.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        return: (osid.id.IdList) - list of assignable bank ``Ids``
        raise:  NullArgument - ``bank_id`` or ``assessment_part_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        # This will likely be overridden by an authorization adapter
        return self.get_assignable_bank_ids(bank_id)

    @utilities.arguments_not_none
    def assign_assessment_part_to_bank(self, assessment_part_id, bank_id):
        """Adds an existing ``AssessmentPart`` to an ``Bank``.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  AlreadyExists - ``assessment_part_id`` is already
                assigned to ``bank_id``
        raise:  NotFound - ``assessment_part_id`` or ``bank_id`` not
                found
        raise:  NullArgument - ``assessment_part_id`` or ``bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._assign_object_to_catalog(assessment_part_id, bank_id)

    @utilities.arguments_not_none
    def unassign_assessment_part_from_bank(self, assessment_part_id, bank_id):
        """Removes an ``AssessmentPart`` from an ``Bank``.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        raise:  NotFound - ``assessment_part_id`` or ``bank_id`` not
                found or ``assessment_part_id`` not assigned to
                ``bank_id``
        raise:  NullArgument - ``assessment_part_id`` or ``bank_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_bank_lookup_session(proxy=self._proxy)
        lookup_session.get_bank(bank_id)  # to raise NotFound
        self._unassign_object_from_catalog(assessment_part_id, bank_id)

    @utilities.arguments_not_none
    def reassign_assessment_part_to_bank(self, assessment_part_id, from_biank_id, to_bank_id):
        """Moves an ``AssessmentPart`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        arg:    assessment_part_id (osid.id.Id): the ``Id`` of the
                ``AssessmentPart``
        arg:    from_biank_id (osid.id.Id): the ``Id`` of the current
                ``Bank``
        arg:    to_bank_id (osid.id.Id): the ``Id`` of the destination
                ``Bank``
        raise:  NotFound - ``assessment_part_id, from_bank_id,`` or
                ``to_bank_id`` not found or ``assessment_part_id`` not
                mapped to ``from_bank_id``
        raise:  NullArgument - ``assessment_part_id, from_bank_id,`` or
                ``to_bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceBinAssignmentSession.reassign_resource_to_bin
        self.assign_assessment_part_to_bank(assessment_part_id, to_bank_id)
        try:
            self.unassign_assessment_part_from_bank(assessment_part_id, from_biank_id)
        except:  # something went wrong, roll back assignment to to_bank_id
            self.unassign_assessment_part_from_bank(assessment_part_id, to_bank_id)
            raise


class AssessmentPartItemSession(abc_assessment_authoring_sessions.AssessmentPartItemSession, osid_sessions.OsidSession):
    """This session defines methods for looking up ``Item`` to ``AssessmentPart`` mappings."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_access_assessment_part_items(self):
        """Tests if this user can perform assessment part lookups.

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
        # osid.repository.AssetCompositionSession.can_access_asset_compositions
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    def use_comparative_asseessment_part_item_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_assessment_part_item_view(self):
        """A complete view of the returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment parts in catalogs which
        are children of this catalog in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    @utilities.arguments_not_none
    def get_assessment_part_items(self, assessment_part_id):
        """Gets the list of items mapped to the given ``AssessmentPart``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those items that are accessible through this session.

        arg:    assessment_part_id (osid.id.Id): ``Id`` of the
                ``AssessmentPart``
        return: (osid.assessment.ItemList) - list of items
        raise:  NotFound - ``assessment_part_id`` not found
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
        if self._catalog_view == ISOLATED:
            lookup_session.use_isolated_bank_view()
        else:
            lookup_session.use_federated_bank_view()
        item_ids = lookup_session.get_assessment_part(assessment_part_id).get_item_ids()
        mgr = self._get_provider_manager('ASSESSMENT')
        lookup_session = mgr.get_item_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        return lookup_session.get_items_by_ids(item_ids)

    @utilities.arguments_not_none
    def get_assessment_parts_by_item(self, item_id):
        """Gets the assessment parts containing the given item.

        In plenary mode, the returned list contains all known assessment
        parts or an error results. Otherwise, the returned list may
        contain only those assessment parts that are accessible through
        this session.

        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart list``
        raise:  NotFound - ``item_id`` is not found
        raise:  NullArgument - ``item_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetCompositionSession.get_compositions_by_asset
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'itemIds': {'$in': [str(item_id)]}},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.AssessmentPartList(result, runtime=self._runtime)


class AssessmentPartItemDesignSession(abc_assessment_authoring_sessions.AssessmentPartItemDesignSession, osid_sessions.OsidSession):
    """This session provides the means for adding items to an assessment part.

    The item is identified inside an assesment part using its own Id. To
    add the same item to the assessment part, multiple assessment parts
    should be used and placed at the same level in the
    ``AssessmentPart`` hierarchy.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the ``Bank`` associated with
                this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_design_assessment_parts(self):
        """Tests if this user can manage mapping of ``Items`` to ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        return: (boolean) - ``false`` if assessment part composition is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.AssetCompositionDesignSession.can_compose_assets_template
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def add_item(self, item_id, assessment_part_id):
        """Appends an item to an assessment part.

        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        arg:    assessment_part_id (osid.id.Id): ``Id`` of the
                ``AssessmentPart``
        raise:  AlreadyExists - ``item_id`` already part of
                ``assessment_part_id``
        raise:  NotFound - ``item_id`` or ``assessment_part_id`` not
                found
        raise:  NullArgument - ``item_id`` or ``assessment_part_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        # The item found check may want to be run through _get_provider_manager
        # so as to ensure access control:
        from dlkit.abstract_osid.id.primitives import Id as ABCId
        if not isinstance(item_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (not isinstance(assessment_part_id, ABCId) and
                assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart'):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if item_id.get_identifier_namespace() != 'assessment.Item':
            if item_id.get_authority() != self._authority:
                raise errors.InvalidArgument()
            else:
                mgr = self._get_provider_manager('ASSESSMENT')
                admin_session = mgr.get_item_admin_session_for_bank(self._catalog_id, proxy=self._proxy)
                item_id = admin_session._get_item_id_with_enclosure(item_id)
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self._runtime)
        item = collection.find_one({'_id': ObjectId(item_id.get_identifier())})
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        assessment_part = collection.find_one({'_id': ObjectId(assessment_part_id.get_identifier())})
        if 'itemIds' in assessment_part:
            if str(item_id) not in assessment_part['itemIds']:
                assessment_part['itemIds'].append(str(item_id))
        else:
            assessment_part['itemIds'] = [str(item_id)]
        collection.save(assessment_part)

    @utilities.arguments_not_none
    def move_item_ahead(self, item_id, assessment_part_id, reference_id):
        """Reorders items in an assessment part by moving the specified item in front of a reference item.

        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        arg:    assessment_part_id (osid.id.Id): ``Id`` of the
                ``AssessmentPartId``
        arg:    reference_id (osid.id.Id): ``Id`` of the reference
                ``Item``
        raise:  NotFound - ``item_id`` or ``reference_id``  ``not found
                in assessment_part_id``
        raise:  NullArgument - ``item_id, reference_id`` or
                ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        if (not isinstance(assessment_part_id, ABCId) and
                assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart'):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        assessment_part_map, collection = self._get_assessment_part_collection(assessment_part_id)
        assessment_part_map['itemIds'] = move_id_ahead(item_id, reference_id, assessment_part_map['itemIds'])
        collection.save(assessment_part_map)

    @utilities.arguments_not_none
    def move_item_behind(self, item_id, assessment_part_id, reference_id):
        """Reorders items in an assessment part by moving the specified item behind of a reference item.

        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        arg:    assessment_part_id (osid.id.Id): ``Id of the
                AssessmentPartId``
        arg:    reference_id (osid.id.Id): ``Id`` of the reference
                ``Item``
        raise:  NotFound - ``item_id`` or ``reference_id``  ``not found
                in assessment_part_id``
        raise:  NullArgument - ``item_id, reference_id`` or
                ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        if (not isinstance(assessment_part_id, ABCId) and
                assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart'):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        assessment_part_map, collection = self._get_assessment_part_collection(assessment_part_id)
        assessment_part_map['itemIds'] = move_id_behind(item_id, reference_id, assessment_part_map['itemIds'])
        collection.save(assessment_part_map)

    @utilities.arguments_not_none
    def order_items(self, item_ids, assessment_part_id):
        """Reorders a set of items in an assessment part.

        arg:    item_ids (osid.id.Id[]): ``Ids`` for a set of ``Items``
        arg:    assessment_part_id (osid.id.Id): ``Id`` of the
                ``AssessmentPartId``
        raise:  NotFound - ``assessment_part_id`` not found or, an
                ``item_id`` not related to ``assessment_part_id``
        raise:  NullArgument - ``item_ids`` or ``agenda_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        if (not isinstance(assessment_part_id, ABCId) and
                assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart'):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        assessment_part_map, collection = self._get_assessment_part_collection(assessment_part_id)
        assessment_part_map['itemIds'] = order_ids(item_ids, assessment_part_map['itemIds'])
        collection.save(assessment_part_map)

    @utilities.arguments_not_none
    def remove_item(self, item_id, assessment_part_id):
        """Removes an ``Item`` from an ``AssessmentPartId``.

        arg:    item_id (osid.id.Id): ``Id`` of the ``Item``
        arg:    assessment_part_id (osid.id.Id): ``Id`` of the
                ``AssessmentPartId``
        raise:  NotFound - ``item_id``  ``not found in
                assessment_part_id``
        raise:  NullArgument - ``item_id`` or ``assessment_part_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*

        """
        if (not isinstance(assessment_part_id, ABCId) and
                assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart'):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        assessment_part_map, collection = self._get_assessment_part_collection(assessment_part_id)
        try:
            assessment_part_map['itemIds'].remove(str(item_id))
        except (KeyError, ValueError):
            raise errors.NotFound()
        collection.save(assessment_part_map)

    def _get_assessment_part_collection(self, assessment_part_id):
        """Returns a Mongo Collection and AssessmentPart given a AssessmentPart Id"""
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        assessment_part_map = collection.find_one({'_id': ObjectId(assessment_part_id.get_identifier())})
        if 'itemIds' not in assessment_part_map:
            raise errors.NotFound('no Items are assigned to this AssessmentPart')
        return assessment_part_map, collection


class SequenceRuleLookupSession(abc_assessment_authoring_sessions.SequenceRuleLookupSession, osid_sessions.OsidSession):
    """This session provides methods for retrieving ``SequenceRules``."""
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the bank
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_lookup_sequence_rules(self):
        """Tests if this user can perform ``SequenceRules`` lookups.

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

    def use_comparative_sequence_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._use_comparative_object_view()

    def use_plenary_sequence_rule_view(self):
        """A complete view of the ``SequenceRule`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._use_plenary_object_view()

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule in banks which are
        children of this bank in the bank hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._use_federated_catalog_view()

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_isolated_bin_view
        self._use_isolated_catalog_view()

    def use_active_sequence_rule_view(self):
        """Only active sequence rules are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_active_composition_view_template
        self._status_view = ACTIVE

    def use_any_status_sequence_rule_view(self):
        """All active and inactive sequence rules are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.repository.CompositionLookupSession.use_any_status_composition_view_template
        self._status_view = ANY_STATUS

    @utilities.arguments_not_none
    def get_sequence_rule(self, sequence_rule_id):
        """Gets the ``SequenceRule`` specified by its ``Id``.

        arg:    sequence_rule_id (osid.id.Id): ``Id`` of the
                ``SequenceRule``
        return: (osid.assessment.authoring.SequenceRule) - the sequence
                rule
        raise:  NotFound - ``sequence_rule_id`` not found
        raise:  NullArgument - ``sequence_rule_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resource
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        result = collection.find_one(
            dict({'_id': ObjectId(self._get_id(sequence_rule_id, 'assessment_authoring').get_identifier())},
                 **self._view_filter()))
        return objects.SequenceRule(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_sequence_rules_by_ids(self, sequence_rule_ids):
        """Gets a ``SequenceRuleList`` corresponding to the given ``IdList``.

        arg:    sequence_rule_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NotFound - a ``Id was`` not found
        raise:  NullArgument - ``sequence_rule_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_ids
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        object_id_list = []
        for i in sequence_rule_ids:
            object_id_list.append(ObjectId(self._get_id(i, 'assessment_authoring').get_identifier()))
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
        return objects.SequenceRuleList(sorted_result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_sequence_rules_by_genus_type(self, sequence_rule_genus_type):
        """Gets a ``SequenceRuleList`` corresponding to the given sequence rule genus ``Type`` which does not include sequence rule of genus types derived from the specified ``Type``.

        arg:    sequence_rule_genus_type (osid.type.Type): a sequence
                rule genus type
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``sequence_rule_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'genusTypeId': str(sequence_rule_genus_type)},
                 **self._view_filter())).sort('_id', DESCENDING)
        return objects.SequenceRuleList(result, runtime=self._runtime, proxy=self._proxy)

    @utilities.arguments_not_none
    def get_sequence_rules_by_parent_genus_type(self, sequence_rule_genus_type):
        """Gets a ``SequenceRuleList`` corresponding to the given sequence rule genus ``Type`` and include any additional sequence rule with genus types derived from the specified ``Type``.

        arg:    sequence_rule_genus_type (osid.type.Type): a sequence
                rule genus type
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``sequence_rule_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.SequenceRuleList([])

    @utilities.arguments_not_none
    def get_sequence_rules_by_record_type(self, sequence_rule_record_type):
        """Gets a ``SequenceRuleList`` containing the given sequence rule record ``Type``.

        arg:    sequence_rule_record_type (osid.type.Type): a sequence
                rule record type
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``sequence_rule_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources_by_record_type
        # STILL NEED TO IMPLEMENT!!!
        return objects.SequenceRuleList([])

    @utilities.arguments_not_none
    def get_sequence_rules_for_assessment_part(self, assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given source assessment part.

        arg:    assessment_part_id (osid.id.Id): an assessment part
                ``Id``
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.learning.ActivityLookupSession.get_activities_for_objective_template
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentPartId': str(assessment_part_id)},
                 **self._view_filter()))
        return objects.SequenceRuleList(result, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_sequence_rules_for_next_assessment_part(self, next_assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given target assessment part.

        arg:    next_assessment_part_id (osid.id.Id): an assessment part
                ``Id``
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``next_assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_sequence_rules_for_assessment_parts(self, assessment_part_id, next_assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given source and target assessment parts.

        arg:    assessment_part_id (osid.id.Id): source assessment part
                ``Id``
        arg:    next_assessment_part_id (osid.id.Id): target assessment
                part ``Id``
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``assessment_part_id`` or
                ``next_assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def get_sequence_rules_for_assessment(self, assessment_id):
        """Gets a ``SequenceRuleList`` for an entire assessment.

        arg:    assessment_id (osid.id.Id): an assessment ``Id``
        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  NullArgument - ``assessment_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # First, recursively get all the partIds for the assessment
        def get_all_children_part_ids(part):
            child_ids = []
            if part.has_children():
                child_ids = list(part.get_child_assessment_part_ids())
                for child in part.get_child_assessment_parts():
                    child_ids += get_all_children_part_ids(child)
            return child_ids

        all_assessment_part_ids = []

        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        assessment = lookup_session.get_assessment(assessment_id)

        if assessment.has_children():
            mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
            lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
            lookup_session.use_federated_bank_view()
            all_assessment_part_ids = list(assessment.get_child_ids())
            for child_part_id in assessment.get_child_ids():
                child_part = lookup_session.get_assessment_part(child_part_id)
                all_assessment_part_ids += get_all_children_part_ids(child_part)

        id_strs = [str(part_id) for part_id in all_assessment_part_ids]
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentPartId': {'$in': id_strs}},
                 **self._view_filter()))
        return objects.SequenceRuleList(result, runtime=self._runtime)

    def get_sequence_rules(self):
        """Gets all ``SequenceRules``.

        return: (osid.assessment.authoring.SequenceRuleList) - the
                returned ``SequenceRule`` list
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.get_resources
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        result = collection.find(self._view_filter()).sort('_id', DESCENDING)
        return objects.SequenceRuleList(result, runtime=self._runtime, proxy=self._proxy)

    sequence_rules = property(fget=get_sequence_rules)


class SequenceRuleAdminSession(abc_assessment_authoring_sessions.SequenceRuleAdminSession, osid_sessions.OsidSession):
    """This session creates and removes sequence rules.

    The data for create and update is provided via the
    ``SequenceRuleForm``.

    """
    def __init__(self, catalog_id=None, proxy=None, runtime=None, **kwargs):
        OsidSession.__init__(self)
        self._catalog_class = objects.Bank
        self._catalog_name = 'Bank'
        OsidSession._init_object(
            self,
            catalog_id,
            proxy,
            runtime,
            db_name='assessment_authoring',
            cat_name='Bank',
            cat_class=objects.Bank)
        self._forms = dict()
        self._kwargs = kwargs

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Bank Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        return: (osid.assessment.Bank) - the bank
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        return self._catalog

    bank = property(fget=get_bank)

    def can_create_sequence_rule(self):
        """Tests if this user can create sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        return: (boolean) - ``false`` if ``SequenceRule`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def can_create_sequence_rule_with_record_types(self, sequence_rule_record_types):
        """Tests if this user can create a single ``SequenceRule`` using the desired record types.

        While
        ``AssessmentAuthoringManager.getSequenceRuleRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``SequenceRule``. Providing an empty array tests if a
        ``SequenceRule`` can be created with no records.

        arg:    sequence_rule_record_types (osid.type.Type[]): array of
                sequence rule record types
        return: (boolean) - ``true`` if ``SequenceRule`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        raise:  NullArgument - ``sequence_rule_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_sequence_rule_form_for_create(self, assessment_part_id, next_assessment_part_id, sequence_rule_record_types):
        """Gets the sequence rule form for creating new sequence rules between two assessment parts.

        A new form should be requested for each create transaction.

        arg:    assessment_part_id (osid.id.Id): the source assessment
                part ``Id``
        arg:    next_assessment_part_id (osid.id.Id): the target
                assessment part ``Id``
        arg:    sequence_rule_record_types (osid.type.Type[]): array of
                sequence rule record types
        return: (osid.assessment.authoring.SequenceRuleForm) - the
                sequence rule form
        raise:  InvalidArgument - ``assessment_part_id`` and
                ``next_assessment_part_id`` not on the same assessment
        raise:  NotFound - ``assessment_part_id`` or
                ``next_assessment_part_id`` is not found
        raise:  NullArgument - ``assessment_part_id,
                next_assessment_part_id`` , or
                ``sequence_rule_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        for arg in sequence_rule_record_types:
            if not isinstance(arg, ABCId):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID ${arg0_type}')
        if sequence_rule_record_types == []:
            obj_form = objects.SequenceRuleForm(
                bank_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy,
                next_assessment_part_id=next_assessment_part_id,
                assessment_part_id=assessment_part_id)
        else:
            obj_form = objects.SequenceRuleForm(
                bank_id=self._catalog_id,
                record_types=sequence_rule_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy,
                next_assessment_part_id=next_assessment_part_id,
                assessment_part_id=assessment_part_id)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form

    @utilities.arguments_not_none
    def create_sequence_rule(self, sequence_rule_form):
        """Creates a new ``SequenceRule``.

        arg:    sequence_rule_form
                (osid.assessment.authoring.SequenceRuleForm): the form
                for this ``SequenceRule``
        return: (osid.assessment.authoring.SequenceRule) - the new
                ``SequenceRule``
        raise:  IllegalState - ``sequence_rule_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``sequence_rule_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``sequence_rule_form`` did not originate
                from ``get_sequence_rule_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.create_resource_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        if not isinstance(sequence_rule_form, ABCSequenceRuleForm):
            raise errors.InvalidArgument('argument type is not an SequenceRuleForm')
        if sequence_rule_form.is_for_update():
            raise errors.InvalidArgument('the SequenceRuleForm is for update only, not create')
        try:
            if self._forms[sequence_rule_form.get_id().get_identifier()] == CREATED:
                raise errors.IllegalState('sequence_rule_form already used in a create transaction')
        except KeyError:
            raise errors.Unsupported('sequence_rule_form did not originate from this session')
        if not sequence_rule_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        insert_result = collection.insert_one(sequence_rule_form._my_map)

        self._forms[sequence_rule_form.get_id().get_identifier()] = CREATED
        result = objects.SequenceRule(
            osid_object_map=collection.find_one({'_id': insert_result.inserted_id}),
            runtime=self._runtime,
            proxy=self._proxy)

        return result

    def can_update_sequence_rules(self):
        """Tests if this user can update sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        return: (boolean) - ``false`` if ``SequenceRule`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_update_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def get_sequence_rule_form_for_update(self, sequence_rule_id):
        """Gets the sequence rule form for updating an existing sequence rule.

        A new sequence rule form should be requested for each update
        transaction.

        arg:    sequence_rule_id (osid.id.Id): the ``Id`` of the
                ``SequenceRule``
        return: (osid.assessment.authoring.SequenceRuleForm) - the
                sequence rule form
        raise:  NotFound - ``sequence_rule_id`` is not found
        raise:  NullArgument - ``sequence_rule_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.get_resource_form_for_update_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        if not isinstance(sequence_rule_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (sequence_rule_id.get_identifier_namespace() != 'assessment_authoring.SequenceRule' or
                sequence_rule_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(sequence_rule_id.get_identifier())})

        obj_form = objects.SequenceRuleForm(osid_object_map=result, runtime=self._runtime, proxy=self._proxy)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form

    @utilities.arguments_not_none
    def update_sequence_rule(self, sequence_rule_form):
        """Updates an existing sequence rule.

        arg:    sequence_rule_form
                (osid.assessment.authoring.SequenceRuleForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``sequence_rule_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``sequence_rule_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``sequence_rule_form`` did not originate
                from ``get_sequence_rule_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.update_resource_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        if not isinstance(sequence_rule_form, ABCSequenceRuleForm):
            raise errors.InvalidArgument('argument type is not an SequenceRuleForm')
        if not sequence_rule_form.is_for_update():
            raise errors.InvalidArgument('the SequenceRuleForm is for update only, not create')
        try:
            if self._forms[sequence_rule_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('sequence_rule_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('sequence_rule_form did not originate from this session')
        if not sequence_rule_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(sequence_rule_form._my_map)

        self._forms[sequence_rule_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.SequenceRule(
            osid_object_map=sequence_rule_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)

    def can_delete_sequence_rules(self):
        """Tests if this user can delete sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        return: (boolean) - ``false`` if ``SequenceRule`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.can_delete_resources
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def delete_sequence_rule(self, sequence_rule_id):
        """Deletes a ``SequenceRule``.

        arg:    sequence_rule_id (osid.id.Id): the ``Id`` of the
                ``SequenceRule`` to remove
        raise:  NotFound - ``sequence_rule_id`` not found
        raise:  NullArgument - ``sequence_rule_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.delete_resource_template
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        if not isinstance(sequence_rule_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        sequence_rule_map = collection.find_one(
            dict({'_id': ObjectId(sequence_rule_id.get_identifier())},
                 **self._view_filter()))

        objects.SequenceRule(osid_object_map=sequence_rule_map, runtime=self._runtime, proxy=self._proxy)._delete()
        collection.delete_one({'_id': ObjectId(sequence_rule_id.get_identifier())})

    def can_manage_sequence_rule_aliases(self):
        """Tests if this user can manage ``Id`` aliases for sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``SequenceRule`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # NOTE: It is expected that real authentication hints will be
        # handled in a service adapter above the pay grade of this impl.
        return True

    @utilities.arguments_not_none
    def alias_sequence_rule(self, sequence_rule_id, alias_id):
        """Adds a ``Id`` to a ``SequenceRule`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``SequenceRule`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another sequence rule. it
        is reassigned to the given sequence rule ``Id``.

        arg:    sequence_rule_id (osid.id.Id): the ``Id`` of a
                ``SequenceRule``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``sequence_rule_id`` not found
        raise:  NullArgument - ``sequence_rule_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceAdminSession.alias_resources_template
        self._alias_id(primary_id=sequence_rule_id, equivalent_id=alias_id)

    def can_sequence_sequence_rules(self):
        """Tests if this user can order ``SequenceRules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known sequencing operations
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer sequencing
        operations to an unauthorized user.

        return: (boolean) - ``false`` if ``SequenceRule`` ordering is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def move_sequence_rule_ahead(self, sequence_rule_id, assessment_part_id, reference_id):
        """Reorders sequence rule for a source assessment part by moving the specified sequence rule in front of a reference sequence rule.

        arg:    sequence_rule_id (osid.id.Id): the ``Id`` of a
                ``SequenceRule``
        arg:    assessment_part_id (osid.id.Id): the ``Id`` of an
                ``AssessmentPart``
        arg:    reference_id (osid.id.Id): the reference sequence rule
                ``Id``
        raise:  NotFound - ``sequence_rule_id, assessment_part_id,`` or
                ``reference_id`` not found or, ``sequence_rule_id`` or
                ``reference_id`` not related to ``assessment_part_id``
        raise:  NullArgument - ``sequence_rule_id, assessment_part_id,``
                or ``reference_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def move_sequence_rule_behind(self, sequence_rule_id, assessment_part_id, reference_id):
        """Reorders sequence rule for a source assessment part by moving the specified sequence rule behind a reference sequence rule.

        arg:    sequence_rule_id (osid.id.Id): the ``Id`` of a
                ``SequenceRule``
        arg:    assessment_part_id (osid.id.Id): the ``Id`` of an
                ``AssessmentPart``
        arg:    reference_id (osid.id.Id): the reference sequence rule
                ``Id``
        raise:  NotFound - ``sequence_rule_id, assessment_part_id,`` or
                ``reference_id`` not found or, ``sequence_rule_id`` or
                ``reference_id`` not related to ``assessment_part_id``
        raise:  NullArgument - ``sequence_rule_id, assessment_part_id,``
                or ``reference_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()

    @utilities.arguments_not_none
    def order_sequence_rules(self, sequence_rule_ids, assessment_part_id):
        """Reorders a set of sequence rules for an assessment part.

        arg:    sequence_rule_ids (osid.id.Id[]): the ``Ids`` for a set
                of ``SequenceRules``
        arg:    assessment_part_id (osid.id.Id): the ``Id`` of an
                ``AssessmentPart``
        raise:  NotFound - ``assessment_part_id`` not found or, a
                ``sequence_rule_id`` not related to
                ``assessment_part_id``
        raise:  NullArgument - ``sequence_rule_ids`` or
                ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        raise errors.Unimplemented()
