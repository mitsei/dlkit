"""DLKit Services implementations of grading service."""
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
from dlkit.abstract_osid.grading import objects as abc_grading_objects
from dlkit.manager_impls.grading import managers as grading_managers


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


class GradingProfile(osid.OsidProfile, grading_managers.GradingProfile):
    """GradingProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_grade_system_lookup(self):
        """Pass through to provider supports_grade_system_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_system_lookup()

    def supports_grade_system_query(self):
        """Pass through to provider supports_grade_system_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_system_query()

    def supports_grade_system_admin(self):
        """Pass through to provider supports_grade_system_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_system_admin()

    def supports_grade_entry_lookup(self):
        """Pass through to provider supports_grade_entry_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_entry_lookup()

    def supports_grade_entry_query(self):
        """Pass through to provider supports_grade_entry_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_entry_query()

    def supports_grade_entry_admin(self):
        """Pass through to provider supports_grade_entry_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_grade_entry_admin()

    def supports_gradebook_column_lookup(self):
        """Pass through to provider supports_gradebook_column_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_column_lookup()

    def supports_gradebook_column_query(self):
        """Pass through to provider supports_gradebook_column_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_column_query()

    def supports_gradebook_column_admin(self):
        """Pass through to provider supports_gradebook_column_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_column_admin()

    def supports_gradebook_lookup(self):
        """Pass through to provider supports_gradebook_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_lookup()

    def supports_gradebook_admin(self):
        """Pass through to provider supports_gradebook_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_gradebook_admin()

    def get_grade_record_types(self):
        """Pass through to provider get_grade_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_record_types()

    grade_record_types = property(fget=get_grade_record_types)

    def get_grade_system_record_types(self):
        """Pass through to provider get_grade_system_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_system_record_types()

    grade_system_record_types = property(fget=get_grade_system_record_types)

    def get_grade_system_search_record_types(self):
        """Pass through to provider get_grade_system_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_system_search_record_types()

    grade_system_search_record_types = property(fget=get_grade_system_search_record_types)

    def get_grade_entry_record_types(self):
        """Pass through to provider get_grade_entry_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_entry_record_types()

    grade_entry_record_types = property(fget=get_grade_entry_record_types)

    def get_grade_entry_search_record_types(self):
        """Pass through to provider get_grade_entry_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_grade_entry_search_record_types()

    grade_entry_search_record_types = property(fget=get_grade_entry_search_record_types)

    def get_gradebook_column_record_types(self):
        """Pass through to provider get_gradebook_column_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_column_record_types()

    gradebook_column_record_types = property(fget=get_gradebook_column_record_types)

    def get_gradebook_column_search_record_types(self):
        """Pass through to provider get_gradebook_column_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_column_search_record_types()

    gradebook_column_search_record_types = property(fget=get_gradebook_column_search_record_types)

    def get_gradebook_column_summary_record_types(self):
        """Pass through to provider get_gradebook_column_summary_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_column_summary_record_types()

    gradebook_column_summary_record_types = property(fget=get_gradebook_column_summary_record_types)

    def get_gradebook_record_types(self):
        """Pass through to provider get_gradebook_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_record_types()

    gradebook_record_types = property(fget=get_gradebook_record_types)

    def get_gradebook_search_record_types(self):
        """Pass through to provider get_gradebook_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_gradebook_search_record_types()

    gradebook_search_record_types = property(fget=get_gradebook_search_record_types)


class GradingManager(osid.OsidManager, osid.OsidSession, GradingProfile, grading_managers.GradingManager):
    """GradingManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._gradebook_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_gradebook_view(self, session):
        """Sets the underlying gradebook view to match current view"""
        if self._gradebook_view == COMPARATIVE:
            try:
                session.use_comparative_gradebook_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_gradebook_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_gradebook_view(session)
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
        parameter_id = Id('parameter:gradingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('GRADING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('GRADING', provider_impl)

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

    def get_grade_system_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_grade_system_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_grade_system_lookup_session(*args, **kwargs)

    grade_system_lookup_session = property(fget=get_grade_system_lookup_session)

    def get_grade_system_lookup_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_grade_system_lookup_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_grade_system_lookup_session_for_gradebook(*args, **kwargs)

    def get_grade_system_query_session(self, *args, **kwargs):
        """Pass through to provider get_grade_system_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_grade_system_query_session(*args, **kwargs)

    grade_system_query_session = property(fget=get_grade_system_query_session)

    def get_grade_system_query_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_grade_system_query_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_grade_system_query_session_for_gradebook(*args, **kwargs)

    def get_grade_system_admin_session(self, *args, **kwargs):
        """Pass through to provider get_grade_system_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_grade_system_admin_session(*args, **kwargs)

    grade_system_admin_session = property(fget=get_grade_system_admin_session)

    def get_grade_system_admin_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_grade_system_admin_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_grade_system_admin_session_for_gradebook(*args, **kwargs)

    def get_grade_entry_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_grade_entry_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_grade_entry_lookup_session(*args, **kwargs)

    grade_entry_lookup_session = property(fget=get_grade_entry_lookup_session)

    def get_grade_entry_lookup_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_grade_entry_lookup_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_grade_entry_lookup_session_for_gradebook(*args, **kwargs)

    def get_grade_entry_query_session(self, *args, **kwargs):
        """Pass through to provider get_grade_entry_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_grade_entry_query_session(*args, **kwargs)

    grade_entry_query_session = property(fget=get_grade_entry_query_session)

    def get_grade_entry_query_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_grade_entry_query_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_grade_entry_query_session_for_gradebook(*args, **kwargs)

    def get_grade_entry_admin_session(self, *args, **kwargs):
        """Pass through to provider get_grade_entry_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_grade_entry_admin_session(*args, **kwargs)

    grade_entry_admin_session = property(fget=get_grade_entry_admin_session)

    def get_grade_entry_admin_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_grade_entry_admin_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_grade_entry_admin_session_for_gradebook(*args, **kwargs)

    def get_gradebook_column_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_gradebook_column_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_gradebook_column_lookup_session(*args, **kwargs)

    gradebook_column_lookup_session = property(fget=get_gradebook_column_lookup_session)

    def get_gradebook_column_lookup_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_gradebook_column_lookup_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_gradebook_column_lookup_session_for_gradebook(*args, **kwargs)

    def get_gradebook_column_query_session(self, *args, **kwargs):
        """Pass through to provider get_gradebook_column_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_gradebook_column_query_session(*args, **kwargs)

    gradebook_column_query_session = property(fget=get_gradebook_column_query_session)

    def get_gradebook_column_query_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_gradebook_column_query_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_gradebook_column_query_session_for_gradebook(*args, **kwargs)

    def get_gradebook_column_admin_session(self, *args, **kwargs):
        """Pass through to provider get_gradebook_column_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_gradebook_column_admin_session(*args, **kwargs)

    gradebook_column_admin_session = property(fget=get_gradebook_column_admin_session)

    def get_gradebook_column_admin_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider get_gradebook_column_admin_session_for_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_gradebook_column_admin_session_for_gradebook(*args, **kwargs)

    def get_gradebook_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_gradebook_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_gradebook_lookup_session(*args, **kwargs)

    gradebook_lookup_session = property(fget=get_gradebook_lookup_session)

    def get_gradebook_admin_session(self, *args, **kwargs):
        """Pass through to provider get_gradebook_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_gradebook_admin_session(*args, **kwargs)

    gradebook_admin_session = property(fget=get_gradebook_admin_session)

    def get_grading_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    grading_batch_manager = property(fget=get_grading_batch_manager)

    def get_grading_calculation_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    grading_calculation_manager = property(fget=get_grading_calculation_manager)

    def get_grading_transform_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    grading_transform_manager = property(fget=get_grading_transform_manager)
##
# The following methods are from osid.grading.GradebookLookupSession

    def can_lookup_gradebooks(self):
        """Pass through to provider GradebookLookupSession.can_lookup_gradebooks"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('gradebook_lookup_session').can_lookup_gradebooks()

    def use_comparative_gradebook_view(self):
        """Pass through to provider GradebookLookupSession.use_comparative_gradebook_view"""
        self._gradebook_view = COMPARATIVE
        # self._get_provider_session('gradebook_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_gradebook_view()
            except AttributeError:
                pass

    def use_plenary_gradebook_view(self):
        """Pass through to provider GradebookLookupSession.use_plenary_gradebook_view"""
        self._gradebook_view = PLENARY
        # self._get_provider_session('gradebook_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_gradebook_view()
            except AttributeError:
                pass

    def get_gradebook(self, *args, **kwargs):
        """Pass through to provider GradebookLookupSession.get_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return Gradebook(
            self._provider_manager,
            self._get_provider_session('gradebook_lookup_session').get_gradebook(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_gradebooks_by_ids(self, *args, **kwargs):
        """Pass through to provider GradebookLookupSession.get_gradebooks_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('gradebook_lookup_session').get_gradebooks_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Gradebook(self._provider_manager, cat, self._runtime, self._proxy))
        return GradebookList(cat_list)

    def get_gradebooks_by_genus_type(self, *args, **kwargs):
        """Pass through to provider GradebookLookupSession.get_gradebooks_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('gradebook_lookup_session').get_gradebooks_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Gradebook(self._provider_manager, cat, self._runtime, self._proxy))
        return GradebookList(cat_list)

    def get_gradebooks_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider GradebookLookupSession.get_gradebooks_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('gradebook_lookup_session').get_gradebooks_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Gradebook(self._provider_manager, cat, self._runtime, self._proxy))
        return GradebookList(cat_list)

    def get_gradebooks_by_record_type(self, *args, **kwargs):
        """Pass through to provider GradebookLookupSession.get_gradebooks_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('gradebook_lookup_session').get_gradebooks_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Gradebook(self._provider_manager, cat, self._runtime, self._proxy))
        return GradebookList(cat_list)

    def get_gradebooks_by_provider(self, *args, **kwargs):
        """Pass through to provider GradebookLookupSession.get_gradebooks_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('gradebook_lookup_session').get_gradebooks_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Gradebook(self._provider_manager, cat, self._runtime, self._proxy))
        return GradebookList(cat_list)

    def get_gradebooks(self):
        """Pass through to provider GradebookLookupSession.get_gradebooks"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('gradebook_lookup_session').get_gradebooks()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Gradebook(self._provider_manager, cat, self._runtime, self._proxy))
        return GradebookList(cat_list)

    gradebooks = property(fget=get_gradebooks)
##
# The following methods are from osid.grading.GradebookAdminSession

    def can_create_gradebooks(self):
        """Pass through to provider GradebookAdminSession.can_create_gradebooks"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('gradebook_admin_session').can_create_gradebooks()

    def can_create_gradebook_with_record_types(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.can_create_gradebook_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('gradebook_admin_session').can_create_gradebook_with_record_types(*args, **kwargs)

    def get_gradebook_form_for_create(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.get_gradebook_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('gradebook_admin_session').get_gradebook_form_for_create(*args, **kwargs)

    def create_gradebook(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.create_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return Gradebook(
            self._provider_manager,
            self._get_provider_session('gradebook_admin_session').create_gradebook(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_gradebooks(self):
        """Pass through to provider GradebookAdminSession.can_update_gradebooks"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('gradebook_admin_session').can_update_gradebooks()

    def get_gradebook_form_for_update(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.get_gradebook_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('gradebook_admin_session').get_gradebook_form_for_update(*args, **kwargs)

    def get_gradebook_form(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.get_gradebook_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'gradebook_record_types' in kwargs:
            return self.get_gradebook_form_for_create(*args, **kwargs)
        else:
            return self.get_gradebook_form_for_update(*args, **kwargs)

    def update_gradebook(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.update_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return Gradebook(
            self._provider_manager,
            self._get_provider_session('gradebook_admin_session').update_gradebook(*args, **kwargs),
            self._runtime,
            self._proxy)

    def save_gradebook(self, gradebook_form, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.update_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if gradebook_form.is_for_update():
            return self.update_gradebook(gradebook_form, *args, **kwargs)
        else:
            return self.create_gradebook(gradebook_form, *args, **kwargs)

    def can_delete_gradebooks(self):
        """Pass through to provider GradebookAdminSession.can_delete_gradebooks"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('gradebook_admin_session').can_delete_gradebooks()

    def delete_gradebook(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.delete_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('gradebook_admin_session').delete_gradebook(*args, **kwargs)

    def can_manage_gradebook_aliases(self):
        """Pass through to provider GradebookAdminSession.can_manage_gradebook_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('gradebook_admin_session').can_manage_gradebook_aliases()

    def alias_gradebook(self, *args, **kwargs):
        """Pass through to provider GradebookAdminSession.alias_gradebook"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.alias_bin
        self._get_provider_session('gradebook_admin_session').alias_gradebook(*args, **kwargs)


class GradingProxyManager(osid.OsidProxyManager, GradingProfile, grading_managers.GradingProxyManager):
    """GradingProxyManager convenience adapter including related Session methods."""

    def get_grade_system_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return GradingManager.get_grade_system_lookup_session(*args, **kwargs)

    def get_grade_system_lookup_session_for_gradebook(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return GradingManager.get_grade_system_lookup_session_for_gradebook(*args, **kwargs)

    def get_grade_system_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return GradingManager.get_grade_system_query_session(*args, **kwargs)

    def get_grade_system_query_session_for_gradebook(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return GradingManager.get_grade_system_query_session_for_gradebook(*args, **kwargs)

    def get_grade_system_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_system_admin_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entry_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return GradingManager.get_grade_entry_lookup_session(*args, **kwargs)

    def get_grade_entry_lookup_session_for_gradebook(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return GradingManager.get_grade_entry_lookup_session_for_gradebook(*args, **kwargs)

    def get_grade_entry_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return GradingManager.get_grade_entry_query_session(*args, **kwargs)

    def get_grade_entry_query_session_for_gradebook(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return GradingManager.get_grade_entry_query_session_for_gradebook(*args, **kwargs)

    def get_grade_entry_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entry_admin_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_column_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_column_lookup_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_column_query_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_column_query_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_column_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_column_admin_session_for_gradebook(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_gradebook_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grading_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    grading_batch_proxy_manager = property(fget=get_grading_batch_proxy_manager)

    def get_grading_calculation_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    grading_calculation_proxy_manager = property(fget=get_grading_calculation_proxy_manager)

    def get_grading_transform_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    grading_transform_proxy_manager = property(fget=get_grading_transform_proxy_manager)


class Gradebook(abc_grading_objects.Gradebook, osid.OsidSession, osid.OsidCatalog):
    """Gradebook convenience adapter including related Session methods."""
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
        self._gradebook_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_gradebook_view(self, session):
        """Sets the underlying gradebook view to match current view"""
        if self._gradebook_view == FEDERATED:
            try:
                session.use_federated_gradebook_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_gradebook_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_gradebook')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_gradebook_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_gradebook_id(self):
        """Gets the Id of this gradebook."""
        return self._catalog_id

    def get_gradebook(self):
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

    def get_gradebook_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.grading.GradeSystemLookupSession

    def can_lookup_grade_systems(self):
        """Pass through to provider GradeSystemLookupSession.can_lookup_grade_systems"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('grade_system_lookup_session').can_lookup_grade_systems()

    def use_comparative_grade_system_view(self):
        """Pass through to provider GradeSystemLookupSession.use_comparative_grade_system_view"""
        self._object_views['grade_system'] = COMPARATIVE
        # self._get_provider_session('grade_system_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_grade_system_view()
            except AttributeError:
                pass

    def use_plenary_grade_system_view(self):
        """Pass through to provider GradeSystemLookupSession.use_plenary_grade_system_view"""
        self._object_views['grade_system'] = PLENARY
        # self._get_provider_session('grade_system_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_grade_system_view()
            except AttributeError:
                pass

    def use_federated_gradebook_view(self):
        """Pass through to provider GradeSystemLookupSession.use_federated_gradebook_view"""
        self._gradebook_view = FEDERATED
        # self._get_provider_session('grade_system_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_gradebook_view()
            except AttributeError:
                pass

    def use_isolated_gradebook_view(self):
        """Pass through to provider GradeSystemLookupSession.use_isolated_gradebook_view"""
        self._gradebook_view = ISOLATED
        # self._get_provider_session('grade_system_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_gradebook_view()
            except AttributeError:
                pass

    def get_grade_system(self, *args, **kwargs):
        """Pass through to provider GradeSystemLookupSession.get_grade_system"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('grade_system_lookup_session').get_grade_system(*args, **kwargs)

    def get_grade_system_by_grade(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_systems_by_ids(self, *args, **kwargs):
        """Pass through to provider GradeSystemLookupSession.get_grade_systems_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('grade_system_lookup_session').get_grade_systems_by_ids(*args, **kwargs)

    def get_grade_systems_by_genus_type(self, *args, **kwargs):
        """Pass through to provider GradeSystemLookupSession.get_grade_systems_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('grade_system_lookup_session').get_grade_systems_by_genus_type(*args, **kwargs)

    def get_grade_systems_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider GradeSystemLookupSession.get_grade_systems_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('grade_system_lookup_session').get_grade_systems_by_parent_genus_type(*args, **kwargs)

    def get_grade_systems_by_record_type(self, *args, **kwargs):
        """Pass through to provider GradeSystemLookupSession.get_grade_systems_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('grade_system_lookup_session').get_grade_systems_by_record_type(*args, **kwargs)

    def get_grade_systems(self):
        """Pass through to provider GradeSystemLookupSession.get_grade_systems"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('grade_system_lookup_session').get_grade_systems()

    grade_systems = property(fget=get_grade_systems)
##
# The following methods are from osid.grading.GradeSystemQuerySession

    def can_search_grade_systems(self):
        """Pass through to provider GradeSystemQuerySession.can_search_grade_systems"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('grade_system_query_session').can_search_grade_systems()

    def get_grade_system_query(self):
        """Pass through to provider GradeSystemQuerySession.get_grade_system_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('grade_system_query_session').get_grade_system_query()

    grade_system_query = property(fget=get_grade_system_query)

    def get_grade_systems_by_query(self, *args, **kwargs):
        """Pass through to provider GradeSystemQuerySession.get_grade_systems_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('grade_system_query_session').get_grade_systems_by_query(*args, **kwargs)
##
# The following methods are from osid.grading.GradeSystemAdminSession

    def can_create_grade_systems(self):
        """Pass through to provider GradeSystemAdminSession.can_create_grade_systems"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('grade_system_admin_session').can_create_grade_systems()

    def can_create_grade_system_with_record_types(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.can_create_grade_system_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('grade_system_admin_session').can_create_grade_system_with_record_types(*args, **kwargs)

    def get_grade_system_form_for_create(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.get_grade_system_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('grade_system_admin_session').get_grade_system_form_for_create(*args, **kwargs)

    def create_grade_system(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.create_grade_system"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('grade_system_admin_session').create_grade_system(*args, **kwargs)

    def can_update_grade_systems(self):
        """Pass through to provider GradeSystemAdminSession.can_update_grade_systems"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('grade_system_admin_session').can_update_grade_systems()

    def get_grade_system_form_for_update(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.get_grade_system_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('grade_system_admin_session').get_grade_system_form_for_update(*args, **kwargs)

    def get_grade_system_form(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.get_grade_system_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'grade_system_record_types' in kwargs:
            return self.get_grade_system_form_for_create(*args, **kwargs)
        else:
            return self.get_grade_system_form_for_update(*args, **kwargs)

    def duplicate_grade_system(self, grade_system_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('grade_system_admin_session').duplicate_grade_system(grade_system_id)

    def update_grade_system(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.update_grade_system"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('grade_system_admin_session').update_grade_system(*args, **kwargs)

    def save_grade_system(self, grade_system_form, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.update_grade_system"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if grade_system_form.is_for_update():
            return self.update_grade_system(grade_system_form, *args, **kwargs)
        else:
            return self.create_grade_system(grade_system_form, *args, **kwargs)

    def can_delete_grade_systems(self):
        """Pass through to provider GradeSystemAdminSession.can_delete_grade_systems"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('grade_system_admin_session').can_delete_grade_systems()

    def delete_grade_system(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.delete_grade_system"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('grade_system_admin_session').delete_grade_system(*args, **kwargs)

    def can_manage_grade_system_aliases(self):
        """Pass through to provider GradeSystemAdminSession.can_manage_grade_system_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('grade_system_admin_session').can_manage_grade_system_aliases()

    def alias_grade_system(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.alias_grade_system"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('grade_system_admin_session').alias_grade_system(*args, **kwargs)

    def can_create_grades(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.can_create_grades"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('grade_system_admin_session').can_create_grades(*args, **kwargs)

    def can_create_grade_with_record_types(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.can_create_grade_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('grade_system_admin_session').can_create_grade_with_record_types(*args, **kwargs)

    def get_grade_form_for_create(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.get_grade_form_for_create"""
        # Implemented from -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        return self._get_provider_session('grade_system_admin_session').get_grade_form_for_create(*args, **kwargs)

    def create_grade(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.create_grade"""
        # Implemented from -
        # osid.repository.AssetAdminSession.create_asset_content_template
        return self._get_provider_session('grade_system_admin_session').create_grade(*args, **kwargs)

    def can_update_grades(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_form_for_update(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.get_grade_form_for_update"""
        # Implemented from -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        return self._get_provider_session('grade_system_admin_session').get_grade_form_for_update(*args, **kwargs)

    def update_grade(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.update_grade"""
        # Implemented from -
        # osid.repository.AssetAdminSession.update_asset_template
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('grade_system_admin_session').update_grade(*args, **kwargs)

    def can_delete_grades(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.can_delete_grades"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('grade_system_admin_session').can_delete_grades(*args, **kwargs)

    def delete_grade(self, *args, **kwargs):
        """Pass through to provider GradeSystemAdminSession.delete_grade"""
        # Implemented from -
        # osid.repository.AssetAdminSession.delete_asset_content_template
        # Note: The OSID spec does not require returning updated object
        self._get_provider_session('grade_system_admin_session').delete_grade(*args, **kwargs)

    def can_manage_grade_aliases(self):
        """Pass through to provider GradeSystemAdminSession.can_manage_grade_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('grade_system_admin_session').can_manage_grade_aliases()

    def alias_grade(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.grading.GradeEntryLookupSession

    def can_lookup_grade_entries(self):
        """Pass through to provider GradeEntryLookupSession.can_lookup_grade_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('grade_entry_lookup_session').can_lookup_grade_entries()

    def use_comparative_grade_entry_view(self):
        """Pass through to provider GradeEntryLookupSession.use_comparative_grade_entry_view"""
        self._object_views['grade_entry'] = COMPARATIVE
        # self._get_provider_session('grade_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_grade_entry_view()
            except AttributeError:
                pass

    def use_plenary_grade_entry_view(self):
        """Pass through to provider GradeEntryLookupSession.use_plenary_grade_entry_view"""
        self._object_views['grade_entry'] = PLENARY
        # self._get_provider_session('grade_entry_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_grade_entry_view()
            except AttributeError:
                pass

    def use_effective_grade_entry_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_any_effective_grade_entry_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_grade_entry(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entry(*args, **kwargs)

    def get_grade_entries_by_ids(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries_by_ids(*args, **kwargs)

    def get_grade_entries_by_genus_type(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries_by_genus_type(*args, **kwargs)

    def get_grade_entries_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries_by_parent_genus_type(*args, **kwargs)

    def get_grade_entries_by_record_type(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries_by_record_type(*args, **kwargs)

    def get_grade_entries_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entries_for_gradebook_column(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_for_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries_for_gradebook_column(*args, **kwargs)

    def get_grade_entries_for_gradebook_column_on_date(self, *args, **kwargs):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries_for_gradebook_column_on_date(*args, **kwargs)

    def get_grade_entries_for_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entries_for_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entries_for_gradebook_column_and_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entries_by_grader(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_grade_entries(self):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('grade_entry_lookup_session').get_grade_entries()

    grade_entries = property(fget=get_grade_entries)
##
# The following methods are from osid.grading.GradeEntryQuerySession

    def can_search_grade_entries(self):
        """Pass through to provider GradeEntryQuerySession.can_search_grade_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('grade_entry_query_session').can_search_grade_entries()

    def get_grade_entry_query(self):
        """Pass through to provider GradeEntryQuerySession.get_grade_entry_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('grade_entry_query_session').get_grade_entry_query()

    grade_entry_query = property(fget=get_grade_entry_query)

    def get_grade_entries_by_query(self, *args, **kwargs):
        """Pass through to provider GradeEntryQuerySession.get_grade_entries_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('grade_entry_query_session').get_grade_entries_by_query(*args, **kwargs)
##
# The following methods are from osid.grading.GradeEntryAdminSession

    def can_create_grade_entries(self):
        """Pass through to provider GradeEntryAdminSession.can_create_grade_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('grade_entry_admin_session').can_create_grade_entries()

    def can_create_grade_entry_with_record_types(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.can_create_grade_entry_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('grade_entry_admin_session').can_create_grade_entry_with_record_types(*args, **kwargs)

    def get_grade_entry_form_for_create(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.get_grade_entry_form_for_create"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create_template
        return self._get_provider_session('grade_entry_admin_session').get_grade_entry_form_for_create(*args, **kwargs)

    def create_grade_entry(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.create_grade_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('grade_entry_admin_session').create_grade_entry(*args, **kwargs)

    def can_overridecalculated_grade_entries(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_grade_entry_form_for_override(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def override_calculated_grade_entry(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def can_update_grade_entries(self):
        """Pass through to provider GradeEntryAdminSession.can_update_grade_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('grade_entry_admin_session').can_update_grade_entries()

    def get_grade_entry_form_for_update(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.get_grade_entry_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('grade_entry_admin_session').get_grade_entry_form_for_update(*args, **kwargs)

    def get_grade_entry_form(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.get_grade_entry_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'grade_entry_record_types' in kwargs:
            return self.get_grade_entry_form_for_create(*args, **kwargs)
        else:
            return self.get_grade_entry_form_for_update(*args, **kwargs)

    def duplicate_grade_entry(self, grade_entry_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('grade_entry_admin_session').duplicate_grade_entry(grade_entry_id)

    def update_grade_entry(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.update_grade_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('grade_entry_admin_session').update_grade_entry(*args, **kwargs)

    def save_grade_entry(self, grade_entry_form, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.update_grade_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if grade_entry_form.is_for_update():
            return self.update_grade_entry(grade_entry_form, *args, **kwargs)
        else:
            return self.create_grade_entry(grade_entry_form, *args, **kwargs)

    def can_delete_grade_entries(self):
        """Pass through to provider GradeEntryAdminSession.can_delete_grade_entries"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('grade_entry_admin_session').can_delete_grade_entries()

    def delete_grade_entry(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.delete_grade_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('grade_entry_admin_session').delete_grade_entry(*args, **kwargs)

    def can_manage_grade_entry_aliases(self):
        """Pass through to provider GradeEntryAdminSession.can_manage_grade_entry_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('grade_entry_admin_session').can_manage_grade_entry_aliases()

    def alias_grade_entry(self, *args, **kwargs):
        """Pass through to provider GradeEntryAdminSession.alias_grade_entry"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('grade_entry_admin_session').alias_grade_entry(*args, **kwargs)
##
# The following methods are from osid.grading.GradebookColumnLookupSession

    def can_lookup_gradebook_columns(self):
        """Pass through to provider GradebookColumnLookupSession.can_lookup_gradebook_columns"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('gradebook_column_lookup_session').can_lookup_gradebook_columns()

    def use_comparative_gradebook_column_view(self):
        """Pass through to provider GradebookColumnLookupSession.use_comparative_gradebook_column_view"""
        self._object_views['gradebook_column'] = COMPARATIVE
        # self._get_provider_session('gradebook_column_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_gradebook_column_view()
            except AttributeError:
                pass

    def use_plenary_gradebook_column_view(self):
        """Pass through to provider GradebookColumnLookupSession.use_plenary_gradebook_column_view"""
        self._object_views['gradebook_column'] = PLENARY
        # self._get_provider_session('gradebook_column_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_gradebook_column_view()
            except AttributeError:
                pass

    def get_gradebook_column(self, *args, **kwargs):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_column(*args, **kwargs)

    def get_gradebook_columns_by_ids(self, *args, **kwargs):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_columns_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_columns_by_ids(*args, **kwargs)

    def get_gradebook_columns_by_genus_type(self, *args, **kwargs):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_columns_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_columns_by_genus_type(*args, **kwargs)

    def get_gradebook_columns_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_columns_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_columns_by_parent_genus_type(*args, **kwargs)

    def get_gradebook_columns_by_record_type(self, *args, **kwargs):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_columns_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_columns_by_record_type(*args, **kwargs)

    def get_gradebook_columns(self):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_columns"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_columns()

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_gradebook_column_summary(self, *args, **kwargs):
        """Pass through to provider GradebookColumnLookupSession.get_gradebook_column_summary"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('gradebook_column_lookup_session').get_gradebook_column_summary(*args, **kwargs)
##
# The following methods are from osid.grading.GradebookColumnQuerySession

    def can_search_gradebook_columns(self):
        """Pass through to provider GradebookColumnQuerySession.can_search_gradebook_columns"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('gradebook_column_query_session').can_search_gradebook_columns()

    def get_gradebook_column_query(self):
        """Pass through to provider GradebookColumnQuerySession.get_gradebook_column_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('gradebook_column_query_session').get_gradebook_column_query()

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def get_gradebook_columns_by_query(self, *args, **kwargs):
        """Pass through to provider GradebookColumnQuerySession.get_gradebook_columns_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('gradebook_column_query_session').get_gradebook_columns_by_query(*args, **kwargs)
##
# The following methods are from osid.grading.GradebookColumnAdminSession

    def can_create_gradebook_columns(self):
        """Pass through to provider GradebookColumnAdminSession.can_create_gradebook_columns"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('gradebook_column_admin_session').can_create_gradebook_columns()

    def can_create_gradebook_column_with_record_types(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.can_create_gradebook_column_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('gradebook_column_admin_session').can_create_gradebook_column_with_record_types(*args, **kwargs)

    def get_gradebook_column_form_for_create(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.get_gradebook_column_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('gradebook_column_admin_session').get_gradebook_column_form_for_create(*args, **kwargs)

    def create_gradebook_column(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.create_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('gradebook_column_admin_session').create_gradebook_column(*args, **kwargs)

    def can_update_gradebook_columns(self):
        """Pass through to provider GradebookColumnAdminSession.can_update_gradebook_columns"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('gradebook_column_admin_session').can_update_gradebook_columns()

    def get_gradebook_column_form_for_update(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.get_gradebook_column_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('gradebook_column_admin_session').get_gradebook_column_form_for_update(*args, **kwargs)

    def get_gradebook_column_form(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.get_gradebook_column_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'gradebook_column_record_types' in kwargs:
            return self.get_gradebook_column_form_for_create(*args, **kwargs)
        else:
            return self.get_gradebook_column_form_for_update(*args, **kwargs)

    def duplicate_gradebook_column(self, gradebook_column_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('gradebook_column_admin_session').duplicate_gradebook_column(gradebook_column_id)

    def update_gradebook_column(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.update_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('gradebook_column_admin_session').update_gradebook_column(*args, **kwargs)

    def save_gradebook_column(self, gradebook_column_form, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.update_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if gradebook_column_form.is_for_update():
            return self.update_gradebook_column(gradebook_column_form, *args, **kwargs)
        else:
            return self.create_gradebook_column(gradebook_column_form, *args, **kwargs)

    def sequence_gradebook_columns(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def move_gradebook_column(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def copy_gradebook_column_entries(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def can_delete_gradebook_columns(self):
        """Pass through to provider GradebookColumnAdminSession.can_delete_gradebook_columns"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('gradebook_column_admin_session').can_delete_gradebook_columns()

    def delete_gradebook_column(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.delete_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('gradebook_column_admin_session').delete_gradebook_column(*args, **kwargs)

    def can_manage_gradebook_column_aliases(self):
        """Pass through to provider GradebookColumnAdminSession.can_manage_gradebook_column_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('gradebook_column_admin_session').can_manage_gradebook_column_aliases()

    def alias_gradebook_column(self, *args, **kwargs):
        """Pass through to provider GradebookColumnAdminSession.alias_gradebook_column"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('gradebook_column_admin_session').alias_gradebook_column(*args, **kwargs)


class GradebookList(abc_grading_objects.GradebookList, osid.OsidList):
    """GradebookList convenience adapter including related Session methods."""

    def get_next_gradebook(self):
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

    next_gradebook = property(fget=get_next_gradebook)

    def get_next_gradebooks(self, n):
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
