"""Implementations of logging abstract base class managers."""
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


class LoggingProfile:
    """The logging profile describes the interoperability among logging services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if visible federation is supported.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_logging(self):
        """Tests if logging is supported.

        :return: ``true`` if logging is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_lookup(self):
        """Tests if reading logs is supported.

        :return: ``true`` if reading logs is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_query(self):
        """Tests if querying log entries is supported.

        :return: ``true`` if querying log entries is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_search(self):
        """Tests if searching log entries is supported.

        :return: ``true`` if searching log entries is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_notification(self):
        """Tests if log entry notification is supported,.

        :return: ``true`` if log entry notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_log(self):
        """Tests if looking up log entry log mappings is supported.

        :return: ``true`` if log entry logs is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_log_assignment(self):
        """Tests if managing log entry log mappings is supported.

        :return: ``true`` if log entry logs mapping assignment is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_smart_log(self):
        """Tests if smart logs is supported.

        :return: ``true`` if smart logs is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_lookup(self):
        """Tests for the availability of a log lookup service.

        :return: ``true`` if log lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_query(self):
        """Tests if querying logs is available.

        :return: ``true`` if log query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_search(self):
        """Tests if searching for logs is available.

        :return: ``true`` if log search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_admin(self):
        """Tests for the availability of a log administrative service for creating and deleting logs.

        :return: ``true`` if log administration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_notification(self):
        """Tests for the availability of a log notification service.

        :return: ``true`` if log notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_hierarchy(self):
        """Tests for the availability of a log hierarchy traversal service.

        :return: ``true`` if log hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_hierarchy_design(self):
        """Tests for the availability of a log hierarchy design service.

        :return: ``true`` if log hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_logging_batch(self):
        """Tests for the availability of a logging batch service.

        :return: ``true`` if loggin batch service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_entry_record_types(self):
        """Gets the supported ``Log`` record types.

        :return: a list containing the supported log record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    log_entry_record_types = property(fget=get_log_entry_record_types)

    @abc.abstractmethod
    def supports_log_entry_record_type(self, log_entry_record_type):
        """Tests if the given ``LogEntry`` record type is supported.

        :param log_entry_record_type: a ``Type`` indicating a ``LogEntry`` record type
        :type log_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_entry_search_record_types(self):
        """Gets the supported log entry search record types.

        :return: a list containing the supported log entry search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    @abc.abstractmethod
    def supports_log_entry_search_record_type(self, log_entry_search_record_type):
        """Tests if the given log entry search record type is supported.

        :param log_entry_search_record_type: a ``Type`` indicating a log entry record type
        :type log_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_record_types(self):
        """Gets the supported ``Log`` record types.

        :return: a list containing the supported log record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    log_record_types = property(fget=get_log_record_types)

    @abc.abstractmethod
    def supports_log_record_type(self, log_record_type):
        """Tests if the given ``Log`` record type is supported.

        :param log_record_type: a ``Type`` indicating a ``Log`` record type
        :type log_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_log_search_record_types(self):
        """Gets the supported log search record types.

        :return: a list containing the supported log search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    log_search_record_types = property(fget=get_log_search_record_types)

    @abc.abstractmethod
    def supports_log_search_record_type(self, log_search_record_type):
        """Tests if the given log search record type is supported.

        :param log_search_record_type: a ``Type`` indicating a log record type
        :type log_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_priority_types(self):
        """Gets the priority types supported, in ascending order of the priority level.

        :return: a list containing the supported priority types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    priority_types = property(fget=get_priority_types)

    @abc.abstractmethod
    def supports_priority_type(self, priority_type):
        """Tests if the priority type is supported.

        :param priority_type: a ``Type`` indicating a priority type
        :type priority_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_content_types(self):
        """Gets the content types supported.

        :return: a list containing the supported content types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    content_types = property(fget=get_content_types)

    @abc.abstractmethod
    def supports_content_type(self, content_type):
        """Tests if the content type is supported.

        :param content_type: a ``Type`` indicating a content type
        :type content_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``content_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_log_entry_admin(self):
        """Tests if log entry admin is supported.

        :return: ``true`` if log entry admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class LoggingManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_logging_session(self):
        """Gets the ``OsidSession`` associated with the logging service.

        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` is ``true``.*

        """
        return  # osid.logging.LoggingSession

    logging_session = property(fget=get_logging_session)

    @abc.abstractmethod
    def get_logging_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the logging service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` and ``supports_visible_federation()`` are
        ``true``*

        """
        return  # osid.logging.LoggingSession

    @abc.abstractmethod
    def get_log_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log reading service.

        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` is ``true``.*

        """
        return  # osid.logging.LogEntryLookupSession

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    @abc.abstractmethod
    def get_log_entry_lookup_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log reading service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryLookupSession

    @abc.abstractmethod
    def get_log_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the logging entry query service.

        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` is ``true``.*

        """
        return  # osid.logging.LogEntryQuerySession

    log_entry_query_session = property(fget=get_log_entry_query_session)

    @abc.abstractmethod
    def get_log_entry_query_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log entry query service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryQuerySession

    @abc.abstractmethod
    def get_log_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the logging entry search service.

        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` is ``true``.*

        """
        return  # osid.logging.LogEntrySearchSession

    log_entry_search_session = property(fget=get_log_entry_search_session)

    @abc.abstractmethod
    def get_log_entry_search_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log entry search service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntrySearchSession

    @abc.abstractmethod
    def get_log_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the logging entry administrative service.

        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` is ``true``.*

        """
        return  # osid.logging.LogEntryAdminSession

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    @abc.abstractmethod
    def get_log_entry_admin_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log entry administrative service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryAdminSession

    @abc.abstractmethod
    def get_log_entry_notification_session(self, log_entry_receiver):
        """Gets the ``OsidSession`` associated with the logging entry notification service.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``log_entry_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` is ``true``.*

        """
        return  # osid.logging.LogEntryNotificationSession

    @abc.abstractmethod
    def get_log_entry_notification_session_for_log(self, log_entry_receiver, log_id):
        """Gets the ``OsidSession`` associated with the log entry notification service for the given log.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_entry_receiver`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryNotificationSession

    @abc.abstractmethod
    def get_log_entry_log_session(self):
        """Gets the session for retrieving log entry to log mappings.

        :return: a ``LogEntryLogSession``
        :rtype: ``osid.logging.LogEntryLogSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log()`` is ``true``.*

        """
        return  # osid.logging.LogEntryLogSession

    log_entry_log_session = property(fget=get_log_entry_log_session)

    @abc.abstractmethod
    def get_log_entry_log_assignment_session(self):
        """Gets the session for assigning log entry to logs mappings.

        :return: a ``LogEntryLogAssignmentSession``
        :rtype: ``osid.logging.LogEntryLogAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log_assignment()`` is ``true``.*

        """
        return  # osid.logging.LogEntryLogAssignmentSession

    log_entry_log_assignment_session = property(fget=get_log_entry_log_assignment_session)

    @abc.abstractmethod
    def get_log_entry_smart_log_session(self, log_id):
        """Gets the session for managing dynamic logEntry log.

        :param log_id: the ``Id`` of the log
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntrySmartLogSession``
        :rtype: ``osid.logging.LogEntrySmartLogSession``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_smart_log()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_smart_log()`` is ``true``.*

        """
        return  # osid.logging.LogEntrySmartLogSession

    @abc.abstractmethod
    def get_log_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log lookup service.

        :return: a ``LogLookupSession``
        :rtype: ``osid.logging.LogLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_lookup()`` is ``true``.*

        """
        return  # osid.logging.LogLookupSession

    log_lookup_session = property(fget=get_log_lookup_session)

    @abc.abstractmethod
    def get_log_query_session(self):
        """Gets the ``OsidSession`` associated with the log query service.

        :return: a ``LogQuerySession``
        :rtype: ``osid.logging.LogQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_query()`` is ``true``.*

        """
        return  # osid.logging.LogQuerySession

    log_query_session = property(fget=get_log_query_session)

    @abc.abstractmethod
    def get_log_search_session(self):
        """Gets the ``OsidSession`` associated with the log search service.

        :return: a ``LogSearchSession``
        :rtype: ``osid.logging.LogSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_search()`` is ``true``.*

        """
        return  # osid.logging.LogSearchSession

    log_search_session = property(fget=get_log_search_session)

    @abc.abstractmethod
    def get_log_admin_session(self):
        """Gets the ``OsidSession`` associated with the log administrative service.

        :return: a ``LogAdminSession``
        :rtype: ``osid.logging.LogAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_admin()`` is ``true``.*

        """
        return  # osid.logging.LogAdminSession

    log_admin_session = property(fget=get_log_admin_session)

    @abc.abstractmethod
    def get_log_notification_session(self, log_receiver):
        """Gets the ``OsidSession`` associated with the log notification service.

        :param log_receiver: the receiver
        :type log_receiver: ``osid.logging.LogReceiver``
        :return: a ``LogNotificationSession``
        :rtype: ``osid.logging.LogNotificationSession``
        :raise: ``NullArgument`` -- ``log_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_notification()`` is ``true``.*

        """
        return  # osid.logging.LogNotificationSession

    @abc.abstractmethod
    def get_log_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the log hierarchy service.

        :return: a ``LogHierarchySession`` for logs
        :rtype: ``osid.logging.LogHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy()`` is ``true``.*

        """
        return  # osid.logging.LogHierarchySession

    log_hierarchy_session = property(fget=get_log_hierarchy_session)

    @abc.abstractmethod
    def get_log_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the log hierarchy design service.

        :return: a ``HierarchyDesignSession`` for logs
        :rtype: ``osid.logging.LogHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy_design()`` is ``true``.*

        """
        return  # osid.logging.LogHierarchyDesignSession

    log_hierarchy_design_session = property(fget=get_log_hierarchy_design_session)

    @abc.abstractmethod
    def get_logging_batch_manager(self):
        """Gets a ``LoggingBatchManager``.

        :return: a ``LoggingBatchManager``
        :rtype: ``osid.logging.batch.LoggingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging_batch()`` is ``true``.*

        """
        return  # osid.logging.batch.LoggingBatchManager

    logging_batch_manager = property(fget=get_logging_batch_manager)


class LoggingProxyManager:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_logging_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` is ``true``.*

        """
        return  # osid.logging.LoggingSession

    @abc.abstractmethod
    def get_logging_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the logging service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` and ``supports_visible_federation()`` are
        ``true``*

        """
        return  # osid.logging.LoggingSession

    @abc.abstractmethod
    def get_log_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging reading service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` is ``true``.*

        """
        return  # osid.logging.LogEntryLookupSession

    @abc.abstractmethod
    def get_log_entry_lookup_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log reading service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryLookupSession

    @abc.abstractmethod
    def get_log_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging entry query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` is ``true``.*

        """
        return  # osid.logging.LogEntryQuerySession

    @abc.abstractmethod
    def get_log_entry_query_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry query service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryQuerySession

    @abc.abstractmethod
    def get_log_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging entry search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` is ``true``.*

        """
        return  # osid.logging.LogEntrySearchSession

    @abc.abstractmethod
    def get_log_entry_search_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry search service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntrySearchSession

    @abc.abstractmethod
    def get_log_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging entry administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` is ``true``.*

        """
        return  # osid.logging.LogEntryAdminSession

    @abc.abstractmethod
    def get_log_entry_admin_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry administrative service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryAdminSession

    @abc.abstractmethod
    def get_log_entry_notification_session(self, log_entry_receiver, proxy):
        """Gets the ``OsidSession`` associated with the logging entry notification service.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``log_entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` is ``true``.*

        """
        return  # osid.logging.LogEntryNotificationSession

    @abc.abstractmethod
    def get_log_entry_notification_session_for_log(self, log_entry_receiver, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry notification service for the given log.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_entry_receiver, log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.logging.LogEntryNotificationSession

    @abc.abstractmethod
    def get_log_entry_log_session(self, proxy):
        """Gets the session for retrieving log entry to log mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLogSession``
        :rtype: ``osid.logging.LogEntryLogSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log()`` is ``true``.*

        """
        return  # osid.logging.LogEntryLogSession

    @abc.abstractmethod
    def get_log_entry_log_assignment_session(self, proxy):
        """Gets the session for assigning log entry to log mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLogAssignmentSession``
        :rtype: ``osid.logging.LogEntryLogAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_log_assignment()`` is ``true``.*

        """
        return  # osid.logging.LogEntryLogAssignmentSession

    @abc.abstractmethod
    def get_log_entry_smart_log_session(self, log_id, proxy):
        """Gets the session for managing dynamic log entry logs.

        :param log_id: the ``Id`` of the log
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntrySmartLogSession``
        :rtype: ``osid.logging.LogEntrySmartLogSession``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_smart_log()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_entry_smart_log()`` is ``true``.*

        """
        return  # osid.logging.LogEntrySmartLogSession

    @abc.abstractmethod
    def get_log_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogLookupSession``
        :rtype: ``osid.logging.LogLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_lookup()`` is ``true``.*

        """
        return  # osid.logging.LogLookupSession

    @abc.abstractmethod
    def get_log_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogQuerySession``
        :rtype: ``osid.logging.LogQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_query()`` is ``true``.*

        """
        return  # osid.logging.LogQuerySession

    @abc.abstractmethod
    def get_log_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogSearchSession``
        :rtype: ``osid.logging.LogSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_search()`` is ``true``.*

        """
        return  # osid.logging.LogSearchSession

    @abc.abstractmethod
    def get_log_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogAdminSession``
        :rtype: ``osid.logging.LogAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_admin()`` is ``true``.*

        """
        return  # osid.logging.LogAdminSession

    @abc.abstractmethod
    def get_log_notification_session(self, log_receiver, proxy):
        """Gets the ``OsidSession`` associated with the log notification service.

        :param log_receiver: the receiver
        :type log_receiver: ``osid.logging.LogReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogNotificationSession``
        :rtype: ``osid.logging.LogNotificationSession``
        :raise: ``NullArgument`` -- ``log_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_notification()`` is ``true``.*

        """
        return  # osid.logging.LogNotificationSession

    @abc.abstractmethod
    def get_log_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogHierarchySession`` for logs
        :rtype: ``osid.logging.LogHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy()`` is ``true``.*

        """
        return  # osid.logging.LogHierarchySession

    @abc.abstractmethod
    def get_log_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for logs
        :rtype: ``osid.logging.LogHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_log_hierarchy_design()`` is ``true``.*

        """
        return  # osid.logging.LogHierarchyDesignSession

    @abc.abstractmethod
    def get_logging_batch_proxy_manager(self):
        """Gets a ``LoggingBatchProxyManager``.

        :return: a ``LoggingBatchProxyManager``
        :rtype: ``osid.logging.batch.LoggingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging_batch()`` is ``true``.*

        """
        return  # osid.logging.batch.LoggingBatchProxyManager

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)
