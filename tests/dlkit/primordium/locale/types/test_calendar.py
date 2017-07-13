import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.calendar import get_type_data


class TestCalendar(object):
    def test_get_type_data_with_celestial(self):
        results = get_type_data('xhosa')
        assert results['domain'] == 'Calendar Types'
        assert results['display_name'] == 'Xhosa Calendar Type'
        assert results['display_label'] == 'Xhosa'
        assert results['description'] == 'The time type for the Xhosa calendar.'

    def test_get_type_data_with_ancient_calendar(self):
        results = get_type_data('assyrian')
        assert results['domain'] == 'Ancient Calendar Types'
        assert results['display_name'] == 'Assyrian Calendar Type'
        assert results['display_label'] == 'Assyrian'
        assert results['description'] == 'The time type for the Assyrian calendar.'

    def test_get_type_data_with_alternate_calendar(self):
        results = get_type_data('middle_earth')
        assert results['domain'] == 'Alternative Calendar Types'
        assert results['display_name'] == 'MiddleEarth, Middle-earth Calendar Type'
        assert results['display_label'] == 'MiddleEarth, Middle-earth'
        assert results['description'] == 'The time type for the MiddleEarth, Middle-earth calendar.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
