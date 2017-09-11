"""DLKit Services implementations of id service."""
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
from dlkit.manager_impls.id import managers as id_managers


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


class IdProfile(osid.OsidProfile, id_managers.IdProfile):
    """IdProfile convenience adapter including related Session methods."""
    pass


class IdManager(osid.OsidManager, osid.OsidSession, IdProfile, id_managers.IdManager):
    """IdManager convenience adapter including related Session methods."""

    def get_id_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    id_batch_manager = property(fget=get_id_batch_manager)


class IdProxyManager(osid.OsidProxyManager, IdProfile, id_managers.IdProxyManager):
    """IdProxyManager convenience adapter including related Session methods."""

    def get_id_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    id_batch_proxy_manager = property(fget=get_id_batch_proxy_manager)
