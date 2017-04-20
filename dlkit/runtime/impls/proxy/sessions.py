# -*- coding: utf-8 -*-

# This module contains all the Proxy session classes for use by the DLKit
# consumer services API.

from dlkit.abstract_osid.proxy import sessions as abc_proxy_sessions
from ..osid import sessions as osid_sessions
from ..authentication_process.objects import DjangoAuthentication, XBlockAuthentication
from .. import settings
from ..primitives import Id, Type, DisplayText
from ..osid.osid_errors import *
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

    def get_proxy(self, input_):
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
        if input_._http_request is not None:
            authentication = DjangoAuthentication()
            authentication.set_django_user(input_._http_request.user, input_._use_user_id)
        elif input_._xblock_user is not None:
            authentication = XBlockAuthentication()
            authentication.set_xblock_user(input_._xblock_user)
        else:
            authentication = None

        if authentication is not None:
            effective_agent_id = authentication.get_agent_id()
        else:
            effective_agent_id = input_._effective_agent_id

        if input_._locale is not None:
            locale = input_._locale
        else:
            locale = None
        return rules.Proxy(authentication=authentication,
                           effective_agent_id=effective_agent_id,
                           locale=locale)
