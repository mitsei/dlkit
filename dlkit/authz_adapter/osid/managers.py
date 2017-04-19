"""AuthZ Adapter implementations of osid managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import markers as osid_markers
from ..osid.osid_errors import Unimplemented, IllegalState, NullArgument
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.abstract_osid.osid import managers as abc_osid_managers


COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1


class OsidProfile(abc_osid_managers.OsidProfile, osid_markers.Sourceable):
    """Adapts underlying OsidProfile methodswith authorization checks."""
    def __init__(self):
        self._provider_manager = None
        self._my_runtime = None

    def initialize(self, runtime):
        if runtime is None:
            raise NullArgument()
        if self._my_runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._my_runtime = runtime

    def _get_authz_manager(self):
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        return self._my_runtime.get_manager('AUTHORIZATION', provider_impl)  # need to add version argument

    def _get_vault_lookup_session(self):
        return self._get_authz_manager().get_vault_lookup_session()

    def _get_authz_session(self):
        """Gets the AuthorizationSession for the default (bootstrap) typed Vault

        Assumes only one vault of this Type, but it can have children depending on underlying impl.

        """
        from ..utilities import BOOTSTRAP_VAULT_TYPE
        try:
            vaults = self._get_vault_lookup_session().get_vaults_by_genus_type(BOOTSTRAP_VAULT_TYPE)
        except Unimplemented:
            return self._get_authz_manager().get_authorization_session()
        if vaults.available():
            vault = vaults.next()
            return self._get_authz_manager().get_authorization_session_for_vault(vault.get_id())
        else:
            return self._get_authz_manager().get_authorization_session()

    def _get_override_lookup_session(self):
        """Gets the AuthorizationLookupSession for the override typed Vault

        Assumes only one

        """
        from ..utilities import OVERRIDE_VAULT_TYPE
        try:
            override_vaults = self._get_vault_lookup_session().get_vaults_by_genus_type(OVERRIDE_VAULT_TYPE)
        except Unimplemented:
            return None
        if override_vaults.available():
            vault = override_vaults.next()
        else:
            return None
        session = self._get_authz_manager().get_authorization_lookup_session_for_vault(vault.get_id())
        session.use_isolated_vault_view()
        return session

    def get_id(self):
        pass

    id_ = property(fget=get_id)

    ident = property(fget=get_id)

    def get_display_name(self):
        pass

    display_name = property(fget=get_display_name)

    def get_description(self):
        pass

    description = property(fget=get_description)

    def get_version(self):
        pass

    version = property(fget=get_version)

    def get_release_date(self):
        pass

    release_date = property(fget=get_release_date)

    @raise_null_argument
    def supports_osid_version(self, version):
        pass

    def get_locales(self):
        pass

    locales = property(fget=get_locales)

    def supports_journal_rollback(self):
        pass

    def supports_journal_branching(self):
        pass

    def get_branch_id(self):
        pass

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        pass

    branch = property(fget=get_branch)

    def get_proxy_record_types(self):
        pass

    proxy_record_types = property(fget=get_proxy_record_types)

    @raise_null_argument
    def supports_proxy_record_type(self, proxy_record_type):
        pass


class OsidManager(abc_osid_managers.OsidManager, OsidProfile):
    """Adapts underlying OsidManager methodswith authorization checks."""
    def __init__(self):
        OsidProfile.__init__(self)

    @raise_null_argument
    def initialize(self, runtime):
        OsidProfile.initialize(self, runtime)

    @raise_null_argument
    def rollback_service(self, rollback_time):
        raise Unimplemented()

    @raise_null_argument
    def change_branch(self, branch_id):
        raise Unimplemented()


class OsidProxyManager(abc_osid_managers.OsidProxyManager, OsidProfile):
    """Adapts underlying OsidProxyManager methodswith authorization checks."""
    def __init__(self):
        OsidProfile.__init__(self)

    @raise_null_argument
    def initialize(self, runtime):
        OsidProfile.initialize(self, runtime)

    @raise_null_argument
    def rollback_service(self, rollback_time, proxy):
        raise Unimplemented()

    @raise_null_argument
    def change_branch(self, branch_id, proxy):
        raise Unimplemented()


class OsidRuntimeProfile(abc_osid_managers.OsidRuntimeProfile, OsidProfile):
    """Adapts underlying OsidRuntimeProfile methodswith authorization checks."""

    def supports_configuration(self):
        raise Unimplemented()


class OsidRuntimeManager(abc_osid_managers.OsidRuntimeManager, OsidManager, OsidRuntimeProfile):
    """Adapts underlying OsidRuntimeManager methodswith authorization checks."""

    @raise_null_argument
    def get_manager(self, osid, impl_class_name, version):
        raise Unimplemented()

    @raise_null_argument
    def get_proxy_manager(self, osid, implementation, version):
        raise Unimplemented()

    def get_configuration(self):
        raise Unimplemented()

    configuration = property(fget=get_configuration)
