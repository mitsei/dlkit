"""DLKit Services implementations of proxy service."""
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
from dlkit.manager_impls.proxy import managers as proxy_managers


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


class ProxyProfile(osid.OsidProfile, proxy_managers.ProxyProfile):
    """ProxyProfile convenience adapter including related Session methods."""
    def __init__(self):
        self._provider_manager = None

    def supports_proxy(self):
        """Pass through to provider supports_proxy"""
        # Built from: templates/osid_managers.GenericProfile.supports_object_lookup
        return self._provider_manager.supports_proxy()

    def get_proxy_record_types(self):
        """Pass through to provider get_proxy_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_proxy_record_types()

    proxy_record_types = property(fget=get_proxy_record_types)

    def get_proxy_condition_record_types(self):
        """Pass through to provider get_proxy_condition_record_types"""
        # Built from: templates/osid_managers.GenericProfile.get_object_record_types
        return self._provider_manager.get_proxy_condition_record_types()

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)


class ProxyManager(osid.OsidManager, osid.OsidSession, ProxyProfile, Manager, proxy_managers.ProxyManager):
    """ProxyManager convenience adapter including related Session methods."""


    def get_proxy_session(self, *args, **kwargs):
        """Pass through to provider get_proxy_session"""
        # Built from: templates/osid_managers.GenericManager.get_object_admin_session
        return self._provider_manager.get_proxy_session(*args, **kwargs)

    proxy_session = property(fget=get_proxy_session)
##
# The following methods are from osid.proxy.ProxySession

    def get_proxy_condition(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    proxy_condition = property(fget=get_proxy_condition)

    def get_proxy(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


class ProxyProxyManager(osid.OsidProxyManager, ProxyProfile, Manager, proxy_managers.ProxyProxyManager):
    """ProxyProxyManager convenience adapter including related Session methods."""
    pass
