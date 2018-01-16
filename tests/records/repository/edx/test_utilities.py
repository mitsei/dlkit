import os
import pytest
import tarfile

from bs4 import BeautifulSoup
from copy import deepcopy
from six import BytesIO

from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.objects import OsidObject
from dlkit.records.repository.edx.utilities import *

from ... import utilities

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))


class TestUtilityMethods(object):
    def test_clean_str_removes_non_words(self):
        assert clean_str('123 Foo !@#,-_') == '123_Foo_______'

    def test_get_byte_stream_size_returns_obj_size(self):
        test_stream = BytesIO('foo'.encode('utf-8'))
        assert get_byte_stream_size(test_stream) == 3

    def test_get_current_time_in_secs_is_accurate(self):
        assert isinstance(get_current_time_in_secs(), int)
        assert get_current_time_in_secs() > 0

    def test_remove_redundant_drafts_works(self):
        assert remove_redundant_drafts('/drafts/drafts') == '/drafts'
        assert remove_redundant_drafts('/drafts') == '/drafts'

    def test_remove_trailing_slash_works(self):
        assert remove_trailing_slash('/foo/') == '/foo'
        assert remove_trailing_slash('/foo') == '/foo'

    def test_slugify_works_without_django(self):
        assert slugify('6.001X, 123-') == '6001x-123-'


@pytest.fixture(scope="class")
def edx_utilities_mixin_class_fixture(request):
    request.cls.mixin = EdXUtilitiesMixin()

    obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
    obj_map['displayName'] = {
        'text': 'Fake Display Name, 123',
        'languageTypeId': '639-2%3AENG%40ISO',
        'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
        'scriptTypeId': '15924%3ALATN%40ISO'
    }
    request.cls.mixin.my_osid_object = OsidObject(object_name='TEST_OBJECT',
                                                  osid_object_map=obj_map)

    request.cls.test_file = open(os.path.join(ABS_PATH,
                                              '..',
                                              '..',
                                              '..',
                                              'tests',
                                              'fixtures',
                                              'assets',
                                              'draggable.green.dot.png'), 'rb')

    def class_tear_down():
        request.cls.test_file.close()

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def edx_utilities_mixin_test_fixture(request):
    stream = BytesIO()
    request.cls.tarfile = tarfile.open(fileobj=stream, mode='w')
    test_file = tarfile.TarInfo(name='/vertical/a-simple-path.xml')
    test_data = BytesIO('foo'.encode('utf-8'))
    request.cls.tarfile.addfile(test_file, test_data)


@pytest.mark.usefixtures('edx_utilities_mixin_class_fixture', 'edx_utilities_mixin_test_fixture')
class TestEdXUtilitiesMixin(object):
    def test_get_unique_name_works(self):
        assert self.mixin.get_unique_name(self.tarfile, 'a-simple-path', 'vertical', '/') == 'a-simple-path-1'

    def test_can_get_url_property(self):
        assert self.mixin.url == 'fake-display-name-123'

    def test_can_write_pretty_soup_to_tarfile(self):
        soup = BeautifulSoup('<vertical display_name="My hat" />', 'xml')
        assert '/vertical/my-hat.xml' not in self.tarfile.getnames()
        self.mixin.write_to_tarfile(self.tarfile, '/vertical/my-hat.xml', soup=soup)
        assert '/vertical/my-hat.xml' in self.tarfile.getnames()

    def test_can_write_unpretty_soup_to_tarfile(self):
        soup = BeautifulSoup('<vertical display_name="My hat" />', 'xml')
        assert '/vertical/my-hat.xml' not in self.tarfile.getnames()
        self.mixin.write_to_tarfile(self.tarfile, '/vertical/my-hat.xml', soup=soup, prettify=False)
        assert '/vertical/my-hat.xml' in self.tarfile.getnames()

    def test_can_write_file_to_tarfile(self):
        file_list = self.tarfile.getnames()
        assert 'green.dot.png' not in file_list
        self.mixin.write_to_tarfile(self.tarfile, '/green.dot.png', fileobj=self.test_file)
        file_list = self.tarfile.getnames()
        assert 'green.dot.png' in file_list

    def test_cannot_write_both_soup_and_file_to_tarfile(self):
        with pytest.raises(errors.IllegalState):
            self.mixin.write_to_tarfile(self.tarfile, '/foo.xml', soup='123', fileobj='123')

    def test_can_write_empty_directory_to_tarfile(self):
        file_list = self.tarfile.getnames()
        assert '/foo-directory' not in file_list
        self.mixin.write_to_tarfile(self.tarfile, '/foo-directory')
        file_list = self.tarfile.getnames()
        assert '/foo-directory' in file_list
