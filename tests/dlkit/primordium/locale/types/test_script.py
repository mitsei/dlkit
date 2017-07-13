import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.script import get_type_data


class TestScript(object):
    def test_get_type_data_with_iso(self):
        results = get_type_data('xsux')
        assert results['identifier'] == 'XSUX'
        assert results['namespace'] == '15924'
        assert results['display_name'] == 'Cuneiform Script Type'
        assert results['display_label'] == 'Cuneiform'
        assert results['description'] == 'The display text script type for the Cuneiform script.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
