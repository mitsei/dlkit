"""JSON implementations of logging managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import profile
from . import sessions
from .. import utilities
from ..osid import managers as osid_managers
from ..primitives import Type
from ..type.objects import TypeList
from ..utilities import get_registry
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.logging_ import managers as logging_managers


class LoggingProfile(osid_managers.OsidProfile, logging_managers.LoggingProfile):
    """The logging profile describes the interoperability among logging services."""

    def supports_logging(self):
        """Tests if logging is supported.

        return: (boolean) - ``true`` if logging is supported, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_logging' in profile.SUPPORTS

    def supports_log_entry_lookup(self):
        """Tests if reading logs is supported.

        return: (boolean) - ``true`` if reading logs is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_entry_lookup' in profile.SUPPORTS

    def supports_log_entry_query(self):
        """Tests if querying log entries is supported.

        return: (boolean) - ``true`` if querying log entries is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_entry_query' in profile.SUPPORTS

    def supports_log_entry_log(self):
        """Tests if looking up log entry log mappings is supported.

        return: (boolean) - ``true`` if log entry logs is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_entry_log' in profile.SUPPORTS

    def supports_log_entry_log_assignment(self):
        """Tests if managing log entry log mappings is supported.

        return: (boolean) - ``true`` if log entry logs mapping
                assignment is supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_entry_log_assignment' in profile.SUPPORTS

    def supports_log_lookup(self):
        """Tests for the availability of a log lookup service.

        return: (boolean) - ``true`` if log lookup is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_lookup' in profile.SUPPORTS

    def supports_log_admin(self):
        """Tests for the availability of a log administrative service for creating and deleting logs.

        return: (boolean) - ``true`` if log administration is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_admin' in profile.SUPPORTS

    def supports_log_hierarchy(self):
        """Tests for the availability of a log hierarchy traversal service.

        return: (boolean) - ``true`` if log hierarchy traversal is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_hierarchy' in profile.SUPPORTS

    def supports_log_hierarchy_design(self):
        """Tests for the availability of a log hierarchy design service.

        return: (boolean) - ``true`` if log hierarchy design is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_hierarchy_design' in profile.SUPPORTS

    def get_log_entry_record_types(self):
        """Gets the supported ``Log`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                log record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('LOG_ENTRY_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def get_log_entry_search_record_types(self):
        """Gets the supported log entry search record types.

        return: (osid.type.TypeList) - a list containing the supported
                log entry search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('LOG_ENTRY_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def get_log_record_types(self):
        """Gets the supported ``Log`` record types.

        return: (osid.type.TypeList) - a list containing the supported
                log record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('LOG_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    log_record_types = property(fget=get_log_record_types)

    def get_log_search_record_types(self):
        """Gets the supported log search record types.

        return: (osid.type.TypeList) - a list containing the supported
                log search record types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = get_registry('LOG_SEARCH_RECORD_TYPES', self._runtime)
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    log_search_record_types = property(fget=get_log_search_record_types)

    def get_priority_types(self):
        """Gets the priority types supported, in ascending order of the priority level.

        return: (osid.type.TypeList) - a list containing the supported
                priority types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    priority_types = property(fget=get_priority_types)

    def get_content_types(self):
        """Gets the content types supported.

        return: (osid.type.TypeList) - a list containing the supported
                content types
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.repository.RepositoryProfile.get_coordinate_types
        return TypeList([])

    content_types = property(fget=get_content_types)

    def supports_log_entry_admin(self):
        """Tests if log entry admin is supported.

        return: (boolean) - ``true`` if log entry admin is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_log_entry_admin' in profile.SUPPORTS


class LoggingManager(osid_managers.OsidManager, LoggingProfile, logging_managers.LoggingManager):
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
    def __init__(self):
        osid_managers.OsidManager.__init__(self)

    @utilities.remove_null_proxy_kwarg
    def get_logging_session(self):
        """Gets the ``OsidSession`` associated with the logging service.

        return: (osid.logging.LoggingSession) - a ``LoggingSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` is ``true``.*

        """
        if not self.supports_logging():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LoggingSession(runtime=self._runtime)

    logging_session = property(fget=get_logging_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_logging_session_for_log(self, log_id):
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
        if not self.supports_logging():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LoggingSession(log_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_entry_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryLookupSession(runtime=self._runtime)

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_log_entry_lookup_session_for_log(self, log_id):
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
        if not self.supports_log_entry_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LogEntryLookupSession(log_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_entry_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryQuerySession(runtime=self._runtime)

    log_entry_query_session = property(fget=get_log_entry_query_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_log_entry_query_session_for_log(self, log_id):
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
        if not self.supports_log_entry_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LogEntryQuerySession(log_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_entry_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryAdminSession(runtime=self._runtime)

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_log_entry_admin_session_for_log(self, log_id):
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
        if not self.supports_log_entry_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LogEntryAdminSession(log_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_entry_log():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryLogSession(runtime=self._runtime)

    log_entry_log_session = property(fget=get_log_entry_log_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_entry_log_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryLogAssignmentSession(runtime=self._runtime)

    log_entry_log_assignment_session = property(fget=get_log_entry_log_assignment_session)

    @utilities.remove_null_proxy_kwarg
    def get_log_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log lookup service.

        return: (osid.logging.LogLookupSession) - a ``LogLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_lookup()`` is ``true``.*

        """
        if not self.supports_log_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogLookupSession(runtime=self._runtime)

    log_lookup_session = property(fget=get_log_lookup_session)

    @utilities.remove_null_proxy_kwarg
    def get_log_admin_session(self):
        """Gets the ``OsidSession`` associated with the log administrative service.

        return: (osid.logging.LogAdminSession) - a ``LogAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_admin()`` is ``true``.*

        """
        if not self.supports_log_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogAdminSession(runtime=self._runtime)

    log_admin_session = property(fget=get_log_admin_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogHierarchySession(runtime=self._runtime)

    log_hierarchy_session = property(fget=get_log_hierarchy_session)

    @utilities.remove_null_proxy_kwarg
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
        if not self.supports_log_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogHierarchyDesignSession(runtime=self._runtime)

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
        raise errors.Unimplemented()

    logging_batch_manager = property(fget=get_logging_batch_manager)


class LoggingProxyManager(osid_managers.OsidProxyManager, LoggingProfile, logging_managers.LoggingProxyManager):
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
    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)

    @utilities.arguments_not_none
    def get_logging_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LoggingSession) - a ``LoggingSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_logging()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_logging()`` is ``true``.*

        """
        if not self.supports_logging():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LoggingSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_logging_session_for_log(self, log_id, proxy):
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
        if not self.supports_logging():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LoggingSession(log_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_lookup_session(self, proxy):
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
        if not self.supports_log_entry_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_lookup_session_for_log(self, log_id, proxy):
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
        if not self.supports_log_entry_lookup():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LogEntryLookupSession(log_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_query_session(self, proxy):
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
        if not self.supports_log_entry_query():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryQuerySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_query_session_for_log(self, log_id, proxy):
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
        if not self.supports_log_entry_query():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LogEntryQuerySession(log_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_admin_session(self, proxy):
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
        if not self.supports_log_entry_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_admin_session_for_log(self, log_id, proxy):
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
        if not self.supports_log_entry_admin():
            raise errors.Unimplemented()
        ##
        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        ##
        # pylint: disable=no-member
        return sessions.LogEntryAdminSession(log_id, proxy, self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_log_session(self, proxy):
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
        if not self.supports_log_entry_log():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryLogSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_entry_log_assignment_session(self, proxy):
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
        if not self.supports_log_entry_log_assignment():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogEntryLogAssignmentSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogLookupSession) - a ``LogLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_lookup()`` is ``true``.*

        """
        if not self.supports_log_lookup():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogLookupSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log administrative service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.logging.LogAdminSession) - a ``LogAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_log_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_log_admin()`` is ``true``.*

        """
        if not self.supports_log_admin():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogAdminSession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_hierarchy_session(self, proxy):
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
        if not self.supports_log_hierarchy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogHierarchySession(proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_log_hierarchy_design_session(self, proxy):
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
        if not self.supports_log_hierarchy_design():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.LogHierarchyDesignSession(proxy=proxy, runtime=self._runtime)

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
        raise errors.Unimplemented()

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)
