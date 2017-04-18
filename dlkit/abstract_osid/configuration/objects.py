"""Implementations of configuration abstract base class objects."""
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


class Parameter:
    """A parameter is used to map configuration values to an identifier and syntax.

    The type of the value must be used across all values of the same
    parameter. The values associated with a parameter should be queried
    through the ``ValueLookupSession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_syntax(self):
        """Gets the syntax for the values of this parameter.

        :return: the syntax of the values
        :rtype: ``osid.Syntax``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Syntax

    value_syntax = property(fget=get_value_syntax)

    @abc.abstractmethod
    def get_value_coordinate_type(self):
        """Gets the type of the value if the syntax is a coordinate.

        :return: the type of the values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``get_value_syntax() != coordinate``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    value_coordinate_type = property(fget=get_value_coordinate_type)

    @abc.abstractmethod
    def implements_value_coordinate_type(self, coordinate_type):
        """Tests if the coordinate supports the given coordinate ``Type``.

        :param coordinate_type: a coordinate type
        :type coordinate_type: ``osid.type.Type``
        :return: ``true`` if the coordinate values associated with this parameter implement the given coordinate
        ``Type,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``get_value_syntax() != coordinate``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_heading_type(self):
        """Gets the type of the value if the syntax is a heading.

        :return: the type of the values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``get_value_syntax() != heading``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    value_heading_type = property(fget=get_value_heading_type)

    @abc.abstractmethod
    def implements_value_heading_type(self, heading_type):
        """Tests if the heading supports the given heading ``Type``.

        :param heading_type: a heading type
        :type heading_type: ``osid.type.Type``
        :return: ``true`` if the heading values associated with this parameter implement the given heading ``Type,``
        ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``get_value_syntax() != heading``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_object_type(self):
        """Gets the type of the value if the syntax is an object.

        :return: the type of the values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``get_value_syntax() != object``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    value_object_type = property(fget=get_value_object_type)

    @abc.abstractmethod
    def implements_value_object_type(self, value_type):
        """Tests if the object supports the given ``Type``.

        This method should be checked before retrieving the object
        value.

        :param value_type: a type
        :type value_type: ``osid.type.Type``
        :return: ``true`` if the obect values associated with this parameter implement the given ``Type,``  ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``get_value_syntax() != object``
        :raise: ``NullArgument`` -- ``value_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_spatial_unit_record_type(self):
        """Gets the type of the value if the syntax is a spatial unit.

        :return: the type of the values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``get_value_syntax() != spatialunit``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    value_spatial_unit_record_type = property(fget=get_value_spatial_unit_record_type)

    @abc.abstractmethod
    def implements_value_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if the spatial unit supports the given record ``Type``.

        :param spatial_unit_record_type: a spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the spatial unit values associated with this parameter implement the given record ``Type,``
        ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``get_value_syntax() != spatialunit``
        :raise: ``NullArgument`` -- ``spatial_unit_record_t_ype`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_version_scheme(self):
        """Gets the type of the value if the syntax is a version.

        :return: the type of the values
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``get_value_syntax() != version``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    value_version_scheme = property(fget=get_value_version_scheme)

    @abc.abstractmethod
    def implements_value_version_scheme(self, version_type):
        """Tests if the version supports the given version ``Type``.

        :param version_type: a version type
        :type version_type: ``osid.type.Type``
        :return: ``true`` if the version values associated with this parameter implement the given version ``Type,``
        ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``get_value_syntax() != version``
        :raise: ``NullArgument`` -- ``version_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def are_values_shuffled(self):
        """Tests if if the values assigned to this parameter will be shuffled or values are sorted by index.

        :return: ``true`` if the values are shuffled, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_record(self, parameter_record_type):
        """Gets the parameter record corresponding to the given ``Parameter`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``parameter_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(parameter_record_type)`` is ``true`` .

        :param parameter_record_type: the type of parameter record to retrieve
        :type parameter_record_type: ``osid.type.Type``
        :return: the parameter record
        :rtype: ``osid.configuration.records.ParameterRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterRecord


class ParameterForm:
    """This is the form for creating and updating ``Parameters``.

    Various data elements may be set here for use in the create and
    update methods in the ``ParameterAdminSession``. For each data
    element that may be set, metadata may be examined to provide display
    hints or data constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_syntax_metadata(self):
        """Gets the metadata for the value syntax.

        :return: metadata for the value syntax
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    value_syntax_metadata = property(fget=get_value_syntax_metadata)

    @abc.abstractmethod
    def set_value_syntax(self, syntax):
        """Sets a value syntax.

        :param syntax: the new value type
        :type syntax: ``osid.Syntax``
        :raise: ``InvalidArgument`` -- ``syntax`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``syntax`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_syntax(self):
        """Clears the value syntax.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_syntax = property(fset=set_value_syntax, fdel=clear_value_syntax)

    @abc.abstractmethod
    def get_value_coordinate_type_metadata(self):
        """Gets the metadata for the coordinate type for coordinate values.

        :return: metadata for the coordinate type
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    value_coordinate_type_metadata = property(fget=get_value_coordinate_type_metadata)

    @abc.abstractmethod
    def set_value_coordinate_type(self, coordinate_type):
        """Sets a coordinate type.

        :param coordinate_type: the new coordinate type
        :type coordinate_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``coordinate_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_coordinate_type(self):
        """Clears the coordinate type.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_coordinate_type = property(fset=set_value_coordinate_type, fdel=clear_value_coordinate_type)

    @abc.abstractmethod
    def get_value_heading_type_metadata(self):
        """Gets the metadata for the heading type for coordinate values.

        :return: metadata for the heading type
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    value_heading_type_metadata = property(fget=get_value_heading_type_metadata)

    @abc.abstractmethod
    def set_value_heading_type(self, heading_type):
        """Sets a heading type.

        :param heading_type: the new heading type
        :type heading_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``heading_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_heading_type(self):
        """Clears the heading type.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_heading_type = property(fset=set_value_heading_type, fdel=clear_value_heading_type)

    @abc.abstractmethod
    def get_value_object_type_metadata(self):
        """Gets the metadata for the object value type for object values.

        :return: metadata for the object type
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    value_object_type_metadata = property(fget=get_value_object_type_metadata)

    @abc.abstractmethod
    def set_value_object_type(self, object_type):
        """Sets an object value type.

        :param object_type: the new object type
        :type object_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``object_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``object_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_object_type(self):
        """Clears the object value type.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_object_type = property(fset=set_value_object_type, fdel=clear_value_object_type)

    @abc.abstractmethod
    def get_value_spatial_unit_record_type_metadata(self):
        """Gets the metadata for the spatial unit record type for coordinate values.

        :return: metadata for the spatial unit record type
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    value_spatial_unit_record_type_metadata = property(fget=get_value_spatial_unit_record_type_metadata)

    @abc.abstractmethod
    def set_value_spatial_unit_record_type(self, spatial_unit_record_type):
        """Sets a spatial unit record type.

        :param spatial_unit_record_type: the new spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``spatial_unit_record_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_spatial_unit_record_type(self):
        """Clears the spatial unit record type.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_spatial_unit_record_type = property(fset=set_value_spatial_unit_record_type, fdel=clear_value_spatial_unit_record_type)

    @abc.abstractmethod
    def get_value_version_scheme_metadata(self):
        """Gets the metadata for the version type for object values.

        :return: metadata for the version type
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    value_version_scheme_metadata = property(fget=get_value_version_scheme_metadata)

    @abc.abstractmethod
    def set_value_version_scheme(self, version_type):
        """Sets a version type.

        :param version_type: the new version type
        :type version_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``version_type`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``version_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value_version_scheme(self):
        """Clears the version value type.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value_version_scheme = property(fset=set_value_version_scheme, fdel=clear_value_version_scheme)

    @abc.abstractmethod
    def get_values_shuffled_metadata(self):
        """Gets the metadata for the shuffle type.

        :return: metadata for the shuffle flag
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    values_shuffled_metadata = property(fget=get_values_shuffled_metadata)

    @abc.abstractmethod
    def set_values_shuffled(self, shuffle):
        """Sets the shuffle order.

        :param shuffle: ``true`` to shuffle values by weight, ``false`` to order values by index
        :type shuffle: ``boolean``
        :raise: ``InvalidArgument`` -- ``shuffle`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_values_shuffled(self):
        """Clears the shuffle flag.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly() is true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    values_shuffled = property(fset=set_values_shuffled, fdel=clear_values_shuffled)

    @abc.abstractmethod
    def get_parameter_form_record(self, parameter_record_type):
        """Gets the ``ParameterFormRecord`` corresponding to the given parameter record ``Type``.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: the parameter form record
        :rtype: ``osid.configuration.records.ParameterFormRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ParameterFormRecord


class ParameterList:
    """Like all ``OsidLists,``  ``ParameterList`` provides a means for accessing ``Parameter`` elements sequentially either one
        at a time or many at a time.

    Examples: while (pl.hasNext()) { Parameter parameter =
    pl.getNextParameter(); }

    or
      while (pl.hasNext()) {
           Parameter[] parameters = pl.getNextParameters(pl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_parameter(self):
        """Gets the next ``Parameter`` in this list.

        :return: the next ``Parameter`` in this list. The ``has_next()`` method should be used to test that a next
        ``Parameter`` is available before calling this method.
        :rtype: ``osid.configuration.Parameter``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Parameter

    next_parameter = property(fget=get_next_parameter)

    @abc.abstractmethod
    def get_next_parameters(self, n):
        """Gets the next set of ``Parameters`` in this list which must be less than or equal to the return from
        ``available()``.

        :param n: the number of ``Parameter`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Parameter`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.configuration.Parameter``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Parameter


class Value:
    """This interface specifies the value of a configuration parameter."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_parameter_id(self):
        """Gets the parameter ``Id`` of this value.

        :return: the parameter ``Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    parameter_id = property(fget=get_parameter_id)

    @abc.abstractmethod
    def get_parameter(self):
        """Gets the parameter of this value.

        :return: the parameter
        :rtype: ``osid.configuration.Parameter``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Parameter

    parameter = property(fget=get_parameter)

    @abc.abstractmethod
    def get_priority(self):
        """Gets the priority of this value.

        If the values for this parameter are not shuffled, the priority
        indicates a static ordering of the values from lowest to
        highest. If the values for this parameter are shuffled, the
        priority effects the weight with greater numbers having greater
        weights.

        :return: the index of this value
        :rtype: ``cardinal``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    priority = property(fget=get_priority)

    @abc.abstractmethod
    def get_boolean_value(self):
        """Gets the value if it is a boolean.

        :return: the value
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != BOOLEAN``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    boolean_value = property(fget=get_boolean_value)

    @abc.abstractmethod
    def get_bytes_value(self):
        """Gets the value if it is a byte.

        :return: the value
        :rtype: ``byte``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != BYTE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # byte

    bytes_value = property(fget=get_bytes_value)

    @abc.abstractmethod
    def get_cardinal_value(self):
        """Gets the value if it is a cardinal.

        :return: the value
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != CARDINAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # cardinal

    cardinal_value = property(fget=get_cardinal_value)

    @abc.abstractmethod
    def get_coordinate_value(self):
        """Gets the value if it is a coordinate.

        :return: the value
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != COORDINATE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Coordinate

    coordinate_value = property(fget=get_coordinate_value)

    @abc.abstractmethod
    def get_currency_value(self):
        """Gets the value if it is a currency.

        :return: the value
        :rtype: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != CURRENCY``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.financials.Currency

    currency_value = property(fget=get_currency_value)

    @abc.abstractmethod
    def get_date_time_value(self):
        """Gets the value if it is a ``DateTime``.

        :return: the value
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DATETIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.DateTime

    date_time_value = property(fget=get_date_time_value)

    @abc.abstractmethod
    def get_decimal_value(self):
        """Gets the value if it is a decimal.

        :return: the value
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DECIMAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # decimal

    decimal_value = property(fget=get_decimal_value)

    @abc.abstractmethod
    def get_distance_value(self):
        """Gets the value if it is a ``Distance``.

        :return: the value
        :rtype: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DISTANCE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Distance

    distance_value = property(fget=get_distance_value)

    @abc.abstractmethod
    def get_duration_value(self):
        """Gets the value if it is a ``Duration``.

        :return: the value
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DURATION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Duration

    duration_value = property(fget=get_duration_value)

    @abc.abstractmethod
    def get_heading_value(self):
        """Gets the value if it is a ``Heading``.

        :return: the value
        :rtype: ``osid.mapping.Heading``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != HEADING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Heading

    heading_value = property(fget=get_heading_value)

    @abc.abstractmethod
    def get_id_value(self):
        """Gets the value if it is an ``Id``.

        :return: the value
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != ID``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    id_value = property(fget=get_id_value)

    @abc.abstractmethod
    def get_integer_value(self):
        """Gets the value if it is an integer.

        :return: the value
        :rtype: ``integer``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != INTEGER``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # integer

    integer_value = property(fget=get_integer_value)

    @abc.abstractmethod
    def get_object_value(self):
        """Gets the value if it is an object.

        :return: the value
        :rtype: ``object``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != OBJECT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # object

    object_value = property(fget=get_object_value)

    @abc.abstractmethod
    def get_spatial_unit_value(self):
        """Gets the value if it is a spatial unit.

        :return: the value
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != SPATIALUNIT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.SpatialUnit

    spatial_unit_value = property(fget=get_spatial_unit_value)

    @abc.abstractmethod
    def get_speed_value(self):
        """Gets the value if it is a speed.

        :return: the value
        :rtype: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != SPEED``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.Speed

    speed_value = property(fget=get_speed_value)

    @abc.abstractmethod
    def get_string_value(self):
        """Gets the value if it is a string.

        :return: the value
        :rtype: ``string``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # string

    string_value = property(fget=get_string_value)

    @abc.abstractmethod
    def get_time_value(self):
        """Gets the value if it is a time.

        :return: the value
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.calendaring.Time

    time_value = property(fget=get_time_value)

    @abc.abstractmethod
    def get_type_value(self):
        """Gets the value if it is a ``Type``.

        :return: the value
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != TYPE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.Type

    type_value = property(fget=get_type_value)

    @abc.abstractmethod
    def get_version_value(self):
        """Gets the value if it is a version.

        :return: the value
        :rtype: ``osid.installation.Version``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != VERSION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.installation.Version

    version_value = property(fget=get_version_value)

    @abc.abstractmethod
    def get_value_record(self, value_record_type):
        """Gets the value record corresponding to the given ``Value`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``value_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(value_record_type)``
        is ``true`` .

        :param value_record_type: the type of value record to retrieve
        :type value_record_type: ``osid.type.Type``
        :return: the value record
        :rtype: ``osid.configuration.records.ValueRecord``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueRecord


class ValueForm:
    """This is the form for creating and updating ``Values``.

    Various data elements may be set here for use in the create and
    update methods in the ``ValueAdminSession`` For each data element
    that may be set, metadata may be examined to provide display hints
    or data constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_priority_metadata(self):
        """Gets the metadata for the value priority.

        The metadata returned may depend on the state of the shuffle
        behavior.

        :return: metadata for the priority
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    priority_metadata = property(fget=get_priority_metadata)

    @abc.abstractmethod
    def set_priority(self, priority):
        """Sets the priority.

        :param priority: the new priority
        :type priority: ``cardinal``
        :raise: ``InvalidArgument`` -- ``priority`` is invalid
        :raise: ``NoAccess`` -- ``priority`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_priority(self):
        """Clears the priority.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    priority = property(fset=set_priority, fdel=clear_priority)

    @abc.abstractmethod
    def get_boolean_value_metadata(self):
        """Gets the metadata for a boolean value.

        :return: metadata for a boolean
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != BOOLEAN``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    boolean_value_metadata = property(fget=get_boolean_value_metadata)

    @abc.abstractmethod
    def set_boolean_value(self, value):
        """Sets a boolean value.

        :param value: the new boolean value
        :type value: ``boolean``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != BOOLEAN``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    boolean_value = property(fset=set_boolean_value)

    @abc.abstractmethod
    def get_byte_value_metadata(self):
        """Gets the metadata for a byte value.

        :return: metadata for a byte
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != BYTE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    byte_value_metadata = property(fget=get_byte_value_metadata)

    @abc.abstractmethod
    def set_bytes_value(self, value):
        """Sets a byte value.

        :param value: the new byte value
        :type value: ``byte[]``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != BYTE``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    bytes_value = property(fset=set_bytes_value)

    @abc.abstractmethod
    def get_cardinal_value_metadata(self):
        """Gets the metadata for a cardinal value.

        :return: metadata for a cardinal
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != CARDINAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    cardinal_value_metadata = property(fget=get_cardinal_value_metadata)

    @abc.abstractmethod
    def set_cardinal_value(self, value):
        """Sets a cardinal value.

        :param value: the new cardinal value
        :type value: ``cardinal``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != CARDINAL``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    cardinal_value = property(fset=set_cardinal_value)

    @abc.abstractmethod
    def get_coordinate_value_metadata(self):
        """Gets the metadata for a coordinate value.

        :return: metadata for a coordinate
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != COORDINATE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    coordinate_value_metadata = property(fget=get_coordinate_value_metadata)

    @abc.abstractmethod
    def set_coordinate_value(self, value):
        """Sets a coordinate value.

        :param value: the new coordinate value
        :type value: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != COORDINATE``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    coordinate_value = property(fset=set_coordinate_value)

    @abc.abstractmethod
    def get_currency_value_metadata(self):
        """Gets the metadata for a currency value.

        :return: metadata for a currency
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != CURRENCY``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    currency_value_metadata = property(fget=get_currency_value_metadata)

    @abc.abstractmethod
    def set_currency_value(self, value):
        """Sets a currency value.

        :param value: the new currency value
        :type value: ``osid.financials.Currency``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != CURRENCY``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    currency_value = property(fset=set_currency_value)

    @abc.abstractmethod
    def get_date_time_value_metadata(self):
        """Gets the metadata for a ``DateTime`` value.

        :return: metadata for a datetime
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DATETIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    date_time_value_metadata = property(fget=get_date_time_value_metadata)

    @abc.abstractmethod
    def set_date_time_value(self, value):
        """Sets a ``DateTime`` value.

        :param value: the new datetime value
        :type value: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DATETIME``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    date_time_value = property(fset=set_date_time_value)

    @abc.abstractmethod
    def get_decimal_value_metadata(self):
        """Gets the metadata for a decimal value.

        :return: metadata for a decimal
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DECIMAL``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    decimal_value_metadata = property(fget=get_decimal_value_metadata)

    @abc.abstractmethod
    def set_decimal_value(self, value):
        """Sets a decimal value.

        :param value: the new decimal value
        :type value: ``decimal``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DECIMAL``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    decimal_value = property(fset=set_decimal_value)

    @abc.abstractmethod
    def get_distance_value_metadata(self):
        """Gets the metadata for a ``Distance`` value.

        :return: metadata for a distance
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DISTANCE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    distance_value_metadata = property(fget=get_distance_value_metadata)

    @abc.abstractmethod
    def set_distance_value(self, value):
        """Sets a ``Distance`` value.

        :param value: the new distance value
        :type value: ``osid.mapping.Distance``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DISTANCE``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    distance_value = property(fset=set_distance_value)

    @abc.abstractmethod
    def get_duration_value_metadata(self):
        """Gets the metadata for a ``Duration`` value.

        :return: metadata for a duration
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DURATION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    duration_value_metadata = property(fget=get_duration_value_metadata)

    @abc.abstractmethod
    def set_duration_value(self, value):
        """Sets a ``Duration`` value.

        :param value: the new duration value
        :type value: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != DURATION``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    duration_value = property(fset=set_duration_value)

    @abc.abstractmethod
    def get_id_value_metadata(self):
        """Gets the metadata for an ``Id`` value.

        :return: metadata for an ``Id``
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != ID``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    id_value_metadata = property(fget=get_id_value_metadata)

    @abc.abstractmethod
    def set_id_value(self, value):
        """Sets an ``Id`` value.

        :param value: the new ``Id`` value
        :type value: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != ID``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    id_value = property(fset=set_id_value)

    @abc.abstractmethod
    def get_integer_value_metadata(self):
        """Gets the metadata for an integer value.

        :return: metadata for an integer
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != INTEGER``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    integer_value_metadata = property(fget=get_integer_value_metadata)

    @abc.abstractmethod
    def set_integer_value(self, value):
        """Sets an integer value.

        :param value: the new integer value
        :type value: ``integer``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != INTEGER``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    integer_value = property(fset=set_integer_value)

    @abc.abstractmethod
    def get_spatial_unit_value_metadata(self):
        """Gets the metadata for a spatial unit value.

        :return: metadata for a spatial unit
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != SPATIALUNIT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    spatial_unit_value_metadata = property(fget=get_spatial_unit_value_metadata)

    @abc.abstractmethod
    def set_spatial_unit_value(self, value):
        """Sets a spatial unit value.

        :param value: the new spatial unit value
        :type value: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != SPATIALUNIT``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_unit_value = property(fset=set_spatial_unit_value)

    @abc.abstractmethod
    def get_speed_value_metadata(self):
        """Gets the metadata for a speed value.

        :return: metadata for a speed
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != SPEED``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    speed_value_metadata = property(fget=get_speed_value_metadata)

    @abc.abstractmethod
    def set_speed_value(self, value):
        """Sets a speed value.

        :param value: the new speed value
        :type value: ``osid.mapping.Speed``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != SPEED``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    speed_value = property(fset=set_speed_value)

    @abc.abstractmethod
    def get_string_value_metadata(self):
        """Gets the metadata for a string value.

        :return: metadata for a string
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != STRING``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    string_value_metadata = property(fget=get_string_value_metadata)

    @abc.abstractmethod
    def set_string_value(self, value):
        """Sets a string value.

        :param value: the new string value
        :type value: ``string``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != STRING``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    string_value = property(fset=set_string_value)

    @abc.abstractmethod
    def get_time_value_metadata(self):
        """Gets the metadata for a ``Time`` value.

        :return: metadata for a ``Time``
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != TIME``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    time_value_metadata = property(fget=get_time_value_metadata)

    @abc.abstractmethod
    def set_time_value(self, value):
        """Sets a ``Time`` value.

        :param value: the new ``Time`` value
        :type value: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != TIME``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_value = property(fset=set_time_value)

    @abc.abstractmethod
    def get_type_value_metadata(self):
        """Gets the metadata for a ``Type`` value.

        :return: metadata for a ``Type``
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != TYPE``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    type_value_metadata = property(fget=get_type_value_metadata)

    @abc.abstractmethod
    def set_type_value(self, value):
        """Sets a ``Type`` value.

        :param value: the new ``Type`` value
        :type value: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != TYPE``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    type_value = property(fset=set_type_value)

    @abc.abstractmethod
    def get_version_value_metadata(self):
        """Gets the metadata for a ``Version`` value.

        :return: metadata for a ``Version``
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != VERSION``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    version_value_metadata = property(fget=get_version_value_metadata)

    @abc.abstractmethod
    def set_version_value(self, value):
        """Sets a ``Version`` value.

        :param value: the new ``Version`` value
        :type value: ``osid.installation.Version``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != VERSION``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    version_value = property(fset=set_version_value)

    @abc.abstractmethod
    def get_object_value_metadata(self):
        """Gets the metadata for an object value.

        :return: metadata for an object
        :rtype: ``osid.Metadata``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != OBJECT``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    object_value_metadata = property(fget=get_object_value_metadata)

    @abc.abstractmethod
    def set_object_value(self, value, object_type):
        """Sets an object value.

        :param value: the new object value
        :type value: ``object``
        :param object_type: the object type
        :type object_type: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``Parameter.getSyntax() != OBJECT``
        :raise: ``InvalidArgument`` -- ``value`` is invalid
        :raise: ``NoAccess`` -- ``value`` cannot be modified
        :raise: ``NullArgument`` -- ``value`` or ``object_type`` is ``null``
        :raise: ``Unsupported`` -- ``Metadata.supportsObjectType(objectType)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_value(self):
        """Clears the value.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    value = property(fdel=clear_value)

    @abc.abstractmethod
    def get_value_form_record(self, value_record_type):
        """Gets the ``ValueFormRecord`` corresponding to the given value record ``Type``.

        :param value_record_type: a value record type
        :type value_record_type: ``osid.type.Type``
        :return: the value form record
        :rtype: ``osid.configuration.records.ValueFormRecord``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ValueFormRecord


class ValueList:
    """Like all ``OsidLists,``  ``ValueList`` provides a means for accessing ``Value`` elements sequentially either one at a
        time or many at a time.

    Examples: while (vl.hasNext()) { Value value = vl.getNextValue(); }

    or
      while (vl.hasNext()) {
           Value[] values = vl.getNextValues(vl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_value(self):
        """Gets the next ``Value`` in this list.

        :return: the next ``Value`` in this list. The ``has_next()`` method should be used to test that a next ``Value``
        is available before calling this method.
        :rtype: ``osid.configuration.Value``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Value

    next_value = property(fget=get_next_value)

    @abc.abstractmethod
    def get_next_values(self, n):
        """Gets the next set of ``Values`` in this list which must be less than or equal to the return from
        ``available()``.

        :param n: the number of ``Value`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Value`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.configuration.Value``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Value


class Configuration:
    """``Configuration`` represents a configuration object.

    It contains a name, description and a set of properties that
    describe a configuration data set.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_registry(self):
        """Tests if this configuration is a parameter registry.

        A parameter registry contains parameter definitions with no
        values.

        :return: ``true`` if this is a registry, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_record(self, configuration_record_type):
        """Gets the configuration record corresponding to the given ``Configuration`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``configuration_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(configuration_record_type)`` is ``true`` .

        :param configuration_record_type: the type of configuration record to retrieve
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration record
        :rtype: ``osid.configuration.records.ConfigurationRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationRecord


class ConfigurationForm:
    """This is the form for creating and updating configuration objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ConfigurationAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_registry_metadata(self):
        """Gets the metadata for the registry flag.

        :return: metadata for the registry
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.Metadata

    registry_metadata = property(fget=get_registry_metadata)

    @abc.abstractmethod
    def set_registry(self, registry):
        """Sets the registry flag that indicates if the parameters mapped to this configuration contain no values.

        :param registry: ``true`` if the parameters in this configuration cannot contain values, ``false`` otherwise
        :type registry: ``boolean``
        :raise: ``InvalidArgument`` -- ``registry`` is invalid
        :raise: ``NoAccess`` -- ``registry`` cannot be modified

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    registry = property(fset=set_registry)

    @abc.abstractmethod
    def get_configuration_form_record(self, configuration_record_type):
        """Gets the ``ConfigurationFormRecord`` corresponding to the given configuration record interface ``Type``.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration form record
        :rtype: ``osid.configuration.records.ConfigurationFormRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.records.ConfigurationFormRecord


class ConfigurationList:
    """Like all ``OsidLists,``  ``ConfigurationList`` provides a means for accessing ``Configuration`` elements sequentially
        either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Configuration config =
    cl.getNextConfiguration(); }

    or
      while (cl.hasNext()) {
           Configuration[] configs = cl.getNextConfigurations(cl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_configuration(self):
        """Gets the next ``Configuration`` in this list.

        :return: the next ``Configuration`` in this list. The ``has_next()`` method should be used to test that a next
        ``Configuration`` is available before calling this method.
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    next_configuration = property(fget=get_next_configuration)

    @abc.abstractmethod
    def get_next_configurations(self, n):
        """Gets the next set of ``Configuration`` objects in this lis which must be less than or equal to whst is
        returned from ``available()``.

        :param n: the number of ``Configuration`` elements requested which should be less than or equal to
        ``available()``
        :type n: ``cardinal``
        :return: an array of ``Configuration`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration


class ConfigurationNode:
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``ConfigurationHierarchySession``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` at this node.

        :return: the configuration represented by this node
        :rtype: ``osid.configuration.Configuration``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def get_parent_configuration_nodes(self):
        """Gets the parents of this configuration.

        :return: the parents of the ``id``
        :rtype: ``osid.configuration.ConfigurationNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationNodeList

    parent_configuration_nodes = property(fget=get_parent_configuration_nodes)

    @abc.abstractmethod
    def get_child_configuration_nodes(self):
        """Gets the children of this configuration.

        :return: the children of this configuration
        :rtype: ``osid.configuration.ConfigurationNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationNodeList

    child_configuration_nodes = property(fget=get_child_configuration_nodes)


class ConfigurationNodeList:
    """Like all ``OsidLists,``  ``ConfigurationNodeList`` provides a means for accessing ``ConfigurationNode`` elements
        sequentially either one at a time or many at a time.

    Examples: while (cnl.hasNext()) { ConfigurationNode node =
    cnl.getNextConfigurationNode(); }

    or
      while (cnl.hasNext()) {
           ConfigurationNode[] nodes = cl.getNextConfigurationNodes(cnl.available());
      }


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_next_configuration_node(self):
        """Gets the next ``ConfigurationNode`` in this list.

        :return: the next ``ConfigurationNode`` in this list. The ``has_next()`` method should be used to test that a
        next ``ConfigurationNode`` is available before calling this method.
        :rtype: ``osid.configuration.ConfigurationNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationNode

    next_configuration_node = property(fget=get_next_configuration_node)

    @abc.abstractmethod
    def get_next_configuration_nodes(self, n):
        """Gets the next set of ``ConfigurationNode`` objects in this lis which must be less than or equal to whst is
        returned from ``available()``.

        :param n: the number of ``ConfigurationNode`` elements requested which should be less than or equal to
        ``available()``
        :type n: ``cardinal``
        :return: an array of ``ConfigurationNode`` elements.The length of the array is less than or equal to the number
        specified.
        :rtype: ``osid.configuration.ConfigurationNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationNode
