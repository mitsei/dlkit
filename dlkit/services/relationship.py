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
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_relationship_lookup()

    def supports_relationship_query(self):
        """Pass through to provider supports_relationship_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_relationship_query()

    def supports_relationship_admin(self):
        """Pass through to provider supports_relationship_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_relationship_admin()

    def supports_family_lookup(self):
        """Pass through to provider supports_family_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_family_lookup()

    def supports_family_admin(self):
        """Pass through to provider supports_family_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_family_admin()

    def supports_family_hierarchy(self):
        """Pass through to provider supports_family_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_family_hierarchy()

    def supports_family_hierarchy_design(self):
        """Pass through to provider supports_family_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_family_hierarchy_design()

    def get_relationship_record_types(self):
        """Pass through to provider get_relationship_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_relationship_record_types()

    relationship_record_types = property(fget=get_relationship_record_types)

    def get_relationship_search_record_types(self):
        """Pass through to provider get_relationship_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_relationship_search_record_types()

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    def get_family_record_types(self):
        """Pass through to provider get_family_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_family_record_types()

    family_record_types = property(fget=get_family_record_types)

    def get_family_search_record_types(self):
        """Pass through to provider get_family_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
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
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_relationship_lookup_session(*args, **kwargs)

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    def get_relationship_lookup_session_for_family(self, *args, **kwargs):
        """Pass through to provider get_relationship_lookup_session_for_family"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_relationship_lookup_session_for_family(*args, **kwargs)

    def get_relationship_query_session(self, *args, **kwargs):
        """Pass through to provider get_relationship_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_relationship_query_session(*args, **kwargs)

    relationship_query_session = property(fget=get_relationship_query_session)

    def get_relationship_query_session_for_family(self, *args, **kwargs):
        """Pass through to provider get_relationship_query_session_for_family"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_relationship_query_session_for_family(*args, **kwargs)

    def get_relationship_admin_session(self, *args, **kwargs):
        """Pass through to provider get_relationship_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_relationship_admin_session(*args, **kwargs)

    relationship_admin_session = property(fget=get_relationship_admin_session)

    def get_relationship_admin_session_for_family(self, *args, **kwargs):
        """Pass through to provider get_relationship_admin_session_for_family"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_relationship_admin_session_for_family(*args, **kwargs)

    def get_family_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_family_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_family_lookup_session(*args, **kwargs)

    family_lookup_session = property(fget=get_family_lookup_session)

    def get_family_admin_session(self, *args, **kwargs):
        """Pass through to provider get_family_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_family_admin_session(*args, **kwargs)

    family_admin_session = property(fget=get_family_admin_session)

    def get_family_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_family_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_family_hierarchy_session(*args, **kwargs)

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    def get_family_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_family_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
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
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('family_lookup_session').can_lookup_families()

    def use_comparative_family_view(self):
        """Pass through to provider FamilyLookupSession.use_comparative_family_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._family_view = COMPARATIVE
        # self._get_provider_session('family_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_family_view()
            except AttributeError:
                pass

    def use_plenary_family_view(self):
        """Pass through to provider FamilyLookupSession.use_plenary_family_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._family_view = PLENARY
        # self._get_provider_session('family_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_family_view()
            except AttributeError:
                pass

    def get_family(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_family"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return Family(
            self._provider_manager,
            self._get_provider_session('family_lookup_session').get_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_families_by_ids(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_genus_type(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_record_type(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families_by_provider(self, *args, **kwargs):
        """Pass through to provider FamilyLookupSession.get_families_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('family_lookup_session').get_families_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Family(self._provider_manager, cat, self._runtime, self._proxy))
        return FamilyList(cat_list)

    def get_families(self):
        """Pass through to provider FamilyLookupSession.get_families"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
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
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('family_admin_session').can_create_families()

    def can_create_family_with_record_types(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.can_create_family_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('family_admin_session').can_create_family_with_record_types(*args, **kwargs)

    def get_family_form_for_create(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.get_family_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('family_admin_session').get_family_form_for_create(*args, **kwargs)

    def create_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.create_family"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return Family(
            self._provider_manager,
            self._get_provider_session('family_admin_session').create_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_families(self):
        """Pass through to provider FamilyAdminSession.can_update_families"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('family_admin_session').can_update_families()

    def get_family_form_for_update(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.get_family_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('family_admin_session').get_family_form_for_update(*args, **kwargs)

    def update_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.update_family"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return Family(
            self._provider_manager,
            self._get_provider_session('family_admin_session').update_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_families(self):
        """Pass through to provider FamilyAdminSession.can_delete_families"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('family_admin_session').can_delete_families()

    def delete_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.delete_family"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.delete_catalog
        self._get_provider_session('family_admin_session').delete_family(*args, **kwargs)

    def can_manage_family_aliases(self):
        """Pass through to provider FamilyAdminSession.can_manage_family_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('family_admin_session').can_manage_family_aliases()

    def alias_family(self, *args, **kwargs):
        """Pass through to provider FamilyAdminSession.alias_family"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('family_admin_session').alias_family(*args, **kwargs)
##
# The following methods are from osid.relationship.FamilyHierarchySession

    def get_family_hierarchy_id(self):
        """Pass through to provider FamilyHierarchySession.get_family_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('family_hierarchy_session').get_family_hierarchy_id()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Pass through to provider FamilyHierarchySession.get_family_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('family_hierarchy_session').get_family_hierarchy()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_access_family_hierarchy(self):
        """Pass through to provider FamilyHierarchySession.can_access_family_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('family_hierarchy_session').can_access_family_hierarchy()

    def get_root_family_ids(self):
        """Pass through to provider FamilyHierarchySession.get_root_family_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('family_hierarchy_session').get_root_family_ids()

    root_family_ids = property(fget=get_root_family_ids)

    def get_root_families(self):
        """Pass through to provider FamilyHierarchySession.get_root_families"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('family_hierarchy_session').get_root_families()

    root_families = property(fget=get_root_families)

    def has_parent_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.has_parent_families"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('family_hierarchy_session').has_parent_families(*args, **kwargs)

    def is_parent_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_parent_of_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('family_hierarchy_session').is_parent_of_family(*args, **kwargs)

    def get_parent_family_ids(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_parent_family_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('family_hierarchy_session').get_parent_family_ids(*args, **kwargs)

    def get_parent_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_parent_families"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('family_hierarchy_session').get_parent_families(*args, **kwargs)

    def is_ancestor_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_ancestor_of_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('family_hierarchy_session').is_ancestor_of_family(*args, **kwargs)

    def has_child_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.has_child_families"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('family_hierarchy_session').has_child_families(*args, **kwargs)

    def is_child_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_child_of_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('family_hierarchy_session').is_child_of_family(*args, **kwargs)

    def get_child_family_ids(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_child_family_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('family_hierarchy_session').get_child_family_ids(*args, **kwargs)

    def get_child_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_child_families"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('family_hierarchy_session').get_child_families(*args, **kwargs)

    def is_descendant_of_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.is_descendant_of_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('family_hierarchy_session').is_descendant_of_family(*args, **kwargs)

    def get_family_node_ids(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_family_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('family_hierarchy_session').get_family_node_ids(*args, **kwargs)

    def get_family_nodes(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchySession.get_family_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('family_hierarchy_session').get_family_nodes(*args, **kwargs)
##
# The following methods are from osid.relationship.FamilyHierarchyDesignSession

    def can_modify_family_hierarchy(self):
        """Pass through to provider FamilyHierarchyDesignSession.can_modify_family_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('family_hierarchy_design_session').can_modify_family_hierarchy()

    def add_root_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.add_root_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('family_hierarchy_design_session').add_root_family(*args, **kwargs)

    def remove_root_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.remove_root_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('family_hierarchy_design_session').remove_root_family(*args, **kwargs)

    def add_child_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.add_child_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('family_hierarchy_design_session').add_child_family(*args, **kwargs)

    def remove_child_family(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.remove_child_family"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('family_hierarchy_design_session').remove_child_family(*args, **kwargs)

    def remove_child_families(self, *args, **kwargs):
        """Pass through to provider FamilyHierarchyDesignSession.remove_child_families"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('family_hierarchy_design_session').remove_child_families(*args, **kwargs)


class RelationshipProxyManager(osid.OsidProxyManager, RelationshipProfile, RelationshipManager, relationship_managers.RelationshipProxyManager):
    """RelationshipProxyManager convenience adapter including related Session methods."""
    pass


class Family(abc_relationship_objects.Family, osid.OsidSession, osid.OsidCatalog):
    """Family convenience adapter including related Session methods."""
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

    def get_family_id(self):
        """Pass through to provider RelationshipLookupSession.get_family_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('relationship_lookup_session').get_family_id()

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Pass through to provider RelationshipLookupSession.get_family"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return Family(
            self._provider_manager,
            self._get_provider_session('relationship_lookup_session').get_family(*args, **kwargs),
            self._runtime,
            self._proxy)

    family = property(fget=get_family)

    def can_lookup_relationships(self):
        """Pass through to provider RelationshipLookupSession.can_lookup_relationships"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('relationship_lookup_session').can_lookup_relationships()

    def use_comparative_relationship_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider RelationshipLookupSession.use_comparative_relationship_view"""
        self._object_views['relationship'] = COMPARATIVE
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_relationship_view()
            except AttributeError:
                pass

    def use_plenary_relationship_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider RelationshipLookupSession.use_plenary_relationship_view"""
        self._object_views['relationship'] = PLENARY
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_relationship_view()
            except AttributeError:
                pass

    def use_federated_family_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_federated_catalog_view
        """Pass through to provider RelationshipLookupSession.use_federated_family_view"""
        self._family_view = FEDERATED
        # self._get_provider_session('relationship_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_family_view()
            except AttributeError:
                pass

    def use_isolated_family_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_isolated_catalog_view
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
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('relationship_lookup_session').get_relationship(*args, **kwargs)

    def get_relationships_by_ids(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_ids(*args, **kwargs)

    def get_relationships_by_genus_type(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_genus_type(*args, **kwargs)

    def get_relationships_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_parent_genus_type(*args, **kwargs)

    def get_relationships_by_record_type(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_record_type(*args, **kwargs)

    def get_relationships_on_date(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_on_date
        return self._get_provider_session('relationship_lookup_session').get_relationships_on_date(*args, **kwargs)

    def get_relationships_for_source(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_source"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_source(*args, **kwargs)

    def get_relationships_for_source_on_date(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_source_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_source_on_date
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_source_on_date(*args, **kwargs)

    def get_relationships_by_genus_type_for_source(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_genus_type_for_source"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_source
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_genus_type_for_source(*args, **kwargs)

    def get_relationships_by_genus_type_for_source_on_date(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_genus_type_for_source_on_date(*args, **kwargs)

    def get_relationships_for_destination(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_destination"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_destination(*args, **kwargs)

    def get_relationships_for_destination_on_date(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_destination_on_date"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_destination_on_date
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_destination_on_date(*args, **kwargs)

    def get_relationships_by_genus_type_for_destination(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_genus_type_for_destination"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_destination
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_genus_type_for_destination(*args, **kwargs)

    def get_relationships_by_genus_type_for_destination_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_for_peers(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_for_peers"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_for_peers
        return self._get_provider_session('relationship_lookup_session').get_relationships_for_peers(*args, **kwargs)

    def get_relationships_for_peers_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships_by_genus_type_for_peers(self, *args, **kwargs):
        """Pass through to provider RelationshipLookupSession.get_relationships_by_genus_type_for_peers"""
        # Built from: templates/osid_session.GenericRelationshipLookupSession.get_relationships_by_genus_type_for_peers
        return self._get_provider_session('relationship_lookup_session').get_relationships_by_genus_type_for_peers(*args, **kwargs)

    def get_relationships_by_genus_type_for_peers_on_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_relationships(self):
        """Pass through to provider RelationshipLookupSession.get_relationships"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('relationship_lookup_session').get_relationships()

    relationships = property(fget=get_relationships)
##
# The following methods are from osid.relationship.RelationshipQuerySession

    def can_search_relationships(self):
        """Pass through to provider RelationshipQuerySession.can_search_relationships"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('relationship_query_session').can_search_relationships()

    def get_relationship_query(self):
        """Pass through to provider RelationshipQuerySession.get_relationship_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('relationship_query_session').get_relationship_query()

    relationship_query = property(fget=get_relationship_query)

    def get_relationships_by_query(self, *args, **kwargs):
        """Pass through to provider RelationshipQuerySession.get_relationships_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('relationship_query_session').get_relationships_by_query(*args, **kwargs)
##
# The following methods are from osid.relationship.RelationshipAdminSession

    def can_create_relationships(self):
        """Pass through to provider RelationshipAdminSession.can_create_relationships"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('relationship_admin_session').can_create_relationships()

    def can_create_relationship_with_record_types(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.can_create_relationship_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('relationship_admin_session').can_create_relationship_with_record_types(*args, **kwargs)

    def get_relationship_form_for_create(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.get_relationship_form_for_create"""
        # Built from: templates/osid_session.GenericRelationshipAdminSession.get_relationship_form_for_create
        return self._get_provider_session('relationship_admin_session').get_relationship_form_for_create(*args, **kwargs)

    def create_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.create_relationship"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('relationship_admin_session').create_relationship(*args, **kwargs)

    def can_update_relationships(self):
        """Pass through to provider RelationshipAdminSession.can_update_relationships"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('relationship_admin_session').can_update_relationships()

    def get_relationship_form_for_update(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.get_relationship_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('relationship_admin_session').get_relationship_form_for_update(*args, **kwargs)

    def update_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.update_relationship"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('relationship_admin_session').update_relationship(*args, **kwargs)

    def can_delete_relationships(self):
        """Pass through to provider RelationshipAdminSession.can_delete_relationships"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('relationship_admin_session').can_delete_relationships()

    def delete_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.delete_relationship"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('relationship_admin_session').delete_relationship(*args, **kwargs)

    def can_manage_relationship_aliases(self):
        """Pass through to provider RelationshipAdminSession.can_manage_relationship_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('relationship_admin_session').can_manage_relationship_aliases()

    def alias_relationship(self, *args, **kwargs):
        """Pass through to provider RelationshipAdminSession.alias_relationship"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('relationship_admin_session').alias_relationship(*args, **kwargs)


class FamilyList(abc_relationship_objects.FamilyList, osid.OsidList):
    """FamilyList convenience adapter including related Session methods."""

    def get_next_family(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(Family)

    __next__ = next

    next_family = property(fget=get_next_family)

    def get_next_families(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(FamilyList, number=n)
