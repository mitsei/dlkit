import pytest

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type


@pytest.fixture(scope="function")
def display_text_test_wrapper(request):
    request.cls.display_text = DisplayText(display_text_map={
        'text': 'foo',
        'languageTypeId': '639-2%3AHIN%40ISO',
        'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
        'scriptTypeId': '15924%3ADEVA%40ISO'
    })


@pytest.mark.usefixtures("display_text_test_wrapper")
class TestDisplayText(object):
    def test_can_create_display_text_with_map(self):
        result = DisplayText(display_text_map={
            'text': 'foo',
            'languageTypeId': '639-2%3AHIN%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ADEVA%40ISO'
        })
        assert result._text == 'foo'
        assert isinstance(result._language_type, Type)
        assert str(result._language_type) == '639-2%3AHIN%40ISO'
        assert isinstance(result._format_type, Type)
        assert str(result._format_type) == 'TextFormats%3APLAIN%40okapia.net'
        assert isinstance(result._script_type, Type)
        assert str(result._script_type) == '15924%3ADEVA%40ISO'

    def test_can_create_display_text_with_kwargs(self):
        result = DisplayText(text='foo',
                             language_type=Type('639-2%3AHIN%40ISO'),
                             format_type=Type('TextFormats%3APLAIN%40okapia.net'),
                             script_type=Type('15924%3ADEVA%40ISO'))
        assert result._text == 'foo'
        assert isinstance(result._language_type, Type)
        assert str(result._language_type) == '639-2%3AHIN%40ISO'
        assert isinstance(result._format_type, Type)
        assert str(result._format_type) == 'TextFormats%3APLAIN%40okapia.net'
        assert isinstance(result._script_type, Type)
        assert str(result._script_type) == '15924%3ADEVA%40ISO'

    def test_initer_raises_null_argument(self):
        with pytest.raises(errors.NullArgument):
            DisplayText()

    def test_can_get_text(self):
        assert self.display_text.text == 'foo'

    def test_can_get_language_type(self):
        assert isinstance(self.display_text.language_type, Type)
        assert str(self.display_text.language_type) == '639-2%3AHIN%40ISO'

    def test_can_get_script_type(self):
        assert isinstance(self.display_text.script_type, Type)
        assert str(self.display_text.script_type) == '15924%3ADEVA%40ISO'

    def test_can_get_format_type(self):
        assert isinstance(self.display_text.format_type, Type)
        assert str(self.display_text.format_type) == 'TextFormats%3APLAIN%40okapia.net'
