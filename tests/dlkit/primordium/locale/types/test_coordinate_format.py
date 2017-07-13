import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.coordinate_format import get_type_data


class TestCoordinateFormat(object):
    def test_get_type_data_with_dms(self):
        results = get_type_data('dms')
        assert results['identifier'] == 'DMS'
        assert results['domain'] == 'Coordinate Format Types'
        assert results['display_name'] == 'Degree/Minute/Second Coordinate Format Type'
        assert results['display_label'] == 'Degree/Minute/Second'
        assert results['description'] == 'The type for the Degree/Minute/Second Geographic coordinate format.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
