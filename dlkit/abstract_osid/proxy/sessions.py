"""Implementations of proxy abstract base class sessions."""
# pylint: disable=invalid-name
#     Method names comply with OSID specification.
# pylint: disable=no-init
#     Abstract classes do not define __init__.
# pylint: disable=too-few-public-methods
#     Some interfaces are specified as 'markers' and include no methods.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification
# pylint: disable=too-many-arguments
#     Argument signature defined in specification.
# pylint: disable=duplicate-code
#     All apparent duplicates have been inspected. They aren't.
import abc


class ProxySession:
    """This session converts external data into a proxy for use in OSID proxy managers.

    The external data is specified in the form of a ``ProxyCondition``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_proxy_condition(self):
        """Gets a proxy condition for acquiring a proxy.

        A new proxy condition should be acquired for each proxy request.

        :return: a proxy condiiton
        :rtype: ``osid.proxy.ProxyCondition``


        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.proxy.ProxyCondition

    proxy_condition = property(fget=get_proxy_condition)

    @abc.abstractmethod
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
        return  # osid.proxy.Proxy
