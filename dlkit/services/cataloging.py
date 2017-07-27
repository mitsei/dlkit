"""DLKit Services implementations of cataloging service."""
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
from dlkit.abstract_osid.cataloging import objects as abc_cataloging_objects
from dlkit.manager_impls.cataloging import managers as cataloging_managers


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


class CatalogingProfile(osid.OsidProfile, cataloging_managers.CatalogingProfile):
    """CatalogingProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_catalog_lookup(self):
        """Pass through to provider supports_catalog_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_catalog_lookup()

    def supports_catalog_query(self):
        """Pass through to provider supports_catalog_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_catalog_query()

    def supports_catalog_admin(self):
        """Pass through to provider supports_catalog_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_catalog_admin()

    def supports_catalog_hierarchy(self):
        """Pass through to provider supports_catalog_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_catalog_hierarchy()

    def supports_catalog_hierarchy_design(self):
        """Pass through to provider supports_catalog_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_catalog_hierarchy_design()

    def get_catalog_record_types(self):
        """Pass through to provider get_catalog_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_catalog_record_types()

    catalog_record_types = property(fget=get_catalog_record_types)

    def get_catalog_search_record_types(self):
        """Pass through to provider get_catalog_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_catalog_search_record_types()

    catalog_search_record_types = property(fget=get_catalog_search_record_types)


class CatalogingManager(osid.OsidManager, osid.OsidSession, CatalogingProfile, cataloging_managers.CatalogingManager):
    """CatalogingManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._catalog_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_catalog_view(self, session):
        """Sets the underlying catalog view to match current view"""
        if self._catalog_view == COMPARATIVE:
            try:
                session.use_comparative_catalog_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_catalog_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_catalog_view(session)
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
        parameter_id = Id('parameter:catalogingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('CATALOGING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('CATALOGING', provider_impl)

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

    def get_catalog_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_catalog_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_catalog_lookup_session(*args, **kwargs)

    catalog_lookup_session = property(fget=get_catalog_lookup_session)

    def get_catalog_query_session(self, *args, **kwargs):
        """Pass through to provider get_catalog_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_catalog_query_session(*args, **kwargs)

    catalog_query_session = property(fget=get_catalog_query_session)

    def get_catalog_admin_session(self, *args, **kwargs):
        """Pass through to provider get_catalog_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_catalog_admin_session(*args, **kwargs)

    catalog_admin_session = property(fget=get_catalog_admin_session)

    def get_catalog_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_catalog_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_catalog_hierarchy_session(*args, **kwargs)

    catalog_hierarchy_session = property(fget=get_catalog_hierarchy_session)

    def get_catalog_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_catalog_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_catalog_hierarchy_design_session(*args, **kwargs)

    catalog_hierarchy_design_session = property(fget=get_catalog_hierarchy_design_session)

    def get_cataloging_rules_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    cataloging_rules_manager = property(fget=get_cataloging_rules_manager)
##
# The following methods are from osid.cataloging.CatalogLookupSession

    def can_lookup_catalogs(self):
        """Pass through to provider CatalogLookupSession.can_lookup_catalogs"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('catalog_lookup_session').can_lookup_catalogs()

    def use_comparative_catalog_view(self):
        """Pass through to provider CatalogLookupSession.use_comparative_catalog_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._catalog_view = COMPARATIVE
        # self._get_provider_session('catalog_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_catalog_view()
            except AttributeError:
                pass

    def use_plenary_catalog_view(self):
        """Pass through to provider CatalogLookupSession.use_plenary_catalog_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._catalog_view = PLENARY
        # self._get_provider_session('catalog_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_catalog_view()
            except AttributeError:
                pass

    def get_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogLookupSession.get_catalog"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return Catalog(
            self._provider_manager,
            self._get_provider_session('catalog_lookup_session').get_catalog(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_catalogs_by_ids(self, *args, **kwargs):
        """Pass through to provider CatalogLookupSession.get_catalogs_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('catalog_lookup_session').get_catalogs_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Catalog(self._provider_manager, cat, self._runtime, self._proxy))
        return CatalogList(cat_list)

    def get_catalogs_by_genus_type(self, *args, **kwargs):
        """Pass through to provider CatalogLookupSession.get_catalogs_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('catalog_lookup_session').get_catalogs_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Catalog(self._provider_manager, cat, self._runtime, self._proxy))
        return CatalogList(cat_list)

    def get_catalogs_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider CatalogLookupSession.get_catalogs_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('catalog_lookup_session').get_catalogs_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Catalog(self._provider_manager, cat, self._runtime, self._proxy))
        return CatalogList(cat_list)

    def get_catalogs_by_record_type(self, *args, **kwargs):
        """Pass through to provider CatalogLookupSession.get_catalogs_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('catalog_lookup_session').get_catalogs_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Catalog(self._provider_manager, cat, self._runtime, self._proxy))
        return CatalogList(cat_list)

    def get_catalogs_by_provider(self, *args, **kwargs):
        """Pass through to provider CatalogLookupSession.get_catalogs_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('catalog_lookup_session').get_catalogs_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Catalog(self._provider_manager, cat, self._runtime, self._proxy))
        return CatalogList(cat_list)

    def get_catalogs(self):
        """Pass through to provider CatalogLookupSession.get_catalogs"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
        catalogs = self._get_provider_session('catalog_lookup_session').get_catalogs()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Catalog(self._provider_manager, cat, self._runtime, self._proxy))
        return CatalogList(cat_list)

    catalogs = property(fget=get_catalogs)
##
# The following methods are from osid.cataloging.CatalogQuerySession

    def can_search_catalogs(self):
        """Pass through to provider CatalogQuerySession.can_search_catalogs"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.can_search_catalogs
        return self._get_provider_session('catalog_query_session').can_search_catalogs()

    def get_catalog_query(self):
        """Pass through to provider CatalogQuerySession.get_catalog_query"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.get_catalog_query
        return self._get_provider_session('catalog_query_session').get_catalog_query()

    catalog_query = property(fget=get_catalog_query)

    def get_catalogs_by_query(self, *args, **kwargs):
        """Pass through to provider CatalogQuerySession.get_catalogs_by_query"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.get_catalogs_by_query
        return self._get_provider_session('catalog_query_session').get_catalogs_by_query(*args, **kwargs)
##
# The following methods are from osid.cataloging.CatalogAdminSession

    def can_create_catalogs(self):
        """Pass through to provider CatalogAdminSession.can_create_catalogs"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('catalog_admin_session').can_create_catalogs()

    def can_create_catalog_with_record_types(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.can_create_catalog_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('catalog_admin_session').can_create_catalog_with_record_types(*args, **kwargs)

    def get_catalog_form_for_create(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.get_catalog_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('catalog_admin_session').get_catalog_form_for_create(*args, **kwargs)

    def create_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.create_catalog"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return Catalog(
            self._provider_manager,
            self._get_provider_session('catalog_admin_session').create_catalog(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_catalogs(self):
        """Pass through to provider CatalogAdminSession.can_update_catalogs"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('catalog_admin_session').can_update_catalogs()

    def get_catalog_form_for_update(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.get_catalog_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('catalog_admin_session').get_catalog_form_for_update(*args, **kwargs)

    def update_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.update_catalog"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return Catalog(
            self._provider_manager,
            self._get_provider_session('catalog_admin_session').update_catalog(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_catalogs(self):
        """Pass through to provider CatalogAdminSession.can_delete_catalogs"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('catalog_admin_session').can_delete_catalogs()

    def delete_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.delete_catalog"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('catalog_admin_session').delete_catalog(*args, **kwargs)

    def can_manage_catalog_aliases(self):
        """Pass through to provider CatalogAdminSession.can_manage_catalog_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('catalog_admin_session').can_manage_catalog_aliases()

    def alias_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogAdminSession.alias_catalog"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('catalog_admin_session').alias_catalog(*args, **kwargs)
##
# The following methods are from osid.cataloging.CatalogHierarchySession

    def get_catalog_hierarchy_id(self):
        """Pass through to provider CatalogHierarchySession.get_catalog_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('catalog_hierarchy_session').get_catalog_hierarchy_id()

    catalog_hierarchy_id = property(fget=get_catalog_hierarchy_id)

    def get_catalog_hierarchy(self):
        """Pass through to provider CatalogHierarchySession.get_catalog_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('catalog_hierarchy_session').get_catalog_hierarchy()

    catalog_hierarchy = property(fget=get_catalog_hierarchy)

    def can_access_catalog_hierarchy(self):
        """Pass through to provider CatalogHierarchySession.can_access_catalog_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('catalog_hierarchy_session').can_access_catalog_hierarchy()

    def get_root_catalog_ids(self):
        """Pass through to provider CatalogHierarchySession.get_root_catalog_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('catalog_hierarchy_session').get_root_catalog_ids()

    root_catalog_ids = property(fget=get_root_catalog_ids)

    def get_root_catalogs(self):
        """Pass through to provider CatalogHierarchySession.get_root_catalogs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('catalog_hierarchy_session').get_root_catalogs()

    root_catalogs = property(fget=get_root_catalogs)

    def has_parent_catalogs(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.has_parent_catalogs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('catalog_hierarchy_session').has_parent_catalogs(*args, **kwargs)

    def is_parent_of_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.is_parent_of_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('catalog_hierarchy_session').is_parent_of_catalog(*args, **kwargs)

    def get_parent_catalog_ids(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.get_parent_catalog_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('catalog_hierarchy_session').get_parent_catalog_ids(*args, **kwargs)

    def get_parent_catalogs(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.get_parent_catalogs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('catalog_hierarchy_session').get_parent_catalogs(*args, **kwargs)

    def is_ancestor_of_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.is_ancestor_of_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('catalog_hierarchy_session').is_ancestor_of_catalog(*args, **kwargs)

    def has_child_catalogs(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.has_child_catalogs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('catalog_hierarchy_session').has_child_catalogs(*args, **kwargs)

    def is_child_of_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.is_child_of_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('catalog_hierarchy_session').is_child_of_catalog(*args, **kwargs)

    def get_child_catalog_ids(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.get_child_catalog_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('catalog_hierarchy_session').get_child_catalog_ids(*args, **kwargs)

    def get_child_catalogs(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.get_child_catalogs"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('catalog_hierarchy_session').get_child_catalogs(*args, **kwargs)

    def is_descendant_of_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.is_descendant_of_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('catalog_hierarchy_session').is_descendant_of_catalog(*args, **kwargs)

    def get_catalog_node_ids(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.get_catalog_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('catalog_hierarchy_session').get_catalog_node_ids(*args, **kwargs)

    def get_catalog_nodes(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchySession.get_catalog_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('catalog_hierarchy_session').get_catalog_nodes(*args, **kwargs)
##
# The following methods are from osid.cataloging.CatalogHierarchyDesignSession

    def can_modify_catalog_hierarchy(self):
        """Pass through to provider CatalogHierarchyDesignSession.can_modify_catalog_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('catalog_hierarchy_design_session').can_modify_catalog_hierarchy()

    def add_root_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchyDesignSession.add_root_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('catalog_hierarchy_design_session').add_root_catalog(*args, **kwargs)

    def remove_root_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchyDesignSession.remove_root_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('catalog_hierarchy_design_session').remove_root_catalog(*args, **kwargs)

    def add_child_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchyDesignSession.add_child_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('catalog_hierarchy_design_session').add_child_catalog(*args, **kwargs)

    def remove_child_catalog(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchyDesignSession.remove_child_catalog"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('catalog_hierarchy_design_session').remove_child_catalog(*args, **kwargs)

    def remove_child_catalogs(self, *args, **kwargs):
        """Pass through to provider CatalogHierarchyDesignSession.remove_child_catalogs"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('catalog_hierarchy_design_session').remove_child_catalogs(*args, **kwargs)


class CatalogingProxyManager(osid.OsidProxyManager, CatalogingProfile, CatalogingManager, cataloging_managers.CatalogingProxyManager):
    """CatalogingProxyManager convenience adapter including related Session methods."""
    pass


class Catalog(abc_cataloging_objects.Catalog, osid.OsidSession, osid.OsidCatalog):
    """Catalog convenience adapter including related Session methods."""
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
        self._catalog_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_catalog_view(self, session):
        """Sets the underlying catalog view to match current view"""
        if self._catalog_view == FEDERATED:
            try:
                session.use_federated_catalog_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_catalog_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_catalog')
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
            self._set_catalog_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_catalog_id(self):
        """Gets the Id of this catalog."""
        return self._catalog_id

    def get_catalog(self):
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

    def get_catalog_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class CatalogList(abc_cataloging_objects.CatalogList, osid.OsidList):
    """CatalogList convenience adapter including related Session methods."""

    def get_next_catalog(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(Catalog)

    __next__ = next

    next_catalog = property(fget=get_next_catalog)

    def get_next_catalogs(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(CatalogList, number=n)
