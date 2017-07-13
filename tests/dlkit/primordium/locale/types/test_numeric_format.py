import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.numeric_format import get_type_data


class TestNumericFormat(object):
    def test_get_type_data_with_gnu(self):
        results = get_type_data('e8.1')
        assert results['identifier'] == 'E8.1'
        assert results['domain'] == 'Numeric Format Types'
        assert results['display_name'] == 'E8.1, (3.1E+003, -3.1E+003) Numeric Format Type'
        assert results['display_label'] == 'E8.1, (3.1E+003, -3.1E+003)'
        assert results['description'] == 'The type for the E8.1, (3.1E+003, -3.1E+003) numeric format.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
