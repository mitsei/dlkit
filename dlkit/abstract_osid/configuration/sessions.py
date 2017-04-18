"""Implementations of configuration abstract base class sessions."""
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


class ValueRetrievalSession:
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
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_lookup_values(self):
        """Tests if this user can perform ``Value`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_value_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_value_view(self):
        """A complete view of the ``Value`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include values from parent configurations
        in the configuration hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this configuration only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_conditional_view(self):
        """Returns only values that pass the defined parameter condition.

        Some parameter conditions do not require explicit conditional
        data to be passed and the ``Values`` returned from any method in
        this session are filtered on an implicit condition.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_unconditional_view(self):
        """Values that are filtered based on an implicit condition are not filtered out from methods in this session.

        Methods that take an explicit condition as a parameter are
        filtered on only those conditions that are specified.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_value_by_parameter(self, parameter_id):
        """Gets a ``Value`` for the given parameter ``Id``.

        If more than one value exists for the given parameter, the most
        preferred value is returned. This method can be used as a
        convenience when only one value is expected.
        ``get_values_by_parameters()`` should be used for getting all
        the active values.

        :param parameter_id: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_id: ``osid.id.Id``
        :return: the value
        :rtype: ``osid.configuration.Value``
        :raise: ``NotFound`` -- the ``parameter_id`` not found or no value available
        :raise: ``NullArgument`` -- the ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Value

    @abc.abstractmethod
    def get_values_by_parameter(self, parameter_id):
        """Gets all the ``Values`` for the given parameter ``Id``.

        :param parameter_id: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_id: ``osid.id.Id``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- the ``parameter_id`` not found
        :raise: ``NullArgument`` -- the ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_values_by_parameters(self, parameter_ids):
        """Gets the ``Values`` for the given parameter ``Ids``.

        :param parameter_ids: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_ids: ``osid.id.IdList``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- a parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_value_condition(self, parameter_id):
        """Gets a value condition for the given parameter.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: a value condition
        :rtype: ``osid.configuration.ValueCondition``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueCondition

    @abc.abstractmethod
    def get_value_by_parameter_on_condition(self, parameter_id, value_condition):
        """Gets a value in this configuration based on a condition.

        If multiple values are available the most preferred one is
        returned. The condition specified is applied to any or all
        parameters in this configuration as applicable.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param value_condition: the condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value
        :rtype: ``osid.configuration.Value``
        :raise: ``NotFound`` -- parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Value

    @abc.abstractmethod
    def get_values_by_parameter_on_condition(self, parameter_id, value_condition):
        """Gets all the values for a parameter based on a condition.

        In plenary mode, all values are returned or an error results. In
        comparative mode, inaccessible values may be omitted.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param value_condition: the condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_values_by_parameters_on_condition(self, parameter_ids, value_condition):
        """Gets the values for parameters based on a condition.

        The specified condition is applied to any or all of the
        parameters as applicable. In plenary mode, all values are
        returned or an error results. In comparative mode, inaccessible
        values may be omitted.

        :param parameter_ids: the ``Id`` of a ``Parameter``
        :type parameter_ids: ``osid.id.IdList``
        :param value_condition: the condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- a parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_ids`` or ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList


class ValueLookupSession:
    """This session is used to retrieve configuration values.

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
      * active value view: All value lookup methods return active
        values.
      * any status value view: Values of any active or inactive status
        are returned from methods.


    Values are not OSID objects and are obtained using a reference to a
    Parameter.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def use_active_value_view(self):
        """Only active values are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_status_value_view(self):
        """All active and inactive values are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_value(self, value_id):
        """Gets the ``Value`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Value`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Value`` and retained for compatibility.

        :param value_id: the ``Id`` of the ``Value`` to retrieve
        :type value_id: ``osid.id.Id``
        :return: the returned ``Value``
        :rtype: ``osid.configuration.Value``
        :raise: ``NotFound`` -- no ``Value`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Value

    @abc.abstractmethod
    def get_values_by_ids(self, value_ids):
        """Gets a ``ValueList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the values
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Values`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param value_ids: the list of ``Ids`` to retrieve
        :type value_ids: ``osid.id.IdList``
        :return: the returned ``Value`` list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``value_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_values_by_genus_type(self, value_genus_type):
        """Gets a ``ValueList`` corresponding to the given value genus ``Type`` which does not include values of genus
        types derived from the specified ``Type``.

        :param value_genus_type: a value genus type
        :type value_genus_type: ``osid.type.Type``
        :return: the returned ``Value list``
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_values_by_parent_genus_type(self, value_genus_type):
        """Gets a ``ValueList`` corresponding to the given value genus ``Type`` and include any additional values with
        genus types derived from the specified ``Type``.

        :param value_genus_type: a value genus type
        :type value_genus_type: ``osid.type.Type``
        :return: the returned ``Value list``
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_values_by_record_type(self, value_record_type):
        """Gets a ``ValueList`` corresponding to the given value record ``Type`` which does not include values of record
        types derived from the specified ``Type``.

        :param value_record_type: a value type
        :type value_record_type: ``osid.type.Type``
        :return: the returned ``Value`` list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    @abc.abstractmethod
    def get_values(self):
        """Gets all the values in this configuration.

        In plenary mode, all values are returned or an error results. In
        comparative mode, inaccessible values may be omitted.

        In plenary mode, the returned list contains all known values or
        an error results. Otherwise, the returned list may contain only
        those values that are accessible through this session.

        In active mode, values are returned that are currently active.
        In any status mode, active and inactive values are returned.

        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList

    values = property(fget=get_values)

    @abc.abstractmethod
    def get_values_on_condition(self, value_condition):
        """Gets the values in this configuration based on a condition.

        The condition specified is applied to any or all parameters in
        this configuration as applicable. In plenary mode, all values
        are returned or an error results. In comparative mode,
        inaccessible values may be omitted.

        :param value_condition: a value condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList


class ValueQuerySession:
    """This session provides methods for searching ``Value`` objects.

    The search query is constructed using the ``ValueQuery``. The
    parameter ``Type`` also specifies the record for the value query.

    Two views of the configuration data are defined;

      * federated: values defined in configurations that are a parent of
        this configuration in the configuration hierarchy are included
      * isolated: values are contained to within this configuration

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_search_values(self):
        """Tests if this user can perform ``Value`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include values from parent configurations
        in the configuration hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this configuration only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_value_query(self):
        """Gets a value query.

        :return: the value query
        :rtype: ``osid.configuration.ValueQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueQuery

    value_query = property(fget=get_value_query)

    @abc.abstractmethod
    def get_values_by_query(self, value_query):
        """Gets a list of ``Values`` matching the given value query.

        :param value_query: the value query
        :type value_query: ``osid.configuration.ValueQuery``
        :return: the returned ``ValueList``
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a query form is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueList


class ValueSearchSession:
    """This session provides methods for searching ``Value`` objects.

    The search query is constructed using the ``ValueQuery``. The
    parameter ``Type`` also specifies the record for the value query.

    ``get_values_by_query()`` is the basic search method and returns a
    list of ``Values``. A more advanced search may be performed with
    ``getValuesBySearch()``. It accepts a ``ValueSearch`` in addition to
    the query for the purpose of specifying additional options affecting
    the entire search, such as ordering. ``get_values_by_search()``
    returns a ``ValueSearchResults`` that can be used to access the
    resulting ``ValueList`` or be used to perform a search within the
    result set through ``ValueSearch``.

    Two views of the configuration data are defined;

      * federated: values defined in configurations that are a parent of
        this configuration in the configuration hierarchy are included
      * isolated: values are contained to within this configuration

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_search(self):
        """Gets a value search.

        :return: the value search
        :rtype: ``osid.configuration.ValueSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueSearch

    value_search = property(fget=get_value_search)

    @abc.abstractmethod
    def get_value_search_order(self):
        """Gets a value search order.

        The ``ValueSearchOrder`` is supplied to a ``ValueSearch`` to
        specify the ordering of results.

        :return: the value search order
        :rtype: ``osid.configuration.ValueSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueSearchOrder

    value_search_order = property(fget=get_value_search_order)

    @abc.abstractmethod
    def get_values_by_search(self, value_query, value_search):
        """Gets a list of ``Values`` matching the given search query using the given search.

        :param value_query: the value query
        :type value_query: ``osid.configuration.ValueQuery``
        :param value_search: the value search
        :type value_search: ``osid.configuration.ValueSearch``
        :return: the serach results
        :rtype: ``osid.configuration.ValueSearchResults``
        :raise: ``NullArgument`` -- ``value_query`` or ``value_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_query`` or ``value_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueSearchResults

    @abc.abstractmethod
    def get_value_query_from_inspector(self, value_query_inspector):
        """Gets a value query from an inspector.

        The inspector is available from a ``ValueSearchResults``.

        :param value_query_inspector: a value query inspector
        :type value_query_inspector: ``osid.configuration.ValueQueryInspector``
        :return: the value query
        :rtype: ``osid.configuration.ValueQuery``
        :raise: ``NullArgument`` -- ``value_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``value_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueQuery


class ValueAdminSession:
    """This session creates, updates, and deletes ``Values`` The data for create and update is provided by the consumer via the
        form object.

    ``OsidForms`` are requested for each create or update and may not be
    reused.

    Create and update operations differ in their usage. To create a
    ``Value,`` a ``ValueForm`` is requested using
    ``get_value_form_for_create()`` specifying the desired parameter and
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``ValueForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``ValueForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ValueForm`` corresponds
    to an attempted transaction.

    For updates, ``ValueForms`` are requested to the ``Value``  ``Id``
    that is to be updated using ``getValueFormForUpdate()``. Similarly,
    the ``ValueForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``ValueForm`` can only be used once for a successful update and
    cannot be reused.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def support_value_conditions(self):
        """Tests if applying conditions to values is supported.

        :return: ``true`` if ``Value`` conditions are supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_values(self):
        """Tests if this user can create ``Values``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Value``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_value_with_record_types(self, value_record_types):
        """Tests if this user can create a single ``Value`` using the desired record types.

        While ``ConfigurationManager.getValueRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Value``.
        Providing an empty array tests if a ``Value`` can be created
        with no records.

        :param value_record_types: array of value record types
        :type value_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Value`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_form_for_create(self, parameter_id, value_record_types):
        """Gets the form for creating new values.

        A new form should be requested for each create transaction.

        :param parameter_id: the parameter
        :type parameter_id: ``osid.id.Id``
        :param value_record_types: array of value record types
        :type value_record_types: ``osid.type.Type[]``
        :return: the value form
        :rtype: ``osid.configuration.ValueForm``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueForm

    @abc.abstractmethod
    def create_value(self, value_form):
        """Creates a value.

        :param value_form: the form
        :type value_form: ``osid.configuration.ValueForm``
        :return: the value
        :rtype: ``osid.configuration.Value``
        :raise: ``IllegalState`` -- ``value_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``value_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_form`` did not originate from ``get_value_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Value

    @abc.abstractmethod
    def can_update_values(self):
        """Tests if this user can update ``Values``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Value``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_form_for_update(self, value_id):
        """Gets the value form for updating an existing value.

        A new value form should be requested for each update
        transaction.

        :param value_id: the ``Id`` of the ``Value``
        :type value_id: ``osid.id.Id``
        :return: the value form
        :rtype: ``osid.configuration.ValueForm``
        :raise: ``NotFound`` -- the value is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ValueForm

    @abc.abstractmethod
    def update_value(self, value_form):
        """Updates an existing value.

        :param value_form: the form containing the elemnts to be updated
        :type value_form: ``osid.configuration.ValueForm``
        :raise: ``IllegalState`` -- ``value_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``parameter_id, value_id`` or ``value_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_form`` did not originate from ``get_value_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_values(self):
        """Tests if this user can delete ``Values``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Value``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_value(self, value_id):
        """Deletes the specified value.

        :param value_id: the ``Id`` of the ``Value`` to delete
        :type value_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``value_id`` is not found
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_value_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Values``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_value(self, value_id, alias_id):
        """Adds an ``Id`` to a ``Value`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Value`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another value it is
        reassigned to the given value ``Id``.

        :param value_id: the ``Id`` of a ``Value``
        :type value_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``value_id`` not found
        :raise: ``NullArgument`` -- ``value_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ValueNotificationSession:
    """This session defines methods to receive notifications on changes to ``Values``.

    A particular value in a set may have been added or deleted, but all
    changes appear as a change to a parameter. Once a change
    notification is received, the new value list can be obtained through
    the ``ValueLookupSession``. This session is intended for adapters
    and providers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.

    Two views are defined;

      * federated: parameters defined in configurations that are a
        parent of this configuration in the configuration hierarchy are
        included for notifications
      * isolated: notifications are restricted to parameters are defined
        to within this configuration


    The methods ``federate_valuer_view()`` and ``isolate_value_view()``
    behave as a radio group and one should be selected before invoking
    any lookup methods.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_register_for_value_notifications(self):
        """Tests if this user can register for ``Value`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include parameters in configurations of
        which this configuration is a child in the configuration
        hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for parameter values to
        this configuration only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_value_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_value_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_value_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_value_notification(self, notification_id):
        """Acknowledge a value notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_values(self):
        """Assigns a callback for notifications of new values.

        ``ValueReceiver.newValues()`` is invoked when a new ``Value`` is
        added to this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_values_for_parameter(self, parameter_id):
        """Assigns a callback for notifications of new values for the given parameter.

        ``ValueReceiver.newValues()`` is invoked when a new ``Value`` is
        added to this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_values(self):
        """Assigns a callback for notification of updated parameter values in this configuration.

        ``ValueReceiver.changedValues()`` is invoked when a ``Value`` is
        changed in this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_values_for_parameter(self, parameter_id):
        """Assigns a callback for notifications of changed values for the given parameter.

        ``ValueReceiver.changedValues()`` is invoked when a ``Value`` is
        updated to this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_value(self, value_id):
        """Assigns a callback for notifications of an update to a value in this configuration.

        ``ValueReceiver.changedValues()`` is invoked when the specified
        ``Value`` is updated in this configuration.

        :param value_id: the ``Id`` of the ``Value`` to monitor
        :type value_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_values(self):
        """Assigns a callback for notification of deleted values in this configuration.

        ``ValueReceiver.changedValues()`` is invoked when a ``Value`` is
        removed from this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_values_for_parameter(self, parameter_id):
        """Assigns a callback for notifications of changed values for the given parameter.

        ``ValueReceiver.changedValues()`` is invoked when a ``Value`` is
        removed from this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_value(self, value_id):
        """Assigns a callback for notifications of an update to a value in this configuration.

        ``ValueReceiver.changedValues()`` is invoked when the specified
        ``Value`` is removed from this configuration.

        :param value_id: the ``Id`` of the ``Value`` to monitor
        :type value_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ParameterLookupSession:
    """This session is used to retrieve parameters from a configuration registry of parameters."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_lookup_parameters(self):
        """Tests if this user can perform ``Parameter`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_parameter_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_parameter_view(self):
        """A complete view of the ``Parameter`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include paramaters from parent
        configurations in the configuration hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this configuration only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_active_parameter_view(self):
        """Only active parameters are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_any_status_parameter_view(self):
        """All active and inactive parameters are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_parameter(self, parameter_id):
        """Gets the ``Parameter`` specified by its ``Id``.

        :param parameter_id: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_id: ``osid.id.Id``
        :return: the returned ``Parameter``
        :rtype: ``osid.configuration.Parameter``
        :raise: ``NotFound`` -- no ``Parameter`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Parameter

    @abc.abstractmethod
    def get_parameters_by_ids(self, parameter_ids):
        """Gets a ``ParameterList`` corresponding to the given ``IdList``.

        :param parameter_ids: the list of ``Ids`` to retrieve
        :type parameter_ids: ``osid.id.IdList``
        :return: the returned ``Parameter`` list
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``parameter_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    @abc.abstractmethod
    def get_parameters_by_genus_type(self, parameter_genus_type):
        """Gets a ``ParameterList`` corresponding to the given parameter genus ``Type`` which does not include
        parameters of genus types derived from the specified ``Type``.

        :param parameter_genus_type: a parameter genus type
        :type parameter_genus_type: ``osid.type.Type``
        :return: the returned ``Parameter list``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    @abc.abstractmethod
    def get_parameters_by_parent_genus_type(self, parameter_genus_type):
        """Gets a ``ParameterList`` corresponding to the given parameters genus ``Type`` and include any additional
        parameters with genus types derived from the specified ``Type``.

        :param parameter_genus_type: a parameter genus type
        :type parameter_genus_type: ``osid.type.Type``
        :return: the returned ``Parameter list``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    @abc.abstractmethod
    def get_parameters_by_record_type(self, parameter_record_type):
        """Gets a ``ParameterList`` corresponding to the given parameter record ``Type`` which does not include
        parameters of record types derived from the specified ``Type``.

        :param parameter_record_type: a parameter type
        :type parameter_record_type: ``osid.type.Type``
        :return: the returned ``Parameter`` list
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    @abc.abstractmethod
    def get_parameters(self):
        """Gets all ``Parameters``.

        :return: a list of ``Parameters``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    parameters = property(fget=get_parameters)


class ParameterQuerySession:
    """This session provides methods for searching ``Parameter`` objects.

    The search query is constructed using the ``ParameterQuery``.

    Two views of the configuration data are defined;

      * federated: parameters defined in configurations that are a
        parent of this configuration in the configuration hierarchy are
        included
      * isolated: parameters are contained to within this configuration

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_search_parameters(self):
        """Tests if this user can perform ``Parameter`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include parameters from parent
        configurations in the configuration hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this configuration only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_parameter_query(self):
        """Gets a paraameter query.

        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQuery

    parameter_query = property(fget=get_parameter_query)

    @abc.abstractmethod
    def get_parameters_by_query(self, parameter_query):
        """Gets a list of ``Parameters`` matching the given query.

        :param parameter_query: the parameter query
        :type parameter_query: ``osid.configuration.ParameterQuery``
        :return: the returned ``ParameterList``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a query form is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList


class ParameterSearchSession:
    """This session provides methods for searching ``Parameter`` objects.

    The search query is constructed using the ``ParameterQuery``.

    ``get_parameters_by_query()`` is the basic search method and returns
    a list of ``Parameters``. A more advanced search may be performed
    with ``getParametersBySearch()``. It accepts a ``ParameterSearch``
    in addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_parameters_by_search()`` returns a ``ParameterSearchResults``
    that can be used to access the resulting ``ParameterList`` or be
    used to perform a search within the result set through
    ``ParameterSearch``.

    Two views of the configuration data are defined;

      * federated: parameters defined in configurations that are a
        parent of this configuration in the configuration hierarchy are
        included
      * isolated: parameters are contained to within this configuration

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_parameter_search(self):
        """Gets a parameter search.

        :return: the parameter search
        :rtype: ``osid.configuration.ParameterSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterSearch

    parameter_search = property(fget=get_parameter_search)

    @abc.abstractmethod
    def get_parameter_search_order(self):
        """Gets a parameter entry search order.

        The ``ParameterEntrySearchOrder`` is supplied to an
        ``ParameterEntrySearch`` to specify the ordering of results.

        :return: the parameter search order
        :rtype: ``osid.configuration.ParameterSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterSearchOrder

    parameter_search_order = property(fget=get_parameter_search_order)

    @abc.abstractmethod
    def get_parameters_by_search(self, parameter_query, parameter_search):
        """Gets a list of ``Parameters`` matching the given search query using the given search.

        :param parameter_query: the parameter query
        :type parameter_query: ``osid.configuration.ParameterQuery``
        :param parameter_search: the parameter search
        :type parameter_search: ``osid.configuration.ParameterSearch``
        :return: the parameter search results
        :rtype: ``osid.configuration.ParameterSearchResults``
        :raise: ``NullArgument`` -- ``parameter_query`` or ``parameter_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``parameter_query`` or ``parameter_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterSearchResults

    @abc.abstractmethod
    def get_parameter_query_from_inspector(self, parameter_query_inspector):
        """Gets a parameter query from an inspector.

        The inspector is available from a ``ParameterSearchResults``.

        :param parameter_query_inspector: a parameter query inspector
        :type parameter_query_inspector: ``osid.configuration.ParameterQueryInspector``
        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``
        :raise: ``NullArgument`` -- ``parameter_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``parameter_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQuery


class ParameterAdminSession:
    """This session creates, updates, and deletes ``Parameters``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Parameter,`` a ``ParameterForm`` is requested using
    ``get_parameter_form_for_create()`` specifying the desired
    relationship peers and record ``Types`` or none if no record
    ``Types`` are needed. The returned ``ParameterForm`` will indicate
    that it is to be used with a create operation and can be used to
    examine metdata or validate data prior to creation. Once the
    ``ParameterForm`` is submiited to a create operation, it cannot be
    reused with another create operation unless the first operation was
    unsuccessful. Each ``ParameterForm`` corresponds to an attempted
    transaction.

    For updates, ``ParameterForms`` are requested to the ``Parameter``
    ``Id`` that is to be updated using ``getParameterFormForUpdate()``.
    Similarly, the ``ParameterForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``ParameterForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Parameters``. To unmap a
    ``Parameter`` from the current ``Configuration,`` the
    ``ParameterConfigurationAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Parameter`` itself thus
    removing it from all known ``Configuration`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_create_parameters(self):
        """Tests if this user can create ``Parameters``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Parameter`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_parameter_with_record_types(self, parameter_record_types):
        """Tests if this user can create a single ``Parameter`` using the desired record types.

        While ``ConfigurationManager.getParameterRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Parameter``. Providing an empty array tests if a ``Parameter``
        can be created with no records.

        :param parameter_record_types: array of parameter record types
        :type parameter_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Parameter`` creation using the specified record ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_form_for_create(self, parameter_record_types):
        """Gets the paramater form for creating new parameters.

        :param parameter_record_types: array of parameter record types
        :type parameter_record_types: ``osid.type.Type[]``
        :return: the parameter form
        :rtype: ``osid.configuration.ParameterForm``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterForm

    @abc.abstractmethod
    def create_parameter(self, parameter_form):
        """Creates a new ``Parameter``.

        :param parameter_form: the form for this ``Parameter``
        :type parameter_form: ``osid.configuration.ParameterForm``
        :return: the new ``Parameter``
        :rtype: ``osid.configuration.Parameter``
        :raise: ``IllegalState`` -- ``parameter_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``parameter_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``parameter_form`` did not originate from ``get_parameter_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Parameter

    @abc.abstractmethod
    def can_update_parameters(self):
        """Tests if this user can update ``Parameters``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Parameter`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_form_for_update(self, parameter_id):
        """Gets the parameter form for updating an existing parameters.

        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: the parameter form
        :rtype: ``osid.configuration.ParameterForm``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterForm

    @abc.abstractmethod
    def update_parameter(self, parameter_form):
        """Updates an existing parameter.

        :param parameter_form: the form containing the elements to be updated
        :type parameter_form: ``osid.configuration.ParameterForm``
        :raise: ``IllegalState`` -- ``parameter_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``parameter_id`` or ``parameter_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``parameter_form`` did not originate from ``get_parameter_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_parameters(self):
        """Tests if this user can delete ``Parameters``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Parameter`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_parameter(self, parameter_id):
        """Deletes a ``Parameter``.

        :param parameter_id: the ``Id`` of the ``Parameter`` to remove
        :type parameter_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parameter_id`` not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_parameter_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Parameters``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_parameter(self, parameter_id, alias_id):
        """Adds an ``Id`` to a ``Parameter`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Parameter`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another parameter it is
        reassigned to the given parameter ``Id``.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``parameter_id`` not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ParameterNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Configurations`` and their properties.

    This session is intended for adapters and providers needing to
    synchronize their state with this service without the use of
    polling. Notifications are cancelled when this session is closed.

    Two views are defined;

      * federated: parameters defined in configurations that are a
        parent of this configuration in the configuration hierarchy are
        included for notifications
      * isolated: notifications are restricted to parameters are defined
        to within this configuration


    The methods ``federate_parameter_view()`` and
    ``isolate_parameter_view()`` behave as a radio group and one should
    be selected before invoking any lookup methods.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_register_for_parameter_notifications(self):
        """Tests if this user can register for ``Parameter`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.

        A federated view will include parameters in configurations of
        which this registries is a child in the configuration hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications for parameter values to
        this configuration only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reliable_parameter_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_parameter_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_parameter_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_parameter_notification(self, notification_id):
        """Acknowledge a parameter notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_parameters(self):
        """Assigns a callback for notifications of new parameters.

        ``ParameterReceiver.newParameters()`` is invoked when a new
        ``Parameter`` is added to this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_parameters(self):
        """Assigns a callback for notification of updated parameters.

        ``ParameterReceiver.changedParameters()`` is invoked when a
        ``Parameter`` is changed in this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_parameter(self, parameter_id):
        """Assigns a callback for notifications of an update to a parameter.

        ``ParamaterReceiver.changedParameters()`` is invoked when the
        specified ``Parameter`` is changed in this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_parameters(self):
        """Assigns a callback for notification of deleted parameters.

        ``ParameterReceiver.deletedParamaters()`` is invoked when a
        ``Parameter`` is deleted or removed from this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_parameter(self, parameter_id):
        """Assigns a callback for notifications of a deleted parameter.

        ``ParameterReceiver.deletedParameters()`` is invoked when the
        specified ``Parameter`` is deleted or removed from this
        configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ParameterConfigurationSession:
    """This session defines methods for accessing the configurations of a parameter.

    A ``Parameter`` may appear in multiple ``Configurations``. Each
    ``Configuration`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_parameter_configurations(self):
        """Tests if this user can perform lookups on configurations of parameters.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookups are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_parameter_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_parameter_view(self):
        """A complete view of the ``Parameter`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_parameter_ids_by_configuration(self, configuration_id):
        """Gets the list of ``Parameter``  ``Ids`` associated with a ``Configuration``.

        :param configuration_id: ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: list of matching parameter ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parameters_by_configuration(self, configuration_id):
        """Gets the list of ``Parameters`` associated with a ``Configuration``.

        :param configuration_id: ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: list of matching parameters
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    @abc.abstractmethod
    def get_parameter_ids_by_configurations(self, configuration_ids):
        """Gets the list of ``Parameter Ids`` associated with a list of ``Configurations``.

        :param configuration_ids: list of configurations
        :type configuration_ids: ``osid.id.IdList``
        :return: list of parameter ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parameters_by_configurations(self, configuration_ids):
        """Gets the list of ``Parameters`` associated with a list of ``Configurations``.

        :param configuration_ids: list of configurations
        :type configuration_ids: ``osid.id.IdList``
        :return: list of parameters
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterList

    @abc.abstractmethod
    def get_configuration_ids_by_parameter(self, parameter_id):
        """Gets the ``Configuration Ids`` mapped to a ``Parameter``.

        :param parameter_id: ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: list of configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_configurations_by_parameter(self, parameter_id):
        """Gets the ``Configurations`` mapped to a ``Parameter``.

        :param parameter_id: ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: list of configurations
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList


class ParameterConfigurationAssignmentSession:
    """This session provides methods to re-assign ``Parameters`` to ``Configurations``.

    A ``Parameter`` may appear in multiple ``Configurations`` and
    removing the last reference to a ``Parameter`` is the equivalent of
    deleting it which may or may not be permitted. Each
    ``Configuration`` may have its own authorizations as to who is
    allowed to operate on it.

    Moving or adding a reference of a ``Parameter`` to another
    ``Configuration`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_assign_parameter_configurations(self):
        """Tests if this user can change parameter configuration mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not wish to offer
        assignment operations.

        :return: ``false`` if parameter configuration assignment is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_assign_parameters_to_configuration(self, configuration_id):
        """Tests if this user can alter parameter/configuration parameters.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known parameter methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: ``false`` if configuration is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_assignable_configuration_ids(self, configuration_id):
        """Gets a list of configurations including and under the given configuration node in which any parameter can be
        assigned.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: list of assignable configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_assignable_configuration_ids_for_parameter(self, configuration_id, parameter_id):
        """Gets a list of configurations including and under the given configuration node in which a specific parameter
        can be assigned.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: list of assignable configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_id`` or ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def assign_parameter_to_configuration(self, parameter_id, configuration_id):
        """Adds an existing ``Parameter`` to a ``Configuration``.

        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``parameter_id`` and ``configuration_id`` already mapped
        :raise: ``NotFound`` -- ``parameter_id`` or ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unassign_parameter_from_configuration(self, parameter_id, configuration_id):
        """Removes a ``Parameter`` from a ``Configuration``.

        :param parameter_id: the Id of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param configuration_id: the Id of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parameter_id`` or ``configuration_id`` not found or is not mapped
        :raise: ``NullArgument`` -- ``parameter_id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def reassign_parameter_to_configuration(self, parameter_id, from_configuration_id, to_configuration_id):
        """Moves a ``Parameter`` from one ``Configuration`` to another.

        Mappings to other ``Configurations`` are unaffected.

        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param from_configuration_id: the ``Id`` of the current ``Configuration``
        :type from_configuration_id: ``osid.id.Id``
        :param to_configuration_id: the ``Id`` of the destination ``Configuration``
        :type to_configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parameter_id from_configuration_id,`` or ``to_configuration_id`` not found or
        ``credit_id`` not mapped to ``from_configuration_id``
        :raise: ``NullArgument`` -- ``parameter_id, from_configuration_id,`` or ``to_configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ParameterSmartConfigurationSession:
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``ParameterQuery`` can be retrieved from this session and mapped
    to this ``Configuration`` to create a virtual collection of
    ``Parameters``. The parameters may be sequenced using the
    ``ParameterSearchOrder`` from this session.

    This ``Configuration`` has a default query that matches any
    parameter and a default search order that specifies no sequencing.
    The queries may be examined using a ``ParameterQueryInspector``. The
    query may be modified by converting the inspector back to a
    ``ParameterQuery``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_id = property(fget=get_configuration_id)

    @abc.abstractmethod
    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    configuration = property(fget=get_configuration)

    @abc.abstractmethod
    def can_manage_smart_configurations(self):
        """Tests if this user can manage smart configurations.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart cobfiguration management is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_query(self):
        """Gets a parameter query.

        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQuery

    parameter_query = property(fget=get_parameter_query)

    @abc.abstractmethod
    def get_parameter_search_order(self):
        """Gets a parameter search order.

        :return: the parameter search order
        :rtype: ``osid.configuration.ParameterSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterSearchOrder

    parameter_search_order = property(fget=get_parameter_search_order)

    @abc.abstractmethod
    def apply_parameter_query(self, parameter_query):
        """Applies a parameter query to this configuration.

        :param parameter_query: the parameter query
        :type parameter_query: ``osid.configuration.ParameterQuery``
        :raise: ``NullArgument`` -- ``parameter_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``parameter_query`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def inspec_parameter_query(self):
        """Gets a parameter query inspector for this configuration.

        :return: the parameter query inspector
        :rtype: ``osid.configuration.ParameterQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQueryInspector

    @abc.abstractmethod
    def apply_parameter_sequencing(self, parameter_search_order):
        """Applies a parameter search order to this configuration.

        :param parameter_search_order: the parameter search order
        :type parameter_search_order: ``osid.configuration.ParameterSearchOrder``
        :raise: ``NullArgument`` -- ``parameter_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``parameter_search_order`` not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_parameter_query_from_inspector(self, parameter_query_inspector):
        """Gets a parameter query from an inspector.

        :param parameter_query_inspector: a parameter query inspector
        :type parameter_query_inspector: ``osid.configuration.ParameterQueryInspector``
        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``
        :raise: ``NullArgument`` -- ``parameter_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``parameter_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ParameterQuery


class ConfigurationLookupSession:
    """This session provides methods for retrieving ``Configuration`` objects.

    The ``Configuration`` represents a collection of parameter values.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Configurations`` it can access, without breaking
    execution. However, an assessment may only be useful if all
    ``Configurations`` referenced by it are available, and a test-taking
    applicationmay sacrifice some interoperability for the sake of
    precision.

    Configurations may have an additional interface indicated by their
    respective types. The interface extension is accessed via the
    ``Configuration``. The returns may not be cast directly from the
    returns in the lookup methods.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_lookup_configurations(self):
        """Tests if this user can perform ``Configuration`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_configuration_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_configuration_view(self):
        """A complete view of the ``Configuration`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_configuration(self, configuration_id):
        """Gets the ``Configuration`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Configuration`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Configuration`` and
        retained for compatibility.

        :param configuration_id: the ``Id`` of the ``Configuration`` to retrieve
        :type configuration_id: ``osid.id.Id``
        :return: the ``Configuration``
        :rtype: ``osid.configuration.Configuration``
        :raise: ``NotFound`` -- no ``Configuration`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    @abc.abstractmethod
    def get_configurations_by_ids(self, configuration_ids):
        """Gets a ``ConfigurationList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        configurations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Configurations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param configuration_ids: the list of ``Ids`` to retrieve
        :type configuration_ids: ``osid.id.IdList``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def get_configurations_by_genus_type(self, configuration_genus_type):
        """Gets an ``ConfigurationList`` corresponding to the given configuration genus ``Type`` which does not include
        configuration types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param configuration_genus_type: a configuration genus type
        :type configuration_genus_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def get_configurations_by_parent_genus_type(self, configuration_genus_type):
        """Gets an ``ConfigurationList`` corresponding to the given configuration genus ``Type`` and include any
        additional configurations with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param configuration_genus_type: a configuration genus type
        :type configuration_genus_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def get_configurations_by_record_type(self, configuration_record_type):
        """Gets a ``ConfigurationList`` containing the given configuration record ``Type``.

        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def get_configurations_by_provider(self, resource_id):
        """Gets a ``ConfigurationList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def get_configurations(self):
        """Gets all ``Configurations,`` In plenary mode, the returned list contains all known configurations or an error
        results.

        Otherwise, the returned list may contain only those
        configurations that are accessible through this session.

        :return: a list of ``Configurations``
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    configurations = property(fget=get_configurations)


class ConfigurationQuerySession:
    """This session provides methods for searching among ``Configuration`` objects.

    The search query is constructed using the ``ConfigurationQuery``.

    Configurations may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``ConfigurationQuery``. The returns in this session may not be cast
    directly to these interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_search_configurations(self):
        """Tests if this user can perform ``Configuration`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_query(self):
        """Gets a configuration query.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQuery

    configuration_query = property(fget=get_configuration_query)

    @abc.abstractmethod
    def get_configurations_by_query(self, configuration_query):
        """Gets a list of ``Configurations`` matching the given search.

        :param configuration_query: the configuration query
        :type configuration_query: ``osid.configuration.ConfigurationQuery``
        :return: the returned ``ConfigurationList``
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList


class ConfigurationSearchSession:
    """This session provides methods for searching among ``Configuration`` objects.

    The search query is constructed using the ``ConfigurationQuery``.

    ``get_configurations_by_query()`` is the basic search method and
    returns a list of ``Configuration`` objects.A more advanced search
    may be performed with ``getConfigurationsBySearch()``. It accepts a
    ``ConfigurationSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_configurations_by_search()`` returns a
    ``ConfigurationSearchResults`` that can be used to access the
    resulting ``ConfigurationList`` or be used to perform a search
    within the result set through ``ConfigurationSearch``.

    Configurations may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``ConfigurationQuery``. The returns in this session may not be cast
    directly to these interfaces.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_search(self):
        """Gets a configuration search.

        :return: the configuration search
        :rtype: ``osid.configuration.ConfigurationSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationSearch

    configuration_search = property(fget=get_configuration_search)

    @abc.abstractmethod
    def get_configuration_search_order(self):
        """Gets a log search order.

        The ``ConfigurationSearchOrder`` is supplied to a
        ``ConfigurationSearch`` to specify the ordering of results.

        :return: the configuration search order
        :rtype: ``osid.configuration.ConfigurationSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationSearchOrder

    configuration_search_order = property(fget=get_configuration_search_order)

    @abc.abstractmethod
    def get_configurations_by_search(self, configuration_query, configuration_search):
        """Gets a list of ``Configurations`` matching the given search.

        Each element in the array is OR'd.

        :param configuration_query: the configuration query
        :type configuration_query: ``osid.configuration.ConfigurationQuery``
        :param configuration_search: the configuration search
        :type configuration_search: ``osid.configuration.ConfigurationSearch``
        :return: the configuration search results
        :rtype: ``osid.configuration.ConfigurationSearchResults``
        :raise: ``NullArgument`` -- ``configuration_query`` or ``configuration_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_query`` or ``configuration_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationSearchResults

    @abc.abstractmethod
    def get_configuration_query_from_inspector(self, configuration_query_inspector):
        """Gets a configuration query from an inspector.

        The inspector is available from a
        ``ConfigurationSearchResults``.

        :param configuration_query_inspector: a configuration query inspector
        :type configuration_query_inspector: ``osid.configuration.ConfigurationQueryInspector``
        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``NullArgument`` -- ``configuration_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``configuration_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationQuery


class ConfigurationAdminSession:
    """This session creates, updates, and deletes ``Configuration``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Configuration,`` a ``ConfigurationForm`` is requested using
    ``get_configuration_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``ConfigurationForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``ConfigurationForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``ConfigurationForm`` corresponds to an attempted transaction.

    For updates, ``ConfigurationForms`` are requested to the
    ``Configuration``  ``Id`` that is to be updated using
    ``getConfigurationFormForUpdate()``. Similarly, the
    ``ConfigurationForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``ConfigurationForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Configurations``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_create_configurations(self):
        """Tests if this user can create ``Configurations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a C
        ``onfiguration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def can_create_configuration_with_record_types(self, configuration_record_types):
        """Tests if this user can create a single ``Configuration`` using the desired record types.

        While ``ConfigurationManager.getConfigurationRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Configuration``. Providing an empty array tests if a
        ``Configuration`` can be created with no records.

        :param configuration_record_types: array of configuration record types
        :type configuration_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Configuration`` creation using the specified record ``Types`` is supported, ``false``
        otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_form_for_create(self, configuration_record_types):
        """Gets the configuration form for creating new configurations.

        A new form should be requested for each create transaction.

        :param configuration_record_types: array of configuration record types
        :type configuration_record_types: ``osid.type.Type[]``
        :return: the configuration form
        :rtype: ``osid.configuration.ConfigurationForm``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationForm

    @abc.abstractmethod
    def create_configuration(self, configuration_form):
        """Creates a new ``Configuration``.

        :param configuration_form: the configuration form
        :type configuration_form: ``osid.configuration.ConfigurationForm``
        :return: the new ``Configuration``
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- ``configuration_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``configuration_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_form`` did not originate from ``get_configuration_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.Configuration

    @abc.abstractmethod
    def can_update_configurations(self):
        """Tests if this user can update ``Configurations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a C
        ``onfiguration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_form_for_update(self, configuration_id):
        """Gets the configuration form for updating existing configurations.

        A new configuration form should be requested for each update
        transaction.

        :param configuration_id: ``Id`` of a ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: the configuration form
        :rtype: ``osid.configuration.ConfigurationForm``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationForm

    @abc.abstractmethod
    def update_configuration(self, configuration_form):
        """Updates an existing ``Configuration``.

        :param configuration_form: the configuration form
        :type configuration_form: ``osid.configuration.ConfigurationForm``
        :raise: ``IllegalState`` -- ``configuration_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``configuration_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_form`` did not originate from ``get_configuration_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_delete_configurations(self):
        """Tests if this user can delete ``Configurations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Configuration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def delete_configuration(self, configuration_id):
        """Deletes a ``Configuration``.

        :param configuration_id: the ``Id`` of the ``Configuration`` to delete
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def can_manage_configuration_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Configurations``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def alias_configuration(self, configuration_id, alias_id):
        """Adds an ``Id`` to a ``Configuration`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Configuration`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another configuration it is
        reassigned to the given configuration ``Id``.

        :param configuration_id: the ``Id`` of a ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ConfigurationNotificationSession:
    """This session defines methods to receive notifications on adds/changes to ``Configurations``.

    Notrifications related to adding or removing of parameters are
    handled through the ``ValueNotificationSession``. This session is
    intended for adapters and providers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def can_register_for_configuration_notifications(self):
        """Tests if this user can register for ``Configuration`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def reliable_configuration_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_configuration_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def unreliable_configuration_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def acknowledge_configuration_notification(self, notification_id):
        """Acknowledge a configuration notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_new_configurations(self):
        """Registers for notifications of new configurations.

        ``ConfigurationReceiver.newConfigurations()`` is invoked when a
        new ``Configuration`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_configurations(self):
        """Registers for notification of updated configurations.

        ``ConfigurationReceiver.changedConfigurations()`` is invoked
        when a configuration is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_configuration(self, configuration_id):
        """Registers for notifications of an update to a configuration.

        ``ConfigurationReceiver.changedConfigurations()`` is invoked
        when the specified ``Configuration`` is changed.

        :param configuration_id: the ``Id`` of the ``Configuration`` to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Configuration`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_configurations(self):
        """Registers for notification of deleted configurations.

        ``ConfigurationReceiver.deletedConfigurations()`` is invoked
        when a ``Configuration`` is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_deleted_configuration(self, configuration_id):
        """Registers for notifications of a deleted configuration.

        ``ConfiguratinReceiver.deletedConfigurations()`` is invoked when
        the specified configuration is deleted.

        :param configuration_id: the ``Id`` of the ``Configuration`` to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Configuration`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_configuration_hierarchy(self):
        """Registers for notification of an updated configuration hierarchy structure.

        ``ConfigurationReceiver.changedChildOfConfigurations()`` is
        invoked when a node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_configuration_hierarchy_for_ancestors(self, configuration_id):
        """Registers for notification of an updated configuration hierarchy structure.

        ``ConfigurationReceiver.changedChildOfConfigurations()`` is
        invoked when the specified node or any of its ancestors
        experiences a change in its children.

        :param configuration_id: the ``Id`` of the ``Configuration`` node to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def register_for_changed_configuration_hierarchy_for_descendants(self, configuration_id):
        """Registers for notification of an updated configuration hierarchy structure.

        ``ConfigurationReceiver.changedChildOfConfigurations()`` is
        invoked when the specified node or any of its descendants
        experiences a change in its children.

        :param configuration_id: the ``Id`` of the ``Configuration`` node to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ConfigurationHierarchySession:
    """This session defines methods for traversing a hierarchy of ``Configuration`` objects.

    Each node in the hierarchy is a unique ``Configuration``. The
    hierarchy may be traversed recursively to establish the tree
    structure through ``get_parent_configurations()`` and
    ``getChildConfigurations()``. To relate these ``Ids`` to another
    OSID, ``get_configuration_nodes()`` can be used for retrievals that
    can be used for bulk lookups in other OSIDs. Any ``Configuration``
    available in the Configuration OSID is known to this hierarchy but
    does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_configurationss()`` or
    ``get_child_configurations()`` in lieu of a ``PermissionDenied``
    error that may disrupt the traversal through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: configuration elements may be silently omitted
        or re-ordered
      * plenary view: provides a complete set or is an error condition

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the configuration ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_hierarchy_id = property(fget=get_configuration_hierarchy_id)

    @abc.abstractmethod
    def get_configuration_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    configuration_hierarchy = property(fget=get_configuration_hierarchy)

    @abc.abstractmethod
    def can_access_configuration_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def use_comparative_configuration_view(self):
        """The returns from the configuration methods may omit or translate elements based on this session, such as
        authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def use_plenary_configuration_view(self):
        """A complete view of the ``Configuration`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_root_configuration_ids(self):
        """Gets the root configuration ``Ids`` in this hierarchy.

        :return: the root configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    root_configuration_ids = property(fget=get_root_configuration_ids)

    @abc.abstractmethod
    def get_root_configurations(self):
        """Gets the root configurations in the configuration hierarchy.

        A node with no parents is an orphan. While all configuration
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root configurations
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    root_configurations = property(fget=get_root_configurations)

    @abc.abstractmethod
    def has_parent_configurations(self, configuration_id):
        """Tests if the ``Configuration`` has any parents.

        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the configuration has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_parent_of_configuration(self, id_, configuration_id):
        """Tests if an ``Id`` is a direct parent of configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``configuration_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_parent_configuration_ids(self, configuration_id):
        """Gets the parent ``Ids`` of the given configuration.

        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: the parent Ids of the configuration
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_parent_configurations(self, configuration_id):
        """Gets the parents of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the parents of the configuration
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def is_ancestor_of_configuration(self, id_, configuration_id):
        """Tests if an Id is an ancestor of a configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def has_child_configurations(self, configuration_id):
        """Tests if a configuration has any children.

        :param configuration_id: a ``configuration_id``
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``configuration_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def is_child_of_configuration(self, id_, configuration_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_child_configuration_ids(self, configuration_id):
        """Gets the child ``Ids`` of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the children of the configuration
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.IdList

    @abc.abstractmethod
    def get_child_configurations(self, configuration_id):
        """Gets the children of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the children of the configuration
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationList

    @abc.abstractmethod
    def is_descendant_of_configuration(self, id_, configuration_id):
        """Tests if an ``Id`` is a descendant of a configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_node_ids(self, configuration_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a configuration node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Node

    @abc.abstractmethod
    def get_configuration_nodes(self, configuration_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
        node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
        in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a configuration node
        :rtype: ``osid.configuration.ConfigurationNode``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.configuration.ConfigurationNode


class ConfigurationHierarchyDesignSession:
    """This session defines methods for managing a hierarchy of ``Configuration`` objects.

    Each node in the hierarchy is a unique ``Configuration``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_configuration_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.id.Id

    configuration_hierarchy_id = property(fget=get_configuration_hierarchy_id)

    @abc.abstractmethod
    def get_configuration_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.hierarchy.Hierarchy

    configuration_hierarchy = property(fget=get_configuration_hierarchy)

    @abc.abstractmethod
    def can_modify_configuration_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def add_root_configuration(self, configuration_id):
        """Adds a root configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``configuration_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_root_configuration(self, configuration_id):
        """Removes a root configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not a root
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def add_child_configuration(self, configuration_id, child_id):
        """Adds a child to a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``configuration_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``configuration_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_configuration(self, configuration_id, child_id):
        """Removes a child from a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``configuration_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def remove_child_configurations(self, configuration_id):
        """Removes all children from a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass
