"""Implementations of configuration abstract base class managers."""
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


class ConfigurationProfile:
    """The ``ConfigurationProfile`` describes the profile of the configuration service."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if federation is visible for this service.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_value_retrieval(self):
        """Tests for the availability of a configuration value retrieval service.

        :return: ``true`` if value retrieval is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_value_lookup(self):
        """Tests for the availability of a configuration value lookup service.

        :return: ``true`` if value lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_value_query(self):
        """Tests for the availability of a configuration value query service.

        :return: ``true`` if value query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_value_search(self):
        """Tests for the availability of a configuration value search service.

        :return: ``true`` if value search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_value_admin(self):
        """Tests for the availability of a configuration value administration service.

        :return: ``true`` if value administration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_value_notification(self):
        """Tests for the availability of a configuration value notification service.

        :return: ``true`` if value notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_lookup(self):
        """Tests for the availability of a parameter lookup service.

        :return: ``true`` if parameter lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_query(self):
        """Tests for the availability of a parameter query service.

        :return: ``true`` if parameter query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_search(self):
        """Tests for the availability of a parameter search service.

        :return: ``true`` if parameter search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_admin(self):
        """Tests for the availability of a parameter update service.

        :return: ``true`` if parameter update is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_notification(self):
        """Tests for the availability of a parameter notification service.

        :return: ``true`` if parameter notification is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_configuration(self):
        """Tests for the availability of a service to lookup mappings of parameters to configurations.

        :return: ``true`` if parameter configuration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_configuration_assignment(self):
        """Tests for the availability of a service to map parameters to configurations.

        :return: ``true`` if parameter configuration assignment is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_parameter_smart_configuration(self):
        """Tests for the availability of a parameter smart configuration service.

        :return: ``true`` if parameter smart configuration service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_lookup(self):
        """Tests for the availability of a configuration lookup service.

        :return: ``true`` if configuration lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_query(self):
        """Tests for the availability of a configuration query service.

        :return: ``true`` if configuration query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_search(self):
        """Tests for the availability of a configuration search service.

        :return: ``true`` if configuration search is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_admin(self):
        """Tests for the availability of a configuration admin service.

        :return: ``true`` if configuration admin is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_notification(self):
        """Tests for the availability of a notification service for subscribing to changes to configurations.

        :return: ``true`` if a configuration notification service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_hierarchy(self):
        """Tests for the availability of a configuration hierarchy traversal service.

        :return: ``true`` if a configuration hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_hierarchy_design(self):
        """Tests for the availability of a configuration hierarchy design service.

        :return: ``true`` if a configuration hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_batch(self):
        """Tests for the availability of a configuration batch service.

        :return: ``true`` if a configuration batch service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_configuration_rules(self):
        """Tests for the availability of a configuration rules service.

        :return: ``true`` if a configuration rules service is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_condition_record_types(self):
        """Gets the supported value condition record types.

        :return: a list containing the supported ``ValueCondition`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    value_condition_record_types = property(fget=get_value_condition_record_types)

    @abc.abstractmethod
    def supports_value_condition_record_type(self, value_condition_record_type):
        """Tests if the given ``ValueCondition`` record type is supported.

        :param value_condition_record_type: a ``Type`` indicating a ``ValueCondition`` record type
        :type value_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given value condition record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_condition_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_record_types(self):
        """Gets all the value record types supported.

        :return: the list of supported value record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    value_record_types = property(fget=get_value_record_types)

    @abc.abstractmethod
    def supports_value_record_type(self, value_record_type):
        """Tests if a given value record type is supported.

        :param value_record_type: the value record type
        :type value_record_type: ``osid.type.Type``
        :return: ``true`` if the value record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_value_search_record_types(self):
        """Gets all the value search record types supported.

        :return: the list of supported value search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    value_search_record_types = property(fget=get_value_search_record_types)

    @abc.abstractmethod
    def supports_value_search_record_type(self, value_search_record_type):
        """Tests if a given value search type is supported.

        :param value_search_record_type: the value search record type
        :type value_search_record_type: ``osid.type.Type``
        :return: ``true`` if the value search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_record_types(self):
        """Gets all the parameter record types supported.

        :return: the list of supported parameter record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    parameter_record_types = property(fget=get_parameter_record_types)

    @abc.abstractmethod
    def supports_parameter_record_type(self, parameter_record_type):
        """Tests if a given parameter record type is supported.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: ``true`` if the parameter record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_parameter_search_record_types(self):
        """Gets all the parameter search record types supported.

        :return: the list of supported parameter search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    parameter_search_record_types = property(fget=get_parameter_search_record_types)

    @abc.abstractmethod
    def supports_parameter_search_record_type(self, parameter_search_record_type):
        """Tests if a given parameter search record type is supported.

        :param parameter_search_record_type: the value search type
        :type parameter_search_record_type: ``osid.type.Type``
        :return: ``true`` if the parameter search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_record_types(self):
        """Gets all the configuration record types supported.

        :return: the list of supported configuration record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    configuration_record_types = property(fget=get_configuration_record_types)

    @abc.abstractmethod
    def supports_configuration_record_type(self, configuration_record_type):
        """Tests if a given configuration record type is supported.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: ``true`` if the configuration record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_configuration_search_record_types(self):
        """Gets all the configuration search record types supported.

        :return: the list of supported configuration search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    configuration_search_record_types = property(fget=get_configuration_search_record_types)

    @abc.abstractmethod
    def supports_configuration_search_record_type(self, configuration_search_record_type):
        """Tests if a given configuration search record type is supported.

        :param configuration_search_record_type: the configuration search record type
        :type configuration_search_record_type: ``osid.type.Type``
        :return: ``true`` if the configuration search record type is support ``e`` d, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class ConfigurationManager:
    """The configuration manager provides access sessions to retrieve and manage configurations.

    A manager may support federation in that values can be accessed in a
    specified configuration and parameters may be defined in a specified
    registry. The sessions included in this manager are:

      * ``ValueRetrievalSession:`` a basic session for retrieving
        configuration values
      * ``ValueLookupSession:`` a basic session for looking up
        configuration values
      * ``ValueQuerySession:`` a basic session for querying
        configuration values
      * ``ValueSearchSession:`` a basic session for searching
        configuration values
      * ``ValueAdminSession:`` a session for setting and changing
        configuration values
      * ``ValueNotificationSession:`` a session for subscribing to
        changes of configuration values

      * ``ParameterLookupSession:`` a session for retrieving defined
        parameters
      * ``ParameterQuerySession:`` a session for querying defined
        parameters
      * ``ParameterSearchSession:`` a session for searching defined
        parameters
      * ``ParameterAdminSession:`` a session for creating, updating and
        deleting parameter definitions
      * ``ParameterNoitificationSession:`` a session for subscribing to
        adds and changes of parameters
      * ``ParamaterRegistrySession:`` a session for examining mappings
        of parameters to registries
      * ``ParamaterRegistryAssignmentSession:`` a session for making
        mappings of parameters to registries
      * ``ParameterConfigurationSession:`` a session for examining
        mappings of parameters to configurations
      * ``ParameterConfigurationAssignmentSession:`` a session for
        mapping parameters to configurations
      * ``ParameterSmartConfigurationSession:`` a session for managing
        smart configurations of parameters

      * ``ConfigurationLookupSession:`` a session for retrieving
        configurations
      * ``ConfigurationQuerySession:`` a session for querying
        configurations
      * ``ConfigurationSearchSession:`` a session for searching
        configurations
      * ``ConfigurationAdminSession:`` a session for creating and
        updating configurations
      * ``ConfigurationNotificationSession:`` a session for subscribing
        to adds and changes to configurations
      * ``ConfigurationHierarchySession:`` a session for traversing a
        hierarchy of configurations
      * ``ConfigurationHierarchyDesignSession:`` a session for managing
        a hierarchy of configurations

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_retrieval_session(self):
        """Gets a configuration value retrieval session.

        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_retrieval()`` is ``true``.*

        """
        return  # osid.configuration.ValueRetrievalSession

    value_retrieval_session = property(fget=get_value_retrieval_session)

    @abc.abstractmethod
    def get_value_retrieval_session_for_configuration(self, configuration_id):
        """Gets a configuration value retrieval session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_retrieval()`` are ``true``.*

        """
        return  # osid.configuration.ValueRetrievalSession

    @abc.abstractmethod
    def get_value_lookup_session(self):
        """Gets a configuration value lookup session.

        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ValueLookupSession

    value_lookup_session = property(fget=get_value_lookup_session)

    @abc.abstractmethod
    def get_value_lookup_session_for_configuration(self, configuration_id):
        """Gets a configuration value lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_lookup()`` are ``true``.*

        """
        return  # osid.configuration.ValueLookupSession

    @abc.abstractmethod
    def get_value_query_session(self):
        """Gets a configuration value query session.

        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_query()`` is ``true``.*

        """
        return  # osid.configuration.ValueQuerySession

    value_query_session = property(fget=get_value_query_session)

    @abc.abstractmethod
    def get_value_query_session_for_configuration(self, configuration_id):
        """Gets a configuration value query session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and ``supports_value_query()``
        are ``true``.*

        """
        return  # osid.configuration.ValueQuerySession

    @abc.abstractmethod
    def get_value_search_session(self):
        """Gets a configuration value search session.

        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_search()`` is ``true``.*

        """
        return  # osid.configuration.ValueSearchSession

    value_search_session = property(fget=get_value_search_session)

    @abc.abstractmethod
    def get_value_search_session_for_configuration(self, configuration_id):
        """Gets a configuration value search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_search()`` are ``true``.*

        """
        return  # osid.configuration.ValueSearchSession

    @abc.abstractmethod
    def get_value_admin_session(self):
        """Gets a configuration value administration session.

        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_admin()`` is ``true``.*

        """
        return  # osid.configuration.ValueAdminSession

    value_admin_session = property(fget=get_value_admin_session)

    @abc.abstractmethod
    def get_value_admin_session_for_configuration(self, configuration_id):
        """Gets a value administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- ``supports_value_admin()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unimplemented`` -- ``supports_value_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and ``supports_value_admin()``
        are ``true``.*

        """
        return  # osid.configuration.ValueAdminSession

    @abc.abstractmethod
    def get_value_notification_session(self, value_receiver):
        """Gets a value notification session.

        :param value_receiver: the notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NullArgument`` -- ``value_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_notification()`` is ``true``.*

        """
        return  # osid.configuration.ValueNotificationSession

    @abc.abstractmethod
    def get_value_notification_session_for_configuration(self, value_receiver, configuration_id):
        """Gets a value notification session using the specified configuration.

        :param value_receiver: the notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``value_receiver`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_notification()`` are ``true``.*

        """
        return  # osid.configuration.ValueNotificationSession

    @abc.abstractmethod
    def get_parameter_lookup_session(self):
        """Gets a parameter lookup session.

        :return: a ``ParameterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ParameterLookupSession

    parameter_lookup_session = property(fget=get_parameter_lookup_session)

    @abc.abstractmethod
    def get_parameter_lookup_session_for_configuration(self, configuration_id):
        """Gets a parameter lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParamaterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_lookup()`` are ``true``.*

        """
        return  # osid.configuration.ParameterLookupSession

    @abc.abstractmethod
    def get_parameter_query_session(self):
        """Gets a parameter query session.

        :return: a ``ParameterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_query()`` is ``true``.*

        """
        return  # osid.configuration.ParameterQuerySession

    parameter_query_session = property(fget=get_parameter_query_session)

    @abc.abstractmethod
    def get_parameter_query_session_for_configuration(self, configuration_id):
        """Gets a parameter search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParamaterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_query()`` are ``true``.*

        """
        return  # osid.configuration.ParameterQuerySession

    @abc.abstractmethod
    def get_parameter_search_session(self):
        """Gets a parameter search session.

        :return: a ``ParameterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_search()`` is ``true``.*

        """
        return  # osid.configuration.ParameterSearchSession

    parameter_search_session = property(fget=get_parameter_search_session)

    @abc.abstractmethod
    def get_parameter_search_session_for_configuration(self, configuration_id):
        """Gets a parameter search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParamaterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_search()`` are ``true``.*

        """
        return  # osid.configuration.ParameterSearchSession

    @abc.abstractmethod
    def get_parameter_admin_session(self):
        """Gets a parameter administration session.

        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_admin()`` is ``true``.*

        """
        return  # osid.configuration.ParameterAdminSession

    parameter_admin_session = property(fget=get_parameter_admin_session)

    @abc.abstractmethod
    def get_parameter_admin_session_for_configuration(self, configuration_id):
        """Gets a parameter administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_admin()`` are ``true``.*

        """
        return  # osid.configuration.ParameterAdminSession

    @abc.abstractmethod
    def get_parameter_notification_session(self, parameter_receiver):
        """Gets a parameter notification session.

        :param parameter_receiver: the notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NullArgument`` -- ``parameter_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_notification()`` is ``true``.*

        """
        return  # osid.configuration.ParameterNotificationSession

    @abc.abstractmethod
    def get_parameter_notification_session_for_configuration(self, parameter_receiver, configuration_id):
        """Gets a parameter notification session using the specified configuration.

        :param parameter_receiver: the notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_receiver`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_notification()`` are ``true``.*

        """
        return  # osid.configuration.ParameterNotificationSession

    @abc.abstractmethod
    def get_parameter_configuration_session(self):
        """Gets a session for looking up mappings of parameters to configurations.

        :return: a ``ParameterConfigurationSession``
        :rtype: ``osid.configuration.ParameterConfigurationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_configuration()`` is ``true``.*

        """
        return  # osid.configuration.ParameterConfigurationSession

    parameter_configuration_session = property(fget=get_parameter_configuration_session)

    @abc.abstractmethod
    def get_parameter_configuration_assignment_session(self):
        """Gets a session for managing mappings of parameters to configurations.

        :return: a ``ParameterConfigurationAssignmentSession``
        :rtype: ``osid.configuration.ParameterConfigurationAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_configuration_assignment()`` is ``true``.*

        """
        return  # osid.configuration.ParameterConfigurationAssignmentSession

    parameter_configuration_assignment_session = property(fget=get_parameter_configuration_assignment_session)

    @abc.abstractmethod
    def get_parameter_smart_configuration_session(self, configuration_id):
        """Gets a session for managing smart configurations.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParameterSmartConfigurationSession``
        :rtype: ``osid.configuration.ParameterSmartConfigurationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_smart_configuration()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_smart_configuration()`` is ``true``.*

        """
        return  # osid.configuration.ParameterSmartConfigurationSession

    @abc.abstractmethod
    def get_configuration_lookup_session(self):
        """Gets a configuration lookup session.

        :return: a ``ConfigurationLookupSession``
        :rtype: ``osid.configuration.ConfigurationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationLookupSession

    configuration_lookup_session = property(fget=get_configuration_lookup_session)

    @abc.abstractmethod
    def get_configuration_query_session(self):
        """Gets a configuration query session.

        :return: a ``ConfigurationQuerySession``
        :rtype: ``osid.configuration.ConfigurationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_query()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationQuerySession

    configuration_query_session = property(fget=get_configuration_query_session)

    @abc.abstractmethod
    def get_configuration_search_session(self):
        """Gets a configuration search session.

        :return: a ``ConfigurationSearchSession``
        :rtype: ``osid.configuration.ConfigurationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_search()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationSearchSession

    configuration_search_session = property(fget=get_configuration_search_session)

    @abc.abstractmethod
    def get_configuration_admin_session(self):
        """Gets a configuration administration session.

        :return: a ``ConfigurationAdminSession``
        :rtype: ``osid.configuration.ConfigurationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_admin()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationAdminSession

    configuration_admin_session = property(fget=get_configuration_admin_session)

    @abc.abstractmethod
    def get_configuration_notification_session(self, configuration_receiver):
        """Gets the notification session for subscribing to changes to configurations.

        :param configuration_receiver: the notification callback
        :type configuration_receiver: ``osid.configuration.ConfigurationReceiver``
        :return: a ``ConfigurationNotificationSession``
        :rtype: ``osid.configuration.ConfigurationNotificationSession``
        :raise: ``NullArgument`` -- ``configuration_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_notification()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationNotificationSession

    @abc.abstractmethod
    def get_configuration_hierarchy_session(self):
        """Gets a hierarchy traversal service for configurations.

        :return: a ``ConfigurationHierarchySession``
        :rtype: ``osid.configuration.ConfigurationHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_hierarchy()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationHierarchySession

    configuration_hierarchy_session = property(fget=get_configuration_hierarchy_session)

    @abc.abstractmethod
    def get_configuration_hierarchy_design_session(self):
        """Gets a hierarchy design service for configurations.

        :return: a ``ConfigurationHierarchyDesignSession``
        :rtype: ``osid.configuration.ConfigurationHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_hierarchy_design()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationHierarchyDesignSession

    configuration_hierarchy_design_session = property(fget=get_configuration_hierarchy_design_session)

    @abc.abstractmethod
    def get_configuration_batch_manager(self):
        """Gets a ``ConfigurationBatchManager``.

        :return: a ``ConfigurationBatchManager``
        :rtype: ``osid.configuration.batch.ConfigurationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_batch()`` is ``true``.*

        """
        return  # osid.configuration.batch.ConfigurationBatchManager

    configuration_batch_manager = property(fget=get_configuration_batch_manager)

    @abc.abstractmethod
    def get_configuration_rules_manager(self):
        """Gets a ``ConfigurationRulesManager``.

        :return: a ``ConfigurationRulesManager``
        :rtype: ``osid.configuration.rules.ConfigurationRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_rules()`` is ``true``.*

        """
        return  # osid.configuration.rules.ConfigurationRulesManager

    configuration_rules_manager = property(fget=get_configuration_rules_manager)


class ConfigurationProxyManager:
    """The configuration manager provides access to sessions to retrieve and manage configurations.

    Methods in this manager support the passing a ``Proxy``. A manager
    may support federation in that values can be accessed in a specified
    configuration and paramaters may be defined in a specified registry.
    The sessions included in this manager are:

      * ``ValueRetrievalSession:`` a basic session for retrieving
        configuration values
      * ``ValueLookupSession:`` a basic session for looking up
        configuration values
      * ``ValueQuerySession:`` a basic session for querying
        configuration values
      * ``ValueSearchSession:`` a basic session for searching
        configuration values
      * ``ValueAdminSession:`` a session for setting and changing
        configuration values
      * ``ValueNotificationSession:`` a session for subscribing to
        changes of configuration values

      * ``ParameterLookupSession:`` a session for retrieving defined
        parameters
      * ``ParameterQuerySession:`` a session for querying defined
        parameters
      * ``ParameterSearchSession:`` a session for searching defined
        parameters
      * ``ParameterAdminSession:`` a session for creating, updating and
        deleting parameter definitions
      * ``ParameterNoitificationSession:`` a session for subscribing to
        adds and changes of parameters
      * ``ParamaterRegistrySession:`` a session for examining mappings
        of parameters to registries
      * ``ParamaterRegistryAssignmentSession:`` a session for making
        mappings of parameters to registries
      * ``ParameterConfigurationSession:`` a session for examining
        mappings of parameters to configurations
      * ``ParameterConfigurationAssignmentSession:`` a session for
        mapping parameters to configurations
      * ``ParameterSmartConfigurationSession:`` a session for managing
        smart configurations of parameters

      * ``ConfigurationLookupSession:`` a session for retrieving
        configurations
      * ``ConfigurationQuerySession:`` a session for querying
        configurations
      * ``ConfigurationSearchSession:`` a session for searching
        configurations
      * ``ConfigurationAdminSession:`` a session for creating and
        updating configurations
      * ``ConfigurationNotificationSession:`` a session for subscribing
        to adds and changes to configurations
      * ``ConfigurationHierarchySession:`` a session for traversing a
        hierarchy of configurations
      * ``ConfigurationHierarchyDesignSession:`` a session for managing
        a hierarchy of configurations

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_value_retrieval_session(self, proxy):
        """Gets a configuration value retrieval session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_retrieval()`` is ``true``.*

        """
        return  # osid.configuration.ValueRetrievalSession

    @abc.abstractmethod
    def get_value_retrieval_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value retrieval session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` or ``supports_visible_federation()`` is ``False``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_retrieval()`` are ``true``*

        """
        return  # osid.configuration.ValueRetrievalSession

    @abc.abstractmethod
    def get_value_lookup_session(self, proxy):
        """Gets a configuration value lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ValueLookupSession

    @abc.abstractmethod
    def get_value_lookup_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` or ``supports_visible_federation()`` is ``False``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_lookup()`` are ``true``*

        """
        return  # osid.configuration.ValueLookupSession

    @abc.abstractmethod
    def get_value_query_session(self, proxy):
        """Gets a configuration value query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_query()`` is ``true``.*

        """
        return  # osid.configuration.ValueQuerySession

    @abc.abstractmethod
    def get_value_query_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value query session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` or ``supports_visible_federation()`` is ``False``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and ``supports_value_query()``
        are ``true``*

        """
        return  # osid.configuration.ValueQuerySession

    @abc.abstractmethod
    def get_value_search_session(self, proxy):
        """Gets a configuration value search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ValueSearchSession

    @abc.abstractmethod
    def get_value_search_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` or ``supports_visible_federation()`` is ``False``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_search()`` are ``true``*

        """
        return  # osid.configuration.ValueSearchSession

    @abc.abstractmethod
    def get_value_notification_session(self, value_receiver, proxy):
        """Gets a value notification session.

        :param value_receiver: notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NullArgument`` -- ``value_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_notification()`` is ``true``.*

        """
        return  # osid.configuration.ValueNotificationSession

    @abc.abstractmethod
    def get_value_notification_session_for_configuration(self, value_receiver, configuration_id, proxy):
        """Gets a value notification session using the specified configuration.

        :param value_receiver: notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``value_receiver, configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_value_notification()`` are ``true``.*

        """
        return  # osid.configuration.ValueNotificationSession

    @abc.abstractmethod
    def get_value_admin_session(self, proxy):
        """Gets a configuration value administration session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_value_admin()`` is ``true``.*

        """
        return  # osid.configuration.ValueAdminSession

    @abc.abstractmethod
    def get_value_admin_session_for_configuration(self, configuration_id, proxy):
        """Gets a value administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and ``supports_value_admin()``
        are ``true``.*

        """
        return  # osid.configuration.ValueAdminSession

    @abc.abstractmethod
    def get_parameter_lookup_session(self, proxy):
        """Gets a parameter lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ParameterLookupSession

    @abc.abstractmethod
    def get_parameter_lookup_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParamaterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_lookup()`` are ``true``.*

        """
        return  # osid.configuration.ParameterLookupSession

    @abc.abstractmethod
    def get_parameter_query_session(self, proxy):
        """Gets a parameter query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_query()`` is ``true``.*

        """
        return  # osid.configuration.ParameterQuerySession

    @abc.abstractmethod
    def get_parameter_query_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter query session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParamaterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_query()`` are ``true``.*

        """
        return  # osid.configuration.ParameterQuerySession

    @abc.abstractmethod
    def get_parameter_search_session(self, proxy):
        """Gets a parameter search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_search()`` is ``true``.*

        """
        return  # osid.configuration.ParameterSearchSession

    @abc.abstractmethod
    def get_parameter_search_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParamaterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_search()`` are ``true``.*

        """
        return  # osid.configuration.ParameterSearchSession

    @abc.abstractmethod
    def get_parameter_admin_session(self, proxy):
        """Gets a parameter administration session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_admin()`` is ``true``.*

        """
        return  # osid.configuration.ParameterAdminSession

    @abc.abstractmethod
    def get_parameter_admin_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_admin()`` are ``true``.*

        """
        return  # osid.configuration.ParameterAdminSession

    @abc.abstractmethod
    def get_parameter_notification_session(self, parameter_receiver, proxy):
        """Gets a parameter notification session.

        :param parameter_receiver: notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NullArgument`` -- ``parameter_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_notification()`` is ``true``.*

        """
        return  # osid.configuration.ParameterNotificationSession

    @abc.abstractmethod
    def get_parameter_notification_session_for_configuration(self, parameter_receiver, configuration_id, proxy):
        """Gets a parameter notification session using the specified configuration.

        :param parameter_receiver: notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NotFound`` -- ``registry_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_receiver, configuration_id,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` or ``supports_visible_federation()`` is
        ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_visible_federation()`` and
        ``supports_parameter_notification()`` are ``true``.*

        """
        return  # osid.configuration.ParameterNotificationSession

    @abc.abstractmethod
    def get_parameter_configuration_session(self, proxy):
        """Gets a session for examining mappings of parameters to configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterConfigurationSession``
        :rtype: ``osid.configuration.ParameterConfigurationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_configuration()`` is ``true``.*

        """
        return  # osid.configuration.ParameterConfigurationSession

    @abc.abstractmethod
    def get_parameter_configuration_assignment_session(self, proxy):
        """Gets a session for managing mappings of parameters to configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterConfigurationAssignmentSession``
        :rtype: ``osid.configuration.ParameterConfigurationAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_configuration_assignment()`` is ``true``.*

        """
        return  # osid.configuration.ParameterConfigurationAssignmentSession

    @abc.abstractmethod
    def get_parameter_smart_configuration_session(self, configuration_id, proxy):
        """Gets a session for managing smart configurations of parameters.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterSmartConfigurationSession``
        :rtype: ``osid.configuration.ParameterSmartConfigurationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuratin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_smart_configuration()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_parameter_smart_configuration()`` is ``true``.*

        """
        return  # osid.configuration.ParameterSmartConfigurationSession

    @abc.abstractmethod
    def get_configuration_lookup_session(self, proxy):
        """Gets a configuration lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationLookupSession``
        :rtype: ``osid.configuration.ConfigurationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_lookup()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationLookupSession

    @abc.abstractmethod
    def get_configuration_query_session(self, proxy):
        """Gets a configuration query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationQuerySession``
        :rtype: ``osid.configuration.ConfigurationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_query()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationQuerySession

    @abc.abstractmethod
    def get_configuration_search_session(self, proxy):
        """Gets a configuration search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationSearchSession``
        :rtype: ``osid.configuration.ConfigurationSearchSession``
        :raise: ``OperationFailed`` -- ``proxy`` is ``null``
        :raise: ``NullArgument`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_search()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationSearchSession

    @abc.abstractmethod
    def get_configuration_notification_session(self, configuration_receiver, proxy):
        """Gets the notification session for subscribing to changes to configurations.

        :param configuration_receiver: notification callback
        :type configuration_receiver: ``osid.configuration.ConfigurationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationNotificationSession``
        :rtype: ``osid.configuration.ConfigurationNotificationSession``
        :raise: ``NullArgument`` -- ``configuration_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_notification()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationNotificationSession

    @abc.abstractmethod
    def get_configuration_admin_session(self, proxy):
        """Gets a configuration administration session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationAdminSession``
        :rtype: ``osid.configuration.ConfigurationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_admin()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationAdminSession

    @abc.abstractmethod
    def get_configuration_hierarchy_session(self, proxy):
        """Gets a hierarchy traversal service for configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfiguraqtionHierarchySession``
        :rtype: ``osid.configuration.ConfigurationHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_hierarchy()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationHierarchySession

    @abc.abstractmethod
    def get_configuration_hierarchy_design_session(self, proxy):
        """Gets a hierarchy design service for configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationHierarchyDesignSession``
        :rtype: ``osid.configuration.ConfigurationHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_hierarchy_design()`` is ``true``.*

        """
        return  # osid.configuration.ConfigurationHierarchyDesignSession

    @abc.abstractmethod
    def get_configuration_batch_proxy_manager(self):
        """Gets a ``ConfigurationProxyManager``.

        :return: a ``ConfigurationBatchProxyManager``
        :rtype: ``osid.configuration.batch.ConfigurationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_batch()`` is ``true``.*

        """
        return  # osid.configuration.batch.ConfigurationBatchProxyManager

    configuration_batch_proxy_manager = property(fget=get_configuration_batch_proxy_manager)

    @abc.abstractmethod
    def get_configuration_rules_proxy_manager(self):
        """Gets a ``ConfigurationProxyManager``.

        :return: a ``ConfigurationRulesProxyManager``
        :rtype: ``osid.configuration.rules.ConfigurationRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_rules()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_configuration_rules()`` is ``true``.*

        """
        return  # osid.configuration.rules.ConfigurationRulesProxyManager

    configuration_rules_proxy_manager = property(fget=get_configuration_rules_proxy_manager)
