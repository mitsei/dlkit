"""AuthZ Adapter implementations of id managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented, OperationFailed, Unsupported
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.id import managers as id_managers


class IdProfile(osid_managers.OsidProfile, id_managers.IdProfile):
    """Adapts underlying IdProfile methodswith authorization checks."""


class IdManager(osid_managers.OsidManager, IdProfile, id_managers.IdManager):
    """Adapts underlying IdManager methodswith authorization checks."""

    def get_id_batch_manager(self):
        raise Unimplemented()

    id_batch_manager = property(fget=get_id_batch_manager)


class IdProxyManager(osid_managers.OsidProxyManager, IdProfile, id_managers.IdProxyManager):
    """Adapts underlying IdProxyManager methodswith authorization checks."""

    def get_id_batch_proxy_manager(self):
        raise Unimplemented()

    id_batch_proxy_manager = property(fget=get_id_batch_proxy_manager)
