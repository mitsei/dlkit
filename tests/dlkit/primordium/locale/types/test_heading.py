import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.types.heading import get_type_data


class TestHeading(object):
    def test_get_type_data_with_degree(self):
        results = get_type_data('degree')
        assert results['identifier'] == 'DEGREE'
        assert results['domain'] == 'Headings'
        assert results['display_name'] == 'Degree Heading Type'
        assert results['display_label'] == 'Degree'
        assert results['description'] == 'The heading type for the Degree heading.'

    def test_unknown_type(self):
        with pytest.raises(errors.NotFound):
            get_type_data('foo')
