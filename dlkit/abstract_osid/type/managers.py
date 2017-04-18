"""Implementations of type abstract base class managers."""
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


class TypeProfile:
    """The ``TypeProfile`` describes the interoperability among type services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_type_lookup(self):
        """Tests if ``Type`` lookup is supported.

        :return: ``true`` if ``Type`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_type_admin(self):
        """Tests if a ``Type`` administrative service is supported.

        :return: ``true`` if ``Type`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class TypeManager:
    """This manager provides access to the available sessions of the type service.

    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_type_lookup_session(self):
        """Gets the ``OsidSession`` associated with the type lookup service.

        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*

        """
        return  # osid.type.TypeLookupSession

    type_lookup_session = property(fget=get_type_lookup_session)

    @abc.abstractmethod
    def get_type_admin_session(self):
        """Gets the ``OsidSession`` associated with the type admin service.

        :return: a ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*

        """
        return  # osid.type.TypeAdminSession

    type_admin_session = property(fget=get_type_admin_session)


class TypeProxyManager:
    """This manager provides access to the available sessions of the type service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_type_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the type lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TypeLookupSession``
        :rtype: ``osid.type.TypeLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_type_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_type_lookup()`` is ``true``.*

        """
        return  # osid.type.TypeLookupSession

    @abc.abstractmethod
    def get_type_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``TypeAdmin`` service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: the new ``TypeAdminSession``
        :rtype: ``osid.type.TypeAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_type_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_type_admin()`` is ``true``.*

        """
        return  # osid.type.TypeAdminSession
