import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.unit_system import get_type_data


class TestUnitSystem(object):
    def test_get_type_data_with_time(self):
        results = get_type_data('metric')
        assert results['identifier'] == 'METRIC'
        assert results['domain'] == 'Unit System Types'
        assert results['display_name'] == 'Metric Unit System Type'
        assert results['display_label'] == 'Metric'
        assert results['description'] == 'The unit system type for the Metric System'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
