"""DLKit Services implementations of logging service."""
# pylint: disable=no-init
#     osid specification includes some 'marker' interfaces.
# pylint: disable=too-many-ancestors
#     number of ancestors defined in spec.
# pylint: disable=too-few-public-methods,too-many-public-methods
#     number of methods defined in spec. Worse yet, these are aggregates.
# pylint: disable=invalid-name
#     method and class names defined in spec.
# pylint: disable=no-self-use,unused-argument
#     to catch unimplemented methods.
# pylint: disable=super-init-not-called
#     it just isn't.


from . import osid
from .osid_errors import Unimplemented, IllegalState, InvalidArgument
from dlkit.abstract_osid.logging_ import objects as abc_logging_objects
from dlkit.manager_impls.logging_ import managers as logging_managers


DEFAULT = 0
COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
ANY_STATUS = 0
ACTIVE = 1
UNSEQUESTERED = 0
SEQUESTERED = 1
AUTOMATIC = 0
MANDATORY = 1
DISABLED = -1


class LoggingProfile(osid.OsidProfile, logging_managers.LoggingProfile):
    """LoggingProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_logging(self):
        """Pass through to provider supports_logging"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_logging()

    def supports_log_entry_lookup(self):
        """Pass through to provider supports_log_entry_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_lookup()

    def supports_log_entry_query(self):
        """Pass through to provider supports_log_entry_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_query()

    def supports_log_lookup(self):
        """Pass through to provider supports_log_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_lookup()

    def supports_log_admin(self):
        """Pass through to provider supports_log_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_admin()

    def get_log_entry_record_types(self):
        """Pass through to provider get_log_entry_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_entry_record_types()

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def get_log_entry_search_record_types(self):
        """Pass through to provider get_log_entry_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_entry_search_record_types()

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def get_log_record_types(self):
        """Pass through to provider get_log_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_record_types()

    log_record_types = property(fget=get_log_record_types)

    def get_log_search_record_types(self):
        """Pass through to provider get_log_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_log_search_record_types()

    log_search_record_types = property(fget=get_log_search_record_types)

    def get_priority_types(self):
        """Pass through to provider get_priority_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_priority_types()

    priority_types = property(fget=get_priority_types)

    def get_content_types(self):
        """Pass through to provider get_content_types"""
        # Implemented from kitosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_content_types()

    content_types = property(fget=get_content_types)

    def supports_log_entry_admin(self):
        """Pass through to provider supports_log_entry_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_log_entry_admin()


class LoggingManager(osid.OsidManager, osid.OsidSession, LoggingProfile, logging_managers.LoggingManager):
    """LoggingManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._log_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_log_view(self, session):
        """Sets the underlying log view to match current view"""
        if self._log_view == COMPARATIVE:
            try:
                session.use_comparative_log_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_log_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_log_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:loggingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('LOGGING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('LOGGING', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

    def get_logging_session(self, *args, **kwargs):
        """Pass through to provider get_logging_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_logging_session(*args, **kwargs)

    logging_session = property(fget=get_logging_session)

    def get_logging_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_logging_session_for_log"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_manager_template
        return self._provider_manager.get_logging_session_for_log(*args, **kwargs)

    def get_log_entry_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_log_entry_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_log_entry_lookup_session(*args, **kwargs)

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    def get_log_entry_lookup_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_log_entry_lookup_session_for_log"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_log_entry_lookup_session_for_log(*args, **kwargs)

    def get_log_entry_query_session(self, *args, **kwargs):
        """Pass through to provider get_log_entry_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_log_entry_query_session(*args, **kwargs)

    log_entry_query_session = property(fget=get_log_entry_query_session)

    def get_log_entry_query_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_log_entry_query_session_for_log"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_log_entry_query_session_for_log(*args, **kwargs)

    def get_log_entry_admin_session(self, *args, **kwargs):
        """Pass through to provider get_log_entry_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_log_entry_admin_session(*args, **kwargs)

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    def get_log_entry_admin_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_log_entry_admin_session_for_log"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_log_entry_admin_session_for_log(*args, **kwargs)

    def get_log_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_log_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_log_lookup_session(*args, **kwargs)

    log_lookup_session = property(fget=get_log_lookup_session)

    def get_log_admin_session(self, *args, **kwargs):
        """Pass through to provider get_log_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_log_admin_session(*args, **kwargs)

    log_admin_session = property(fget=get_log_admin_session)

    def get_logging_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    logging_batch_manager = property(fget=get_logging_batch_manager)
##
# The following methods are from osid.logging.LoggingSession

    def get_log_id(self):
        return self._get_provider_session('logging_session').get_log_id()

    log_id = property(fget=get_log_id)

    def can_log(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def log(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def log_at_priority(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_form(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    log_entry_form = property(fget=get_log_entry_form)

    def create_log_entry(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.logging.LogLookupSession

    def can_lookup_logs(self):
        """Pass through to provider LogLookupSession.can_lookup_logs"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('log_lookup_session').can_lookup_logs()

    def use_comparative_log_view(self):
        """Pass through to provider LogLookupSession.use_comparative_log_view"""
        self._log_view = COMPARATIVE
        # self._get_provider_session('log_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_log_view()
            except AttributeError:
                pass

    def use_plenary_log_view(self):
        """Pass through to provider LogLookupSession.use_plenary_log_view"""
        self._log_view = PLENARY
        # self._get_provider_session('log_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_log_view()
            except AttributeError:
                pass

    def get_log(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return Log(
            self._provider_manager,
            self._get_provider_session('log_lookup_session').get_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_logs_by_ids(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_genus_type(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_record_type(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_provider(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs(self):
        """Pass through to provider LogLookupSession.get_logs"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('log_lookup_session').get_logs()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    logs = property(fget=get_logs)
##
# The following methods are from osid.logging.LogAdminSession

    def can_create_logs(self):
        """Pass through to provider LogAdminSession.can_create_logs"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('log_admin_session').can_create_logs()

    def can_create_log_with_record_types(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.can_create_log_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('log_admin_session').can_create_log_with_record_types(*args, **kwargs)

    def get_log_form_for_create(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.get_log_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('log_admin_session').get_log_form_for_create(*args, **kwargs)

    def create_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.create_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return Log(
            self._provider_manager,
            self._get_provider_session('log_admin_session').create_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_logs(self):
        """Pass through to provider LogAdminSession.can_update_logs"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('log_admin_session').can_update_logs()

    def get_log_form_for_update(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.get_log_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('log_admin_session').get_log_form_for_update(*args, **kwargs)

    def get_log_form(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.get_log_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'log_record_types' in kwargs:
            return self.get_log_form_for_create(*args, **kwargs)
        else:
            return self.get_log_form_for_update(*args, **kwargs)

    def update_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.update_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return Log(
            self._provider_manager,
            self._get_provider_session('log_admin_session').update_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    def save_log(self, log_form, *args, **kwargs):
        """Pass through to provider LogAdminSession.update_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if log_form.is_for_update():
            return self.update_log(log_form, *args, **kwargs)
        else:
            return self.create_log(log_form, *args, **kwargs)

    def can_delete_logs(self):
        """Pass through to provider LogAdminSession.can_delete_logs"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('log_admin_session').can_delete_logs()

    def delete_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.delete_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('log_admin_session').delete_log(*args, **kwargs)

    def can_manage_log_aliases(self):
        """Pass through to provider LogAdminSession.can_manage_log_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('log_admin_session').can_manage_log_aliases()

    def alias_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.alias_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.alias_bin
        self._get_provider_session('log_admin_session').alias_log(*args, **kwargs)


class LoggingProxyManager(osid.OsidProxyManager, LoggingProfile, logging_managers.LoggingProxyManager):
    """LoggingProxyManager convenience adapter including related Session methods."""

    def get_logging_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_logging_session_for_log(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_lookup_session_for_log(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_query_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_query_session_for_log(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entry_admin_session_for_log(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_logging_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)


class Log(abc_logging_objects.Log, osid.OsidSession, osid.OsidCatalog):
    """Log convenience adapter including related Session methods."""
    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, runtime, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        self._runtime = runtime
        osid.OsidObject.__init__(self, self._catalog)  # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy)  # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._log_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_log_view(self, session):
        """Sets the underlying log view to match current view"""
        if self._log_view == FEDERATED:
            try:
                session.use_federated_log_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_log_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_operable_view(self, session):
        """Sets the underlying operable views to match current view"""
        for obj_name in self._operable_views:
            if self._operable_views[obj_name] == ACTIVE:
                try:
                    getattr(session, 'use_active_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_any_status_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_containable_view(self, session):
        """Sets the underlying containable views to match current view"""
        for obj_name in self._containable_views:
            if self._containable_views[obj_name] == SEQUESTERED:
                try:
                    getattr(session, 'use_sequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_unsequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session.

        Instantiates a new one if the named session is not already known.

        """
        agent_key = self._get_agent_key()
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_log')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_log_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_log_id(self):
        """Gets the Id of this log."""
        return self._catalog_id

    def get_log(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        else:
            raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

    def get_log_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.logging.LogEntryLookupSession

    def can_read_log(self):
        """Pass through to provider LogEntryLookupSession.can_read_log"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('log_entry_lookup_session').can_read_log()

    def use_comparative_log_entry_view(self):
        """Pass through to provider LogEntryLookupSession.use_comparative_log_entry_view"""
        self._object_views['log_entry'] = COMPARATIVE
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_log_entry_view()
            except AttributeError:
                pass

    def use_plenary_log_entry_view(self):
        """Pass through to provider LogEntryLookupSession.use_plenary_log_entry_view"""
        self._object_views['log_entry'] = PLENARY
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_log_entry_view()
            except AttributeError:
                pass

    def use_federated_log_view(self):
        """Pass through to provider LogEntryLookupSession.use_federated_log_view"""
        self._log_view = FEDERATED
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_log_view()
            except AttributeError:
                pass

    def use_isolated_log_view(self):
        """Pass through to provider LogEntryLookupSession.use_isolated_log_view"""
        self._log_view = ISOLATED
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_log_view()
            except AttributeError:
                pass

    def get_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('log_entry_lookup_session').get_log_entry(*args, **kwargs)

    def get_log_entries_by_ids(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_ids(*args, **kwargs)

    def get_log_entries_by_genus_type(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_genus_type(*args, **kwargs)

    def get_log_entries_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_parent_genus_type(*args, **kwargs)

    def get_log_entries_by_record_type(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_record_type(*args, **kwargs)

    def get_log_entries_by_priority_type(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entries_by_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entries_by_priority_type_and_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entries_for_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entries_by_date_for_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entries_by_priority_type_and_date_for_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_log_entries(self):
        """Pass through to provider LogEntryLookupSession.get_log_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('log_entry_lookup_session').get_log_entries()

    log_entries = property(fget=get_log_entries)
##
# The following methods are from osid.logging.LogEntryQuerySession

    def can_search_log_entries(self):
        """Pass through to provider LogEntryQuerySession.can_search_log_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('log_entry_query_session').can_search_log_entries()

    def get_log_entry_query(self):
        """Pass through to provider LogEntryQuerySession.get_log_entry_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('log_entry_query_session').get_log_entry_query()

    log_entry_query = property(fget=get_log_entry_query)

    def get_log_entries_by_query(self, *args, **kwargs):
        """Pass through to provider LogEntryQuerySession.get_log_entries_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('log_entry_query_session').get_log_entries_by_query(*args, **kwargs)
##
# The following methods are from osid.logging.LogEntryAdminSession

    def can_create_log_entries(self):
        """Pass through to provider LogEntryAdminSession.can_create_log_entries"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('log_entry_admin_session').can_create_log_entries()

    def can_create_log_entry_with_record_types(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.can_create_log_entry_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('log_entry_admin_session').can_create_log_entry_with_record_types(*args, **kwargs)

    def get_log_entry_form_for_create(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.get_log_entry_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('log_entry_admin_session').get_log_entry_form_for_create(*args, **kwargs)

    def create_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.create_log_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('log_entry_admin_session').create_log_entry(*args, **kwargs)

    def can_update_log_entries(self):
        """Pass through to provider LogEntryAdminSession.can_update_log_entries"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('log_entry_admin_session').can_update_log_entries()

    def get_log_entry_form_for_update(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.get_log_entry_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('log_entry_admin_session').get_log_entry_form_for_update(*args, **kwargs)

    def get_log_entry_form(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.get_log_entry_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'log_entry_record_types' in kwargs:
            return self.get_log_entry_form_for_create(*args, **kwargs)
        else:
            return self.get_log_entry_form_for_update(*args, **kwargs)

    def duplicate_log_entry(self, log_entry_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('log_entry_admin_session').duplicate_log_entry(log_entry_id)

    def update_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.update_log_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('log_entry_admin_session').update_log_entry(*args, **kwargs)

    def save_log_entry(self, log_entry_form, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.update_log_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if log_entry_form.is_for_update():
            return self.update_log_entry(log_entry_form, *args, **kwargs)
        else:
            return self.create_log_entry(log_entry_form, *args, **kwargs)

    def can_delete_log_entries(self):
        """Pass through to provider LogEntryAdminSession.can_delete_log_entries"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('log_entry_admin_session').can_delete_log_entries()

    def delete_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.delete_log_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('log_entry_admin_session').delete_log_entry(*args, **kwargs)

    def can_manage_log_entry_aliases(self):
        """Pass through to provider LogEntryAdminSession.can_manage_log_entry_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('log_entry_admin_session').can_manage_log_entry_aliases()

    def alias_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.alias_log_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('log_entry_admin_session').alias_log_entry(*args, **kwargs)


class LogList(abc_logging_objects.LogList, osid.OsidList):
    """LogList convenience adapter including related Session methods."""

    def get_next_log(self):
        """Gets next object"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        try:
            next_item = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        else:
            return next_item

    def next(self):
        """next method for enumerator"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        next_item = osid.OsidList.next(self)
        return next_item

    __next__ = next

    next_log = property(fget=get_next_log)

    def get_next_logs(self, n):
        """gets next n objects from list"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            i = 0
            while i < n:
                try:
                    next_list.append(next(self))
                except StopIteration:
                    break
                i += 1
            return next_list
