# -*- coding: utf-8 -*-

# This module contains all the Proxy session classes for use with the MIT
# Core Concept Catalog (MC3) Handcar service.

from ...abstract_osid.proxy import sessions as abc_proxy_sessions
from ..osid import sessions as osid_sessions
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import AlreadyExists, NullArgument, InvalidArgument, NotFound, IllegalState, OperationFailed, PermissionDenied, Unsupported, Unimplemented
from . import rules


class ProxySession(abc_proxy_sessions.ProxySession, osid_sessions.OsidSession):
    """This session converts external data into a proxy for use in OSID proxy managers.

    The external data is specified in the form of a ``ProxyCondition``.

    """

    def get_proxy_condition(self):
        """Gets a proxy condition for acquiring a proxy.

        A new proxy condition should be acquired for each proxy request.

        :return: a proxy condiiton
        :rtype: ``osid.proxy.ProxyCondition``


        *compliance: mandatory -- This method is must be implemented.*

        """
        return rules.ProxyCondition()

    proxy_condition = property(fget=get_proxy_condition)

    def get_proxy(self, input):
        """Gets a proxy.

        :param input: a proxy condition
        :type input: ``osid.proxy.ProxyCondition``
        :return: a proxy
        :rtype: ``osid.proxy.Proxy``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``input`` is not of this service

        *compliance: mandatory -- This method is must be implemented.*

        """
        from ..authentication_process.objects import Authentication
        agent_id = input.user.username
        host = settings.HOST
        url_path = ('/handcar/services/authentication/agentkeys/' + agent_id +
                    '?proxyname=' + settings.APP_KEYS[host.lower()])
        authentication = Authentication(agent_id, self._get_request(url_path))

        return rules.Proxy(authentication=authentication)
