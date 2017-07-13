import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.language import get_type_data


class TestLanguage(object):
    def test_get_type_data_with_iso(self):
        results = get_type_data('gl')
        assert results['identifier'] == 'GLG'
        assert results['namespace'] == '639-2'
        assert results['display_name'] == 'Galician Language Type'
        assert results['display_label'] == 'Galician'
        assert results['description'] == 'The display text language type for the Galician language.'

    def test_get_type_data_with_iso_major(self):
        results = get_type_data('twi')
        assert results['identifier'] == 'TWI'
        assert results['namespace'] == '639-2'
        assert results['display_name'] == 'Twi Language Type'
        assert results['display_label'] == 'Twi'
        assert results['description'] == 'The display text language type for the Twi language.'

    def test_get_type_data_with_iso_other(self):
        results = get_type_data('zrp')
        assert results['identifier'] == 'ZRP'
        assert results['namespace'] == '639-3'
        assert results['display_name'] == 'Zarphatic Language Type'
        assert results['display_label'] == 'Zarphatic'
        assert results['description'] == 'The display text language type for the Zarphatic language.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
