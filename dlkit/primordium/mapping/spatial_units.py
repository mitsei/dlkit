"""
Implementions of osid.mapping.SpatialUnit.

Can be used by implementations and consumer applications alike.

"""

from dlkit.abstract_osid.mapping import primitives as abc_mapping_primitives
from dlkit.abstract_osid.osid.errors import NullArgument, InvalidArgument
from ..osid.primitives import OsidPrimitive
from ..type.primitives import Type
from dlkit.primordium.mapping.coordinate_primitives import BasicCoordinate
from decimal import Decimal


class SpatialUnitFactory(object):
    """returns the right SpatialUnit depending on the record type in the spatial_unit_map

    Assumes only one record type for now!

    """

    def get_spatial_unit(self, spatial_unit_map):
        record_type = Type(idstr=spatial_unit_map['recordTypes'][0])
        if (record_type.get_authority() != 'ODL.MIT.EDU' or
                record_type.get_identifier_namespace() != 'osid.mapping.SpatialUnit'):
            raise InvalidArgument()
        if record_type.get_identifier() == 'rectangle':
            return RectangularSpatialUnit(spatial_unit_map=spatial_unit_map)
        raise InvalidArgument()


class RectangularSpatialUnit(abc_mapping_primitives.SpatialUnit, OsidPrimitive):
    """
    A spatial unit represents a region in space.

    In this case a rectangle in a 2 dimensional coordinate space.

    """

    def __init__(self, coordinate=None, width=None, height=None, spatial_unit_map=None):
        if spatial_unit_map is None and coordinate is None and width is None and height is None:
            raise NullArgument('must provide a coordinate or a spatial_unit_map')
        if spatial_unit_map is not None:
            self._coordinate = BasicCoordinate(spatial_unit_map['coordinateValues'])
            self._width = spatial_unit_map['width']
            self._height = spatial_unit_map['height']
        else:
            if not isinstance(coordinate, abc_mapping_primitives.Coordinate):
                raise InvalidArgument('coordinate must be a Coordinate')
            if height is None:
                raise NullArgument('height must be provided with a coordinate')
            if width is None:
                raise NullArgument('width must be provided with a coordinate')
            if not (isinstance(height, int) or isinstance(height, float)):
                raise InvalidArgument('height must be an int or float')
            if not (isinstance(width, int) or isinstance(width, float)):
                raise InvalidArgument('width must be an int or float')
            if width <= 0 or height <= 0:
                raise InvalidArgument('width and height must be positive values')
            self._coordinate = coordinate
            self._width = width
            self._height = height

    def get_center_coordinate(self):
        x, y = self._coordinate.get_values()
        return BasicCoordinate([
            float(Decimal(x) + Decimal(self._width) / 2),
            float(Decimal(y) + Decimal(self._height) / 2)
        ])

    center_coordinate = property(fget=get_center_coordinate)

    def get_bounding_coordinates(self):
        x, y = self._coordinate.get_values()
        return [
            self._coordinate,
            BasicCoordinate([x + self._width, y]),
            BasicCoordinate([x + self._width, y + self._height]),
            BasicCoordinate([x, y + self._height])
        ]

    bounding_coordinates = property(fget=get_bounding_coordinates)

    def get_spatial_unit_record(self):
        pass  # This should return a record type for

    spatial_unit_record = property(fget=get_spatial_unit_record)

    def __contains__(self, coordinate):
        if not isinstance(coordinate, abc_mapping_primitives.Coordinate):
            raise TypeError('osid.mapping.SpatialUnit requires osid.mapping.Coordinate as left operand')
        x, y = self._coordinate.get_values()
        return bool(coordinate >= self._coordinate and
                    coordinate <= BasicCoordinate([x + self._width, y + self._height]))

    def get_record_types(self):
        return [
            Type(authority='ODL.MIT.EDU',
                 namespace='osid.mapping.SpatialUnit',
                 identifier='rectangle')]

    def is_of_record_type(self, record_type):
        return bool(record_type in self.get_record_types())

    def get_spatial_unit_map(self):
        record_types = []
        for rtype in self.get_record_types():
            record_types.append(str(rtype))
        return {
            'type': 'SpatialUnit',
            'recordTypes': record_types,
            'coordinateValues': self._coordinate.get_values(),
            'width': self._width,
            'height': self._height
        }
