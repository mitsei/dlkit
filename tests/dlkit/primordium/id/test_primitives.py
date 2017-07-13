import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id


@pytest.fixture(scope="function")
def id_test_wrapper(request):
    request.cls.id = Id(idstr='package.Object%3Aidentifier%40AUTHORITY')


@pytest.mark.usefixtures("id_test_wrapper")
class TestId(object):
    def test_can_create_id_with_idstr(self):
        result = Id(idstr='package.Object%3Aidentifier%40AUTHORITY')
        assert result._authority == 'AUTHORITY'
        assert result._identifier == 'identifier'
        assert result._namespace == 'package.Object'

    def test_can_create_id_with_kwargs(self):
        result = Id(authority='AUTHORITY', namespace='package.Object', identifier='identifier')
        assert result._authority == 'AUTHORITY'
        assert result._identifier == 'identifier'
        assert result._namespace == 'package.Object'

    def test_initer_raises_null_argument(self):
        with pytest.raises(errors.NullArgument):
            Id()

    def test_can_get_string_representation(self):
        result = Id(idstr='package.Object%3Aidentifier%40AUTHORITY')
        assert str(result) == 'package.Object%3Aidentifier%40AUTHORITY'

    def test_can_get_authority(self):
        assert self.id.authority == 'AUTHORITY'

    def test_can_get_namespace(self):
        assert self.id.namespace == 'package.Object'

    def test_can_get_identifier_namespace(self):
        assert self.id.identifier_namespace == 'package.Object'

    def test_can_get_identifier(self):
        assert self.id.identifier == 'identifier'
