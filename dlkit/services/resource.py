"""DLKit Services implementations of resource service."""
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
from dlkit.abstract_osid.resource import objects as abc_resource_objects
from dlkit.manager_impls.resource import managers as resource_managers


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


class ResourceProfile(osid.OsidProfile, resource_managers.ResourceProfile):
    """ResourceProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_resource_lookup(self):
        """Pass through to provider supports_resource_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_lookup()

    def supports_resource_query(self):
        """Pass through to provider supports_resource_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_query()

    def supports_resource_search(self):
        """Pass through to provider supports_resource_search"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_search()

    def supports_resource_admin(self):
        """Pass through to provider supports_resource_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_admin()

    def supports_resource_notification(self):
        """Pass through to provider supports_resource_notification"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_notification()

    def supports_resource_bin(self):
        """Pass through to provider supports_resource_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_bin()

    def supports_resource_bin_assignment(self):
        """Pass through to provider supports_resource_bin_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_bin_assignment()

    def supports_resource_agent(self):
        """Pass through to provider supports_resource_agent"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_agent()

    def supports_resource_agent_assignment(self):
        """Pass through to provider supports_resource_agent_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_agent_assignment()

    def supports_bin_lookup(self):
        """Pass through to provider supports_bin_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_lookup()

    def supports_bin_query(self):
        """Pass through to provider supports_bin_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_query()

    def supports_bin_admin(self):
        """Pass through to provider supports_bin_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_admin()

    def supports_bin_hierarchy(self):
        """Pass through to provider supports_bin_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_hierarchy()

    def supports_bin_hierarchy_design(self):
        """Pass through to provider supports_bin_hierarchy_design"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_hierarchy_design()

    def get_resource_record_types(self):
        """Pass through to provider get_resource_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_record_types()

    resource_record_types = property(fget=get_resource_record_types)

    def get_resource_search_record_types(self):
        """Pass through to provider get_resource_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_search_record_types()

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def get_resource_relationship_record_types(self):
        """Pass through to provider get_resource_relationship_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_relationship_record_types()

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def get_resource_relationship_search_record_types(self):
        """Pass through to provider get_resource_relationship_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_relationship_search_record_types()

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def get_bin_record_types(self):
        """Pass through to provider get_bin_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bin_record_types()

    bin_record_types = property(fget=get_bin_record_types)

    def get_bin_search_record_types(self):
        """Pass through to provider get_bin_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bin_search_record_types()

    bin_search_record_types = property(fget=get_bin_search_record_types)


class ResourceManager(osid.OsidManager, osid.OsidSession, ResourceProfile, resource_managers.ResourceManager):
    """ResourceManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._bin_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_bin_view(self, session):
        """Sets the underlying bin view to match current view"""
        if self._bin_view == COMPARATIVE:
            try:
                session.use_comparative_bin_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_bin_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_bin_view(session)
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
        parameter_id = Id('parameter:resourceProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('RESOURCE', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('RESOURCE', provider_impl)

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

    def get_resource_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_resource_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_resource_lookup_session(*args, **kwargs)

    resource_lookup_session = property(fget=get_resource_lookup_session)

    def get_resource_lookup_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_lookup_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_resource_lookup_session_for_bin(*args, **kwargs)

    def get_resource_query_session(self, *args, **kwargs):
        """Pass through to provider get_resource_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_resource_query_session(*args, **kwargs)

    resource_query_session = property(fget=get_resource_query_session)

    def get_resource_query_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_query_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_resource_query_session_for_bin(*args, **kwargs)

    def get_resource_search_session(self, *args, **kwargs):
        """Pass through to provider get_resource_search_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_resource_search_session(*args, **kwargs)

    resource_search_session = property(fget=get_resource_search_session)

    def get_resource_search_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_search_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_resource_search_session_for_bin(*args, **kwargs)

    def get_resource_admin_session(self, *args, **kwargs):
        """Pass through to provider get_resource_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_resource_admin_session(*args, **kwargs)

    resource_admin_session = property(fget=get_resource_admin_session)

    def get_resource_admin_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_admin_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_resource_admin_session_for_bin(*args, **kwargs)

    def get_resource_notification_session(self, *args, **kwargs):
        """Pass through to provider get_resource_notification_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_notification_session_catalog_template
        return self._provider_manager.get_resource_notification_session(*args, **kwargs)

    def get_resource_notification_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_notification_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_notification_session_for_bin_catalog_template
        return self._provider_manager.get_resource_notification_session_for_bin(*args, **kwargs)

    def get_resource_bin_session(self, *args, **kwargs):
        """Pass through to provider get_resource_bin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_resource_bin_session(*args, **kwargs)

    resource_bin_session = property(fget=get_resource_bin_session)

    def get_resource_bin_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_resource_bin_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_resource_bin_assignment_session(*args, **kwargs)

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)

    def get_resource_agent_session(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_resource_agent_session(*args, **kwargs)

    resource_agent_session = property(fget=get_resource_agent_session)

    def get_resource_agent_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_resource_agent_session_for_bin(*args, **kwargs)

    def get_resource_agent_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_resource_agent_assignment_session(*args, **kwargs)

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)

    def get_resource_agent_assignment_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_assignment_session_for_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_resource_agent_assignment_session_for_bin(*args, **kwargs)

    def get_bin_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_bin_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_bin_lookup_session(*args, **kwargs)

    bin_lookup_session = property(fget=get_bin_lookup_session)

    def get_bin_query_session(self, *args, **kwargs):
        """Pass through to provider get_bin_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_bin_query_session(*args, **kwargs)

    bin_query_session = property(fget=get_bin_query_session)

    def get_bin_admin_session(self, *args, **kwargs):
        """Pass through to provider get_bin_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_bin_admin_session(*args, **kwargs)

    bin_admin_session = property(fget=get_bin_admin_session)

    def get_bin_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_bin_hierarchy_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_bin_hierarchy_session(*args, **kwargs)

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)

    def get_bin_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_bin_hierarchy_design_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_bin_hierarchy_design_session(*args, **kwargs)

    bin_hierarchy_design_session = property(fget=get_bin_hierarchy_design_session)

    def get_resource_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    resource_batch_manager = property(fget=get_resource_batch_manager)

    def get_resource_demographic_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    resource_demographic_manager = property(fget=get_resource_demographic_manager)
##
# The following methods are from osid.resource.ResourceBinSession

    def use_comparative_bin_view(self):
        """Pass through to provider ResourceBinSession.use_comparative_bin_view"""
        self._bin_view = COMPARATIVE
        # self._get_provider_session('resource_bin_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_bin_view()
            except AttributeError:
                pass

    def use_plenary_bin_view(self):
        """Pass through to provider ResourceBinSession.use_plenary_bin_view"""
        self._bin_view = PLENARY
        # self._get_provider_session('resource_bin_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_bin_view()
            except AttributeError:
                pass

    def can_lookup_resource_bin_mappings(self):
        """Pass through to provider ResourceBinSession.can_lookup_resource_bin_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('resource_bin_session').can_lookup_resource_bin_mappings()

    def get_resource_ids_by_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resource_ids_by_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('resource_bin_session').get_resource_ids_by_bin(*args, **kwargs)

    def get_resources_by_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resources_by_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('resource_bin_session').get_resources_by_bin(*args, **kwargs)

    def get_resource_ids_by_bins(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resource_ids_by_bins"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('resource_bin_session').get_resource_ids_by_bins(*args, **kwargs)

    def get_resources_by_bins(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resources_by_bins"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('resource_bin_session').get_resources_by_bins(*args, **kwargs)

    def get_bin_ids_by_resource(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_bin_ids_by_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('resource_bin_session').get_bin_ids_by_resource(*args, **kwargs)

    def get_bins_by_resource(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_bins_by_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        catalogs = self._get_provider_session('resource_bin_session').get_bins_by_resource(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)
##
# The following methods are from osid.resource.ResourceBinAssignmentSession

    def can_assign_resources(self):
        """Pass through to provider ResourceBinAssignmentSession.can_assign_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('resource_bin_assignment_session').can_assign_resources()

    def can_assign_resources_to_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.can_assign_resources_to_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('resource_bin_assignment_session').can_assign_resources_to_bin(*args, **kwargs)

    def get_assignable_bin_ids(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.get_assignable_bin_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        return self._get_provider_session('resource_bin_assignment_session').get_assignable_bin_ids(*args, **kwargs)

    def get_assignable_bin_ids_for_resource(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('resource_bin_assignment_session').get_assignable_bin_ids_for_resource(*args, **kwargs)

    def assign_resource_to_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.assign_resource_to_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('resource_bin_assignment_session').assign_resource_to_bin(*args, **kwargs)

    def unassign_resource_from_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.unassign_resource_from_bin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('resource_bin_assignment_session').unassign_resource_from_bin(*args, **kwargs)
##
# The following methods are from osid.resource.BinLookupSession

    def can_lookup_bins(self):
        """Pass through to provider BinLookupSession.can_lookup_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('bin_lookup_session').can_lookup_bins()

    def get_bin(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return Bin(
            self._provider_manager,
            self._get_provider_session('bin_lookup_session').get_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_bins_by_ids(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_genus_type(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_record_type(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_provider(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins(self):
        """Pass through to provider BinLookupSession.get_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('bin_lookup_session').get_bins()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    bins = property(fget=get_bins)
##
# The following methods are from osid.resource.BinQuerySession

    def can_search_bins(self):
        """Pass through to provider BinQuerySession.can_search_bins"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('bin_query_session').can_search_bins()

    def get_bin_query(self):
        """Pass through to provider BinQuerySession.get_bin_query"""
        # Implemented from kitosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        return self._get_provider_session('bin_query_session').get_bin_query()

    bin_query = property(fget=get_bin_query)

    def get_bins_by_query(self, *args, **kwargs):
        """Pass through to provider BinQuerySession.get_bins_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        return self._get_provider_session('bin_query_session').get_bins_by_query(*args, **kwargs)
##
# The following methods are from osid.resource.BinAdminSession

    def can_create_bins(self):
        """Pass through to provider BinAdminSession.can_create_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('bin_admin_session').can_create_bins()

    def can_create_bin_with_record_types(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.can_create_bin_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('bin_admin_session').can_create_bin_with_record_types(*args, **kwargs)

    def get_bin_form_for_create(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.get_bin_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('bin_admin_session').get_bin_form_for_create(*args, **kwargs)

    def create_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.create_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return Bin(
            self._provider_manager,
            self._get_provider_session('bin_admin_session').create_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_bins(self):
        """Pass through to provider BinAdminSession.can_update_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('bin_admin_session').can_update_bins()

    def get_bin_form_for_update(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.get_bin_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('bin_admin_session').get_bin_form_for_update(*args, **kwargs)

    def get_bin_form(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.get_bin_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'bin_record_types' in kwargs:
            return self.get_bin_form_for_create(*args, **kwargs)
        else:
            return self.get_bin_form_for_update(*args, **kwargs)

    def update_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.update_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return Bin(
            self._provider_manager,
            self._get_provider_session('bin_admin_session').update_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    def save_bin(self, bin_form, *args, **kwargs):
        """Pass through to provider BinAdminSession.update_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if bin_form.is_for_update():
            return self.update_bin(bin_form, *args, **kwargs)
        else:
            return self.create_bin(bin_form, *args, **kwargs)

    def can_delete_bins(self):
        """Pass through to provider BinAdminSession.can_delete_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('bin_admin_session').can_delete_bins()

    def delete_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.delete_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('bin_admin_session').delete_bin(*args, **kwargs)

    def can_manage_bin_aliases(self):
        """Pass through to provider BinAdminSession.can_manage_bin_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('bin_admin_session').can_manage_bin_aliases()

    def alias_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.alias_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.alias_bin
        self._get_provider_session('bin_admin_session').alias_bin(*args, **kwargs)
##
# The following methods are from osid.resource.BinHierarchySession

    def get_bin_hierarchy_id(self):
        """Pass through to provider BinHierarchySession.get_bin_hierarchy_id"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._get_provider_session('bin_hierarchy_session').get_bin_hierarchy_id()

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        """Pass through to provider BinHierarchySession.get_bin_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        return self._get_provider_session('bin_hierarchy_session').get_bin_hierarchy()

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        """Pass through to provider BinHierarchySession.can_access_bin_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._get_provider_session('bin_hierarchy_session').can_access_bin_hierarchy()

    def get_root_bin_ids(self):
        """Pass through to provider BinHierarchySession.get_root_bin_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        return self._get_provider_session('bin_hierarchy_session').get_root_bin_ids()

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        """Pass through to provider BinHierarchySession.get_root_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        return self._get_provider_session('bin_hierarchy_session').get_root_bins()

    root_bins = property(fget=get_root_bins)

    def has_parent_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.has_parent_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        return self._get_provider_session('bin_hierarchy_session').has_parent_bins(*args, **kwargs)

    def is_parent_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_parent_of_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        return self._get_provider_session('bin_hierarchy_session').is_parent_of_bin(*args, **kwargs)

    def get_parent_bin_ids(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_parent_bin_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        return self._get_provider_session('bin_hierarchy_session').get_parent_bin_ids(*args, **kwargs)

    def get_parent_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_parent_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        return self._get_provider_session('bin_hierarchy_session').get_parent_bins(*args, **kwargs)

    def is_ancestor_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_ancestor_of_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        return self._get_provider_session('bin_hierarchy_session').is_ancestor_of_bin(*args, **kwargs)

    def has_child_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.has_child_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        return self._get_provider_session('bin_hierarchy_session').has_child_bins(*args, **kwargs)

    def is_child_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_child_of_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        return self._get_provider_session('bin_hierarchy_session').is_child_of_bin(*args, **kwargs)

    def get_child_bin_ids(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_child_bin_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        return self._get_provider_session('bin_hierarchy_session').get_child_bin_ids(*args, **kwargs)

    def get_child_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_child_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bins
        return self._get_provider_session('bin_hierarchy_session').get_child_bins(*args, **kwargs)

    def is_descendant_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_descendant_of_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        return self._get_provider_session('bin_hierarchy_session').is_descendant_of_bin(*args, **kwargs)

    def get_bin_node_ids(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_bin_node_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        return self._get_provider_session('bin_hierarchy_session').get_bin_node_ids(*args, **kwargs)

    def get_bin_nodes(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_bin_nodes"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        return self._get_provider_session('bin_hierarchy_session').get_bin_nodes(*args, **kwargs)
##
# The following methods are from osid.resource.BinHierarchyDesignSession

    def can_modify_bin_hierarchy(self):
        """Pass through to provider BinHierarchyDesignSession.can_modify_bin_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._get_provider_session('bin_hierarchy_design_session').can_modify_bin_hierarchy()

    def create_bin_hierarchy(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.can_modify_bin_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('bin_hierarchy_design_session').create_bin_hierarchy(*args, **kwargs)

    def delete_bin_hierarchy(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.can_modify_bin_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('bin_hierarchy_design_session').delete_bin_hierarchy(*args, **kwargs)

    def add_root_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.add_root_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin
        self._get_provider_session('bin_hierarchy_design_session').add_root_bin(*args, **kwargs)

    def remove_root_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.remove_root_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_root_bin
        self._get_provider_session('bin_hierarchy_design_session').remove_root_bin(*args, **kwargs)

    def add_child_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.add_child_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_child_bin
        self._get_provider_session('bin_hierarchy_design_session').add_child_bin(*args, **kwargs)

    def remove_child_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.remove_child_bin"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bin
        self._get_provider_session('bin_hierarchy_design_session').remove_child_bin(*args, **kwargs)

    def remove_child_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.remove_child_bins"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bins
        self._get_provider_session('bin_hierarchy_design_session').remove_child_bins(*args, **kwargs)


class ResourceProxyManager(osid.OsidProxyManager, ResourceProfile, resource_managers.ResourceProxyManager):
    """ResourceProxyManager convenience adapter including related Session methods."""

    def get_resource_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return ResourceManager.get_resource_lookup_session(*args, **kwargs)

    def get_resource_lookup_session_for_bin(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return ResourceManager.get_resource_lookup_session_for_bin(*args, **kwargs)

    def get_resource_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return ResourceManager.get_resource_query_session(*args, **kwargs)

    def get_resource_query_session_for_bin(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return ResourceManager.get_resource_query_session_for_bin(*args, **kwargs)

    def get_resource_search_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_search_session_for_bin(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_admin_session_for_bin(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_notification_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_notification_session_for_bin(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_bin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_bin_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_group_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_agent_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_agent_session_for_bin(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_agent_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_agent_assignment_session_for_bin(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bin_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bin_query_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bin_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bin_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bin_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_resource_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    resource_batch_proxy_manager = property(fget=get_resource_batch_proxy_manager)

    def get_resource_demographic_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    resource_demographic_proxy_manager = property(fget=get_resource_demographic_proxy_manager)


class Bin(abc_resource_objects.Bin, osid.OsidSession, osid.OsidCatalog):
    """Bin convenience adapter including related Session methods."""
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
        self._bin_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_bin_view(self, session):
        """Sets the underlying bin view to match current view"""
        if self._bin_view == FEDERATED:
            try:
                session.use_federated_bin_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_bin_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_bin')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_bin_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_bin_id(self):
        """Gets the Id of this bin."""
        return self._catalog_id

    def get_bin(self):
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

    def get_bin_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.resource.ResourceLookupSession

    def can_lookup_resources(self):
        """Pass through to provider ResourceLookupSession.can_lookup_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('resource_lookup_session').can_lookup_resources()

    def use_comparative_resource_view(self):
        """Pass through to provider ResourceLookupSession.use_comparative_resource_view"""
        self._object_views['resource'] = COMPARATIVE
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_resource_view()
            except AttributeError:
                pass

    def use_plenary_resource_view(self):
        """Pass through to provider ResourceLookupSession.use_plenary_resource_view"""
        self._object_views['resource'] = PLENARY
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_resource_view()
            except AttributeError:
                pass

    def use_federated_bin_view(self):
        """Pass through to provider ResourceLookupSession.use_federated_bin_view"""
        self._bin_view = FEDERATED
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_bin_view()
            except AttributeError:
                pass

    def use_isolated_bin_view(self):
        """Pass through to provider ResourceLookupSession.use_isolated_bin_view"""
        self._bin_view = ISOLATED
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_bin_view()
            except AttributeError:
                pass

    def get_resource(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('resource_lookup_session').get_resource(*args, **kwargs)

    def get_resources_by_ids(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('resource_lookup_session').get_resources_by_ids(*args, **kwargs)

    def get_resources_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('resource_lookup_session').get_resources_by_genus_type(*args, **kwargs)

    def get_resources_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('resource_lookup_session').get_resources_by_parent_genus_type(*args, **kwargs)

    def get_resources_by_record_type(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('resource_lookup_session').get_resources_by_record_type(*args, **kwargs)

    def get_resources(self):
        """Pass through to provider ResourceLookupSession.get_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('resource_lookup_session').get_resources()

    resources = property(fget=get_resources)
##
# The following methods are from osid.resource.ResourceQuerySession

    def can_search_resources(self):
        """Pass through to provider ResourceQuerySession.can_search_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('resource_query_session').can_search_resources()

    def get_resource_query(self):
        """Pass through to provider ResourceQuerySession.get_resource_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('resource_query_session').get_resource_query()

    resource_query = property(fget=get_resource_query)

    def get_resources_by_query(self, *args, **kwargs):
        """Pass through to provider ResourceQuerySession.get_resources_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('resource_query_session').get_resources_by_query(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceSearchSession

    def get_resource_search(self):
        """Pass through to provider ResourceSearchSession.get_resource_search"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        return self._get_provider_session('resource_search_session').get_resource_search()

    resource_search = property(fget=get_resource_search)

    def get_resource_search_order(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    resource_search_order = property(fget=get_resource_search_order)

    def get_resources_by_search(self, *args, **kwargs):
        """Pass through to provider ResourceSearchSession.get_resources_by_search"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        return self._get_provider_session('resource_search_session').get_resources_by_search(*args, **kwargs)

    def get_resource_query_from_inspector(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.resource.ResourceAdminSession

    def can_create_resources(self):
        """Pass through to provider ResourceAdminSession.can_create_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('resource_admin_session').can_create_resources()

    def can_create_resource_with_record_types(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.can_create_resource_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('resource_admin_session').can_create_resource_with_record_types(*args, **kwargs)

    def get_resource_form_for_create(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.get_resource_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('resource_admin_session').get_resource_form_for_create(*args, **kwargs)

    def create_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.create_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('resource_admin_session').create_resource(*args, **kwargs)

    def can_update_resources(self):
        """Pass through to provider ResourceAdminSession.can_update_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('resource_admin_session').can_update_resources()

    def get_resource_form_for_update(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.get_resource_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('resource_admin_session').get_resource_form_for_update(*args, **kwargs)

    def get_resource_form(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.get_resource_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'resource_record_types' in kwargs:
            return self.get_resource_form_for_create(*args, **kwargs)
        else:
            return self.get_resource_form_for_update(*args, **kwargs)

    def duplicate_resource(self, resource_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('resource_admin_session').duplicate_resource(resource_id)

    def update_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.update_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('resource_admin_session').update_resource(*args, **kwargs)

    def save_resource(self, resource_form, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.update_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if resource_form.is_for_update():
            return self.update_resource(resource_form, *args, **kwargs)
        else:
            return self.create_resource(resource_form, *args, **kwargs)

    def can_delete_resources(self):
        """Pass through to provider ResourceAdminSession.can_delete_resources"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('resource_admin_session').can_delete_resources()

    def delete_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.delete_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('resource_admin_session').delete_resource(*args, **kwargs)

    def can_manage_resource_aliases(self):
        """Pass through to provider ResourceAdminSession.can_manage_resource_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('resource_admin_session').can_manage_resource_aliases()

    def alias_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.alias_resource"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('resource_admin_session').alias_resource(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceNotificationSession

    def can_register_for_resource_notifications(self):
        """Pass through to provider ResourceNotificationSession.can_register_for_resource_notifications"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._get_provider_session('resource_notification_session').can_register_for_resource_notifications()

    def register_for_new_resources(self):
        """Pass through to provider ResourceNotificationSession.register_for_new_resources"""
        self._get_provider_session('resource_notification_session').register_for_new_resources()

    def register_for_changed_resources(self):
        """Pass through to provider ResourceNotificationSession.register_for_changed_resources"""
        self._get_provider_session('resource_notification_session').register_for_changed_resources()

    def register_for_changed_resource(self, *args, **kwargs):
        """Pass through to provider ResourceNotificationSession.register_for_changed_resource"""
        self._get_provider_session('resource_notification_session').register_for_changed_resource(*args, **kwargs)

    def register_for_deleted_resources(self):
        """Pass through to provider ResourceNotificationSession.register_for_deleted_resources"""
        self._get_provider_session('resource_notification_session').register_for_deleted_resources()

    def register_for_deleted_resource(self, *args, **kwargs):
        """Pass through to provider ResourceNotificationSession.register_for_deleted_resource"""
        self._get_provider_session('resource_notification_session').register_for_deleted_resource(*args, **kwargs)

    def reliable_resource_notifications(self):
        """Pass through to provider ResourceNotificationSession.reliable_resource_notifications"""
        self._get_provider_session('resource_notification_session').reliable_resource_notifications()

    def unreliable_resource_notifications(self):
        """Pass through to provider ResourceNotificationSession.unreliable_resource_notifications"""
        self._get_provider_session('resource_notification_session').unreliable_resource_notifications()

    def acknowledge_resource_notification(self, *args, **kwargs):
        """Pass through to provider ResourceNotificationSession.acknowledge_resource_notification"""
        self._get_provider_session('resource_notification_session').acknowledge_resource_notification(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceAgentSession

    def can_lookup_resource_agent_mappings(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_comparative_agent_view(self):
        """Pass through to provider ResourceAgentSession.use_comparative_agent_view"""
        self._object_views['agent'] = COMPARATIVE
        # self._get_provider_session('resource_agent_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_agent_view()
            except AttributeError:
                pass

    def use_plenary_agent_view(self):
        """Pass through to provider ResourceAgentSession.use_plenary_agent_view"""
        self._object_views['agent'] = PLENARY
        # self._get_provider_session('resource_agent_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_agent_view()
            except AttributeError:
                pass

    def get_resource_id_by_agent(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_session').get_resource_id_by_agent(*args, **kwargs)

    def get_resource_by_agent(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_session').get_resource_by_agent(*args, **kwargs)

    def get_agent_ids_by_resource(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_session').get_agent_ids_by_resource(*args, **kwargs)

    def get_agents_by_resource(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_session').get_agents_by_resource(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceAgentAssignmentSession

    def can_assign_agents(self):
        return self._get_provider_session('resource_agent_assignment_session').can_assign_agents()

    def can_assign_agents_to_resource(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_assignment_session').can_assign_agents_to_resource(*args, **kwargs)

    def assign_agent_to_resource(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_assignment_session').assign_agent_to_resource(*args, **kwargs)

    def unassign_agent_from_resource(self, *args, **kwargs):
        return self._get_provider_session('resource_agent_assignment_session').unassign_agent_from_resource(*args, **kwargs)


class BinList(abc_resource_objects.BinList, osid.OsidList):
    """BinList convenience adapter including related Session methods."""

    def get_next_bin(self):
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

    next_bin = property(fget=get_next_bin)

    def get_next_bins(self, n):
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
