"""Implementations of assessment.authoring abstract base class sessions."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class AssessmentPartLookupSession:
    """This session defines methods for retrieving assessment parts."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_assessment_parts(self):
        """Tests if this user can perform ``AssessmentPart`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_assessment_part_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_assessment_part_view(self):
        """A complete view of the ``AssessmentPart`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment parts in catalogs which
        are children of this catalog in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_active_assessment_part_view(self):
        """Only active assessment parts are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_status_assessment_part_view(self):
        """All active and inactive assessment parts are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_sequestered_assessment_part_view(self):
        """The methods in this session omit sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_unsequestered_assessment_part_view(self):
        """The methods in this session return all assessment parts, including sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part(self, assessment_part_id):
        """Gets the ``AssessmentPart`` specified by its ``Id``.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to retrieve
        :type assessment_part_id: ``osid.id.Id``
        :return: the returned ``AssessmentPart``
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``NotFound`` -- no ``AssessmentPart`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    @abc.abstractmethod
    def get_assessment_parts_by_ids(self, assessment_part_ids):
        """Gets an ``AssessmentPartList`` corresponding to the given ``IdList``.

        :param assessment_part_ids: the list of ``Ids`` to retrieve
        :type assessment_part_ids: ``osid.id.IdList``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_part_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_assessment_parts_by_genus_type(self, assessment_part_genus_type):
        """Gets an ``AssessmentPartList`` corresponding to the given assessment part genus ``Type`` which does not include assessment parts of types derived from the specified ``Type``.

        :param assessment_part_genus_type: an assessment part genus type
        :type assessment_part_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_assessment_parts_by_parent_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentPartList`` corresponding to the given assessment part genus ``Type`` and include any additional assessment parts with genus types derived from the specified ``Type``.

        :param assessment_genus_type: an assessment part genus type
        :type assessment_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_assessment_parts_by_record_type(self, assessment_part_record_type):
        """Gets an ``AssessmentPart`` containing the given assessment part record ``Type``.

        :param assessment_part_record_type: an assessment part record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_assessment_parts_for_assessment(self, assessment_id):
        """Gets an ``AssessmentPart`` for the given assessment.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_assessment_parts(self):
        """Gets all ``AssessmentParts``.

        :return: a list of ``AssessmentParts``
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    assessment_parts = property(fget=get_assessment_parts)


class AssessmentPartQuerySession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_assessment_parts(self):
        """Tests if this user can perform ``AssessmentPart`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment part in banks which are
        children of this step in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_sequestered_assessment_part_view(self):
        """The methods in this session omit sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_unsequestered_assessment_part_view(self):
        """The methods in this session return all assessment parts, including sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part_query(self):
        """Gets an assessment part query.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartQuery

    assessment_part_query = property(fget=get_assessment_part_query)

    @abc.abstractmethod
    def get_assessment_parts_by_query(self, assessment_part_query):
        """Gets a list of ``AssessmentParts`` matching the given assessment part query.

        :param assessment_part_query: the assessment part query
        :type assessment_part_query: ``osid.assessment.authoring.AssessmentPartQuery``
        :return: the returned ``AssessmentPartList``
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``assessment_part_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList


class AssessmentPartSearchSession:
    """This session provides methods for searching among ``AssessmentPart`` objects.

    The search query is constructed using the ``AssessmentPartyQuery``.

    ``get_assessment_parts_by_query()`` is the basic search method and
    returns a list of ``AssessmentParts``. A more advanced search may be
    performed with ``getAssessmentPartsBySearch()``. It accepts an
    ``AssessmentPartSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    workflow. ``get_assessment_parts_by_search()`` returns an
    ``AssessmentPartSearchResults`` that can be used to access the
    resulting ``AssessmentPartList`` or be used to perform a search
    within the result set through ``AssessmentPartSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessment part in bank of
        which this bank matchmaker is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessment part
        in this bank


    ``AssessmentParts`` may have a query record indicated by their
    respective record types. Thequery record is accessed via the
    ``AssessmentPartQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_assessment_part_search(self):
        """Gets an assessment part search.

        :return: the assessment part search
        :rtype: ``osid.assessment.authoring.AssessmentPartSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartSearch

    assessment_part_search = property(fget=get_assessment_part_search)

    @abc.abstractmethod
    def get_assessment_part_search_order(self):
        """Gets an assessment part search order.

        The ``AssessmentPartSearchOrder`` is supplied to an
        ``AssessmentPartSearch`` to specify the ordering of results.

        :return: the assessment part search order
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartSearchOrder

    assessment_part_search_order = property(fget=get_assessment_part_search_order)

    @abc.abstractmethod
    def get_assessment_parts_by_search(self, assessment_part_query, assessment_part_search):
        """Gets the search results matching the given search query using the given search.

        :param assessment_part_query: the assessment part query
        :type assessment_part_query: ``osid.assessment.authoring.AssessmentPartQuery``
        :param assessment_part_search: the assessment part search
        :type assessment_part_search: ``osid.assessment.authoring.AssessmentPartSearch``
        :return: the returned search results
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchResults``
        :raise: ``NullArgument`` -- ``assessment_part_query`` or ``assessment_part_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``assessment_part_query`` or ``assessment_part_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartSearchResults

    @abc.abstractmethod
    def get_assessment_part_query_from_inspector(self, assessment_part_query_inspector):
        """Gets an assessment part query from an inspector.

        The inspector is available from an
        ``AssessmentPartSearchResults``.

        :param assessment_part_query_inspector: an assessment part query inspector
        :type assessment_part_query_inspector: ``osid.assessment.authoring.AssessmentPartQueryInspector``
        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``NullArgument`` -- ``assessment_part_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_part_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartQuery


class AssessmentPartAdminSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_assessment_parts(self):
        """Tests if this user can create assessment parts.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to unauthorized users.

        :return: ``false`` if ``AssessmentPart`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_assessment_part_with_record_types(self, assessment_part_record_types):
        """Tests if this user can create a single ``AssessmentPart`` using the desired record types.

        While
        ``AssessmentAuthoringManager.getAssessmentPartRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentPart``. Providing an empty array tests if an
        ``AssessmentPart`` can be created with no records.

        :param assessment_part_record_types: array of assessment part record types
        :type assessment_part_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssessmentPart`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_part_form_for_create_for_assessment(self, assessment_id, assessment_part_record_types):
        """Gets the assessment part form for creating new assessment parts for an assessment.

        A new form should be requested for each create transaction.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param assessment_part_record_types: array of assessment part record types to be included in the create operation or an empty list if none
        :type assessment_part_record_types: ``osid.type.Type[]``
        :return: the assessment part form
        :rtype: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``assessment_part_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartForm

    @abc.abstractmethod
    def create_assessment_part_for_assessment(self, assessment_part_form):
        """Creates a new assessment part.

        :param assessment_part_form: assessment part form
        :type assessment_part_form: ``osid.assessment.authoring.AssessmentPartForm``
        :return: the new part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- ``assessment_part_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- ``assessment_part_form`` is invalid
        :raise: ``NullArgument`` -- ``assessment_part_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_form`` did not originate from ``get_assessment_part_form_for_create_for_assessment()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    @abc.abstractmethod
    def get_assessment_part_form_for_create_for_assessment_part(self, assessment_part_id, assessment_part_record_types):
        """Gets the assessment part form for creating new assessment parts under another assessment part.

        A new form should be requested for each create transaction.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param assessment_part_record_types: array of assessment part record types to be included in the create operation or an empty list if none
        :type assessment_part_record_types: ``osid.type.Type[]``
        :return: the assessment part form
        :rtype: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``assessment_part_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartForm

    @abc.abstractmethod
    def create_assessment_part_for_assessment_part(self, assessment_part_form):
        """Creates a new assessment part.

        :param assessment_part_form: assessment part form
        :type assessment_part_form: ``osid.assessment.authoring.AssessmentPartForm``
        :return: the new part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- ``assessment_part_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- ``assessment_part_form`` is invalid
        :raise: ``NullArgument`` -- ``assessment_part_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_form`` did not originate from ``get_assessment_part_form_for_create_for_assessment_part()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPart

    @abc.abstractmethod
    def can_update_assessment_parts(self):
        """Tests if this user can update ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentPart`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if assessment part modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_part_form_for_update(self, assessment_part_id):
        """Gets the assessment part form for updating an existing assessment part.

        A new assessment part form should be requested for each update
        transaction.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: the assessment part form
        :rtype: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartForm

    @abc.abstractmethod
    def update_assessment_part(self, assessment_part_id, assessment_part_form):
        """Updates an existing assessment part.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param assessment_part_form: part form
        :type assessment_part_form: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_form`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_assessment_parts(self):
        """Tests if this user can delete ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentPart`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``AssessmentPart`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_assessment_part(self, assessment_part_id):
        """Removes an asessment part and all mapped items.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_assessment_part_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``AssessmentPart`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_assessment_part(self, assessment_part_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentPart`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentPart`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment part, it is
        reassigned to the given assessment part ``Id``.

        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentPartNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``AssessmentPart`` objects in this ``Bank``.

    This also includes existing ``AssessmentParts`` that may appear or
    disappear due to changes in the ``Bank`` hierarchy, This session is
    intended for consumers needing to synchronize their state with this
    service without the use of polling. Notifications are cancelled when
    this session is closed.

    The two views defined in this session correspond to the views in the
    ``AssessmentPartLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_assessment_part_notifications(self):
        """Tests if this user can register for ``AssessmentPart`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include in bank which are children of this
        bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_part_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_assessment_part_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_part_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_part_notification(self, notification_id):
        """Acknowledge an assessment part notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_assessment_parts(self):
        """Register for notifications of new assessment parts.

        ``AssessmentPartReceiver.newAssessmentParst()`` is invoked when
        a new ``AssessmentPart`` appears in this bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessment_parts(self):
        """Registers for notification of updated bank.

        ``AssessmentPartReceiver.changedAssessmentParts()`` is invoked
        when an assessment part in this bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_assessment_part(self, assessment_part_id):
        """Registers for notification of an updated assessment part.

        ``ProvisionableReceiver.changedAssessmentParts()`` is invoked
        when the specified assessment part in this bank is changed.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an assessment part was not found in this step matchmaker identified by the given ``Id``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessment_parts(self):
        """Registers for notification of deleted assessment parts.

        ``AssessmentPartReceiver.deletedAssessmentParts()`` is invoked
        when an assessment part is deleted or removed from this bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_assessment_part(self, assessment_part_id):
        """Registers for notification of a deleted assessment part.

        ``AssessmentPartReceiver.deletedAssessmentParts()`` is invoked
        when the specified assessment part is deleted or removed from
        this bank.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an assessment part was not found in this step matchmaker identified by the given ``Id``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_assessment_part_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_assessment_part_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_assessment_part_notification(self, notification_id):
        """Acknowledge an assessment_part notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentPartBankSession:
    """This session provides methods to retrieve ``AssessmentPart`` to ``Bank`` mappings.

    an ``AssessmentPart`` may appear in multiple ``Bank`` objects. Each
    bank may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_assessment_part_bank_mappings(self):
        """Tests if this user can perform lookups of assessment part/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_assessment_part_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_assessment_part_bank_view(self):
        """A complete view of the ``AssessmentPart`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part_ids_by_bank(self, bank_id):
        """Gets the list of ``AssessmentPartIds`` associated with an ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment part ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessment_parts_by_bank(self, bank_id):
        """Gets the list of assessment parts associated with an ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related assessment parts
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_assessment_part_ids_by_banks(self, bank_ids):
        """Gets the list of ``AssessmentPart Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessment part ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assessment_parts_by_banks(self, bank_ids):
        """Gets the list of assessment part corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of assessment parts
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList

    @abc.abstractmethod
    def get_bank_ids_by_assessment_part(self, assessment_part_id):
        """Gets the ``Bank``  ``Ids`` mapped to an ``AssessmentPart``.

        :param assessment_part_id: ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_assessment_part(self, assessment_part_id):
        """Gets the ``Banks`` mapped to an ``AssessmentPart``.

        :param assessment_part_id: ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class AssessmentPartBankAssignmentSession:
    """This session provides methods to re-assign ``AssessmentPart`` to ``Bank`` mappings.

    An ``AssessmentPart`` may appear in multiple ``Bank`` objects and
    removing the last reference to an ``AssessmentPart`` is the
    equivalent of deleting it. Each ``Bank`` may have its own
    authorizations governing who is allowed to operate on it.

    Adding a reference of an ``AssessmentPart`` to another ``Bank`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_assessment_parts(self):
        """Tests if this user can alter assessment part/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_assessment_parts_to_bank(self, bank_id):
        """Tests if this user can alter assessment part/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of bank including and under the given bank node in which any assessment part can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_assessment_part(self, bank_id, assessment_part_id):
        """Gets a list of bank including and under the given bank node in which a specific assessment part can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_assessment_part_to_bank(self, assessment_part_id, bank_id):
        """Adds an existing ``AssessmentPart`` to an ``Bank``.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``assessment_part_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``assessment_part_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_assessment_part_from_bank(self, assessment_part_id, bank_id):
        """Removes an ``AssessmentPart`` from an ``Bank``.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` or ``bank_id`` not found or ``assessment_part_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_assessment_part_to_bank(self, assessment_part_id, from_biank_id, to_bank_id):
        """Moves an ``AssessmentPart`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param from_biank_id: the ``Id`` of the current ``Bank``
        :type from_biank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id, from_bank_id,`` or ``to_bank_id`` not found or ``assessment_part_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``assessment_part_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentPartSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic bank.

    An ``AssessmentPartQuery`` can be retrieved from this session and
    mapped to this ``Bank`` to create a virtual collection of assessment
    parts. The assessment part may be sequenced using the
    ``AssessmentPartSearchOrder`` from this session.

    This ``Bank`` has a default query that matches any assessment part
    and a default search order that specifies no sequencing. The queries
    may be examined using an ``AssessmentPartQueryInspector``. The query
    may be modified by converting the inspector back to an
    ``AssessmentPartQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart bank.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assessment_part_query(self):
        """Gets an assessment part query.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartQuery

    assessment_part_query = property(fget=get_assessment_part_query)

    @abc.abstractmethod
    def get_assessment_part_search_order(self):
        """Gets an assessment part search order.

        :return: the assessment part search order
        :rtype: ``osid.assessment.authoring.AssessmentPartSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartSearchOrder

    assessment_part_search_order = property(fget=get_assessment_part_search_order)

    @abc.abstractmethod
    def apply_assessment_part_query(self, assessment_part_query):
        """Applies an assessment part query to this bank.

        :param assessment_part_query: the assessment part query
        :type assessment_part_query: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``NullArgument`` -- ``assessment_part_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_assessment_part_query(self):
        """Gets an assessment part query inspector for this bank.

        :return: the assessment part query inspector
        :rtype: ``osid.assessment.authoring.AssessmentPartQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartQueryInspector

    @abc.abstractmethod
    def apply_assessment_part_sequencing(self, assessment_part_search_order):
        """Applies an assessment part search order to this bank.

        :param assessment_part_search_order: the assessment part search order
        :type assessment_part_search_order: ``osid.assessment.authoring.AssessmentPartSearchOrder``
        :raise: ``NullArgument`` -- ``assessment_part_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part_query_from_inspector(self, assessment_part_query_inspector):
        """Gets an assessment part query from an inspector.

        :param assessment_part_query_inspector: an assessment part query inspector
        :type assessment_part_query_inspector: ``osid.assessment.authoring.AssessmentPartQueryInspector``
        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``
        :raise: ``NullArgument`` -- ``assessment_part_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``assessment_part_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartQuery


class AssessmentPartItemSession:
    """This session defines methods for looking up ``Item`` to ``AssessmentPart`` mappings."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_access_assessment_part_items(self):
        """Tests if this user can perform assessment part lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_asseessment_part_item_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_assessment_part_item_view(self):
        """A complete view of the returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment parts in catalogs which
        are children of this catalog in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_assessment_part_items(self, assessment_part_id):
        """Gets the list of items mapped to the given ``AssessmentPart``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those items that are accessible through this session.

        :param assessment_part_id: ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: list of items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.ItemList

    @abc.abstractmethod
    def get_assessment_parts_by_item(self, item_id):
        """Gets the assessment parts containing the given item.

        In plenary mode, the returned list contains all known assessment
        parts or an error results. Otherwise, the returned list may
        contain only those assessment parts that are accessible through
        this session.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the returned ``AssessmentPart list``
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.AssessmentPartList


class AssessmentPartItemDesignSession:
    """This session provides the means for adding items to an assessment part.

    The item is identified inside an assesment part using its own Id. To
    add the same item to the assessment part, multiple assessment parts
    should be used and placed at the same level in the
    ``AssessmentPart`` hierarchy.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_design_assessment_parts(self):
        """Tests if this user can manage mapping of ``Items`` to ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        :return: ``false`` if assessment part composition is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_item(self, item_id, assessment_part_id):
        """Appends an item to an assessment part.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``item_id`` already part of ``assessment_part_id``
        :raise: ``NotFound`` -- ``item_id`` or ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``item_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def move_item_ahead(self, item_id, assessment_part_id, reference_id):
        """Reorders items in an assessment part by moving the specified item in front of a reference item.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id`` of the ``AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Item``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id`` or ``reference_id``  ``not found in assessment_part_id``
        :raise: ``NullArgument`` -- ``item_id, reference_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def move_item_behind(self, item_id, assessment_part_id, reference_id):
        """Reorders items in an assessment part by moving the specified item behind of a reference item.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id of the AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Item``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id`` or ``reference_id``  ``not found in assessment_part_id``
        :raise: ``NullArgument`` -- ``item_id, reference_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_items(self, item_ids, assessment_part_id):
        """Reorders a set of items in an assessment part.

        :param item_ids: ``Ids`` for a set of ``Items``
        :type item_ids: ``osid.id.Id[]``
        :param assessment_part_id: ``Id`` of the ``AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found or, an ``item_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``item_ids`` or ``agenda_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_item(self, item_id, assessment_part_id):
        """Removes an ``Item`` from an ``AssessmentPartId``.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id`` of the ``AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id``  ``not found in assessment_part_id``
        :raise: ``NullArgument`` -- ``item_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleLookupSession:
    """This session provides methods for retrieving ``SequenceRules``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_sequence_rules(self):
        """Tests if this user can perform ``SequenceRules`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_sequence_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_sequence_rule_view(self):
        """A complete view of the ``SequenceRule`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_active_sequence_rule_view(self):
        """Only active sequence rules are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_status_sequence_rule_view(self):
        """All active and inactive sequence rules are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule(self, sequence_rule_id):
        """Gets the ``SequenceRule`` specified by its ``Id``.

        :param sequence_rule_id: ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: the sequence rule
        :rtype: ``osid.assessment.authoring.SequenceRule``
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRule

    @abc.abstractmethod
    def get_sequence_rules_by_ids(self, sequence_rule_ids):
        """Gets a ``SequenceRuleList`` corresponding to the given ``IdList``.

        :param sequence_rule_ids: the list of ``Ids`` to retrieve
        :type sequence_rule_ids: ``osid.id.IdList``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NotFound`` -- a ``Id was`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_by_genus_type(self, sequence_rule_genus_type):
        """Gets a ``SequenceRuleList`` corresponding to the given sequence rule genus ``Type`` which does not include sequence rule of genus types derived from the specified ``Type``.

        :param sequence_rule_genus_type: a sequence rule genus type
        :type sequence_rule_genus_type: ``osid.type.Type``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_by_parent_genus_type(self, sequence_rule_genus_type):
        """Gets a ``SequenceRuleList`` corresponding to the given sequence rule genus ``Type`` and include any additional sequence rule with genus types derived from the specified ``Type``.

        :param sequence_rule_genus_type: a sequence rule genus type
        :type sequence_rule_genus_type: ``osid.type.Type``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_by_record_type(self, sequence_rule_record_type):
        """Gets a ``SequenceRuleList`` containing the given sequence rule record ``Type``.

        :param sequence_rule_record_type: a sequence rule record type
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_for_assessment_part(self, assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given source assessment part.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_for_next_assessment_part(self, next_assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given target assessment part.

        :param next_assessment_part_id: an assessment part ``Id``
        :type next_assessment_part_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``next_assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_for_assessment_parts(self, assessment_part_id, next_assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given source and target assessment parts.

        :param assessment_part_id: source assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param next_assessment_part_id: target assessment part ``Id``
        :type next_assessment_part_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``next_assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules_for_assessment(self, assessment_id):
        """Gets a ``SequenceRuleList`` for an entire assessment.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rules(self):
        """Gets all ``SequenceRules``.

        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    sequence_rules = property(fget=get_sequence_rules)


class SequenceRuleQuerySession:
    """This session provides methods for searching among ``SequenceRule`` objects.

    The search query is constructed using the ``SequenceRuleQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include sequence rule in bank of
        which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to sequence rule in
        this bank


    sequence rule may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``SequenceRuleQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_sequence_rules(self):
        """Tests if this user can perform ``SequenceRule`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule in banks which are
        children of this step in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_query(self):
        """Gets a sequence rule query.

        :return: the sequence rule query
        :rtype: ``osid.assessment.authoring.SequenceRuleQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleQuery

    sequence_rule_query = property(fget=get_sequence_rule_query)

    @abc.abstractmethod
    def get_sequence_rules_by_query(self, sequence_rule_query):
        """Gets a list of ``SequenceRules`` matching the given sequence rule query.

        :param sequence_rule_query: the sequence rule query
        :type sequence_rule_query: ``osid.assessment.authoring.SequenceRuleQuery``
        :return: the returned ``SequenceRuleList``
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList


class SequenceRuleSearchSession:
    """This session provides methods for searching among ``SequenceRule`` objects.

    The search query is constructed using the ``SequenceRuleyQuery``.

    ``get_sequence_rules_by_query()`` is the basic search method and
    returns a list of ``SequenceRules``. A more advanced search may be
    performed with ``getSequenceRulesBySearch()``. It accepts a
    ``SequenceRuleSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    workflow. ``get_sequence_rules_by_search()`` returns a
    ``SequenceRuleSearchResults`` that can be used to access the
    resulting ``SequenceRuleList`` or be used to perform a search within
    the result set through ``SequenceRuleSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include sequence rule in bank of
        which this bank matchmaker is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to sequence rule in
        this bank


    ``SequenceRules`` may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``SequenceRuleQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rule_search(self):
        """Gets a sequence rule search.

        :return: the sequence rule search
        :rtype: ``osid.assessment.authoring.SequenceRuleSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleSearch

    sequence_rule_search = property(fget=get_sequence_rule_search)

    @abc.abstractmethod
    def get_sequence_rule_search_order(self):
        """Gets a sequence rule search order.

        The ``SequenceRuleSearchOrder`` is supplied to a
        ``SequenceRuleSearch`` to specify the ordering of results.

        :return: the sequence rule search order
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleSearchOrder

    sequence_rule_search_order = property(fget=get_sequence_rule_search_order)

    @abc.abstractmethod
    def get_sequence_rules_by_search(self, sequence_rule_query, sequence_rule_search):
        """Gets the search results matching the given search query using the given search.

        :param sequence_rule_query: the sequence rule query
        :type sequence_rule_query: ``osid.assessment.authoring.SequenceRuleQuery``
        :param sequence_rule_search: the sequence rule search
        :type sequence_rule_search: ``osid.assessment.authoring.SequenceRuleSearch``
        :return: the returned search results
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchResults``
        :raise: ``NullArgument`` -- ``sequence_rule_query`` or ``sequence_rule_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_query`` or ``sequence_rule_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleSearchResults

    @abc.abstractmethod
    def get_sequence_rule_query_from_inspector(self, sequence_rule_query_inspector):
        """Gets a sequence rule query from an inspector.

        The inspector is available from a ``SequenceRuleSearchResults``.

        :param sequence_rule_query_inspector: a sequence rule query inspector
        :type sequence_rule_query_inspector: ``osid.assessment.authoring.SequenceRuleQueryInspector``
        :return: the sequence rule query
        :rtype: ``osid.assessment.authoring.SequenceRuleQuery``
        :raise: ``NullArgument`` -- ``sequence_rule_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``sequence_rule_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleQuery


class SequenceRuleAdminSession:
    """This session creates and removes sequence rules.

    The data for create and update is provided via the
    ``SequenceRuleForm``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_sequence_rule(self):
        """Tests if this user can create sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_sequence_rule_with_record_types(self, sequence_rule_record_types):
        """Tests if this user can create a single ``SequenceRule`` using the desired record types.

        While
        ``AssessmentAuthoringManager.getSequenceRuleRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``SequenceRule``. Providing an empty array tests if a
        ``SequenceRule`` can be created with no records.

        :param sequence_rule_record_types: array of sequence rule record types
        :type sequence_rule_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``SequenceRule`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_sequence_rule_form_for_create(self, assessment_part_id, next_assessment_part_id, sequence_rule_record_types):
        """Gets the sequence rule form for creating new sequence rules between two assessment parts.

        A new form should be requested for each create transaction.

        :param assessment_part_id: the source assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param next_assessment_part_id: the target assessment part ``Id``
        :type next_assessment_part_id: ``osid.id.Id``
        :param sequence_rule_record_types: array of sequence rule record types
        :type sequence_rule_record_types: ``osid.type.Type[]``
        :return: the sequence rule form
        :rtype: ``osid.assessment.authoring.SequenceRuleForm``
        :raise: ``InvalidArgument`` -- ``assessment_part_id`` and ``next_assessment_part_id`` not on the same assessment
        :raise: ``NotFound`` -- ``assessment_part_id`` or ``next_assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id, next_assessment_part_id`` , or ``sequence_rule_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleForm

    @abc.abstractmethod
    def create_sequence_rule(self, sequence_rule_form):
        """Creates a new ``SequenceRule``.

        :param sequence_rule_form: the form for this ``SequenceRule``
        :type sequence_rule_form: ``osid.assessment.authoring.SequenceRuleForm``
        :return: the new ``SequenceRule``
        :rtype: ``osid.assessment.authoring.SequenceRule``
        :raise: ``IllegalState`` -- ``sequence_rule_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``sequence_rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_form`` did not originate from ``get_sequence_rule_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRule

    @abc.abstractmethod
    def can_update_sequence_rules(self):
        """Tests if this user can update sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_sequence_rule_form_for_update(self, sequence_rule_id):
        """Gets the sequence rule form for updating an existing sequence rule.

        A new sequence rule form should be requested for each update
        transaction.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: the sequence rule form
        :rtype: ``osid.assessment.authoring.SequenceRuleForm``
        :raise: ``NotFound`` -- ``sequence_rule_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleForm

    @abc.abstractmethod
    def update_sequence_rule(self, sequence_rule_form):
        """Updates an existing sequence rule.

        :param sequence_rule_form: the form containing the elements to be updated
        :type sequence_rule_form: ``osid.assessment.authoring.SequenceRuleForm``
        :raise: ``IllegalState`` -- ``sequence_rule_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``sequence_rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_form`` did not originate from ``get_sequence_rule_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_sequence_rules(self):
        """Tests if this user can delete sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_sequence_rule(self, sequence_rule_id):
        """Deletes a ``SequenceRule``.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule`` to remove
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_sequence_rule_aliases(self):
        """Tests if this user can manage ``Id`` aliases for sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_sequence_rule(self, sequence_rule_id, alias_id):
        """Adds a ``Id`` to a ``SequenceRule`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``SequenceRule`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another sequence rule. it
        is reassigned to the given sequence rule ``Id``.

        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_sequence_sequence_rules(self):
        """Tests if this user can order ``SequenceRules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known sequencing operations
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer sequencing
        operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` ordering is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def move_sequence_rule_ahead(self, sequence_rule_id, assessment_part_id, reference_id):
        """Reorders sequence rule for a source assessment part by moving the specified sequence rule in front of a reference sequence rule.

        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: the reference sequence rule ``Id``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` not found or, ``sequence_rule_id`` or ``reference_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def move_sequence_rule_behind(self, sequence_rule_id, assessment_part_id, reference_id):
        """Reorders sequence rule for a source assessment part by moving the specified sequence rule behind a reference sequence rule.

        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: the reference sequence rule ``Id``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` not found or, ``sequence_rule_id`` or ``reference_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_sequence_rules(self, sequence_rule_ids, assessment_part_id):
        """Reorders a set of sequence rules for an assessment part.

        :param sequence_rule_ids: the ``Ids`` for a set of ``SequenceRules``
        :type sequence_rule_ids: ``osid.id.Id[]``
        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found or, a ``sequence_rule_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``sequence_rule_ids`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``SequenceRule`` objects in this ``Bank``.

    This also includes existing ``SequenceRules`` that may appear or
    disappear due to changes in the ``Bank`` hierarchy, This session is
    intended for consumers needing to synchronize their state with this
    service without the use of polling. Notifications are cancelled when
    this session is closed.

    The two views defined in this session correspond to the views in the
    ``SequenceRuleLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_sequence_rule_notifications(self):
        """Tests if this user can register for ``SequenceRule`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include in banks which are children of
        this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_sequence_rule_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_sequence_rule_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_sequence_rule_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_sequence_rule_notification(self, notification_id):
        """Acknowledge a sequence rule notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_sequence_rules(self):
        """Register for notifications of new sequence rules.

        ``SequenceRuleReceiver.newSequenceRules()`` is invoked when a
        new ``SequenceRule`` appears in this bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_sequence_rules_for_assessment_part(self, assessment_part_id):
        """Register for notifications of new sequence rules for the given assessment part.

        ``SequenceRuleReceiver.newSequenceRules()`` is invoked when a
        new ``SequenceRule`` appears in this bank.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_sequence_rules_for_next_assessment_part(self, assessment_part_id):
        """Register for notifications of new sequence rules for the given assessment part.

        ``SequenceRuleReceiver.newSequenceRules()`` is invoked when a
        new ``SequenceRule`` appears in this bank.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_sequence_rules(self):
        """Registers for notification of updated sequence rules.

        ``SequenceRuleReceiver.changedSequenceRules()`` is invoked when
        a sequence rule in this bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_sequence_rules_for_assessment_part(self, assessment_part_id):
        """Register for notifications of updated sequence rules for the given assessment part.

        ``SequenceRuleReceiver.changedSequenceRules()`` is invoked when
        a new ``SequenceRule`` in this bank is changed.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_sequence_rules_for_next_assessment_part(self, assessment_part_id):
        """Register for notifications of updated sequence rules for the given assessment part.

        ``SequenceRuleReceiver.changedSequenceRules()`` is invoked when
        a new ``SequenceRule`` in this bank is changed.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_sequence_rule(self, sequence_rule_id):
        """Registers for notification of an updated sequence rule.

        ``ProvisionableReceiver.changedSequenceRules()`` is invoked when
        the specified sequence rule in this bank is changed.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule`` to monitor
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_sequence_rules(self):
        """Registers for notification of deleted sequence rules.

        ``SequenceRuleReceiver.deletedSequenceRules()`` is invoked when
        a sequence rule is deleted or removed from this bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_sequence_rules_for_assessment_part(self, assessment_part_id):
        """Registers for notification of deleted sequence rules for the given assessment part.

        ``SequenceRuleReceiver.deletedSequenceRule()`` is invoked when a
        sequence rule is deleted or removed from this bank.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_sequence_rules_for_next_assessment_part(self, assessment_part_id):
        """Registers for notification of deleted sequence rules for the given assessment part.

        ``SequenceRuleReceiver.deletedSequenceRule()`` is invoked when a
        sequence rule is deleted or removed from this bank.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to monitor
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_sequence_rule(self, sequence_rule_id):
        """Registers for notification of a deleted sequence rule.

        ``SequenceRuleReceiver.deletedSequenceRule()`` is invoked when
        the specified sequence rule is deleted or removed from this
        bank.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule`` to monitor
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_sequence_rule_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_sequence_rule_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_sequence_rule_notification(self, notification_id):
        """Acknowledge an sequence_rule notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleBankSession:
    """This session provides methods to retrieve ``SequenceRule`` to ``Bank`` mappings.

    a ``SequenceRule`` may appear in multiple ``Bank`` objects. Each
    bank may have its own authorizations governing who is allowed to
    look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_sequence_rule_bank_mappings(self):
        """Tests if this user can perform lookups of sequence rule/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_sequence_rule_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_sequence_rule_bank_view(self):
        """A complete view of the ``SequenceRule`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_ids_by_bank(self, bank_id):
        """Gets the list of ``SequenceRuleIds`` associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related sequence rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_sequence_rules_by_bank(self, bank_id):
        """Gets the list of sequence rule associated with a ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related sequence rules
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_sequence_rule_ids_by_banks(self, bank_ids):
        """Gets the list of ``SequenceRule Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of sequence rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_sequence_rules_by_banks(self, bank_ids):
        """Gets the list of sequence rule corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of sequence rules
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList

    @abc.abstractmethod
    def get_bank_ids_by_sequence_rule(self, sequence_rule_id):
        """Gets the ``Bank``  ``Ids`` mapped to a ``SequenceRule``.

        :param sequence_rule_id: ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``sequence_rule_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_sequence_rule(self, sequence_rule_id):
        """Gets the ``Banks`` mapped to a ``SequenceRule``.

        :param sequence_rule_id: ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``sequence_rule_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class SequenceRuleBankAssignmentSession:
    """This session provides methods to re-assign ``SequenceRule`` to ``Bank`` mappings.

    a ``SequenceRule`` may appear in multiple ``Bank`` objects and
    removing the last reference to a ``SequenceRule`` is the equivalent
    of deleting it. Each ``Bank`` may have its own authorizations
    governing who is allowed to operate on it.

    Adding a reference of a ``SequenceRule`` to another ``Bank`` is not
    a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_sequence_rules(self):
        """Tests if this user can alter sequence rule/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_sequence_rules_to_bank(self, bank_id):
        """Tests if this user can alter sequence rule/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of bank including and under the given bank node in which any sequence rule can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_sequence_rule(self, bank_id, sequence_rule_id):
        """Gets a list of bank including and under the given bank node in which a specific sequence rule can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_sequence_rule_to_bank(self, sequence_rule_id, bank_id):
        """Adds an existing ``SequenceRule`` to a ``Bank``.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``sequence_rule_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``sequence_rule_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_sequence_rule_from_bank(self, sequence_rule_id, bank_id):
        """Removes a ``SequenceRule`` from a ``Bank``.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id`` or ``bank_id`` not found or ``sequence_rule_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``sequence_rule_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_sequence_rule_to_bank(self, sequence_rule_id, from_bank_id, to_bank_id):
        """Moves a ``SequenceRule`` from one ``Bank`` to another.

        Mappings to other ``Banks`` are unaffected.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param from_bank_id: the ``Id`` of the current ``Bank``
        :type from_bank_id: ``osid.id.Id``
        :param to_bank_id: the ``Id`` of the destination ``Bank``
        :type to_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id, from_bank_id,`` or ``to_bank_id`` not found or ``sequence_rule_id`` not mapped to ``from_bank_id``
        :raise: ``NullArgument`` -- ``sequence_rule_id, from_bank_id,`` or ``to_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic bank.

    a ``SequenceRuleQuery`` can be retrieved from this session and
    mapped to this ``Bank`` to create a virtual collection of sequence
    rules. The sequence rule may be sequenced using the
    ``SequenceRuleSearchOrder`` from this session.

    This ``Bank`` has a default query that matches any sequence rule and
    a default search order that specifies no sequencing. The queries may
    be examined using a ``SequenceRuleQueryInspector``. The query may be
    modified by converting the inspector back to a
    ``SequenceRuleQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart bank.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_sequence_rule_query(self):
        """Gets a sequence rule query.

        :return: the sequence rule query
        :rtype: ``osid.assessment.authoring.SequenceRuleQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleQuery

    sequence_rule_query = property(fget=get_sequence_rule_query)

    @abc.abstractmethod
    def get_sequence_rule_search_order(self):
        """Gets a sequence rule search order.

        :return: the sequence rule search order
        :rtype: ``osid.assessment.authoring.SequenceRuleSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleSearchOrder

    sequence_rule_search_order = property(fget=get_sequence_rule_search_order)

    @abc.abstractmethod
    def apply_sequence_rule_query(self, sequence_rule_query):
        """Applies a sequence rule query to this bank.

        :param sequence_rule_query: the sequence rule query
        :type sequence_rule_query: ``osid.assessment.authoring.SequenceRuleQuery``
        :raise: ``NullArgument`` -- ``sequence_rule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``sequence_rule_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_sequence_rule_query(self):
        """Gets a sequence rule query inspector for this bank.

        :return: the sequence rule query inspector
        :rtype: ``osid.assessment.authoring.SequenceRuleQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleQueryInspector

    @abc.abstractmethod
    def apply_sequence_rule_sequencing(self, sequence_rule_search_order):
        """Applies a sequence rule search order to this bank.

        :param sequence_rule_search_order: the sequence rule search order
        :type sequence_rule_search_order: ``osid.assessment.authoring.SequenceRuleSearchOrder``
        :raise: ``NullArgument`` -- ``sequence_rule_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``sequence_rule_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_query_from_inspector(self, sequence_rule_query_inspector):
        """Gets a sequence rule query from an inspector.

        :param sequence_rule_query_inspector: a sequence rule query inspector
        :type sequence_rule_query_inspector: ``osid.assessment.authoring.SequenceRuleQueryInspector``
        :return: the sequence rule query
        :rtype: ``osid.assessment.authoring.SequenceRuleQuery``
        :raise: ``NullArgument`` -- ``sequence_rule_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``sequence_rule_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleQuery


class SequenceRuleEnablerLookupSession:
    """This session provides methods for retrieving ``SequenceRuleEnablers``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_sequence_rule_enablers(self):
        """Tests if this user can perform ``SequenceRuleEnablers`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_sequence_rule_enabler_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_sequence_rule_enabler_view(self):
        """A complete view of the ``SequenceRuleEnabler`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule enablers in banks
        which are children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_active_sequence_rule_enabler_view(self):
        """Only active sequence rule enablers are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_status_sequence_rule_enabler_view(self):
        """All active and inactive sequence rule enablers are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Gets the ``SequenceRuleEnabler`` specified by its ``Id``.

        :param sequence_rule_enabler_id: ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: the sequence rule enabler
        :rtype: ``osid.assessment.authoring.SequenceRuleEnabler``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnabler

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_ids(self, sequence_rule_enabler_ids):
        """Gets a ``SequenceRuleEnablerList`` corresponding to the given ``IdList``.

        :param sequence_rule_enabler_ids: the list of ``Ids`` to retrieve
        :type sequence_rule_enabler_ids: ``osid.id.IdList``
        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NotFound`` -- a ``Id was`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_genus_type(self, sequence_rule_enabler_genus_type):
        """Gets a ``SequenceRuleEnablerList`` corresponding to the given sequence rule enabler genus ``Type`` which does not include sequence rule enablers of genus types derived from the specified ``Type``.

        :param sequence_rule_enabler_genus_type: a sequence rule enabler genus type
        :type sequence_rule_enabler_genus_type: ``osid.type.Type``
        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_parent_genus_type(self, sequence_rule_enabler_genus_type):
        """Gets a ``SequenceRuleEnablerList`` corresponding to the given sequence rule enabler genus ``Type`` and include any additional sequence rule enablers with genus types derived from the specified ``Type``.

        :param sequence_rule_enabler_genus_type: a sequence rule enabler genus type
        :type sequence_rule_enabler_genus_type: ``osid.type.Type``
        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_record_type(self, sequence_rule_enabler_record_type):
        """Gets a ``SequenceRuleEnablerList`` containing the given sequence rule enabler record ``Type``.

        :param sequence_rule_enabler_record_type: a sequence rule enabler record type
        :type sequence_rule_enabler_record_type: ``osid.type.Type``
        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enablers_on_date(self, from_, to):
        """Gets a ``SequenceRuleEnablerList`` that are effective for the entire given date range inclusive but not confined to the date range for any agent.

        :param from: a start date
        :type from: ``osid.calendaring.DateTime``
        :param to: an end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``InvalidArgument`` -- ``from`` is greater tha ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enablers_on_date_with_agent(self, agent_id, from_, to):
        """Gets a ``SequenceRuleEnablerList`` that are effective for the entire given date range inclusive but not confined to the date range and evaluated against the given agent.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param from: a start date
        :type from: ``osid.calendaring.DateTime``
        :param to: an end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``InvalidArgument`` -- ``from`` is greater tha ``to``
        :raise: ``NullArgument`` -- ``agent_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enablers(self):
        """Gets all ``SequenceRuleEnablers``.

        :return: the returned ``SequenceRuleEnabler`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    sequence_rule_enablers = property(fget=get_sequence_rule_enablers)


class SequenceRuleEnablerQuerySession:
    """This session provides methods for searching among ``SequenceRuleEnabler`` objects.

    The search query is constructed using the
    ``SequenceRuleEnablerQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include sequence rule enablers in
        bank of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to sequence rule
        enablers in this bank


    sequence rule enablers may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``SequenceRuleEnablerQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_search_sequence_rule_enablers(self):
        """Tests if this user can perform ``SequenceRuleEnabler`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule enablers in banks
        which are children of this step in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_enabler_query(self):
        """Gets a sequence rule enabler query.

        :return: the sequence rule enabler query
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerQuery

    sequence_rule_enabler_query = property(fget=get_sequence_rule_enabler_query)

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_query(self, sequence_rule_enabler_query):
        """Gets a list of ``SequenceRuleEnablers`` matching the given sequence rule enabler query.

        :param sequence_rule_enabler_query: the sesequence rule enabler query
        :type sequence_rule_enabler_query: ``osid.assessment.authoring.SequenceRuleEnablerQuery``
        :return: the returned ``SequenceRuleEnablerList``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList


class SequenceRuleEnablerSearchSession:
    """This session provides methods for searching among ``SequenceRuleEnabler`` objects.

    The search query is constructed using the
    ``SequenceRuleEnableryQuery``.

    ``get_sequence_rule_enablers_by_query()`` is the basic search method
    and returns a list of ``SequenceRuleEnablers``. A more advanced
    search may be performed with ``getSequenceRuleEnablersBySearch()``.
    It accepts a ``SequenceRuleEnablerSearch`` in addition to the query
    for the purpose of specifying additional options affecting the
    entire search, such as workflow.
    ``get_sequence_rule_enablers_by_search()`` returns a
    ``SequenceRuleEnablerSearchResults`` that can be used to access the
    resulting ``SequenceRuleEnablerList`` or be used to perform a search
    within the result set through ``SequenceRuleEnablerSearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include sequence rule enablers in
        bank of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to sequence rule
        enablers in this bank


    ``SequenceRuleEnablers`` may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``SequenceRuleEnablerQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_sequence_rule_enabler_search(self):
        """Gets a sequence rule enabler search.

        :return: the sequence rule enabler search
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerSearch

    sequence_rule_enabler_search = property(fget=get_sequence_rule_enabler_search)

    @abc.abstractmethod
    def get_sequence_rule_enabler_search_order(self):
        """Gets a sequence rule enabler search order.

        The ``SequenceRuleEnablerSearchOrder`` is supplied to a
        ``SequenceRuleEnablerSearch`` to specify the ordering of
        results.

        :return: the sequence rule enabler search order
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerSearchOrder

    sequence_rule_enabler_search_order = property(fget=get_sequence_rule_enabler_search_order)

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_search(self, sequence_rule_enabler_query, sequence_rule_enabler_search):
        """Gets the search results matching the given search query using the given search.

        :param sequence_rule_enabler_query: the sequence rule enabler query
        :type sequence_rule_enabler_query: ``osid.assessment.authoring.SequenceRuleEnablerQuery``
        :param sequence_rule_enabler_search: the sequence rule enabler search
        :type sequence_rule_enabler_search: ``osid.assessment.authoring.SequenceRuleEnablerSearch``
        :return: the returned search results
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchResults``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_query`` or ``sequence_rule_enabler_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_query`` or ``sequence_rule_enabler_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerSearchResults

    @abc.abstractmethod
    def get_sequence_rule_enabler_query_from_inspector(self, sequence_rule_enabler_query_inspector):
        """Gets a sequence rule enabler query from an inspector.

        The inspector is available from a
        ``SequenceRuleEnablerSearchResults``.

        :param sequence_rule_enabler_query_inspector: a sequence rule enabler query inspector
        :type sequence_rule_enabler_query_inspector: ``osid.assessment.authoring.SequenceRuleEnablerQueryInspector``
        :return: the sequence rule enabler query
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuery``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerQuery


class SequenceRuleEnablerAdminSession:
    """This session creates and removes sequence rule enablers.

    The data for create and update is provided via the
    ``SequenceRuleEnablerForm``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_create_sequence_rule_enabler(self):
        """Tests if this user can create sequence rule enablers.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``SequenceRuleEnabler`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``SequenceRuleEnabler`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_sequence_rule_enabler_with_record_types(self, sequence_rule_enabler_record_types):
        """Tests if this user can create a single ``SequenceRuleEnabler`` using the desired record types.

        While ``AssessmentAuthoringManag
        er.getSequenceRuleEnablerRecordTypes()`` can be used to examine
        which records are supported, this method tests which record(s)
        are required for creating a specific ``SequenceRuleEnabler``.
        Providing an empty array tests if a ``SequenceRuleEnabler`` can
        be created with no records.

        :param sequence_rule_enabler_record_types: array of sequence rule enabler record types
        :type sequence_rule_enabler_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``SequenceRuleEnabler`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_sequence_rule_enabler_form_for_create(self, sequence_rule_enabler_record_types):
        """Gets the sequence rule enabler form for creating new sequence rule enablers.

        A new form should be requested for each create transaction.

        :param sequence_rule_enabler_record_types: array of sequence rule enabler record types
        :type sequence_rule_enabler_record_types: ``osid.type.Type[]``
        :return: the sequence rule enabler form
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerForm``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerForm

    @abc.abstractmethod
    def create_sequence_rule_enabler(self, sequence_rule_enabler_form):
        """Creates a new ``SequenceRuleEnabler``.

        :param sequence_rule_enabler_form: the form for this ``SequenceRuleEnabler``
        :type sequence_rule_enabler_form: ``osid.assessment.authoring.SequenceRuleEnablerForm``
        :return: the new ``SequenceRuleEnabler``
        :rtype: ``osid.assessment.authoring.SequenceRuleEnabler``
        :raise: ``IllegalState`` -- ``sequence_rule_enabler_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_form`` did not originate from ``get_sequence_rule_enabler_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnabler

    @abc.abstractmethod
    def can_update_sequence_rule_enablers(self):
        """Tests if this user can update sequence rule enablers.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``SequenceRuleEnabler`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if ``SequenceRuleEnabler`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_sequence_rule_enabler_form_for_update(self, sequence_rule_enabler_id):
        """Gets the sequence rule enabler form for updating an existing sequence rule enabler.

        A new sequence rule enabler form should be requested for each
        update transaction.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: the sequence rule enabler form
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerForm``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerForm

    @abc.abstractmethod
    def update_sequence_rule_enabler(self, sequence_rule_enabler_form):
        """Updates an existing sequence rule enabler.

        :param sequence_rule_enabler_form: the form containing the elements to be updated
        :type sequence_rule_enabler_form: ``osid.assessment.authoring.SequenceRuleEnablerForm``
        :raise: ``IllegalState`` -- ``sequence_rule_enabler_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_form`` did not originate from ``get_sequence_rule_enabler_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_sequence_rule_enablers(self):
        """Tests if this user can delete sequence rule enablers.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``SequenceRuleEnabler`` will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``SequenceRuleEnabler`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Deletes a ``SequenceRuleEnabler``.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler`` to remove
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_sequence_rule_enabler_aliases(self):
        """Tests if this user can manage ``Id`` aliases for sequence rule enablers.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``SequenceRuleEnabler`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_sequence_rule_enabler(self, sequence_rule_enabler_id, alias_id):
        """Adds a ``Id`` to a ``SequenceRuleEnabler`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``SequenceRuleEnabler`` is determined
        by the provider. The new ``Id`` performs as an alias to the
        primary ``Id`` . If the alias is a pointer to another sequence
        rule enabler. it is reassigned to the given sequence rule
        enabler ``Id``.

        :param sequence_rule_enabler_id: the ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleEnablerNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``SequenceRuleEnabler`` objects in this ``Bank``.

    This also includes existing ``SequenceRuleEnablers`` that may appear
    or disappear due to changes in the ``Bank`` hierarchy, This session
    is intended for consumers needing to synchronize their state with
    this service without the use of polling. Notifications are cancelled
    when this session is closed.

    The two views defined in this session correspond to the views in the
    ``SequenceRuleEnablerLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_register_for_sequence_rule_enabler_notifications(self):
        """Tests if this user can register for ``SequenceRuleEnabler`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include enablers in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_sequence_rule_enabler_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_sequence_rule_enabler_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_sequence_rule_enabler_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_sequence_rule_enabler_notification(self, notification_id):
        """Acknowledge a sequence rule enabler notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_sequence_rule_enablers(self):
        """Register for notifications of new sequence rule enablers.

        ``SequenceRuleEnablerReceiver.newSequenceRuleEnablers()`` is
        invoked when a new ``SequenceRuleEnabler`` appears in this bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_sequence_rule_enablers(self):
        """Registers for notification of updated bank enabelrs.

        ``SequenceRuleEnablerReceiver.changedSequenceRuleEnablers()`` is
        invoked when a sequence rule enabler in this bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Registers for notification of an updated sequence rule enabler.

        ``ProvisionableReceiver.changedSequenceRuleEnablers()`` is
        invoked when the specified sequence rule enabler in this bank is
        changed.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler`` to monitor
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_sequence_rule_enablers(self):
        """Registers for notification of deleted sequence rule enablers.

        ``SequenceRuleEnablerReceiver.deletedSequenceRuleEnablers()`` is
        invoked when a sequence rule enabler is deleted or removed from
        this bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Registers for notification of a deleted sequence rule enabler.

        ``SequenceRuleEnablerReceiver.deletedSequenceRuleEnablers()`` is
        invoked when the specified sequence rule enabler is deleted or
        removed from this bank.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler`` to monitor
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_sequence_rule_enabler_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_sequence_rule_enabler_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_sequence_rule_enabler_notification(self, notification_id):
        """Acknowledge an sequence_rule_enabler notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleEnablerBankSession:
    """This session provides methods to retrieve ``SequenceRuleEnabler`` to ``Bank`` mappings.

    a ``SequenceRuleEnabler`` may appear in multiple ``Bank`` objects.
    Each bank may have its own authorizations governing who is allowed
    to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_sequence_rule_enabler_bank_mappings(self):
        """Tests if this user can perform lookups of sequence rule enabler/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_sequence_rule_enabler_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_sequence_rule_enabler_bank_view(self):
        """A complete view of the ``SequenceRuleEnabler`` and ``Bank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_enabler_ids_by_bank(self, bank_id):
        """Gets the list of ``SequenceRuleEnablerIds`` associated with an ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related sequence rule enabler ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_bank(self, bank_id):
        """Gets the list of sequence rule enablers associated with an ``Bank``.

        :param bank_id: ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of related sequence rule enablers
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NotFound`` -- ``bank_id`` is not found
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_enabler_ids_by_banks(self, bank_ids):
        """Gets the list of ``SequenceRuleEnabler Ids`` corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of sequence rule enabler ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_sequence_rule_enablers_by_banks(self, bank_ids):
        """Gets the list of sequence rule enablers corresponding to a list of ``Banks``.

        :param bank_ids: list of bank ``Ids``
        :type bank_ids: ``osid.id.IdList``
        :return: list of sequence rule enablers
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NullArgument`` -- ``bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_bank_ids_by_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Gets the ``Bank``  ``Ids`` mapped to a ``SequenceRuleEnabler``.

        :param sequence_rule_enabler_id: ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_banks_by_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Gets the ``Banks`` mapped to a ``SequenceRuleEnabler``.

        :param sequence_rule_enabler_id: ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: list of banks
        :rtype: ``osid.assessment.BankList``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.BankList


class SequenceRuleEnablerBankAssignmentSession:
    """This session provides methods to re-assign ``SequenceRuleEnabler`` to ``Bank`` mappings.

    a ``SequenceRuleEnabler`` may appear in multiple ``Bank`` objects
    and removing the last reference to a ``SequenceRuleEnabler`` is the
    equivalent of deleting it. Each ``Bank`` may have its own
    authorizations governing who is allowed to operate on it.

    Adding a reference of a ``SequenceRuleEnabler`` to another ``Bank``
    is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_sequence_rule_enablers(self):
        """Tests if this user can alter sequence rule enabler/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_sequence_rule_enablers_to_bank(self, bank_id):
        """Tests if this user can alter sequence rule enabler/bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_bank_ids(self, bank_id):
        """Gets a list of bank including and under the given bank node in which any sequence rule enabler can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_bank_ids_for_sequence_rule_enabler(self, bank_id, sequence_rule_enabler_id):
        """Gets a list of bank including and under the given bank node in which a specific sequence rule enabler can be assigned.

        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: list of assignable bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bank_id`` or ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_sequence_rule_enabler_to_bank(self, sequence_rule_enabler_id, bank_id):
        """Adds an existing ``SequenceRuleEnabler`` to a ``Bank``.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``sequence_rule_enabler_id`` is already assigned to ``bank_id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` or ``bank_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_sequence_rule_enabler_from_bank(self, sequence_rule_enabler_id, bank_id):
        """Removes a ``SequenceRuleEnabler`` from a ``Bank``.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param bank_id: the ``Id`` of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` or ``bank_id`` not found or ``sequence_rule_enabler_id`` not assigned to ``bank_id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` or ``bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleEnablerSmartBankSession:
    """This session manages queries and sequencing to create "smart" dynamic bank.

    a ``SequenceRuleEnablerQuery`` can be retrieved from this session
    and mapped to this ``Bank`` to create a virtual collection of
    sequence rule enablers. The sequence rule enablers may be sequenced
    using the ``SequenceRuleEnablerSearchOrder`` from this session.

    This ``Bank`` has a default query that matches any sequence rule
    enabler and a default search order that specifies no sequencing. The
    queries may be examined using a
    ``SequenceRuleEnablerQueryInspector``. The query may be modified by
    converting the inspector back to a ``SequenceRuleEnablerQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_manage_smart_banks(self):
        """Tests if this user can manage smart bank.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_sequence_rule_enabler_query(self):
        """Gets a sequence rule enabler query.

        :return: the sequence rule enabler query
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerQuery

    sequence_rule_enabler_query = property(fget=get_sequence_rule_enabler_query)

    @abc.abstractmethod
    def get_sequence_rule_enabler_search_order(self):
        """Gets a sequence rule enabler search order.

        :return: the sequence rule enabler search order
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerSearchOrder

    sequence_rule_enabler_search_order = property(fget=get_sequence_rule_enabler_search_order)

    @abc.abstractmethod
    def apply_sequence_rule_enabler_query(self, sequence_rule_enabler_query):
        """Applies a sequence rule enabler query to this bank.

        :param sequence_rule_enabler_query: the sequence rule enabler query
        :type sequence_rule_enabler_query: ``osid.assessment.authoring.SequenceRuleEnablerQuery``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_sequence_rule_enabler_query(self):
        """Gets a sequence rule enabler query inspector for this bank.

        :return: the sequence rule enabler query inspector
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerQueryInspector

    @abc.abstractmethod
    def apply_sequence_rule_enabler_sequencing(self, sequence_rule_enabler_search_order):
        """Applies a sequence rule enabler search order to this bank.

        :param sequence_rule_enabler_search_order: the sequence rule enabler search order
        :type sequence_rule_enabler_search_order: ``osid.assessment.authoring.SequenceRuleEnablerSearchOrder``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_enabler_query_from_inspector(self, sequence_rule_enabler_query_inspector):
        """Gets a sequence rule enabler query from an inspector.

        :param sequence_rule_enabler_query_inspector: a sequence rule enabler query inspector
        :type sequence_rule_enabler_query_inspector: ``osid.assessment.authoring.SequenceRuleEnablerQueryInspector``
        :return: the sequence rule enabler query
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerQuery``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``sequence_rule_enabler_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerQuery


class SequenceRuleEnablerRuleLookupSession:
    """This session provides methods to retrieve ``SequenceRuleEnabler`` to ``SequenceRule`` mappings.

    a ``Step`` with multiple ``SequenceRuleEnablers`` means any positive
    rule evaluation across the enablers result in an effective
    ``SequenceRule``.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated bank view: All methods in this session operate,
        retrieve and pertain sequence rule enablers defined explicitly
        in the current bank
      * federated bank view: All methods in this session operate,
        retrieve and pertain to all sequence rule enablers defined in
        this bank and any other sequence rule enablers implicitly
        available in this bank through bank inheritence.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_lookup_sequence_rule_enabler_rules(self):
        """Tests if this user can perform lookups of sequence rule enabler/sequence rule mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_sequence_rule_enabler_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_sequence_rule_enabler_rule_view(self):
        """A complete view of the ``SequenceRuleEnabler`` and ``SequenceRule`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule enablers in banks
        which are children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_sequence_rule_enabler_ids_for_sequence_rule(self, sequence_rule_id):
        """Gets the ``SequenceRuleEnabler Id`` associated with a ``SequenceRule``.

        :param  sequence_rule_id: ``Id`` of the ``SequenceRule``
        :type  sequence_rule_id: ``osid.id.Id``
        :return: the sequence rule enabler ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``sequence_rule_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_sequence_rule_enablers_for_sequence_rule(self, sequence_rule_id):
        """Gets the ``SequenceRuleEnablers`` associated with a ``SequenceRule``.

        :param sequence_rule_id: ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: the sequence rule enablers
        :rtype: ``osid.assessment.authoring.SequenceRuleEnablerList``
        :raise: ``NotFound`` -- ``sequence_rule_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleEnablerList

    @abc.abstractmethod
    def get_sequence_rule_ids_for_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Gets the ``SequenceRule``  ``Ids`` mapped to a ``SequenceRuleEnabler``.

        :param sequence_rule_enabler_id: ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: list of sequence rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_sequence_rules_for_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """Gets the ``SequenceRules`` mapped to a ``SequenceRuleEnabler``.

        :param sequence_rule_enabler_id: ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :return: list of sequence rules
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.authoring.SequenceRuleList


class SequenceRuleEnablerRuleApplicationSession:
    """This session provides methods to apply ``SequenceRuleEnablers`` to ``SequenceRules``.

    a ``SequenceRule`` with multiple ``SequenceRuleEnablers`` means any
    positive rule evaluation across the enablers result in an effective
    ``SequenceRule``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    bank_id = property(fget=get_bank_id)

    @abc.abstractmethod
    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.assessment.Bank

    bank = property(fget=get_bank)

    @abc.abstractmethod
    def can_assign_sequence_rule_enablers(self):
        """Tests if this user can alter sequence rule enabler/sequence rule mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def assign_sequence_rule_enabler_to_sequence_rule(self, sequence_rule_enabler_id, sequence_rule_id):
        """Adds an existing ``SequenceRuleEnabler`` to a ``SequenceRule``.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``sequence_rule_enabler_id`` is already applied to ``sequence_rule_id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` or ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` or ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_sequence_rule_enabler_from_sequence_rule(self, sequence_rule_enabler_id, sequence_rule_id):
        """Removes a ``SequenceRuleEnabler`` from a ``SequenceRule``.

        :param sequence_rule_enabler_id: the ``Id`` of the ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id`` or ``sequence_rule_id`` not found or ``sequence_rule_enabler_id`` not applied to ``sequence_rule_id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id`` or ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_sequence_sequence_rule_enablers(self):
        """Tests if this user can order ``SequenceRuleEnablers``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known sequencing operations
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer sequencing
        operations to an unauthorized user.

        :return: ``false`` if ``SequenceRuleEnabler`` ordering is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def move_sequence_rule_enabler_ahead(self, sequence_rule_enabler_id, sequence_rule_id, reference_id):
        """Reorders sequence rule enablers for a sequence rule by moving the specified sequence rule enabler in front of a reference sequence rule enabler.

        :param sequence_rule_enabler_id: the ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param reference_id: the reference sequence rule enabler ``Id``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id, sequence_rule_id,`` or ``reference_id`` not found or, ``sequence_rule_enabler_id`` or ``reference_id`` not related to ``sequence_rule_id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id, sequence_rule_id,`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def move_sequence_rule_enabler_behind(self, sequence_rule_enabler_id, sequence_rule_id, reference_id):
        """Reorders sequence rule enablers for a sequence rule by moving the specified sequence rule enabler behind a reference sequence rule enabler.

        :param sequence_rule_enabler_id: the ``Id`` of a ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``
        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param reference_id: the reference sequence rule enabler ``Id``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_enabler_id, sequence_rule_id,`` or ``reference_id`` not found or, ``sequence_rule_enabler_id`` or ``reference_id`` not related to ``sequence_rule_id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_id, sequence_rule_id,`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_sequence_rule_enablers(self, sequence_rule_enabler_ids, sequence_rule_id):
        """Reorders a set of sequence rule enablers for a sequence rule.

        :param sequence_rule_enabler_ids: the ``Ids`` for a set of ``SequenceRuleEnablers``
        :type sequence_rule_enabler_ids: ``osid.id.Id[]``
        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found or, an ``sequence_rule_enabler_id`` not related to ``sequence_rule_id``
        :raise: ``NullArgument`` -- ``sequence_rule_enabler_ids`` or ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
