# NOTE: most of this file is tested in tests/other/test_mapping_primitives.py
# So these tests only cover the lines not included in the other tests

import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.mapping.coordinate_primitives import BasicCoordinate
from dlkit.primordium.type.primitives import Type


@pytest.fixture(scope="function")
def coordinate_test_wrapper(request):
    request.cls.coordinate = BasicCoordinate(values=[1, 250, 69])


@pytest.mark.usefixtures("coordinate_test_wrapper")
class TestBasicCoordinate(object):
    def test_float_list_throws_invalid_argument_for_non_list(self):
        with pytest.raises(errors.InvalidArgument):
            self.coordinate._float_list('foo')

    def test_float_list_throws_invalid_argument_for_mismatching_dimensions(self):
        with pytest.raises(errors.InvalidArgument):
            self.coordinate._float_list([1, 2], dimensions=3)

    def test_float_list_throws_invalid_argument_for_non_numeric_values(self):
        with pytest.raises(errors.InvalidArgument):
            self.coordinate._float_list(['1', '2'])

    def test_compare_with_two_different_dimension_lists_returns_false(self):
        other = BasicCoordinate(values=[1, 250, 69, 6])
        assert not self.coordinate._compare(other, lambda s, o: s == o)

    def test_compare_returns_not_implemented_if_not_coordinate(self):
        assert self.coordinate._compare('foo', lambda s, o: s == o) == NotImplemented

    def test_ne_returns_not_implemented_if_not_coordinate(self):
        assert self.coordinate != 'foo'

    def test_get_coordinate_type_returns_type(self):
        assert isinstance(self.coordinate.coordinate_type, Type)

    def test_can_check_defines_uncertainty(self):
        assert not self.coordinate.defines_uncertainty()

        other = BasicCoordinate(values=[1, 250, 69],
                                uncertainty_minus=[1, 1, 1],
                                uncertainty_plus=[2, 2, 2])
        assert other.defines_uncertainty()

    def test_can_get_uncertainty_minus(self):
        result = BasicCoordinate(values=[1, 250, 69],
                                 uncertainty_minus=[1, 1, 1])
        assert result.uncertainty_minus == [1, 1, 1]

    def test_can_get_uncertainty_plus(self):
        result = BasicCoordinate(values=[1, 250, 69],
                                 uncertainty_plus=[1, 1, 1])
        assert result.uncertainty_plus == [1, 1, 1]
