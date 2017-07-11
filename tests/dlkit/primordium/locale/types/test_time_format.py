import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.time_format import get_type_data


class TestTimeFormat(object):
    def test_get_type_data_with_time(self):
        results = get_type_data('hhmmss')
        assert results['identifier'] == 'HHMMSS'
        assert results['domain'] == 'Time Format Types'
        assert results['display_name'] == '24 Hour Clock (hh:mm:ss) Time Format Type'
        assert results['display_label'] == '24 Hour Clock (hh:mm:ss)'
        assert results['description'] == 'The time format type for 24 Hour Clock (hh:mm:ss)'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
