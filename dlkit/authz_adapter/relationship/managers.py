"""AuthZ Adapter implementations of relationship managers."""
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
from dlkit.manager_impls.relationship import managers as relationship_managers


class RelationshipProfile(osid_managers.OsidProfile, relationship_managers.RelationshipProfile):
    """Adapts underlying RelationshipProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_family_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_family_hierarchy_session()
        except Unimplemented:
            return None

    def supports_relationship_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_relationship_lookup()

    def supports_relationship_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_relationship_query()

    def supports_relationship_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_relationship_admin()

    def supports_family_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_lookup()

    def supports_family_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_admin()

    def supports_family_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_hierarchy()

    def supports_family_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_family_hierarchy_design()

    def get_relationship_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_relationship_record_types()

    relationship_record_types = property(fget=get_relationship_record_types)

    def get_relationship_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_relationship_search_record_types()

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    def get_family_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_family_record_types()

    family_record_types = property(fget=get_family_record_types)

    def get_family_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_family_search_record_types()

    family_search_record_types = property(fget=get_family_search_record_types)


class RelationshipManager(osid_managers.OsidManager, RelationshipProfile, relationship_managers.RelationshipManager):
    """Adapts underlying RelationshipManager methodswith authorization checks."""
    def __init__(self):
        RelationshipProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:relationshipProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('RELATIONSHIP', provider_impl)
        # need to add version argument

    def get_relationship_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_relationship_query_session()
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipLookupSession')(
                provider_session=self._provider_manager.get_relationship_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    @raise_null_argument
    def get_relationship_lookup_session_for_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_relationship_query_session_for_family(family_id)
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipLookupSession')(
                provider_session=self._provider_manager.get_relationship_lookup_session_for_family(family_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_relationship_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_relationship_query_session()
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipQuerySession')(
                provider_session=self._provider_manager.get_relationship_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    relationship_query_session = property(fget=get_relationship_query_session)

    @raise_null_argument
    def get_relationship_query_session_for_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_relationship_query_session_for_family(family_id)
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipQuerySession')(
                provider_session=self._provider_manager.get_relationship_query_session_for_family(family_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_relationship_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RelationshipAdminSession')(
                provider_session=self._provider_manager.get_relationship_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    relationship_admin_session = property(fget=get_relationship_admin_session)

    @raise_null_argument
    def get_relationship_admin_session_for_family(self, family_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'RelationshipAdminSession')(
                provider_session=self._provider_manager.get_relationship_admin_session_for_family(family_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_family_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyLookupSession')(
                provider_session=self._provider_manager.get_family_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    family_lookup_session = property(fget=get_family_lookup_session)

    def get_family_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyAdminSession')(
                provider_session=self._provider_manager.get_family_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    family_admin_session = property(fget=get_family_admin_session)

    def get_family_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyHierarchySession')(
                provider_session=self._provider_manager.get_family_hierarchy_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    def get_family_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyHierarchyDesignSession')(
                provider_session=self._provider_manager.get_family_hierarchy_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    family_hierarchy_design_session = property(fget=get_family_hierarchy_design_session)

    def get_relationship_batch_manager(self):
        raise Unimplemented()

    relationship_batch_manager = property(fget=get_relationship_batch_manager)

    def get_relationship_rules_manager(self):
        raise Unimplemented()

    relationship_rules_manager = property(fget=get_relationship_rules_manager)


class RelationshipProxyManager(osid_managers.OsidProxyManager, RelationshipProfile, relationship_managers.RelationshipProxyManager):
    """Adapts underlying RelationshipProxyManager methodswith authorization checks."""
    def __init__(self):
        RelationshipProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:relationshipProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('RELATIONSHIP', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_relationship_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_relationship_query_session(proxy)
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipLookupSession')(
                provider_session=self._provider_manager.get_relationship_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_relationship_lookup_session_for_family(self, family_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_relationship_query_session_for_family(family_id, proxy)
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipLookupSession')(
                provider_session=self._provider_manager.get_relationship_lookup_session_for_family(family_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_relationship_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_relationship_query_session(proxy)
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipQuerySession')(
                provider_session=self._provider_manager.get_relationship_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_relationship_query_session_for_family(self, family_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_relationship_query_session_for_family(family_id, proxy)
            query_session.use_federated_family_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'RelationshipQuerySession')(
                provider_session=self._provider_manager.get_relationship_query_session_for_family(family_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_relationship_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'RelationshipAdminSession')(
                provider_session=self._provider_manager.get_relationship_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_relationship_admin_session_for_family(self, family_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'RelationshipAdminSession')(
                provider_session=self._provider_manager.get_relationship_admin_session_for_family(family_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_family_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyLookupSession')(
                provider_session=self._provider_manager.get_family_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_family_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyAdminSession')(
                provider_session=self._provider_manager.get_family_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_family_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyHierarchySession')(
                provider_session=self._provider_manager.get_family_hierarchy_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_family_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'FamilyHierarchyDesignSession')(
                provider_session=self._provider_manager.get_family_hierarchy_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_relationship_batch_proxy_manager(self):
        raise Unimplemented()

    relationship_batch_proxy_manager = property(fget=get_relationship_batch_proxy_manager)

    def get_relationship_rules_proxy_manager(self):
        raise Unimplemented()

    relationship_rules_proxy_manager = property(fget=get_relationship_rules_proxy_manager)
