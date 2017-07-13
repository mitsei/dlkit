import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.format import get_type_data


class TestFormat(object):
    def test_get_type_data_with_format(self):
        results = get_type_data('troff')
        assert results['identifier'] == 'TROFF'
        assert results['domain'] == 'DisplayText Formats'
        assert results['display_name'] == 'troff Format Type'
        assert results['display_label'] == 'troff'
        assert results['description'] == 'The display text format type for the troff format.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
