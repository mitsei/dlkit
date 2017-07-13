import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.currency_format import get_type_data


class TestCurrencyFormat(object):
    def test_get_type_data_with_us(self):
        results = get_type_data('us')
        assert results['identifier'] == 'US'
        assert results['domain'] == 'Currency Format Types'
        assert results['display_name'] == 'US ($1,234.56) Currency Format Type'
        assert results['display_label'] == 'US ($1,234.56)'
        assert results['description'] == 'The format type for the US ($1,234.56) currency'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
