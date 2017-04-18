"""Implementations of mapping abstract base class queries."""
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


class LocationQuery:
    """This is the query for searching locations.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_coordinate(self, coordinate, match):
        """Matches locations at the specified ``Coordinate``.

        :param coordinate: a coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def match_any_coordinate(self, match):
        """Matches locations that have any coordinate assignment.

        :param match: ``true`` to match locations with any coordinate, ``false`` to match locations with no coordinates
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_coordinate_terms(self):
        """Clears the coordinate query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    coordinate_terms = abc.abstractproperty(fdel=clear_coordinate_terms)

    @abc.abstractmethod
    def match_contained_spatial_unit(self, spatial_unit, match):
        """Matches locations containing the specified ``SpatialUnit``.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_contained_spatial_unit_terms(self):
        """Clears the spatial unit terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    contained_spatial_unit_terms = abc.abstractproperty(fdel=clear_contained_spatial_unit_terms)

    @abc.abstractmethod
    def match_overlapping_spatial_unit(self, spatial_unit, match):
        """Matches locations overlapping with the specified ``SpatialUnit``.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_overlapping_spatial_unit_terms(self):
        """Clears the overlapping spatial unit terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    overlapping_spatial_unit_terms = abc.abstractproperty(fdel=clear_overlapping_spatial_unit_terms)

    @abc.abstractmethod
    def match_any_spatial_unit(self, match):
        """Matches locations that have any spatial unit assignment.

        :param match: ``true`` to match locations with any boundary, ``false`` to match locations with no boundaries
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_spatial_unit_terms(self):
        """Clears the spatial unit query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    spatial_unit_terms = abc.abstractproperty(fdel=clear_spatial_unit_terms)

    @abc.abstractmethod
    def match_route_id(self, route_id, match):
        """Sets the route ``Id`` for this query to match locations along the given route.

        :param route_id: the route ``Id``
        :type route_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``route_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_route_id_terms(self):
        """Clears the route ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    route_id_terms = abc.abstractproperty(fdel=clear_route_id_terms)

    @abc.abstractmethod
    def supports_route_query(self):
        """Tests if a ``RouteQuery`` is available.

        :return: ``true`` if a route query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_route_query(self):
        """Gets the query for a route.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the route query
        :rtype: ``osid.mapping.route.RouteQuery``
        :raise: ``Unimplemented`` -- ``supports_route_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_route_query()`` is ``true``.*

        """
        return  # osid.mapping.route.RouteQuery

    route_query = abc.abstractproperty(fget=get_route_query)

    @abc.abstractmethod
    def match_any_route(self, match):
        """Matches locations that are used on any route.

        :param match: ``true`` to match locations on any route, ``false`` to match locations on no routes
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_route_terms(self):
        """Clears the route query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    route_terms = abc.abstractproperty(fdel=clear_route_terms)

    @abc.abstractmethod
    def match_path_id(self, path_id, match):
        """Sets the path ``Id`` for this query to match locations along the given path.

        :param path_id: the path ``Id``
        :type path_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``path_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_path_id_terms(self):
        """Clears the path ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    path_id_terms = abc.abstractproperty(fdel=clear_path_id_terms)

    @abc.abstractmethod
    def supports_path_query(self):
        """Tests if a ``PathQuery`` is available.

        :return: ``true`` if a path query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_path_query(self):
        """Gets the query for a path.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the path query
        :rtype: ``osid.mapping.path.PathQuery``
        :raise: ``Unimplemented`` -- ``supports_path_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_path_query()`` is ``true``.*

        """
        return  # osid.mapping.path.PathQuery

    path_query = abc.abstractproperty(fget=get_path_query)

    @abc.abstractmethod
    def match_any_path(self, match):
        """Matches locations that exist along any path.

        :param match: ``true`` to match locations on any path, ``false`` to match locations on no path
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_path_terms(self):
        """Clears the path query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    path_terms = abc.abstractproperty(fdel=clear_path_terms)

    @abc.abstractmethod
    def match_containing_location_id(self, location_id, match):
        """Sets the location ``Id`` for this query to match locations contained within the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_containing_location_id_terms(self):
        """Clears the pcontaining location ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_location_id_terms = abc.abstractproperty(fdel=clear_containing_location_id_terms)

    @abc.abstractmethod
    def supports_containing_location_query(self):
        """Tests if a ``LocationQuery`` is available.

        :return: ``true`` if a location query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_containing_location_query(self):
        """Gets the query for a parent location.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``Unimplemented`` -- ``supports_containing_location_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_containing_location_query()`` is ``true``.*

        """
        return  # osid.mapping.LocationQuery

    containing_location_query = abc.abstractproperty(fget=get_containing_location_query)

    @abc.abstractmethod
    def match_any_containing_location(self, match):
        """Matches locations that have any ancestor.

        :param match: ``true`` to match locations with any parent location, ``false`` to match root locations
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_containing_location_terms(self):
        """Clears the containing location query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    containing_location_terms = abc.abstractproperty(fdel=clear_containing_location_terms)

    @abc.abstractmethod
    def match_contained_location_id(self, location_id, match):
        """Sets the location ``Id`` for this query to match locations containing the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_contained_location_id_terms(self):
        """Clears the contained location ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    contained_location_id_terms = abc.abstractproperty(fdel=clear_contained_location_id_terms)

    @abc.abstractmethod
    def supports_contained_location_query(self):
        """Tests if a ``LocationQuery`` is available.

        :return: ``true`` if a location query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_contained_location_query(self):
        """Gets the query for a contained location.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``Unimplemented`` -- ``supports_contained_location_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_contained_location_query()`` is ``true``.*

        """
        return  # osid.mapping.LocationQuery

    contained_location_query = abc.abstractproperty(fget=get_contained_location_query)

    @abc.abstractmethod
    def match_any_contained_location(self, match):
        """Matches locations that have any children.

        :param match: ``true`` to match locations containing any other location, ``false`` to match empty locations
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_contained_location_terms(self):
        """Clears the contained location query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    contained_location_terms = abc.abstractproperty(fdel=clear_contained_location_terms)

    @abc.abstractmethod
    def match_map_id(self, map_id, match):
        """Sets the map ``Id`` for this query.

        :param map_id: the map ``Id``
        :type map_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_map_id_terms(self):
        """Clears the map ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    map_id_terms = abc.abstractproperty(fdel=clear_map_id_terms)

    @abc.abstractmethod
    def supports_map_query(self):
        """Tests if a ``MapQuery`` is available.

        :return: ``true`` if a map query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_map_query(self):
        """Gets the query for a map.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``
        :raise: ``Unimplemented`` -- ``supports_map_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_map_query()`` is ``true``.*

        """
        return  # osid.mapping.MapQuery

    map_query = abc.abstractproperty(fget=get_map_query)

    @abc.abstractmethod
    def clear_map_terms(self):
        """Clears the map query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    map_terms = abc.abstractproperty(fdel=clear_map_terms)

    @abc.abstractmethod
    def get_location_query_record(self, location_record_type):
        """Gets the location query record corresponding to the given ``Location`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the location query record
        :rtype: ``osid.mapping.records.LocationQueryRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.LocationQueryRecord


class MapQuery:
    """This is the query for searching maps.

    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match_location_id(self, location_id, match):
        """Sets the location ``Id`` for this query to match maps that have a related location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param match: ``true`` if a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_location_id_terms(self):
        """Clears the location ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    location_id_terms = abc.abstractproperty(fdel=clear_location_id_terms)

    @abc.abstractmethod
    def supports_location_query(self):
        """Tests if a ``LocationQuery`` is available.

        :return: ``true`` if a location query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_location_query(self):
        """Gets the query for a location.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_location_query()`` is ``true``.*

        """
        return  # osid.mapping.LocationQuery

    location_query = abc.abstractproperty(fget=get_location_query)

    @abc.abstractmethod
    def match_any_location(self, match):
        """Matches maps that have any location.

        :param match: ``true`` to match maps with any location, ``false`` to match maps with no location
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_location_terms(self):
        """Clears the location query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    location_terms = abc.abstractproperty(fdel=clear_location_terms)

    @abc.abstractmethod
    def match_path_id(self, path_id, match):
        """Sets the path ``Id`` for this query to match maps containing paths.

        :param path_id: the path ``Id``
        :type path_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``path_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_path_id_terms(self):
        """Clears the path ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    path_id_terms = abc.abstractproperty(fdel=clear_path_id_terms)

    @abc.abstractmethod
    def supports_path_query(self):
        """Tests if a ``PathQuery`` is available.

        :return: ``true`` if a path query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_path_query(self):
        """Gets the query for a path.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the path query
        :rtype: ``osid.mapping.path.PathQuery``
        :raise: ``Unimplemented`` -- ``supports_path_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_path_query()`` is ``true``.*

        """
        return  # osid.mapping.path.PathQuery

    path_query = abc.abstractproperty(fget=get_path_query)

    @abc.abstractmethod
    def match_any_path(self, match):
        """Matches maps that have any path.

        :param match: ``true`` to match maps with any path, ``false`` to match maps with no path
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_path_terms(self):
        """Clears the path query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    path_terms = abc.abstractproperty(fdel=clear_path_terms)

    @abc.abstractmethod
    def match_route_id(self, path_id, match):
        """Sets the path ``Id`` for this query to match maps containing paths.

        :param path_id: the path ``Id``
        :type path_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``path_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_route_id_terms(self):
        """Clears the route ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    route_id_terms = abc.abstractproperty(fdel=clear_route_id_terms)

    @abc.abstractmethod
    def supports_route_query(self):
        """Tests if a ``RouteQuery`` is available.

        :return: ``true`` if a route query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_route_query(self):
        """Gets the query for a route.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the route query
        :rtype: ``osid.mapping.route.RouteQuery``
        :raise: ``Unimplemented`` -- ``supports_route_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_route_query()`` is ``true``.*

        """
        return  # osid.mapping.route.RouteQuery

    route_query = abc.abstractproperty(fget=get_route_query)

    @abc.abstractmethod
    def match_any_route(self, match):
        """Matches maps that have any route.

        :param match: ``true`` to match maps with any route, ``false`` to match maps with no route
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_route_terms(self):
        """Clears the route query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    route_terms = abc.abstractproperty(fdel=clear_route_terms)

    @abc.abstractmethod
    def match_ancestor_map_id(self, map_id, match):
        """Sets the map ``Id`` for this query to match maps that have the specified map as an ancestor.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_map_id_terms(self):
        """Clears the ancestor map ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_map_id_terms = abc.abstractproperty(fdel=clear_ancestor_map_id_terms)

    @abc.abstractmethod
    def supports_ancestor_map_query(self):
        """Tests if a ``MapQuery`` is available.

        :return: ``true`` if a map query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_ancestor_map_query(self):
        """Gets the query for a map.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_map_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_map_query()`` is ``true``.*

        """
        return  # osid.mapping.MapQuery

    ancestor_map_query = abc.abstractproperty(fget=get_ancestor_map_query)

    @abc.abstractmethod
    def match_any_ancestor_map(self, match):
        """Matches maps with any ancestor.

        :param match: ``true`` to match maps with any ancestor, ``false`` to match root maps
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_ancestor_map_terms(self):
        """Clears the ancestor map query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_map_terms = abc.abstractproperty(fdel=clear_ancestor_map_terms)

    @abc.abstractmethod
    def match_descendant_map_id(self, map_id, match):
        """Sets the map ``Id`` for this query to match maps that have the specified map as a descendant.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_map_id_terms(self):
        """Clears the descendant map ``Id`` query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_map_id_terms = abc.abstractproperty(fdel=clear_descendant_map_id_terms)

    @abc.abstractmethod
    def supports_descendant_map_query(self):
        """Tests if a ``MapQuery`` is available.

        :return: ``true`` if a map query is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # boolean

    @abc.abstractmethod
    def get_descendant_map_query(self):
        """Gets the query for a map.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_map_query()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_descendant_map_query()`` is ``true``.*

        """
        return  # osid.mapping.MapQuery

    descendant_map_query = abc.abstractproperty(fget=get_descendant_map_query)

    @abc.abstractmethod
    def match_any_descendant_map(self, match):
        """Matches maps with any descendant.

        :param match: ``true`` to match maps with any descendant, ``false`` to match leaf maps
        :type match: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    @abc.abstractmethod
    def clear_descendant_map_terms(self):
        """Clears the descendant map query terms.



        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_map_terms = abc.abstractproperty(fdel=clear_descendant_map_terms)

    @abc.abstractmethod
    def get_map_query_record(self, map_record_type):
        """Gets the map query record corresponding to the given ``Map`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the map query record
        :rtype: ``osid.mapping.records.MapQueryRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.MapQueryRecord
