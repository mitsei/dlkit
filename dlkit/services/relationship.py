"""DLKit Services implementations of relationship service."""
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
from dlkit.abstract_osid.relationship import objects as abc_relationship_objects
from dlkit.manager_impls.relationship import managers as relationship_managers


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


class RelationshipProfile(osid.OsidProfile, relationship_managers.RelationshipProfile):
    """RelationshipProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_relationship_lookup(self):
        """Pass through to provider supports_relationship_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_relationship_lookup()

    def supports_relationship_query(self):
        """Pass through to provider supports_relationship_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_relationship_query()

    def supports_relationship_admin(self):
        """Pass through to provider supports_relationship_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_relationship_admin()

    def supports_family_lookup(self):
        """Pass through to provider supports_family_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_lookup()

    def supports_family_admin(self):
        """Pass through to provider supports_family_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_admin()

    def supports_family_hierarchy(self):
        """Pass through to provider supports_family_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_hierarchy()

    def supports_family_hierarchy_design(self):
        """Pass through to provider supports_family_hierarchy_design"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_hierarchy_design()

    def get_relationship_record_types(self):
        """Pass through to provider get_relationship_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_relationship_record_types()

    relationship_record_types = property(fget=get_relationship_record_types)

    def get_relationship_search_record_types(self):
        """Pass through to provider get_relationship_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_relationship_search_record_types()

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    def get_family_record_types(self):
        """Pass through to provider get_family_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_family_record_types()

    family_record_types = property(fget=get_family_record_types)

    def get_family_search_record_types(self):
        """Pass through to provider get_family_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_family_search_record_types()

    family_search_record_types = property(fget=get_family_search_record_types)


class RelationshipManager(osid.OsidManager, osid.OsidSession, RelationshipProfile, relationship_managers.RelationshipManager):
    """RelationshipManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._family_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_family_view(self, session):
        """Sets the underlying family view to match current view"""
        if self._family_view == COMPARATIVE:
            try:
                session.use_comparative_family_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_family_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_family_view(session)
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
            try:
                session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                    proxy=self._proxy,
                                                    manager=manager)
            except AttributeError:
                session = self._instantiate_session('get_' + session_name,
                                                    proxy=self._proxy,
                                                    manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        if 'manager' in kwargs:
            session_class = getattr(kwargs['manager'], method_name)
            del kwargs['manager']
        else:
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
        parameter_id = Id('parameter:relationshipProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('RELATIONSHIP', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('RELATIONSHIP', provider_impl)

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

    def get_relationship_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_relationship_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_relationship_lookup_session(*args, **kwargs)

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    def get_relationship_lookup_session_for_family(self, *args, **kwargs):
        """Pass through to provider get_relationship_lookup_session_for_family"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_relationship_lookup_session_for_family(*args, **kwargs)

    def get_relationship_query_session(self, *args, **kwargs):
        """Pass through to provider get_relationship_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_relationship_query_session(*args, **kwargs)

    relationship_query_session = property(fget=get_relationship_query_session)

    def get_relationship_query_session_for_family(self, *args, **kwargs):
        """Pass through to provider get_relationship_query_session_for_family"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_relationship_query_session_for_family(*args, **kwargs)

    def get_relationship_admin_session(self, *args, **kwargs):
        """Pass through to provider get_relationship_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        return self._provider_manager.get_relationship_admin_session(*args, **kwargs)

    relationship_admin_session = property(fget=get_relationship_admin_session)

    def get_relationship_admin_session_for_family(self, *args, **kwargs):
        """Pass through to provider get_relationship_admin_session_for_family"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        return self._provider_manager.get_relationship_admin_session_for_family(*args, **kwargs)

    def get_family_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_family_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_family_lookup_session(*args, **kwargs)

    family_lookup_session = property(fget=get_family_lookup_session)

    def get_family_admin_session(self, *args, **kwargs):
        """Pass through to provider get_family_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_family_admin_session(*args, **kwargs)

    family_admin_session = property(fget=get_family_admin_session)

    def get_family_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_family_hierarchy_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_family_hierarchy_session(*args, **kwargs)

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    def get_family_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_family_hierarchy_design_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        return self._provider_manager.get_family_hierarchy_design_session(*args, **kwargs)

    family_hierarchy_design_session = property(fget=get_family_hierarchy_design_session)

    def get_relationship_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    relationship_batch_manager = property(fget=get_relationship_batch_manager)

    def get_relationship_rules_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    relationship_rules_manager = property(fget=get_relationship_rules_manager)
##
# The following methods are from osid.relationship.FamilyLookupSession

    def can_lookup_families(self):
        """Pass through to provider FamilyLookupSession.can_lookup_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.can_lookup_bins_template
        return self._get_provider_session('family_lookup_session').can_lookup_families()

    def use_comparative_family_view(self):
        """Pass through to provider FamilyLookupSession.use_comparative_family_view"""
        self._family_view = COMPARATIVE
        # self._get_provider_session('family_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_family_view()
            except AttributeError:
                pass

    def use_plenary_family_view(self):
        """Pass through to provider FamilyLookupSession.use_plenary_family_view"""
        self._family_view = PLENARY
        # self._get_provider_session('family_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_family_view()
            except AttributeError:
                pass

    def get_family(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return Family(
            self._provider_manager,
            self._get_provider_session('family_lookup_session').get_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_families_by_ids(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_genus_type(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_record_type(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_provider(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families(self):
        """Pass through to provider FamilyLookupSession.get_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('family_lookup_session').get_families()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    families = property(fget=get_families)
##
# The following methods are from osid.relationship.FamilyAdminSession

    def can_create_families(self):
        """Pass through to provider FamilyAdminSession.can_create_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bins
        return self._get_provider_session('family_admin_session').can_create_families()

    def can_create_family_with_record_types(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.can_create_family_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_create_bin_with_record_types
        return self._get_provider_session('family_admin_session').can_create_family_with_record_types(*args, **kwargs)

    def get_family_form_for_create(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.get_family_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('family_admin_session').get_family_form_for_create(*args, **kwargs)

    def create_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.create_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return Family(
            self._provider_manager,
            self._get_provider_session('family_admin_session').create_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_families(self):
        """Pass through to provider FamilyAdminSession.can_update_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_update_bins
        return self._get_provider_session('family_admin_session').can_update_families()

    def get_family_form_for_update(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.get_family_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('family_admin_session').get_family_form_for_update(*args, **kwargs)

    def get_family_form(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.get_family_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'family_record_types' in kwargs:
            return self.get_family_form_for_create(*args, **kwargs)
        else:
            return self.get_family_form_for_update(*args, **kwargs)

    def update_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.update_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return Family(
            self._provider_manager,
            self._get_provider_session('family_admin_session').update_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    def save_family(self, family_form, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.update_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if family_form.is_for_update():
            return self.update_family(family_form, *args, **kwargs)
        else:
            return self.create_family(family_form, *args, **kwargs)

    def can_delete_families(self):
        """Pass through to provider FamilyAdminSession.can_delete_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.can_delete_bins
        return self._get_provider_session('family_admin_session').can_delete_families()

    def delete_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.delete_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('family_admin_session').delete_family(*args, **kwargs)

    def can_manage_family_aliases(self):
        """Pass through to provider FamilyAdminSession.can_manage_family_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('family_admin_session').can_manage_family_aliases()

    def alias_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.alias_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.alias_bin
        self._get_provider_session('family_admin_session').alias_family(*args, **kwargs)
##
# The following methods are from osid.relationship.FamilyHierarchySession

    def get_family_hierarchy_id(self):
        """Pass through to provider FamilyHierarchySession.get_family_hierarchy_id"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._get_provider_session('family_hierarchy_session').get_family_hierarchy_id()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Pass through to provider FamilyHierarchySession.get_family_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        return self._get_provider_session('family_hierarchy_session').get_family_hierarchy()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_access_family_hierarchy(self):
        """Pass through to provider FamilyHierarchySession.can_access_family_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._get_provider_session('family_hierarchy_session').can_access_family_hierarchy()

    def get_root_family_ids(self):
        """Pass through to provider FamilyHierarchySession.get_root_family_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        return self._get_provider_session('family_hierarchy_session').get_root_family_ids()

    root_family_ids = property(fget=get_root_family_ids)

    def get_root_families(self):
        """Pass through to provider FamilyHierarchySession.get_root_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        return self._get_provider_session('family_hierarchy_session').get_root_families()

    root_families = property(fget=get_root_families)

    def has_parent_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.has_parent_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        return self._get_provider_session('family_hierarchy_session').has_parent_families(*args, **kwargs)

    def is_parent_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_parent_of_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        return self._get_provider_session('family_hierarchy_session').is_parent_of_family(*args, **kwargs)

    def get_parent_family_ids(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_parent_family_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        return self._get_provider_session('family_hierarchy_session').get_parent_family_ids(*args, **kwargs)

    def get_parent_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_parent_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        return self._get_provider_session('family_hierarchy_session').get_parent_families(*args, **kwargs)

    def is_ancestor_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_ancestor_of_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        return self._get_provider_session('family_hierarchy_session').is_ancestor_of_family(*args, **kwargs)

    def has_child_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.has_child_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        return self._get_provider_session('family_hierarchy_session').has_child_families(*args, **kwargs)

    def is_child_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_child_of_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        return self._get_provider_session('family_hierarchy_session').is_child_of_family(*args, **kwargs)

    def get_child_family_ids(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_child_family_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        return self._get_provider_session('family_hierarchy_session').get_child_family_ids(*args, **kwargs)

    def get_child_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_child_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bins
        return self._get_provider_session('family_hierarchy_session').get_child_families(*args, **kwargs)

    def is_descendant_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_descendant_of_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        return self._get_provider_session('family_hierarchy_session').is_descendant_of_family(*args, **kwargs)

    def get_family_node_ids(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_family_node_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        return self._get_provider_session('family_hierarchy_session').get_family_node_ids(*args, **kwargs)

    def get_family_nodes(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_family_nodes"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        return self._get_provider_session('family_hierarchy_session').get_family_nodes(*args, **kwargs)
##
# The following methods are from osid.relationship.FamilyHierarchyDesignSession

    def can_modify_family_hierarchy(self):
        """Pass through to provider FamilyHierarchyDesignSession.can_modify_family_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._get_provider_session('family_hierarchy_design_session').can_modify_family_hierarchy()

    def create_family_hierarchy(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.can_modify_family_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('family_hierarchy_design_session').create_family_hierarchy(*args, **kwargs)

    def delete_family_hierarchy(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.can_modify_family_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('family_hierarchy_design_session').delete_family_hierarchy(*args, **kwargs)

    def add_root_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.add_root_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin
        self._get_provider_session('family_hierarchy_design_session').add_root_family(*args, **kwargs)

    def remove_root_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.remove_root_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_root_bin
        self._get_provider_session('family_hierarchy_design_session').remove_root_family(*args, **kwargs)

    def add_child_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.add_child_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_child_bin
        self._get_provider_session('family_hierarchy_design_session').add_child_family(*args, **kwargs)

    def remove_child_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.remove_child_family"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bin
        self._get_provider_session('family_hierarchy_design_session').remove_child_family(*args, **kwargs)

    def remove_child_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.remove_child_families"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bins
        self._get_provider_session('family_hierarchy_design_session').remove_child_families(*args, **kwargs)


class RelationshipProxyManager(osid.OsidProxyManager, RelationshipProfile, relationship_managers.RelationshipProxyManager):
    """RelationshipProxyManager convenience adapter including related Session methods."""

    def get_relationship_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return RelationshipManager.get_relationship_lookup_session(*args, **kwargs)

    def get_relationship_lookup_session_for_family(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return RelationshipManager.get_relationship_lookup_session_for_family(*args, **kwargs)

    def get_relationship_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return RelationshipManager.get_relationship_query_session(*args, **kwargs)

    def get_relationship_query_session_for_family(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return RelationshipManager.get_relationship_query_session_for_family(*args, **kwargs)

    def get_relationship_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationship_admin_session_for_family(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_family_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_family_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_family_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_family_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationship_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    relationship_batch_proxy_manager = property(fget=get_relationship_batch_proxy_manager)

    def get_relationship_rules_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    relationship_rules_proxy_manager = property(fget=get_relationship_rules_proxy_manager)


class Family(abc_relationship_objects.Family, osid.OsidSession, osid.OsidCatalog):
    """Family convenience adapter including related Session methods."""
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
        self._family_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_family_view(self, session):
        """Sets the underlying family view to match current view"""
        if self._family_view == FEDERATED:
            try:
                session.use_federated_family_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_family_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_family')
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
            self._set_family_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_family_id(self):
        """Gets the Id of this family."""
        return self._catalog_id

    def get_family(self):
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

    def get_family_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.relationship.RelationshipLookupSession

    def can_lookup_relationships(self):
        """Pass through to provider RelationshipLookupSession.can_lookup_relationships"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('relationship_lookup_session').can_lookup_relationships()

    def use_comparative_relationship_view(self):
        """Pass through to provider RelationshipLookupSession.use_comparative_relationship_view"""
        self._object_views['relationship'] = COMPARATIVE
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_relationship_view()
            except AttributeError:
                pass

    def use_plenary_relationship_view(self):
        """Pass through to provider RelationshipLookupSession.use_plenary_relationship_view"""
        self._object_views['relationship'] = PLENARY
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_relationship_view()
            except AttributeError:
                pass

    def use_federated_family_view(self):
        """Pass through to provider RelationshipLookupSession.use_federated_family_view"""
        self._family_view = FEDERATED
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_family_view()
            except AttributeError:
                pass

    def use_isolated_family_view(self):
        """Pass through to provider RelationshipLookupSession.use_isolated_family_view"""
        self._family_view = ISOLATED
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_family_view()
            except AttributeError:
                pass

    def use_effective_relationship_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def use_any_effective_relationship_view(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def get_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationship"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('relationship_lookup_session').get_relationship(*args, **kwargs)

    def get_relationships_by_ids(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_ids(*args, **kwargs)

    def get_relationships_by_genus_type(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_genus_type(*args, **kwargs)

    def get_relationships_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_parent_genus_type(*args, **kwargs)

    def get_relationships_by_record_type(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_record_type(*args, **kwargs)

    def get_relationships_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_for_source(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_source"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_template
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_source(*args, **kwargs)

    def get_relationships_for_source_on_date(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_source_on_date"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_source_on_date(*args, **kwargs)

    def get_relationships_by_genus_type_for_source(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_by_genus_type_for_source_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_for_destination(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_for_destination_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_by_genus_type_for_destination(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_by_genus_type_for_destination_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_for_peers(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_for_peers_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_by_genus_type_for_peers(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_by_genus_type_for_peers_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships(self):
        """Pass through to provider RelationshipLookupSession.get_relationships"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('relationship_lookup_session').get_relationships()

    relationships = property(fget=get_relationships)
##
# The following methods are from osid.relationship.RelationshipQuerySession

    def can_search_relationships(self):
        """Pass through to provider RelationshipQuerySession.can_search_relationships"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('relationship_query_session').can_search_relationships()

    def get_relationship_query(self):
        """Pass through to provider RelationshipQuerySession.get_relationship_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('relationship_query_session').get_relationship_query()

    relationship_query = property(fget=get_relationship_query)

    def get_relationships_by_query(self, *args, **kwargs):
        """Pass through to provider RelationshipQuerySession.get_relationships_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('relationship_query_session').get_relationships_by_query(*args, **kwargs)
##
# The following methods are from osid.relationship.RelationshipAdminSession

    def can_create_relationships(self):
        """Pass through to provider RelationshipAdminSession.can_create_relationships"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('relationship_admin_session').can_create_relationships()

    def can_create_relationship_with_record_types(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.can_create_relationship_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('relationship_admin_session').can_create_relationship_with_record_types(*args, **kwargs)

    def get_relationship_form_for_create(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.get_relationship_form_for_create"""
        # Implemented from kitosid template for -
        # osid.relationship.RelationshipAdminSession.get_relationship_form_for_create_template
        return self._get_provider_session('relationship_admin_session').get_relationship_form_for_create(*args, **kwargs)

    def create_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.create_relationship"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('relationship_admin_session').create_relationship(*args, **kwargs)

    def can_update_relationships(self):
        """Pass through to provider RelationshipAdminSession.can_update_relationships"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_update_resources
        return self._get_provider_session('relationship_admin_session').can_update_relationships()

    def get_relationship_form_for_update(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.get_relationship_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('relationship_admin_session').get_relationship_form_for_update(*args, **kwargs)

    def get_relationship_form(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.get_relationship_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'relationship_record_types' in kwargs:
            return self.get_relationship_form_for_create(*args, **kwargs)
        else:
            return self.get_relationship_form_for_update(*args, **kwargs)

    def duplicate_relationship(self, relationship_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('relationship_admin_session').duplicate_relationship(relationship_id)

    def update_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.update_relationship"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('relationship_admin_session').update_relationship(*args, **kwargs)

    def save_relationship(self, relationship_form, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.update_relationship"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if relationship_form.is_for_update():
            return self.update_relationship(relationship_form, *args, **kwargs)
        else:
            return self.create_relationship(relationship_form, *args, **kwargs)

    def can_delete_relationships(self):
        """Pass through to provider RelationshipAdminSession.can_delete_relationships"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_delete_resources
        return self._get_provider_session('relationship_admin_session').can_delete_relationships()

    def delete_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.delete_relationship"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('relationship_admin_session').delete_relationship(*args, **kwargs)

    def can_manage_relationship_aliases(self):
        """Pass through to provider RelationshipAdminSession.can_manage_relationship_aliases"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_manage_resource_aliases_template
        return self._get_provider_session('relationship_admin_session').can_manage_relationship_aliases()

    def alias_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.alias_relationship"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('relationship_admin_session').alias_relationship(*args, **kwargs)


class FamilyList(abc_relationship_objects.FamilyList, osid.OsidList):
    """FamilyList convenience adapter including related Session methods."""

    def get_next_family(self):
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

    next_family = property(fget=get_next_family)

    def get_next_families(self, n):
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
