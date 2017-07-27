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
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_logging()

    def supports_log_entry_lookup(self):
        """Pass through to provider supports_log_entry_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_log_entry_lookup()

    def supports_log_entry_query(self):
        """Pass through to provider supports_log_entry_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_log_entry_query()

    def supports_log_lookup(self):
        """Pass through to provider supports_log_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_log_lookup()

    def supports_log_admin(self):
        """Pass through to provider supports_log_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_log_admin()

    def supports_log_hierarchy(self):
        """Pass through to provider supports_log_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_log_hierarchy()

    def supports_log_hierarchy_design(self):
        """Pass through to provider supports_log_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_log_hierarchy_design()

    def get_log_entry_record_types(self):
        """Pass through to provider get_log_entry_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_log_entry_record_types()

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def get_log_entry_search_record_types(self):
        """Pass through to provider get_log_entry_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_log_entry_search_record_types()

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def get_log_record_types(self):
        """Pass through to provider get_log_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_log_record_types()

    log_record_types = property(fget=get_log_record_types)

    def get_log_search_record_types(self):
        """Pass through to provider get_log_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_log_search_record_types()

    log_search_record_types = property(fget=get_log_search_record_types)

    def get_priority_types(self):
        """Pass through to provider get_priority_types"""
        # Built from: templates/osid_managers.GenericProfile.get_type_list
        return self._provider_manager.get_priority_types()

    priority_types = property(fget=get_priority_types)

    def get_content_types(self):
        """Pass through to provider get_content_types"""
        # Built from: templates/osid_managers.GenericProfile.get_type_list
        return self._provider_manager.get_content_types()

    content_types = property(fget=get_content_types)

    def supports_log_entry_admin(self):
        """Pass through to provider supports_log_entry_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
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
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_logging_session(*args, **kwargs)

    logging_session = property(fget=get_logging_session)

    def get_logging_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_logging_session_for_log"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_logging_session_for_log(*args, **kwargs)

    def get_log_entry_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_log_entry_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_entry_lookup_session(*args, **kwargs)

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    def get_log_entry_lookup_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_log_entry_lookup_session_for_log"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_log_entry_lookup_session_for_log(*args, **kwargs)

    def get_log_entry_query_session(self, *args, **kwargs):
        """Pass through to provider get_log_entry_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_entry_query_session(*args, **kwargs)

    log_entry_query_session = property(fget=get_log_entry_query_session)

    def get_log_entry_query_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_log_entry_query_session_for_log"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_log_entry_query_session_for_log(*args, **kwargs)

    def get_log_entry_admin_session(self, *args, **kwargs):
        """Pass through to provider get_log_entry_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_entry_admin_session(*args, **kwargs)

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    def get_log_entry_admin_session_for_log(self, *args, **kwargs):
        """Pass through to provider get_log_entry_admin_session_for_log"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_log_entry_admin_session_for_log(*args, **kwargs)

    def get_log_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_log_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_lookup_session(*args, **kwargs)

    log_lookup_session = property(fget=get_log_lookup_session)

    def get_log_admin_session(self, *args, **kwargs):
        """Pass through to provider get_log_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_admin_session(*args, **kwargs)

    log_admin_session = property(fget=get_log_admin_session)

    def get_log_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_log_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_hierarchy_session(*args, **kwargs)

    log_hierarchy_session = property(fget=get_log_hierarchy_session)

    def get_log_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_log_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_log_hierarchy_design_session(*args, **kwargs)

    log_hierarchy_design_session = property(fget=get_log_hierarchy_design_session)

    def get_logging_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    logging_batch_manager = property(fget=get_logging_batch_manager)
##
# The following methods are from osid.logging.LoggingSession

    def get_log_id(self):
        """Pass through to provider LoggingSession.get_log_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('logging_session').get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Pass through to provider LoggingSession.get_log"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return Log(
            self._provider_manager,
            self._get_provider_session('logging_session').get_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    log = property(fget=get_log)

    def can_log(self):
        """Pass through to provider LoggingSession.can_log"""
        # Not templated -- check the hand-built implementations
        self._get_provider_session('logging_session').can_log()

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
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('log_lookup_session').can_lookup_logs()

    def use_comparative_log_view(self):
        """Pass through to provider LogLookupSession.use_comparative_log_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._log_view = COMPARATIVE
        # self._get_provider_session('log_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_log_view()
            except AttributeError:
                pass

    def use_plenary_log_view(self):
        """Pass through to provider LogLookupSession.use_plenary_log_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._log_view = PLENARY
        # self._get_provider_session('log_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_log_view()
            except AttributeError:
                pass

    def get_log(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_log"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return Log(
            self._provider_manager,
            self._get_provider_session('log_lookup_session').get_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_logs_by_ids(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_genus_type(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_record_type(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs_by_provider(self, *args, **kwargs):
        """Pass through to provider LogLookupSession.get_logs_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('log_lookup_session').get_logs_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Log(self._provider_manager, cat, self._runtime, self._proxy))
        return LogList(cat_list)

    def get_logs(self):
        """Pass through to provider LogLookupSession.get_logs"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
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
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('log_admin_session').can_create_logs()

    def can_create_log_with_record_types(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.can_create_log_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('log_admin_session').can_create_log_with_record_types(*args, **kwargs)

    def get_log_form_for_create(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.get_log_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('log_admin_session').get_log_form_for_create(*args, **kwargs)

    def create_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.create_log"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return Log(
            self._provider_manager,
            self._get_provider_session('log_admin_session').create_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_logs(self):
        """Pass through to provider LogAdminSession.can_update_logs"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('log_admin_session').can_update_logs()

    def get_log_form_for_update(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.get_log_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('log_admin_session').get_log_form_for_update(*args, **kwargs)

    def update_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.update_log"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return Log(
            self._provider_manager,
            self._get_provider_session('log_admin_session').update_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_logs(self):
        """Pass through to provider LogAdminSession.can_delete_logs"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('log_admin_session').can_delete_logs()

    def delete_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.delete_log"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.delete_catalog
        self._get_provider_session('log_admin_session').delete_log(*args, **kwargs)

    def can_manage_log_aliases(self):
        """Pass through to provider LogAdminSession.can_manage_log_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('log_admin_session').can_manage_log_aliases()

    def alias_log(self, *args, **kwargs):
        """Pass through to provider LogAdminSession.alias_log"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('log_admin_session').alias_log(*args, **kwargs)
##
# The following methods are from osid.logging.LogHierarchySession

    def get_log_hierarchy_id(self):
        """Pass through to provider LogHierarchySession.get_log_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('log_hierarchy_session').get_log_hierarchy_id()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        """Pass through to provider LogHierarchySession.get_log_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('log_hierarchy_session').get_log_hierarchy()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_access_log_hierarchy(self):
        """Pass through to provider LogHierarchySession.can_access_log_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('log_hierarchy_session').can_access_log_hierarchy()

    def get_root_log_ids(self):
        """Pass through to provider LogHierarchySession.get_root_log_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('log_hierarchy_session').get_root_log_ids()

    root_log_ids = property(fget=get_root_log_ids)

    def get_root_logs(self):
        """Pass through to provider LogHierarchySession.get_root_logs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('log_hierarchy_session').get_root_logs()

    root_logs = property(fget=get_root_logs)

    def has_parent_logs(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.has_parent_logs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('log_hierarchy_session').has_parent_logs(*args, **kwargs)

    def is_parent_of_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.is_parent_of_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('log_hierarchy_session').is_parent_of_log(*args, **kwargs)

    def get_parent_log_ids(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.get_parent_log_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('log_hierarchy_session').get_parent_log_ids(*args, **kwargs)

    def get_parent_logs(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.get_parent_logs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('log_hierarchy_session').get_parent_logs(*args, **kwargs)

    def is_ancestor_of_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.is_ancestor_of_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('log_hierarchy_session').is_ancestor_of_log(*args, **kwargs)

    def has_child_logs(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.has_child_logs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('log_hierarchy_session').has_child_logs(*args, **kwargs)

    def is_child_of_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.is_child_of_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('log_hierarchy_session').is_child_of_log(*args, **kwargs)

    def get_child_log_ids(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.get_child_log_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('log_hierarchy_session').get_child_log_ids(*args, **kwargs)

    def get_child_logs(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.get_child_logs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('log_hierarchy_session').get_child_logs(*args, **kwargs)

    def is_descendant_of_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.is_descendant_of_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('log_hierarchy_session').is_descendant_of_log(*args, **kwargs)

    def get_log_node_ids(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.get_log_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('log_hierarchy_session').get_log_node_ids(*args, **kwargs)

    def get_log_nodes(self, *args, **kwargs):
        """Pass through to provider LogHierarchySession.get_log_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('log_hierarchy_session').get_log_nodes(*args, **kwargs)
##
# The following methods are from osid.logging.LogHierarchyDesignSession

    def can_modify_log_hierarchy(self):
        """Pass through to provider LogHierarchyDesignSession.can_modify_log_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('log_hierarchy_design_session').can_modify_log_hierarchy()

    def add_root_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchyDesignSession.add_root_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('log_hierarchy_design_session').add_root_log(*args, **kwargs)

    def remove_root_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchyDesignSession.remove_root_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('log_hierarchy_design_session').remove_root_log(*args, **kwargs)

    def add_child_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchyDesignSession.add_child_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('log_hierarchy_design_session').add_child_log(*args, **kwargs)

    def remove_child_log(self, *args, **kwargs):
        """Pass through to provider LogHierarchyDesignSession.remove_child_log"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('log_hierarchy_design_session').remove_child_log(*args, **kwargs)

    def remove_child_logs(self, *args, **kwargs):
        """Pass through to provider LogHierarchyDesignSession.remove_child_logs"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('log_hierarchy_design_session').remove_child_logs(*args, **kwargs)


class LoggingProxyManager(osid.OsidProxyManager, LoggingProfile, LoggingManager, logging_managers.LoggingProxyManager):
    """LoggingProxyManager convenience adapter including related Session methods."""
    pass


class Log(abc_logging_objects.Log, osid.OsidSession, osid.OsidCatalog):
    """Log convenience adapter including related Session methods."""
    # Built from: templates/osid_catalog.GenericCatalog.init_template
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
                if 'notification_session' in session_name:
                    # Is there something else we should do about the receiver field?
                    session = session_class('fake receiver', self._catalog.get_id())
                else:
                    session = session_class(self._catalog.get_id())
            else:
                if 'notification_session' in session_name:
                    # Is there something else we should do about the receiver field?
                    session = session_class('fake receiver', self._catalog.get_id(), self._proxy)
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

    def get_log_id(self):
        """Pass through to provider LogEntryLookupSession.get_log_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('log_entry_lookup_session').get_log_id()

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Pass through to provider LogEntryLookupSession.get_log"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return Log(
            self._provider_manager,
            self._get_provider_session('log_entry_lookup_session').get_log(*args, **kwargs),
            self._runtime,
            self._proxy)

    log = property(fget=get_log)

    def can_read_log(self):
        """Pass through to provider LogEntryLookupSession.can_read_log"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('log_entry_lookup_session').can_read_log()

    def use_comparative_log_entry_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider LogEntryLookupSession.use_comparative_log_entry_view"""
        self._object_views['log_entry'] = COMPARATIVE
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_log_entry_view()
            except AttributeError:
                pass

    def use_plenary_log_entry_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider LogEntryLookupSession.use_plenary_log_entry_view"""
        self._object_views['log_entry'] = PLENARY
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_log_entry_view()
            except AttributeError:
                pass

    def use_federated_log_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_federated_catalog_view
        """Pass through to provider LogEntryLookupSession.use_federated_log_view"""
        self._log_view = FEDERATED
        # self._get_provider_session('log_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_log_view()
            except AttributeError:
                pass

    def use_isolated_log_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_isolated_catalog_view
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('log_entry_lookup_session').get_log_entry(*args, **kwargs)

    def get_log_entries_by_ids(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_ids(*args, **kwargs)

    def get_log_entries_by_genus_type(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_genus_type(*args, **kwargs)

    def get_log_entries_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('log_entry_lookup_session').get_log_entries_by_parent_genus_type(*args, **kwargs)

    def get_log_entries_by_record_type(self, *args, **kwargs):
        """Pass through to provider LogEntryLookupSession.get_log_entries_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('log_entry_lookup_session').get_log_entries()

    log_entries = property(fget=get_log_entries)
##
# The following methods are from osid.logging.LogEntryQuerySession

    def can_search_log_entries(self):
        """Pass through to provider LogEntryQuerySession.can_search_log_entries"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('log_entry_query_session').can_search_log_entries()

    def get_log_entry_query(self):
        """Pass through to provider LogEntryQuerySession.get_log_entry_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('log_entry_query_session').get_log_entry_query()

    log_entry_query = property(fget=get_log_entry_query)

    def get_log_entries_by_query(self, *args, **kwargs):
        """Pass through to provider LogEntryQuerySession.get_log_entries_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('log_entry_query_session').get_log_entries_by_query(*args, **kwargs)
##
# The following methods are from osid.logging.LogEntryAdminSession

    def can_create_log_entries(self):
        """Pass through to provider LogEntryAdminSession.can_create_log_entries"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('log_entry_admin_session').can_create_log_entries()

    def can_create_log_entry_with_record_types(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.can_create_log_entry_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('log_entry_admin_session').can_create_log_entry_with_record_types(*args, **kwargs)

    def get_log_entry_form_for_create(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.get_log_entry_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_create
        return self._get_provider_session('log_entry_admin_session').get_log_entry_form_for_create(*args, **kwargs)

    def create_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.create_log_entry"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('log_entry_admin_session').create_log_entry(*args, **kwargs)

    def can_update_log_entries(self):
        """Pass through to provider LogEntryAdminSession.can_update_log_entries"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('log_entry_admin_session').can_update_log_entries()

    def get_log_entry_form_for_update(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.get_log_entry_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('log_entry_admin_session').get_log_entry_form_for_update(*args, **kwargs)

    def update_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.update_log_entry"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('log_entry_admin_session').update_log_entry(*args, **kwargs)

    def can_delete_log_entries(self):
        """Pass through to provider LogEntryAdminSession.can_delete_log_entries"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('log_entry_admin_session').can_delete_log_entries()

    def delete_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.delete_log_entry"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('log_entry_admin_session').delete_log_entry(*args, **kwargs)

    def can_manage_log_entry_aliases(self):
        """Pass through to provider LogEntryAdminSession.can_manage_log_entry_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('log_entry_admin_session').can_manage_log_entry_aliases()

    def alias_log_entry(self, *args, **kwargs):
        """Pass through to provider LogEntryAdminSession.alias_log_entry"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('log_entry_admin_session').alias_log_entry(*args, **kwargs)


class LogList(abc_logging_objects.LogList, osid.OsidList):
    """LogList convenience adapter including related Session methods."""

    def get_next_log(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(Log)

    __next__ = next

    next_log = property(fget=get_next_log)

    def get_next_logs(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(LogList, number=n)
