"""Implementations of mapping abstract base class query_inspectors."""
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


class LocationQueryInspector:
    """This is the query inspector for searching locations."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_coordinate_terms(self):
        """Gets the coordinate query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CoordinateTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.CoordinateTerm

    coordinate_terms = abc.abstractproperty(fget=get_coordinate_terms)

    @abc.abstractmethod
    def get_contained_spatial_unit_terms(self):
        """Gets the contained spatial unit query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    contained_spatial_unit_terms = abc.abstractproperty(fget=get_contained_spatial_unit_terms)

    @abc.abstractmethod
    def get_overlapping_spatial_unit_terms(self):
        """Gets the overlapping spatial unit query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    overlapping_spatial_unit_terms = abc.abstractproperty(fget=get_overlapping_spatial_unit_terms)

    @abc.abstractmethod
    def get_spatial_unit_terms(self):
        """Gets the spatial unit query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.SpatialUnitTerm

    spatial_unit_terms = abc.abstractproperty(fget=get_spatial_unit_terms)

    @abc.abstractmethod
    def get_route_id_terms(self):
        """Gets the route ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    route_id_terms = abc.abstractproperty(fget=get_route_id_terms)

    @abc.abstractmethod
    def get_route_terms(self):
        """Gets the route query terms.

        :return: the query terms
        :rtype: ``osid.mapping.route.RouteQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.route.RouteQueryInspector

    route_terms = abc.abstractproperty(fget=get_route_terms)

    @abc.abstractmethod
    def get_path_id_terms(self):
        """Gets the path ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    path_id_terms = abc.abstractproperty(fget=get_path_id_terms)

    @abc.abstractmethod
    def get_path_terms(self):
        """Gets the path query terms.

        :return: the query terms
        :rtype: ``osid.mapping.path.PathQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.path.PathQueryInspector

    path_terms = abc.abstractproperty(fget=get_path_terms)

    @abc.abstractmethod
    def get_containing_location_id_terms(self):
        """Gets the containing location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    containing_location_id_terms = abc.abstractproperty(fget=get_containing_location_id_terms)

    @abc.abstractmethod
    def get_containing_location_terms(self):
        """Gets the containing location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    containing_location_terms = abc.abstractproperty(fget=get_containing_location_terms)

    @abc.abstractmethod
    def get_contained_location_id_terms(self):
        """Gets the contained location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    contained_location_id_terms = abc.abstractproperty(fget=get_contained_location_id_terms)

    @abc.abstractmethod
    def get_contained_location_terms(self):
        """Gets the contained location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    contained_location_terms = abc.abstractproperty(fget=get_contained_location_terms)

    @abc.abstractmethod
    def get_map_id_terms(self):
        """Gets the map ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    map_id_terms = abc.abstractproperty(fget=get_map_id_terms)

    @abc.abstractmethod
    def get_map_terms(self):
        """Gets the map query terms.

        :return: the query terms
        :rtype: ``osid.mapping.MapQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapQueryInspector

    map_terms = abc.abstractproperty(fget=get_map_terms)

    @abc.abstractmethod
    def get_location_query_inspector_record(self, location_record_type):
        """Gets the location query inspector record corresponding to the given ``Location`` record ``Type``.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the location query inspector record
        :rtype: ``osid.mapping.records.LocationQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.LocationQueryInspectorRecord


class MapQueryInspector:
    """This is the query inspector for searching maps."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_location_id_terms(self):
        """Gets the location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    location_id_terms = abc.abstractproperty(fget=get_location_id_terms)

    @abc.abstractmethod
    def get_location_terms(self):
        """Gets the location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.LocationQueryInspector

    location_terms = abc.abstractproperty(fget=get_location_terms)

    @abc.abstractmethod
    def get_path_id_terms(self):
        """Gets the path ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    path_id_terms = abc.abstractproperty(fget=get_path_id_terms)

    @abc.abstractmethod
    def get_path_terms(self):
        """Gets the path query terms.

        :return: the query terms
        :rtype: ``osid.mapping.path.PathQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.path.PathQueryInspector

    path_terms = abc.abstractproperty(fget=get_path_terms)

    @abc.abstractmethod
    def get_route_id_terms(self):
        """Gets the route ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    route_id_terms = abc.abstractproperty(fget=get_route_id_terms)

    @abc.abstractmethod
    def get_route_terms(self):
        """Gets the route query terms.

        :return: the query terms
        :rtype: ``osid.mapping.route.RouteQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.route.RouteQueryInspector

    route_terms = abc.abstractproperty(fget=get_route_terms)

    @abc.abstractmethod
    def get_ancestor_map_id_terms(self):
        """Gets the ancestor map ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    ancestor_map_id_terms = abc.abstractproperty(fget=get_ancestor_map_id_terms)

    @abc.abstractmethod
    def get_ancestor_map_terms(self):
        """Gets the ancestor map query terms.

        :return: the query terms
        :rtype: ``osid.mapping.MapQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapQueryInspector

    ancestor_map_terms = abc.abstractproperty(fget=get_ancestor_map_terms)

    @abc.abstractmethod
    def get_descendant_map_id_terms(self):
        """Gets the descendant map ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.search.terms.IdTerm

    descendant_map_id_terms = abc.abstractproperty(fget=get_descendant_map_id_terms)

    @abc.abstractmethod
    def get_descendant_map_terms(self):
        """Gets the descendant map query terms.

        :return: the query terms
        :rtype: ``osid.mapping.MapQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.MapQueryInspector

    descendant_map_terms = abc.abstractproperty(fget=get_descendant_map_terms)

    @abc.abstractmethod
    def get_map_query_inspector_record(self, map_record_type):
        """Gets the record query inspector interface corresponding to the given ``Map`` record ``Type``.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the map query inspector record
        :rtype: ``osid.mapping.records.MapQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return  # osid.mapping.records.MapQueryInspectorRecord
