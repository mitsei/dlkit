"""Implementations of mapping abstract base class managers."""
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


class MappingProfile:
    """The mapping profile describes the interoperability among mapping services."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def supports_visible_federation(self):
        """Tests if any map federation is exposed.

        Federation is exposed when a specific map may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of maps appears as a single
        map.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_lookup(self):
        """Tests if looking up locations is supported.

        :return: ``true`` if location lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_query(self):
        """Tests if querying locations is supported.

        :return: ``true`` if location query is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_search(self):
        """Tests if searching locations is supported.

        :return: ``true`` if location search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_admin(self):
        """Tests if locationadministrative service is supported.

        :return: ``true`` if location administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_notification(self):
        """Tests if a locationnotification service is supported.

        :return: ``true`` if location notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_hierarchy(self):
        """Tests if a locationhierarchy service is supported.

        :return: ``true`` if location hierarchy is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_hierarchy_design(self):
        """Tests if a location hierarchy design service is supported.

        :return: ``true`` if location hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_map(self):
        """Tests if a location map lookup service is supported.

        :return: ``true`` if a location map lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_map_assignment(self):
        """Tests if a location map assignment service is supported.

        :return: ``true`` if a location to map assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_smart_map(self):
        """Tests if a location smart map service is supported.

        :return: ``true`` if a location smart map service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_adjacency(self):
        """Tests if a location adjacency service is supported.

        :return: ``true`` if a location adjacency service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_location_spatial(self):
        """Tests if a location spatial service is supported.

        :return: ``true`` if a location spatial service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_location(self):
        """Tests if a resource location service is supported.

        :return: ``true`` if a resource location service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_location_update(self):
        """Tests if a resource location update service is supported.

        :return: ``true`` if a resource location update service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_location_notification(self):
        """Tests if a resource location notification service is supported.

        :return: ``true`` if a resource location notification service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_resource_position_notification(self):
        """Tests if a resource position notification service is supported.

        :return: ``true`` if a resource position notification service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_my_location(self):
        """Tests if a location service is supported for the current agent.

        :return: ``true`` if my location is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_lookup(self):
        """Tests if looking up maps is supported.

        :return: ``true`` if map lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_query(self):
        """Tests if querying maps is supported.

        :return: ``true`` if a map query service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_search(self):
        """Tests if searching maps is supported.

        :return: ``true`` if map search is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_admin(self):
        """Tests if map administrative service is supported.

        :return: ``true`` if map administration is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_notification(self):
        """Tests if a mapnotification service is supported.

        :return: ``true`` if map notification is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_hierarchy(self):
        """Tests for the availability of a map hierarchy traversal service.

        :return: ``true`` if map hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented in all
        providers.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_map_hierarchy_design(self):
        """Tests for the availability of a map hierarchy design service.

        :return: ``true`` if map hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_mapping_batch(self):
        """Tests if the mapping batch service is supported.

        :return: ``true`` if maping batch service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_mapping_path(self):
        """Tests if the mapping path service is supported.

        :return: ``true`` if maping path service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def supports_mapping_route(self):
        """Tests if the mapping route service is supported.

        :return: ``true`` if maping route service is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_record_types(self):
        """Gets the supported ``Location`` record types.

        :return: a list containing the supported ``Location`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    location_record_types = abc.abstractproperty(fget=get_location_record_types)

    @abc.abstractmethod
    def supports_location_record_type(self, location_record_type):
        """Tests if the given ``Location`` record type is supported.

        :param location_record_type: a ``Type`` indicating a ``Location`` record type
        :type location_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_search_record_types(self):
        """Gets the supported ``Location`` search types.

        :return: a list containing the supported ``Location`` search types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    location_search_record_types = abc.abstractproperty(fget=get_location_search_record_types)

    @abc.abstractmethod
    def supports_location_search_record_type(self, location_search_record_type):
        """Tests if the given ``Location`` search type is supported.

        :param location_search_record_type: a ``Type`` indicating a ``Location`` search type
        :type location_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``location_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_record_types(self):
        """Gets the supported ``Map`` record types.

        :return: a list containing the supported ``Map`` types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    map_record_types = abc.abstractproperty(fget=get_map_record_types)

    @abc.abstractmethod
    def supports_map_record_type(self, map_record_type):
        """Tests if the given ``Map`` record type is supported.

        :param map_record_type: a ``Type`` indicating a ``Map`` record type
        :type map_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_search_record_types(self):
        """Gets the supported ``Map`` search record types.

        :return: a list containing the supported ``Map`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    map_search_record_types = abc.abstractproperty(fget=get_map_search_record_types)

    @abc.abstractmethod
    def supports_map_search_record_type(self, map_search_record_type):
        """Tests if the given ``Map`` search record type is supported.

        :param map_search_record_type: a ``Type`` indicating a ``Map`` search record type
        :type map_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_search_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_resource_location_record_types(self):
        """Gets the supported ``ResourceLocation`` record types.

        :return: a list containing the supported ``ResourceLocation`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    resource_location_record_types = abc.abstractproperty(fget=get_resource_location_record_types)

    @abc.abstractmethod
    def supports_resource_location_record_type(self, resource_location_record_type):
        """Tests if the given ``ResourceLocationRecord`` record type is supported.

        :param resource_location_record_type: a ``Type`` indicating a ``ResourceLocation`` type
        :type resource_location_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_location_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_coordinate_types(self):
        """Gets the supported ``Coordinate`` types.

        :return: a list containing the supported ``Coordinate`` types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    coordinate_types = abc.abstractproperty(fget=get_coordinate_types)

    @abc.abstractmethod
    def supports_coordinate_type(self, coordinate_type):
        """Tests if the given ``Coordinate`` type is supported.

        :param coordinate_type: a ``Type`` indicating a ``Coordinate`` type
        :type coordinate_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_heading_types(self):
        """Gets the supported ``Heading`` types.

        :return: a list containing the supported ``Heading`` types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    heading_types = abc.abstractproperty(fget=get_heading_types)

    @abc.abstractmethod
    def supports_heading_type(self, heading_type):
        """Tests if the given ``Heading`` type is supported.

        :param heading_type: a ``Type`` indicating a ``Heading`` type
        :type heading_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_spatial_unit_record_types(self):
        """Gets the supported ``SpatialUnit`` record types.

        :return: a list containing the supported ``SpatialUnit`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.type.TypeList

    spatial_unit_record_types = abc.abstractproperty(fget=get_spatial_unit_record_types)

    @abc.abstractmethod
    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if the given ``SpatialUnit`` record type is supported.

        :param spatial_unit_record_type: a ``Type`` indicating a ``SpatialUnit`` record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean


class MappingManager:
    """The mapping manager provides access to mapping sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``LocationLookupSession:`` a session to retrieve locations
      * ``LocationQuerySession:`` a session to query for locations
      * ``LocationSearchSession:`` a session to search for locations
      * ``LocationAdminSession:`` a session to create and delete
        locations
      * ``LocationNotificationSession:`` a session to receive
        notifications pertaining to location changes
      * ``LocationHierarchySession:`` a session to examine locations in
        a hierarchy
      * ``LocationHierarchyAssignmentSession:`` a session to traverse
        the location hierarchy
      * ``LocationMapSession:`` a session to look up location to map
        mappings
      * ``LocationMapAssignmentSession:`` a session to manage location
        to map mappings
      * ``LocationSmartMapSession:`` a session to manage dynamic maps of
        locations

      * ``LocationAdjacencySession:`` a session to query neighboring
        locations
      * ``LocationSpatialSession:`` a session to lookup locations
        spatially
      * ``ResourceLocationSession:`` a session query resources at
        locations
      * ``ResourceLocationUpdateSession:`` a session to assign resources
        to locations
      * ``ResourceLocationNotificationSession:`` a session to subscribe
        to notifications when resources move among locations
      * ``ResourcePositionNotificationSession:`` a session to subscribe
        to notifications when resources change positions
      * ``MyLocationSession:`` a session to query locations for the user
        agent

      * ``MapLookupSession:`` a session to retrieve maps
      * ``MapQuerySession:`` a session to search for maps
      * ``MapSearchSession:`` a session to search for maps
      * ``MapAdminSession:`` a session to create and delete maps
      * ``MapNotificationSession:`` a session to receive notifications
        pertaining to map changes
      * ``MapHierarchySession:`` a session to traverse a hierarchy of
        map
      * ``MapHierarchyDesignSession:`` a session to manage a map
        hierarchy


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_location_lookup_session(self):
        """Gets the ``OsidSession`` associated with the location lookup service.

        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_lookup()`` is ``true``.*

        """
        return  # osid.mapping.LocationLookupSession

    location_lookup_session = abc.abstractproperty(fget=get_location_lookup_session)

    @abc.abstractmethod
    def get_location_lookup_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location lookup service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationLookupSession

    @abc.abstractmethod
    def get_location_query_session(self):
        """Gets the ``OsidSession`` associated with the location query service.

        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` is ``true``.*

        """
        return  # osid.mapping.LocationQuerySession

    location_query_session = abc.abstractproperty(fget=get_location_query_session)

    @abc.abstractmethod
    def get_location_query_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location query service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationQuerySession

    @abc.abstractmethod
    def get_location_search_session(self):
        """Gets the ``OsidSession`` associated with the location search service.

        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search()`` is ``true``.*

        """
        return  # osid.mapping.LocationSearchSession

    location_search_session = abc.abstractproperty(fget=get_location_search_session)

    @abc.abstractmethod
    def get_location_search_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location search service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationSearchSession

    @abc.abstractmethod
    def get_location_admin_session(self):
        """Gets the ``OsidSession`` associated with the location administration service.

        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_admin()`` is ``true``.*

        """
        return  # osid.mapping.LocationAdminSession

    location_admin_session = abc.abstractproperty(fget=get_location_admin_session)

    @abc.abstractmethod
    def get_location_admin_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location administration service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationAdminSession

    @abc.abstractmethod
    def get_location_notification_session(self, location_receiver):
        """Gets the ``OsidSession`` associated with the location notification service.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NullArgument`` -- ``location_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_notification()`` is ``true``.*

        """
        return  # osid.mapping.LocationNotificationSession

    @abc.abstractmethod
    def get_location_notification_session_for_map(self, location_receiver, map_id):
        """Gets the ``OsidSession`` associated with the location notification service for the given map.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``location_receiver`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationNotificationSession

    @abc.abstractmethod
    def get_location_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the location hierarchy service.

        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy()`` is ``true``.*

        """
        return  # osid.mapping.LocationHierarchySession

    location_hierarchy_session = abc.abstractproperty(fget=get_location_hierarchy_session)

    @abc.abstractmethod
    def get_location_hierarchy_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location hierarchy service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationHierarchySession

    @abc.abstractmethod
    def get_location_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the location hierarchy design service.

        :return: a ``LocationHierarchyDesignSession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy_design()`` is ``true``.*

        """
        return  # osid.mapping.LocationHierarchyDesignSession

    location_hierarchy_design_session = abc.abstractproperty(fget=get_location_hierarchy_design_session)

    @abc.abstractmethod
    def get_location_hierarchy_design_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location hierarchy design service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationHierarchyDesignSession

    @abc.abstractmethod
    def get_location_map_session(self):
        """Gets the ``OsidSession`` to lookup location/map mappings.

        :return: a ``LocationMapSession``
        :rtype: ``osid.mapping.LocationMapSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_map()`` is ``true``.*

        """
        return  # osid.mapping.LocationMapSession

    location_map_session = abc.abstractproperty(fget=get_location_map_session)

    @abc.abstractmethod
    def get_location_map_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning locations to maps.

        :return: a ``LocationMapAssignmentSession``
        :rtype: ``osid.mapping.LocationMapAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_map_assignment()`` is ``true``.*

        """
        return  # osid.mapping.LocationMapAssignmentSession

    location_map_assignment_session = abc.abstractproperty(fget=get_location_map_assignment_session)

    @abc.abstractmethod
    def get_location_smart_map_session(self, map_id):
        """Gets the ``OsidSession`` to manage locatin smart maps.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationSmartMapSession``
        :rtype: ``osid.mapping.LocationSmartMapSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_smart_map()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_smart_map()`` is ``true``.*

        """
        return  # osid.mapping.LocationSmartMapSession

    @abc.abstractmethod
    def get_location_adjacency_session(self):
        """Gets the ``OsidSession`` associated with the location adjacency service.

        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_adjacency()`` is ``true``.*

        """
        return  # osid.mapping.LocationAdjacencySession

    location_adjacency_session = abc.abstractproperty(fget=get_location_adjacency_session)

    @abc.abstractmethod
    def get_location_adjacency_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location adjacency service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_adjacency()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationAdjacencySession

    @abc.abstractmethod
    def get_location_spatial_session(self):
        """Gets the ``OsidSession`` associated with the location spatial service.

        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_spatial()`` is ``true``.*

        """
        return  # osid.mapping.LocationSpatialSession

    location_spatial_session = abc.abstractproperty(fget=get_location_spatial_session)

    @abc.abstractmethod
    def get_location_spatial_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location spatial service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_spatial()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationSpatialSession

    @abc.abstractmethod
    def get_resource_location_session(self):
        """Gets the ``OsidSession`` associated with the resource location service.

        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationSession

    resource_location_session = abc.abstractproperty(fget=get_resource_location_session)

    @abc.abstractmethod
    def get_resource_location_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the resource location service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourceLocationSession

    @abc.abstractmethod
    def get_resource_location_update_session(self):
        """Gets the ``OsidSession`` associated with the resource location update service.

        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_update()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationUpdateSession

    resource_location_update_session = abc.abstractproperty(fget=get_resource_location_update_session)

    @abc.abstractmethod
    def get_resource_location_update_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the resource location update service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_update()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourceLocationUpdateSession

    @abc.abstractmethod
    def get_resource_location_notification_session(self, resource_location_receiver):
        """Gets the ``OsidSession`` associated with the resource location notification service.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NullArgument`` -- ``resource_location_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_notification()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationNotificationSession

    @abc.abstractmethod
    def get_resource_location_notification_session_for_map(self, resource_location_receiver, map_id):
        """Gets the ``OsidSession`` associated with the resource location notification service for the given map.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_location_receiver`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourceLocationNotificationSession

    @abc.abstractmethod
    def get_resource_position_notification_session(self, resource_position_receiver):
        """Gets the ``OsidSession`` associated with the resource position notification service.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourcePositionNotificationSession``
        :raise: ``NullArgument`` -- ``resource_position_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_position_notification()`` is ``true``.*

        """
        return  # osid.mapping.ResourcePositionNotificationSession

    @abc.abstractmethod
    def get_resource_position_notification_session_for_map(self, resource_position_receiver, map_id):
        """Gets the ``OsidSession`` associated with the resource position notification service for the given map.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourcePositionNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_position_receiver`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_position_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourcePositionNotificationSession

    @abc.abstractmethod
    def get_my_location_session(self):
        """Gets the ``OsidSession`` associated with the my location service.

        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_location_lookup()`` is ``true``.*

        """
        return  # osid.mapping.MyLocationSession

    my_location_session = abc.abstractproperty(fget=get_my_location_session)

    @abc.abstractmethod
    def get_my_location_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the my location service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_location_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.MyLocationSession

    @abc.abstractmethod
    def get_map_lookup_session(self):
        """Gets the ``OsidSession`` associated with the map lookup service.

        :return: a ``MapLookupSession``
        :rtype: ``osid.mapping.MapLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_lookup()`` is ``true``.*

        """
        return  # osid.mapping.MapLookupSession

    map_lookup_session = abc.abstractproperty(fget=get_map_lookup_session)

    @abc.abstractmethod
    def get_map_query_session(self):
        """Gets the ``OsidSession`` associated with the map query service.

        :return: a ``MapQuerySession``
        :rtype: ``osid.mapping.MapQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_query()`` is ``true``.*

        """
        return  # osid.mapping.MapQuerySession

    map_query_session = abc.abstractproperty(fget=get_map_query_session)

    @abc.abstractmethod
    def get_map_search_session(self):
        """Gets the ``OsidSession`` associated with the map search service.

        :return: a ``MapSearchSession``
        :rtype: ``osid.mapping.MapSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_search()`` is ``true``.*

        """
        return  # osid.mapping.MapSearchSession

    map_search_session = abc.abstractproperty(fget=get_map_search_session)

    @abc.abstractmethod
    def get_map_admin_session(self):
        """Gets the ``OsidSession`` associated with the map administrative service.

        :return: a ``MapAdminSession``
        :rtype: ``osid.mapping.MapAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_admin()`` is ``true``.*

        """
        return  # osid.mapping.MapAdminSession

    map_admin_session = abc.abstractproperty(fget=get_map_admin_session)

    @abc.abstractmethod
    def get_map_notification_session(self, map_receiver):
        """Gets the ``OsidSession`` associated with the map notification service.

        :param map_receiver: the notification callback
        :type map_receiver: ``osid.mapping.MapReceiver``
        :return: a ``MapNotificationSession``
        :rtype: ``osid.mapping.MapNotificationSession``
        :raise: ``NullArgument`` -- ``map_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_notification()`` is ``true``.*

        """
        return  # osid.mapping.MapNotificationSession

    @abc.abstractmethod
    def get_map_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the map hierarchy service.

        :return: a ``MapHierarchySession`` for maps
        :rtype: ``osid.mapping.MapHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_hierarchy()`` is ``true``.*

        """
        return  # osid.mapping.MapHierarchySession

    map_hierarchy_session = abc.abstractproperty(fget=get_map_hierarchy_session)

    @abc.abstractmethod
    def get_map_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the map hierarchy design service.

        :return: a ``HierarchyDesignSession`` for maps
        :rtype: ``osid.mapping.MapHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_hierarchy_design()`` is ``true``.*

        """
        return  # osid.mapping.MapHierarchyDesignSession

    map_hierarchy_design_session = abc.abstractproperty(fget=get_map_hierarchy_design_session)

    @abc.abstractmethod
    def get_mapping_batch_manager(self):
        """Gets the mapping batch manager.

        :return: a ``MappingBatchManager`` for paths
        :rtype: ``osid.mapping.batch.MappingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_mapping_batch()`` is ``true``.*

        """
        return  # osid.mapping.batch.MappingBatchManager

    mapping_batch_manager = abc.abstractproperty(fget=get_mapping_batch_manager)

    @abc.abstractmethod
    def get_mapping_path_manager(self):
        """Gets the mapping path manager.

        :return: a ``MappingPathManager`` for paths
        :rtype: ``osid.mapping.path.MappingPathManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_path()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_mapping_path()`` is ``true``.*

        """
        return  # osid.mapping.path.MappingPathManager

    mapping_path_manager = abc.abstractproperty(fget=get_mapping_path_manager)

    @abc.abstractmethod
    def get_mapping_route_manager(self):
        """Gets the mapping route manager.

        :return: a ``MappingRouteManager`` for routes
        :rtype: ``osid.mapping.route.MappingRouteManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_route()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_mapping_route()`` is ``true``.*

        """
        return  # osid.mapping.route.MappingRouteManager

    mapping_route_manager = abc.abstractproperty(fget=get_mapping_route_manager)


class MappingProxyManager:
    """The mapping proxy manager provides access to mapping sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager pass a ``Proxy`` for passing information
    from server environments. The sessions included in this manager are:

      * ``LocationLookupSession:`` a session to retrieve locations
      * ``LocationQuerySession:`` a session to query for locations
      * ``LocationSearchSession:`` a session to search for locations
      * ``LocationAdminSession:`` a session to create and delete
        locations
      * ``LocationNotificationSession:`` a session to receive
        notifications pertaining to location changes
      * ``LocationHierarchySession:`` a session to examine locations in
        a hierarchy
      * ``LocationHierarchyAssignmentSession:`` a session to traverse
        the location hierarchy
      * ``LocationMapSession:`` a session to lookup location to map
        mappings
      * ``LocationMapAssignmentSession:`` a session to manage location
        to map mappings
      * ``LocationSmartMapSession:`` a session to manage dynamic maps of
        locations

      * ``LocationAdjacencySession:`` a session to query neighboring
        locations
      * ``LocationSpatialSession:`` a session to lookup locations
        spatially
      * ``ResourceLocationSession:`` a session query resources at
        locations
      * ``ResourceLocationUpdateSession:`` a session to assign resources
        to locations
      * ``ResourceLocationNotificationSession:`` a session to subscribe
        to notifications when resources move among locations
      * ``ResourcePositionNotificationSession:`` a session to subscribe
        to notifications when resources change positions
      * ``MyLocationSession:`` a session to query locations for the user
        agent

      * ``MapLookupSession:`` a session to retrieve maps
      * ``MapQuerySession:`` a session to search for maps
      * ``MapSearchSession:`` a session to search for maps
      * ``MapAdminSession:`` a session to create and delete maps
      * ``MapNotificationSession:`` a session to receive notifications
        pertaining to map changes
      * ``MapHierarchySession:`` a session to traverse a hierarchy of
        map
      * ``MapHierarchyDesignSession:`` a session to manage a map
        hierarchy


    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_location_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_lookup()`` is ``true``.*

        """
        return  # osid.mapping.LocationLookupSession

    @abc.abstractmethod
    def get_location_lookup_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location lookup service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationLookupSession

    @abc.abstractmethod
    def get_location_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` is ``true``.*

        """
        return  # osid.mapping.LocationQuerySession

    @abc.abstractmethod
    def get_location_query_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location query service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationQuerySession

    @abc.abstractmethod
    def get_location_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search()`` is ``true``.*

        """
        return  # osid.mapping.LocationSearchSession

    @abc.abstractmethod
    def get_location_search_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location search service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_search()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationSearchSession

    @abc.abstractmethod
    def get_location_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_admin()`` is ``true``.*

        """
        return  # osid.mapping.LocationAdminSession

    @abc.abstractmethod
    def get_location_admin_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location administration service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_admin()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationAdminSession

    @abc.abstractmethod
    def get_location_notification_session(self, location_receiver, proxy):
        """Gets the ``OsidSession`` associated with the location notification service.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NullArgument`` -- ``location_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_notification()`` is ``true``.*

        """
        return  # osid.mapping.LocationNotificationSession

    @abc.abstractmethod
    def get_location_notification_session_for_map(self, location_receiver, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location notification service for the given map.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``location_receiver, map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationNotificationSession

    @abc.abstractmethod
    def get_location_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy()`` is ``true``.*

        """
        return  # osid.mapping.LocationHierarchySession

    @abc.abstractmethod
    def get_location_hierarchy_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationHierarchySession

    @abc.abstractmethod
    def get_location_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchyDesignSession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy_design()`` is ``true``.*

        """
        return  # osid.mapping.LocationHierarchyDesignSession

    @abc.abstractmethod
    def get_location_hierarchy_design_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy design service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_hierarchy_design()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationHierarchyDesignSession

    @abc.abstractmethod
    def get_location_map_session(self, proxy):
        """Gets the ``OsidSession`` to lookup location/map mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationMapSession``
        :rtype: ``osid.mapping.LocationMapSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_map()`` is ``true``.*

        """
        return  # osid.mapping.LocationMapSession

    @abc.abstractmethod
    def get_location_map_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning locations to maps.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationMapAssignmentSession``
        :rtype: ``osid.mapping.LocationMapAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map_assignment()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_map_assignment()`` is ``true``.*

        """
        return  # osid.mapping.LocationMapAssignmentSession

    @abc.abstractmethod
    def get_location_smart_map_session(self, map_id, proxy):
        """Gets the ``OsidSession`` to manage location smart maps.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSmartMapSession``
        :rtype: ``osid.mapping.LocationSmartMapSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_smart_map()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_smart_map()`` is ``true``.*

        """
        return  # osid.mapping.LocationSmartMapSession

    @abc.abstractmethod
    def get_location_adjacency_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location adjacency service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_adjacency()`` is ``true``.*

        """
        return  # osid.mapping.LocationAdjacencySession

    @abc.abstractmethod
    def get_location_adjacency_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location adjacency service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_adjacency()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationAdjacencySession

    @abc.abstractmethod
    def get_location_spatial_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location spatial service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_spatial()`` is ``true``.*

        """
        return  # osid.mapping.LocationSpatialSession

    @abc.abstractmethod
    def get_location_spatial_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location spatial service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_spatial()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.LocationSpatialSession

    @abc.abstractmethod
    def get_resource_location_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource location service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationSession

    @abc.abstractmethod
    def get_resource_location_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource location service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourceLocationSession

    @abc.abstractmethod
    def get_resource_location_update_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource location update service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_update()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationUpdateSession

    @abc.abstractmethod
    def get_resource_location_update_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource location update service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_update()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourceLocationUpdateSession

    @abc.abstractmethod
    def get_resource_location_notification_session(self, resource_location_receiver, proxy):
        """Gets the ``OsidSession`` associated with the resource location notification service.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NullArgument`` -- ``resource_location_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_notification()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationNotificationSession

    @abc.abstractmethod
    def get_resource_location_notification_session_for_map(self, resource_location_receiver, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource location notification service for the given map.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_location_receiver, map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_location_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourceLocationNotificationSession

    @abc.abstractmethod
    def get_resource_position_notification_session(self, resource_position_receiver, proxy):
        """Gets the ``OsidSession`` associated with the resource position notification service.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NullArgument`` -- ``resource_position_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_position_notification()`` is ``true``.*

        """
        return  # osid.mapping.ResourceLocationNotificationSession

    @abc.abstractmethod
    def get_resource_position_notification_session_for_map(self, resource_position_receiver, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource position notification service for the given map.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourcePositionNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_position_receiver, map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_resource_position_notification()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.ResourcePositionNotificationSession

    @abc.abstractmethod
    def get_my_location_session(self, proxy):
        """Gets the ``OsidSession`` associated with the my location service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_location_lookup()`` is ``true``.*

        """
        return  # osid.mapping.MyLocationSession

    @abc.abstractmethod
    def get_my_location_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the my location service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_my_location_lookup()`` and
        ``supports_visible_federation()`` are ``true``*

        """
        return  # osid.mapping.MyLocationSession

    @abc.abstractmethod
    def get_map_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapLookupSession``
        :rtype: ``osid.mapping.MapLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_lookup()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_lookup()`` is ``true``.*

        """
        return  # osid.mapping.MapLookupSession

    @abc.abstractmethod
    def get_map_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapQuerySession``
        :rtype: ``osid.mapping.MapQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_query()`` is ``true``.*

        """
        return  # osid.mapping.MapQuerySession

    @abc.abstractmethod
    def get_map_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapSearchSession``
        :rtype: ``osid.mapping.MapSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_search()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_search()`` is ``true``.*

        """
        return  # osid.mapping.MapSearchSession

    @abc.abstractmethod
    def get_map_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapAdminSession``
        :rtype: ``osid.mapping.MapAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_admin()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_admin()`` is ``true``.*

        """
        return  # osid.mapping.MapAdminSession

    @abc.abstractmethod
    def get_map_notification_session(self, map_receiver, proxy):
        """Gets the ``OsidSession`` associated with the map notification service.

        :param map_receiver: the notification callback
        :type map_receiver: ``osid.mapping.MapReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapNotificationSession``
        :rtype: ``osid.mapping.MapNotificationSession``
        :raise: ``NullArgument`` -- ``map_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_notification()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_notification()`` is ``true``.*

        """
        return  # osid.mapping.MapNotificationSession

    @abc.abstractmethod
    def get_map_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapHierarchySession`` for maps
        :rtype: ``osid.mapping.MapHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_hierarchy()`` is ``true``.*

        """
        return  # osid.mapping.MapHierarchySession

    @abc.abstractmethod
    def get_map_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for maps
        :rtype: ``osid.mapping.MapHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy_design()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_hierarchy_design()`` is ``true``.*

        """
        return  # osid.mapping.MapHierarchyDesignSession

    @abc.abstractmethod
    def get_mapping_batch_proxy_manager(self):
        """Gets the mapping batch manager.

        :return: a ``MappingBatchProxyManager`` for paths
        :rtype: ``osid.mapping.batch.MappingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_mapping_batch()`` is ``true``.*

        """
        return  # osid.mapping.batch.MappingBatchProxyManager

    mapping_batch_proxy_manager = abc.abstractproperty(fget=get_mapping_batch_proxy_manager)

    @abc.abstractmethod
    def get_mapping_path_proxy_manager(self):
        """Gets the mapping path manager.

        :return: a ``MappingPathProxyManager`` for paths
        :rtype: ``osid.mapping.path.MappingPathProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_path()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_mapping_path()`` is ``true``.*

        """
        return  # osid.mapping.path.MappingPathProxyManager

    mapping_path_proxy_manager = abc.abstractproperty(fget=get_mapping_path_proxy_manager)

    @abc.abstractmethod
    def get_mapping_route_proxy_manager(self):
        """Gets the mapping route manager.

        :return: a ``MappingRouteProxyManager`` for routes
        :rtype: ``osid.mapping.route.MappingRouteProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_route()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_mapping_route()`` is ``true``.*

        """
        return  # osid.mapping.route.MappingRouteProxyManager

    mapping_route_proxy_manager = abc.abstractproperty(fget=get_mapping_route_proxy_manager)
