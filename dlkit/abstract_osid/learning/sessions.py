"""Implementations of learning abstract base class sessions."""
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


class ObjectiveLookupSession:
    """This session provides methods for retrieving ``Objective`` s."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_lookup_objectives(self):
        """Tests if this user can perform ``Objective`` lookups.

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
    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_view(self):
        """A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective(self, objective_id):
        """Gets the ``Objective`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Objective`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Objective`` and retained
        for compatibility.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the objective
        :rtype: ``osid.learning.Objective``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.Objective

    @abc.abstractmethod
    def get_objectives_by_ids(self, objective_ids):
        """Gets an ``ObjectiveList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        objectives specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Objectives`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param objective_ids: the list of ``Ids`` to retrieve
        :type objective_ids: ``osid.id.IdList``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objectives_by_genus_type(self, objective_genus_type):
        """Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` which does not include objectives of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :param objective_genus_type: an objective genus type
        :type objective_genus_type: ``osid.type.Type``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objectives_by_parent_genus_type(self, objective_genus_type):
        """Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` and include any additional objective with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session

        :param objective_genus_type: an objective genus type
        :type objective_genus_type: ``osid.type.Type``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objectives_by_record_type(self, objective_record_type):
        """Gets an ``ObjectiveList`` containing the given objective record ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :param objective_record_type: an objective record type
        :type objective_record_type: ``osid.type.Type``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objectives(self):
        """Gets all ``Objectives``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :return: an ``ObjectiveList``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    objectives = property(fget=get_objectives)


class ObjectiveQuerySession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_search_objectives(self):
        """Tests if this user can perform ``Objectives`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective_query(self):
        """Gets an objective query.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQuery

    objective_query = property(fget=get_objective_query)

    @abc.abstractmethod
    def get_objectives_by_query(self, objective_query):
        """Gets a list of ``Objectives`` matching the given objective query.

        :param objective_query: the objective query
        :type objective_query: ``osid.learning.ObjectiveQuery``
        :return: the returned ``ObjectiveList``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList


class ObjectiveSearchSession:
    """This session provides methods for searching ``Objective`` objects.

    The search query is constructed using the ``ObjectiveQuery``. The
    objective record ``Type`` also specifies the record for the
    objective query.

    ``get_objectives_by_query()`` is the basic search method and returns
    a list of ``Objectives``. A more advanced search may be performed
    with ``getObjectivesBySearch()``. It accepts a ``ObjectiveSearch``
    in addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_objectives_by_search()`` returns an ``ObjectiveSearchResults``
    that can be used to access the resulting ``ObjectiveList`` or be
    used to perform a search within the result set through
    ``ObjectiveSearch``.

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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_search(self):
        """Gets an objective search.

        :return: the objective search
        :rtype: ``osid.learning.ObjectiveSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveSearch

    objective_search = property(fget=get_objective_search)

    @abc.abstractmethod
    def get_objective_search_order(self):
        """Gets a n objective search order.

        The ``ObjectiveSearchOrder`` is supplied to an
        ``ObjectiveSearch`` to specify the ordering of results.

        :return: the objective search order
        :rtype: ``osid.learning.ObjectiveSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveSearchOrder

    objective_search_order = property(fget=get_objective_search_order)

    @abc.abstractmethod
    def get_objectives_by_search(self, objective_query, objective_search):
        """Gets the search results matching the given search query using the given search.

        :param objective_query: the objective search query
        :type objective_query: ``osid.learning.ObjectiveQuery``
        :param objective_search: the objective search
        :type objective_search: ``osid.learning.ObjectiveSearch``
        :return: the returned search results
        :rtype: ``osid.learning.ObjectiveSearchResults``
        :raise: ``NullArgument`` -- ``objective_query`` or ``objective_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_search`` or ``objective_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveSearchResults

    @abc.abstractmethod
    def get_objective_query_from_inspector(self, objective_query_inspector):
        """Gets an objective query from an inspector.

        The inspector is available from an ``ObjectiveSearchResults``.

        :param objective_query_inspector: an objective bank query inspector
        :type objective_query_inspector: ``osid.learning.ObjectiveQueryInspector``
        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``NullArgument`` -- ``objective_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``objective_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQuery


class ObjectiveAdminSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_create_objectives(self):
        """Tests if this user can create ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Objective
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Objective`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_objective_with_record_types(self, objective_record_types):
        """Tests if this user can create a single ``Objective`` using the desired record types.

        While ``LearningManager.getObjectiveRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Objective``.
        Providing an empty array tests if an ``Objective`` can be
        created with no records.

        :param objective_record_types: array of objective record types
        :type objective_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Objective`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_form_for_create(self, objective_record_types):
        """Gets the objective form for creating new objectives.

        A new form should be requested for each create transaction.

        :param objective_record_types: array of objective record types
        :type objective_record_types: ``osid.type.Type[]``
        :return: the objective form
        :rtype: ``osid.learning.ObjectiveForm``
        :raise: ``NullArgument`` -- ``objective_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveForm

    @abc.abstractmethod
    def create_objective(self, objective_form):
        """Creates a new ``Objective``.

        :param objective_form: the form for this ``Objective``
        :type objective_form: ``osid.learning.ObjectiveForm``
        :return: the new ``Objective``
        :rtype: ``osid.learning.Objective``
        :raise: ``IllegalState`` -- ``objective_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``objective_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_form`` did not originate from ``get_objective_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Objective

    @abc.abstractmethod
    def can_update_objectives(self):
        """Tests if this user can update ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if objective modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_form_for_update(self, objective_id):
        """Gets the objective form for updating an existing objective.

        A new objective form should be requested for each update
        transaction.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the objective form
        :rtype: ``osid.learning.ObjectiveForm``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveForm

    @abc.abstractmethod
    def update_objective(self, objective_form):
        """Updates an existing objective.

        :param objective_form: the form containing the elements to be updated
        :type objective_form: ``osid.learning.ObjectiveForm``
        :raise: ``IllegalState`` -- ``objective_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``objective_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_form`` did not originate from ``get_objective_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_objectives(self):
        """Tests if this user can delete ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Objective`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_objective(self, objective_id):
        """Deletes the ``Objective`` identified by the given ``Id``.

        :param objective_id: the ``Id`` of the ``Objective`` to delete
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Objective`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_objective_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Objective`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_objective(self, objective_id, alias_id):
        """Adds an ``Id`` to an ``Objective`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Objective`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective, it is
        reassigned to the given objective ``Id``.

        :param objective_id: the ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Objective`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``ObjectiveLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_register_for_objective_notifications(self):
        """Tests if this user can register for ``Objective`` notifications.

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
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for objectives in
        objective banks which are children of this objective bank in the
        objective bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this objective bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_objective_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_objective_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_objective_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_objective_notification(self, notification_id):
        """Acknowledge an objective notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_objectives(self):
        """Register for notifications of new objectives.

        ``ObjectiveReceiver.newObjectives()`` is invoked when a new
        objective is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objectives(self):
        """Registers for notification of updated objectives.

        ``ObjectiveReceiver.changedObjectives()`` is invoked when an
        objective is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective(self, objective_id):
        """Registers for notification of an updated objective.

        ``ObjectiveReceiver.changedObjectives()`` is invoked when the
        specified objective is changed.

        :param objective_id: the ``Id`` of the ``Objective`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_objectives(self):
        """Registers for notification of deleted objectives.

        ``ObjectiveReceiver.deletedObjectives()`` is invoked when an
        objective is removed from this objective bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_objective(self, objective_id):
        """Registers for notification of a deleted objective.

        ``ObjectiveReceiver.changedObjectives()`` is invoked when the
        specified objective is removed from this objective bank.

        :param objective_id: the ``Id`` of the ``Objective`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objectiveid is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_hierarchy(self):
        """Registers for notification of an updated objective hierarchy structure.

        ``ObjectiveReceiver.changedChildOfObjectives()`` is invoked when
        a node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_hierarchy_for_ancestors(self, objective_id):
        """Registers for notification of an updated objective hierarchy structure.

        ``ObjectiveReceiver.changedChildOfObjectives()`` is invoked when
        the specified node or any of its ancestors experiences a change
        in its children.

        :param objective_id: the ``Id`` of the ``Objective`` node to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_hierarchy_for_descendants(self, objective_id):
        """Registers for notification of an updated objective hierarchy structure.

        ``ObjectiveReceiver.changedChildOfObjectives()`` is invoked when
        the specified node or any of its descendants experiences a
        change in its children.

        :param objective_id: the ``Id`` of the ``Objective`` node to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_objective_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_objective_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_objective_notification(self, notification_id):
        """Acknowledge an objective notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveHierarchySession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    @abc.abstractmethod
    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    objective_hierarchy = property(fget=get_objective_hierarchy)

    @abc.abstractmethod
    def can_access_objective_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_objective_view(self):
        """The returns from the objective methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_objective_ids(self):
        """Gets the root objective ``Ids`` in this hierarchy.

        :return: the root objective ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_objective_ids = property(fget=get_root_objective_ids)

    @abc.abstractmethod
    def get_root_objectives(self):
        """Gets the root objective in this objective hierarchy.

        :return: the root objective
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    root_objectives = property(fget=get_root_objectives)

    @abc.abstractmethod
    def has_parent_objectives(self, objective_id):
        """Tests if the ``Objective`` has any parents.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the objective has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is a direct parent of an objective.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_objective_ids(self, objective_id):
        """Gets the parent ``Ids`` of the given objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the objective
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_objectives(self, objective_id):
        """Gets the parents of the given objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: the parents of the objective
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def is_ancestor_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is an ancestor of an objective.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_objectives(self, objective_id):
        """Tests if an objective has any children.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the ``objective_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_objective(self, id_, objective_id):
        """Tests if an objective is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_objective_ids(self, objective_id):
        """Gets the child ``Ids`` of the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :return: the children of the objective
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_objectives(self, objective_id):
        """Gets the children of the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :return: the children of the objective
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def is_descendant_of_objective(self, id_, objective_id):
        """Tests if an ``Id`` is a descendant of an objective.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_node_ids(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_objective_nodes(self, objective_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective.

        :param objective_id: the ``Id`` to query
        :type objective_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an objective node
        :rtype: ``osid.learning.ObjectiveNode``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveNode


class ObjectiveHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Objective`` objects.

    Each node in the hierarchy is a unique ``Objective``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    @abc.abstractmethod
    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    objective_hierarchy = property(fget=get_objective_hierarchy)

    @abc.abstractmethod
    def can_modify_objective_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_objective(self, objective_id):
        """Adds a root objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_objective(self, objective_id):
        """Removes a root objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_objective(self, objective_id, child_id):
        """Adds a child to an objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_objective(self, objective_id, child_id):
        """Removes a child from an objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_objectives(self, objective_id):
        """Removes all children from an objective.

        :param objective_id: the ``Id`` of an objective
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveSequencingSession:
    """This session provides methods to sequence the objectives in the objective hierarchy."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_hierarchy_id = property(fget=get_objective_hierarchy_id)

    @abc.abstractmethod
    def get_objective_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    objective_hierarchy = property(fget=get_objective_hierarchy)

    @abc.abstractmethod
    def can_sequence_objectives(self):
        """Tests if this user can sequence objectives.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if sequencing objectives is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def move_objective_ahead(self, parent_objective_id, reference_objective_id, objective_id):
        """Moves an objective ahead of a refrence objective under the given parent.

        :param parent_objective_id: the ``Id`` of the parent objective
        :type parent_objective_id: ``osid.id.Id``
        :param reference_objective_id: the ``Id`` of the objective
        :type reference_objective_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the objective to move ahead of ``reference_objective_id``
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_objective_id, reference_objective_id,`` or ``objective_id`` not found, or ``reference_objective_id`` or ``objective_id`` is not a child of ``parent_objective_id``
        :raise: ``NullArgument`` -- ``parent_objective_id, reference_objective_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def move_objective_behind(self, parent_objective_id, reference_objective_id, objective_id):
        """Moves an objective behind a refrence objective under the given parent.

        :param parent_objective_id: the ``Id`` of the parent objective
        :type parent_objective_id: ``osid.id.Id``
        :param reference_objective_id: the ``Id`` of the objective
        :type reference_objective_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the objective to move behind ``reference_objective_id``
        :type objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parent_objective_id, reference_objective_id,`` or ``objective_id`` not found, or ``reference_objective_id`` or ``objective_id`` is not a child of ``parent_objective_id``
        :raise: ``NullArgument`` -- ``parent_objective_id, reference_objective_id,`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def sequence_objectives(self, parent_objective_id, objective_ids):
        """Sequences a set of objectives under a parent.

        :param parent_objective_id: the ``Id`` of the parent objective
        :type parent_objective_id: ``osid.id.Id``
        :param objective_ids: the ``Id`` of the objectives
        :type objective_ids: ``osid.id.Id[]``
        :raise: ``NotFound`` -- ``parent_id`` or an ``objective_id`` not found, or an ``objective_id`` is not a child of ``parent_objective_id``
        :raise: ``NullArgument`` -- ``paren_objectivet_id`` or ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveObjectiveBankSession:
    """This session provides methods to retrieve ``Objective`` to ``ObjectiveBank`` mappings.

    An ``Objective`` may appear in multiple ``ObjectiveBanks``. Each
    ``ObjectiveBank`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_objective_objective_bank_mappings(self):
        """Tests if this user can perform lookups of objective/objective bank mappings.

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
    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objectives
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_objectives_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related objective ``Ids``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objective_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objective ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_objectives_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objective_bank_ids_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_objective_banks_by_objective(self, objective_id):
        """Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        :param objective_id: ``Id`` of an ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList


class ObjectiveObjectiveBankAssignmentSession:
    """This session provides methods to re-assign ``Objectives`` to ``ObjectiveBanks``.

    An ``Objective`` may map to multiple ``ObjectiveBanks`` and removing
    the last reference to an ``Objective`` is the equivalent of deleting
    it. Each ``ObjectiveBank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``Objective`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_objectives(self):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_objectives_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any objective can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_objective_bank_ids_for_objective(self, objective_bank_id, objective_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific objective can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_objective_to_objective_bank(self, objective_id, objective_bank_id):
        """Adds an existing ``Objective`` to an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_objective_from_objective_bank(self, objective_id, objective_bank_id):
        """Removes an ``Objective`` from an ``ObjectiveBank``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``objective_bank_id`` not found or ``objective_id`` not mapped to ``objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_proficiency_to_objective_bank(self, objective_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or ``objective_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``objective_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveSmartObjectiveBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``ObjectiveQuery`` can be retrieved from this session and mapped
    to this ``ObjectiveBank`` to create a virtual collection of
    ``Objectives``. The objectives may be sequenced using the
    ``ObjectiveSearchOrder`` from this session.

    This ``ObjectiveBank`` has a default query that matches any
    objective and a default search order that specifies no sequencing.
    The queries may be examined using an ``ObjectiveQueryInspector``.
    The query may be modified by converting the inspector back to an
    ``ObjectiveQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_manage_smart_objective_banks(self):
        """Tests if this user can manage smart objective banks.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart objective bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_query(self):
        """Gets an objective query.

        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQuery

    objective_query = property(fget=get_objective_query)

    @abc.abstractmethod
    def get_objective_search_order(self):
        """Gets an objective search order.

        :return: the objective search order
        :rtype: ``osid.learning.ObjectiveSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveSearchOrder

    objective_search_order = property(fget=get_objective_search_order)

    @abc.abstractmethod
    def apply_objective_query(self, objective_query):
        """Applies an objective query to this bank.

        :param objective_query: the objective query
        :type objective_query: ``osid.learning.ObjectiveQuery``
        :raise: ``NullArgument`` -- ``objective_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``objective_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_objective_query(self):
        """Gets an objective query inspector for this objective bank.

        :return: the objective query inspector
        :rtype: ``osid.learning.ObjectiveQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQueryInspector

    @abc.abstractmethod
    def apply_objective_sequencing(self, objective_search_order):
        """Applies an objective search order to this objective bank.

        :param objective_search_order: the objective search order
        :type objective_search_order: ``osid.learning.ObjectiveSearchOrder``
        :raise: ``NullArgument`` -- ``objective_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``objective_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective_query_from_inspector(self, objective_query_inspector):
        """Gets an objective query from an inspector.

        :param objective_query_inspector: a query inspector
        :type objective_query_inspector: ``osid.learning.ObjectiveQueryInspector``
        :return: the objective query
        :rtype: ``osid.learning.ObjectiveQuery``
        :raise: ``NullArgument`` -- ``objective_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``objective_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveQuery


class ObjectiveRequisiteSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_lookup_objective_prerequisites(self):
        """Tests if this user can perform ``Objective`` lookups.

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
    def use_comparative_objective_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_view(self):
        """A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_requisite_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are the immediate requisites for the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned requisite ``Objectives``
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_all_requisite_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are the requisites for the given ``Objective`` including the requistes of the requisites, and so on.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_dependent_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that require the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def is_objective_required(self, objective_id, required_objective_id):
        """Tests if an objective is required before proceeding with an objective.

        One objective may indirectly depend on another objective by way
        of one or more other objectives.

        :param objective_id: ``Id`` of the dependent ``Objective``
        :type objective_id: ``osid.id.Id``
        :param required_objective_id: ``Id`` of the required ``Objective``
        :type required_objective_id: ``osid.id.Id``
        :return: ``true`` if ``objective_id`` depends on ``required_objective_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_equivalent_objectives(self, objective_id):
        """Gets a list of ``Objectives`` that are equivalent to the given ``Objective`` for the purpose of requisites.

        An equivalent objective can satisfy the given objective. In
        plenary mode, the returned list contains all of the equivalent
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Objective`` list
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList


class ObjectiveRequisiteAssignmentSession:
    """This session provides methods to manage requisites.

    Each ``ObjectiveBank`` may have its own authorizations governing who
    is allowed to operate on it.

    Moving or adding a reference of an ``Objective`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_assign_requisites(self):
        """Tests if this user can manage objective requisites.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def assign_objective_requisite(self, objective_id, requisite_objective_id):
        """Creates a requirement dependency between two ``Objectives``.

        :param objective_id: the ``Id`` of the dependent ``Objective``
        :type objective_id: ``osid.id.Id``
        :param requisite_objective_id: the ``Id`` of the required ``Objective``
        :type requisite_objective_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``requisite_objective_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``requisite_objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``requisite_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_objective_requisite(self, objective_id, requisite_objective_id):
        """Removes an ``Objective`` requisite from an ``Objective``.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param requisite_objective_id: the ``Id`` of the required ``Objective``
        :type requisite_objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``requisite_objective_id`` not found or ``objective_id`` not mapped to ``requisite_objective_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``requisite_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def assign_equivalent_objective(self, objective_id, equivalent_objective_id):
        """Makes an objective equivalent to another objective for the purposes of satisfying a requisite.

        :param objective_id: the ``Id`` of the principal ``Objective``
        :type objective_id: ``osid.id.Id``
        :param equivalent_objective_id: the ``Id`` of the equivalent ``Objective``
        :type equivalent_objective_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_id`` already mapped to ``equiavelnt_objective_id``
        :raise: ``NotFound`` -- ``objective_id`` or ``equivalent_objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``equivalent_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_equivalent_objective(self, objective_id, equivalent_objective_id):
        """Removes an ``Objective`` requisite from an ``Objective``.

        :param objective_id: the ``Id`` of the principal ``Objective``
        :type objective_id: ``osid.id.Id``
        :param equivalent_objective_id: the ``Id`` of the equivalent ``Objective``
        :type equivalent_objective_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_id`` or ``equivalent_objective_id`` not found or ``objective_id`` is already equivalent to ``equivalent_objective_id``
        :raise: ``NullArgument`` -- ``objective_id`` or ``equivalent_objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ActivityLookupSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_lookup_activities(self):
        """Tests if this user can perform ``Activity`` lookups.

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
    def use_comparative_activity_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_activity_view(self):
        """A complete view of the ``Activity`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_activity(self, activity_id):
        """Gets the ``Activity`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Activity`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Activity`` and retained for
        compatibility.

        :param activity_id: ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: the activity
        :rtype: ``osid.learning.Activity``
        :raise: ``NotFound`` -- ``activity_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.Activity

    @abc.abstractmethod
    def get_activities_by_ids(self, activity_ids):
        """Gets an ``ActivityList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        activities specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Activities`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param activity_ids: the list of ``Ids`` to retrieve
        :type activity_ids: ``osid.id.IdList``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``activity_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_by_genus_type(self, activity_genus_type):
        """Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` which does not include activities of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :param activity_genus_type: an activity genus type
        :type activity_genus_type: ``osid.type.Type``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_by_parent_genus_type(self, activity_genus_type):
        """Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` and include any additional activity with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :param activity_genus_type: an activity genus type
        :type activity_genus_type: ``osid.type.Type``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_by_record_type(self, activity_record_type):
        """Gets a ``ActivityList`` containing the given activity record ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :param activity_record_type: an activity record type
        :type activity_record_type: ``osid.type.Type``
        :return: the returned ``Activity`` list
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_for_objective(self, objective_id):
        """Gets the activities for the given objective.

        In plenary mode, the returned list contains all of the
        activities mapped to the objective ``Id`` or an error results if
        an Id in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param objective_id: ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :return: list of enrollments
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_for_objectives(self, objective_ids):
        """Gets the activities for the given objectives.

        In plenary mode, the returned list contains all of the
        activities specified in the objective ``Id`` list, in the order
        of the list, including duplicates, or an error results if a
        course offering ``Id`` in the supplied list is not found or
        inaccessible. Otherwise, inaccessible ``Activities`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param objective_ids: list of objective ``Ids``
        :type objective_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- an ``objective_id`` not found
        :raise: ``NullArgument`` -- ``objective_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_by_asset(self, asset_id):
        """Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param asset_id: ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities_by_assets(self, asset_ids):
        """Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param asset_ids: ``Ids`` of ``Assets``
        :type asset_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- an ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activities(self):
        """Gets all ``Activities``.

        In plenary mode, the returned list contains all known activites
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :return: a ``ActivityList``
        :rtype: ``osid.learning.ActivityList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    activities = property(fget=get_activities)


class ActivityQuerySession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_search_activities(self):
        """Tests if this user can perform ``Activity`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_activity_query(self):
        """Gets an activity query.

        :return: the activity query
        :rtype: ``osid.learning.ActivityQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQuery

    activity_query = property(fget=get_activity_query)

    @abc.abstractmethod
    def get_activities_by_query(self, activity_query):
        """Gets a list of ``Activities`` matching the given activity query.

        :param activity_query: the activity query
        :type activity_query: ``osid.learning.ActivityQuery``
        :return: the returned ``ActivityList``
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``activity_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``activity_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList


class ActivitySearchSession:
    """This session provides methods for searching ``Activity`` objects.

    The search query is constructed using the ``ActivityQuery``. The
    activity record ``Type`` also specifies the record for the activity
    query.

    ``get_activities_by_query()`` is the basic search method and returns
    a list of ``Activities``. A more advanced search may be performed
    with ``getActivitiesBySearch()``. It accepts a ``ActivitySearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_activities_by_search()`` returns an ``ActivitySearchResults``
    that can be used to access the resulting ``ActivityList`` or be used
    to perform a search within the result set through
    ``ActivitySearch``.

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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_activity_search(self):
        """Gets an activity search.

        :return: the activity search
        :rtype: ``osid.learning.ActivitySearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivitySearch

    activity_search = property(fget=get_activity_search)

    @abc.abstractmethod
    def get_activity_search_order(self):
        """Gets an activity search order.

        The ``ActivitySearchOrder`` is supplied to a ``ActivitySearch``
        to specify the ordering of results.

        :return: the activity search order
        :rtype: ``osid.learning.ActivitySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivitySearchOrder

    activity_search_order = property(fget=get_activity_search_order)

    @abc.abstractmethod
    def get_activities_by_search(self, activity_query, activitiesearch):
        """Gets the search results matching the given search query using the given search.

        :param activity_query: the activity query
        :type activity_query: ``osid.learning.ActivityQuery``
        :param activitiesearch: the activity search
        :type activitiesearch: ``osid.learning.ActivitySearch``
        :return: the returned search results
        :rtype: ``osid.learning.ActivitySearchResults``
        :raise: ``NullArgument`` -- ``activity_query`` or ``activitiesearch`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``activitiesearch`` or ``activity_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivitySearchResults

    @abc.abstractmethod
    def get_activity_query_from_inspector(self, activity_query_inspector):
        """Gets an activity query from an inspector.

        The inspector is available from an ``ActivitySearchResults``.

        :param activity_query_inspector: an activity bank query inspector
        :type activity_query_inspector: ``osid.learning.ActivityQueryInspector``
        :return: the activity query
        :rtype: ``osid.learning.ActivityQuery``
        :raise: ``NullArgument`` -- ``activity_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``activity_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQuery


class ActivityAdminSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_create_activities(self):
        """Tests if this user can create ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Activity`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_activity_with_record_types(self, activity_record_types):
        """Tests if this user can create a single ``Activity`` using the desired record types.

        While ``LearningManager.getActivityRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Activity``.
        Providing an empty array tests if an ``Activity`` can be created
        with no records.

        :param activity_record_types: array of activity record types
        :type activity_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Activity`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``activity_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_activity_form_for_create(self, objective_id, activity_record_types):
        """Gets the activity form for creating new activities.

        A new form should be requested for each create transaction.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param activity_record_types: array of activity record types
        :type activity_record_types: ``osid.type.Type[]``
        :return: the activity form
        :rtype: ``osid.learning.ActivityForm``
        :raise: ``NotFound`` -- ``objective_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id`` or ``activity_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityForm

    @abc.abstractmethod
    def create_activity(self, activity_form):
        """Creates a new ``Activity``.

        :param activity_form: the form for this ``Activity``
        :type activity_form: ``osid.learning.ActivityForm``
        :return: the new ``Activity``
        :rtype: ``osid.learning.Activity``
        :raise: ``IllegalState`` -- ``activity_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``activity_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``activity_form`` did not originate from ``get_activity_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Activity

    @abc.abstractmethod
    def can_update_activities(self):
        """Tests if this user can update ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if activity modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_activity_form_for_update(self, activity_id):
        """Gets the activity form for updating an existing activity.

        A new activity form should be requested for each update
        transaction.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: the activity form
        :rtype: ``osid.learning.ActivityForm``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityForm

    @abc.abstractmethod
    def update_activity(self, activity_form):
        """Updates an existing activity,.

        :param activity_form: the form containing the elements to be updated
        :type activity_form: ``osid.learning.ActivityForm``
        :raise: ``IllegalState`` -- ``activity_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``activity_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``activity_form`` did not originate from ``get_activity_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_activities(self):
        """Tests if this user can delete ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Activity`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_activity(self, activity_id):
        """Deletes the ``Activity`` identified by the given ``Id``.

        :param activity_id: the ``Id`` of the ``Activity`` to delete
        :type activity_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Activity`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_activity_aliases(self):
        """Tests if this user can manage ``Id`` aliases for activities.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Activity`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_activity(self, activity_id, alias_id):
        """Adds an ``Id`` to an ``Activity`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Activity`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another activity, it is
        reassigned to the given activity ``Id``.

        :param activity_id: the ``Id`` of an ``Activity``
        :type activity_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``activity_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ActivityNotificationSession:
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Activity`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``ActivityLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_register_for_activity_notifications(self):
        """Tests if this user can register for ``Activity`` notifications.

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
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for activities in
        objective banks which are children of this objective bank in the
        objective bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this objective bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_activity_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_activity_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_activity_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_activity_notification(self, notification_id):
        """Acknowledge an activity notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_activities(self):
        """Register for notifications of new activities.

        ``ActivityReceiver.newActivities()`` is invoked when a new
        activity is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_activities_for_objective(self, objective_id):
        """Register for notifications of new activities for the given objective.

        ``ActivityReceiver.newActivities()`` is invoked when a new
        activity is created.

        :param objective_id: the ``Id`` of the ``Activity`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_activities(self):
        """Registers for notification of updated activities.

        ``ActivityReceiver.changedActivities()`` is invoked when an
        activity is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_activities_for_objective(self, objective_id):
        """Registers for notification of updated activities.

        ``ActivityReceiver.changedActivities()`` is invoked when an
        activity is changed.

        :param objective_id: the ``Id`` of the ``Objective`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_activity(self, activity_id):
        """Registers for notification of an updated activity.

        ``ActivityReceiver.changedActivities()`` is invoked when the
        specified activity is changed.

        :param activity_id: the ``Id`` of the ``Activity`` to monitor
        :type activity_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``activity_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_activities(self):
        """Registers for notification of deleted activities.

        ``ActivityReceiver.deletedActivities()`` is invoked when an
        activity is removed from this objective bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_activities_for_objective(self, objective_id):
        """Registers for notification of deleted activities.

        ``ActivityReceiver.deletedActivities()`` is invoked when an
        activity is removed from this objective bank.

        :param objective_id: the ``Id`` of the ``Objective`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_activity(self, activity_id):
        """Registers for notification of a deleted activity.

        ``ActivityReceiver.changedActivities()`` is invoked when the
        specified activity is removed from this objective bank.

        :param activity_id: the ``Id`` of the ``Activity`` to monitor
        :type activity_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``activity_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_activity_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_activity_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_activity_notification(self, notification_id):
        """Acknowledge an activity notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ActivityObjectiveBankSession:
    """This session provides methods to retrieve ``Activity`` to ``ObjectiveBank`` mappings.

    An ``Activity`` may appear in multiple ``ObjectiveBanks``. Each
    ``ObjectiveBank`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_activity_objective_bank_mappings(self):
        """Tests if this user can perform lookups of activity/objective bank mappings.

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
    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_activity_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_activities_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_activity_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activity ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_activities_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objective bank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of activities
        :rtype: ``osid.learning.ActivityList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityList

    @abc.abstractmethod
    def get_objective_bank_ids_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_objective_banks_by_activity(self, activity_id):
        """Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        :param activity_id: ``Id`` of a ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of objective bank ``Ids``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``activity_id`` is not found
        :raise: ``NullArgument`` -- ``activity_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList


class ActivityObjectiveBankAssignmentSession:
    """This session provides methods to re-assign ``Activities`` to ``ObjectiveBanks``.

    An ``Activity`` may map to multiple ``ObjectiveBanks`` and removing
    the last reference to a ``Activity`` is the equivalent of deleting
    it. Each ``ObjectiveBank`` may have its own authorizations governing
    who is allowed to operate on it.

    Moving or adding a reference of an ``Activity`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_activities(self):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_activities_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank node in which any activity can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_objective_bank_ids_for_activity(self, objective_bank_id, activity_id):
        """Gets a list of objective banks including and under the given objective bank node in which a specific activity can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :return: list of assignable objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_activity_to_objective_bank(self, activity_id, objective_bank_id):
        """Adds an existing ``Activity`` to a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``activity_id`` already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_activity_from_objective_bank(self, activity_id, objective_bank_id):
        """Removes a ``Activity`` from a ``ObjectiveBank``.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id`` or ``objective_bank_id`` not found or ``activity_id`` not mapped to ``objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_activity_to_objective_bank(self, activity_id, from_objective_bank_id, to_objective_bank_id):
        """Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param activity_id: the ``Id`` of the ``Activity``
        :type activity_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or ``activity_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``activity_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ActivitySmartObjectiveBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    An ``ActivityQuery`` can be retrieved from this session and mapped
    to this ``ObjectiveBank`` to create a virtual collection of
    activities. The activities may be sequenced using the
    ``ActivitySearchOrder`` from this session.

    This ``ObjectiveBank`` has a default query that matches any activity
    and a default search order that specifies no sequencing. The queries
    may be examined using an ``ActivityQueryInspector``. The query may
    be modified by converting the inspector back to an
    ``ActivityQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the ``ObjectiveBank`` associated with this session
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_manage_smart_objective_banks(self):
        """Tests if this user can manage smart objective banks.

        A return of true does not guarantee successful assessment. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart objective bank management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_activity_query(self):
        """Gets an activity query.

        :return: the activity query
        :rtype: ``osid.learning.ActivityQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQuery

    activity_query = property(fget=get_activity_query)

    @abc.abstractmethod
    def get_activity_search_order(self):
        """Gets an activity search order.

        :return: the activity search order
        :rtype: ``osid.learning.ActivitySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivitySearchOrder

    activity_search_order = property(fget=get_activity_search_order)

    @abc.abstractmethod
    def apply_activity_query(self, activity_query):
        """Applies an activity query to this bank.

        :param activity_query: the activity query
        :type activity_query: ``osid.learning.ActivityQuery``
        :raise: ``NullArgument`` -- ``activity_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``activity_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_activity_query(self):
        """Gets an activity query inspector for this objective bank.

        :return: the activity query inspector
        :rtype: ``osid.learning.ActivityQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQueryInspector

    @abc.abstractmethod
    def apply_activity_sequencing(self, activity_search_order):
        """Applies an activity search order to this objective bank.

        :param activity_search_order: the activity search order
        :type activity_search_order: ``osid.learning.ActivitySearchOrder``
        :raise: ``NullArgument`` -- ``activity_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``activity_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_activity_query_from_inspector(self, activity_query_inspector):
        """Gets an activity query from an inspector.

        :param activity_query_inspector: an activity query inspector
        :type activity_query_inspector: ``osid.learning.ActivityQueryInspector``
        :return: the activity query
        :rtype: ``osid.learning.ActivityQuery``
        :raise: ``NullArgument`` -- ``activity_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``activity_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ActivityQuery


class ProficiencyLookupSession:
    """This session defines methods for retrieving proficiencies."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_lookup_proficiencies(self):
        """Tests if this user can perform ``Proficiency`` lookups.

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
    def use_comparative_proficiency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_proficiency_view(self):
        """A complete view of the ``Proficiency`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this objective bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_effective_proficiency_view(self):
        """Only proficiencies whose effective dates are current are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_effective_proficiency_view(self):
        """All proficienies of any effective dates are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_proficiency(self, proficiency_id):
        """Gets the ``Proficiency`` specified by its ``Id``.

        :param proficiency_id: the ``Id`` of the ``Proficiency`` to retrieve
        :type proficiency_id: ``osid.id.Id``
        :return: the returned ``Proficiency``
        :rtype: ``osid.learning.Proficiency``
        :raise: ``NotFound`` -- no ``Proficiency`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Proficiency

    @abc.abstractmethod
    def get_proficiencies_by_ids(self, proficiency_ids):
        """Gets a ``ProficiencyList`` corresponding to the given ``IdList``.

        :param proficiency_ids: the list of ``Ids`` to retrieve
        :type proficiency_ids: ``osid.id.IdList``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``proficiency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type(self, proficiency_genus_type):
        """Gets a ``ProficiencyList`` corresponding to the given proficiency genus ``Type`` which does not include proficiencies of types derived from the specified ``Type``.

        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_parent_genus_type(self, proficiency_genus_type):
        """Gets a ``ProficiencyList`` corresponding to the given proficiency genus ``Type`` and include any additional proficiencies with genus types derived from the specified ``Type``.

        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_record_type(self, proficiency_record_type):
        """Gets a ``ProficiencyList`` containing the given proficiency record ``Type``.

        :param proficiency_record_type: a proficiency record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_on_date(self, from_, to):
        """Gets a ``ProficiencyList`` effecyive during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_on_date(self, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given proficiency genus type effective during the entire given date range inclusive but not confined to the date range.

        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``proficiency_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_objective(self, objective_id):
        """Gets a ``ProficiencyList`` relating to the given objective.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_objective_on_date(self, objective_id, from_, to):
        """Gets a ``ProficiencyList`` relating to the given objective effective during the entire given date range inclusive but not confined to the date range.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``objective_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_for_objective(self, objective_id, proficiency_genus_type):
        """Gets a ``ProficiencyList`` relating to the given objective and proficiency genus ``Type``.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``objective_id`` or ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_for_objective_on_date(self, objective_id, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given proficiency genus type relating to the given objective effective during the entire given date range inclusive but not confined to the date range.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``objective_id, proficiency_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_objectives(self, objective_ids):
        """Gets a ``ProficiencyList`` relating to the given objectives.

        :param objective_ids: the objective ``Ids``
        :type objective_ids: ``osid.id.IdList``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``objective_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_resource(self, resource_id):
        """Gets a ``ProficiencyList`` relating to the given resource.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``ProficiencyList`` relating to the given resource effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_for_resource(self, resource_id, proficiency_genus_type):
        """Gets a ``ProficiencyList`` relating to the given resource and proficiency genus ``Type``.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_for_resource_on_date(self, resource_id, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given proficiency genus type relating to the given resource effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, proficiency_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_resources(self, resource_ids):
        """Gets a ``ProficiencyList`` relating to the given resources.

        :param resource_ids: the resource ``Ids``
        :type resource_ids: ``osid.id.IdList``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_objective_and_resource(self, objective_id, resource_id):
        """Gets a ``ProficiencyList`` relating to the given objective and resource ````.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``objective_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_for_objective_and_resource_on_date(self, objective_id, resource_id, from_, to):
        """Gets a ``ProficiencyList`` relating to the given resource and objective effective during the entire given date range inclusive but not confined to the date range.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``objective_id, resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_for_objective_and_resource(self, objective_id, resource_id, proficiency_genus_type):
        """Gets a ``ProficiencyList`` of the given genus type relating to the given objective and resource ````.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``objective_id, resource_id`` or ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self, objective_id, resource_id, proficiency_genus_type, from_, to):
        """Gets a ``ProficiencyList`` of the given genus type relating to the given resource and objective effective during the entire given date range inclusive but not confined to the date range.

        :param objective_id: an objective ``Id``
        :type objective_id: ``osid.id.Id``
        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param proficiency_genus_type: a proficiency genus type
        :type proficiency_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Proficiency`` list
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``objective_id, resource_id, proficiency_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiencies(self):
        """Gets all ``Proficiencies``.

        :return: a list of ``Proficiencies``
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    proficiencies = property(fget=get_proficiencies)


class ProficiencyQuerySession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_search_proficiencies(self):
        """Tests if this user can perform ``Proficiency`` lookups.

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
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_proficiency_query(self):
        """Gets a proficiency query.

        :return: the proficiency query
        :rtype: ``osid.learning.ProficiencyQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyQuery

    proficiency_query = property(fget=get_proficiency_query)

    @abc.abstractmethod
    def get_proficiencies_by_query(self, proficiency_query):
        """Gets a list of ``Proficiencies`` matching the given proficiency query.

        :param proficiency_query: the proficiency query
        :type proficiency_query: ``osid.learning.ProficiencyQuery``
        :return: the returned ``ProficiencyList``
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``proficiency_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``proficiency_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList


class ProficiencySearchSession:
    """This session provides methods for searching among ``Proficiency`` objects.

    The search query is constructed using the ``ProficiencyQuery``.

    ``get_proficiencies_by_query()`` is the basic search method and
    returns a list of ``Proficiencies``. A more advanced search may be
    performed with ``getProficienciesBySearch()``. It accepts a
    ``ProficiencySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_proficiencies_by_search()`` returns a
    ``ProficiencySearchResults`` that can be used to access the
    resulting ``ProficiencyList`` or be used to perform a search within
    the result set through ``ProficiencySearch``.

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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_proficiency_search(self):
        """Gets a proficiency search.

        :return: the proficiency search
        :rtype: ``osid.learning.ProficiencySearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencySearch

    proficiency_search = property(fget=get_proficiency_search)

    @abc.abstractmethod
    def get_proficiency_search_order(self):
        """Gets a proficiency search order.

        The ``ProficiencySearchOrder`` is supplied to a
        ``ProficiencySearch`` to specify the ordering of results.

        :return: the proficiency search order
        :rtype: ``osid.learning.ProficiencySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencySearchOrder

    proficiency_search_order = property(fget=get_proficiency_search_order)

    @abc.abstractmethod
    def get_proficiencies_by_search(self, proficiency_query, proficiency_search):
        """Gets the search results matching the given search query using the given search.

        :param proficiency_query: the proficiency query
        :type proficiency_query: ``osid.learning.ProficiencyQuery``
        :param proficiency_search: the proficiency search
        :type proficiency_search: ``osid.learning.ProficiencySearch``
        :return: the returned search results
        :rtype: ``osid.learning.ProficiencySearchResults``
        :raise: ``NullArgument`` -- ``proficiency_query`` or ``proficiency_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``proficiency_query`` or ``proficiency_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencySearchResults

    @abc.abstractmethod
    def get_proficiency_query_from_inspector(self, proficiency_query_inspector):
        """Gets a proficiency query from an inspector.

        The inspector is available from a ``ProficiencySearchResults``.

        :param proficiency_query_inspector: a proficiency query inspector
        :type proficiency_query_inspector: ``osid.learning.ProficiencyQueryInspector``
        :return: the proficiency query
        :rtype: ``osid.learning.ProficiencyQuery``
        :raise: ``NullArgument`` -- ``proficiency_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``proficiency_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyQuery


class ProficiencyAdminSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_create_proficiencies(self):
        """Tests if this user can create ``Proficiencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Proficiency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Proficiency`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_proficiency_with_record_types(self, proficiency_record_types):
        """Tests if this user can create a single ``Proficiency`` using the desired record types.

        While ``LearningManager.getProficiencyRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Proficiency``. Providing an empty array tests if a
        ``Proficiency`` can be created with no records.

        :param proficiency_record_types: array of proficiency record types
        :type proficiency_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Proficiency`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proficiency_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_proficiency_form_for_create(self, objective_id, resource_id, proficiency_record_types):
        """Gets the proficiency form for creating new proficiencies.

        A new form should be requested for each create transaction.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param proficiency_record_types: array of proficiency record types
        :type proficiency_record_types: ``osid.type.Type[]``
        :return: the proficiency form
        :rtype: ``osid.learning.ProficiencyForm``
        :raise: ``NotFound`` -- ``objective_id`` or ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``objective_id, resource_id,`` or ``proficieny_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyForm

    @abc.abstractmethod
    def create_proficiency(self, proficiency_form):
        """Creates a new ``Proficiency``.

        A new form should be requested for each create transaction.

        :param proficiency_form: the form for this ``Proficiency``
        :type proficiency_form: ``osid.learning.ProficiencyForm``
        :return: the new ``Proficiency``
        :rtype: ``osid.learning.Proficiency``
        :raise: ``IllegalState`` -- ``proficiency_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``proficiency_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``proficiency_form`` did not originate from ``get_proficiency_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.Proficiency

    @abc.abstractmethod
    def can_update_proficiencies(self):
        """Tests if this user can update ``Proficiencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Proficiency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Proficiency`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_proficiency_form_for_update(self, proficiency_id):
        """Gets the proficiency form for updating an existing proficiency.

        :param proficiency_id: the ``Id`` of the ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :return: the proficiency form
        :rtype: ``osid.learning.ProficiencyForm``
        :raise: ``NotFound`` -- ``proficiency_id`` is not found
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyForm

    @abc.abstractmethod
    def update_proficiency(self, proficiency_form):
        """Updates an existing proficiency.

        :param proficiency_form: the form containing the elements to be updated
        :type proficiency_form: ``osid.learning.ProficiencyForm``
        :raise: ``IllegalState`` -- ``proficiency_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``proficiency_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``proficiency_form`` did not originate from ``get_proficiency_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_proficiencies(self):
        """Tests if this user can delete ``Proficiencies``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Proficiency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Proficiency`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_proficiency(self, proficiency_id):
        """Deletes a ``Proficiency``.

        :param proficiency_id: the ``Id`` of the ``Proficiency`` to remove
        :type proficiency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``proficiency_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def delete_proficiencies(self):
        """Deletes all proficiencies in this ``ObjectiveBank``.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_proficiency_aliases(self):
        """Tests if this user can manage ``Id`` aliases for proficiency entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Proficiency`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_proficiency(self, proficiency_id, alias_id):
        """Adds an ``Id`` to a ``Proficiency`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Proficiency`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another proficiency, it is
        reassigned to the given proficiency ``Id``.

        :param proficiency_id: the ``Id`` of a ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``proficiency_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ProficiencyNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Proficiency`` objects in this ``ObjectiveBank``.

    This also includes existing proficiencies that may appear or
    disappear due to changes in the ``ObjectiveBank`` hierarchy, This
    session is intended for consumers needing to synchronize their state
    with this service without the use of polling. Notifications are
    cancelled when this session is closed.

    The two views defined in this session correspond to the views in the
    ``ProficiencyLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_register_for_proficiency_notifications(self):
        """Tests if this user can register for ``Proficiency`` notifications.

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
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this objective bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_proficiency_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_proficiency_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_proficiency_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_proficiency_notification(self, notification_id):
        """Acknowledge a proficiency notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_proficiencies(self):
        """Register for notifications of new proficiencies.

        ``ProficiencyReceiver.newProficiencies()`` is invoked when a new
        ``Proficiency`` appears in this objective bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_proficiencies_by_genus_type(self, proficiency_genus_type):
        """Register for notifications of new proficiencies with the given genus type.

        ``ProficiencyReceiver.newProficiencies()`` is invoked when a new
        ``Proficiency`` appears for the given resource in this objective
        bank.

        :param proficiency_genus_type: the genus type of a proficiency to monitor
        :type proficiency_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_proficiencies_for_objective(self, objective_id):
        """Register for notifications of new proficiencies.

        ``ProficiencyReceiver.newProficiencies()`` is invoked when a new
        ``Proficiency`` appears for the given objective in this
        objective bank.

        :param objective_id: the ``Id`` of a resource to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_proficiencies_for_resource(self, resource_id):
        """Register for notifications of new proficiencies.

        ``ProficiencyReceiver.newProficiencies()`` is invoked when a new
        ``Proficiency`` appears for the given resource in this objective
        bank.

        :param resource_id: the ``Id`` of a resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_proficiencies(self):
        """Registers for notification of updated proficiencies.

        ``ProficiencyReceiver.changedProficiencies()`` is invoked when a
        proficiency in this objective bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_proficiencies_by_genus_type(self, proficiency_genus_type):
        """Registers for notification of updated proficiencies of the given genus type.

        ``ProficiencyReceiver.changedProficiencies()`` is invoked when a
        proficiency in this objective bank is changed.

        :param proficiency_genus_type: the genus type of the ``Proficiency`` to monitor
        :type proficiency_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``proficiency_genus_t_ype`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_proficiencies_for_objective(self, objective_id):
        """Registers for notification of an updated proficiency.

        ``ProficiencyReceiver.changedProficiencies()`` is invoked when
        the specified proficiency related to the given objective is
        changed in this objective bank.

        :param objective_id: the ``Id`` of the ``Objective`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_proficiencies_for_resource(self, resource_id):
        """Registers for notification of an updated proficiency.

        ``ProficiencyReceiver.changedProficiencies()`` is invoked when
        the specified proficiency related to the given resource is
        changed in this objective bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_proficiency(self, proficiency_id):
        """Registers for notification of an updated proficiency.

        ``ProficiencyReceiver.changedProficiencies()`` is invoked when
        the specified proficiency in this objective bank is changed.

        :param proficiency_id: the ``Id`` of the ``Proficiency`` to monitor
        :type proficiency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_proficiencies(self):
        """Registers for notification of deleted proficiencies.

        ``ProficiencyReceiver.deletedProficiencies()`` is invoked when a
        proficiency is deleted or removed from this objective bank.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_proficiencies_by_genus_type(self, proficiency_genus_type):
        """Registers for notification of deleted proficiencies of the given genus type.

        ``ProficiencyReceiver.deletedProficiencies()`` is invoked when a
        proficiency is deleted or removed from this objective bank.

        :param proficiency_genus_type: the genus type of the ``Proficiency`` to monitor
        :type proficiency_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``proficiency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_proficiencies_for_objective(self, objective_id):
        """Registers for notification of a deleted proficiency.

        ``ProficiencyReceiver.deletedProficiencies()`` is invoked when
        the specified proficiency related to the objective is deleted or
        removed from this objective bank.

        :param objective_id: the ``Id`` of the ``Objective`` to monitor
        :type objective_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_proficiencies_for_resource(self, resource_id):
        """Registers for notification of a deleted proficiency.

        ``ProficiencyReceiver.deletedProficiencies()`` is invoked when
        the specified proficiency related to the resource is deleted or
        removed from this objective bank.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_proficiency(self, proficiency_id):
        """Registers for notification of a deleted proficiency.

        ``ProficiencyReceiver.deletedProficiencies()`` is invoked when
        the specified proficiency is deleted or removed from this
        objective bank.

        :param proficiency_id: the ``Id`` of the ``Proficiency`` to monitor
        :type proficiency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_proficiency_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_proficiency_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_proficiency_notification(self, notification_id):
        """Acknowledge an proficiency notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ProficiencyObjectiveBankSession:
    """This session provides methods to retrieve ``Proficiency`` to ``ObjectiveBank`` mappings.

    A ``Proficiency`` may appear in multiple ``ObjectiveBank`` objects.
    Each objective bank may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_proficiency_objective_bank_mappings(self):
        """Tests if this user can perform lookups of proficiency/objective bank mappings.

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
    def use_comparative_proficiency_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_proficiency_objective_bank_view(self):
        """A complete view of the ``Proficiency`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_proficiency_ids_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Proficiency Ids`` associated with a ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related proficiency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_proficiencies_by_objective_bank(self, objective_bank_id):
        """Gets the list of ``Proficiencies`` associated with a ``ObjectiveBank``.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of related proficiencies
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_proficiency_ids_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Proficiency Ids`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objectiveBank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of proficiency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_proficiencies_by_objective_banks(self, objective_bank_ids):
        """Gets the list of ``Proficiencies`` corresponding to a list of ``ObjectiveBanks``.

        :param objective_bank_ids: list of objectiveBank ``Ids``
        :type objective_bank_ids: ``osid.id.IdList``
        :return: list of proficiencies
        :rtype: ``osid.learning.ProficiencyList``
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyList

    @abc.abstractmethod
    def get_objective_bank_ids_by_proficiency(self, proficiency_id):
        """Gets the ``ObjectiveBank``  ``Ids`` mapped to a ``Proficiency``.

        :param proficiency_id: ``Id`` of a ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :return: list of objective banks
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``proficiency_id`` is not found
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_objective_banks_by_proficiency(self, proficiency_id):
        """Gets the ``ObjectiveBanks`` mapped to a ``Proficiency``.

        :param proficiency_id: ``Id`` of a ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :return: list of objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``proficiency_id`` is not found
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList


class ProficiencyObjectiveBankAssignmentSession:
    """This session provides methods to re-assign ``Proficiencies`` to ``ObjectiveBank`` objects.

    A ``Proficiency`` may appear in multiple ``ObjectiveBank`` objects
    and removing the last reference to a ``Proficiency`` is the
    equivalent of deleting it. Each ``ObjectiveBank`` may have its own
    authorizations governing who is allowed to operate on it.

    Adding a reference of a ``Proficiency`` to another ``ObjectiveBank``
    is not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_proficiencies(self):
        """Tests if this user can alter proficiency/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_proficiencies_to_objective_bank(self, objective_bank_id):
        """Tests if this user can alter proficiency/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_objective_bank_ids(self, objective_bank_id):
        """Gets a list of objective banks including and under the given objective bank proficiency in which any proficiency can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: list of assignable objectiveBank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_objective_bank_ids_for_proficiency(self, objective_bank_id, proficiency_id):
        """Gets a list of objective banks including and under the given objective bank proficiency in which a specific proficiency can be assigned.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proficiency_id: the ``Id`` of the ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :return: list of assignable objectiveBank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_proficiency_to_objective_bank(self, proficiency_id, objective_bank_id):
        """Adds an existing ``Proficiency`` to a ``ObjectiveBank``.

        :param proficiency_id: the ``Id`` of the ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``proficiency_id`` is already mapped to ``objective_bank_id``
        :raise: ``NotFound`` -- ``proficiency_id`` or ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_proficiency_from_objective_bank(self, proficiency_id, objective_bank_id):
        """Removes a ``Proficiency`` from a ``ObjectiveBank``.

        :param proficiency_id: the ``Id`` of the ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``proficiency_id`` or ``objective_bank_id`` not found or ``proficiency_id`` not mapped to ``objective_bank_id``
        :raise: ``NullArgument`` -- ``proficiency_id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_proficiency_to_objective_bank(self, proficiency_id, from_objective_bank_id, to_objective_bank_id):
        """Moves a ``Proficiency`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :param proficiency_id: the ``Id`` of the ``Proficiency``
        :type proficiency_id: ``osid.id.Id``
        :param from_objective_bank_id: the ``Id`` of the current ``ObjectiveBank``
        :type from_objective_bank_id: ``osid.id.Id``
        :param to_objective_bank_id: the ``Id`` of the destination ``ObjectiveBank``
        :type to_objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``proficiency_id, from_objective_bank_id,`` or ``to_objective_bank_id`` not found or ``proficiency_id`` not mapped to ``from_objective_bank_id``
        :raise: ``NullArgument`` -- ``proficiency_id, from_objective_bank_id,`` or ``to_objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ProficiencySmartObjectiveBankSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``ProficiencyQuery`` can be retrieved from this session and mapped
    to this ``ObjectiveBank`` to create a virtual collection of
    ``Proficiencies``. The proficiencies may be sequenced using the
    ``ProficiencySearchOrder`` from this session.

    This ``ObjectiveBank`` has a default query that matches any
    proficiency and a default search order that specifies no sequencing.
    The queries may be examined using a ``ProficiencyQueryInspector``.
    The query may be modified by converting the inspector back to a
    ``ProficiencyQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``Familt``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_manage_smart_objective_banks(self):
        """Tests if this user can manage smart objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart objective bank methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_proficiency_query(self):
        """Gets a proficiency query.

        :return: the proficiency query
        :rtype: ``osid.learning.ProficiencyQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyQuery

    proficiency_query = property(fget=get_proficiency_query)

    @abc.abstractmethod
    def get_proficiency_search_order(self):
        """Gets a proficiency search order.

        :return: the proficiency search order
        :rtype: ``osid.learning.ProficiencySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencySearchOrder

    proficiency_search_order = property(fget=get_proficiency_search_order)

    @abc.abstractmethod
    def apply_proficiency_query(self, proficiency_query):
        """Applies a proficiency query to this objective bank.

        :param proficiency_query: the proficiency query
        :type proficiency_query: ``osid.learning.ProficiencyQuery``
        :raise: ``NullArgument`` -- ``proficiency_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``proficiency_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_proficiency_query(self):
        """Gets a proficiency query inspector for this objective bank.

        :return: the proficiency query inspector
        :rtype: ``osid.learning.ProficiencyQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyQueryInspector

    @abc.abstractmethod
    def apply_proficiency_sequencing(self, proficiency_search_order):
        """Applies a proficiency search order to this objective bank.

        :param proficiency_search_order: the proficiency search order
        :type proficiency_search_order: ``osid.learning.ProficiencySearchOrder``
        :raise: ``NullArgument`` -- ``proficiency_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``proficiency_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_proficiency_query_from_inspector(self, proficiency_query_inspector):
        """Gets a proficiency query from an inspector.

        :param proficiency_query_inspector: a proficiency query inspector
        :type proficiency_query_inspector: ``osid.learning.ProficiencyQueryInspector``
        :return: the proficiency query
        :rtype: ``osid.learning.ProficiencyQuery``
        :raise: ``NullArgument`` -- ``relatinship_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``proficiency_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ProficiencyQuery


class MyLearningPathSession:
    """This session defines methods for finding learning paths through an objective hierarchy based on proficiencies."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_lookup_learning_paths(self):
        """Tests if this user can perform learning path lookups.

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
    def use_comparative_proficiency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_proficiency_view(self):
        """A complete view of the ``Proficiency`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this objective bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def find_path(self, objective_id):
        """Gets the shortest path to an objective.

        The path is a list of objectives for which there is a deficient
        proficiency.

        :param objective_id: the ``Id`` of the ``Objective`` to reach
        :type objective_id: ``osid.id.Id``
        :return: the returned list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def find_path_at_proficiency(self, objective_id, grade_id):
        """Gets the shortest path to an objective.

        The path is a list of objectives for which there is a
        proficiency less than the given proficiency.

        :param objective_id: the ``Id`` of the ``Objective`` to reach
        :type objective_id: ``osid.id.Id``
        :param grade_id: the ``Id`` of a proficiency level
        :type grade_id: ``osid.id.Id``
        :return: the returned list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` or ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objectives_by_completion(self, objective_id, completion):
        """Gets the list of objectives for there is a minimum completion.

        :param objective_id: the ``Id`` of the ``Objective`` to reach
        :type objective_id: ``osid.id.Id``
        :param completion: the minimum completion as a percentage number
        :type completion: ``cardinal``
        :return: the returned list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList


class LearningPathSession:
    """This session defines methods for finding learning paths through an objective hierarchy based on proficiencies."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_id(self):
        """Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: the ``ObjectiveBank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_id = property(fget=get_objective_bank_id)

    @abc.abstractmethod
    def get_objective_bank(self):
        """Gets the ``ObjectiveBank`` associated with this session.

        :return: the obective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    objective_bank = property(fget=get_objective_bank)

    @abc.abstractmethod
    def can_lookup_learning_paths(self):
        """Tests if this user can perform learning path lookups.

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
    def use_comparative_proficiency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_proficiency_view(self):
        """A complete view of the ``Proficiency`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_objective_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include proficiencies in objective banks
        which are children of this objective bank in the obective bank
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_objective_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this objective bank
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def find_path_for_resource(self, objective_id, resource_id):
        """Gets the shortest path to an objective.

        The path is a list of objectives for which the resource has a
        deficient proficiency.

        :param objective_id: the ``Id`` of the ``Objective`` to reach
        :type objective_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: the returned list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` or ``resource_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def find_path_for_resource_at_proficiency(self, objective_id, resource_id, grade_id):
        """Gets the shortest path to an objective.

        The path is a list of objectives for which the resource has a
        proficiency less than the given proficiency.

        :param objective_id: the ``Id`` of the ``Objective`` to reach
        :type objective_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param grade_id: the ``Id`` of a proficiency level
        :type grade_id: ``osid.id.Id``
        :return: the returned list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` or ``resource_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id, resource_id`` or ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList

    @abc.abstractmethod
    def get_objectives_for_resource_by_completion(self, objective_id, resource_id, completion):
        """Gets the list of objectives for a resource that have a minimum completion.

        :param objective_id: the ``Id`` of the ``Objective`` to reach
        :type objective_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param completion: the minimum completion as a percentage number
        :type completion: ``cardinal``
        :return: the returned list of objectives
        :rtype: ``osid.learning.ObjectiveList``
        :raise: ``NotFound`` -- ``objective_id`` or ``resource_id`` not found
        :raise: ``NullArgument`` -- ``proficiency_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveList


class ObjectiveBankLookupSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_objective_banks(self):
        """Tests if this user can perform ``ObjectiveBank`` lookups.

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
    def use_comparative_objective_bank_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_bank_view(self):
        """A complete view of the ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_objective_bank(self, objective_bank_id):
        """Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        :param objective_bank_id: ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    @abc.abstractmethod
    def get_objective_banks_by_ids(self, objective_bank_ids):
        """Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :param objective_bank_ids: the list of ``Ids`` to retrieve
        :type objective_bank_ids: ``osid.id.IdList``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``objective_bank_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def get_objective_banks_by_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which does not include objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def get_objective_banks_by_parent_genus_type(self, objective_bank_genus_type):
        """Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and include any additional objective banks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_genus_type: an objective bank genus type
        :type objective_bank_genus_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def get_objective_banks_by_record_type(self, objective_bank_record_type):
        """Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param objective_bank_record_type: an objective bank record type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def get_objective_banks_by_provider(self, resource_id):
        """Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``ObjectiveBank`` list
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def get_objective_banks(self):
        """Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :return: a ``ObjectiveBankList``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    objective_banks = property(fget=get_objective_banks)


class ObjectiveBankQuerySession:
    """This session provides methods for searching among ``ObjectiveBank`` objects.

    The search query is constructed using the ``ObjectiveBankQuery``.

    ``ObjectiveBanks`` may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``ObjectiveBankQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_objective_banks(self):
        """Tests if this user can perform ``ObjectiveBank`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_query(self):
        """Gets an objective bank query.

        :return: an objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQuery

    objective_bank_query = property(fget=get_objective_bank_query)

    @abc.abstractmethod
    def get_objective_banks_by_query(self, objective_bank_query):
        """Gets a list of ``ObjectiveBank`` objects matching the given objectiove bank query.

        :param objective_bank_query: the objective bank query
        :type objective_bank_query: ``osid.learning.ObjectiveBankQuery``
        :return: the returned ``ObjectiveBankList``
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NullArgument`` -- ``objective_bank_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList


class ObjectiveBankSearchSession:
    """This session provides methods for searching among ``ObjectiveBank`` objects.

    The search query is constructed using the ``ObjectiveBankQuery``.

    ``get_objective_banks_by_query()`` is the basic search method and
    returns a list of ``ObjectiveBank`` objects.A more advanced search
    may be performed with ``getObjectiveBanksBySearch()``. It accepts a
    ``ObjectiveBankSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_objective_banks_by_search()`` returns a
    ``ObjectiveBankSearchResults`` that can be used to access the
    resulting ``ObjectiveBankList`` or be used to perform a search
    within the result set through ``ObjectiveBankSearch``.

    ``ObjectiveBanks`` may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``ObjectiveBankQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_search(self):
        """Gets an objective bank search.

        :return: an objective bank search
        :rtype: ``osid.learning.ObjectiveBankSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankSearch

    objective_bank_search = property(fget=get_objective_bank_search)

    @abc.abstractmethod
    def get_objective_bank_search_order(self):
        """Gets an objective bank search order.

        The ``ObjectiveBankSearchOrder`` is supplied to a
        ``ObjectiveBankSearch`` to specify the ordering of results.

        :return: the objective bank search order
        :rtype: ``osid.learning.ObjectiveBankSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankSearchOrder

    objective_bank_search_order = property(fget=get_objective_bank_search_order)

    @abc.abstractmethod
    def get_objective_banks_by_search(self, objective_bank_query, objective_bank_search):
        """Gets the search results matching the given search query using the given search.

        :param objective_bank_query: the objective bank query
        :type objective_bank_query: ``osid.learning.ObjectiveBankQuery``
        :param objective_bank_search: the objective bank search
        :type objective_bank_search: ``osid.learning.ObjectiveBankSearch``
        :return: the search results
        :rtype: ``osid.learning.ObjectiveBankSearchResults``
        :raise: ``NullArgument`` -- ``objective_bank_query`` or ``objective_bank_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_query`` or ``objective_bank_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankSearchResults

    @abc.abstractmethod
    def get_objective_bank_query_from_inspector(self, objective_bank_query_inspector):
        """Gets an objective bank query from an inspector.

        The inspector is available from an
        ``ObjectiveBankSearchResults``.

        :param objective_bank_query_inspector: an objective bank query inspector
        :type objective_bank_query_inspector: ``osid.learning.ObjectiveBankQueryInspector``
        :return: the objective bank query
        :rtype: ``osid.learning.ObjectiveBankQuery``
        :raise: ``NullArgument`` -- ``objective_bank_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``objective_bank_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankQuery


class ObjectiveBankAdminSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_objective_banks(self):
        """Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_objective_bank_with_record_types(self, objective_bank_record_types):
        """Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``ObjectiveBank`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_form_for_create(self, objective_bank_record_types):
        """Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        :param objective_bank_record_types: array of objective bank record types
        :type objective_bank_record_types: ``osid.type.Type[]``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NullArgument`` -- ``objective_bank_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types.

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankForm

    @abc.abstractmethod
    def create_objective_bank(self, objective_bank_form):
        """Creates a new ``ObjectiveBank``.

        :param objective_bank_form: the form for this ``ObjectiveBank``
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :return: the new ``ObjectiveBank``
        :rtype: ``osid.learning.ObjectiveBank``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form`` did not originate from ``get_objective_bank_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBank

    @abc.abstractmethod
    def can_update_objective_banks(self):
        """Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_form_for_update(self, objective_bank_id):
        """Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: the objective bank form
        :rtype: ``osid.learning.ObjectiveBankForm``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankForm

    @abc.abstractmethod
    def update_objective_bank(self, objective_bank_form):
        """Updates an existing objective bank.

        :param objective_bank_form: the form containing the elements to be updated
        :type objective_bank_form: ``osid.learning.ObjectiveBankForm``
        :raise: ``IllegalState`` -- ``objective_bank_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``objective_bank_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``objective_bank_form did not originate from get_objective_bank_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_objective_banks(self):
        """Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``ObjectiveBank`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_objective_bank(self, objective_bank_id):
        """Deletes an ``ObjectiveBank``.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank`` to remove
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_objective_bank_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``ObjectiveBank`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_objective_bank(self, objective_bank_id, alias_id):
        """Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        :param objective_bank_id: the ``Id`` of an ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveBankNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``ObjectiveBank`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session i

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_objective_bank_notifications(self):
        """Tests if this user can register for ``ObjectiveBank`` notifications.

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
    def reliable_objective_bank_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_objective_bank_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_objective_bank_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_objective_bank_notification(self, notification_id):
        """Acknowledge an objective bank notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_objective_banks(self):
        """Register for notifications of new objective banks.

        ``ObjectiveBankReceiver.newObjectiveBanks()`` is invoked when a
        new ``ObjectiveBank`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_banks(self):
        """Registers for notification of updated objective banks.

        ``ObjectiveBankReceiver.changedObjectiveBanks()`` is invoked
        when an objective bank is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_bank(self, objective_bank_id):
        """Registers for notification of an updated objective bank.

        ``ObjectiveBankReceiver.changedObjectiveBanks()`` is invoked
        when the specified objective bank is changed.

        :param objective_bank_id: the ``Id`` of the objective bank to monitor
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_objective_banks(self):
        """Registers for notification of deleted objective banks.

        ``ObjectiveBankReceiver.deletedObjectiveBanks()`` is invoked
        when a calenedar is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_objective_bank(self, objective_bank_id):
        """Registers for notification of a deleted objective bank.

        ``ObjectiveBankReceiver.deletedObjectiveBanks()`` is invoked
        when the specified objective bank is deleted.

        :param objective_bank_id: the ``Id`` of the objective bank to monitor
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_bank_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_bank_hierarchy(self):
        """Registers for notification of an updated objective bank hierarchy structure.

        ``ObjectiveBankReceiver.changedChildOfObjectiveBanks()`` is
        invoked when a node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_bank_hierarchy_for_ancestors(self, objective_bank_id):
        """Registers for notification of an updated objective bank hierarchy structure.

        ``ObjectiveBankReceiver.changedChildOfObjectiveBanks()`` is
        invoked when the specified node or any of its ancestors
        experiences a change in its children.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank`` node to monitor
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_objective_bank_hierarchy_for_descendants(self, objective_bank_id):
        """Registers for notification of an updated objective bank hierarchy structure.

        ``ObjectiveBankReceiver.changedChildOfObjectiveBanks()`` is
        invoked when the specified node or any of its descendants
        experiences a change in its children.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank`` node to monitor
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_objective_bank_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_objective_bank_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_objective_bank_notification(self, notification_id):
        """Acknowledge an objective_bank notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ObjectiveBankHierarchySession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    @abc.abstractmethod
    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    @abc.abstractmethod
    def can_access_objective_bank_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_objective_bank_view(self):
        """The returns from the objective bank methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_objective_bank_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_objective_bank_ids(self):
        """Gets the root objective bank ``Ids`` in this hierarchy.

        :return: the root objective bank ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_objective_bank_ids = property(fget=get_root_objective_bank_ids)

    @abc.abstractmethod
    def get_root_objective_banks(self):
        """Gets the root objective banks in this objective bank hierarchy.

        :return: the root objective banks
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    root_objective_banks = property(fget=get_root_objective_banks)

    @abc.abstractmethod
    def has_parent_objective_banks(self, objective_bank_id):
        """Tests if the ``ObjectiveBank`` has any parents.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the objective bank has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a direct parent of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_objective_bank_ids(self, objective_bank_id):
        """Gets the parent ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_objective_banks(self, objective_bank_id):
        """Gets the parents of the given objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: the parents of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def is_ancestor_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is an ancestor of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_objective_banks(self, objective_bank_id):
        """Tests if an objective bank has any children.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``objective_bank_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an objective bank is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_objective_bank_ids(self, objective_bank_id):
        """Gets the child ``Ids`` of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_objective_banks(self, objective_bank_id):
        """Gets the children of the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :return: the children of the objective bank
        :rtype: ``osid.learning.ObjectiveBankList``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankList

    @abc.abstractmethod
    def is_descendant_of_objective_bank(self, id_, objective_bank_id):
        """Tests if an ``Id`` is a descendant of an objective bank.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``objective_bank_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_objective_bank_node_ids(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_objective_bank_nodes(self, objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given objective bank.

        :param objective_bank_id: the ``Id`` to query
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an objective bank node
        :rtype: ``osid.learning.ObjectiveBankNode``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.learning.ObjectiveBankNode


class ObjectiveBankHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``ObjectiveBank`` objects.

    Each node in the hierarchy is a unique ``ObjectiveBank``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_objective_bank_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    objective_bank_hierarchy_id = property(fget=get_objective_bank_hierarchy_id)

    @abc.abstractmethod
    def get_objective_bank_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    objective_bank_hierarchy = property(fget=get_objective_bank_hierarchy)

    @abc.abstractmethod
    def can_modify_objective_bank_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_objective_bank(self, objective_bank_id):
        """Adds a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_objective_bank(self, objective_bank_id):
        """Removes a root objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` is not a root
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_objective_bank(self, objective_bank_id, child_id):
        """Adds a child to an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``objective_bank_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``objective_bank_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_objective_bank(self, objective_bank_id, child_id):
        """Removes a child from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_objective_banks(self, objective_bank_id):
        """Removes all children from an objective bank.

        :param objective_bank_id: the ``Id`` of an objective bank
        :type objective_bank_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``objective_bank_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
