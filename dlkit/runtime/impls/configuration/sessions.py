from dlkit.abstract_osid.configuration import sessions as abc_configuration_sessions
from ..osid import sessions as osid_sessions
from ..osid.osid_errors import *
from ..primitives import *
from .objects import Parameter, Value
COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
CONDITIONAL = 0
UNCONDITIONAL = 1
DEFAULT = 0
CREATED = True
UPDATED = True


class ValueRetrievalSession(abc_configuration_sessions.ValueRetrievalSession, osid_sessions.OsidSession):
    """This session is used to retrieve active configuration values.

    Two views of the configuration data are defined:

      * federated: parameters defined in configurations that are a
        parent of this configuration in the configuration hierarchy are
        included
      * isolated: parameters are contained to within this configuration
      * conditional: values are filtered that do not pass any defined
        conditions, whether or not they are explciity passed into the
        lookup methods of this session
      * unconditional: values are filtered only for the conditions that
        are explicity passed as parameters. Any conditions defined for
        the value that do not require explicit data for retrieval are
        ignored.

    This session assumes an active view.

    Values are not OSID objects and are obtained using a reference to a
    Parameter.

    """

    def __init__(self, configuration):
        self._catalog = configuration
        self._catalog_id = configuration.get_id()
        self._object_view = COMPARATIVE
        self._catalog_view = ISOLATED
        self._conditional_view = UNCONDITIONAL

    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        return: (osid.id.Id) - the ``Configuration``  ``Id`` associated
                with this session
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin_id
        return self._catalog_id

    configuration_id = property(fget=get_configuration_id)

    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        return: (osid.configuration.Configuration) - the
                ``Configuration`` associated with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        # Implemented from template for osid.resource.ResourceLookupSession.get_bin
        from ..osid.osid_errors import OperationFailed, PermissionDenied
        return self._catalog

    configuration = property(fget=get_configuration)

    def can_lookup_values(self):
        """Tests if this user can perform ``Value`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return True

    def use_comparative_value_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_comparative_resource_view
        self._object_view = COMPARATIVE

    def use_plenary_value_view(self):
        """A complete view of the ``Value`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_plenary_resource_view
        self._object_view = PLENARY

    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include values from parent configurations
        in the configuration hierarchy.

        *compliance: mandatory -- This method is must be implemented.*

        """
        # Implemented from template for
        # osid.resource.ResourceLookupSession.use_federated_bin_view
        self._catalog_view = FEDERATED

    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this configuration only.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._catalog_view = ISOLATED

    def use_conditional_view(self):
        """Returns only values that pass the defined parameter condition.

        Some parameter conditions do not require explicit conditional
        data to be passed and the ``Values`` returned from any method in
        this session are filtered on an implicit condition.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._conditional_view = CONDITIONAL

    def use_unconditional_view(self):
        """Values that are filtered based on an implicit condition are not filtered out from methods in this session.

        Methods that take an explicit condition as a parameter are
        filtered on only those conditions that are specified.

        *compliance: mandatory -- This method is must be implemented.*

        """
        self._conditional_view = UNCONDITIONAL

    def get_value_by_parameter(self, parameter_id=None):
        """Gets a ``Value`` for the given parameter ``Id``.

        If more than one value exists for the given parameter, the most
        preferred value is returned. This method can be used as a
        convenience when only one value is expected.
        ``get_values_by_parameters()`` should be used for getting all
        the active values.

        arg:    parameter_id (osid.id.Id): the ``Id`` of the
                ``Parameter`` to retrieve
        return: (osid.configuration.Value) - the value
        raise:  NotFound - the ``parameter_id`` not found or no value
                available
        raise:  NullArgument - the ``parameter_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass
        if parameter_id is None:
            raise NullArgument
        try:
            parameter_key = parameter_id.get_identifier() + '.' + parameter_id.get_identifier_namespace()
            parameter_map = self._catalog._config_map['parameters'][parameter_key]
        except KeyError:
            try:
                parameter_key = parameter_id.get_identifier()
                parameter_map = self._catalog._config_map['parameters'][parameter_key]
            except KeyError:
                raise NotFound(str(parameter_id))
        if len(parameter_map['values']) == 0:
            raise NotFound()
        lowest_priority_value_map = None
        for value_map in parameter_map['values']:
            if lowest_priority_value_map is None or lowest_priority_value_map['priority'] < value_map['priority']:
                lowest_priority_value_map = value_map
        return Value(lowest_priority_value_map, Parameter(parameter_map))

    def get_values_by_parameter(self, parameter_id=None):
        """Gets all the ``Values`` for the given parameter ``Id``.

        arg:    parameter_id (osid.id.Id): the ``Id`` of the
                ``Parameter`` to retrieve
        return: (osid.configuration.ValueList) - the value list
        raise:  NotFound - the ``parameter_id`` not found
        raise:  NullArgument - the ``parameter_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_values_by_parameters(self, parameter_ids=None):
        """Gets the ``Values`` for the given parameter ``Ids``.

        arg:    parameter_ids (osid.id.IdList): the ``Id`` of the
                ``Parameter`` to retrieve
        return: (osid.configuration.ValueList) - the value list
        raise:  NotFound - a parameter ``Id`` is not found
        raise:  NullArgument - ``parameter_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_value_condition(self, parameter_id=None):
        """Gets a value condition for the given parameter.

        arg:    parameter_id (osid.id.Id): the ``Id`` of a ``Parameter``
        return: (osid.configuration.ValueCondition) - a value condition
        raise:  NullArgument - ``parameter_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_value_by_parameter_on_condition(self, parameter_id=None, value_condition=None):
        """Gets a value in this configuration based on a condition.

        If multiple values are available the most preferred one is
        returned. The condition specified is applied to any or all
        parameters in this configuration as applicable.

        arg:    parameter_id (osid.id.Id): the ``Id`` of a ``Parameter``
        arg:    value_condition (osid.configuration.ValueCondition): the
                condition
        return: (osid.configuration.Value) - the value
        raise:  NotFound - parameter ``Id`` is not found
        raise:  NullArgument - ``parameter_id`` or ``value_condition``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``value_condition`` not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_values_by_parameter_on_condition(self, parameter_id=None, value_condition=None):
        """Gets all the values for a parameter based on a condition.

        In plenary mode, all values are returned or an error results. In
        comparative mode, inaccessible values may be omitted.

        arg:    parameter_id (osid.id.Id): the ``Id`` of a ``Parameter``
        arg:    value_condition (osid.configuration.ValueCondition): the
                condition
        return: (osid.configuration.ValueList) - the value list
        raise:  NotFound - parameter ``Id`` is not found
        raise:  NullArgument - ``parameter_id`` or ``value_condition``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``value_condition`` is not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_values_by_parameters_on_condition(self, parameter_ids=None, value_condition=None):
        """Gets the values for parameters based on a condition.

        The specified condition is applied to any or all of the
        parameters as applicable. In plenary mode, all values are
        returned or an error results. In comparative mode, inaccessible
        values may be omitted.

        arg:    parameter_ids (osid.id.IdList): the ``Id`` of a
                ``Parameter``
        arg:    value_condition (osid.configuration.ValueCondition): the
                condition
        return: (osid.configuration.ValueList) - the value list
        raise:  NotFound - a parameter ``Id`` is not found
        raise:  NullArgument - ``parameter_ids`` or ``value_condition``
                is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``value_condition`` not of this service
        *compliance: mandatory -- This method must be implemented.*

        """
        pass
