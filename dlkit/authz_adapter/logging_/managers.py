"""AuthZ Adapter implementations of logging managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from ..osid.osid_errors import Unimplemented, OperationFailed, Unsupported
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.logging_ import managers as logging_managers


class LoggingProfile(osid_managers.OsidProfile, logging_managers.LoggingProfile):
    """Adapts underlying LoggingProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_log_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_log_hierarchy_session()
        except Unimplemented:
            return None

    def supports_logging(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_logging()

    def supports_log_entry_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_lookup()

    def supports_log_entry_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_query()

    def supports_log_entry_log(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_log()

    def supports_log_entry_log_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_log_assignment()

    def supports_log_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_lookup()

    def supports_log_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_admin()

    def supports_log_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_hierarchy()

    def supports_log_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_hierarchy_design()

    def get_log_entry_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_entry_record_types()

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def get_log_entry_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_entry_search_record_types()

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def get_log_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_record_types()

    log_record_types = property(fget=get_log_record_types)

    def get_log_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_search_record_types()

    log_search_record_types = property(fget=get_log_search_record_types)

    def get_priority_types(self):
        # Implemented from azosid template for -
        # osid.logging.LoggingProfile.get_priority_types
        return self._provider_manager.get_priority_types()

    priority_types = property(fget=get_priority_types)

    def get_content_types(self):
        # Implemented from azosid template for -
        # osid.logging.LoggingProfile.get_content_types
        return self._provider_manager.get_content_types()

    content_types = property(fget=get_content_types)

    def supports_log_entry_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_admin()


class LoggingManager(osid_managers.OsidManager, LoggingProfile, logging_managers.LoggingManager):
    """Adapts underlying LoggingManager methodswith authorization checks."""
    def __init__(self):
        LoggingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:loggingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('LOGGING', provider_impl)
        # need to add version argument

    def get_logging_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LoggingSession')(
            provider_session=self._provider_manager.get_logging_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    logging_session = property(fget=get_logging_session)

    @raise_null_argument
    def get_logging_session_for_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        return getattr(sessions, 'LoggingSession')(
            provider_session=self._provider_manager.get_logging_session_for_log(log_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    def get_log_entry_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session()
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryLookupSession')(
            provider_session=self._provider_manager.get_log_entry_lookup_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            hierarchy_session=self._get_hierarchy_session(),
            query_session=query_session)

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    @raise_null_argument
    def get_log_entry_lookup_session_for_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session_for_log(log_id)
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryLookupSession')(
            provider_session=self._provider_manager.get_log_entry_lookup_session_for_log(log_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            hierarchy_session=self._get_hierarchy_session(),
            query_session=query_session)

    def get_log_entry_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session()
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryQuerySession')(
            provider_session=self._provider_manager.get_log_entry_query_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            hierarchy_session=self._get_hierarchy_session(),
            query_session=query_session)

    log_entry_query_session = property(fget=get_log_entry_query_session)

    @raise_null_argument
    def get_log_entry_query_session_for_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session_for_log(log_id)
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryQuerySession')(
            provider_session=self._provider_manager.get_log_entry_query_session_for_log(log_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            hierarchy_session=self._get_hierarchy_session(),
            query_session=query_session)

    def get_log_entry_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogEntryAdminSession')(
            provider_session=self._provider_manager.get_log_entry_admin_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    @raise_null_argument
    def get_log_entry_admin_session_for_log(self, log_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        return getattr(sessions, 'LogEntryAdminSession')(
            provider_session=self._provider_manager.get_log_entry_admin_session_for_log(log_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    def get_log_entry_log_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogEntryLogSession')(
            provider_session=self._provider_manager.get_log_entry_log_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_entry_log_session = property(fget=get_log_entry_log_session)

    def get_log_entry_log_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogEntryLogAssignmentSession')(
            provider_session=self._provider_manager.get_log_entry_log_assignment_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_entry_log_assignment_session = property(fget=get_log_entry_log_assignment_session)

    def get_log_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogLookupSession')(
            provider_session=self._provider_manager.get_log_lookup_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_lookup_session = property(fget=get_log_lookup_session)

    def get_log_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogAdminSession')(
            provider_session=self._provider_manager.get_log_admin_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_admin_session = property(fget=get_log_admin_session)

    def get_log_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogHierarchySession')(
            provider_session=self._provider_manager.get_log_hierarchy_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_hierarchy_session = property(fget=get_log_hierarchy_session)

    def get_log_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogHierarchyDesignSession')(
            provider_session=self._provider_manager.get_log_hierarchy_design_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    log_hierarchy_design_session = property(fget=get_log_hierarchy_design_session)

    def get_logging_batch_manager(self):
        raise Unimplemented()

    logging_batch_manager = property(fget=get_logging_batch_manager)


class LoggingProxyManager(osid_managers.OsidProxyManager, LoggingProfile, logging_managers.LoggingProxyManager):
    """Adapts underlying LoggingProxyManager methodswith authorization checks."""
    def __init__(self):
        LoggingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:loggingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('LOGGING', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_logging_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LoggingSession')(
            provider_session=self._provider_manager.get_logging_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_logging_session_for_log(self, log_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        return getattr(sessions, 'LoggingSession')(
            provider_session=self._provider_manager.get_logging_session_for_log(log_id, proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_entry_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session(proxy)
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryLookupSession')(
            provider_session=self._provider_manager.get_log_entry_lookup_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            proxy=proxy,
            hierarchy_session=self._get_hierarchy_session(proxy),
            query_session=query_session)

    @raise_null_argument
    def get_log_entry_lookup_session_for_log(self, log_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session_for_log(log_id, proxy)
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryLookupSession')(
            provider_session=self._provider_manager.get_log_entry_lookup_session_for_log(log_id, proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            proxy=proxy,
            hierarchy_session=self._get_hierarchy_session(proxy),
            query_session=query_session)

    @raise_null_argument
    def get_log_entry_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session(proxy)
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryQuerySession')(
            provider_session=self._provider_manager.get_log_entry_query_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            proxy=proxy,
            hierarchy_session=self._get_hierarchy_session(proxy),
            query_session=query_session)

    @raise_null_argument
    def get_log_entry_query_session_for_log(self, log_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_log_entry_query_session_for_log(log_id, proxy)
            query_session.use_federated_log_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'LogEntryQuerySession')(
            provider_session=self._provider_manager.get_log_entry_query_session_for_log(log_id, proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            proxy=proxy,
            hierarchy_session=self._get_hierarchy_session(proxy),
            query_session=query_session)

    @raise_null_argument
    def get_log_entry_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogEntryAdminSession')(
            provider_session=self._provider_manager.get_log_entry_admin_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_entry_admin_session_for_log(self, log_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        return getattr(sessions, 'LogEntryAdminSession')(
            provider_session=self._provider_manager.get_log_entry_admin_session_for_log(log_id, proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_entry_log_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogEntryLogSession')(
            provider_session=self._provider_manager.get_log_entry_log_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_entry_log_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogEntryLogAssignmentSession')(
            provider_session=self._provider_manager.get_log_entry_log_assignment_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogLookupSession')(
            provider_session=self._provider_manager.get_log_lookup_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogAdminSession')(
            provider_session=self._provider_manager.get_log_admin_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogHierarchySession')(
            provider_session=self._provider_manager.get_log_hierarchy_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_log_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'LogHierarchyDesignSession')(
            provider_session=self._provider_manager.get_log_hierarchy_design_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    def get_logging_batch_proxy_manager(self):
        raise Unimplemented()

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)
