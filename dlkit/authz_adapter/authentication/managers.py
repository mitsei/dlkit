"""AuthZ Adapter implementations of authentication managers."""
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
from dlkit.manager_impls.authentication import managers as authentication_managers


class AuthenticationProfile(osid_managers.OsidProfile, authentication_managers.AuthenticationProfile):
    """Adapts underlying AuthenticationProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        if proxy is not None:
            try:
                return self._provider_manager.get_agency_hierarchy_session(proxy)
            except Unimplemented:
                return None
        try:
            return self._provider_manager.get_agency_hierarchy_session()
        except Unimplemented:
            return None

    def supports_agent_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_agent_lookup()

    def get_agent_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_agent_record_types()

    agent_record_types = property(fget=get_agent_record_types)

    def get_agent_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_agent_search_record_types()

    agent_search_record_types = property(fget=get_agent_search_record_types)

    def get_agency_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_agency_record_types()

    agency_record_types = property(fget=get_agency_record_types)

    def get_agency_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_agency_search_record_types()

    agency_search_record_types = property(fget=get_agency_search_record_types)


class AuthenticationManager(osid_managers.OsidManager, AuthenticationProfile, authentication_managers.AuthenticationManager):
    """Adapts underlying AuthenticationManager methodswith authorization checks."""
    def __init__(self):
        AuthenticationProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authenticationProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('AUTHENTICATION', provider_impl)
        # need to add version argument

    def get_agent_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_agent_query_session()
            query_session.use_federated_agency_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'AgentLookupSession')(
            provider_session=self._provider_manager.get_agent_lookup_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            hierarchy_session=self._get_hierarchy_session(),
            query_session=query_session)

    agent_lookup_session = property(fget=get_agent_lookup_session)

    @raise_null_argument
    def get_agent_lookup_session_for_agency(self, agency_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_agent_query_session_for_agency(agency_id)
            query_session.use_federated_agency_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'AgentLookupSession')(
            provider_session=self._provider_manager.get_agent_lookup_session_for_agency(agency_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            hierarchy_session=self._get_hierarchy_session(),
            query_session=query_session)

    def get_authentication_batch_manager(self):
        raise Unimplemented()

    authentication_batch_manager = property(fget=get_authentication_batch_manager)

    def get_authentication_keys_manager(self):
        raise Unimplemented()

    authentication_keys_manager = property(fget=get_authentication_keys_manager)

    def get_authentication_process_manager(self):
        raise Unimplemented()

    authentication_process_manager = property(fget=get_authentication_process_manager)


class AuthenticationProxyManager(osid_managers.OsidProxyManager, AuthenticationProfile, authentication_managers.AuthenticationProxyManager):
    """Adapts underlying AuthenticationProxyManager methodswith authorization checks."""
    def __init__(self):
        AuthenticationProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authenticationProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('AUTHENTICATION', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_agent_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_agent_query_session(proxy)
            query_session.use_federated_agency_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'AgentLookupSession')(
            provider_session=self._provider_manager.get_agent_lookup_session(proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            proxy=proxy,
            hierarchy_session=self._get_hierarchy_session(proxy),
            query_session=query_session)

    @raise_null_argument
    def get_agent_lookup_session_for_agency(self, agency_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_agent_query_session_for_agency(agency_id, proxy)
            query_session.use_federated_agency_view()
        except Unimplemented:
            query_session = None
        return getattr(sessions, 'AgentLookupSession')(
            provider_session=self._provider_manager.get_agent_lookup_session_for_agency(agency_id, proxy),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            proxy=proxy,
            hierarchy_session=self._get_hierarchy_session(proxy),
            query_session=query_session)

    def get_authentication_batch_proxy_manager(self):
        raise Unimplemented()

    authentication_batch_proxy_manager = property(fget=get_authentication_batch_proxy_manager)

    def get_authentication_keys_proxy_manager(self):
        raise Unimplemented()

    authentication_keys_proxy_manager = property(fget=get_authentication_keys_proxy_manager)

    def get_authentication_process_proxy_manager(self):
        raise Unimplemented()

    authentication_process_proxy_manager = property(fget=get_authentication_process_proxy_manager)
