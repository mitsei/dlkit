import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.installation.primitives import Version


class TestVersion(object):
    def test_can_create_version_with_components(self):
        result = Version(components=[0, 3, 0])
        assert result._components == [0, 3, 0]

    def test_can_create_version_with_none_components(self):
        result = Version()
        assert result._components == []

    def test_initer_raises_invalid_argument(self):
        with pytest.raises(errors.InvalidArgument):
            Version(components='foo')

    def test_can_get_scheme(self):
        result = Version()
        assert result.scheme is None

    def test_can_get_components(self):
        result = Version(components=[0, 3, 0])
        assert result.components == [0, 3, 0]
