"""Implementations of logging abstract base class search_orders."""
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


class LogEntrySearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_priority(self, style):
        """Specifies a preference for ordering log entris by priority type.

        :param style: search otrder style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_timestamp(self, style):
        """Specifies a preference for ordering log entries by time.

        :param style: search otrder style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_resource(self, style):
        """Specifies a preference for ordering log entries by resource.

        :param style: search otrder style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_resource_search_order(self):
        """Tests if a resource order is available.

        :return: ``true`` if a resource order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_search_order(self):
        """Gets the resource order.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_search_order()`` is ``true``.*

        """
        return  # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    @abc.abstractmethod
    def order_by_agent(self, style):
        """Specifies a preference for ordering log entries by agent.

        :param style: search otrder style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_agent_search_order(self):
        """Tests if an agent order is available.

        :return: ``true`` if an agent order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_agent_search_order(self):
        """Gets the agent order.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_agent_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_agent_search_order()`` is ``true``.*

        """
        return  # osid.authentication.AgentSearchOrder

    agent_search_order = property(fget=get_agent_search_order)

    @abc.abstractmethod
    def get_log_entry_search_order_record(self, log_entry_record_type):
        """Gets the log entry search order record corresponding to the given log entry record ``Type``.

        Multiple retrievals return the same underlying object.

        :param log_entry_record_type: a log entry record type
        :type log_entry_record_type: ``osid.type.Type``
        :return: the log entry search order record
        :rtype: ``osid.logging.records.LogEntrySearchOrderRecord``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_entry_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.records.LogEntrySearchOrderRecord


class LogSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_log_search_order_record(self, log_record_type):
        """Gets the log search order record corresponding to the given log record Type.

        Multiple retrievals return the same underlying object.

        :param log_record_type: a log record type
        :type log_record_type: ``osid.type.Type``
        :return: the log search order record
        :rtype: ``osid.logging.records.LogSearchOrderRecord``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.logging.records.LogSearchOrderRecord
