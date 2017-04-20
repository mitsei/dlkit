"""Manager utility implementations of proxy managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from ..osid import managers as osid_managers
from ..osid.osid_errors import NullArgument
from ..osid.osid_errors import Unimplemented
from ..type.objects import TypeList
from dlkit.abstract_osid.proxy import managers as abc_proxy_managers


class ProxyProfile(abc_proxy_managers.ProxyProfile, osid_managers.OsidProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""

    def supports_proxy(self):
        """Tests if a proxy session is supported.

        return: (boolean) - ``true`` if proxy is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.

        return: (osid.type.TypeList) - a list containing the supported
                ``Proxy`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, proxy_record_type=None):
        """Tests if the given ``Proxy`` record interface type is supported.

        arg:    proxy_record_type (osid.type.Type): a ``Type``
                indicating a ``Proxy`` record type
        return: (boolean) - ``true`` if the given type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``proxy_record_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if proxy_record_type is None:
            raise NullArgument()
        return False

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        return: (osid.type.TypeList) - a list containing the supported
                ``ProxyCondition`` record types
        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList([])

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)

    def supports_proxy_condition_record_type(self, proxy_condition_record_type=None):
        """Tests if the given ``ProxyCondition`` record interface type is supported.

        arg:    proxy_condition_record_type (osid.type.Type): a ``Type``
                indicating a ``ProxyCondition`` record type
        return: (boolean) - ``true`` if the given type is supported,
                ``false`` otherwise
        raise:  NullArgument - ``proxy_condition_record_type`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if proxy_condition_record_type is None:
            raise NullArgument()
        return False


class ProxyManager(abc_proxy_managers.ProxyManager, osid_managers.OsidManager, ProxyProfile):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxy interfaces

    """

    def get_proxy_session(self):
        """Gets a ``ProxySession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        return: (osid.proxy.ProxySession) - a proxy session for this
                service
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proxy()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proxy()`` is ``true``.*

        """
        raise Unimplemented()

    proxy_session = property(fget=get_proxy_session)


class ProxyProxyManager(abc_proxy_managers.ProxyProxyManager, osid_managers.OsidProxyManager, ProxyProfile):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxies

    """

    def get_proxy_session(self, proxy=None):
        """Gets the ``OsidSession`` associated with the ``ProxySession`` using the supplied ``Proxy``.

        arg:    proxy (osid.proxy.Proxy): proxy
        return: (osid.proxy.ProxySession) - a ``ProxySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proxy()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proxy()`` is ``true``.*

        """
        if proxy is None:
            raise NullArgument()
        raise Unimplemented()
