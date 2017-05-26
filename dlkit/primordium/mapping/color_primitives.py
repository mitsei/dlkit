"""
Color coordinate implementions of osid.mapping.coordinate.

Can be used by implementations and consumer applications alike.

"""

from dlkit.abstract_osid.mapping import primitives as abc_mapping_primitives
from dlkit.abstract_osid.osid.errors import NullArgument, InvalidArgument
from dlkit.json_.utilities import is_string
from ..osid.primitives import OsidPrimitive
from ..type.primitives import Type


class RGBColorCoordinate(abc_mapping_primitives.Coordinate, OsidPrimitive):
    """
    A coordinate represents a position.

    In this case a position in a 3 dimentional RGB color space.

    """

    def __init__(self, hexstr=None,
                 values=None,
                 uncertainty_minus=None,
                 uncertainty_plus=None):
        if values is not None:
            if not isinstance(values, list) or len(values) != 3:
                raise InvalidArgument()
            self._values = values
        elif hexstr is not None:
            if not is_string(hexstr) or len(hexstr) != 6:
                raise InvalidArgument()
            try:
                self._values = [int(hexstr[:-4], 16), int(hexstr[2:-2], 16), int(hexstr[4:], 16)]
            except:
                raise InvalidArgument(hexstr)
        else:
            raise NullArgument()
        self._uncertainty_minus = uncertainty_minus
        self._uncertainty_plus = uncertainty_plus

    def __str__(self):
        hexlist = []
        for value in self._values:
            hexstr = hex(value)[2:]
            if len(hexstr) == 1:
                hexstr = '0' + hexstr
            hexlist.append(hexstr)
        return ''.join(hexlist)

    def get_coordinate_type(self):
        return Type(identifier='rgb_color',
                    authority='ODL.MIT.EDU',
                    namespace='mapping.Coordinate',
                    display_name='RGB Color Coordinate',
                    display_label='RGB Color',
                    description='Coordinate Type for an RGB Color',
                    domain='mapping.Coordinate')

    coordinate_type = property(fget=get_coordinate_type)

    def get_dimensions(self):
        return len(self._values)

    dimensions = property(fget=get_dimensions)

    def get_values(self):
        return self._values

    values = property(fget=get_values)

    def defines_uncertainty(self):
        return self._uncertainty_minus or self._uncertainty_plus

    def get_uncertainty_minus(self):
        return self._uncertainty_minus

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        return self._uncertainty_plus

    uncertainty_plus = property(fget=get_uncertainty_plus)
