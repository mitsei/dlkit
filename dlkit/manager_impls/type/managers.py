"""Manager utility implementations of type managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from dlkit.abstract_osid.type import managers as abc_type_managers


class TypeProfile(abc_type_managers.TypeProfile, osid_managers.OsidProfile):
    """The ``TypeProfile`` describes the interoperability among type services."""

    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.

        return: (boolean) - ``true`` if ``Type`` lookup is supported,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.

        return: (boolean) - ``true`` if ``Type`` administration is
                supported, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False


class TypeManager(abc_type_managers.TypeManager, osid_managers.OsidManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """

    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.

        return: (osid.type.TypeLookupSession) - a ``TypeLookupSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_type_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    type_lookup_session = property(fget=get_type_lookup_session)

    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.

        return: (osid.type.TypeAdminSession) - a ``TypeAdminSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_type_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*

        """
        raise Unimplemented()

    type_admin_session = property(fget=get_type_admin_session)


class TypeProxyManager(abc_type_managers.TypeProxyManager, osid_managers.OsidProxyManager, TypeProfile):
    """This manager provides access to the available sessions of the type service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """

    def get_type_lookup_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the type lookup service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.type.TypeLookupSession) - a ``TypeLookupSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_type_lookup()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*

        """
        raise Unimplemented()

    def get_type_admin_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the ``TypeAdmin`` service.

        arg:    proxy (osid.proxy.Proxy): a proxy
        return: (osid.type.TypeAdminSession) - the new
                ``TypeAdminSession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - ``unable to complete request``
        raise:  Unimplemented - ``supports_type_admin()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*

        """
        raise Unimplemented()
