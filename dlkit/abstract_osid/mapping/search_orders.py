"""Implementations of mapping abstract base class search_orders."""
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


class LocationSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def order_by_distance(self, style):
        """Orders the results by distance.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def get_location_search_order_record(self, location_record_type):
        """Gets the location search order record corresponding to the given location record ``Type``.

        Multiple retrievals return the same underlying object.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the location search order record
        :rtype: ``osid.mapping.records.LocationSearchOrderRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.LocationSearchOrderRecord


class MapSearchOrder:
    """An interface for specifying the ordering of search results."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_map_search_order_record(self, map_record_type):
        """Gets the map search order record corresponding to the given map ``Type``.

        Multiple retrievals return the same underlying object.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the map search order record
        :rtype: ``osid.mapping.records.MapSearchOrderRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.MapSearchOrderRecord
