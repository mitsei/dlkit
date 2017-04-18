"""Implementations of mapping abstract base class searches."""
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


class LocationSearch:
    """The search interface for governing location searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_locations(self, location_ids):
        """Execute this search among the given list of locations.

        :param location_ids: list of locations
        :type location_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``location_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_location_results(self, location_search_order):
        """Specify an ordering to the search results.

        :param location_search_order: location search order
        :type location_search_order: ``osid.mapping.LocationSearchOrder``
        :raise: ``NullArgument`` -- ``location_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``location_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location_search_record(self, location_search_record_type):
        """Gets the record corresponding to the given location search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param location_search_record_type: a location search record type
        :type location_search_record_type: ``osid.type.Type``
        :return: the location search record
        :rtype: ``osid.mapping.records.LocationSearchRecord``
        :raise: ``NullArgument`` -- ``location_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.LocationSearchRecord


class LocationSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_locations(self):
        """Gets the location list resulting from a search.

        :return: the location list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationList

    locations = abc.abstractproperty(fget=get_locations)

    @abc.abstractmethod
    def get_location_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the location query inspector
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    location_query_inspector = abc.abstractproperty(fget=get_location_query_inspector)

    @abc.abstractmethod
    def get_location_search_results_record(self, location_search_record_type):
        """Gets the record corresponding to the given location search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param location_search_record_type: a location search record type
        :type location_search_record_type: ``osid.type.Type``
        :return: the location search results record
        :rtype: ``osid.mapping.records.LocationSearchResultsRecord``
        :raise: ``NullArgument`` -- ``location_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.LocationSearchResultsRecord


class MapSearch:
    """The search interface for governing map searches."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search_among_maps(self, map_ids):
        """Execute this search among the given list of maps.

        :param map_ids: list of maps
        :type map_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def order_map_results(self, map_search_order):
        """Specify an ordering to the search results.

        :param map_search_order: map search order
        :type map_search_order: ``osid.mapping.MapSearchOrder``
        :raise: ``NullArgument`` -- ``map_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``map_search_order`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_map_search_record(self, map_search_record_type):
        """Gets the map search record corresponding to the given map search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record interface along with all of its ancestor
        interfaces.

        :param map_search_record_type: a map search record type
        :type map_search_record_type: ``osid.type.Type``
        :return: the map search record
        :rtype: ``osid.mapping.records.MapSearchRecord``
        :raise: ``NullArgument`` -- ``map_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.MapSearchRecord


class MapSearchResults:
    """This interface provides a means to capture results of a search."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_maps(self):
        """Gets the map list resulting from a search.

        :return: the map list
        :rtype: ``osid.mapping.MapList``
        :raise: ``IllegalState`` -- list already retrieved

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapList

    maps = abc.abstractproperty(fget=get_maps)

    @abc.abstractmethod
    def get_map_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the map query inspector
        :rtype: ``osid.mapping.MapQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapQueryInspector

    map_query_inspector = abc.abstractproperty(fget=get_map_query_inspector)

    @abc.abstractmethod
    def get_map_search_results_record(self, map_search_record_type):
        """Gets the map search results record corresponding to the given map search record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record interface along with all of its ancestor
        interfaces.

        :param map_search_record_type: a map search record type
        :type map_search_record_type: ``osid.type.Type``
        :return: the map search results record
        :rtype: ``osid.mapping.records.MapSearchResultsRecord``
        :raise: ``NullArgument`` -- ``map_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_search_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.MapSearchResultsRecord
