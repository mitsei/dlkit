"""AuthZ Adapter implementations of repository managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from ..osid.osid_errors import Unimplemented, OperationFailed
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.repository import managers as repository_managers


class RepositoryProfile(osid_managers.OsidProfile, repository_managers.RepositoryProfile):
    """Adapts underlying RepositoryProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_repository_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_repository_hierarchy_session()
        except Unimplemented:
            return None

    def supports_asset_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_lookup()

    def supports_asset_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_query()

    def supports_asset_search(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_search()

    def supports_asset_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_admin()

    def supports_asset_notification(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_notification()

    def supports_asset_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_repository()

    def supports_asset_repository_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_repository_assignment()

    def supports_asset_composition(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_composition()

    def supports_asset_composition_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_asset_composition_design()

    def supports_composition_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_composition_lookup()

    def supports_composition_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_composition_query()

    def supports_composition_search(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_composition_search()

    def supports_composition_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_composition_admin()

    def supports_composition_repository(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_composition_repository()

    def supports_composition_repository_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_composition_repository_assignment()

    def supports_repository_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_repository_lookup()

    def supports_repository_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_repository_query()

    def supports_repository_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_repository_admin()

    def supports_repository_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_repository_hierarchy()

    def supports_repository_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_repository_hierarchy_design()

    def get_asset_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_asset_record_types()

    asset_record_types = property(fget=get_asset_record_types)

    def get_asset_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_asset_search_record_types()

    asset_search_record_types = property(fget=get_asset_search_record_types)

    def get_asset_content_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_asset_content_record_types()

    asset_content_record_types = property(fget=get_asset_content_record_types)

    def get_composition_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_composition_record_types()

    composition_record_types = property(fget=get_composition_record_types)

    def get_composition_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_composition_search_record_types()

    composition_search_record_types = property(fget=get_composition_search_record_types)

    def get_repository_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_repository_record_types()

    repository_record_types = property(fget=get_repository_record_types)

    def get_repository_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_repository_search_record_types()

    repository_search_record_types = property(fget=get_repository_search_record_types)

    def get_spatial_unit_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_spatial_unit_record_types()

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    def get_coordinate_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_coordinate_types()

    coordinate_types = property(fget=get_coordinate_types)


class RepositoryManager(osid_managers.OsidManager, RepositoryProfile, repository_managers.RepositoryManager):
    """Adapts underlying RepositoryManager methodswith authorization checks."""
    def __init__(self):
        RepositoryProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:repositoryProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('REPOSITORY', provider_impl)
        # need to add version argument

    def get_asset_composition_session_for_repository(self, repository_id):
        # This impl is temporary until Tom adds missing methods to RepositoryProxyManager in spec
        try:
            return getattr(sessions, 'AssetCompositionSession')(
                provider_session=self._provider_manager.get_asset_composition_session_for_repository(repository_id),
                authz_session=self._authz_session)
        except AttributeError:
            raise OperationFailed('AssetCompositionSession not implemented in authz_adapter')

    def get_asset_composition_design_session_for_repository(self, repository_id):
        # This impl is temporary until Tom adds missing methods to RepositoryProxyManager in spec
        try:
            return getattr(sessions, 'AssetCompositionDesignSession')(
                provider_session=self._provider_manager.get_asset_composition_design_session_for_repository(repository_id),
                authz_session=self._authz_session)
        except AttributeError:
            raise OperationFailed('AssetCompositionDesignSession not implemented in authz_adapter')

    def get_asset_content_lookup_session(self):
        """Pass through to provider get_asset_content_lookup_session"""
        try:
            return getattr(sessions, 'AssetContentLookupSession')(
                provider_session=self._provider_manager.get_asset_content_lookup_session(),
                authz_session=self._authz_session)
        except AttributeError:
            raise OperationFailed('AssetContentLookupSession not implemented in authz_adapter')

    def get_asset_content_lookup_session_for_repository(self, repository_id):
        """Pass through to provider get_asset_content_lookup_session_for_repository"""
        try:
            return getattr(sessions, 'AssetContentLookupSession')(
                provider_session=self._provider_manager.get_asset_content_lookup_session_for_repository(repository_id),
                authz_session=self._authz_session)
        except AttributeError:
            raise OperationFailed('AssetContentLookupSession not implemented in authz_adapter')

    def get_asset_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_asset_query_session()
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetLookupSession')(
                provider_session=self._provider_manager.get_asset_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    asset_lookup_session = property(fget=get_asset_lookup_session)

    @raise_null_argument
    def get_asset_lookup_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_asset_query_session_for_repository(repository_id)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetLookupSession')(
                provider_session=self._provider_manager.get_asset_lookup_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_asset_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_asset_query_session()
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetQuerySession')(
                provider_session=self._provider_manager.get_asset_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    asset_query_session = property(fget=get_asset_query_session)

    @raise_null_argument
    def get_asset_query_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_asset_query_session_for_repository(repository_id)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetQuerySession')(
                provider_session=self._provider_manager.get_asset_query_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_asset_search_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetSearchSession')(
                provider_session=self._provider_manager.get_asset_search_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    asset_search_session = property(fget=get_asset_search_session)

    @raise_null_argument
    def get_asset_search_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssetSearchSession')(
                provider_session=self._provider_manager.get_asset_search_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_asset_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetAdminSession')(
                provider_session=self._provider_manager.get_asset_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    asset_admin_session = property(fget=get_asset_admin_session)

    @raise_null_argument
    def get_asset_admin_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssetAdminSession')(
                provider_session=self._provider_manager.get_asset_admin_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_notification_session(self, asset_receiver):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id):
        raise Unimplemented()

    def get_asset_repository_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetRepositorySession')(
                provider_session=self._provider_manager.get_asset_repository_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    asset_repository_session = property(fget=get_asset_repository_session)

    def get_asset_repository_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetRepositoryAssignmentSession')(
                provider_session=self._provider_manager.get_asset_repository_assignment_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    asset_repository_assignment_session = property(fget=get_asset_repository_assignment_session)

    def get_asset_composition_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetCompositionSession')(
                provider_session=self._provider_manager.get_asset_composition_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    asset_composition_session = property(fget=get_asset_composition_session)

    def get_asset_composition_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetCompositionDesignSession')(
                provider_session=self._provider_manager.get_asset_composition_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    asset_composition_design_session = property(fget=get_asset_composition_design_session)

    def get_composition_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_composition_query_session()
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionLookupSession')(
                provider_session=self._provider_manager.get_composition_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    composition_lookup_session = property(fget=get_composition_lookup_session)

    @raise_null_argument
    def get_composition_lookup_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_composition_query_session_for_repository(repository_id)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionLookupSession')(
                provider_session=self._provider_manager.get_composition_lookup_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_composition_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_composition_query_session()
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionQuerySession')(
                provider_session=self._provider_manager.get_composition_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    composition_query_session = property(fget=get_composition_query_session)

    @raise_null_argument
    def get_composition_query_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_composition_query_session_for_repository(repository_id)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionQuerySession')(
                provider_session=self._provider_manager.get_composition_query_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_composition_search_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionSearchSession')(
                provider_session=self._provider_manager.get_composition_search_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    composition_search_session = property(fget=get_composition_search_session)

    @raise_null_argument
    def get_composition_search_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'CompositionSearchSession')(
                provider_session=self._provider_manager.get_composition_search_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_composition_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionAdminSession')(
                provider_session=self._provider_manager.get_composition_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    composition_admin_session = property(fget=get_composition_admin_session)

    @raise_null_argument
    def get_composition_admin_session_for_repository(self, repository_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'CompositionAdminSession')(
                provider_session=self._provider_manager.get_composition_admin_session_for_repository(repository_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_composition_repository_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionRepositorySession')(
                provider_session=self._provider_manager.get_composition_repository_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    composition_repository_session = property(fget=get_composition_repository_session)

    def get_composition_repository_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionRepositoryAssignmentSession')(
                provider_session=self._provider_manager.get_composition_repository_assignment_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    composition_repository_assignment_session = property(fget=get_composition_repository_assignment_session)

    def get_repository_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryLookupSession')(
                provider_session=self._provider_manager.get_repository_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    repository_lookup_session = property(fget=get_repository_lookup_session)

    def get_repository_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryQuerySession')(
                provider_session=self._provider_manager.get_repository_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    repository_query_session = property(fget=get_repository_query_session)

    def get_repository_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryAdminSession')(
                provider_session=self._provider_manager.get_repository_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    repository_admin_session = property(fget=get_repository_admin_session)

    def get_repository_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryHierarchySession')(
                provider_session=self._provider_manager.get_repository_hierarchy_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    repository_hierarchy_session = property(fget=get_repository_hierarchy_session)

    def get_repository_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryHierarchyDesignSession')(
                provider_session=self._provider_manager.get_repository_hierarchy_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    repository_hierarchy_design_session = property(fget=get_repository_hierarchy_design_session)

    def get_repository_batch_manager(self):
        raise Unimplemented()

    repository_batch_manager = property(fget=get_repository_batch_manager)

    def get_repository_rules_manager(self):
        raise Unimplemented()

    repository_rules_manager = property(fget=get_repository_rules_manager)


class RepositoryProxyManager(osid_managers.OsidProxyManager, RepositoryProfile, repository_managers.RepositoryProxyManager):
    """Adapts underlying RepositoryProxyManager methodswith authorization checks."""
    def __init__(self):
        RepositoryProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:repositoryProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('REPOSITORY', provider_impl)
        # need to add version argument

    def get_asset_composition_session_for_repository(self, repository_id, proxy):
        # This impl is temporary until Tom adds missing methods to RepositoryProxyManager in spec
        try:
            return getattr(sessions, 'AssetCompositionSession')(
                provider_session=self._provider_manager.get_asset_composition_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                proxy=proxy)
        except AttributeError:
            raise OperationFailed('AssetCompositionSession not implemented in authz_adapter')

    def get_asset_composition_design_session_for_repository(self, repository_id, proxy):
        # This impl is temporary until Tom adds missing methods to RepositoryProxyManager in spec
        try:
            return getattr(sessions, 'AssetCompositionDesignSession')(
                provider_session=self._provider_manager.get_asset_composition_design_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                proxy=proxy)
        except AttributeError:
            raise OperationFailed('AssetCompositionDesignSession not implemented in authz_adapter')

    def get_asset_content_lookup_session(self, proxy):
        """Pass through to provider get_asset_content_lookup_session"""
        try:
            return getattr(sessions, 'AssetContentLookupSession')(
                provider_session=self._provider_manager.get_asset_content_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                proxy=proxy)
        except AttributeError:
            raise OperationFailed('AssetContentLookupSession not implemented in authz_adapter')

    def get_asset_content_lookup_session_for_repository(self, repository_id, proxy):
        """Pass through to provider get_asset_content_lookup_session_for_repository"""
        try:
            return getattr(sessions, 'AssetContentLookupSession')(
                provider_session=self._provider_manager.get_asset_content_lookup_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                proxy=proxy)
        except AttributeError:
            raise OperationFailed('AssetContentLookupSession not implemented in authz_adapter')

    @raise_null_argument
    def get_asset_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_asset_query_session(proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetLookupSession')(
                provider_session=self._provider_manager.get_asset_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_lookup_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_asset_query_session_for_repository(repository_id, proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetLookupSession')(
                provider_session=self._provider_manager.get_asset_lookup_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_asset_query_session(proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetQuerySession')(
                provider_session=self._provider_manager.get_asset_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_query_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_asset_query_session_for_repository(repository_id, proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssetQuerySession')(
                provider_session=self._provider_manager.get_asset_query_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_search_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetSearchSession')(
                provider_session=self._provider_manager.get_asset_search_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_search_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssetSearchSession')(
                provider_session=self._provider_manager.get_asset_search_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetAdminSession')(
                provider_session=self._provider_manager.get_asset_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_admin_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssetAdminSession')(
                provider_session=self._provider_manager.get_asset_admin_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_notification_session(self, asset_receiver, proxy):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_notification_session_for_repository(self, asset_receiver, repository_id, proxy):
        raise Unimplemented()

    @raise_null_argument
    def get_asset_repository_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetRepositorySession')(
                provider_session=self._provider_manager.get_asset_repository_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_repository_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetRepositoryAssignmentSession')(
                provider_session=self._provider_manager.get_asset_repository_assignment_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_composition_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetCompositionSession')(
                provider_session=self._provider_manager.get_asset_composition_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_asset_composition_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssetCompositionDesignSession')(
                provider_session=self._provider_manager.get_asset_composition_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_composition_query_session(proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionLookupSession')(
                provider_session=self._provider_manager.get_composition_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_lookup_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_composition_query_session_for_repository(repository_id, proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionLookupSession')(
                provider_session=self._provider_manager.get_composition_lookup_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_composition_query_session(proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionQuerySession')(
                provider_session=self._provider_manager.get_composition_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_query_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_composition_query_session_for_repository(repository_id, proxy)
            query_session.use_federated_repository_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'CompositionQuerySession')(
                provider_session=self._provider_manager.get_composition_query_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_search_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionSearchSession')(
                provider_session=self._provider_manager.get_composition_search_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_search_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'CompositionSearchSession')(
                provider_session=self._provider_manager.get_composition_search_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionAdminSession')(
                provider_session=self._provider_manager.get_composition_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_admin_session_for_repository(self, repository_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'CompositionAdminSession')(
                provider_session=self._provider_manager.get_composition_admin_session_for_repository(repository_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_repository_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionRepositorySession')(
                provider_session=self._provider_manager.get_composition_repository_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_composition_repository_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'CompositionRepositoryAssignmentSession')(
                provider_session=self._provider_manager.get_composition_repository_assignment_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_repository_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryLookupSession')(
                provider_session=self._provider_manager.get_repository_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_repository_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryQuerySession')(
                provider_session=self._provider_manager.get_repository_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_repository_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryAdminSession')(
                provider_session=self._provider_manager.get_repository_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_repository_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryHierarchySession')(
                provider_session=self._provider_manager.get_repository_hierarchy_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_repository_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RepositoryHierarchyDesignSession')(
                provider_session=self._provider_manager.get_repository_hierarchy_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_repository_batch_proxy_manager(self):
        raise Unimplemented()

    repository_batch_proxy_manager = property(fget=get_repository_batch_proxy_manager)

    def get_repository_rules_proxy_manager(self):
        raise Unimplemented()

    repository_rules_proxy_manager = property(fget=get_repository_rules_proxy_manager)
