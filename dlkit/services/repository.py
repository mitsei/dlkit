"""DLKit Services implementations of repository service."""
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
from dlkit.abstract_osid.repository import objects as abc_repository_objects
from dlkit.manager_impls.repository import managers as repository_managers


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


class RepositoryProfile(osid.OsidProfile, repository_managers.RepositoryProfile):
    """RepositoryProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_asset_lookup(self):
        """Pass through to provider supports_asset_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_lookup()

    def supports_asset_query(self):
        """Pass through to provider supports_asset_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_query()

    def supports_asset_search(self):
        """Pass through to provider supports_asset_search"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_search()

    def supports_asset_admin(self):
        """Pass through to provider supports_asset_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_admin()

    def supports_asset_notification(self):
        """Pass through to provider supports_asset_notification"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_notification()

    def supports_asset_repository(self):
        """Pass through to provider supports_asset_repository"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_repository()

    def supports_asset_repository_assignment(self):
        """Pass through to provider supports_asset_repository_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_repository_assignment()

    def supports_asset_composition(self):
        """Pass through to provider supports_asset_composition"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_composition()

    def supports_asset_composition_design(self):
        """Pass through to provider supports_asset_composition_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_asset_composition_design()

    def supports_composition_lookup(self):
        """Pass through to provider supports_composition_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_composition_lookup()

    def supports_composition_query(self):
        """Pass through to provider supports_composition_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_composition_query()

    def supports_composition_search(self):
        """Pass through to provider supports_composition_search"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_composition_search()

    def supports_composition_admin(self):
        """Pass through to provider supports_composition_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_composition_admin()

    def supports_composition_repository(self):
        """Pass through to provider supports_composition_repository"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_composition_repository()

    def supports_composition_repository_assignment(self):
        """Pass through to provider supports_composition_repository_assignment"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_composition_repository_assignment()

    def supports_repository_lookup(self):
        """Pass through to provider supports_repository_lookup"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_repository_lookup()

    def supports_repository_query(self):
        """Pass through to provider supports_repository_query"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_repository_query()

    def supports_repository_admin(self):
        """Pass through to provider supports_repository_admin"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_repository_admin()

    def supports_repository_hierarchy(self):
        """Pass through to provider supports_repository_hierarchy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_repository_hierarchy()

    def supports_repository_hierarchy_design(self):
        """Pass through to provider supports_repository_hierarchy_design"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_repository_hierarchy_design()

    def get_asset_record_types(self):
        """Pass through to provider get_asset_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_asset_record_types()

    asset_record_types = property(fget=get_asset_record_types)

    def get_asset_search_record_types(self):
        """Pass through to provider get_asset_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_asset_search_record_types()

    asset_search_record_types = property(fget=get_asset_search_record_types)

    def get_asset_content_record_types(self):
        """Pass through to provider get_asset_content_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_asset_content_record_types()

    asset_content_record_types = property(fget=get_asset_content_record_types)

    def get_composition_record_types(self):
        """Pass through to provider get_composition_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_composition_record_types()

    composition_record_types = property(fget=get_composition_record_types)

    def get_composition_search_record_types(self):
        """Pass through to provider get_composition_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_composition_search_record_types()

    composition_search_record_types = property(fget=get_composition_search_record_types)

    def get_repository_record_types(self):
        """Pass through to provider get_repository_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_repository_record_types()

    repository_record_types = property(fget=get_repository_record_types)

    def get_repository_search_record_types(self):
        """Pass through to provider get_repository_search_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_repository_search_record_types()

    repository_search_record_types = property(fget=get_repository_search_record_types)

    def get_spatial_unit_record_types(self):
        """Pass through to provider get_spatial_unit_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_spatial_unit_record_types()

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    def get_coordinate_types(self):
        """Pass through to provider get_coordinate_types"""
        # Built from: templates/osid_managers.GenericProfile.get_type_list
        return self._provider_manager.get_coordinate_types()

    coordinate_types = property(fget=get_coordinate_types)

    def get_asset_content_lookup_session(self, *args, **kwargs):
        """Pass through to provider """
        return self._provider_manager.get_asset_content_lookup_session(*args, **kwargs)

    asset_content_lookup_session = property(fget=get_asset_content_lookup_session)

    def get_asset_content_lookup_session_for_repository(self, *args, **kwargs):
        """Pass through to provider """
        return self._provider_manager.get_asset_content_lookup_session_for_repository(args, kwargs)


class RepositoryManager(osid.OsidManager, osid.OsidSession, RepositoryProfile, repository_managers.RepositoryManager):
    """RepositoryManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._repository_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_repository_view(self, session):
        """Sets the underlying repository view to match current view"""
        if self._repository_view == COMPARATIVE:
            try:
                session.use_comparative_repository_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_repository_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_repository_view(session)
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
        parameter_id = Id('parameter:repositoryProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('REPOSITORY', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('REPOSITORY', provider_impl)

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

    def get_asset_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_asset_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_asset_lookup_session(*args, **kwargs)

    asset_lookup_session = property(fget=get_asset_lookup_session)

    def get_asset_lookup_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_asset_lookup_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_asset_lookup_session_for_repository(*args, **kwargs)

    def get_asset_query_session(self, *args, **kwargs):
        """Pass through to provider get_asset_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_asset_query_session(*args, **kwargs)

    asset_query_session = property(fget=get_asset_query_session)

    def get_asset_query_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_asset_query_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_asset_query_session_for_repository(*args, **kwargs)

    def get_asset_search_session(self, *args, **kwargs):
        """Pass through to provider get_asset_search_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_asset_search_session(*args, **kwargs)

    asset_search_session = property(fget=get_asset_search_session)

    def get_asset_search_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_asset_search_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_asset_search_session_for_repository(*args, **kwargs)

    def get_asset_admin_session(self, *args, **kwargs):
        """Pass through to provider get_asset_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_asset_admin_session(*args, **kwargs)

    asset_admin_session = property(fget=get_asset_admin_session)

    def get_asset_admin_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_asset_admin_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_asset_admin_session_for_repository(*args, **kwargs)

    def get_asset_notification_session(self, *args, **kwargs):
        """Pass through to provider get_asset_notification_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_notification_session
        return self._provider_manager.get_asset_notification_session(*args, **kwargs)

    def get_asset_notification_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_asset_notification_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_notification_session_for_catalog
        return self._provider_manager.get_asset_notification_session_for_repository(*args, **kwargs)

    def get_asset_repository_session(self, *args, **kwargs):
        """Pass through to provider get_asset_repository_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_asset_repository_session(*args, **kwargs)

    asset_repository_session = property(fget=get_asset_repository_session)

    def get_asset_repository_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_asset_repository_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_asset_repository_assignment_session(*args, **kwargs)

    asset_repository_assignment_session = property(fget=get_asset_repository_assignment_session)

    def get_asset_composition_session(self, *args, **kwargs):
        """Pass through to provider get_asset_composition_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_asset_composition_session(*args, **kwargs)

    asset_composition_session = property(fget=get_asset_composition_session)

    def get_asset_composition_design_session(self, *args, **kwargs):
        """Pass through to provider get_asset_composition_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_asset_composition_design_session(*args, **kwargs)

    asset_composition_design_session = property(fget=get_asset_composition_design_session)

    def get_composition_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_composition_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_composition_lookup_session(*args, **kwargs)

    composition_lookup_session = property(fget=get_composition_lookup_session)

    def get_composition_lookup_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_composition_lookup_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_composition_lookup_session_for_repository(*args, **kwargs)

    def get_composition_query_session(self, *args, **kwargs):
        """Pass through to provider get_composition_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session
        return self._provider_manager.get_composition_query_session(*args, **kwargs)

    composition_query_session = property(fget=get_composition_query_session)

    def get_composition_query_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_composition_query_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_lookup_session_for_catalog
        return self._provider_manager.get_composition_query_session_for_repository(*args, **kwargs)

    def get_composition_search_session(self, *args, **kwargs):
        """Pass through to provider get_composition_search_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_composition_search_session(*args, **kwargs)

    composition_search_session = property(fget=get_composition_search_session)

    def get_composition_search_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_composition_search_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_composition_search_session_for_repository(*args, **kwargs)

    def get_composition_admin_session(self, *args, **kwargs):
        """Pass through to provider get_composition_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_composition_admin_session(*args, **kwargs)

    composition_admin_session = property(fget=get_composition_admin_session)

    def get_composition_admin_session_for_repository(self, *args, **kwargs):
        """Pass through to provider get_composition_admin_session_for_repository"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session_for_catalog
        return self._provider_manager.get_composition_admin_session_for_repository(*args, **kwargs)

    def get_composition_repository_session(self, *args, **kwargs):
        """Pass through to provider get_composition_repository_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_composition_repository_session(*args, **kwargs)

    composition_repository_session = property(fget=get_composition_repository_session)

    def get_composition_repository_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_composition_repository_assignment_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_composition_repository_assignment_session(*args, **kwargs)

    composition_repository_assignment_session = property(fget=get_composition_repository_assignment_session)

    def get_repository_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_repository_lookup_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_repository_lookup_session(*args, **kwargs)

    repository_lookup_session = property(fget=get_repository_lookup_session)

    def get_repository_query_session(self, *args, **kwargs):
        """Pass through to provider get_repository_query_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_repository_query_session(*args, **kwargs)

    repository_query_session = property(fget=get_repository_query_session)

    def get_repository_admin_session(self, *args, **kwargs):
        """Pass through to provider get_repository_admin_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_repository_admin_session(*args, **kwargs)

    repository_admin_session = property(fget=get_repository_admin_session)

    def get_repository_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_repository_hierarchy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_repository_hierarchy_session(*args, **kwargs)

    repository_hierarchy_session = property(fget=get_repository_hierarchy_session)

    def get_repository_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_repository_hierarchy_design_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_repository_hierarchy_design_session(*args, **kwargs)

    repository_hierarchy_design_session = property(fget=get_repository_hierarchy_design_session)

    def get_repository_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    repository_batch_manager = property(fget=get_repository_batch_manager)

    def get_repository_rules_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    repository_rules_manager = property(fget=get_repository_rules_manager)
##
# The following methods are from osid.repository.AssetRepositorySession

    def can_lookup_asset_repository_mappings(self):
        """Pass through to provider AssetRepositorySession.can_lookup_asset_repository_mappings"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.can_lookup_object_catalog_mappings
        return self._get_provider_session('asset_repository_session').can_lookup_asset_repository_mappings()

    def use_comparative_repository_view(self):
        """Pass through to provider AssetRepositorySession.use_comparative_repository_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._repository_view = COMPARATIVE
        # self._get_provider_session('asset_repository_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_repository_view()
            except AttributeError:
                pass

    def use_plenary_repository_view(self):
        """Pass through to provider AssetRepositorySession.use_plenary_repository_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._repository_view = PLENARY
        # self._get_provider_session('asset_repository_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_repository_view()
            except AttributeError:
                pass

    def get_asset_ids_by_repository(self, *args, **kwargs):
        """Pass through to provider AssetRepositorySession.get_asset_ids_by_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalog
        return self._get_provider_session('asset_repository_session').get_asset_ids_by_repository(*args, **kwargs)

    def get_assets_by_repository(self, *args, **kwargs):
        """Pass through to provider AssetRepositorySession.get_assets_by_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalog
        return self._get_provider_session('asset_repository_session').get_assets_by_repository(*args, **kwargs)

    def get_asset_ids_by_repositories(self, *args, **kwargs):
        """Pass through to provider AssetRepositorySession.get_asset_ids_by_repositories"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalogs
        return self._get_provider_session('asset_repository_session').get_asset_ids_by_repositories(*args, **kwargs)

    def get_assets_by_repositories(self, *args, **kwargs):
        """Pass through to provider AssetRepositorySession.get_assets_by_repositories"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalogs
        return self._get_provider_session('asset_repository_session').get_assets_by_repositories(*args, **kwargs)

    def get_repository_ids_by_asset(self, *args, **kwargs):
        """Pass through to provider AssetRepositorySession.get_repository_ids_by_asset"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalog_ids_by_object
        return self._get_provider_session('asset_repository_session').get_repository_ids_by_asset(*args, **kwargs)

    def get_repositories_by_asset(self, *args, **kwargs):
        """Pass through to provider AssetRepositorySession.get_repositories_by_asset"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalogs_by_object
        catalogs = self._get_provider_session('asset_repository_session').get_repositories_by_asset(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)
##
# The following methods are from osid.repository.AssetRepositoryAssignmentSession

    def can_assign_assets(self):
        """Pass through to provider AssetRepositoryAssignmentSession.can_assign_assets"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects
        return self._get_provider_session('asset_repository_assignment_session').can_assign_assets()

    def can_assign_assets_to_repository(self, *args, **kwargs):
        """Pass through to provider AssetRepositoryAssignmentSession.can_assign_assets_to_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects_to_catalog
        return self._get_provider_session('asset_repository_assignment_session').can_assign_assets_to_repository(*args, **kwargs)

    def get_assignable_repository_ids(self, *args, **kwargs):
        """Pass through to provider AssetRepositoryAssignmentSession.get_assignable_repository_ids"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids
        return self._get_provider_session('asset_repository_assignment_session').get_assignable_repository_ids(*args, **kwargs)

    def get_assignable_repository_ids_for_asset(self, *args, **kwargs):
        """Pass through to provider AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids_for_object
        return self._get_provider_session('asset_repository_assignment_session').get_assignable_repository_ids_for_asset(*args, **kwargs)

    def assign_asset_to_repository(self, *args, **kwargs):
        """Pass through to provider AssetRepositoryAssignmentSession.assign_asset_to_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.assign_object_to_catalog
        self._get_provider_session('asset_repository_assignment_session').assign_asset_to_repository(*args, **kwargs)

    def unassign_asset_from_repository(self, *args, **kwargs):
        """Pass through to provider AssetRepositoryAssignmentSession.unassign_asset_from_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.unassign_object_from_catalog
        self._get_provider_session('asset_repository_assignment_session').unassign_asset_from_repository(*args, **kwargs)
##
# The following methods are from osid.repository.CompositionRepositorySession

    def use_comparative_composition_repository_view(self):
        """Pass through to provider CompositionRepositorySession.use_comparative_composition_repository_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_comparative_catalog_view
        self._repository_view = COMPARATIVE
        # self._get_provider_session('composition_repository_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_composition_repository_view()
            except AttributeError:
                pass

    def use_plenary_composition_repository_view(self):
        """Pass through to provider CompositionRepositorySession.use_plenary_composition_repository_view"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.use_plenary_catalog_view
        self._repository_view = PLENARY
        # self._get_provider_session('composition_repository_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_composition_repository_view()
            except AttributeError:
                pass

    def can_lookup_composition_repository_mappings(self):
        """Pass through to provider CompositionRepositorySession.can_lookup_composition_repository_mappings"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.can_lookup_object_catalog_mappings
        return self._get_provider_session('composition_repository_session').can_lookup_composition_repository_mappings()

    def get_composition_ids_by_repository(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_composition_ids_by_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalog
        return self._get_provider_session('composition_repository_session').get_composition_ids_by_repository(*args, **kwargs)

    def get_compositions_by_repository(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_compositions_by_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalog
        return self._get_provider_session('composition_repository_session').get_compositions_by_repository(*args, **kwargs)

    def get_composition_ids_by_repositories(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_composition_ids_by_repositories"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_object_ids_by_catalogs
        return self._get_provider_session('composition_repository_session').get_composition_ids_by_repositories(*args, **kwargs)

    def get_compositions_by_repositories(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_compositions_by_repositories"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_objects_by_catalogs
        return self._get_provider_session('composition_repository_session').get_compositions_by_repositories(*args, **kwargs)

    def get_repository_ids_by_composition(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_repository_ids_by_composition"""
        # Not templated -- check the hand-built implementations
        return self._get_provider_session('composition_repository_session').get_repository_ids_by_composition(*args, **kwargs)

    def get_repositories_by_composition(self, *args, **kwargs):
        """Pass through to provider CompositionRepositorySession.get_repositories_by_composition"""
        # Built from: templates/osid_session.GenericObjectCatalogSession.get_catalogs_by_object
        catalogs = self._get_provider_session('composition_repository_session').get_repositories_by_composition(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)
##
# The following methods are from osid.repository.CompositionRepositoryAssignmentSession

    def can_assign_compositions(self):
        """Pass through to provider CompositionRepositoryAssignmentSession.can_assign_compositions"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects
        return self._get_provider_session('composition_repository_assignment_session').can_assign_compositions()

    def can_assign_compositions_to_repository(self, *args, **kwargs):
        """Pass through to provider CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.can_assign_objects_to_catalog
        return self._get_provider_session('composition_repository_assignment_session').can_assign_compositions_to_repository(*args, **kwargs)

    def get_assignable_repository_ids_for_composition(self, *args, **kwargs):
        """Pass through to provider CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.get_assignable_catalog_ids_for_object
        return self._get_provider_session('composition_repository_assignment_session').get_assignable_repository_ids_for_composition(*args, **kwargs)

    def assign_composition_to_repository(self, *args, **kwargs):
        """Pass through to provider CompositionRepositoryAssignmentSession.assign_composition_to_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.assign_object_to_catalog
        self._get_provider_session('composition_repository_assignment_session').assign_composition_to_repository(*args, **kwargs)

    def unassign_composition_from_repository(self, *args, **kwargs):
        """Pass through to provider CompositionRepositoryAssignmentSession.unassign_composition_from_repository"""
        # Built from: templates/osid_session.GenericObjectCatalogAssignmentSession.unassign_object_from_catalog
        self._get_provider_session('composition_repository_assignment_session').unassign_composition_from_repository(*args, **kwargs)
##
# The following methods are from osid.repository.RepositoryLookupSession

    def can_lookup_repositories(self):
        """Pass through to provider RepositoryLookupSession.can_lookup_repositories"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.can_lookup_catalogs
        return self._get_provider_session('repository_lookup_session').can_lookup_repositories()

    def get_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryLookupSession.get_repository"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalog
        return Repository(
            self._provider_manager,
            self._get_provider_session('repository_lookup_session').get_repository(*args, **kwargs),
            self._runtime,
            self._proxy)

    def get_repositories_by_ids(self, *args, **kwargs):
        """Pass through to provider RepositoryLookupSession.get_repositories_by_ids"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_ids
        catalogs = self._get_provider_session('repository_lookup_session').get_repositories_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)

    def get_repositories_by_genus_type(self, *args, **kwargs):
        """Pass through to provider RepositoryLookupSession.get_repositories_by_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_genus_type
        catalogs = self._get_provider_session('repository_lookup_session').get_repositories_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)

    def get_repositories_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider RepositoryLookupSession.get_repositories_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_parent_genus_type
        catalogs = self._get_provider_session('repository_lookup_session').get_repositories_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)

    def get_repositories_by_record_type(self, *args, **kwargs):
        """Pass through to provider RepositoryLookupSession.get_repositories_by_record_type"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_record_type
        catalogs = self._get_provider_session('repository_lookup_session').get_repositories_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)

    def get_repositories_by_provider(self, *args, **kwargs):
        """Pass through to provider RepositoryLookupSession.get_repositories_by_provider"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs_by_provider
        catalogs = self._get_provider_session('repository_lookup_session').get_repositories_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)

    def get_repositories(self):
        """Pass through to provider RepositoryLookupSession.get_repositories"""
        # Built from: templates/osid_session.GenericCatalogLookupSession.get_catalogs
        catalogs = self._get_provider_session('repository_lookup_session').get_repositories()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Repository(self._provider_manager, cat, self._runtime, self._proxy))
        return RepositoryList(cat_list)

    repositories = property(fget=get_repositories)
##
# The following methods are from osid.repository.RepositoryQuerySession

    def can_search_repositories(self):
        """Pass through to provider RepositoryQuerySession.can_search_repositories"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.can_search_catalogs
        return self._get_provider_session('repository_query_session').can_search_repositories()

    def get_repository_query(self):
        """Pass through to provider RepositoryQuerySession.get_repository_query"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.get_catalog_query
        return self._get_provider_session('repository_query_session').get_repository_query()

    repository_query = property(fget=get_repository_query)

    def get_repositories_by_query(self, *args, **kwargs):
        """Pass through to provider RepositoryQuerySession.get_repositories_by_query"""
        # Built from: templates/osid_session.GenericCatalogQuerySession.get_catalogs_by_query
        return self._get_provider_session('repository_query_session').get_repositories_by_query(*args, **kwargs)
##
# The following methods are from osid.repository.RepositoryAdminSession

    def can_create_repositories(self):
        """Pass through to provider RepositoryAdminSession.can_create_repositories"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalogs
        return self._get_provider_session('repository_admin_session').can_create_repositories()

    def can_create_repository_with_record_types(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.can_create_repository_with_record_types"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_create_catalog_with_record_types
        return self._get_provider_session('repository_admin_session').can_create_repository_with_record_types(*args, **kwargs)

    def get_repository_form_for_create(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.get_repository_form_for_create"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_create
        return self._get_provider_session('repository_admin_session').get_repository_form_for_create(*args, **kwargs)

    def create_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.create_repository"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.create_catalog
        return Repository(
            self._provider_manager,
            self._get_provider_session('repository_admin_session').create_repository(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_update_repositories(self):
        """Pass through to provider RepositoryAdminSession.can_update_repositories"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_update_catalogs
        return self._get_provider_session('repository_admin_session').can_update_repositories()

    def get_repository_form_for_update(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.get_repository_form_for_update"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.get_catalog_form_for_update
        return self._get_provider_session('repository_admin_session').get_repository_form_for_update(*args, **kwargs)

    def update_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.update_repository"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.update_catalog
        return Repository(
            self._provider_manager,
            self._get_provider_session('repository_admin_session').update_repository(*args, **kwargs),
            self._runtime,
            self._proxy)

    def can_delete_repositories(self):
        """Pass through to provider RepositoryAdminSession.can_delete_repositories"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.can_delete_catalogs
        return self._get_provider_session('repository_admin_session').can_delete_repositories()

    def delete_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.delete_repository"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.delete_catalog
        self._get_provider_session('repository_admin_session').delete_repository(*args, **kwargs)

    def can_manage_repository_aliases(self):
        """Pass through to provider RepositoryAdminSession.can_manage_repository_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('repository_admin_session').can_manage_repository_aliases()

    def alias_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryAdminSession.alias_repository"""
        # Built from: templates/osid_session.GenericCatalogAdminSession.alias_catalog
        self._get_provider_session('repository_admin_session').alias_repository(*args, **kwargs)
##
# The following methods are from osid.repository.RepositoryHierarchySession

    def get_repository_hierarchy_id(self):
        """Pass through to provider RepositoryHierarchySession.get_repository_hierarchy_id"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy_id
        return self._get_provider_session('repository_hierarchy_session').get_repository_hierarchy_id()

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Pass through to provider RepositoryHierarchySession.get_repository_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_hierarchy
        return self._get_provider_session('repository_hierarchy_session').get_repository_hierarchy()

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_access_repository_hierarchy(self):
        """Pass through to provider RepositoryHierarchySession.can_access_repository_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.can_access_catalog_hierarchy
        return self._get_provider_session('repository_hierarchy_session').can_access_repository_hierarchy()

    def get_root_repository_ids(self):
        """Pass through to provider RepositoryHierarchySession.get_root_repository_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalog_ids
        return self._get_provider_session('repository_hierarchy_session').get_root_repository_ids()

    root_repository_ids = property(fget=get_root_repository_ids)

    def get_root_repositories(self):
        """Pass through to provider RepositoryHierarchySession.get_root_repositories"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_root_catalogs
        return self._get_provider_session('repository_hierarchy_session').get_root_repositories()

    root_repositories = property(fget=get_root_repositories)

    def has_parent_repositories(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.has_parent_repositories"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_parent_catalogs
        return self._get_provider_session('repository_hierarchy_session').has_parent_repositories(*args, **kwargs)

    def is_parent_of_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.is_parent_of_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_parent_of_catalog
        return self._get_provider_session('repository_hierarchy_session').is_parent_of_repository(*args, **kwargs)

    def get_parent_repository_ids(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.get_parent_repository_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalog_ids
        return self._get_provider_session('repository_hierarchy_session').get_parent_repository_ids(*args, **kwargs)

    def get_parent_repositories(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.get_parent_repositories"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_parent_catalogs
        return self._get_provider_session('repository_hierarchy_session').get_parent_repositories(*args, **kwargs)

    def is_ancestor_of_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.is_ancestor_of_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_ancestor_of_catalog
        return self._get_provider_session('repository_hierarchy_session').is_ancestor_of_repository(*args, **kwargs)

    def has_child_repositories(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.has_child_repositories"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.has_child_catalogs
        return self._get_provider_session('repository_hierarchy_session').has_child_repositories(*args, **kwargs)

    def is_child_of_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.is_child_of_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_child_of_catalog
        return self._get_provider_session('repository_hierarchy_session').is_child_of_repository(*args, **kwargs)

    def get_child_repository_ids(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.get_child_repository_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalog_ids
        return self._get_provider_session('repository_hierarchy_session').get_child_repository_ids(*args, **kwargs)

    def get_child_repositories(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.get_child_repositories"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_child_catalogs
        return self._get_provider_session('repository_hierarchy_session').get_child_repositories(*args, **kwargs)

    def is_descendant_of_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.is_descendant_of_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.is_descendant_of_catalog
        return self._get_provider_session('repository_hierarchy_session').is_descendant_of_repository(*args, **kwargs)

    def get_repository_node_ids(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.get_repository_node_ids"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_node_ids
        return self._get_provider_session('repository_hierarchy_session').get_repository_node_ids(*args, **kwargs)

    def get_repository_nodes(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchySession.get_repository_nodes"""
        # Built from: templates/osid_session.GenericCatalogHierarchySession.get_catalog_nodes
        return self._get_provider_session('repository_hierarchy_session').get_repository_nodes(*args, **kwargs)
##
# The following methods are from osid.repository.RepositoryHierarchyDesignSession

    def can_modify_repository_hierarchy(self):
        """Pass through to provider RepositoryHierarchyDesignSession.can_modify_repository_hierarchy"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.can_modify_catalog_hierarchy
        return self._get_provider_session('repository_hierarchy_design_session').can_modify_repository_hierarchy()

    def add_root_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchyDesignSession.add_root_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_root_catalog
        self._get_provider_session('repository_hierarchy_design_session').add_root_repository(*args, **kwargs)

    def remove_root_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchyDesignSession.remove_root_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_root_catalog
        self._get_provider_session('repository_hierarchy_design_session').remove_root_repository(*args, **kwargs)

    def add_child_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchyDesignSession.add_child_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.add_child_catalog
        self._get_provider_session('repository_hierarchy_design_session').add_child_repository(*args, **kwargs)

    def remove_child_repository(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchyDesignSession.remove_child_repository"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalog
        self._get_provider_session('repository_hierarchy_design_session').remove_child_repository(*args, **kwargs)

    def remove_child_repositories(self, *args, **kwargs):
        """Pass through to provider RepositoryHierarchyDesignSession.remove_child_repositories"""
        # Built from: templates/osid_session.GenericCatalogHierarchyDesignSession.remove_child_catalogs
        self._get_provider_session('repository_hierarchy_design_session').remove_child_repositories(*args, **kwargs)


class RepositoryProxyManager(osid.OsidProxyManager, RepositoryProfile, RepositoryManager, repository_managers.RepositoryProxyManager):
    """RepositoryProxyManager convenience adapter including related Session methods."""
    pass


class Repository(abc_repository_objects.Repository, osid.OsidSession, osid.OsidCatalog):
    """Repository convenience adapter including related Session methods."""
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
        self._repository_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_repository_view(self, session):
        """Sets the underlying repository view to match current view"""
        if self._repository_view == FEDERATED:
            try:
                session.use_federated_repository_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_repository_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_repository')
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
            self._set_repository_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_repository_id(self):
        """Gets the Id of this repository."""
        return self._catalog_id

    def get_repository(self):
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

    def get_repository_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.repository.AssetLookupSession

    def get_repository_id(self):
        """Pass through to provider AssetLookupSession.get_repository_id"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog_id
        return self._get_provider_session('asset_lookup_session').get_repository_id()

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Pass through to provider AssetLookupSession.get_repository"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_catalog
        return Repository(
            self._provider_manager,
            self._get_provider_session('asset_lookup_session').get_repository(*args, **kwargs),
            self._runtime,
            self._proxy)

    repository = property(fget=get_repository)

    def can_lookup_assets(self):
        """Pass through to provider AssetLookupSession.can_lookup_assets"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('asset_lookup_session').can_lookup_assets()

    def use_comparative_asset_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider AssetLookupSession.use_comparative_asset_view"""
        self._object_views['asset'] = COMPARATIVE
        # self._get_provider_session('asset_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_asset_view()
            except AttributeError:
                pass

    def use_plenary_asset_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider AssetLookupSession.use_plenary_asset_view"""
        self._object_views['asset'] = PLENARY
        # self._get_provider_session('asset_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_asset_view()
            except AttributeError:
                pass

    def use_federated_repository_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_federated_catalog_view
        """Pass through to provider AssetLookupSession.use_federated_repository_view"""
        self._repository_view = FEDERATED
        # self._get_provider_session('asset_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_federated_repository_view()
            except AttributeError:
                pass

    def use_isolated_repository_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_isolated_catalog_view
        """Pass through to provider AssetLookupSession.use_isolated_repository_view"""
        self._repository_view = ISOLATED
        # self._get_provider_session('asset_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_isolated_repository_view()
            except AttributeError:
                pass

    def get_asset(self, *args, **kwargs):
        """Pass through to provider AssetLookupSession.get_asset"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('asset_lookup_session').get_asset(*args, **kwargs)

    def get_assets_by_ids(self, *args, **kwargs):
        """Pass through to provider AssetLookupSession.get_assets_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('asset_lookup_session').get_assets_by_ids(*args, **kwargs)

    def get_assets_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetLookupSession.get_assets_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('asset_lookup_session').get_assets_by_genus_type(*args, **kwargs)

    def get_assets_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetLookupSession.get_assets_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('asset_lookup_session').get_assets_by_parent_genus_type(*args, **kwargs)

    def get_assets_by_record_type(self, *args, **kwargs):
        """Pass through to provider AssetLookupSession.get_assets_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('asset_lookup_session').get_assets_by_record_type(*args, **kwargs)

    def get_assets_by_provider(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assets(self):
        """Pass through to provider AssetLookupSession.get_assets"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('asset_lookup_session').get_assets()

    assets = property(fget=get_assets)
##
# The following methods are from osid.repository.AssetQuerySession

    def can_search_assets(self):
        """Pass through to provider AssetQuerySession.can_search_assets"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('asset_query_session').can_search_assets()

    def get_asset_query(self):
        """Pass through to provider AssetQuerySession.get_asset_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('asset_query_session').get_asset_query()

    asset_query = property(fget=get_asset_query)

    def get_assets_by_query(self, *args, **kwargs):
        """Pass through to provider AssetQuerySession.get_assets_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('asset_query_session').get_assets_by_query(*args, **kwargs)
##
# The following methods are from osid.repository.AssetSearchSession

    def get_asset_search(self):
        """Pass through to provider AssetSearchSession.get_asset_search"""
        # Built from: templates/osid_session.GenericObjectSearchSession.get_object_search
        return self._get_provider_session('asset_search_session').get_asset_search()

    asset_search = property(fget=get_asset_search)

    def get_asset_search_order(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    asset_search_order = property(fget=get_asset_search_order)

    def get_assets_by_search(self, *args, **kwargs):
        """Pass through to provider AssetSearchSession.get_assets_by_search"""
        # Built from: templates/osid_session.GenericObjectSearchSession.get_objects_by_search
        return self._get_provider_session('asset_search_session').get_assets_by_search(*args, **kwargs)

    def get_asset_query_from_inspector(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.repository.AssetAdminSession

    def can_create_assets(self):
        """Pass through to provider AssetAdminSession.can_create_assets"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('asset_admin_session').can_create_assets()

    def can_create_asset_with_record_types(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.can_create_asset_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('asset_admin_session').can_create_asset_with_record_types(*args, **kwargs)

    def get_asset_form_for_create(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.get_asset_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_create
        return self._get_provider_session('asset_admin_session').get_asset_form_for_create(*args, **kwargs)

    def create_asset(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.create_asset"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('asset_admin_session').create_asset(*args, **kwargs)

    def can_update_assets(self):
        """Pass through to provider AssetAdminSession.can_update_assets"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('asset_admin_session').can_update_assets()

    def get_asset_form_for_update(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.get_asset_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('asset_admin_session').get_asset_form_for_update(*args, **kwargs)

    def update_asset(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.update_asset"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('asset_admin_session').update_asset(*args, **kwargs)

    def can_delete_assets(self):
        """Pass through to provider AssetAdminSession.can_delete_assets"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('asset_admin_session').can_delete_assets()

    def delete_asset(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.delete_asset"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('asset_admin_session').delete_asset(*args, **kwargs)

    def can_manage_asset_aliases(self):
        """Pass through to provider AssetAdminSession.can_manage_asset_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('asset_admin_session').can_manage_asset_aliases()

    def alias_asset(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.alias_asset"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('asset_admin_session').alias_asset(*args, **kwargs)

    def can_create_asset_content(self):
        """Pass through to provider AssetAdminSession.can_create_asset_content"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('asset_admin_session').can_create_asset_content()

    def can_create_asset_content_with_record_types(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.can_create_asset_content_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('asset_admin_session').can_create_asset_content_with_record_types(*args, **kwargs)

    def get_asset_content_form_for_create(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.get_asset_content_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_subjugated_object_form_for_create
        return self._get_provider_session('asset_admin_session').get_asset_content_form_for_create(*args, **kwargs)

    def create_asset_content(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.create_asset_content"""
        # Built from: templates/osid_session.GenericDependentObjectAdminSession.create_dependent_object
        return self._get_provider_session('asset_admin_session').create_asset_content(*args, **kwargs)

    def can_update_asset_contents(self):
        """Pass through to provider AssetAdminSession.can_update_asset_contents"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('asset_admin_session').can_update_asset_contents()

    def get_asset_content_form_for_update(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.get_asset_content_form_for_update"""
        # Built from: templates/osid_session.GenericDependentObjectAdminSession.get_dependent_object_form_for_update
        return self._get_provider_session('asset_admin_session').get_asset_content_form_for_update(*args, **kwargs)

    def update_asset_content(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.update_asset_content"""
        # Built from: templates/osid_session.GenericDependentObjectAdminSession.update_dependent_object
        return self._get_provider_session('asset_admin_session').update_asset_content(*args, **kwargs)

    def can_delete_asset_contents(self):
        """Pass through to provider AssetAdminSession.can_delete_asset_contents"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('asset_admin_session').can_delete_asset_contents()

    def delete_asset_content(self, *args, **kwargs):
        """Pass through to provider AssetAdminSession.delete_asset_content"""
        # Built from: templates/osid_session.GenericDependentObjectAdminSession.delete_dependent_object
        self._get_provider_session('asset_admin_session').delete_asset_content(*args, **kwargs)

    # This is out of spec, but used by the EdX / LORE record extensions...
    def duplicate_asset(self, asset_id):
        return self._get_provider_session('asset_admin_session').duplicate_asset(asset_id)
##
# The following methods are from osid.repository.AssetNotificationSession

    def can_register_for_asset_notifications(self):
        """Pass through to provider AssetNotificationSession.can_register_for_asset_notifications"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.can_register_for_object_notifications
        return self._get_provider_session('asset_notification_session').can_register_for_asset_notifications()

    def register_for_new_assets(self):
        """Pass through to provider AssetNotificationSession.register_for_new_assets"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_new_objects
        self._get_provider_session('asset_notification_session').register_for_new_assets()

    def register_for_new_assets_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetNotificationSession.register_for_new_assets_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_object
        self._get_provider_session('asset_notification_session').register_for_new_assets_by_genus_type(*args, **kwargs)

    def register_for_changed_assets(self):
        """Pass through to provider AssetNotificationSession.register_for_changed_assets"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_objects
        self._get_provider_session('asset_notification_session').register_for_changed_assets()

    def register_for_changed_assets_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetNotificationSession.register_for_changed_assets_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_object
        self._get_provider_session('asset_notification_session').register_for_changed_assets_by_genus_type(*args, **kwargs)

    def register_for_changed_asset(self, *args, **kwargs):
        """Pass through to provider AssetNotificationSession.register_for_changed_asset"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_object
        self._get_provider_session('asset_notification_session').register_for_changed_asset(*args, **kwargs)

    def register_for_deleted_assets(self):
        """Pass through to provider AssetNotificationSession.register_for_deleted_assets"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_deleted_objects
        self._get_provider_session('asset_notification_session').register_for_deleted_assets()

    def register_for_deleted_assets_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetNotificationSession.register_for_deleted_assets_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_changed_object
        self._get_provider_session('asset_notification_session').register_for_deleted_assets_by_genus_type(*args, **kwargs)

    def register_for_deleted_asset(self, *args, **kwargs):
        """Pass through to provider AssetNotificationSession.register_for_deleted_asset"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.register_for_deleted_object
        self._get_provider_session('asset_notification_session').register_for_deleted_asset(*args, **kwargs)

    def reliable_asset_notifications(self):
        """Pass through to provider AssetNotificationSession.reliable_asset_notifications"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.reliable_object_notifications
        self._get_provider_session('asset_notification_session').reliable_asset_notifications()

    def unreliable_asset_notifications(self):
        """Pass through to provider AssetNotificationSession.unreliable_asset_notifications"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.unreliable_object_notifications
        self._get_provider_session('asset_notification_session').unreliable_asset_notifications()

    def acknowledge_asset_notification(self, *args, **kwargs):
        """Pass through to provider AssetNotificationSession.acknowledge_asset_notification"""
        # Built from: templates/osid_session.GenericObjectNotificationSession.acknowledge_object_notification
        self._get_provider_session('asset_notification_session').acknowledge_asset_notification(*args, **kwargs)
##
# The following methods are from osid.repository.AssetCompositionSession

    def can_access_asset_compositions(self):
        """Pass through to provider AssetCompositionSession.can_access_asset_compositions"""
        # Built from: templates/osid_session.GenericObjectContainableSession.can_access_object_containables
        return self._get_provider_session('asset_composition_session').can_access_asset_compositions()

    def use_comparative_asset_composition_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider AssetCompositionSession.use_comparative_asset_composition_view"""
        self._object_views['asset_composition'] = COMPARATIVE
        # self._get_provider_session('asset_composition_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_asset_composition_view()
            except AttributeError:
                pass

    def use_plenary_asset_composition_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider AssetCompositionSession.use_plenary_asset_composition_view"""
        self._object_views['asset_composition'] = PLENARY
        # self._get_provider_session('asset_composition_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_asset_composition_view()
            except AttributeError:
                pass

    def get_composition_assets(self, *args, **kwargs):
        """Pass through to provider AssetCompositionSession.get_composition_assets"""
        # Built from: templates/osid_session.GenericObjectContainableSession.get_containable_objects
        return self._get_provider_session('asset_composition_session').get_composition_assets(*args, **kwargs)

    def get_compositions_by_asset(self, *args, **kwargs):
        """Pass through to provider AssetCompositionSession.get_compositions_by_asset"""
        # Built from: templates/osid_session.GenericObjectContainableSession.get_containables_by_object
        return self._get_provider_session('asset_composition_session').get_compositions_by_asset(*args, **kwargs)
##
# The following methods are from osid.repository.AssetCompositionDesignSession

    def can_compose_assets(self):
        """Pass through to provider AssetCompositionDesignSession.can_compose_assets"""
        # Built from: templates/osid_session.GenericObjectContainableDesignSession.can_compose_objects
        return self._get_provider_session('asset_composition_design_session').can_compose_assets()

    def add_asset(self, *args, **kwargs):
        """Pass through to provider AssetCompositionDesignSession.add_asset"""
        # Built from: templates/osid_session.GenericObjectContainableDesignSession.add_object_to_containable
        return self._get_provider_session('asset_composition_design_session').add_asset(*args, **kwargs)

    def move_asset_ahead(self, *args, **kwargs):
        """Pass through to provider AssetCompositionDesignSession.move_asset_ahead"""
        # Built from: templates/osid_session.GenericObjectContainableDesignSession.move_object_ahead
        return self._get_provider_session('asset_composition_design_session').move_asset_ahead(*args, **kwargs)

    def move_asset_behind(self, *args, **kwargs):
        """Pass through to provider AssetCompositionDesignSession.move_asset_behind"""
        # Built from: templates/osid_session.GenericObjectContainableDesignSession.move_object_behind
        return self._get_provider_session('asset_composition_design_session').move_asset_behind(*args, **kwargs)

    def order_assets(self, *args, **kwargs):
        """Pass through to provider AssetCompositionDesignSession.order_assets"""
        # Built from: templates/osid_session.GenericObjectContainableDesignSession.order_objects
        return self._get_provider_session('asset_composition_design_session').order_assets(*args, **kwargs)

    def remove_asset(self, *args, **kwargs):
        """Pass through to provider AssetCompositionDesignSession.remove_asset"""
        # Built from: templates/osid_session.GenericObjectContainableDesignSession.remove_object_from_containable
        return self._get_provider_session('asset_composition_design_session').remove_asset(*args, **kwargs)
##
# The following methods are from osid.repository.CompositionLookupSession

    def can_lookup_compositions(self):
        """Pass through to provider CompositionLookupSession.can_lookup_compositions"""
        # Built from: templates/osid_session.GenericObjectLookupSession.can_lookup_objects
        return self._get_provider_session('composition_lookup_session').can_lookup_compositions()

    def use_comparative_composition_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_comparative_object_view
        """Pass through to provider CompositionLookupSession.use_comparative_composition_view"""
        self._object_views['composition'] = COMPARATIVE
        # self._get_provider_session('composition_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_comparative_composition_view()
            except AttributeError:
                pass

    def use_plenary_composition_view(self):
        # Built from: templates/osid_session.GenericObjectLookupSession.use_plenary_object_view
        """Pass through to provider CompositionLookupSession.use_plenary_composition_view"""
        self._object_views['composition'] = PLENARY
        # self._get_provider_session('composition_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_plenary_composition_view()
            except AttributeError:
                pass

    def use_active_composition_view(self):
        """Pass through to provider CompositionLookupSession.use_active_composition_view"""
        # Built from: templates/osid_session.GenericContainableObjectLookupSession.use_active_containable_view
        self._operable_views['composition'] = ACTIVE
        # self._get_provider_session('composition_lookup_session')  # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_active_composition_view()
            except AttributeError:
                pass

    def use_any_status_composition_view(self):
        """Pass through to provider CompositionLookupSession.use_any_status_composition_view"""
        # Built from: templates/osid_session.GenericContainableObjectLookupSession.use_any_status_containable_view
        self._operable_views['composition'] = ANY_STATUS
        # self._get_provider_session('composition_lookup_session')  # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_any_status_composition_view()
            except AttributeError:
                pass

    def use_sequestered_composition_view(self):
        """Pass through to provider CompositionLookupSession.use_sequestered_composition_view"""
        # Built from: templates/osid_session.GenericContainableObjectLookupSession.use_sequestered_containable_view
        self._containable_views['composition'] = SEQUESTERED
        # self._get_provider_session('composition_lookup_session')  # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_sequestered_composition_view()
            except AttributeError:
                pass

    def use_unsequestered_composition_view(self):
        """Pass through to provider CompositionLookupSession.use_unsequestered_composition_view"""
        # Built from: templates/osid_session.GenericContainableObjectLookupSession.use_unsequestered_containable_view
        self._containable_views['composition'] = UNSEQUESTERED
        # self._get_provider_session('composition_lookup_session') # To make sure the session is tracked
        for session in self._get_provider_sessions():
            try:
                session.use_unsequestered_composition_view()
            except AttributeError:
                pass

    def get_composition(self, *args, **kwargs):
        """Pass through to provider CompositionLookupSession.get_composition"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_object
        return self._get_provider_session('composition_lookup_session').get_composition(*args, **kwargs)

    def get_compositions_by_ids(self, *args, **kwargs):
        """Pass through to provider CompositionLookupSession.get_compositions_by_ids"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_ids
        return self._get_provider_session('composition_lookup_session').get_compositions_by_ids(*args, **kwargs)

    def get_compositions_by_genus_type(self, *args, **kwargs):
        """Pass through to provider CompositionLookupSession.get_compositions_by_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_genus_type
        return self._get_provider_session('composition_lookup_session').get_compositions_by_genus_type(*args, **kwargs)

    def get_compositions_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider CompositionLookupSession.get_compositions_by_parent_genus_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_parent_genus_type
        return self._get_provider_session('composition_lookup_session').get_compositions_by_parent_genus_type(*args, **kwargs)

    def get_compositions_by_record_type(self, *args, **kwargs):
        """Pass through to provider CompositionLookupSession.get_compositions_by_record_type"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects_by_record_type
        return self._get_provider_session('composition_lookup_session').get_compositions_by_record_type(*args, **kwargs)

    def get_compositions_by_provider(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_compositions(self):
        """Pass through to provider CompositionLookupSession.get_compositions"""
        # Built from: templates/osid_session.GenericObjectLookupSession.get_objects
        return self._get_provider_session('composition_lookup_session').get_compositions()

    compositions = property(fget=get_compositions)
##
# The following methods are from osid.repository.CompositionQuerySession

    def can_search_compositions(self):
        """Pass through to provider CompositionQuerySession.can_search_compositions"""
        # Built from: templates/osid_session.GenericObjectQuerySession.can_search_objects
        return self._get_provider_session('composition_query_session').can_search_compositions()

    def get_composition_query(self):
        """Pass through to provider CompositionQuerySession.get_composition_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_object_query
        return self._get_provider_session('composition_query_session').get_composition_query()

    composition_query = property(fget=get_composition_query)

    def get_compositions_by_query(self, *args, **kwargs):
        """Pass through to provider CompositionQuerySession.get_compositions_by_query"""
        # Built from: templates/osid_session.GenericObjectQuerySession.get_objects_by_query
        return self._get_provider_session('composition_query_session').get_compositions_by_query(*args, **kwargs)
##
# The following methods are from osid.repository.CompositionSearchSession

    def get_composition_search(self):
        """Pass through to provider CompositionSearchSession.get_composition_search"""
        # Built from: templates/osid_session.GenericObjectSearchSession.get_object_search
        return self._get_provider_session('composition_search_session').get_composition_search()

    composition_search = property(fget=get_composition_search)

    def get_composition_search_order(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    composition_search_order = property(fget=get_composition_search_order)

    def get_compositions_by_search(self, *args, **kwargs):
        """Pass through to provider CompositionSearchSession.get_compositions_by_search"""
        # Built from: templates/osid_session.GenericObjectSearchSession.get_objects_by_search
        return self._get_provider_session('composition_search_session').get_compositions_by_search(*args, **kwargs)

    def get_composition_query_from_inspector(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.repository.CompositionAdminSession

    def can_create_compositions(self):
        """Pass through to provider CompositionAdminSession.can_create_compositions"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_objects
        return self._get_provider_session('composition_admin_session').can_create_compositions()

    def can_create_composition_with_record_types(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.can_create_composition_with_record_types"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_create_object_with_record_types
        return self._get_provider_session('composition_admin_session').can_create_composition_with_record_types(*args, **kwargs)

    def get_composition_form_for_create(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.get_composition_form_for_create"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_create
        return self._get_provider_session('composition_admin_session').get_composition_form_for_create(*args, **kwargs)

    def create_composition(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.create_composition"""
        # Built from: templates/osid_session.GenericObjectAdminSession.create_object
        return self._get_provider_session('composition_admin_session').create_composition(*args, **kwargs)

    def can_update_compositions(self):
        """Pass through to provider CompositionAdminSession.can_update_compositions"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_update_objects
        return self._get_provider_session('composition_admin_session').can_update_compositions()

    def get_composition_form_for_update(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.get_composition_form_for_update"""
        # Built from: templates/osid_session.GenericObjectAdminSession.get_object_form_for_update
        return self._get_provider_session('composition_admin_session').get_composition_form_for_update(*args, **kwargs)

    def update_composition(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.update_composition"""
        # Built from: templates/osid_session.GenericObjectAdminSession.update_object
        return self._get_provider_session('composition_admin_session').update_composition(*args, **kwargs)

    def can_delete_compositions(self):
        """Pass through to provider CompositionAdminSession.can_delete_compositions"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_delete_objects
        return self._get_provider_session('composition_admin_session').can_delete_compositions()

    def delete_composition(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.delete_composition"""
        # Built from: templates/osid_session.GenericObjectAdminSession.delete_object
        self._get_provider_session('composition_admin_session').delete_composition(*args, **kwargs)

    def delete_composition_node(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def add_composition_child(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def remove_composition_child(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def can_manage_composition_aliases(self):
        """Pass through to provider CompositionAdminSession.can_manage_composition_aliases"""
        # Built from: templates/osid_session.GenericObjectAdminSession.can_manage_object_aliases
        return self._get_provider_session('composition_admin_session').can_manage_composition_aliases()

    def alias_composition(self, *args, **kwargs):
        """Pass through to provider CompositionAdminSession.alias_composition"""
        # Built from: templates/osid_session.GenericObjectAdminSession.alias_object
        self._get_provider_session('composition_admin_session').alias_composition(*args, **kwargs)

    # This is out of spec, but used by the EdX / LORE record extensions...
    def duplicate_composition(self, composition_id):
        return self._get_provider_session('composition_admin_session').duplicate_composition(composition_id)

    def can_lookup_asset_contents(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.can_lookup_asset_contents
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').can_lookup_asset_contents(*args, **kwargs)

    def get_asset_content(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_content
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_content(*args, **kwargs)

    def get_asset_contents_by_ids(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_contents_by_ids
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_contents_by_ids(*args, **kwargs)

    def get_asset_contents_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_contents_by_genus_type
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_contents_by_genus_type(*args, **kwargs)

    def get_asset_contents_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_contents_by_parent_genus_type
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_contents_by_parent_genus_type(*args, **kwargs)

    def get_asset_contents_by_record_type(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_contents_by_record_type
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_contents_by_record_type(*args, **kwargs)

    def get_asset_contents_for_asset(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_contents_for_asset
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_contents_for_asset(*args, **kwargs)

    def get_asset_contents_by_genus_type_for_asset(self, *args, **kwargs):
        """Pass through to provider AssetContentLookupSession.get_asset_contents_by_genus_type_for_asset
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_content_lookup_session').get_asset_contents_by_genus_type_for_asset(*args, **kwargs)

    def get_asset_content_query(self, *args, **kwargs):
        """Pass through to provider AssetQuerySession.get_asset_content_query
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_query_session').get_asset_content_query(*args, **kwargs)

    def get_asset_contents_by_query(self, *args, **kwargs):
        """Pass through to provider AssetQuerySession.get_asset_contents_by_query
            Out-of-band, non-OSID convenience method
        """
        return self._get_provider_session('asset_query_session').get_asset_contents_by_query(*args, **kwargs)


class RepositoryList(abc_repository_objects.RepositoryList, osid.OsidList):
    """RepositoryList convenience adapter including related Session methods."""

    def get_next_repository(self):
        """Gets next object"""
        # Built from: templates/osid_list.GenericObjectList.get_next_object
        return next(self)

    def next(self):
        """next method for enumerator"""
        return self._get_next_object(Repository)

    __next__ = next

    next_repository = property(fget=get_next_repository)

    def get_next_repositories(self, n):
        # Built from: templates/osid_list.GenericObjectList.get_next_objects
        return self._get_next_n(RepositoryList, number=n)
