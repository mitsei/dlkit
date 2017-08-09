"""AuthZ Adapter implementations of cataloging managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from ..osid.osid_errors import Unimplemented, OperationFailed, Unsupported
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.cataloging import managers as cataloging_managers


class CatalogingProfile(osid_managers.OsidProfile, cataloging_managers.CatalogingProfile):
    """Adapts underlying CatalogingProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_catalog_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_catalog_hierarchy_session()
        except Unimplemented:
            return None

    def supports_catalog_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_catalog_lookup()

    def supports_catalog_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_catalog_query()

    def supports_catalog_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_catalog_admin()

    def supports_catalog_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_catalog_hierarchy()

    def supports_catalog_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_catalog_hierarchy_design()

    def get_catalog_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_catalog_record_types()

    catalog_record_types = property(fget=get_catalog_record_types)

    def get_catalog_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_catalog_search_record_types()

    catalog_search_record_types = property(fget=get_catalog_search_record_types)


class CatalogingManager(osid_managers.OsidManager, CatalogingProfile, cataloging_managers.CatalogingManager):
    """Adapts underlying CatalogingManager methodswith authorization checks."""
    def __init__(self):
        CatalogingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:catalogingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('CATALOGING', provider_impl)
        # need to add version argument

    def get_catalog_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogLookupSession')(
            provider_session=self._provider_manager.get_catalog_lookup_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    catalog_lookup_session = property(fget=get_catalog_lookup_session)

    def get_catalog_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogQuerySession')(
            provider_session=self._provider_manager.get_catalog_query_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    catalog_query_session = property(fget=get_catalog_query_session)

    def get_catalog_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogAdminSession')(
            provider_session=self._provider_manager.get_catalog_admin_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    catalog_admin_session = property(fget=get_catalog_admin_session)

    def get_catalog_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogHierarchySession')(
            provider_session=self._provider_manager.get_catalog_hierarchy_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    catalog_hierarchy_session = property(fget=get_catalog_hierarchy_session)

    def get_catalog_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogHierarchyDesignSession')(
            provider_session=self._provider_manager.get_catalog_hierarchy_design_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    catalog_hierarchy_design_session = property(fget=get_catalog_hierarchy_design_session)

    def get_cataloging_rules_manager(self):
        raise Unimplemented()

    cataloging_rules_manager = property(fget=get_cataloging_rules_manager)


class CatalogingProxyManager(osid_managers.OsidProxyManager, CatalogingProfile, cataloging_managers.CatalogingProxyManager):
    """Adapts underlying CatalogingProxyManager methodswith authorization checks."""
    def __init__(self):
        CatalogingProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:catalogingProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('CATALOGING', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_catalog_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogLookupSession')(
            provider_session=self._provider_manager.get_catalog_lookup_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_catalog_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogQuerySession')(
            provider_session=self._provider_manager.get_catalog_query_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_catalog_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogAdminSession')(
            provider_session=self._provider_manager.get_catalog_admin_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_catalog_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogHierarchySession')(
            provider_session=self._provider_manager.get_catalog_hierarchy_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    @raise_null_argument
    def get_catalog_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_admin_session_template
        return getattr(sessions, 'CatalogHierarchyDesignSession')(
            provider_session=self._provider_manager.get_catalog_hierarchy_design_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager,
            proxy=proxy)

    def get_cataloging_rules_proxy_manager(self):
        raise Unimplemented()

    cataloging_rules_proxy_manager = property(fget=get_cataloging_rules_proxy_manager)
