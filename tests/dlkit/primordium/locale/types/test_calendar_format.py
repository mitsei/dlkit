import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.calendar_format import get_type_data


class TestCalendarFormat(object):
    def test_get_type_data_with_mmddyyyy(self):
        results = get_type_data('mmddyyyy')
        assert results['identifier'] == 'MMDDYYYY'
        assert results['domain'] == 'Calendar Format Types'
        assert results['display_name'] == 'MM/DD/YYYY Calendar Format Type'
        assert results['display_label'] == 'MM/DD/YYYY'
        assert results['description'] == 'The calendar format type for MM/DD/YYYY'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
