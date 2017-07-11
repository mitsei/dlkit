import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.coordinate import get_type_data


class TestCoordinate(object):
    def test_get_type_data_with_celestial(self):
        results = get_type_data('horizon')
        assert results['domain'] == 'Celestial Coordinate Systems'
        assert results['display_name'] == 'Horizon Type'
        assert results['display_label'] == 'Horizon'
        assert results['description'] == 'The type for the Horizon System.'

    def test_get_type_data_with_geographic(self):
        results = get_type_data('ups')
        assert results['domain'] == 'Geographic Coordinate Systems'
        assert results['display_name'] == 'UPS, Universal Polar Stereographic Coordinate Type'
        assert results['display_label'] == 'UPS, Universal Polar Stereographic Coordinate'
        assert results['description'] == 'The type for the UPS, Universal Polar Stereographic Coordinate System.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
