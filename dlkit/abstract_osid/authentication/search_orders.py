"""Implementations of authentication abstract base class search_orders."""
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


class AgentSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_resource(self, style):
        """Orders the results by resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_resource_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a resource search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_search_order(self):
        """Gets the resource search order.

        :return: the resource search odrer
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    @abc.abstractmethod
    def get_agent_search_order_record(self, agent_record_type):
        """Gets the agent search order record corresponding to the given agent record ``Type``.

        Multiple retrievals return the same underlying object.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent search order record
        :rtype: ``osid.authentication.records.AgentSearchOrderRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgentSearchOrderRecord


class AgencySearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_agency_search_order_record(self, agency_record_type):
        """Gets the agency search order record corresponding to the given agency record ``Type``.

        Multiple retrievals return the same underlying object.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency search order record
        :rtype: ``osid.authentication.records.AgencySearchOrderRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.authentication.records.AgencySearchOrderRecord
