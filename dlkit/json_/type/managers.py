"""JSON implementations of type managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package json package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from .. import utilities
from ..osid import managers as osid_managers
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.type import managers as type_managers


class TypeProfile(osid_managers.OsidProfile, type_managers.TypeProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""


class TypeManager(osid_managers.OsidManager, TypeProfile, type_managers.TypeManager):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """


class TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile, type_managers.TypeProxyManager):
    """This manager provides access to the available sessions of the type service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """
