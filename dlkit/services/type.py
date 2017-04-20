"""DLKit Services implementations of type service."""
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
from dlkit.manager_impls.type import managers as type_managers


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


class TypeProfile(osid.OsidProfile, type_managers.TypeProfile):
    """TypeProfile convenience adapter including related Session methods."""
    pass


class TypeManager(osid.OsidManager, osid.OsidSession, TypeProfile, type_managers.TypeManager):
    """TypeManager convenience adapter including related Session methods."""
    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._bin_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _get_provider_session(self, session):
        if session in self._provider_sessions:
            return self._provider_sessions[session]
        else:
            try:
                get_session = getattr(self._provider_manager, 'get_' + session)
            except:
                raise  # Unimplemented???
            else:
                self._provider_sessions[session] = get_session()
            return self._provider_sessions[session]

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:typeProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        # do not account for TypeProxyManager yet...not used in Handcar
        # need to add version argument
        self._provider_manager = runtime.get_manager('TYPE', provider_impl)

    def get_types(self, *args, **kwargs):
        """Pass through to provider method"""
        # Implemented from
        # osid.type.TypeLookupSession.get_types
        return self._get_provider_session('type_lookup_session').get_types(*args, **kwargs)

    def get_type_lookup_session(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._provider_manager.get_type_lookup_session(*args, **kwargs)

    def get_type_admin_session(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._provider_manager.get_type_admin_session(*args, **kwargs)


class TypeProxyManager(osid.OsidProxyManager, TypeProfile, type_managers.TypeProxyManager):
    """TypeProxyManager convenience adapter including related Session methods."""
    pass
