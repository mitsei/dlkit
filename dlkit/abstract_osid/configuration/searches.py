"""Implementations of configuration abstract base class searches."""
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


class ParameterSearch:
    """``ParameterSearch`` specifies the interface for specifying parameter search options."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_parameters(self, parameter_ids):
        """Executes this search among a given list of parameters.

        :param parameter_ids: list of parameters
        :type parameter_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``parameter_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_parameter_results(self, parameter_search_order):
        """Specify an ordering to the search results.

        :param parameter_search_order: parameter search order
        :type parameter_search_order: ``osid.configuration.ParameterSearchOrder``
        :raise: ``NullArgument`` -- ``parameter_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``parameter_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_parameter_search_record(self, parameter_search_record_type):
        """Gets the parameter search record corresponding to the given parameter search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param parameter_search_record_type: a parameter search record type
        :type parameter_search_record_type: ``osid.type.Type``
        :return: the parameter search record
        :rtype: ``osid.configuration.records.ParameterSearchRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterSearchRecord


class ParameterSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_parameters(self):
        """Gets the parameter list resulting from a search.

        :return: the parameter list
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    parameters = property(fget=get_parameters)

    @abc.abstractmethod
    def get_parameter_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the parameter query inspector
        :rtype: ``osid.configuration.ParameterQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQueryInspector

    parameter_query_inspector = property(fget=get_parameter_query_inspector)

    @abc.abstractmethod
    def get_parameter_search_results_record(self, parameter_search_record_type):
        """Gets the parameter search results record corresponding to the given parameter search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param parameter_search_record_type: a parameter search record type
        :type parameter_search_record_type: ``osid.type.Type``
        :return: the parameter search results record
        :rtype: ``osid.configuration.records.ParameterSearchResultsRecord``
        :raise: ``NullArgument`` -- ``parameter_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterSearchResultsRecord


class ValueSearch:
    """The interface for governing value searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_values(self, value_ids):
        """Executes this search among a given list of values.

        :param value_ids: list of values
        :type value_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``value_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_value_results(self, value_search_order):
        """Specify an ordering to the search results.

        :param value_search_order: value search order
        :type value_search_order: ``osid.configuration.ValueSearchOrder``
        :raise: ``NullArgument`` -- ``value_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``value_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_value_search_record(self, value_search_record_type):
        """Gets the value search record corresponding to the given value search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param value_search_record_type: a value search record type
        :type value_search_record_type: ``osid.type.Type``
        :return: the value search record
        :rtype: ``osid.configuration.records.ValueSearchRecord``
        :raise: ``NullArgument`` -- ``value_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueSearchRecord


class ValueSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_values(self):
        """Gets the vakue list resulting from a search.

        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    values = property(fget=get_values)

    @abc.abstractmethod
    def get_value_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the value query inspector
        :rtype: ``osid.configuration.ValueQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueQueryInspector

    value_query_inspector = property(fget=get_value_query_inspector)

    @abc.abstractmethod
    def get_value_search_results_record(self, value_search_record_type):
        """Gets the value search results record corresponding to the given value search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param value_search_record_type: a value search record type
        :type value_search_record_type: ``osid.type.Type``
        :return: the value search results record
        :rtype: ``osid.configuration.records.ValueSearchResultsRecord``
        :raise: ``NullArgument`` -- ``value_search_record_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_search_record_type) is false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueSearchResultsRecord


class ConfigurationSearch:
    """The search interface to query a configuration."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_configurations(self, configuration_ids):
        """Execute this search among the given list of configurations.

        :param configuration_ids: list of configurations
        :type configuration_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_configuration_results(self, configuration_search_order):
        """Specify an ordering to the search results.

        :param configuration_search_order: configuration search order
        :type configuration_search_order: ``osid.configuration.ConfigurationSearchOrder``
        :raise: ``NullArgument`` -- ``configuration_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``configuration_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_configuration_search_record(self, configuration_search_record_type):
        """Gets the configuration search record corresponding to the given configuration search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param configuration_search_record_type: a configuration search record type
        :type configuration_search_record_type: ``osid.type.Type``
        :return: the configuration search record
        :rtype: ``osid.configuration.records.ConfigurationSearchRecord``
        :raise: ``NullArgument`` -- ``configuration_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationSearchRecord


class ConfigurationSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configurations(self):
        """Gets the configuration list resulting from a search.

        :return: the configuration list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    configurations = property(fget=get_configurations)

    @abc.abstractmethod
    def get_configuration_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the configuration query inspector
        :rtype: ``osid.configuration.ConfigurationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQueryInspector

    configuration_query_inspector = property(fget=get_configuration_query_inspector)

    @abc.abstractmethod
    def get_configuration_search_results_record(self, configuration_search_record_type):
        """Gets the configuration search results record corresponding to the given configuration search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param configuration_search_record_type: a configuration search record type
        :type configuration_search_record_type: ``osid.type.Type``
        :return: the configuration search results
        :rtype: ``osid.configuration.records.ConfigurationSearchResultsRecord``
        :raise: ``NullArgument`` -- ``configuration_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_search_record_type) is false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationSearchResultsRecord
