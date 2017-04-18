"""Implementations of osid abstract base class metadata."""
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


class Metadata:
    """The ``Metadata`` interface defines a set of methods describing a the syntax and rules for creating and updating a data element inside an ``OsidForm``.

    This interface provides a means to retrieve special restrictions
    placed upon data elements such as sizes and ranges that may vary
    from provider to provider or from object to object.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_element_id(self):
        """Gets a unique ``Id`` for the data element.

        :return: an ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    element_id = property(fget=get_element_id)

    @abc.abstractmethod
    def get_element_label(self):
        """Gets a display label for the data element.

        :return: a display label
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    element_label = property(fget=get_element_label)

    @abc.abstractmethod
    def get_instructions(self):
        """Gets instructions for updating this element value.

        This is a human readable description of the data element or
        property that may include special instructions or caveats to the
        end-user above and beyond what this interface provides.

        :return: instructions
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    instructions = property(fget=get_instructions)

    @abc.abstractmethod
    def get_syntax(self):
        """Gets the syntax of this data.

        :return: an enumeration indicating thetype of value
        :rtype: ``osid.Syntax``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Syntax

    syntax = property(fget=get_syntax)

    @abc.abstractmethod
    def is_array(self):
        """Tests if this data element is an array.

        :return: ``true`` if this data is an array, ``false`` if a single element
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_required(self):
        """Tests if this data element is required for creating new objects.

        :return: ``true`` if this element value is required, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_read_only(self):
        """Tests if this data can be updated.

        This may indicate the result of a pre-authorization but is not a
        guarantee that an authorization failure will not occur when the
        create or update transaction is issued.

        :return: ``true`` if this data is not updatable, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_linked(self):
        """Tests if this data element is linked to other data in the object.

        Updating linked data elements should refresh all metadata and
        revalidate object elements.

        :return: true if this element is linked, false if updates have no side effect
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_value_known(self):
        """Tests if an existing value is known for this data element.

        If it is known that a value does not exist, then this method
        returns ``true``.

        :return: ``true`` if the element value is known, ``false`` if the element value is not known
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def has_value(self):
        """Tests if this data element has a set non-default value.

        :return: ``true`` if this element value has been set, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_units(self):
        """Gets the units of this data for display purposes ('lbs', 'gills', 'furlongs').

        :return: the display units of this data or an empty string if not applicable
        :rtype: ``osid.locale.DisplayText``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.locale.DisplayText

    units = property(fget=get_units)

    @abc.abstractmethod
    def get_minimum_elements(self):
        """In the case where an array or list of elements is specified in an ``OsidForm,`` this specifies the minimum number of elements that must be included.

        :return: the minimum elements or ``1`` if ``is_array()`` is ``false``
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    minimum_elements = property(fget=get_minimum_elements)

    @abc.abstractmethod
    def get_maximum_elements(self):
        """In the case where an array or list of elements is specified in an ``OsidForm,`` this specifies the maximum number of elements that can be specified.

        :return: the maximum elements or ``1`` if ``is_array()`` is ``false``
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    maximum_elements = property(fget=get_maximum_elements)

    @abc.abstractmethod
    def get_minimum_cardinal(self):
        """Gets the minimum cardinal value.

        :return: the minimum cardinal
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``CARDINAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    minimum_cardinal = property(fget=get_minimum_cardinal)

    @abc.abstractmethod
    def get_maximum_cardinal(self):
        """Gets the maximum cardinal value.

        :return: the maximum cardinal
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``CARDINAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    maximum_cardinal = property(fget=get_maximum_cardinal)

    @abc.abstractmethod
    def get_cardinal_set(self):
        """Gets the set of acceptable cardinal values.

        :return: a set of cardinals or an empty array if not restricted
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``CARDINAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    cardinal_set = property(fget=get_cardinal_set)

    @abc.abstractmethod
    def get_default_cardinal_values(self):
        """Gets the default cardinal values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default cardinal values
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``CARDINAL`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    default_cardinal_values = property(fget=get_default_cardinal_values)

    @abc.abstractmethod
    def get_existing_cardinal_values(self):
        """Gets the existing cardinal values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing cardinal values
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``CARDINAL`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    existing_cardinal_values = property(fget=get_existing_cardinal_values)

    @abc.abstractmethod
    def get_coordinate_types(self):
        """Gets the set of acceptable coordinate types.

        :return: the set of coordinate types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE or SPATIALUNIT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    coordinate_types = property(fget=get_coordinate_types)

    @abc.abstractmethod
    def supports_coordinate_type(self, coordinate_type):
        """Tests if the given coordinate type is supported.

        :param coordinate_type: a coordinate Type
        :type coordinate_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_axes_for_coordinate_type(self, coordinate_type):
        """Gets the number of axes for a given supported coordinate type.

        :param coordinate_type: a coordinate Type
        :type coordinate_type: ``osid.type.Type``
        :return: the number of axes
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_coordinate_type(coordinate_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def get_minimum_coordinate_values(self, coordinate_type):
        """Gets the minimum coordinate values given supported coordinate type.

        :param coordinate_type: a coordinate Type
        :type coordinate_type: ``osid.type.Type``
        :return: the minimum coordinate values
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_coordinate_type(coordinate_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    @abc.abstractmethod
    def get_maximum_coordinate_values(self, coordinate_type):
        """Gets the maximum coordinate values given supported coordinate type.

        :param coordinate_type: a coordinate Type
        :type coordinate_type: ``osid.type.Type``
        :return: the maximum coordinate values
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_coordinate_type(coordinate_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    @abc.abstractmethod
    def get_coordinate_set(self):
        """Gets the set of acceptable coordinate values.

        :return: a set of coordinates or an empty array if not restricted
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    coordinate_set = property(fget=get_coordinate_set)

    @abc.abstractmethod
    def get_default_coordinate_values(self):
        """Gets the default coordinate values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default coordinate values
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    default_coordinate_values = property(fget=get_default_coordinate_values)

    @abc.abstractmethod
    def get_existing_coordinate_values(self):
        """Gets the existing coordinate values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing coordinate values
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- syntax is not a ``COORDINATE`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    existing_coordinate_values = property(fget=get_existing_coordinate_values)

    @abc.abstractmethod
    def get_currency_types(self):
        """Gets the set of acceptable currency types.

        :return: the set of currency types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    currency_types = property(fget=get_currency_types)

    @abc.abstractmethod
    def supports_currency_type(self, currency_type):
        """Tests if the given currency type is supported.

        :param currency_type: a currency Type
        :type currency_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY``
        :raise: ``NullArgument`` -- ``currency_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_minimum_currency(self):
        """Gets the minimum currency value.

        :return: the minimum currency
        :rtype: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    minimum_currency = property(fget=get_minimum_currency)

    @abc.abstractmethod
    def get_maximum_currency(self):
        """Gets the maximum currency value.

        :return: the maximum currency
        :rtype: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    maximum_currency = property(fget=get_maximum_currency)

    @abc.abstractmethod
    def get_currency_set(self):
        """Gets the set of acceptable currency values.

        :return: a set of currencies or an empty array if not restricted
        :rtype: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    currency_set = property(fget=get_currency_set)

    @abc.abstractmethod
    def get_default_currency_values(self):
        """Gets the default currency values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default currency values
        :rtype: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    default_currency_values = property(fget=get_default_currency_values)

    @abc.abstractmethod
    def get_existing_currency_values(self):
        """Gets the existing currency values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing currency values
        :rtype: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- syntax is not a ``CURRENCY`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    existing_currency_values = property(fget=get_existing_currency_values)

    @abc.abstractmethod
    def get_date_time_resolution(self):
        """Gets the smallest resolution of the date time value.

        :return: the resolution
        :rtype: ``osid.calendaring.DateTimeResolution``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME, DURATION`` , or ``TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTimeResolution

    date_time_resolution = property(fget=get_date_time_resolution)

    @abc.abstractmethod
    def get_calendar_types(self):
        """Gets the set of acceptable calendar types.

        :return: the set of calendar types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME`` or ``DURATION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    calendar_types = property(fget=get_calendar_types)

    @abc.abstractmethod
    def supports_calendar_type(self, calendar_type):
        """Tests if the given calendar type is supported.

        :param calendar_type: a calendar Type
        :type calendar_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME`` or ``DURATION``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_time_types(self):
        """Gets the set of acceptable time types.

        :return: a set of time types or an empty array if not restricted
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME, DURATION,`` or ``TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    time_types = property(fget=get_time_types)

    @abc.abstractmethod
    def supports_time_type(self, time_type):
        """Tests if the given time type is supported.

        :param time_type: a time Type
        :type time_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME, DURATION,`` or ``TIME``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_minimum_date_time(self):
        """Gets the minimum date time value.

        :return: the minimum value
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    minimum_date_time = property(fget=get_minimum_date_time)

    @abc.abstractmethod
    def get_maximum_date_time(self):
        """Gets the maximum date time value.

        :return: the maximum value
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    maximum_date_time = property(fget=get_maximum_date_time)

    @abc.abstractmethod
    def get_date_time_set(self):
        """Gets the set of acceptable date time values.

        :return: a set of values or an empty array if not restricted
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    date_time_set = property(fget=get_date_time_set)

    @abc.abstractmethod
    def get_default_date_time_values(self):
        """Gets the default date time values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default date time values
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    default_date_time_values = property(fget=get_default_date_time_values)

    @abc.abstractmethod
    def get_existing_date_time_values(self):
        """Gets the existing date time values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing date time values
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- syntax is not a ``DATETIME`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    existing_date_time_values = property(fget=get_existing_date_time_values)

    @abc.abstractmethod
    def get_decimal_scale(self):
        """Gets the number of digits to the right of the decimal point.

        :return: the scale
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``DECIMAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    decimal_scale = property(fget=get_decimal_scale)

    @abc.abstractmethod
    def get_minimum_decimal(self):
        """Gets the minimum decimal value.

        :return: the minimum decimal
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``DECIMAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    minimum_decimal = property(fget=get_minimum_decimal)

    @abc.abstractmethod
    def get_maximum_decimal(self):
        """Gets the maximum decimal value.

        :return: the maximum decimal
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``DECIMAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    maximum_decimal = property(fget=get_maximum_decimal)

    @abc.abstractmethod
    def get_decimal_set(self):
        """Gets the set of acceptable decimal values.

        :return: a set of decimals or an empty array if not restricted
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``DECIMAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    decimal_set = property(fget=get_decimal_set)

    @abc.abstractmethod
    def get_default_decimal_values(self):
        """Gets the default decimal values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default decimal values
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``DECIMAL`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    default_decimal_values = property(fget=get_default_decimal_values)

    @abc.abstractmethod
    def get_existing_decimal_values(self):
        """Gets the existing decimal values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing decimal values
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``DECIMAL`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    existing_decimal_values = property(fget=get_existing_decimal_values)

    @abc.abstractmethod
    def get_distance_resolution(self):
        """Gets the smallest resolution of the distance value.

        :return: the resolution
        :rtype: ``osid.mapping.DistanceResolution``
        :raise: ``IllegalState`` -- syntax is not a ``DISTANCE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.DistanceResolution

    distance_resolution = property(fget=get_distance_resolution)

    @abc.abstractmethod
    def get_minimum_distance(self):
        """Gets the minimum distance value.

        :return: the minimum value
        :rtype: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- syntax is not a ``DISTANCE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    minimum_distance = property(fget=get_minimum_distance)

    @abc.abstractmethod
    def get_maximum_distance(self):
        """Gets the maximum distance value.

        :return: the maximum value
        :rtype: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- syntax is not a ``DISTANCE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    maximum_distance = property(fget=get_maximum_distance)

    @abc.abstractmethod
    def get_distance_set(self):
        """Gets the set of acceptable distance values.

        :return: a set of values or an empty array if not restricted
        :rtype: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- syntax is not a ``DISTANCE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    distance_set = property(fget=get_distance_set)

    @abc.abstractmethod
    def get_default_distance_values(self):
        """Gets the default distance values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default distance values
        :rtype: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- syntax is not a ``DISTANCE`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    default_distance_values = property(fget=get_default_distance_values)

    @abc.abstractmethod
    def get_existing_distance_values(self):
        """Gets the existing distance values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing distance values
        :rtype: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- syntax is not a ``DISTANCE`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    existing_distance_values = property(fget=get_existing_distance_values)

    @abc.abstractmethod
    def get_minimum_duration(self):
        """Gets the minimum duration.

        :return: the minimum duration
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- syntax is not a ``DURATION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    minimum_duration = property(fget=get_minimum_duration)

    @abc.abstractmethod
    def get_maximum_duration(self):
        """Gets the maximum duration.

        :return: the maximum duration
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- syntax is not a ``DURATION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    maximum_duration = property(fget=get_maximum_duration)

    @abc.abstractmethod
    def get_duration_set(self):
        """Gets the set of acceptable duration values.

        :return: a set of durations or an empty array if not restricted
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- syntax is not a ``DURATION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    duration_set = property(fget=get_duration_set)

    @abc.abstractmethod
    def get_default_duration_values(self):
        """Gets the default duration values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most at most a single value.

        :return: the default duration values
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- syntax is not a DURATION or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    default_duration_values = property(fget=get_default_duration_values)

    @abc.abstractmethod
    def get_existing_duration_values(self):
        """Gets the existing duration values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing duration values
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- syntax is not a ``DURATION`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    existing_duration_values = property(fget=get_existing_duration_values)

    @abc.abstractmethod
    def get_heading_types(self):
        """Gets the set of acceptable heading types.

        :return: a set of heading types or an empty array if not restricted
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    heading_types = property(fget=get_heading_types)

    @abc.abstractmethod
    def supports_heading_type(self, heading_type):
        """Tests if the given heading type is supported.

        :param heading_type: a heading Type
        :type heading_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_axes_for_heading_type(self, heading_type):
        """Gets the number of axes for a given supported heading type.

        :param heading_type: a heading Type
        :type heading_type: ``osid.type.Type``
        :return: the number of axes
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_heading_type(heading_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    @abc.abstractmethod
    def get_minimum_heading_values(self, heading_type):
        """Gets the minimum heading values given supported heading type.

        :param heading_type: a heading Type
        :type heading_type: ``osid.type.Type``
        :return: the minimum heading values
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_heading_type(heading_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    @abc.abstractmethod
    def get_maximum_heading_values(self, heading_type):
        """Gets the maximum heading values given supported heading type.

        :param heading_type: a heading Type
        :type heading_type: ``osid.type.Type``
        :return: the maximum heading values
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_heading_type(heading_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    @abc.abstractmethod
    def get_heading_set(self):
        """Gets the set of acceptable heading values.

        :return: the set of heading
        :rtype: ``osid.mapping.Heading``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Heading

    heading_set = property(fget=get_heading_set)

    @abc.abstractmethod
    def get_default_heading_values(self):
        """Gets the default heading values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default heading values
        :rtype: ``osid.mapping.Heading``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Heading

    default_heading_values = property(fget=get_default_heading_values)

    @abc.abstractmethod
    def get_existing_heading_values(self):
        """Gets the existing heading values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing heading values
        :rtype: ``osid.mapping.Heading``
        :raise: ``IllegalState`` -- syntax is not a ``HEADING`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Heading

    existing_heading_values = property(fget=get_existing_heading_values)

    @abc.abstractmethod
    def get_id_set(self):
        """Gets the set of acceptable ``Ids``.

        :return: a set of ``Ids`` or an empty array if not restricted
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- syntax is not an ``ID``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    id_set = property(fget=get_id_set)

    @abc.abstractmethod
    def get_default_id_values(self):
        """Gets the default ``Id`` values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default ``Id`` values
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- syntax is not an ``ID`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    default_id_values = property(fget=get_default_id_values)

    @abc.abstractmethod
    def get_existing_id_values(self):
        """Gets the existing ``Id`` values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing ``Id`` values
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- syntax is not an ``ID``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    existing_id_values = property(fget=get_existing_id_values)

    @abc.abstractmethod
    def get_minimum_integer(self):
        """Gets the minimum integer value.

        :return: the minimum value
        :rtype: ``integer``
        :raise: ``IllegalState`` -- syntax is not an ``INTEGER``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    minimum_integer = property(fget=get_minimum_integer)

    @abc.abstractmethod
    def get_maximum_integer(self):
        """Gets the maximum integer value.

        :return: the maximum value
        :rtype: ``integer``
        :raise: ``IllegalState`` -- syntax is not an ``INTEGER``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    maximum_integer = property(fget=get_maximum_integer)

    @abc.abstractmethod
    def get_integer_set(self):
        """Gets the set of acceptable integer values.

        :return: a set of values or an empty array if not restricted
        :rtype: ``integer``
        :raise: ``IllegalState`` -- syntax is not an ``INTEGER``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    integer_set = property(fget=get_integer_set)

    @abc.abstractmethod
    def get_default_integer_values(self):
        """Gets the default integer values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default integer values
        :rtype: ``integer``
        :raise: ``IllegalState`` -- syntax is not an ``INTEGER`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    default_integer_values = property(fget=get_default_integer_values)

    @abc.abstractmethod
    def get_existing_integer_values(self):
        """Gets the existing integer values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing integer values
        :rtype: ``integer``
        :raise: ``IllegalState`` -- syntax is not a ``INTEGER`` or isValueKnown() is false

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    existing_integer_values = property(fget=get_existing_integer_values)

    @abc.abstractmethod
    def get_object_types(self):
        """Gets the set of acceptable ``Types`` for an arbitrary object.

        :return: a set of ``Types`` or an empty array if not restricted
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not an ``OBJECT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    object_types = property(fget=get_object_types)

    @abc.abstractmethod
    def supports_object_type(self, object_type):
        """Tests if the given object type is supported.

        :param object_type: an object Type
        :type object_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not an ``OBJECT``
        :raise: ``NullArgument`` -- ``object_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_object_set(self):
        """Gets the set of acceptable object values.

        :return: a set of values or an empty array if not restricted
        :rtype: ``object``
        :raise: ``IllegalState`` -- syntax is not an ``OBJECT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # object

    object_set = property(fget=get_object_set)

    @abc.abstractmethod
    def get_default_object_values(self):
        """Gets the default object values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default object values
        :rtype: ``object``
        :raise: ``IllegalState`` -- syntax is not an ``OBJECT`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # object

    default_object_values = property(fget=get_default_object_values)

    @abc.abstractmethod
    def get_existing_object_values(self):
        """Gets the existing object values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing object values
        :rtype: ``object``
        :raise: ``IllegalState`` -- syntax is not an OBJECT or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # object

    existing_object_values = property(fget=get_existing_object_values)

    @abc.abstractmethod
    def get_spatial_unit_record_types(self):
        """Gets the set of acceptable spatial unit record types.

        :return: the set of spatial unit types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not ``SPATIALUNIT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    @abc.abstractmethod
    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if the given spatial unit record type is supported.

        :param spatial_unit_record_type: a spatial unit record Type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not an ``SPATIALUNIT``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_spatial_unit_set(self):
        """Gets the set of acceptable spatial unit values.

        :return: a set of spatial units or an empty array if not restricted
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- syntax is not a ``SPATIALUNIT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.SpatialUnit

    spatial_unit_set = property(fget=get_spatial_unit_set)

    @abc.abstractmethod
    def get_default_spatial_unit_values(self):
        """Gets the default spatial unit values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default spatial unit values
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- syntax is not a ``SPATIALUNIT`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.SpatialUnit

    default_spatial_unit_values = property(fget=get_default_spatial_unit_values)

    @abc.abstractmethod
    def get_existing_spatial_unit_values(self):
        """Gets the existing spatial unit values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing spatial unit values
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- syntax is not a SPATIALUNIT or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.SpatialUnit

    existing_spatial_unit_values = property(fget=get_existing_spatial_unit_values)

    @abc.abstractmethod
    def get_minimum_speed(self):
        """Gets the minimum speed value.

        :return: the minimum speed
        :rtype: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- syntax is not a ``SPEED``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Speed

    minimum_speed = property(fget=get_minimum_speed)

    @abc.abstractmethod
    def get_maximum_speed(self):
        """Gets the maximum speed value.

        :return: the maximum speed
        :rtype: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- syntax is not a ``SPEED``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Speed

    maximum_speed = property(fget=get_maximum_speed)

    @abc.abstractmethod
    def get_speed_set(self):
        """Gets the set of acceptable speed values.

        :return: a set of speeds or an empty array if not restricted
        :rtype: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- syntax is not a ``SPEED``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Speed

    speed_set = property(fget=get_speed_set)

    @abc.abstractmethod
    def get_default_speed_values(self):
        """Gets the default speed values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default speed values
        :rtype: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- syntax is not a ``SPEED`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Speed

    default_speed_values = property(fget=get_default_speed_values)

    @abc.abstractmethod
    def get_existing_speed_values(self):
        """Gets the existing speed values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing speed values
        :rtype: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- syntax is not a ``SPEED`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Speed

    existing_speed_values = property(fget=get_existing_speed_values)

    @abc.abstractmethod
    def get_minimum_string_length(self):
        """Gets the minimum string length.

        :return: the minimum string length
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    minimum_string_length = property(fget=get_minimum_string_length)

    @abc.abstractmethod
    def get_maximum_string_length(self):
        """Gets the maximum string length.

        :return: the maximum string length
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    maximum_string_length = property(fget=get_maximum_string_length)

    @abc.abstractmethod
    def get_string_match_types(self):
        """Gets the set of valid string match types for use in validating a string.

        If the string match type indicates a regular expression then
        ``get_string_expression()`` returns a regular expression.

        :return: the set of string match types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    string_match_types = property(fget=get_string_match_types)

    @abc.abstractmethod
    def supports_string_match_type(self, string_match_type):
        """Tests if the given string match type is supported.

        :param string_match_type: a string match type
        :type string_match_type: ``osid.type.Type``
        :return: ``true`` if the given string match type Is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``
        :raise: ``NullArgument`` -- ``string_match_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_string_expression(self, string_match_type):
        """Gets the regular expression of an acceptable string for the given string match type.

        :param string_match_type: a string match type
        :type string_match_type: ``osid.type.Type``
        :return: the regular expression
        :rtype: ``string``
        :raise: ``NullArgument`` -- ``string_match_type`` is ``null``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type`` ) is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    @abc.abstractmethod
    def get_string_format_types(self):
        """Gets the set of valid string formats.

        :return: the set of valid text format types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    string_format_types = property(fget=get_string_format_types)

    @abc.abstractmethod
    def get_string_set(self):
        """Gets the set of acceptable string values.

        :return: a set of strings or an empty array if not restricted
        :rtype: ``string``
        :raise: ``IllegalState`` -- syntax is not a ``STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    string_set = property(fget=get_string_set)

    @abc.abstractmethod
    def get_default_string_values(self):
        """Gets the default string values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default string values
        :rtype: ``string``
        :raise: ``IllegalState`` -- syntax is not a ``STRING`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    default_string_values = property(fget=get_default_string_values)

    @abc.abstractmethod
    def get_existing_string_values(self):
        """Gets the existing string values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing string values
        :rtype: ``string``
        :raise: ``IllegalState`` -- syntax is not a ``STRING`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    existing_string_values = property(fget=get_existing_string_values)

    @abc.abstractmethod
    def get_minimum_time(self):
        """Gets the minimum time value.

        :return: the minimum time
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- syntax is not a ``TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    minimum_time = property(fget=get_minimum_time)

    @abc.abstractmethod
    def get_maximum_time(self):
        """Gets the maximum time value.

        :return: the maximum time
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- syntax is not a ``TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    maximum_time = property(fget=get_maximum_time)

    @abc.abstractmethod
    def get_time_set(self):
        """Gets the set of acceptable time values.

        :return: a set of times or an empty array if not restricted
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- syntax is not a ``TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    time_set = property(fget=get_time_set)

    @abc.abstractmethod
    def get_default_time_values(self):
        """Gets the default time values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default time values
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- syntax is not a ``TIME`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    default_time_values = property(fget=get_default_time_values)

    @abc.abstractmethod
    def get_existing_time_values(self):
        """Gets the existing time values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing time values
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- syntax is not a ``TIME`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    existing_time_values = property(fget=get_existing_time_values)

    @abc.abstractmethod
    def get_type_set(self):
        """Gets the set of acceptable ``Types``.

        :return: a set of ``Types`` or an empty array if not restricted
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``TYPE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    type_set = property(fget=get_type_set)

    @abc.abstractmethod
    def get_default_type_values(self):
        """Gets the default type values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default type values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``TYPE`` or ``is_required()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    default_type_values = property(fget=get_default_type_values)

    @abc.abstractmethod
    def get_existing_type_values(self):
        """Gets the existing type values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing type values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``TYPE`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    existing_type_values = property(fget=get_existing_type_values)

    @abc.abstractmethod
    def get_version_types(self):
        """Gets the set of acceptable version types.

        :return: the set of version types
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- syntax is not a ``VERSION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    version_types = property(fget=get_version_types)

    @abc.abstractmethod
    def supports_version_type(self, version_type):
        """Tests if the given version type is supported.

        :param version_type: a version Type
        :type version_type: ``osid.type.Type``
        :return: ``true`` if the type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- syntax is not a ``VERSION``
        :raise: ``NullArgument`` -- ``version_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_minimum_version(self):
        """Gets the minumim acceptable ``Version``.

        :return: the minumim ``Version``
        :rtype: ``osid.installation.Version``
        :raise: ``IllegalState`` -- syntax is not a ``VERSION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    minimum_version = property(fget=get_minimum_version)

    @abc.abstractmethod
    def get_maximum_version(self):
        """Gets the maximum acceptable ``Version``.

        :return: the maximum ``Version``
        :rtype: ``osid.installation.Version``
        :raise: ``IllegalState`` -- syntax is not a ``VERSION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    maximum_version = property(fget=get_maximum_version)

    @abc.abstractmethod
    def get_version_set(self):
        """Gets the set of acceptable ``Versions``.

        :return: a set of ``Versions`` or an empty array if not restricted
        :rtype: ``osid.installation.Version``
        :raise: ``IllegalState`` -- syntax is not a ``VERSION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    version_set = property(fget=get_version_set)

    @abc.abstractmethod
    def get_default_version_values(self):
        """Gets the default version values.

        These are the values used if the element value is not provided
        or is cleared. If ``is_array()`` is false, then this method
        returns at most a single value.

        :return: the default version values
        :rtype: ``osid.installation.Version``
        :raise: ``IllegalState`` -- syntax is not a TIME or isValueKnown() is false

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    default_version_values = property(fget=get_default_version_values)

    @abc.abstractmethod
    def get_existing_version_values(self):
        """Gets the existing version values.

        If ``has_value()`` and ``is_required()`` are ``false,`` then
        these values are the default values ````. If ``is_array()`` is
        false, then this method returns at most a single value.

        :return: the existing version values
        :rtype: ``osid.installation.Version``
        :raise: ``IllegalState`` -- syntax is not a ``VERSION`` or ``is_value_known()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    existing_version_values = property(fget=get_existing_version_values)
