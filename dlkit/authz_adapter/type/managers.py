"""AuthZ Adapter implementations of type managers."""
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
from dlkit.manager_impls.type import managers as type_managers


class TypeProfile(osid_managers.OsidProfile, type_managers.TypeProfile):
    """Adapts underlying TypeProfile methodswith authorization checks."""


class TypeManager(osid_managers.OsidManager, TypeProfile, type_managers.TypeManager):
    """Adapts underlying TypeManager methodswith authorization checks."""


class TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile, type_managers.TypeProxyManager):
    """Adapts underlying TypeProxyManager methodswith authorization checks."""
