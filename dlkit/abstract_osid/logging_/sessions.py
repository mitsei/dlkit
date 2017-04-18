"""Implementations of logging abstract base class sessions."""
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


class LoggingSession:
    """This session is used to log entries to a log."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_id = property(fget=get_log_id)

    @abc.abstractmethod
    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    log = property(fget=get_log)

    @abc.abstractmethod
    def can_log(self):
        """Tests if this user can log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer logging
        operations.

        :return: ``false`` if logging methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def log(self, content, content_type):
        """Logs an item.

        This method is a shortcut to ``createLogEntry()``.

        :param content: the entry to log
        :type content: ``object``
        :param content_type: the type of this entry which must be one of the types returned by ``LoggingManager.getContentTypes()``
        :type content_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``content`` is not of ``content_type``
        :raise: ``NullArgument`` -- ``content`` or ``content_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``LoggingManager.supportsContentType(contentType)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def log_at_priority(self, priority_type, content, content_type):
        """Logs an item.

        :param priority_type: the entry priority
        :type priority_type: ``osid.type.Type``
        :param content: the entry to log
        :type content: ``object``
        :param content_type: the type of this entry which must be one of the types returned by ``LoggingManager.getContentTypes()``
        :type content_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``content`` is not of ``content_type``
        :raise: ``NullArgument`` -- ``content`` , ``content_type`` or ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``LoggingManager.supportsContentType(contentType)`` is ``false`` or ``LoggingManager.supportsPriorityType(priorityType)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_log_entry_form(self):
        """Gets a log entry form for creating a log entry.

        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryForm

    log_entry_form = property(fget=get_log_entry_form)

    @abc.abstractmethod
    def create_log_entry(self, log_entry_form):
        """Logs an entry through the log entry form.

        :param log_entry_form: the log entry form
        :type log_entry_form: ``osid.logging.LogEntryForm``
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``log_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_form`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogEntryLookupSession:
    """This session provides methods for retrieving ``log entries``."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_id = property(fget=get_log_id)

    @abc.abstractmethod
    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    log = property(fget=get_log)

    @abc.abstractmethod
    def can_read_log(self):
        """Tests if this user can read the log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer reading
        operations.

        :return: ``false`` if reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_log_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_log_entry_view(self):
        """A complete view of the ``LogEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in logs which are children
        of this log in the log hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this log only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_log_entry(self, log_entry_id):
        """Gets the ``LogEntry`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``LogEntry`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``LogEntry`` and retained for
        compatibility.

        :param log_entry_id: the ``Id`` of the ``LogEntry`` to retrieve
        :type log_entry_id: ``osid.id.Id``
        :return: the returned ``LogEntry``
        :rtype: ``osid.logging.LogEntry``
        :raise: ``NotFound`` -- no ``LogEntry`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntry

    @abc.abstractmethod
    def get_log_entries_by_ids(self, log_entry_ids):
        """Gets a ``LogEntryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the entries
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible logentries may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param log_entry_ids: the list of ``Ids`` to retrieve
        :type log_entry_ids: ``osid.id.IdList``
        :return: the returned ``LogEntry list``
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``log_entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_genus_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` corresponding to the given log entry genus ``Type`` which doe snot include entries of genus types derived form the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session

        :param log_entry_genus_type: a log entry genus type
        :type log_entry_genus_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_parent_genus_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` corresponding to the given log entry genus ``Type`` and include any additional entries with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param log_entry_genus_type: a log entry genus type
        :type log_entry_genus_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_record_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` containing the given log entry record ``Type``.

        In plenary mode, the returned list contains all known log
        entries or an error results. Otherwise, the returned list may
        contain only those log entries that are accessible through this
        session.

        :param log_entry_genus_type: a log entry genus type
        :type log_entry_genus_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_priority_type(self, priority_type):
        """Gets a ``LogEntryList`` filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param priority_type: a log entry priority type
        :type priority_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_date(self, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_priority_type_and_date(self, priority_type, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param priority_type: a log entry priority type
        :type priority_type: ``osid.type.Type``
        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``priority_type, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_for_resource(self, resource_id):
        """Gets a ``LogEntryList`` for an agent associated with the given resource.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_date_for_resource(self, resource_id, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive for an agent associated with the given resource.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``resource_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries_by_priority_type_and_date_for_resource(self, resource_id, priority_type, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive for an agent associated with the given resource filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param priority_type: a log entry priority type
        :type priority_type: ``osid.type.Type``
        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``resource_id, priority_type, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entries(self):
        """Gets all log entries.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :return: a list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    log_entries = property(fget=get_log_entries)


class LogEntryQuerySession:
    """This session provides methods for searching among log entries.

    The search query is constructed using the ``LogEntryQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated log view: searches include entries in logs of which
        this log is an ancestor in the log hierarchy
      * isolated log view: searches are restricted to entries in this
        log only

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_id = property(fget=get_log_id)

    @abc.abstractmethod
    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the ``Log`` associated with this session
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    log = property(fget=get_log)

    @abc.abstractmethod
    def can_search_log_entries(self):
        """Tests if this user can perform ``LogEntry`` searches.

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
    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in logs which are children
        of this log in the log hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this log only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_log_entry_query(self):
        """Gets a log entry query.

        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryQuery

    log_entry_query = property(fget=get_log_entry_query)

    @abc.abstractmethod
    def get_log_entries_by_query(self, log_entry_query):
        """Gets a list of log entries matching the given log entry query.

        :param log_entry_query: the log entry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :return: the returned ``LogEntryList``
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList


class LogEntrySearchSession:
    """This session provides methods for searching among log entries.

    The search query is constructed using the ``LogEntryQuery``.

    ``get_log_entries_by_query()`` is the basic search method and
    returns a list of log entries. A more advanced search may be
    performed with ``getLogEntriesBySearch()``. It accepts a
    ``LogEntrySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_log_entries_by_search()`` returns a
    ``LogEntrySearchResults`` that can be used to access the resulting
    ``LogEntryList`` or be used to perform a search within the result
    set through ``LogEntrySearch``.

    This session defines views that offer differing behaviors for
    searching.

      * federated log view: searches include entries in logs of which
        this log is an ancestor in the log hierarchy
      * isolated log view: searches are restricted to entries in this
        log only

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_entry_search(self):
        """Gets a log entry search.

        :return: the log entry search
        :rtype: ``osid.logging.LogEntrySearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntrySearch

    log_entry_search = property(fget=get_log_entry_search)

    @abc.abstractmethod
    def get_log_entry_search_order(self):
        """Gets a log entry search order.

        The ``LogEntrySearchOrder`` is supplied to a ``LogEntrySearch``
        to specify the ordering of results.

        :return: the log entry search order
        :rtype: ``osid.logging.LogEntrySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntrySearchOrder

    log_entry_search_order = property(fget=get_log_entry_search_order)

    @abc.abstractmethod
    def get_log_entries_by_search(self, log_entry_query, log_entry_search):
        """Gets the search results matching the given search query using the given search.

        :param log_entry_query: the log entry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :param log_entry_search: the log entry search
        :type log_entry_search: ``osid.logging.LogEntrySearch``
        :return: the returned search results
        :rtype: ``osid.logging.LogEntrySearchResults``
        :raise: ``NullArgument`` -- ``log_entry_query`` or ``log_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_query`` or ``log_entry_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntrySearchResults

    @abc.abstractmethod
    def get_log_entry_query_from_inspector(self, log_entry_query_inspector):
        """Gets a log entry query from an inspector.

        The inspector is available from a ``LogEntrySearchResults``.

        :param log_entry_query_inspector: a log entry query inspector
        :type log_entry_query_inspector: ``osid.logging.LogQueryInspector``
        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_entry_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryQuery


class LogEntryAdminSession:
    """This session creates, updates, and deletes ``LogEntries``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``LogEntry,`` a ``LogEntryForm`` is requested using
    ``get_log_entry_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LogEntryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LogEntryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LogEntryForm``
    corresponds to an attempted transaction.

    For updates, ``LogEntryForms`` are requested to the ``LogEntry``
    ``Id`` that is to be updated using ``getLogEntryFormForUpdate()``.
    Similarly, the ``LogEntryForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``LogEntryForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``LogEntries``. To unmap a ``LogEntry``
    from the current ``Log,`` the ``LogEntryLogAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``LogEntry`` itself thus removing it from all known ``Log``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_id = property(fget=get_log_id)

    @abc.abstractmethod
    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the ``Log`` associated with this session
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    log = property(fget=get_log)

    @abc.abstractmethod
    def can_create_log_entries(self):
        """Tests if this user can create log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_log_entry_with_record_types(self, log_entry_record_types):
        """Tests if this user can create a single ``LogEntry`` using the desired record types.

        While ``LoggingManager.getLogEntryRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``LogEntry``.
        Providing an empty array tests if a ``LogEntry`` can be created
        with no records.

        :param log_entry_record_types: array of log entry record types
        :type log_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``LogEntry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_entry_form_for_create(self, log_entry_record_types):
        """Gets the log entry form for creating new log entries.

        A new form should be requested for each create transaction.

        :param log_entry_record_types: array of log entry record types
        :type log_entry_record_types: ``osid.type.Type[]``
        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``
        :raise: ``NullArgument`` -- ``log_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryForm

    @abc.abstractmethod
    def create_log_entry(self, log_entry_form):
        """Creates a new ``LogEntry``.

        :param log_entry_form: the form for this ``LogEntry``
        :type log_entry_form: ``osid.logging.LogEntryForm``
        :return: the new ``LogEntry``
        :rtype: ``osid.logging.LogEntry``
        :raise: ``IllegalState`` -- ``log_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``log_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_form`` did not originate from ``get_log_entry_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntry

    @abc.abstractmethod
    def can_update_log_entries(self):
        """Tests if this user can update log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_entry_form_for_update(self, log_entry_id):
        """Gets the log entry form for updating an existing log.

        A new log entry form should be requested for each update
        transaction.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryForm

    @abc.abstractmethod
    def update_log_entry(self, log_entry_form):
        """Updates an existing log entry.

        :param log_entry_form: the form containing the elements to be updated
        :type log_entry_form: ``osid.logging.LogEntryForm``
        :raise: ``IllegalState`` -- ``log_entry_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``log_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_form`` did not originate from ``get_log_entry_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_log_entries(self):
        """Tests if this user can delete log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_log_entry(self, log_entry_id):
        """Deletes a ``LogEntry``.

        :param log_entry_id: the ``Id`` of the ``log_entry_id`` to remove
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_log_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``LogEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_log_entry(self, log_entry_id, alias_id):
        """Adds an ``Id`` to a ``LogEntry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``LogEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another log entry, it is
        reassigned to the given log entry ``Id``.

        :param log_entry_id: the ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``log_entry_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogEntryNotificationSession:
    """This session defines methods to receive notifications on new or deleted log entries.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to assignments of ``Ids``
    to this log. For notifications of changes to the ``Log`` object use
    ``LogNotificationSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_id = property(fget=get_log_id)

    @abc.abstractmethod
    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the ``Log`` associated with this session
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    log = property(fget=get_log)

    @abc.abstractmethod
    def can_register_for_log_entry_notifications(self):
        """Tests if this user can register for ``Log`` entry notifications.

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
    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries from parent logs in the
        log hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for entries to this log
        only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_log_entry_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_log_entry_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_log_entry_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_log_entry_notification(self, notification_id):
        """Acknowledge a log entry notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_log_entries(self):
        """Register for notifications of new log entries.

        ``LogEntryReceiver.newLogEntries()`` is invoked when a new
        ``LogEntry`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_log_entries_at_priority(self, priority_type):
        """Register for notifications of new log entries at or above the given priority type.

        ``LogEntryReceiver.newLogEntries()`` is invoked when a new
        ``LogEntry`` is created.

        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_log_entries_for_resource(self, resource_id):
        """Register for notifications of new log entries logged by an agent associated with the given resource.

        ``LogEntryReceiver.newLogEntries()`` is invoked when a new
        ``LogEntry`` is created.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_log_entries(self):
        """Register for notifications of updated log entries.

        ``LogEntryReceiver.changedLogEntries()`` is invoked when a
        ``LogEntry`` iin this log is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_entries_at_priority(self, priority_type):
        """Register for notifications of updated log entries at or above the given priority type.

        ``LogEntryReceiver.changedLogEntries()`` is invoked when a
        ``LogEntry`` in this log is changed.

        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_entries_for_resource(self, resource_id):
        """Register for notifications of updated log entries logged by an agent associated with the given resource.

        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` in this log is changed.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_log_entry(self, log_entry_id):
        """Registers for notification of an updated log entry.

        ``LogEntryReceiver.changedLogEntries()`` is invoked when the
        specified log entry is changed.

        :param log_entry_id: the ``Id`` of the ``LogEntry`` to monitor
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_log_entries(self):
        """Registers for notification of deleted log entries.

        ``LogEntryReceiver.deletedLogEntries()`` is invoked when a log
        entry is deleted or removed from this log.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_log_entries_at_priority(self, priority_type):
        """Register for notifications of deleted log entries at or above the given priority type.

        ``LogEntryReceiver.deletedLogEntries()`` is invoked when a
        ``LogEntry`` is deleted or removed from this log.

        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_log_entries_for_resource(self, resource_id):
        """Register for notifications of deleted log entries logged by an agent associated with the given resource.

        ``LogEntryReceiver.deletedLogEntries()`` is invoked when a
        ``LogEntry`` is deleted or removed from this log.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_log_entry(self, log_entry_id):
        """Registers for notification of a deleted log entry.

        ``LogEntryReceiver.deleteddLogEntries()`` is invoked when the
        specified log entry is deleted or removed from this log.

        :param log_entry_id: the ``Id`` of the ``LogEntry`` to monitor
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_log_entry_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_log_entry_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_log_entry_notification(self, notification_id):
        """Acknowledge an log_entry notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogEntryLogSession:
    """This session provides methods to retrieve ``LogEntry`` to ``Log`` mappings.

    An entry may appear in multiple ``Logs``. Each ``Log`` may have its
    own authorizations governing who is allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_log_view(self):
        """A complete view of the ``LogEntry`` and ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_lookup_log_entry_log_mappings(self):
        """Tests if this user can perform lookups of logEntry/log mappings.

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
    def get_log_entry_ids_by_log(self, log_id):
        """Gets the list of ``LogEntry``  ``Ids`` associated with a ``Log``.

        :param log_id: ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of related logEntry ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_log_entries_by_log(self, log_id):
        """Gets the list of log entries associated with a ``Log``.

        :param log_id: ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of related logEntry
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_entry_ids_by_log(self, log_ids):
        """Gets the list of ``LogEntry Ids`` corresponding to a list of ``Log`` objects.

        :param log_ids: list of log ``Ids``
        :type log_ids: ``osid.id.IdList``
        :return: list of logEntry ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_log_entrie_by_log(self, log_ids):
        """Gets the list of log entries corresponding to a list of ``Log``.

        :param log_ids: list of log ``Ids``
        :type log_ids: ``osid.id.IdList``
        :return: list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryList

    @abc.abstractmethod
    def get_log_ids_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log``  ``Ids`` mapped to a ``LogEntry``.

        :param log_entry_id: ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_log_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log`` objects mapped to a ``LogEntry``.

        :param log_entry_id: ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of log
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList


class LogEntryLogAssignmentSession:
    """This session provides methods to re-assign log entries to ``Logs``.

    A ``LogEntry`` may map to multiple ``Log`` objects and removing the
    last reference to a ``LogEntry`` is the equivalent of deleting it.
    Each ``Log`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of a ``LogEntry`` to another ``Log`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_log_entries(self):
        """Tests if this user can alter log entry/log mappings.

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
    def can_assign_log_entries_to_log(self, log_id):
        """Tests if this user can alter log entry/log mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_log_ids(self, log_id):
        """Gets a list of log including and under the given log node in which any log entry can be assigned.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of assignable log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_log_ids_for_log_entry(self, log_id, log_entry_id):
        """Gets a list of log including and under the given log node in which a specific log entry can be assigned.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of assignable log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_id`` or ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_log_entry_to_log(self, log_entry_id, log_id):
        """Adds an existing ``LogEntry`` to a ``Log``.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_entry_id`` is already assigned to ``log_id``
        :raise: ``NotFound`` -- ``log_entry_id`` or ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_log_entry_from_log(self, log_entry_id, log_id):
        """Removes a ``LogEntry`` from a ``Log``.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` or ``log_id`` not found or ``log_entry_id`` not assigned to ``log_id``
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_log_entry_to_log(self, log_entry_id, from_log_id, to_log_id):
        """Moves a ``LogEntry`` from one ``Log`` to another.

        Mappings to other ``Logs`` are unaffected.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param from_log_id: the ``Id`` of the current ``Log``
        :type from_log_id: ``osid.id.Id``
        :param to_log_id: the ``Id`` of the destination ``Log``
        :type to_log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id, from_log_id,`` or ``to_log_id`` not found or ``log_entry_id`` not mapped to ``from_log_id``
        :raise: ``NullArgument`` -- ``log_entry_id, from_log_id,`` or ``to_log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogEntrySmartLogSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``LogEntryQuery`` can be retrieved from this session and mapped to
    this ``Log`` to create a virtual collection of log entries. The log
    entries may be sequenced using the ``LogEntrySearchOrder`` from this
    session.

    This ``Log`` has a default query that matches any log entry and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``LogEntryQueryInspector``. The query may be
    modified by converting the inspector back to a ``LogEntryQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_id = property(fget=get_log_id)

    @abc.abstractmethod
    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the ``Log`` associated with this session
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    log = property(fget=get_log)

    @abc.abstractmethod
    def can_manage_smart_log(self):
        """Tests if this user can manage smart log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart log management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_entry_query(self):
        """Gets a logEntry query.

        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryQuery

    log_entry_query = property(fget=get_log_entry_query)

    @abc.abstractmethod
    def get_log_entry_search_order(self):
        """Gets a logEntry search order.

        :return: the logEntry search order
        :rtype: ``osid.logging.LogEntrySearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntrySearchOrder

    log_entry_search_order = property(fget=get_log_entry_search_order)

    @abc.abstractmethod
    def apply_log_entry_query(self, log_entry_query):
        """Applies a logEntry query to this log.

        :param log_entry_query: the logEntry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``log_entry_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspect_log_entry_query(self):
        """Gets a logEntry query inspector for this log.

        :return: the logEntry query inspector
        :rtype: ``osid.logging.LogEntryQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryQueryInspector

    @abc.abstractmethod
    def apply_log_entry_sequencing(self, log_entry_search_order):
        """Applies a logEntry search order to this log.

        :param log_entry_search_order: the logEntry search order
        :type log_entry_search_order: ``osid.logging.LogEntrySearchOrder``
        :raise: ``NullArgument`` -- ``log_entry_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``log_entry_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_log_entry_query_from_inspector(self, log_entry_query_inspector):
        """Gets a logEntry query from an inspector.

        :param log_entry_query_inspector: a resorce relationship query inspector
        :type log_entry_query_inspector: ``osid.logging.LogEntryQueryInspector``
        :return: the logEntry query
        :rtype: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_entry_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogEntryQuery


class LogLookupSession:
    """This session provides methods for retrieving ``Log`` objects.

    The ``Log`` represents a collection of log entries.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Logs`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Logs`` referenced
    by it are available, and a test-taking applicationmay sacrifice some
    interoperability for the sake of precision.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_logs(self):
        """Tests if this user can perform ``Log`` lookups.

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
    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_log_view(self):
        """A complete view of the ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_log(self, log_id):
        """Gets the ``Log`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Log`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Log`` and retained for compatibility.

        :param log_id: ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.logging.Log

    @abc.abstractmethod
    def get_logs_by_ids(self, log_ids):
        """Gets a ``LogList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the logs
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Logs`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param log_ids: the list of ``Ids`` to retrieve
        :type log_ids: ``osid.id.IdList``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def get_logs_by_genus_type(self, log_genus_type):
        """Gets a ``LogList`` corresponding to the given log genus ``Type`` which does not include logs of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param log_genus_type: a log genus type
        :type log_genus_type: ``osid.type.Type``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def get_logs_by_parent_genus_type(self, log_genus_type):
        """Gets a ``LogList`` corresponding to the given log genus ``Type`` and include any additional logs with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param log_genus_type: a log genus type
        :type log_genus_type: ``osid.type.Type``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def get_logs_by_record_type(self, log_record_type):
        """Gets a ``LogList`` containing the given log record ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param log_record_type: a log record type
        :type log_record_type: ``osid.type.Type``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def get_logs_by_provider(self, resource_id):
        """Gets a ``LogList`` for a given provider.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def get_logs(self):
        """Gets all ``Logs``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :return: a list of ``Logs``
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    logs = property(fget=get_logs)


class LogQuerySession:
    """This session provides methods for searching ``Log`` objects.

    The search query is constructed using the ``LogQuery``. The log
    record ``Type`` also specifies the record for the log query.

    Logs may have a query record indicated by their respective record
    types. The query record is accessed via the ``LogQuery``. The
    returns in this session may not be cast directly to these
    interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_logs(self):
        """Tests if this user can perform ``Log`` searches.

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
    def get_log_query(self):
        """Gets a log query.

        :return: the log query
        :rtype: ``osid.logging.LogQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogQuery

    log_query = property(fget=get_log_query)

    @abc.abstractmethod
    def get_logs_by_query(self, log_query):
        """Gets a list of ``Logs`` matching the given log query.

        :param log_query: the log query
        :type log_query: ``osid.logging.LogQuery``
        :return: the returned ``LogList``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList


class LogSearchSession:
    """This session provides methods for searching ``Log`` objects.

    The search query is constructed using the ``LogQuery`` . The log
    record ``Type`` also specifies the record for the log query.

    ``get_logs_by_query()`` is the basic search method and returns a
    list of ``Log`` elements. A more advanced search may be performed
    with ``getLogsBySearch()``. It accepts a ``LogSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_logs_by_search()`` returns a ``LogSearchResults`` that can be
    used to access the resulting ``LogList`` or be used to perform a
    search within the result set through ``LogSearch``.

    Logs may have a query record indicated by their respective record
    types. The query record is accessed via the ``LogQuery``. The
    returns in this session may not be cast directly to these
    interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_search(self):
        """Gets a log search.

        :return: the log search
        :rtype: ``osid.logging.LogSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogSearch

    log_search = property(fget=get_log_search)

    @abc.abstractmethod
    def get_log_search_order(self):
        """Gets a log search order.

        The ``LogSearchOrder`` is supplied to a ``LogSearch`` to specify
        the ordering of results.

        :return: the log search order
        :rtype: ``osid.logging.LogSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogSearchOrder

    log_search_order = property(fget=get_log_search_order)

    @abc.abstractmethod
    def get_logs_by_search(self, log_query, log_search):
        """Gets the search results matching the given search.

        :param log_query: the log query
        :type log_query: ``osid.logging.LogQuery``
        :param log_search: the log search
        :type log_search: ``osid.logging.LogSearch``
        :return: the log search results
        :rtype: ``osid.logging.LogSearchResults``
        :raise: ``NullArgument`` -- ``log_query`` or ``log_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_query`` or ``log_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogSearchResults

    @abc.abstractmethod
    def get_log_query_from_inspector(self, log_query_inspector):
        """Gets a log query from an inspector.

        The inspector is available from a ``LogSearchResults``.

        :param log_query_inspector: a log query inspector
        :type log_query_inspector: ``osid.logging.LogQueryInspector``
        :return: the log query
        :rtype: ``osid.logging.LogQuery``
        :raise: ``NullArgument`` -- ``log_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogQuery


class LogAdminSession:
    """This session creates, updates, and deletes ``Logs``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Log,`` a ``LogForm`` is requested using
    ``get_log_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LogForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LogForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LogForm`` corresponds
    to an attempted transaction.

    For updates, ``LogForms`` are requested to the ``Log``  ``Id`` that
    is to be updated using ``getLogFormForUpdate()``. Similarly, the
    ``LogForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``LogForm``
    can only be used once for a successful update and cannot be reused.

    The delete operations delete ``Logs``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_logs(self):
        """Tests if this user can create ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Log`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_log_with_record_types(self, log_record_types):
        """Tests if this user can create a single ``Log`` using the desired record types.

        While ``LoggingManager.getLogRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Log``.
        Providing an empty array tests if a ``Log`` can be created with
        no records.

        :param log_record_types: array of log record types
        :type log_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Log`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_form_for_create(self, log_record_types):
        """Gets the log form for creating new logs.

        A new form should be requested for each create transaction.

        :param log_record_types: array of log record types
        :type log_record_types: ``osid.type.Type[]``
        :return: the log form
        :rtype: ``osid.logging.LogForm``
        :raise: ``NullArgument`` -- ``log_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogForm

    @abc.abstractmethod
    def create_log(self, log_form):
        """Creates a new ``Log``.

        :param log_form: the form for this ``Log``
        :type log_form: ``osid.logging.LogForm``
        :return: the new ``Log``
        :rtype: ``osid.logging.Log``
        :raise: ``IllegalState`` -- ``log_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``log_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_form`` did not originate from ``get_log_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.Log

    @abc.abstractmethod
    def can_update_logs(self):
        """Tests if this user can update ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Log`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_form_for_update(self, log_id):
        """Gets the log form for updating an existing log.

        A new log form should be requested for each update transaction.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: the log form
        :rtype: ``osid.logging.LogForm``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogForm

    @abc.abstractmethod
    def update_log(self, log_form):
        """Updates an existing log.

        :param log_form: the form containing the elements to be updated
        :type log_form: ``osid.logging.LogForm``
        :raise: ``IllegalState`` -- ``log_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``log_id`` or ``log_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_form`` did not originate from ``get_log_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_logs(self):
        """Tests if this user can delete ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Log`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_log(self, log_id):
        """Deletes a ``Log``.

        :param log_id: the ``Id`` of the ``Log`` to remove
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_log_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Log`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_log(self, log_id, alias_id):
        """Adds an ``Id`` to a ``Log`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Log`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another log, it is reassigned to the
        given log ``Id``.

        :param log_id: the ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Log`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to the ``Log`` object
    itself. Adding and removing entries result in notifications
    available from the notification session for log entries.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_log_notifications(self):
        """Tests if this user can register for ``Log`` notifications.

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
    def reliable_log_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_log_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_log_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_log_notification(self, notification_id):
        """Acknowledge a log notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_logs(self):
        """Register for notifications of new logs.

        ``LogReceiver.newLogs()`` is invoked when a new ``Log`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_logs(self):
        """Registers for notification of updated logs.

        ``LogReceiver.changedLogs()`` is invoked when a log is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_log(self, log_id):
        """Registers for notification of an updated log.

        ``LogReceiver.changedLogs()`` is invoked when the specified log
        is changed.

        :param log_id: the ``Id`` of the ``Log`` to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_logs(self):
        """Registers for notification of deleted logs.

        ``LogReceiver.deletedLogs()`` is invoked when a log is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_log(self, log_id):
        """Registers for notification of a deleted log.

        ``LogReceiver.deletedLogs()`` is invoked when the specified log
        is deleted.

        :param log_id: the ``Id`` of the ``Log`` to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_log_hierarchy(self):
        """Registers for notification of an updated log hierarchy structure.

        ``LogReceiver.changedChildOfLogs()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_log_hierarchy_for_ancestors(self, log_id):
        """Log ``Receiver.

        changedChildOfLogs()`` is invoked when the specified node or any
        of its ancestors experiences a change in its children.

        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_log_hierarchy_for_descendants(self, log_id):
        """Registers for notification of an updated log hierarchy structure.

        ``LogReceiver.changedChildOfLogs()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_log_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_log_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_log_notification(self, notification_id):
        """Acknowledge an log notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Log`` objects.

    Each node in the hierarchy is a unique ``Log``. The hierarchy may be
    traversed recursively to establish the tree structure through
    ``get_parent_logs()`` and ``getChildLogs()``. To relate these
    ``Ids`` to another OSID, ``get_log_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Log`` available in the Log OSID is known to this hierarchy but
    does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_logs()`` or ``get_child_logs()`` in lieu of
    a ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: log elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    @abc.abstractmethod
    def get_log_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    log_hierarchy = property(fget=get_log_hierarchy)

    @abc.abstractmethod
    def can_access_log_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_log_view(self):
        """The returns from the log methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_log_view(self):
        """A complete view of the ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_log_ids(self):
        """Gets the root log ``Ids`` in this hierarchy.

        :return: the root log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_log_ids = property(fget=get_root_log_ids)

    @abc.abstractmethod
    def get_root_logs(self):
        """Gets the root logs in the log hierarchy.

        A node with no parents is an orphan. While all log ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root logs
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.logging.LogList

    root_logs = property(fget=get_root_logs)

    @abc.abstractmethod
    def has_parent_logs(self, log_id):
        """Tests if the ``Log`` has any parents.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the log has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct parent of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_log_ids(self, log_id):
        """Gets the parent ``Ids`` of the given log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the log
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_logs(self, log_id):
        """Gets the parent logs of the given ``id``.

        :param log_id: the ``Id`` of the ``Log`` to query
        :type log_id: ``osid.id.Id``
        :return: the parent logs of the ``id``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- a ``Log`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def is_ancestor_of_log(self, id_, log_id):
        """Tests if an ``Id`` is an ancestor of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is an ancestor of the ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_logs(self, log_id):
        """Tests if a log has any children.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``log_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct child of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a child of ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_log_ids(self, log_id):
        """Gets the child ``Ids`` of the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_logs(self, log_id):
        """Gets the child logs of the given ``id``.

        :param log_id: the ``Id`` of the ``Log`` to query
        :type log_id: ``osid.id.Id``
        :return: the child logs of the ``id``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- a ``Log`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogList

    @abc.abstractmethod
    def is_descendant_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a descendant of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_node_ids(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a log node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_log_nodes(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a log node
        :rtype: ``osid.logging.LogNode``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.LogNode


class LogHierarchyDesignSession:
    """This session manages a hierarchy of logs.

    Logs may be organized into a hierarchy for organizing or federating.
    A parent ``Log`` includes all of the Ids of its children such that a
    single root node contains all of the ``Ids`` of the federation.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    @abc.abstractmethod
    def get_log_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    log_hierarchy = property(fget=get_log_hierarchy)

    @abc.abstractmethod
    def can_modify_log_hierarchy(self):
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
    def add_root_log(self, log_id):
        """Adds a root log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_log(self, log_id):
        """Removes a root log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` is not a root
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_log(self, log_id, child_id):
        """Adds a child to a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``log_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_log(self, log_id, child_id):
        """Removes a child from a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``log_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_logs(self, log_id):
        """Removes all children from a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
