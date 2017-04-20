from dlkit.abstract_osid.configuration import objects as abc_configuration_objects
from ..osid import objects as osid_objects
from ..osid.osid_errors import *
from ..primitives import *
from ..osid import markers as osid_markers
import importlib
from ..osid.objects import OsidList


class Parameter(abc_configuration_objects.Parameter, osid_objects.OsidRule):
    """A parameter is used to map configuration values to an identifier and syntax.

    The type of the value must be used across all values of the same
    parameter. The values associated with a parameter should be queried
    through the ``ValueLookupSession``.

    """

    _namespace = 'configuration.Parameter'

    def __init__(self, osid_object_map):
        self._my_map = osid_object_map

    def get_value_syntax(self):
        """Gets the syntax for the values of this parameter.

        return: (osid.Syntax) - the syntax of the values
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._my_map['syntax']

    value_syntax = property(fget=get_value_syntax)

    def get_value_coordinate_type(self):
        """Gets the type of the value if the syntax is a coordinate.

        return: (osid.type.Type) - the type of the values
        raise:  IllegalState - ``get_value_syntax() != coordinate``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    value_coordinate_type = property(fget=get_value_coordinate_type)

    def implements_value_coordinate_type(self, coordinate_type=None):
        """Tests if the coordinate supports the given coordinate ``Type``.

        arg:    coordinate_type (osid.type.Type): a coordinate type
        return: (boolean) - ``true`` if the coordinate values associated
                with this parameter implement the given coordinate
                ``Type,``  ``false`` otherwise
        raise:  IllegalState - ``get_value_syntax() != coordinate``
        raise:  NullArgument - ``coordinate_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_value_heading_type(self):
        """Gets the type of the value if the syntax is a heading.

        return: (osid.type.Type) - the type of the values
        raise:  IllegalState - ``get_value_syntax() != heading``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    value_heading_type = property(fget=get_value_heading_type)

    def implements_value_heading_type(self, heading_type=None):
        """Tests if the heading supports the given heading ``Type``.

        arg:    heading_type (osid.type.Type): a heading type
        return: (boolean) - ``true`` if the heading values associated
                with this parameter implement the given heading
                ``Type,``  ``false`` otherwise
        raise:  IllegalState - ``get_value_syntax() != heading``
        raise:  NullArgument - ``heading_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_value_object_type(self):
        """Gets the type of the value if the syntax is an object.

        return: (osid.type.Type) - the type of the values
        raise:  IllegalState - ``get_value_syntax() != object``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    value_object_type = property(fget=get_value_object_type)

    def implements_value_object_type(self, value_type=None):
        """Tests if the object supports the given ``Type``.

        This method should be checked before retrieving the object
        value.

        arg:    value_type (osid.type.Type): a type
        return: (boolean) - ``true`` if the obect values associated with
                this parameter implement the given ``Type,``  ``false``
                otherwise
        raise:  IllegalState - ``get_value_syntax() != object``
        raise:  NullArgument - ``value_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_value_spatial_unit_record_type(self):
        """Gets the type of the value if the syntax is a spatial unit.

        return: (osid.type.Type) - the type of the values
        raise:  IllegalState - ``get_value_syntax() != spatialunit``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    value_spatial_unit_record_type = property(fget=get_value_spatial_unit_record_type)

    def implements_value_spatial_unit_record_type(self, spatial_unit_record_type=None):
        """Tests if the spatial unit supports the given record ``Type``.

        arg:    spatial_unit_record_type (osid.type.Type): a spatial
                unit record type
        return: (boolean) - ``true`` if the spatial unit values
                associated with this parameter implement the given
                record ``Type,``  ``false`` otherwise
        raise:  IllegalState - ``get_value_syntax() != spatialunit``
        raise:  NullArgument - ``spatial_unit_record_t_ype`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def get_value_version_scheme(self):
        """Gets the type of the value if the syntax is a version.

        return: (osid.type.Type) - the type of the values
        raise:  IllegalState - ``get_value_syntax() != version``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    value_version_scheme = property(fget=get_value_version_scheme)

    def implements_value_version_scheme(self, version_type=None):
        """Tests if the version supports the given version ``Type``.

        arg:    version_type (osid.type.Type): a version type
        return: (boolean) - ``true`` if the version values associated
                with this parameter implement the given version
                ``Type,``  ``false`` otherwise
        raise:  IllegalState - ``get_value_syntax() != version``
        raise:  NullArgument - ``version_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        raise Unimplemented()

    def are_values_shuffled(self):
        """Tests if if the values assigned to this parameter will be shuffled or values are sorted by index.

        return: (boolean) - ``true`` if the values are shuffled,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return False

    def get_parameter_record(self, parameter_record_type=None):
        """Gets the parameter record corresponding to the given ``Parameter`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``parameter_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(parameter_record_type)`` is ``true`` .

        arg:    parameter_record_type (osid.type.Type): the type of
                parameter record to retrieve
        return: (osid.configuration.records.ParameterRecord) - the
                parameter record
        raise:  NullArgument - ``parameter_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(parameter_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """


class ParameterList(abc_configuration_objects.ParameterList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ParameterList`` provides a means for accessing ``Parameter`` elements sequentially either one at a time or many at a time.

    Examples: while (pl.hasNext()) { Parameter parameter =
    pl.getNextParameter(); }

    or
      while (pl.hasNext()) {
           Parameter[] parameters = pl.getNextParameters(pl.available());
      }
    """

    def get_next_parameter(self):
        """Gets the next ``Parameter`` in this list.

        return: (osid.configuration.Parameter) - the next ``Parameter``
                in this list. The ``has_next()`` method should be used
                to test that a next ``Parameter`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        try:
            next_item = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except:  # Need to specify exceptions here
            raise OperationFailed()
        else:
            return next_item

    def next(self):
        from .objects import Parameter
        try:
            next_item = OsidList.next(self)
        except:
            raise
        if isinstance(next_item, dict):
            next_item = Parameter(next_item)
        return next_item

    next_parameter = property(fget=get_next_parameter)

    def get_next_parameters(self, n=None):
        """Gets the next set of ``Parameters`` in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Parameter`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.configuration.Parameter) - an array of
                ``Parameter`` elements.The length of the array is less
                than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(self.next())
                except:  # Need to specify exceptions here
                    raise OperationFailed()
                x = x + 1
            return next_list


class Value(abc_configuration_objects.Value, osid_objects.OsidObject, osid_markers.Operable, osid_markers.Subjugateable):
    """This interface specifies the value of a configuration parameter."""

    _namespace = 'configuration.Value'

    def __init__(self, osid_object_map, parameter):
        self._my_map = osid_object_map
        self._my_parameter = parameter

    def get_id(self):
        from .. import primitives
        return primitives.Id(identifier=self._identifier,
                             namespace=self._namespace,
                             authority=self._authority)

    def get_parameter_id(self):
        """Gets the parameter ``Id`` of this value.

        return: (osid.id.Id) - the parameter ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.learning.Activity.get_objective_id
        return self._my_parameter.get_id()

    parameter_id = property(fget=get_parameter_id)

    def get_parameter(self):
        """Gets the parameter of this value.

        return: (osid.configuration.Parameter) - the parameter
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._my_parameter

    parameter = property(fget=get_parameter)

    def get_priority(self):
        """Gets the priority of this value.

        If the values for this parameter are not shuffled, the priority
        indicates a static ordering of the values from lowest to
        highest. If the values for this parameter are shuffled, the
        priority effects the weight with greater numbers having greater
        weights.

        return: (cardinal) - the index of this value
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    priority = property(fget=get_priority)

    def _get_value(self, syntax):
        if self._my_parameter.get_value_syntax() != syntax:
            raise IllegalState()
        return self._my_map['value']

    def get_boolean_value(self):
        """Gets the value if it is a boolean.

        return: (boolean) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != BOOLEAN``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('BOOLEAN')

    boolean_value = property(fget=get_boolean_value)

    def get_bytes_value(self):
        """Gets the value if it is a byte.

        return: (byte) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != BYTE``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('BYTE')

    bytes_value = property(fget=get_bytes_value)

    def get_cardinal_value(self):
        """Gets the value if it is a cardinal.

        return: (cardinal) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != CARDINAL``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('CARDINAL')

    cardinal_value = property(fget=get_cardinal_value)

    def get_coordinate_value(self):
        """Gets the value if it is a coordinate.

        return: (osid.mapping.Coordinate) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != COORDINATE``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('COORDINATE')

    coordinate_value = property(fget=get_coordinate_value)

    def get_currency_value(self):
        """Gets the value if it is a currency.

        return: (osid.financials.Currency) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != CURRENCY``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('CURRENCY')

    currency_value = property(fget=get_currency_value)

    def get_date_time_value(self):
        """Gets the value if it is a ``DateTime``.

        return: (osid.calendaring.DateTime) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != DATETIME``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('DATETIME')

    date_time_value = property(fget=get_date_time_value)

    def get_decimal_value(self):
        """Gets the value if it is a decimal.

        return: (decimal) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != DECIMAL``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('DECIMAL')

    decimal_value = property(fget=get_decimal_value)

    def get_distance_value(self):
        """Gets the value if it is a ``Distance``.

        return: (osid.mapping.Distance) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != DISTANCE``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('DISTANCE')

    distance_value = property(fget=get_distance_value)

    def get_duration_value(self):
        """Gets the value if it is a ``Duration``.

        return: (osid.calendaring.Duration) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != DURATION``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('DURATION')

    duration_value = property(fget=get_duration_value)

    def get_heading_value(self):
        """Gets the value if it is a ``Heading``.

        return: (osid.mapping.Heading) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != HEADING``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('HEADING')

    heading_value = property(fget=get_heading_value)

    def get_id_value(self):
        """Gets the value if it is an ``Id``.

        return: (osid.id.Id) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != ID``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('ID')

    id_value = property(fget=get_id_value)

    def get_integer_value(self):
        """Gets the value if it is an integer.

        return: (integer) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != INTEGER``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('INTEGER')

    integer_value = property(fget=get_integer_value)

    def get_object_value(self):
        """Gets the value if it is an object.

        return: (object) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != OBJECT``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('OBJECT')

    object_value = property(fget=get_object_value)

    def get_spatial_unit_value(self):
        """Gets the value if it is a spatial unit.

        return: (osid.mapping.SpatialUnit) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != SPATIALUNIT``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('SPATIALUNIT')

    spatial_unit_value = property(fget=get_spatial_unit_value)

    def get_speed_value(self):
        """Gets the value if it is a speed.

        return: (osid.mapping.Speed) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != SPEED``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('SPEED')

    speed_value = property(fget=get_speed_value)

    def get_string_value(self):
        """Gets the value if it is a string.

        return: (string) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != STRING``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('STRING')

    string_value = property(fget=get_string_value)

    def get_time_value(self):
        """Gets the value if it is a time.

        return: (osid.calendaring.Time) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != TIME``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('TIME')

    time_value = property(fget=get_time_value)

    def get_type_value(self):
        """Gets the value if it is a ``Type``.

        return: (osid.type.Type) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != TYPE``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('TYPE')

    type_value = property(fget=get_type_value)

    def get_version_value(self):
        """Gets the value if it is a version.

        return: (osid.installation.Version) - the value
        raise:  IllegalState - ``Parameter.getSyntax() != VERSION``
        *compliance: mandatory -- This method must be implemented.*

        """
        return self._get_value('VERSION')

    version_value = property(fget=get_version_value)

    def get_value_record(self, value_record_type=None):
        """Gets the value record corresponding to the given ``Value`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``value_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(value_record_type)``
        is ``true`` .

        arg:    value_record_type (osid.type.Type): the type of value
                record to retrieve
        return: (osid.configuration.records.ValueRecord) - the value
                record
        raise:  NullArgument - ``value_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(value_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """


class ValueList(abc_configuration_objects.ValueList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ValueList`` provides a means for accessing ``Value`` elements sequentially either one at a time or many at a time.

    Examples: while (vl.hasNext()) { Value value = vl.getNextValue(); }

    or
      while (vl.hasNext()) {
           Value[] values = vl.getNextValues(vl.available());
      }



    """

    def get_next_value(self):
        """Gets the next ``Value`` in this list.

        return: (osid.configuration.Value) - the next ``Value`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Value`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        try:
            next_item = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except:  # Need to specify exceptions here
            raise OperationFailed()
        else:
            return next_item

    def next(self):
        from .objects import Value
        try:
            next_item = OsidList.next(self)
        except:
            raise
        if isinstance(next_item, dict):
            next_item = Value(next_item)
        return next_item

    next_value = property(fget=get_next_value)

    def get_next_values(self, n=None):
        """Gets the next set of ``Values`` in this list which must be less than or equal to the return from ``available()``.

        arg:    n (cardinal): the number of ``Value`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.configuration.Value) - an array of ``Value``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
    # Implemented from template for osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(self.next())
                except:  # Need to specify exceptions here
                    raise OperationFailed()
                x = x + 1
            return next_list


class Configuration(abc_configuration_objects.Configuration, osid_objects.OsidCatalog):
    """``Configuration`` represents a configuration object.

    It contains a name, description and a set of properties that
    describe a configuration data set.

    """

    _namespace = 'configuration.Configuration'

    def __init__(self, config_map):
        self._config_map = config_map
        self._identifier = config_map['id']

    def is_registry(self):
        """Tests if this configuration is a parameter registry.

        A parameter registry contains parameter definitions with no
        values.

        return: (boolean) - ``true`` if this is a registry, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        False

    def get_configuration_record(self, configuration_record_type=None):
        """Gets the configuration record corresponding to the given ``Configuration`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``configuration_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(configuration_record_type)`` is ``true`` .

        arg:    configuration_record_type (osid.type.Type): the type of
                configuration record to retrieve
        return: (osid.configuration.records.ConfigurationRecord) - the
                configuration record
        raise:  NullArgument - ``configuration_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(configuration_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def set_registry(self, registry=None):
        """Sets the registry flag that indicates if the parameters mapped to this configuration contain no values.

        arg:    registry (boolean): ``true`` if the parameters in this
                configuration cannot contain values, ``false`` otherwise
        raise:  InvalidArgument - ``registry`` is invalid
        raise:  NoAccess - ``registry`` cannot be modified
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    registry = property(fset=set_registry)

    def get_configuration_form_record(self, configuration_record_type=None):
        """Gets the ``ConfigurationFormRecord`` corresponding to the given configuration record interface ``Type``.

        arg:    configuration_record_type (osid.type.Type): a
                configuration record type
        return: (osid.configuration.records.ConfigurationFormRecord) -
                the configuration form record
        raise:  NullArgument - ``configuration_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(configuration_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ConfigurationList(abc_configuration_objects.ConfigurationList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ConfigurationList`` provides a means for accessing ``Configuration`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Configuration config =
    cl.getNextConfiguration(); }

    or
      while (cl.hasNext()) {
           Configuration[] configs = cl.getNextConfigurations(cl.available());
      }



    """

    def get_next_configuration(self):
        """Gets the next ``Configuration`` in this list.

        return: (osid.configuration.Configuration) - the next
                ``Configuration`` in this list. The ``has_next()``
                method should be used to test that a next
                ``Configuration`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        try:
            next_item = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except:  # Need to specify exceptions here
            raise OperationFailed()
        else:
            return next_item

    def next(self):
        from .objects import Configuration
        try:
            next_item = OsidList.next(self)
        except:
            raise
        if isinstance(next_item, dict):
            next_item = Configuration(next_item)
        return next_item

    next_configuration = property(fget=get_next_configuration)

    def get_next_configurations(self, n=None):
        """Gets the next set of ``Configuration`` objects in this lis which must be less than or equal to whst is returned from ``available()``.

        arg:    n (cardinal): the number of ``Configuration`` elements
                requested which should be less than or equal to
                ``available()``
        return: (osid.configuration.Configuration) - an array of
                ``Configuration`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
    # Implemented from template for osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            x = 0
            while x < n:
                try:
                    next_list.append(self.next())
                except:  # Need to specify exceptions here
                    raise OperationFailed()
                x = x + 1
            return next_list
