import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.mapping.color_primitives import RGBColorCoordinate
from dlkit.primordium.type.primitives import Type


class TestRGBColorCoordinate(object):
    def test_can_create_color_with_hexstr(self):
        result = RGBColorCoordinate(hexstr='32fa45')
        assert result._values == [50, 250, 69]

    def test_hexstr_throws_invalid_argument_for_non_string(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(hexstr=32)

    def test_hexstr_throws_invalid_argument_for_wrong_length(self):
        with pytest.raises(errors.InvalidArgument):
            RGBColorCoordinate(hexstr='0011001100')

    def test_hexstr_throws_invalid_argument_for_non_hex(self):
        assert False

    def test_values_throws_invalid_argument_for_non_list(self):
        assert False

    def test_values_throws_invalid_argument_for_wrong_length(self):
        assert False

    def test_can_create_color_with_values(self):
        result = DisplayText(text='foo',
                             language_type=Type('639-2%3AHIN%40ISO'),
                             format_type=Type('TextFormats%3APLAIN%40okapia.net'),
                             script_type=Type('15924%3ADEVA%40ISO'))
        assert result._text == 'foo'
        assert isinstance(result._language_type, Type)
        assert str(result._language_type) == '639-2%3AHIN%40ISO'
        assert isinstance(result._format_type, Type)
        assert str(result._format_type) == 'TextFormats%3APLAIN%40okapia.net'
        assert isinstance(result._script_type, Type)
        assert str(result._script_type) == '15924%3ADEVA%40ISO'

    def test_can_create_color_with_uncertainty_minus(self):
        assert False

    def test_can_create_color_with_uncertainty_plus(self):
        assert False

    def test_initer_raises_null_argument(self):
        with pytest.raises(errors.NullArgument):
            DisplayText()

    def test_can_get_string_representation(self):
        assert False

    def test_can_get_coordinate_type(self):
        assert self.display_text.text == 'foo'

    def test_can_get_dimensions(self):
        assert isinstance(self.display_text.language_type, Type)
        assert str(self.display_text.language_type) == '639-2%3AHIN%40ISO'

    def test_can_get_values(self):
        assert isinstance(self.display_text.script_type, Type)
        assert str(self.display_text.script_type) == '15924%3ADEVA%40ISO'

    def test_can_check_defines_uncertainty(self):
        assert isinstance(self.display_text.format_type, Type)
        assert str(self.display_text.format_type) == 'TextFormats%3APLAIN%40okapia.net'

    def test_can_get_uncertainty_plus(self):
        assert False

    def test_can_get_uncertainty_minus(self):
        assert False
