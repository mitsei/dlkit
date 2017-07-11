import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.currency import get_type_data


class TestCurrency(object):
    def test_get_type_data_with_iso(self):
        results = get_type_data('aed')
        assert results['identifier'] == 'AED'
        assert results['domain'] == 'ISO Currency Types'
        assert results['display_name'] == 'UAE Dirham Currency Type'
        assert results['display_label'] == 'UAE Dirham'
        assert results['description'] == 'The ISO currency type for the UAE Dirham.'

    def test_get_type_data_with_iso_element(self):
        results = get_type_data('xau')
        assert results['identifier'] == 'XAU'
        assert results['domain'] == 'ISO Currency Types'
        assert results['display_name'] == 'Gold Currency Type'
        assert results['display_label'] == 'Gold'
        assert results['description'] == 'The ISO currency type for Gold.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
