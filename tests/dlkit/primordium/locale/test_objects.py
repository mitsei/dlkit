import pytest

from dlkit.primordium.locale.objects import InitializableLocale
from dlkit.primordium.type.primitives import Type


@pytest.fixture(scope="function")
def initializable_locale_test_wrapper(request):
    request.cls.locale = InitializableLocale()


@pytest.mark.usefixtures("initializable_locale_test_wrapper")
class TestInitializableLocale(object):
    def test_can_set_language_type_identifier(self):
        result = InitializableLocale(language_type_identifier='foo')
        assert result._language_type_identifier == 'foo'

    def test_can_get_language_type_identifier(self):
        assert isinstance(self.locale.language_type, Type)

    def test_can_set_script_type_identifier(self):
        result = InitializableLocale(script_type_identifier='foo')
        assert result._script_type_identifier == 'foo'

    def test_can_get_script_type_identifier(self):
        assert isinstance(self.locale.script_type, Type)

    def test_can_set_calendar_type_identifier(self):
        result = InitializableLocale(calendar_type_identifier='foo')
        assert result._calendar_type_identifier == 'foo'

    def test_can_get_calendar_type_identifier(self):
        assert isinstance(self.locale.calendar_type, Type)

    def test_can_set_time_type_identifier(self):
        result = InitializableLocale(time_type_identifier='foo')
        assert result._time_type_identifier == 'foo'

    def test_can_get_time_type_identifier(self):
        assert isinstance(self.locale.time_type, Type)

    def test_can_set_currency_type_identifier(self):
        result = InitializableLocale(currency_type_identifier='foo')
        assert result._currency_type_identifier == 'foo'

    def test_can_get_currency_type_identifier(self):
        assert isinstance(self.locale.currency_type, Type)

    def test_can_set_unit_system_type_identifier(self):
        result = InitializableLocale(unit_system_type_identifier='foo')
        assert result._unit_system_type_identifier == 'foo'

    def test_can_get_unit_system_type_identifier(self):
        assert isinstance(self.locale.unit_system_type, Type)

    def test_can_set_numeric_format_type_identifier(self):
        result = InitializableLocale(numeric_format_type_identifier='foo')
        assert result._numeric_format_type_identifier == 'foo'

    def test_can_get_numeric_format_type_identifier(self):
        assert isinstance(self.locale.numeric_format_type, Type)

    def test_can_set_calendar_format_type_identifier(self):
        result = InitializableLocale(calendar_format_type_identifier='foo')
        assert result._calendar_format_type_identifier == 'foo'

    def test_can_get_calendar_format_type_identifier(self):
        assert isinstance(self.locale.calendar_format_type, Type)

    def test_can_set_time_format_type_identifier(self):
        result = InitializableLocale(time_format_type_identifier='foo')
        assert result._time_format_type_identifier == 'foo'

    def test_can_get_time_format_type_identifier(self):
        assert isinstance(self.locale.time_format_type, Type)

    def test_can_set_currency_format_type_identifier(self):
        result = InitializableLocale(currency_format_type_identifier='foo')
        assert result._currency_format_type_identifier == 'foo'

    def test_can_get_currency_format_type_identifier(self):
        assert isinstance(self.locale.currency_format_type, Type)

    def test_can_set_coordinate_format_type_identifier(self):
        result = InitializableLocale(coordinate_format_type_identifier='foo')
        assert result._coordinate_format_type_identifier == 'foo'

    def test_can_get_coordinate_format_type_identifier(self):
        assert isinstance(self.locale.coordinate_format_type, Type)
