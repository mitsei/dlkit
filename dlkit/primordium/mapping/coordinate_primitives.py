"""
Basic coordinate implementions of osid.mapping.coordinate.

Can be used by implementations and consumer applications alike.

"""

from dlkit.abstract_osid.mapping import primitives as abc_mapping_primitives
from dlkit.abstract_osid.osid.errors import NullArgument, InvalidArgument
from ..osid.primitives import OsidPrimitive
from ..type.primitives import Type


class BasicCoordinate(abc_mapping_primitives.Coordinate, OsidPrimitive):
    """
    A coordinate represents a position.

    In this case a position in an N dimentional space where N is defined by the
    number of values in the values list. values and uncertanty list elements must
    be of type float or int.

    """

    def __init__(self,
                 values,
                 uncertainty_minus=None,
                 uncertainty_plus=None):
        self._values = self._float_list(values)
        self._dimensions = len(self._values)
        self._zero_uncertainty = None
        if uncertainty_minus is None:
            uncertainty_minus = self._get_zero_uncertainty()
        if uncertainty_plus is None:
            uncertainty_plus = self._get_zero_uncertainty()
        self._uncertainty_minus = self._float_list(uncertainty_minus, self._dimensions)
        self._uncertainty_plus = self._float_list(uncertainty_plus, self._dimensions)

    def _float_list(self, value_list, dimensions=None):
        if not isinstance(value_list, list):
            raise InvalidArgument('arguments must be list of floating point or integer values')
        if dimensions is not None and len(value_list) != dimensions:
            raise InvalidArgument('dimensions of uncertainty must match dimensions of values')
        return_list = list()
        for value in value_list:
            if isinstance(value, float) or isinstance(value, int):
                return_list.append(float(value))
            else:
                raise InvalidArgument('arguments must be list of floating point or integer values')
        return return_list

    def _get_zero_uncertainty(self):
        if self._zero_uncertainty is None:
            uncertainty_list = list()
            for num in range(self._dimensions):
                uncertainty_list.append(0)
            self._zero_uncertainty = uncertainty_list
        return self._zero_uncertainty

    def _compare(self, other, method):
        """see https://regebro.wordpress.com/2010/12/13/python-implementing-rich-comparison-the-correct-way/"""
        # This needs to be updated to take uncertainty into account:
        if isinstance(other, abc_mapping_primitives.Coordinate):
            if self.get_dimensions() != other.get_dimensions():
                return False
            other_values = other.get_values()
            for index in range(self._dimensions):
                if not method(self._values[index], other_values[index]):
                    return False
            return True
        return NotImplemented

    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)

    def __eq__(self, other):
        return self._compare(other, lambda s, o: s == o)

    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def get_coordinate_type(self):
        return Type(identifier='basic_coordinate',
                    authority='ODL.MIT.EDU',
                    namespace='mapping.Coordinate',
                    display_name='Basic Coordinate',
                    display_label='Basic Coordinate',
                    description='Coordinate Type for a Basic Coordinate',
                    domain='mapping.Coordinate')

    coordinate_type = property(fget=get_coordinate_type)

    def get_dimensions(self):
        return self._dimensions

    dimensions = property(fget=get_dimensions)

    def get_values(self):
        return self._values

    values = property(fget=get_values)

    def defines_uncertainty(self):
        return (self._uncertainty_minus != self._zero_uncertainty and
                self._uncertainty_plus != self._zero_uncertainty)

    def get_uncertainty_minus(self):
        return self._uncertainty_minus

    uncertainty_minus = property(fget=get_uncertainty_minus)

    def get_uncertainty_plus(self):
        return self._uncertainty_plus

    uncertainty_plus = property(fget=get_uncertainty_plus)
