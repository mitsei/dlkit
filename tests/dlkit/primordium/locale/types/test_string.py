import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.string import get_type_data


class TestString(object):
    def test_get_type_data_with_iso(self):
        results = get_type_data('dmetaphone')
        assert results['identifier'] == 'DMETAPHONE'
        assert results['display_name'] == 'Dmetaphone String Match Type'
        assert results['display_label'] == 'Dmetaphone'
        assert results['description'] == 'The string match type for the Dmetaphone'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
