"""Implementations of id abstract base class managers."""
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


class IdProfile:
    """The ``IdProfile`` describes the interoperability among id services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_id_lookup(self):
        """Tests if ``Id`` lookup is supported.

        :return: ``true`` if ``Id`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_id_issue(self):
        """Tests if an ``Id`` issue service is supported.

        :return: ``true`` if ``Id`` issuing is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_id_admin(self):
        """Tests if an ``Id`` administrative service is supported.

        :return: ``true`` if ``Id`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_id_batch(self):
        """Tests for the availability of an Id batch service.

        :return: ``true`` if an Id batch service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class IdManager:
    """This manager provides access to the available sessions of the Id service.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier.

    The ``IdLookupSession`` can be used for mapping one ``Id`` to
    another in addition to getting a list of the assigned identifiers.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_id_lookup_session(self):
        """Gets the session associated with the id lookup service.

        :return: an ``IdLookupSession``
        :rtype: ``osid.id.IdLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_lookup()`` is ``true``.*

        """
        return  # osid.id.IdLookupSession

    id_lookup_session = property(fget=get_id_lookup_session)

    @abc.abstractmethod
    def get_id_issue_session(self):
        """Gets the session associated with the id issue service.

        :return: an ``IdIssueSession``
        :rtype: ``osid.id.IdIssueSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_issue()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_issue()`` is ``true``.*

        """
        return  # osid.id.IdIssueSession

    id_issue_session = property(fget=get_id_issue_session)

    @abc.abstractmethod
    def get_id_admin_session(self):
        """Gets the session associated with the id admin service.

        :return: an ``IdAdminSession``
        :rtype: ``osid.id.IdAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_admin()`` is ``true``.*

        """
        return  # osid.id.IdAdminSession

    id_admin_session = property(fget=get_id_admin_session)

    @abc.abstractmethod
    def get_id_batch_manager(self):
        """Gets an ``IdBatchManager``.

        :return: an ``IdBatchManager``
        :rtype: ``osid.id.batch.IdBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_batch()`` is ``true``.*

        """
        return  # osid.id.batch.IdBatchManager

    id_batch_manager = property(fget=get_id_batch_manager)


class IdProxyManager:
    """This manager provides access to the available sessions of the Id service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of pasisng information from a server envrionment.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier. The ``IdBrowserSession``
    can be used for mapping one ``Id`` to another in addition to getting
    a list of the assigned identifiers.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_id_lookup_session(self, proxy):
        """Gets the session associated with the id lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdLookupSession``
        :rtype: ``osid.id.IdLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_lookup()`` is ``true``.*

        """
        return  # osid.id.IdLookupSession

    @abc.abstractmethod
    def get_id_issue_session(self, proxy):
        """Gets the session associated with the id issue service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdIssueSession``
        :rtype: ``osid.id.IdIssueSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_id_issue()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_issue()`` is ``true``.*

        """
        return  # osid.id.IdIssueSession

    @abc.abstractmethod
    def get_id_admin_session(self, proxy):
        """Gets the session associated with the id administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdAdminSession``
        :rtype: ``osid.id.IdAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_id_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_admin()`` is ``true``.*

        """
        return  # osid.id.IdAdminSession

    @abc.abstractmethod
    def get_id_batch_proxy_manager(self):
        """Gets an ``IdnProxyManager``.

        :return: an ``IdBatchProxyManager``
        :rtype: ``osid.id.batch.IdBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_batch()`` is ``true``.*

        """
        return  # osid.id.batch.IdBatchProxyManager

    id_batch_proxy_manager = property(fget=get_id_batch_proxy_manager)
