"""Implementations of configuration abstract base class search_orders."""
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


class ParameterSearchOrder:
    """This interface specifies options for ordering search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_value_syntax(self, style):
        """Specifies a preference for ordering the results by the value syntax and object type.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_values_shuffled(self, style):
        """Specifies a preference for ordering the results by the shuffle flag.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_parameter_search_order_record(self, parameter_record_type):
        """Gets the parameter search order record corresponding to the given parameter record ``Type``.

        Multiple retrievals return the same underlying object.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: the parameter search order record
        :rtype: ``osid.configuration.records.ParameterSearchOrderRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterSearchOrderRecord


class ValueSearchOrder:
    """This interface specifies options for ordering search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_priority(self, style):
        """Specifies a preference for ordering the results by the value priority.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_by_value(self, style):
        """Specifies a preference for ordering the results by the value.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def supports_parameter_search_order(self):
        """Tests if a ``ParameterSearchOrder`` is available.

        :return: ``true`` if a parameter search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_search_order(self):
        """Gets the parameter search order.

        :return: the parameter search order
        :rtype: ``osid.configuration.ParameterSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_parameter_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented is
        ``supports_parameter_search_order()`` is ``true``.*

        """
        return  # osid.configuration.ParameterSearchOrder

    parameter_search_order = property(fget=get_parameter_search_order)

    @abc.abstractmethod
    def get_value_search_order_record(self, value_record_type):
        """Gets the value search order record corresponding to the given value record ``Type``.

        Multiple retrievals return the same underlying object.

        :param value_record_type: a value record type
        :type value_record_type: ``osid.type.Type``
        :return: the value search order record
        :rtype: ``osid.configuration.records.ValueSearchOrderRecord``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueSearchOrderRecord


class ConfigurationSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_search_order_record(self, configuration_record_type):
        """Gets the configuration search order record corresponding to the given configuration record ``Type``.

        Multiple retrievals return the same underlying object.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration search order record
        :rtype: ``osid.configuration.records.ConfigurationSearchOrderRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationSearchOrderRecord
