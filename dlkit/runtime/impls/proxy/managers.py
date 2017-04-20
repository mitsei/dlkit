# -*- coding: utf-8 -*-

# This module contains all the Proxy manager classes for use with the MIT
# Core Concept Catalog (MC3) Handcar service.

from dlkit.abstract_osid.proxy import managers as abc_proxy_managers
from ..osid import managers as osid_managers
from .. import profile
from ..primitives import Id, DisplayText, Type
from ..type.objects import TypeList
from ..osid.osid_errors import NullArgument, OperationFailed, Unimplemented


class ProxyProfile(abc_proxy_managers.ProxyProfile, osid_managers.OsidProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""

    def supports_proxy(self):
        """Tests if a proxy session is supported.

        :return: ``true`` if proxy is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        *compliance: mandatory -- This method must be implemented.*

        """
        return 'supports_proxy' in profile.SUPPORTS

    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.

        :return: a list containing the supported ``Proxy`` record types
        :rtype: ``osid.type.TypeList``

        *compliance: mandatory -- This method must be implemented.*

        """
        from ..type.objects import TypeList
        return TypeList([])

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, proxy_record_type):
        """Tests if the given ``Proxy`` record interface type is supported.

        :param proxy_record_type: a ``Type`` indicating a ``Proxy`` record type
        :type proxy_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return proxy_record_type in self.get_proxy_record_types()

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        :return: a list containing the supported ``ProxyCondition`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return TypeList(profile.PROXY_CONDITION_RECORD_TYPES)

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)

    def supports_proxy_condition_record_type(self, proxy_condition_record_type):
        """Tests if the given ``ProxyCondition`` record interface type is supported.

        :param proxy_condition_record_type: a ``Type`` indicating a ``ProxyCondition`` record type
        :type proxy_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_condition_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return proxy_condition_record_type in self.get_proxy_condition_record_types()


class ProxyManager(abc_proxy_managers.ProxyManager, osid_managers.OsidManager, ProxyProfile):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxy interfaces
    """

    def get_proxy_session(self):
        """Gets a ``ProxySession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        :return: a proxy session for this service
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``

        *compliance: optional -- This method must be implemented if ``supports_proxy()`` is ``true``.*

        """
        if not self.supports_proxy():
            raise Unimplemented()
        try:
            from . import sessions
        except ImportError:
            raise  # OperationFailed()
        try:
            session = sessions.ProxySession()
        except AttributeError:
            raise  # OperationFailed()
        return session

    proxy_session = property(fget=get_proxy_session)


class ProxyProxyManager(abc_proxy_managers.ProxyProxyManager, osid_managers.OsidProxyManager, ProxyProfile):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxies
    """

    def get_proxy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``ProxySession`` using the supplied ``Proxy``.

        :param proxy: proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProxySession``
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``

        *compliance: optional -- This method must be implemented if ``supports_proxy()`` is ``true``.*

        """
        raise Unimplemented()
