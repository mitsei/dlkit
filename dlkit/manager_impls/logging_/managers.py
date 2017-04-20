"""Manager utility implementations of logging managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import NullArgument
from ..osid.osid_errors import Unimplemented
from ..type.objects import TypeList
from dlkit.abstract_osid.logging_ import managers as abc_logging_managers


class LoggingProfile(abc_logging_managers.LoggingProfile, osid_managers.OsidProfile):
    """The logging profile describes the interoperability among logging services."""

    def supports_visible_federation(self):
        """Tests if visible federation is supported.

        return: (boolean) - ``true`` if visible federation is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_logging(self):
        """Tests if logging is supported.

        return: (boolean) - ``true`` if logging is supported, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_lookup(self):
        """Tests if reading logs is supported.

        return: (boolean) - ``true`` if reading logs is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_query(self):
        """Tests if querying log entries is supported.

        return: (boolean) - ``true`` if querying log entries is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_search(self):
        """Tests if searching log entries is supported.

        return: (boolean) - ``true`` if searching log entries is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_notification(self):
        """Tests if log entry notification is supported,.

        return: (boolean) - ``true`` if log entry notification is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_log(self):
        """Tests if looking up log entry log mappings is supported.

        return: (boolean) - ``true`` if log entry logs is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_log_assignment(self):
        """Tests if managing log entry log mappings is supported.

        return: (boolean) - ``true`` if log entry logs mapping
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_entry_smart_log(self):
        """Tests if smart logs is supported.

        return: (boolean) - ``true`` if smart logs is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_lookup(self):
        """Tests for the availability of a log lookup service.

        return: (boolean) - ``true`` if log lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_query(self):
        """Tests if querying logs is available.

        return: (boolean) - ``true`` if log query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_search(self):
        """Tests if searching for logs is available.

        return: (boolean) - ``true`` if log search is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_admin(self):
        """Tests for the availability of a log administrative service for creating and deleting logs.

        return: (boolean) - ``true`` if log administration is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_notification(self):
        """Tests for the availability of a log notification service.

        return: (boolean) - ``true`` if log notification is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def supports_log_hierarchy(self):
        """Tests for the availability of a log hierarchy traversal service.

        return: (boolean) - ``true`` if log hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_log_hierarchy_design(self):
        """Tests for the availability of a log hierarchy design service.

        return: (boolean) - ``true`` if log hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def supports_logging_batch(self):
        """Tests for the availability of a logging batch service.

        return: (boolean) - ``true`` if loggin batch service is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return False

    def get_log_entry_record_types(self):
        """Gets the supported ``Log`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                log record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def supports_log_entry_record_type(self, log_entry_record_type=None):
        """Tests if the given ``LogEntry`` record type is supported.

        arg:    log_entry_record_type (osid.type.Type): a ``Type``
                indicating a ``LogEntry`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``log_entry_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if log_entry_record_type is None:
            raise NullArgument()
        return False

    def get_log_entry_search_record_types(self):
        """Gets the supported log entry search record types.

        return: (osid.type.TypeList) - a list containing the supported
                log entry search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def supports_log_entry_search_record_type(self, log_entry_search_record_type=None):
        """Tests if the given log entry search record type is supported.

        arg:    log_entry_search_record_type (osid.type.Type): a
                ``Type`` indicating a log entry record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``log_entry_search_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if log_entry_search_record_type is None:
            raise NullArgument()
        return False

    def get_log_record_types(self):
        """Gets the supported ``Log`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                log record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    log_record_types = property(fget=get_log_record_types)

    def supports_log_record_type(self, log_record_type=None):
        """Tests if the given ``Log`` record type is supported.

        arg:    log_record_type (osid.type.Type): a ``Type`` indicating
                a ``Log`` record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``log_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if log_record_type is None:
            raise NullArgument()
        return False

    def get_log_search_record_types(self):
        """Gets the supported log search record types.

        return: (osid.type.TypeList) - a list containing the supported
                log search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    log_search_record_types = property(fget=get_log_search_record_types)

    def supports_log_search_record_type(self, log_search_record_type=None):
        """Tests if the given log search record type is supported.

        arg:    log_search_record_type (osid.type.Type): a ``Type``
                indicating a log record type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``log_search_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if log_search_record_type is None:
            raise NullArgument()
        return False

    def get_priority_types(self):
        """Gets the priority types supported, in ascending order of the priority level.

        return: (osid.type.TypeList) - a list containing the supported
                priority types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    priority_types = property(fget=get_priority_types)

    def supports_priority_type(self, priority_type=None):
        """Tests if the priority type is supported.

        arg:    priority_type (osid.type.Type): a ``Type`` indicating a
                priority type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``priority_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if priority_type is None:
            raise NullArgument()
        return False

    def get_content_types(self):
        """Gets the content types supported.

        return: (osid.type.TypeList) - a list containing the supported
                content types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    content_types = property(fget=get_content_types)

    def supports_content_type(self, content_type=None):
        """Tests if the content type is supported.

        arg:    content_type (osid.type.Type): a ``Type`` indicating a
                content type
        return: (boolean) - ``true`` if the given ``Type`` is supported,
                ``false`` otherwise
        raise:  NullArgument - ``content_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if content_type is None:
            raise NullArgument()
        return False

    def supports_log_entry_admin(self):
        """Tests if log entry admin is supported.

        return: (boolean) - ``true`` if log entry admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False


class LoggingManager(abc_logging_managers.LoggingManager, osid_managers.OsidManager, LoggingProfile):
    """The logging manager provides access to logging sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``LoggingSession:`` a session to write to a log
      * ``LogEntryLookupSession:`` a session to read a log
      * ``LogEntryQuerySession:`` a session to search a log
      * ``LogEntrySearchSession:`` a session to search a log
      * ``LogEntryAdminSession:`` a session to manage log entries in a
        log
      * ``LogEntryNotificationSession:`` a session to subscribe to
        notifications of new log entries
      * ``LogEntryLogSession:`` a session to examine log entry to log
        mappings
      * ``LogEntryLogAssignmentSession:`` a session to manage log entry
        to log mappings
      * ``LogEntrySmartLogSession:`` a session to manage dynamic logs
      * ``LogLookupSession:`` a session to retrieve log objects
      * ``LogQuerySession:`` a session to search for logs
      * ``LogSearchSession:`` a session to search for logs
      * ``LogAdminSession:`` a session to create, update and delete logs
      * ``LogNotificationSession:`` a session to receive notifications
        for changes in logs
      * ``LogHierarchyTraversalSession:`` a session to traverse
        hierarchies of logs
      * ``LogHierarchyDesignSession:`` a session to manage hierarchies
        of logs


    The logging manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def get_logging_session(self):
        """Gets the ``OsidSession`` associated with the logging service.

        return: (osid.logging.LoggingSession) - a ``LoggingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` is ``true``.*

        """
        raise Unimplemented()

    logging_session = property(fget=get_logging_session)

    def get_logging_session_for_log(self, log_id=None):
        """Gets the ``OsidSession`` associated with the logging service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LoggingSession) - a ``LoggingSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` and ``supports_visible_federation()`` are
        ``true``*

        """
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log reading service.

        return: (osid.logging.LogEntryLookupSession) - a
                ``LogEntryLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    def get_log_entry_lookup_session_for_log(self, log_id=None):
        """Gets the ``OsidSession`` associated with the log reading service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LogEntryLookupSession) - a
                ``LogEntryLookupSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the logging entry query service.

        return: (osid.logging.LogEntryQuerySession) - a
                ``LogEntryQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` is ``true``.*

        """
        raise Unimplemented()

    log_entry_query_session = property(fget=get_log_entry_query_session)

    def get_log_entry_query_session_for_log(self, log_id=None):
        """Gets the ``OsidSession`` associated with the log entry query service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LogEntryQuerySession) - a
                ``LogEntryQuerySession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the logging entry search service.

        return: (osid.logging.LogEntrySearchSession) - a
                ``LogEntrySearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` is ``true``.*

        """
        raise Unimplemented()

    log_entry_search_session = property(fget=get_log_entry_search_session)

    def get_log_entry_search_session_for_log(self, log_id=None):
        """Gets the ``OsidSession`` associated with the log entry search service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LogEntrySearchSession) - a
                ``LogEntrySearchSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the logging entry administrative service.

        return: (osid.logging.LogEntryAdminSession) - a
                ``LogEntryAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` is ``true``.*

        """
        raise Unimplemented()

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    def get_log_entry_admin_session_for_log(self, log_id=None):
        """Gets the ``OsidSession`` associated with the log entry administrative service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LogEntryAdminSession) - a
                ``LogEntryAdminSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_notification_session(self, log_entry_receiver=None):
        """Gets the ``OsidSession`` associated with the logging entry notification service.

        arg:    log_entry_receiver (osid.logging.LogEntryReceiver): the
                receiver
        return: (osid.logging.LogEntryNotificationSession) - a
                ``LogEntryNotificationSession``
        raise:  NullArgument - ``log_entry_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_log_entry_notification_session_for_log(self, log_entry_receiver=None, log_id=None):
        """Gets the ``OsidSession`` associated with the log entry notification service for the given log.

        arg:    log_entry_receiver (osid.logging.LogEntryReceiver): the
                receiver
        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        return: (osid.logging.LogEntryNotificationSession) - a
                ``LogEntryNotificationSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_entry_receiver`` or ``log_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_entry_receiver is None:
            raise NullArgument
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_log_session(self):
        """Gets the session for retrieving log entry to log mappings.

        return: (osid.logging.LogEntryLogSession) - a
                ``LogEntryLogSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_log()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log()`` is ``true``.*

        """
        raise Unimplemented()

    log_entry_log_session = property(fget=get_log_entry_log_session)

    def get_log_entry_log_assignment_session(self):
        """Gets the session for assigning log entry to logs mappings.

        return: (osid.logging.LogEntryLogAssignmentSession) - a
                ``LogEntryLogAssignmentSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_log_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log_assignment()`` is ``true``.*

        """
        raise Unimplemented()

    log_entry_log_assignment_session = property(fget=get_log_entry_log_assignment_session)

    def get_log_entry_smart_log_session(self, log_id=None):
        """Gets the session for managing dynamic logEntry log.

        arg:    log_id (osid.id.Id): the ``Id`` of the log
        return: (osid.logging.LogEntrySmartLogSession) - a
                ``LogEntrySmartLogSession``
        raise:  NotFound - ``log_id`` not found
        raise:  NullArgument - ``log_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_smart_log()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_smart_log()`` is ``true``.*

        """
        if log_id is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log lookup service.

        return: (osid.logging.LogLookupSession) - a ``LogLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    log_lookup_session = property(fget=get_log_lookup_session)

    def get_log_query_session(self):
        """Gets the ``OsidSession`` associated with the log query service.

        return: (osid.logging.LogQuerySession) - a ``LogQuerySession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_query()`` is ``true``.*

        """
        raise Unimplemented()

    log_query_session = property(fget=get_log_query_session)

    def get_log_search_session(self):
        """Gets the ``OsidSession`` associated with the log search service.

        return: (osid.logging.LogSearchSession) - a ``LogSearchSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_search()`` is ``true``.*

        """
        raise Unimplemented()

    log_search_session = property(fget=get_log_search_session)

    def get_log_admin_session(self):
        """Gets the ``OsidSession`` associated with the log administrative service.

        return: (osid.logging.LogAdminSession) - a ``LogAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_admin()`` is ``true``.*

        """
        raise Unimplemented()

    log_admin_session = property(fget=get_log_admin_session)

    def get_log_notification_session(self, log_receiver=None):
        """Gets the ``OsidSession`` associated with the log notification service.

        arg:    log_receiver (osid.logging.LogReceiver): the receiver
        return: (osid.logging.LogNotificationSession) - a
                ``LogNotificationSession``
        raise:  NullArgument - ``log_receiver`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_notification()`` is ``true``.*

        """
        raise Unimplemented()

    def get_log_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the log hierarchy service.

        return: (osid.logging.LogHierarchySession) - a
                ``LogHierarchySession`` for logs
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy()`` is ``true``.*

        """
        raise Unimplemented()

    log_hierarchy_session = property(fget=get_log_hierarchy_session)

    def get_log_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the log hierarchy design service.

        return: (osid.logging.LogHierarchyDesignSession) - a
                ``HierarchyDesignSession`` for logs
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy_design()`` is ``true``.*

        """
        raise Unimplemented()

    log_hierarchy_design_session = property(fget=get_log_hierarchy_design_session)

    def get_logging_batch_manager(self):
        """Gets a ``LoggingBatchManager``.

        return: (osid.logging.batch.LoggingBatchManager) - a
                ``LoggingBatchManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging_batch()`` is ``true``.*

        """
        raise Unimplemented()

    logging_batch_manager = property(fget=get_logging_batch_manager)


class LoggingProxyManager(abc_logging_managers.LoggingProxyManager, osid_managers.OsidProxyManager, LoggingProfile):
    """The logging manager provides access to logging sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for the
    purposes of passing information from server environments. The
    sessions included in this manager are:

      * ``LoggingSession:`` a session to write to a log
      * ``LogEntryLookupSession:`` a session to read a log
      * ``LogEntryQuerySession:`` a session to search a log
      * ``LogEntrySearchSession:`` a session to search a log
      * ``LogEntryAdminSession:`` a session to manage log entries in a
        log
      * ``LogEntryNotificationSession:`` a session to subscribe to
        notifications of new log entries
      * ``LogEntryLogSession:`` a session to examine log entry to log
        mappings
      * ``LogEntryLogAssignmentSession:`` a session to manage log entry
        to log mappings
      * ``LogEntrySmartLogSession:`` a session to manage dynamic logs
      * ``LogLookupSession:`` a session to retrieve log objects
      * ``LogQuerySession:`` a session to search for logs
      * ``LogSearchSession:`` a session to search for logs
      * ``LogAdminSession:`` a session to create, update and delete logs
      * ``LogNotificationSession:`` a session to receive notifications
        for changes in logs
      * ``LogHierarchyTraversalSession:`` a session to traverse
        hierarchies of logs
      * ``LogHierarchyDesignSession:`` a session to manage hierarchies
        of logs


    The logging manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def get_logging_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the logging service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LoggingSession) - a ``LoggingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_logging_session_for_log(self, log_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the logging service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LoggingSession) - a ``LoggingSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` and ``supports_visible_federation()`` are
        ``true``*

        """
        if log_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the logging reading service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryLookupSession) - a
                ``LogEntryLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_lookup()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_lookup_session_for_log(self, log_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the log reading service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryLookupSession) - a
                ``LogEntryLookupSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_lookup()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the logging entry query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryQuerySession) - a
                ``LogEntryQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_query_session_for_log(self, log_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the log entry query service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryQuerySession) - a
                ``LogEntryQuerySession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_query()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the logging entry search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntrySearchSession) - a
                ``LogEntrySearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_search()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_search_session_for_log(self, log_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the log entry search service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntrySearchSession) - a
                ``LogEntrySearchSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_search()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the logging entry administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryAdminSession) - a
                ``LogEntryAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_admin()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_admin_session_for_log(self, log_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the log entry administrative service for the given log.

        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryAdminSession) - a
                ``LogEntryAdminSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_admin()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_id is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_notification_session(self, log_entry_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the logging entry notification service.

        arg:    log_entry_receiver (osid.logging.LogEntryReceiver): the
                receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryNotificationSession) - a
                ``LogEntryNotificationSession``
        raise:  NullArgument - ``log_entry_receiver`` or ``proxy`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_notification_session_for_log(self, log_entry_receiver=None, log_id=None, proxy=None):
        """Gets the ``OsidSession`` associated with the log entry notification service for the given log.

        arg:    log_entry_receiver (osid.logging.LogEntryReceiver): the
                receiver
        arg:    log_id (osid.id.Id): the ``Id`` of the ``Log``
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryNotificationSession) - a
                ``LogEntryNotificationSession``
        raise:  NotFound - no ``Log`` found by the given ``Id``
        raise:  NullArgument - ``log_entry_receiver, log_id`` or
                ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_notification()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        if log_entry_receiver is None or proxy is None:
            raise NullArgument
        raise Unimplemented()

    def get_log_entry_log_session(self, proxy=None):
        """Gets the session for retrieving log entry to log mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryLogSession) - a
                ``LogEntryLogSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_log()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_log_assignment_session(self, proxy=None):
        """Gets the session for assigning log entry to log mappings.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntryLogAssignmentSession) - a
                ``LogEntryLogAssignmentSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_log_assignment()``
                is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log_assignment()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_entry_smart_log_session(self, log_id=None, proxy=None):
        """Gets the session for managing dynamic log entry logs.

        arg:    log_id (osid.id.Id): the ``Id`` of the log
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogEntrySmartLogSession) - a
                ``LogEntrySmartLogSession``
        raise:  NotFound - ``log_id`` not found
        raise:  NullArgument - ``log_id`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_entry_smart_log()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_smart_log()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the log lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogLookupSession) - a ``LogLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_lookup()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_query_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the log query service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogQuerySession) - a ``LogQuerySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_query()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_search_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the log search service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogSearchSession) - a ``LogSearchSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_search()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_search()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the log administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogAdminSession) - a ``LogAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_admin()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_notification_session(self, log_receiver=None, proxy=None):
        """Gets the ``OsidSession`` associated with the log notification service.

        arg:    log_receiver (osid.logging.LogReceiver): the receiver
        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogNotificationSession) - a
                ``LogNotificationSession``
        raise:  NullArgument - ``log_receiver`` or ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_notification()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_notification()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_hierarchy_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the log hierarchy service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogHierarchySession) - a
                ``LogHierarchySession`` for logs
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_hierarchy()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_log_hierarchy_design_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the log hierarchy design service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogHierarchyDesignSession) - a
                ``HierarchyDesignSession`` for logs
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_hierarchy_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy_design()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    def get_logging_batch_proxy_manager(self):
        """Gets a ``LoggingBatchProxyManager``.

        return: (osid.logging.batch.LoggingBatchProxyManager) - a
                ``LoggingBatchProxyManager``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging_batch()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging_batch()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)
