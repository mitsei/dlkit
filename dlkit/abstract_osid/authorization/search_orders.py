"""Implementations of authorization abstract base class search_orders."""
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


class AuthorizationSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_resource(self, style):
        """Specifies a preference for ordering the result set by the resource.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_resource_search_order(self):
        """Tests if a ``Resource`` is available.

        :return: ``true`` if a resource search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_search_order(self):
        """Gets the resource search order.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    @abc.abstractmethod
    def order_by_trust(self, style):
        """Specifies a preference for ordering the result set by the trust.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_agent(self, style):
        """Specifies a preference for ordering the result set by the agent.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_agent_search_order(self):
        """Tests if an ``Agent`` is available.

        :return: ``true`` if an agent search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_search_order(self):
        """Gets the agent search order.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_agent_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_search_order()`` is ``true``.*

        """
        return  # osid.authentication.AgentSearchOrder

    agent_search_order = property(fget=get_agent_search_order)

    @abc.abstractmethod
    def order_by_function(self, style):
        """Specifies a preference for ordering the result set by the active status.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_function_search_order(self):
        """Tests if a ``Function`` is available.

        :return: ``true`` if a function search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_function_search_order(self):
        """Gets the function search order.

        :return: the function search order
        :rtype: ``osid.authorization.FunctionSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_function_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search_order()`` is ``true``.*

        """
        return  # osid.authorization.FunctionSearchOrder

    function_search_order = property(fget=get_function_search_order)

    @abc.abstractmethod
    def order_by_qualifier(self, style):
        """Specifies a preference for ordering the result set by the qualifier,.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_qualifier_search_order(self):
        """Tests if a ``Qualifier`` is available.

        :return: ``true`` if a qualifier search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_search_order(self):
        """Gets the qualifier search order.

        :return: the qualifier search order
        :rtype: ``osid.authorization.QualifierSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_qualifier_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_search_order()`` is ``true``.*

        """
        return  # osid.authorization.QualifierSearchOrder

    qualifier_search_order = property(fget=get_qualifier_search_order)

    @abc.abstractmethod
    def get_authorization_search_order_record(self, authorization_record_type):
        """Gets the authorization search order record corresponding to the given function record ``Type``.

        Multiple retrievals return the same underlying object.

        :param authorization_record_type: an authorization record type
        :type authorization_record_type: ``osid.type.Type``
        :return: the authorization search order record
        :rtype: ``osid.authorization.records.AuthorizationSearchOrderRecord``
        :raise: ``NullArgument`` -- ``authorization_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.AuthorizationSearchOrderRecord


class FunctionSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_qualifier_hierarchy(self, style):
        """Specified a preference for ordering results by the qualifier hierarchy.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_qualifier_hierarchy_search_order(self):
        """Tests if a ``HierarchySearchOrder`` interface is available.

        :return: ``true`` if a qualifier hierarchy search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_qualifier_hierarchy_search_order(self):
        """Gets the search order interface for a qualifier hierarchy.

        :return: the hierarchy search order
        :rtype: ``osid.hierarchy.HierarchySearchOrder``
        :raise: ``Unimplemented`` -- ``supports_qualifier_hierarchy_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_qualifier_hierarchy_search_order()`` is ``true``.*

        """
        return  # osid.hierarchy.HierarchySearchOrder

    qualifier_hierarchy_search_order = property(fget=get_qualifier_hierarchy_search_order)

    @abc.abstractmethod
    def get_function_search_order_record(self, function_record_type):
        """Gets the function search order record corresponding to the given function record ``Type``.

        Multiple retrievals return the same underlying object.

        :param function_record_type: a function record type
        :type function_record_type: ``osid.type.Type``
        :return: the function search order record
        :rtype: ``osid.authorization.records.FunctionSearchOrderRecord``
        :raise: ``NullArgument`` -- ``function_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(function_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.FunctionSearchOrderRecord


class QualifierSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_qualifier_search_order_record(self, qualifier_record_type):
        """Gets the qualifier search order record corresponding to the given qualifier record ``Type``.

        Multiple retrievals return the same underlying object.

        :param qualifier_record_type: a qualifier record type
        :type qualifier_record_type: ``osid.type.Type``
        :return: the qualifier search order record
        :rtype: ``osid.authorization.records.QualifierSearchOrderRecord``
        :raise: ``NullArgument`` -- ``qualifier_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(qualifier_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.QualifierSearchOrderRecord


class VaultSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_vault_search_order_record(self, vault_record_type):
        """Gets the vault search order record corresponding to the given vault record ``Type``.

        Multiple retrievals return the same underlying object.

        :param vault_record_type: a vault record type
        :type vault_record_type: ``osid.type.Type``
        :return: the vault search order record
        :rtype: ``osid.authorization.records.VaultSearchOrderRecord``
        :raise: ``NullArgument`` -- ``vault_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(vault_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authorization.records.VaultSearchOrderRecord
