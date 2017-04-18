"""Implementations of configuration abstract base class query_inspectors."""
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


class ParameterQueryInspector:
    """Inspects a parameter query."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_syntax_terms(self):
        """Gets the value syntax query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SyntaxTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SyntaxTerm

    value_syntax_terms = property(fget=get_value_syntax_terms)

    @abc.abstractmethod
    def get_value_coordinate_type_terms(self):
        """Gets the coordinate record type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    value_coordinate_type_terms = property(fget=get_value_coordinate_type_terms)

    @abc.abstractmethod
    def get_value_heading_type_terms(self):
        """Gets the heading record type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    value_heading_type_terms = property(fget=get_value_heading_type_terms)

    @abc.abstractmethod
    def get_value_object_type_terms(self):
        """Gets the object value type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    value_object_type_terms = property(fget=get_value_object_type_terms)

    @abc.abstractmethod
    def get_value_spatial_unit_record_type_terms(self):
        """Gets the spatial unit record type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    value_spatial_unit_record_type_terms = property(fget=get_value_spatial_unit_record_type_terms)

    @abc.abstractmethod
    def get_value_version_scheme_terms(self):
        """Gets the version type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    value_version_scheme_terms = property(fget=get_value_version_scheme_terms)

    @abc.abstractmethod
    def get_value_terms(self):
        """Gets the value query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ValueQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueQueryInspector

    value_terms = property(fget=get_value_terms)

    @abc.abstractmethod
    def get_values_shuffled_terms(self):
        """Gets the shuffle query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    values_shuffled_terms = property(fget=get_values_shuffled_terms)

    @abc.abstractmethod
    def get_configuration_id_terms(self):
        """Gets the configuration ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    configuration_id_terms = property(fget=get_configuration_id_terms)

    @abc.abstractmethod
    def get_configuration_terms(self):
        """Gets the configuration query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ConfigurationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQueryInspector

    configuration_terms = property(fget=get_configuration_terms)

    @abc.abstractmethod
    def get_parameter_query_inspector_record(self, parameter_record_type):
        """Gets the parameter query record corresponding to the given ``Parameter`` record ``Type``.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: the parameter query inspector record
        :rtype: ``osid.configuration.records.ParameterQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterQueryInspectorRecord


class ValueQueryInspector:
    """The interface to inspect a value query."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_priority_terms(self):
        """Gets the priority query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CardinalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalRangeTerm

    priority_terms = property(fget=get_priority_terms)

    @abc.abstractmethod
    def get_boolean_value_terms(self):
        """Gets the boolean value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    boolean_value_terms = property(fget=get_boolean_value_terms)

    @abc.abstractmethod
    def get_bytes_value_terms(self):
        """Gets the bytes value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BytesTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BytesTerm

    bytes_value_terms = property(fget=get_bytes_value_terms)

    @abc.abstractmethod
    def get_cardinal_value_terms(self):
        """Gets the cardinal value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CardinalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CardinalRangeTerm

    cardinal_value_terms = property(fget=get_cardinal_value_terms)

    @abc.abstractmethod
    def get_coordinate_value_terms(self):
        """Gets the coordinate value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CoordinateTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CoordinateTerm

    coordinate_value_terms = property(fget=get_coordinate_value_terms)

    @abc.abstractmethod
    def get_currency_value_terms(self):
        """Gets the currency value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CurrencyTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CurrencyTerm

    currency_value_terms = property(fget=get_currency_value_terms)

    @abc.abstractmethod
    def get_date_time_value_terms(self):
        """Gets the date time value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DateTimeRangeTerm

    date_time_value_terms = property(fget=get_date_time_value_terms)

    @abc.abstractmethod
    def get_decimal_value_terms(self):
        """Gets the decimal value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DecimalRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DecimalRangeTerm

    decimal_value_terms = property(fget=get_decimal_value_terms)

    @abc.abstractmethod
    def get_distance_value_terms(self):
        """Gets the distance value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DistanceTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DistanceTerm

    distance_value_terms = property(fget=get_distance_value_terms)

    @abc.abstractmethod
    def get_duration_value_terms(self):
        """Gets the duration value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DurationTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.DurationTerm

    duration_value_terms = property(fget=get_duration_value_terms)

    @abc.abstractmethod
    def get_heading_value_terms(self):
        """Gets the heading value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.HeadingTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.HeadingTerm

    heading_value_terms = property(fget=get_heading_value_terms)

    @abc.abstractmethod
    def get_id_value_terms(self):
        """Gets the Id value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    id_value_terms = property(fget=get_id_value_terms)

    @abc.abstractmethod
    def get_integer_value_terms(self):
        """Gets the integer value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IntegerRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IntegerRangeTerm

    integer_value_terms = property(fget=get_integer_value_terms)

    @abc.abstractmethod
    def get_spatial_unit_value_terms(self):
        """Gets the spatial unit value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    spatial_unit_value_terms = property(fget=get_spatial_unit_value_terms)

    @abc.abstractmethod
    def get_speed_value_terms(self):
        """Gets the speed value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpeedTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpeedTerm

    speed_value_terms = property(fget=get_speed_value_terms)

    @abc.abstractmethod
    def get_string_value_terms(self):
        """Gets the string value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.StringTerm

    string_value_terms = property(fget=get_string_value_terms)

    @abc.abstractmethod
    def get_time_value_terms(self):
        """Gets the time value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TimeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TimeTerm

    time_value_terms = property(fget=get_time_value_terms)

    @abc.abstractmethod
    def get_type_value_terms(self):
        """Gets the type value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    type_value_terms = property(fget=get_type_value_terms)

    @abc.abstractmethod
    def get_version_value_terms(self):
        """Gets the version value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.VersionRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.VersionRangeTerm

    version_value_terms = property(fget=get_version_value_terms)

    @abc.abstractmethod
    def get_object_value_type_terms(self):
        """Gets the object value type query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.TypeTerm

    object_value_type_terms = property(fget=get_object_value_type_terms)

    @abc.abstractmethod
    def get_object_value_terms(self):
        """Gets the object value query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.ObjectTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.ObjectTerm

    object_value_terms = property(fget=get_object_value_terms)

    @abc.abstractmethod
    def get_parameter_id_terms(self):
        """Gets the parameter ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    parameter_id_terms = property(fget=get_parameter_id_terms)

    @abc.abstractmethod
    def get_parameter_terms(self):
        """Gets the parameter query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ParameterQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQueryInspector

    parameter_terms = property(fget=get_parameter_terms)

    @abc.abstractmethod
    def get_configuration_id_terms(self):
        """Gets the configuration ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    configuration_id_terms = property(fget=get_configuration_id_terms)

    @abc.abstractmethod
    def get_configuration_terms(self):
        """Gets the configuration query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ConfigurationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQueryInspector

    configuration_terms = property(fget=get_configuration_terms)

    @abc.abstractmethod
    def get_value_query_inspector_record(self, value_record_type):
        """Gets the value query record corresponding to the given ``Value`` record ``Type``.

        :param value_record_type: a value record type
        :type value_record_type: ``osid.type.Type``
        :return: the value query inspector record
        :rtype: ``osid.configuration.records.ValueQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueQueryInspectorRecord


class ConfigurationQueryInspector:
    """This is the query inspector for examining configuration queries."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_registry_terms(self):
        """Gets the registry query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.BooleanTerm

    registry_terms = property(fget=get_registry_terms)

    @abc.abstractmethod
    def get_parameter_id_terms(self):
        """Gets the parameter ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    parameter_id_terms = property(fget=get_parameter_id_terms)

    @abc.abstractmethod
    def get_parameter_terms(self):
        """Gets the parameter query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ParameterQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQueryInspector

    parameter_terms = property(fget=get_parameter_terms)

    @abc.abstractmethod
    def get_ancestor_configuration_id_terms(self):
        """Gets the ancestor configuration ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_configuration_id_terms = property(fget=get_ancestor_configuration_id_terms)

    @abc.abstractmethod
    def get_ancestor_configuration_terms(self):
        """Gets the ancestor configuration query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ConfigurationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQueryInspector

    ancestor_configuration_terms = property(fget=get_ancestor_configuration_terms)

    @abc.abstractmethod
    def get_descendant_configuration_id_terms(self):
        """Gets the descendant configuration ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_configuration_id_terms = property(fget=get_descendant_configuration_id_terms)

    @abc.abstractmethod
    def get_descendant_configuration_terms(self):
        """Gets the descendant configuration query terms.

        :return: the query terms
        :rtype: ``osid.configuration.ConfigurationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQueryInspector

    descendant_configuration_terms = property(fget=get_descendant_configuration_terms)

    @abc.abstractmethod
    def get_configuration_query_inspector_record(self, configuration_record_type):
        """Gets the configuration query inspector record corresponding to the given ``Configuration`` record ``Type``.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration query inspector record
        :rtype: ``osid.configuration.records.ConfigurationQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationQueryInspectorRecord
