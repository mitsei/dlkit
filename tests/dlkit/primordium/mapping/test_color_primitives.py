import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.mapping.color_primitives import RGBColorCoordinate
from dlkit.primordium.type.primitives import Type


@pytest.fixture(scope="function")
def color_coordinate_test_wrapper(request):
    request.cls.color = RGBColorCoordinate(values=[1, 250, 69])


@pytest.mark.usefixtures("color_coordinate_test_wrapper")
class TestRGBColorCoordinate(object):
    def test_can_create_color_with_hexstr(self):
        result = RGBColorCoordinate(hexstr='32fa45')
        assert result._values == [50, 250, 69]

    def test_hexstr_throws_invalid_argument_for_non_string(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(hexstr=32)

    def test_hexstr_throws_invalid_argument_for_wrong_length(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(hexstr='0011001')
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(hexstr='00110')

    def test_hexstr_throws_invalid_argument_for_non_hex(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(hexstr='0011zz')

    def test_values_throws_invalid_argument_for_non_list(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(values='32fa45')

    def test_values_throws_invalid_argument_for_wrong_length(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(values=[1, 2, 3, 4])
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(values=[1, 2])

    def test_can_create_color_with_values(self):
        result = RGBColorCoordinate(values=[50, 250, 69])
        assert result._values == [50, 250, 69]

    def test_can_create_color_with_uncertainty_minus(self):
        result = RGBColorCoordinate(values=[50, 250, 69],
                                    uncertainty_minus=[5, 5, 5])
        assert result._uncertainty_minus == [5, 5, 5]

    def test_can_create_color_with_uncertainty_plus(self):
        result = RGBColorCoordinate(values=[50, 250, 69],
                                    uncertainty_plus=[15, 15, 15])
        assert result._uncertainty_plus == [15, 15, 15]

    def test_initer_raises_null_argument(self):
        with pytest.raises(errors.NullArgument):
            RGBColorCoordinate()

    def test_can_get_string_representation(self):
        assert str(self.color) == '01fa45'

    def test_can_get_coordinate_type(self):
        assert isinstance(self.color.coordinate_type, Type)
        assert str(self.color.coordinate_type) == 'mapping.Coordinate%3Argb_color%40ODL.MIT.EDU'

    def test_can_get_dimensions(self):
        assert self.color.dimensions == 3

    def test_can_get_values(self):
        assert self.color.values == [1, 250, 69]

    def test_can_check_defines_uncertainty(self):
        assert not self.color.defines_uncertainty()

        result = RGBColorCoordinate(values=[50, 250, 69],
                                    uncertainty_plus=[15, 15, 15])
        assert result.defines_uncertainty()

        result = RGBColorCoordinate(values=[50, 250, 69],
                                    uncertainty_minus=[5, 5, 5])
        assert result.defines_uncertainty()

    def test_can_get_uncertainty_plus(self):
        assert self.color.uncertainty_plus is None

        result = RGBColorCoordinate(values=[50, 250, 69],
                                    uncertainty_plus=[15, 15, 15])
        assert result.uncertainty_plus == [15, 15, 15]

    def test_can_get_uncertainty_minus(self):
        assert self.color.uncertainty_minus is None

        result = RGBColorCoordinate(values=[50, 250, 69],
                                    uncertainty_minus=[5, 5, 5])
        assert result.uncertainty_minus == [5, 5, 5]
