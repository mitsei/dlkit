import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.time import get_type_data


class TestTime(object):
    def test_get_type_data_with_celestial(self):
        results = get_type_data('et')
        assert results['identifier'] == 'ET'
        assert results['domain'] == 'Celestial Time Systems'
        assert results['display_name'] == 'Ephemeris Time Type'
        assert results['display_label'] == 'Ephemeris'
        assert results['description'] == 'The time type for Ephemeris time.'

    def test_get_type_data_with_earth(self):
        results = get_type_data('utc')
        assert results['identifier'] == 'UTC'
        assert results['domain'] == 'Earth Time Systems'
        assert results['display_name'] == 'Coordinate Universal Time Type'
        assert results['display_label'] == 'Coordinate Universal'
        assert results['description'] == 'The time type for Coordinate Universal time.'

    def test_get_type_data_with_fun(self):
        results = get_type_data('colonial')
        assert results['identifier'] == 'COLONIAL'
        assert results['domain'] == 'Alternative Time Systems'
        assert results['display_name'] == 'Colonial, Battlestar Galactica Time Type'
        assert results['display_label'] == 'Colonial, Battlestar Galactica'
        assert results['description'] == 'The time type for Colonial, Battlestar Galactica time.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
