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
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_lookup()

    def supports_resource_query(self):
        """Pass through to provider supports_resource_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_query()

    def supports_resource_search(self):
        """Pass through to provider supports_resource_search"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_search()

    def supports_resource_admin(self):
        """Pass through to provider supports_resource_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_admin()

    def supports_resource_notification(self):
        """Pass through to provider supports_resource_notification"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_notification()

    def supports_resource_bin(self):
        """Pass through to provider supports_resource_bin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_bin()

    def supports_resource_bin_assignment(self):
        """Pass through to provider supports_resource_bin_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_bin_assignment()

    def supports_resource_agent(self):
        """Pass through to provider supports_resource_agent"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_agent()

    def supports_resource_agent_assignment(self):
        """Pass through to provider supports_resource_agent_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_resource_agent_assignment()

    def supports_bin_lookup(self):
        """Pass through to provider supports_bin_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_bin_lookup()

    def supports_bin_query(self):
        """Pass through to provider supports_bin_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_bin_query()

    def supports_bin_admin(self):
        """Pass through to provider supports_bin_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_bin_admin()

    def supports_bin_hierarchy(self):
        """Pass through to provider supports_bin_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_bin_hierarchy()

    def supports_bin_hierarchy_design(self):
        """Pass through to provider supports_bin_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_bin_hierarchy_design()

    def get_resource_record_types(self):
        """Pass through to provider get_resource_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_resource_record_types()

    resource_record_types = property(fget=get_resource_record_types)

    def get_resource_search_record_types(self):
        """Pass through to provider get_resource_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_resource_search_record_types()

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def get_resource_relationship_record_types(self):
        """Pass through to provider get_resource_relationship_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_resource_relationship_record_types()

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def get_resource_relationship_search_record_types(self):
        """Pass through to provider get_resource_relationship_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_resource_relationship_search_record_types()

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def get_bin_record_types(self):
        """Pass through to provider get_bin_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_bin_record_types()

    bin_record_types = property(fget=get_bin_record_types)

    def get_bin_search_record_types(self):
        """Pass through to provider get_bin_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
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
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_resource_lookup_session(*args, **kwargs)

    resource_lookup_session = property(fget=get_resource_lookup_session)

    def get_resource_lookup_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_lookup_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_resource_lookup_session_for_bin(*args, **kwargs)

    def get_resource_query_session(self, *args, **kwargs):
        """Pass through to provider get_resource_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_resource_query_session(*args, **kwargs)

    resource_query_session = property(fget=get_resource_query_session)

    def get_resource_query_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_query_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_resource_query_session_for_bin(*args, **kwargs)

    def get_resource_search_session(self, *args, **kwargs):
        """Pass through to provider get_resource_search_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_resource_search_session(*args, **kwargs)

    resource_search_session = property(fget=get_resource_search_session)

    def get_resource_search_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_search_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_resource_search_session_for_bin(*args, **kwargs)

    def get_resource_admin_session(self, *args, **kwargs):
        """Pass through to provider get_resource_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_resource_admin_session(*args, **kwargs)

    resource_admin_session = property(fget=get_resource_admin_session)

    def get_resource_admin_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_admin_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_resource_admin_session_for_bin(*args, **kwargs)

    def get_resource_notification_session(self, *args, **kwargs):
        """Pass through to provider get_resource_notification_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_notification_session
        return self._provider_manager.get_resource_notification_session(*args, **kwargs)

    def get_resource_notification_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_notification_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_notification_session_for_catalog
        return self._provider_manager.get_resource_notification_session_for_bin(*args, **kwargs)

    def get_resource_bin_session(self, *args, **kwargs):
        """Pass through to provider get_resource_bin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_resource_bin_session(*args, **kwargs)

    resource_bin_session = property(fget=get_resource_bin_session)

    def get_resource_bin_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_resource_bin_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_resource_bin_assignment_session(*args, **kwargs)

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)

    def get_resource_agent_session(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_resource_agent_session(*args, **kwargs)

    resource_agent_session = property(fget=get_resource_agent_session)

    def get_resource_agent_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_resource_agent_session_for_bin(*args, **kwargs)

    def get_resource_agent_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_resource_agent_assignment_session(*args, **kwargs)

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)

    def get_resource_agent_assignment_session_for_bin(self, *args, **kwargs):
        """Pass through to provider get_resource_agent_assignment_session_for_bin"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_resource_agent_assignment_session_for_bin(*args, **kwargs)

    def get_bin_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_bin_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_bin_lookup_session(*args, **kwargs)

    bin_lookup_session = property(fget=get_bin_lookup_session)

    def get_bin_query_session(self, *args, **kwargs):
        """Pass through to provider get_bin_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_bin_query_session(*args, **kwargs)

    bin_query_session = property(fget=get_bin_query_session)

    def get_bin_admin_session(self, *args, **kwargs):
        """Pass through to provider get_bin_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_bin_admin_session(*args, **kwargs)

    bin_admin_session = property(fget=get_bin_admin_session)

    def get_bin_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_bin_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_bin_hierarchy_session(*args, **kwargs)

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)

    def get_bin_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_bin_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
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
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._bin_view = COMPARATIVE
        # self._get_provider_session('resource_bin_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_bin_view()
            except AttributeError:
                pass

    def use_plenary_bin_view(self):
        """Pass through to provider ResourceBinSession.use_plenary_bin_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._bin_view = PLENARY
        # self._get_provider_session('resource_bin_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_bin_view()
            except AttributeError:
                pass

    def can_lookup_resource_bin_mappings(self):
        """Pass through to provider ResourceBinSession.can_lookup_resource_bin_mappings"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.can_lookup_object_catalog_mappings
        return self._get_provider_session('resource_bin_session').can_lookup_resource_bin_mappings()

    def get_resource_ids_by_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resource_ids_by_bin"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalog
        return self._get_provider_session('resource_bin_session').get_resource_ids_by_bin(*args, **kwargs)

    def get_resources_by_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resources_by_bin"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalog
        return self._get_provider_session('resource_bin_session').get_resources_by_bin(*args, **kwargs)

    def get_resource_ids_by_bins(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resource_ids_by_bins"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalogs
        return self._get_provider_session('resource_bin_session').get_resource_ids_by_bins(*args, **kwargs)

    def get_resources_by_bins(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_resources_by_bins"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalogs
        return self._get_provider_session('resource_bin_session').get_resources_by_bins(*args, **kwargs)

    def get_bin_ids_by_resource(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_bin_ids_by_resource"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalog_ids_by_object
        return self._get_provider_session('resource_bin_session').get_bin_ids_by_resource(*args, **kwargs)

    def get_bins_by_resource(self, *args, **kwargs):
        """Pass through to provider ResourceBinSession.get_bins_by_resource"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalogs_by_object
        catalogs = self._get_provider_session('resource_bin_session').get_bins_by_resource(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)
##
# The following methods are from osid.resource.ResourceBinAssignmentSession

    def can_assign_resources(self):
        """Pass through to provider ResourceBinAssignmentSession.can_assign_resources"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects
        return self._get_provider_session('resource_bin_assignment_session').can_assign_resources()

    def can_assign_resources_to_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.can_assign_resources_to_bin"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects_to_catalog
        return self._get_provider_session('resource_bin_assignment_session').can_assign_resources_to_bin(*args, **kwargs)

    def get_assignable_bin_ids(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.get_assignable_bin_ids"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids
        return self._get_provider_session('resource_bin_assignment_session').get_assignable_bin_ids(*args, **kwargs)

    def get_assignable_bin_ids_for_resource(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids_for_object
        return self._get_provider_session('resource_bin_assignment_session').get_assignable_bin_ids_for_resource(*args, **kwargs)

    def assign_resource_to_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.assign_resource_to_bin"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.assign_object_to_catalog
        self._get_provider_session('resource_bin_assignment_session').assign_resource_to_bin(*args, **kwargs)

    def unassign_resource_from_bin(self, *args, **kwargs):
        """Pass through to provider ResourceBinAssignmentSession.unassign_resource_from_bin"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.unassign_object_from_catalog
        self._get_provider_session('resource_bin_assignment_session').unassign_resource_from_bin(*args, **kwargs)
##
# The following methods are from osid.resource.BinLookupSession

    def can_lookup_bins(self):
        """Pass through to provider BinLookupSession.can_lookup_bins"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('bin_lookup_session').can_lookup_bins()

    def get_bin(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bin"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return Bin(
            self._provider_manager,
            self._get_provider_session('bin_lookup_session').get_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_bins_by_ids(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_genus_type(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_record_type(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins_by_provider(self, *args, **kwargs):
        """Pass through to provider BinLookupSession.get_bins_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('bin_lookup_session').get_bins_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bin(self._provider_manager, cat, self._runtime, self._proxy))
        return BinList(cat_list)

    def get_bins(self):
        """Pass through to provider BinLookupSession.get_bins"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
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
        # Built from: templates/osid_session.GenericCatalogQuerySession.can_search_catalogs
        return self._get_provider_session('bin_query_session').can_search_bins()

    def get_bin_query(self):
        """Pass through to provider BinQuerySession.get_bin_query"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.get_catalog_query
        return self._get_provider_session('bin_query_session').get_bin_query()

    bin_query = property(fget=get_bin_query)

    def get_bins_by_query(self, *args, **kwargs):
        """Pass through to provider BinQuerySession.get_bins_by_query"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.get_catalogs_by_query
        return self._get_provider_session('bin_query_session').get_bins_by_query(*args, **kwargs)
##
# The following methods are from osid.resource.BinAdminSession

    def can_create_bins(self):
        """Pass through to provider BinAdminSession.can_create_bins"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('bin_admin_session').can_create_bins()

    def can_create_bin_with_record_types(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.can_create_bin_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('bin_admin_session').can_create_bin_with_record_types(*args, **kwargs)

    def get_bin_form_for_create(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.get_bin_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('bin_admin_session').get_bin_form_for_create(*args, **kwargs)

    def create_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.create_bin"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return Bin(
            self._provider_manager,
            self._get_provider_session('bin_admin_session').create_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_bins(self):
        """Pass through to provider BinAdminSession.can_update_bins"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('bin_admin_session').can_update_bins()

    def get_bin_form_for_update(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.get_bin_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('bin_admin_session').get_bin_form_for_update(*args, **kwargs)

    def update_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.update_bin"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return Bin(
            self._provider_manager,
            self._get_provider_session('bin_admin_session').update_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_bins(self):
        """Pass through to provider BinAdminSession.can_delete_bins"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('bin_admin_session').can_delete_bins()

    def delete_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.delete_bin"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.delete_catalog
        self._get_provider_session('bin_admin_session').delete_bin(*args, **kwargs)

    def can_manage_bin_aliases(self):
        """Pass through to provider BinAdminSession.can_manage_bin_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('bin_admin_session').can_manage_bin_aliases()

    def alias_bin(self, *args, **kwargs):
        """Pass through to provider BinAdminSession.alias_bin"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('bin_admin_session').alias_bin(*args, **kwargs)
##
# The following methods are from osid.resource.BinHierarchySession

    def get_bin_hierarchy_id(self):
        """Pass through to provider BinHierarchySession.get_bin_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('bin_hierarchy_session').get_bin_hierarchy_id()

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        """Pass through to provider BinHierarchySession.get_bin_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('bin_hierarchy_session').get_bin_hierarchy()

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        """Pass through to provider BinHierarchySession.can_access_bin_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('bin_hierarchy_session').can_access_bin_hierarchy()

    def get_root_bin_ids(self):
        """Pass through to provider BinHierarchySession.get_root_bin_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('bin_hierarchy_session').get_root_bin_ids()

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        """Pass through to provider BinHierarchySession.get_root_bins"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('bin_hierarchy_session').get_root_bins()

    root_bins = property(fget=get_root_bins)

    def has_parent_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.has_parent_bins"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('bin_hierarchy_session').has_parent_bins(*args, **kwargs)

    def is_parent_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_parent_of_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('bin_hierarchy_session').is_parent_of_bin(*args, **kwargs)

    def get_parent_bin_ids(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_parent_bin_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('bin_hierarchy_session').get_parent_bin_ids(*args, **kwargs)

    def get_parent_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_parent_bins"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('bin_hierarchy_session').get_parent_bins(*args, **kwargs)

    def is_ancestor_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_ancestor_of_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('bin_hierarchy_session').is_ancestor_of_bin(*args, **kwargs)

    def has_child_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.has_child_bins"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('bin_hierarchy_session').has_child_bins(*args, **kwargs)

    def is_child_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_child_of_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('bin_hierarchy_session').is_child_of_bin(*args, **kwargs)

    def get_child_bin_ids(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_child_bin_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('bin_hierarchy_session').get_child_bin_ids(*args, **kwargs)

    def get_child_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_child_bins"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('bin_hierarchy_session').get_child_bins(*args, **kwargs)

    def is_descendant_of_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.is_descendant_of_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('bin_hierarchy_session').is_descendant_of_bin(*args, **kwargs)

    def get_bin_node_ids(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_bin_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('bin_hierarchy_session').get_bin_node_ids(*args, **kwargs)

    def get_bin_nodes(self, *args, **kwargs):
        """Pass through to provider BinHierarchySession.get_bin_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('bin_hierarchy_session').get_bin_nodes(*args, **kwargs)
##
# The following methods are from osid.resource.BinHierarchyDesignSession

    def can_modify_bin_hierarchy(self):
        """Pass through to provider BinHierarchyDesignSession.can_modify_bin_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('bin_hierarchy_design_session').can_modify_bin_hierarchy()

    def add_root_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.add_root_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('bin_hierarchy_design_session').add_root_bin(*args, **kwargs)

    def remove_root_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.remove_root_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('bin_hierarchy_design_session').remove_root_bin(*args, **kwargs)

    def add_child_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.add_child_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('bin_hierarchy_design_session').add_child_bin(*args, **kwargs)

    def remove_child_bin(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.remove_child_bin"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('bin_hierarchy_design_session').remove_child_bin(*args, **kwargs)

    def remove_child_bins(self, *args, **kwargs):
        """Pass through to provider BinHierarchyDesignSession.remove_child_bins"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('bin_hierarchy_design_session').remove_child_bins(*args, **kwargs)


class ResourceProxyManager(osid.OsidProxyManager, ResourceProfile, ResourceManager, resource_managers.ResourceProxyManager):
    """ResourceProxyManager convenience adapter including related Session methods."""
    pass


class Bin(abc_resource_objects.Bin, osid.OsidSession, osid.OsidCatalog):
    """Bin convenience adapter including related Session methods."""
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

    def get_bin_id(self):
        """Pass through to provider ResourceLookupSession.get_bin_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('resource_lookup_session').get_bin_id()

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Pass through to provider ResourceLookupSession.get_bin"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return Bin(
            self._provider_manager,
            self._get_provider_session('resource_lookup_session').get_bin(*args, **kwargs),
            self._runtime,
            self._proxy)

    bin = property(fget=get_bin)

    def can_lookup_resources(self):
        """Pass through to provider ResourceLookupSession.can_lookup_resources"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('resource_lookup_session').can_lookup_resources()

    def use_comparative_resource_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider ResourceLookupSession.use_comparative_resource_view"""
        self._object_views['resource'] = COMPARATIVE
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_resource_view()
            except AttributeError:
                pass

    def use_plenary_resource_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider ResourceLookupSession.use_plenary_resource_view"""
        self._object_views['resource'] = PLENARY
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_resource_view()
            except AttributeError:
                pass

    def use_federated_bin_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_federated_catalog_view
        """Pass through to provider ResourceLookupSession.use_federated_bin_view"""
        self._bin_view = FEDERATED
        # self._get_provider_session('resource_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_bin_view()
            except AttributeError:
                pass

    def use_isolated_bin_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_isolated_catalog_view
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('resource_lookup_session').get_resource(*args, **kwargs)

    def get_resources_by_ids(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('resource_lookup_session').get_resources_by_ids(*args, **kwargs)

    def get_resources_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('resource_lookup_session').get_resources_by_genus_type(*args, **kwargs)

    def get_resources_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('resource_lookup_session').get_resources_by_parent_genus_type(*args, **kwargs)

    def get_resources_by_record_type(self, *args, **kwargs):
        """Pass through to provider ResourceLookupSession.get_resources_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('resource_lookup_session').get_resources_by_record_type(*args, **kwargs)

    def get_resources(self):
        """Pass through to provider ResourceLookupSession.get_resources"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('resource_lookup_session').get_resources()

    resources = property(fget=get_resources)
##
# The following methods are from osid.resource.ResourceQuerySession

    def can_search_resources(self):
        """Pass through to provider ResourceQuerySession.can_search_resources"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('resource_query_session').can_search_resources()

    def get_resource_query(self):
        """Pass through to provider ResourceQuerySession.get_resource_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('resource_query_session').get_resource_query()

    resource_query = property(fget=get_resource_query)

    def get_resources_by_query(self, *args, **kwargs):
        """Pass through to provider ResourceQuerySession.get_resources_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('resource_query_session').get_resources_by_query(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceSearchSession

    def get_resource_search(self):
        """Pass through to provider ResourceSearchSession.get_resource_search"""
        # Built from: templates/osid_session.GenericObjectSearchSession.get_object_search
        return self._get_provider_session('resource_search_session').get_resource_search()

    resource_search = property(fget=get_resource_search)

    def get_resource_search_order(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    resource_search_order = property(fget=get_resource_search_order)

    def get_resources_by_search(self, *args, **kwargs):
        """Pass through to provider ResourceSearchSession.get_resources_by_search"""
        # Built from: templates/osid_session.GenericObjectSearchSession.get_objects_by_search
        return self._get_provider_session('resource_search_session').get_resources_by_search(*args, **kwargs)

    def get_resource_query_from_inspector(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.resource.ResourceAdminSession

    def can_create_resources(self):
        """Pass through to provider ResourceAdminSession.can_create_resources"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('resource_admin_session').can_create_resources()

    def can_create_resource_with_record_types(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.can_create_resource_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('resource_admin_session').can_create_resource_with_record_types(*args, **kwargs)

    def get_resource_form_for_create(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.get_resource_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_create
        return self._get_provider_session('resource_admin_session').get_resource_form_for_create(*args, **kwargs)

    def create_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.create_resource"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('resource_admin_session').create_resource(*args, **kwargs)

    def can_update_resources(self):
        """Pass through to provider ResourceAdminSession.can_update_resources"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('resource_admin_session').can_update_resources()

    def get_resource_form_for_update(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.get_resource_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('resource_admin_session').get_resource_form_for_update(*args, **kwargs)

    def update_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.update_resource"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('resource_admin_session').update_resource(*args, **kwargs)

    def can_delete_resources(self):
        """Pass through to provider ResourceAdminSession.can_delete_resources"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('resource_admin_session').can_delete_resources()

    def delete_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.delete_resource"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('resource_admin_session').delete_resource(*args, **kwargs)

    def can_manage_resource_aliases(self):
        """Pass through to provider ResourceAdminSession.can_manage_resource_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('resource_admin_session').can_manage_resource_aliases()

    def alias_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAdminSession.alias_resource"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('resource_admin_session').alias_resource(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceNotificationSession

    def can_register_for_resource_notifications(self):
        """Pass through to provider ResourceNotificationSession.can_register_for_resource_notifications"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.can_register_for_object_notifications
        return self._get_provider_session('resource_notification_session').can_register_for_resource_notifications()

    def register_for_new_resources(self):
        """Pass through to provider ResourceNotificationSession.register_for_new_resources"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_new_objects
        self._get_provider_session('resource_notification_session').register_for_new_resources()

    def register_for_changed_resources(self):
        """Pass through to provider ResourceNotificationSession.register_for_changed_resources"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_objects
        self._get_provider_session('resource_notification_session').register_for_changed_resources()

    def register_for_changed_resource(self, *args, **kwargs):
        """Pass through to provider ResourceNotificationSession.register_for_changed_resource"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_object
        self._get_provider_session('resource_notification_session').register_for_changed_resource(*args, **kwargs)

    def register_for_deleted_resources(self):
        """Pass through to provider ResourceNotificationSession.register_for_deleted_resources"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_deleted_objects
        self._get_provider_session('resource_notification_session').register_for_deleted_resources()

    def register_for_deleted_resource(self, *args, **kwargs):
        """Pass through to provider ResourceNotificationSession.register_for_deleted_resource"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_deleted_object
        self._get_provider_session('resource_notification_session').register_for_deleted_resource(*args, **kwargs)

    def reliable_resource_notifications(self):
        """Pass through to provider ResourceNotificationSession.reliable_resource_notifications"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.reliable_object_notifications
        self._get_provider_session('resource_notification_session').reliable_resource_notifications()

    def unreliable_resource_notifications(self):
        """Pass through to provider ResourceNotificationSession.unreliable_resource_notifications"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.unreliable_object_notifications
        self._get_provider_session('resource_notification_session').unreliable_resource_notifications()

    def acknowledge_resource_notification(self, *args, **kwargs):
        """Pass through to provider ResourceNotificationSession.acknowledge_resource_notification"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.acknowledge_object_notification
        self._get_provider_session('resource_notification_session').acknowledge_resource_notification(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceAgentSession

    def can_lookup_resource_agent_mappings(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_comparative_agent_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider ResourceAgentSession.use_comparative_agent_view"""
        self._object_views['agent'] = COMPARATIVE
        # self._get_provider_session('resource_agent_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_agent_view()
            except AttributeError:
                pass

    def use_plenary_agent_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider ResourceAgentSession.use_plenary_agent_view"""
        self._object_views['agent'] = PLENARY
        # self._get_provider_session('resource_agent_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_agent_view()
            except AttributeError:
                pass

    def get_resource_id_by_agent(self, *args, **kwargs):
        """Pass through to provider ResourceAgentSession.get_resource_id_by_agent"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('resource_agent_session').get_resource_id_by_agent(*args, **kwargs)

    def get_resource_by_agent(self, *args, **kwargs):
        """Pass through to provider ResourceAgentSession.get_resource_by_agent"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('resource_agent_session').get_resource_by_agent(*args, **kwargs)

    def get_agent_ids_by_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAgentSession.get_agent_ids_by_resource"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('resource_agent_session').get_agent_ids_by_resource(*args, **kwargs)

    def get_agents_by_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAgentSession.get_agents_by_resource"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('resource_agent_session').get_agents_by_resource(*args, **kwargs)
##
# The following methods are from osid.resource.ResourceAgentAssignmentSession

    def can_assign_agents(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def can_assign_agents_to_resource(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def assign_agent_to_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAgentAssignmentSession.assign_agent_to_resource"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('resource_agent_assignment_session').assign_agent_to_resource(*args, **kwargs)

    def unassign_agent_from_resource(self, *args, **kwargs):
        """Pass through to provider ResourceAgentAssignmentSession.unassign_agent_from_resource"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('resource_agent_assignment_session').unassign_agent_from_resource(*args, **kwargs)


class BinList(abc_resource_objects.BinList, osid.OsidList):
    """BinList convenience adapter including related Session methods."""

    def get_next_bin(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(Bin)

    __next__ = next

    next_bin = property(fget=get_next_bin)

    def get_next_bins(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(BinList, number=n)
