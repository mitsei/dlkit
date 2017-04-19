"""AuthZ Adapter implementations of authentication.process managers."""
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
from dlkit.manager_impls.authentication_process import managers as authentication_process_managers


class AuthenticationProcessProfile(osid_managers.OsidProfile, authentication_process_managers.AuthenticationProcessProfile):
    """Adapts underlying AuthenticationProcessProfile methodswith authorization checks."""
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

    def get_authentication_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authentication_record_types()

    authentication_record_types = property(fget=get_authentication_record_types)

    def get_authentication_input_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_authentication_input_record_types()

    authentication_input_record_types = property(fget=get_authentication_input_record_types)

    def get_challenge_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_challenge_record_types()

    challenge_record_types = property(fget=get_challenge_record_types)

    def get_credential_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_credential_types()

    credential_types = property(fget=get_credential_types)

    def get_trust_types(self):
        # Implemented from azosid template for -
        # osid.repository.RepositoryProfile.get_coordinate_types
        return self._provider_manager.get_trust_types()

    trust_types = property(fget=get_trust_types)


class AuthenticationProcessManager(osid_managers.OsidManager, AuthenticationProcessProfile, authentication_process_managers.AuthenticationProcessManager):
    """Adapts underlying AuthenticationProcessManager methodswith authorization checks."""
    def __init__(self):
        AuthenticationProcessProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authentication_processProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('AUTHENTICATION_PROCESS', provider_impl)
        # need to add version argument


class AuthenticationProcessProxyManager(osid_managers.OsidProxyManager, AuthenticationProcessProfile, authentication_process_managers.AuthenticationProcessProxyManager):
    """Adapts underlying AuthenticationProcessProxyManager methodswith authorization checks."""
    def __init__(self):
        AuthenticationProcessProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authentication_processProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('AUTHENTICATION_PROCESS', provider_impl)
        # need to add version argument
