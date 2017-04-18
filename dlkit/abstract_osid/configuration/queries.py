"""Implementations of configuration abstract base class queries."""
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


class ParameterQuery:
    """The ``ParameterQuery`` is used to assemble search queries.

    A ``Parameter`` is available from a ``ParameterSearchSession`` and
    defines methods to query for a ``Parameter`` that includes setting a
    display name and a description. Once the desired parameters are set,
    the ``ParameterQuery`` is given to the designated search method. The
    same ``ParameterQuery`` returned from the session must be used in
    the search as the provider may utilize implementation-specific data
    wiithin the object.

    If multiple data elements are set, the results matching all the
    given data (eg: ``AND`` ) are returned. Search methods throughout
    the OSIDs accept multiple ``OsidQuery`` interfaces. Each
    ``ParameterQuery`` in the array behaves like an ``OR`` such that
    results are returned that match any of the given ``ParameterQuery``
    objects.

    Any match method inside a ``ParameterQuery`` may be invoked multiple
    times. In the case of a match method, each invocation adds an
    element to an ``OR`` expression. Any of these terms may also be
    negated through the ``match`` flag.
      Parameter { ParameterQuery.matchDisplayName AND (ParameterQuery.matchDescription OR Parameter.matchDescription)}
        OR ParameterQuery



    String searches are described using a string search Type that
    indicates the type of regular expression or wildcarding encoding.
    Compatibility with a strings search Type can be tested within this
    interface.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_value_syntax(self, syntax, match):
        """Adds a match for parameters of a given value syntax.

        Multiple matches can be added to perform a boolean ``OR`` among
        them.

        :param syntax: the parameter value syntax
        :type syntax: ``osid.Syntax``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``syntax`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_syntax_terms(self):
        """Clears the value syntax terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_syntax_terms = property(fdel=clear_value_syntax_terms)

    @abc.abstractmethod
    def match_value_coordinate_type(self, coordinate_type, match):
        """Adds a match for parameters with a given coordinate type for a coordinate value.

        Multiple matches can be added to perform a boolean ``OR`` among
        them.

        :param coordinate_type: the coordinate type
        :type coordinate_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_coordinate_type_terms(self):
        """Clears the coordinate type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_coordinate_type_terms = property(fdel=clear_value_coordinate_type_terms)

    @abc.abstractmethod
    def match_value_heading_type(self, heading_type, match):
        """Adds a match for parameters with a given heading type for a coordinate value.

        Multiple matches can be added to perform a boolean ``OR`` among
        them.

        :param heading_type: the heading type
        :type heading_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_heading_type_terms(self):
        """Clears the coorheadingdinate record type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_heading_type_terms = property(fdel=clear_value_heading_type_terms)

    @abc.abstractmethod
    def match_value_object_type(self, object_type, match):
        """Adds a match for parameters with a given object type for an object value.

        Multiple matches can be added to perform a boolean ``OR`` among
        them.

        :param object_type: the object type
        :type object_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``object_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_object_type_terms(self):
        """Clears the object value type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_object_type_terms = property(fdel=clear_value_object_type_terms)

    @abc.abstractmethod
    def match_value_spatial_unit_record_type(self, spatial_unit_record_type, match):
        """Adds a match for parameters with a given spatial unit record type for a coordinate value.

        Multiple matches can be added to perform a boolean ``OR`` among
        them.

        :param spatial_unit_record_type: the spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_spatial_unit_record_type_terms(self):
        """Clears the spatial unit record type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_spatial_unit_record_type_terms = property(fdel=clear_value_spatial_unit_record_type_terms)

    @abc.abstractmethod
    def match_value_version_scheme(self, version_type, match):
        """Adds a match for parameters with a given version type for a version value.

        Multiple matches can be added to perform a boolean ``OR`` among
        them.

        :param version_type: the version type
        :type version_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``version_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_version_scheme_terms(self):
        """Clears the value type terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_version_scheme_terms = property(fdel=clear_value_version_scheme_terms)

    @abc.abstractmethod
    def supports_value_query(self):
        """Tests if a ``ValueQuery`` is available.

        :return: ``true`` if a value query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_query(self):
        """Gets the query for a value.

        :return: the value query
        :rtype: ``osid.configuration.ValueQuery``
        :raise: ``Unimplemented`` -- ``supports_value_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_query()`` is ``true``.*

        """
        return  # osid.configuration.ValueQuery

    value_query = property(fget=get_value_query)

    @abc.abstractmethod
    def match_any_value(self, match):
        """Matches parameters that have any value.

        :param match: ``true`` to match parameters with any value, ``false`` to match parameters with no value
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_terms(self):
        """Clears the value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_terms = property(fdel=clear_value_terms)

    @abc.abstractmethod
    def match_values_shuffled(self, shuffle):
        """Matches shuffle order.

        :param shuffle: ``true`` to match shuffle by weight, false to match order by index
        :type shuffle: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_values_shuffled(self, match):
        """Matches parameters that have any shuffle value.

        :param match: ``true`` to match parameters with any shuffle value, ``false`` to match parameters with no shuffle
        value
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_values_shuffled_terms(self):
        """Clears the shuffle terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    values_shuffled_terms = property(fdel=clear_values_shuffled_terms)

    @abc.abstractmethod
    def match_configuration_id(self, configuration_id, match):
        """Sets the configuration ``Id`` for this query.

        :param configuration_id: a configuration ``Id``
        :type configuration_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_configuration_id_terms(self):
        """Clears the configuration ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    configuration_id_terms = property(fdel=clear_configuration_id_terms)

    @abc.abstractmethod
    def supports_configuration_query(self):
        """Tests if a ``ConfigurationQuery`` is available.

        :return: ``true`` if a configuration query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_query(self):
        """Gets the query for a configuration.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``Unimplemented`` -- ``supports_configuration_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_query()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationQuery

    configuration_query = property(fget=get_configuration_query)

    @abc.abstractmethod
    def clear_configuration_terms(self):
        """Clears the configuration terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    configuration_terms = property(fdel=clear_configuration_terms)

    @abc.abstractmethod
    def get_parameter_query_record(self, parameter_record_type):
        """Gets the parameter query record corresponding to the given ``Parameter`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: the parameter query record
        :rtype: ``osid.configuration.records.ParameterQueryRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterQueryRecord


class ValueQuery:
    """The interface to query a value."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_priority(self, low, high, match):
        """Adds a priority match.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start priority value
        :type low: ``cardinal``
        :param high: end priority value
        :type high: ``cardinal``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_priority(self, match):
        """Matches values with any priority.

        :param match: ``true`` if to match values with any priority, ``false`` to match values with no priority
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_priority_terms(self):
        """Clears the priority terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    priority_terms = property(fdel=clear_priority_terms)

    @abc.abstractmethod
    def match_boolean_value(self, value, match):
        """Adds a boolean match.

        :param value: a boolean value
        :type value: ``boolean``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_boolean_value_terms(self):
        """Clears the boolean value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    boolean_value_terms = property(fdel=clear_boolean_value_terms)

    @abc.abstractmethod
    def match_bytes_value(self, value, match, partial):
        """Adds a byte string match.

        Multiple byte arrays can be added to perform a boolean ``OR``
        among them.

        :param value: a byte value
        :type value: ``byte[]``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :param partial: ``true`` if for a partial match, ``false`` for complete match
        :type partial: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_bytes_value_terms(self):
        """Clears the bytes value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bytes_value_terms = property(fdel=clear_bytes_value_terms)

    @abc.abstractmethod
    def match_cardinal_value(self, low, high, match):
        """Adds a cardinal match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start cardinal value
        :type low: ``cardinal``
        :param high: end cardinal value
        :type high: ``cardinal``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_cardinal_value_terms(self):
        """Clears the cardinal value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cardinal_value_terms = property(fdel=clear_cardinal_value_terms)

    @abc.abstractmethod
    def match_coordinate_value(self, coordinate, match):
        """Adds a coordinate match for coordinates inside the specified coordinate.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param coordinate: a coordinate value
        :type coordinate: ``osid.mapping.Coordinate``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_coordinate_value_terms(self):
        """Clears the coordinate value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    coordinate_value_terms = property(fdel=clear_coordinate_value_terms)

    @abc.abstractmethod
    def match_currency_value(self, low, high, match):
        """Adds a curency match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start currency value
        :type low: ``osid.financials.Currency``
        :param high: a currency value
        :type high: ``osid.financials.Currency``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_currency_value_terms(self):
        """Clears the currency value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    currency_value_terms = property(fdel=clear_currency_value_terms)

    @abc.abstractmethod
    def match_date_time_value(self, low, high, match):
        """Adds a ``DateTime`` range match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start datetime value
        :type low: ``osid.calendaring.DateTime``
        :param high: end datetime value
        :type high: ``osid.calendaring.DateTime``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_date_time_value_terms(self):
        """Clears the date time value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    date_time_value_terms = property(fdel=clear_date_time_value_terms)

    @abc.abstractmethod
    def match_decimal_value(self, low, high, match):
        """Adds a decimal match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start decimal value
        :type low: ``decimal``
        :param high: end decimal value
        :type high: ``decimal``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_decimal_value_terms(self):
        """Clears the decimal value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    decimal_value_terms = property(fdel=clear_decimal_value_terms)

    @abc.abstractmethod
    def match_distance_value(self, low, high, match):
        """Adds a ``Distance`` range match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start distance value
        :type low: ``osid.mapping.Distance``
        :param high: end distance value
        :type high: ``osid.mapping.Distance``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_distance_value_terms(self):
        """Clears the distance value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distance_value_terms = property(fdel=clear_distance_value_terms)

    @abc.abstractmethod
    def match_duration_value(self, low, high, match):
        """Adds a ``Duration`` range match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start duration value
        :type low: ``osid.calendaring.Duration``
        :param high: end duration value
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_duration_value_terms(self):
        """Clears the duration value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    duration_value_terms = property(fdel=clear_duration_value_terms)

    @abc.abstractmethod
    def match_heading_value(self, low, high, match):
        """Adds a ``Heading`` range match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start heading value
        :type low: ``osid.mapping.Heading``
        :param high: end heading value
        :type high: ``osid.mapping.Heading``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_heading_value_terms(self):
        """Clears the heading value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    heading_value_terms = property(fdel=clear_heading_value_terms)

    @abc.abstractmethod
    def match_id_value(self, value, match):
        """Adds an ``Id`` to match.

        Multiple ``Ids`` can be added to perform a boolean ``OR`` among
        them.

        :param value: an ``Id`` value
        :type value: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_id_value_terms(self):
        """Clears the Id value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    id_value_terms = property(fdel=clear_id_value_terms)

    @abc.abstractmethod
    def match_integer_value(self, low, high, match):
        """Adds an integer match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start integer value
        :type low: ``integer``
        :param high: end integer value
        :type high: ``integer``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_integer_value_terms(self):
        """Clears the integer value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    integer_value_terms = property(fdel=clear_integer_value_terms)

    @abc.abstractmethod
    def match_spatial_unit_value(self, value, match):
        """Adds a spatial unit match within the given spatial unit inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param value: a spatial unit
        :type value: ``osid.mapping.SpatialUnit``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_spatial_unit_value_terms(self):
        """Clears the spatial unit value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_unit_value_terms = property(fdel=clear_spatial_unit_value_terms)

    @abc.abstractmethod
    def match_speed_value(self, low, high, match):
        """Adds a speed match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start speed value
        :type low: ``osid.mapping.Speed``
        :param high: end speed value
        :type high: ``osid.mapping.Speed``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_speed_value_terms(self):
        """Clears the speed value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    speed_value_terms = property(fdel=clear_speed_value_terms)

    @abc.abstractmethod
    def match_string_value(self, value, string_match_type, match):
        """Adds a string match.

        Multiple strings can be added to perform a boolean ``OR`` among
        them.

        :param value: string to match
        :type value: ``string``
        :param string_match_type: the string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``value is`` not of ``string_match_type``
        :raise: ``NullArgument`` -- ``value`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_string_value_terms(self):
        """Clears the string value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    string_value_terms = property(fdel=clear_string_value_terms)

    @abc.abstractmethod
    def match_time_value(self, low, high, match):
        """Adds a time match within the given range inclusive.

        Multiple ranges can be added to perform a boolean ``OR`` among
        them.

        :param low: start time value
        :type low: ``osid.calendaring.Time``
        :param high: end time value
        :type high: ``osid.calendaring.Time``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_time_value_terms(self):
        """Clears the time value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_value_terms = property(fdel=clear_time_value_terms)

    @abc.abstractmethod
    def match_type_value(self, value, match):
        """Adds a ``Type`` match.

        Multiple types can be added to perform a boolean ``OR`` among
        them.

        :param value: type to match
        :type value: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_type_value_terms(self):
        """Clears the type value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    type_value_terms = property(fdel=clear_type_value_terms)

    @abc.abstractmethod
    def match_version_value(self, low, high, match):
        """Adds a ``Version`` match within the given range inclusive.

        Multiple queries can be added to perform a boolean ``OR`` among
        them.

        :param low: start version value
        :type low: ``osid.installation.Version``
        :param high: end version value
        :type high: ``osid.installation.Version``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``low`` is greater than ``high``
        :raise: ``NullArgument`` -- ``low`` or ``high`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_version_value_terms(self):
        """Clears the version value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    version_value_terms = property(fdel=clear_version_value_terms)

    @abc.abstractmethod
    def match_object_value_type(self, object_type, match):
        """Adds a ``Type`` to match on the type of object.

        Multiple types can be added to perform a boolean ``OR`` among
        them.

        :param object_type: type to match
        :type object_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``object_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_object_value_type_terms(self):
        """Clears the object value type value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    object_value_type_terms = property(fdel=clear_object_value_type_terms)

    @abc.abstractmethod
    def match_object_value(self, object, object_type, match):
        """Adds an object match.

        Multiple objects can be added to perform a boolean ``OR`` among
        them.

        :param object: object to match
        :type object: ``object``
        :param object_type: type of object
        :type object_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``object`` or ``object_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_object_value_terms(self):
        """Clears the object value terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    object_value_terms = property(fdel=clear_object_value_terms)

    @abc.abstractmethod
    def match_parameter_id(self, parameter_id, match):
        """Adds a parameter ``Id`` for this query.

        :param parameter_id: a parameter ``Id``
        :type parameter_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_parameter_id_terms(self):
        """Clears the parameter ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    parameter_id_terms = property(fdel=clear_parameter_id_terms)

    @abc.abstractmethod
    def supports_parameter_query(self):
        """Tests if a ``ParameterQuery`` is available.

        :return: ``true`` if a parameter query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_query(self):
        """Gets the query for a parameter.

        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_query()`` is ``true``.*

        """
        return  # osid.configuration.ParameterQuery

    parameter_query = property(fget=get_parameter_query)

    @abc.abstractmethod
    def clear_parameter_terms(self):
        """Clears the parameter terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    parameter_terms = property(fdel=clear_parameter_terms)

    @abc.abstractmethod
    def match_configuration_id(self, configuration_id, match):
        """Sets the configuration ``Id`` for this query.

        :param configuration_id: a configuration ``Id``
        :type configuration_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_configuration_id_terms(self):
        """Clears the configuration ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    configuration_id_terms = property(fdel=clear_configuration_id_terms)

    @abc.abstractmethod
    def supports_configuration_query(self):
        """Tests if a ``ConfigurationQuery`` is available.

        :return: ``true`` if a configuration query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_query(self):
        """Gets the query for a configuration.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``Unimplemented`` -- ``supports_configuration_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_query()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationQuery

    configuration_query = property(fget=get_configuration_query)

    @abc.abstractmethod
    def clear_configuration_terms(self):
        """Clears the configuration ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    configuration_terms = property(fdel=clear_configuration_terms)

    @abc.abstractmethod
    def get_value_query_record(self, value_record_type):
        """Gets the value query record corresponding to the given ``Value`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param value_record_type: a value record type
        :type value_record_type: ``osid.type.Type``
        :return: the value query record
        :rtype: ``osid.configuration.records.ValueQueryRecord``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueQueryRecord


class ConfigurationQuery:
    """This is the query for searching configurations.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR,`` except for
    accessing the ``ConfigurationQuery`` subinterface.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_registry(self, match):
        """Matches configurations which are parameter registries.

        :param match: ``true`` for a positive match, ``false`` otherwise
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_registry_terms(self):
        """Clears the registry terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    registry_terms = property(fdel=clear_registry_terms)

    @abc.abstractmethod
    def match_parameter_id(self, parameter_id, match):
        """Adds a parameter ``Id`` for this query.

        :param parameter_id: a parameter ``Id``
        :type parameter_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_parameter_id_terms(self):
        """Clears the parameter ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    parameter_id_terms = property(fdel=clear_parameter_id_terms)

    @abc.abstractmethod
    def supports_parameter_query(self):
        """Tests if a ``ParameterQuery`` is available.

        :return: ``true`` if a parameter query interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_query(self):
        """Gets the query interface for a parameter.

        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_query()`` is ``true``.*

        """
        return  # osid.configuration.ParameterQuery

    parameter_query = property(fget=get_parameter_query)

    @abc.abstractmethod
    def match_any_parameter(self, match):
        """Matches configurations that have any parameter.

        :param match: ``true`` to match configurations with any parameter, ``false`` to match configurations with no
        parameter
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_parameter_terms(self):
        """Clears the parameter terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    parameter_terms = property(fdel=clear_parameter_terms)

    @abc.abstractmethod
    def match_ancestor_configuration_id(self, configuration_id, match):
        """Adds a configuration ``Id`` for this query to match configurations which have as an ancestor the specified
        configuration.

        :param configuration_id: a configuration ``Id``
        :type configuration_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_configuration_id_terms(self):
        """Clears the ancestor configuration ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_configuration_id_terms = property(fdel=clear_ancestor_configuration_id_terms)

    @abc.abstractmethod
    def supports_ancestor_configuration_query(self):
        """Tests if a ``ConfigurationQuery`` is available.

        :return: ``true`` if a configuration query interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_configuration_query(self):
        """Gets the query interface for a configuration.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_configuration_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_configuration_query()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationQuery

    ancestor_configuration_query = property(fget=get_ancestor_configuration_query)

    @abc.abstractmethod
    def match_any_ancestor_configuration(self, match):
        """Matches configurations that have any ancestor.

        :param match: ``true`` to match configurations with any ancestor, ``false`` to match root configurations
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_configuration_terms(self):
        """Clears the ancestor configuration terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_configuration_terms = property(fdel=clear_ancestor_configuration_terms)

    @abc.abstractmethod
    def match_descendant_configuration_id(self, configuration_id, match):
        """Adds a configuration ``Id`` for this query to match configurations which have as a descendant the specified
        configuration.

        :param configuration_id: a configuration ``Id``
        :type configuration_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_configuration_id_terms(self):
        """Clears the descendant configuration ``Id`` terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_configuration_id_terms = property(fdel=clear_descendant_configuration_id_terms)

    @abc.abstractmethod
    def supports_descendant_configuration_query(self):
        """Tests if a ``ConfigurationQuery`` is available.

        :return: ``true`` if a configuration query interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_configuration_query(self):
        """Gets the query interface for a configuration.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_configuration_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_configuration_query()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationQuery

    descendant_configuration_query = property(fget=get_descendant_configuration_query)

    @abc.abstractmethod
    def match_any_descendant_configuration(self, match):
        """Matches configurations that have any descendant.

        :param match: ``true`` to match configurations with any descendant, ``false`` to match leaf configurations
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_configuration_terms(self):
        """Clears the descendant configuration terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_configuration_terms = property(fdel=clear_descendant_configuration_terms)

    @abc.abstractmethod
    def get_configuration_query_record(self, configuration_record_type):
        """Gets the configuration query record corresponding to the given ``Configuration`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration query record
        :rtype: ``osid.configuration.records.ConfigurationQueryRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationQueryRecord
