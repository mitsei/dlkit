import os
import pytest
import tarfile

from bs4 import BeautifulSoup
from copy import deepcopy
from six import BytesIO

from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.objects import OsidObject
from dlkit.records.repository.edx.edx_assets import *
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest
from dlkit.runtime.primitives import DataInputStream, DisplayText, Id

from ... import utilities

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))


def get_repository_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('REPOSITORY',
                                       implementation='TEST_SERVICE_FILESYSTEM',
                                       proxy=proxy)


class DummyParent(object):
    def __init__(self):
        self.url = 'a-fake-parent'
        self.display_name = DisplayText(display_text_map={
            'text': 'my name',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        })


@pytest.fixture(scope="class")
def edx_asset_content_class_fixture(request):
    obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
    request.cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                         osid_object_map=obj_map)
    request.cls.asset_content = edXAssetContentRecord(request.cls.osid_object)

    request.cls.test_file = open(os.path.join(ABS_PATH,
                                              '..',
                                              '..',
                                              '..',
                                              'tests',
                                              'fixtures',
                                              'assets',
                                              'draggable.green.dot.png'), 'rb')

    request.cls.rm = get_repository_manager()
    form = request.cls.rm.get_repository_form_for_create([])
    form.display_name = 'Test repo'
    request.cls.repo = request.cls.rm.create_repository(form)

    form = request.cls.repo.get_asset_form_for_create([])
    form.display_name = 'test asset'
    asset = request.cls.repo.create_asset(form)

    asset_content_type_list = []
    try:
        config = request.cls.repo._catalog._runtime.get_configuration()
        parameter_id = Id('parameter:assetContentRecordTypeForFiles@json')
        asset_content_type_list.append(
            config.get_value_by_parameter(parameter_id).get_type_value())
    except (AttributeError, KeyError, errors.NotFound):
        pass

    form = request.cls.repo.get_asset_content_form_for_create(asset.ident, asset_content_type_list)
    form.set_data(DataInputStream(request.cls.test_file))
    request.cls.repo.create_asset_content(form)

    request.cls.asset = request.cls.repo.get_asset(asset.ident)

    def class_tear_down():
        request.cls.test_file.close()
        for asset in request.cls.repo.get_assets():
            request.cls.repo.delete_asset(asset.ident)
        request.cls.rm.delete_repository(request.cls.repo.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def edx_asset_content_test_fixture(request):
    request.cls.stream = BytesIO()
    request.cls.tarfile = tarfile.open(fileobj=request.cls.stream, mode='w')


@pytest.mark.usefixtures('edx_asset_content_class_fixture', 'edx_asset_content_test_fixture')
class TestedXAssetContentRecord(object):
    """ NOTE: for these tests, assume ``TEST_SERVICE_FILESYSTEM`` in get_repository_manager()
              above, so the asset_content URL is something like /api/v1/repository..../stream"""
    def test_can_export_olx_for_html_asset_content(self):
        markup = """
<html>
    <head>
        <script src="{0}">fake script</script>
    </head>
    <body>
        <img src="{0}" />
        <a href="{0}" />
    </body>
</html>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Ahtml%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        expected_path = 'html/a-fake-parent.xml'
        expected_html_path = 'html/a-fake-parent.html'

        assert expected_path not in self.tarfile.getnames()
        assert expected_html_path not in self.tarfile.getnames()

        updated_path = asset_content.export_olx(self.tarfile,
                                                '',
                                                DummyParent())
        assert updated_path == 'html/a-fake-parent.xml'
        assert expected_path in self.tarfile.getnames()
        assert expected_html_path in self.tarfile.getnames()

        self.stream.seek(0)
        readable_tar = tarfile.open(fileobj=self.stream, mode='r')
        xml_doc = readable_tar.extractfile(expected_path)

        xml_soup = BeautifulSoup(xml_doc, 'xml')
        assert xml_soup.html is not None
        html_pointer = xml_soup.html
        assert 'display_name' in html_pointer.attrs
        assert html_pointer['display_name'] == 'my name'
        assert 'filename' in html_pointer.attrs
        assert html_pointer['filename'] == 'a-fake-parent'
        assert 'url_name' in html_pointer.attrs
        assert html_pointer['url_name'] == 'a-fake-parent'

        html_doc = readable_tar.extractfile(expected_html_path)
        html_soup = BeautifulSoup(html_doc, 'html5lib')
        assert 'display_name' in html_soup.html.attrs
        assert html_soup.html['display_name'] == 'my name'
        assert html_soup.script['src'] == '/static/stream'
        assert html_soup.img['src'] == '/static/stream'
        assert html_soup.a['href'] == '/static/stream'

    def test_can_export_olx_for_video_asset_content(self):
        markup = """
<video sub="{0}" youtube="{0}" youtube_id_1_0="{0}">
    <encoded_video url="{0}">
    </encoded_video>
</video>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Avideo%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        expected_path = 'video/a-fake-parent.xml'

        assert expected_path not in self.tarfile.getnames()

        updated_path = asset_content.export_olx(self.tarfile,
                                                '',
                                                DummyParent())
        assert updated_path == 'video/a-fake-parent.xml'
        assert expected_path in self.tarfile.getnames()

        self.stream.seek(0)
        readable_tar = tarfile.open(fileobj=self.stream, mode='r')
        xml_doc = readable_tar.extractfile(expected_path)

        xml_soup = BeautifulSoup(xml_doc, 'xml')
        assert xml_soup.video is not None
        video = xml_soup.video
        assert video['sub'] == '/static/stream'
        assert video['youtube'] == '/static/stream'
        assert video['youtube_id_1_0'] == '/static/stream'
        assert video.encoded_video['url'] == '/static/stream'

    def test_can_export_olx_for_problem_asset_content(self):
        markup = """
<problem>
    <drag_and_drop_input img="{0}">
        <draggable icon="{0}">
        </draggable>
    </drag_and_drop_input>
</problem>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Aproblem%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        expected_path = 'problem/a-fake-parent.xml'

        assert expected_path not in self.tarfile.getnames()

        updated_path = asset_content.export_olx(self.tarfile,
                                                '',
                                                DummyParent())
        assert updated_path == 'problem/a-fake-parent.xml'
        assert expected_path in self.tarfile.getnames()

        self.stream.seek(0)
        readable_tar = tarfile.open(fileobj=self.stream, mode='r')
        xml_doc = readable_tar.extractfile(expected_path)

        xml_soup = BeautifulSoup(xml_doc, 'xml')
        assert xml_soup.problem is not None
        problem = xml_soup.problem
        assert problem.draggable['icon'] == '/static/stream'
        assert problem.drag_and_drop_input['img'] == '/static/stream'

    def test_can_export_olx_for_discussion_asset_content(self):
        markup = """
<discussion display_name="for some problem">
</discussion>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Adiscussion%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        expected_path = 'discussion/a-fake-parent.xml'

        assert expected_path not in self.tarfile.getnames()

        updated_path = asset_content.export_olx(self.tarfile,
                                                '',
                                                DummyParent())
        assert updated_path == 'discussion/a-fake-parent.xml'
        assert expected_path in self.tarfile.getnames()

        self.stream.seek(0)
        readable_tar = tarfile.open(fileobj=self.stream, mode='r')
        xml_doc = readable_tar.extractfile(expected_path)

        xml_soup = BeautifulSoup(xml_doc, 'xml')
        assert xml_soup.discussion is not None

    def test_can_get_edxml_with_aws_urls_for_html_asset_content(self):
        markup = """
<html>
    <head>
        <script src="{0}">fake script</script>
    </head>
    <body>
        <img src="{0}" />
        <a href="{0}" />
    </body>
</html>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Ahtml%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        olx = asset_content.get_edxml_with_aws_urls()

        html_soup = BeautifulSoup(olx, 'html5lib')
        assert html_soup.html is not None
        assert '/api/v1/repository/repositories/' in html_soup.script['src']
        assert '/api/v1/repository/repositories/' in html_soup.img['src']
        assert '/api/v1/repository/repositories/' in html_soup.a['href']

    def test_can_get_edxml_with_aws_urls_for_video_asset_content(self):
        markup = """
<video sub="{0}" youtube="{0}" youtube_id_1_0="{0}">
    <encoded_video url="{0}">
    </encoded_video>
</video>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Avideo%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        olx = asset_content.get_edxml_with_aws_urls()

        xml_soup = BeautifulSoup(olx, 'xml')
        assert xml_soup.video is not None
        video = xml_soup.video
        assert '/api/v1/repository/repositories/' in video['sub']
        assert '/api/v1/repository/repositories/' in video['youtube']
        assert '/api/v1/repository/repositories/' in video['youtube_id_1_0']
        assert '/api/v1/repository/repositories/' in video.encoded_video['url']

    def test_can_get_edxml_with_aws_urls_for_problem_asset_content(self):
        markup = """
        <problem>
            <drag_and_drop_input img="{0}">
                <draggable icon="{0}">
                </draggable>
            </drag_and_drop_input>
        </problem>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Aproblem%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        olx = asset_content.get_edxml_with_aws_urls()

        xml_soup = BeautifulSoup(olx, 'xml')
        assert xml_soup.problem is not None
        problem = xml_soup.problem
        assert '/api/v1/repository/repositories/' in problem.draggable['icon']
        assert '/api/v1/repository/repositories/' in problem.drag_and_drop_input['img']

    def test_can_get_edxml_with_aws_urls_for_discussion_asset_content(self):
        markup = """
        <discussion display_name="for some problem">
        </discussion>""".format(str(self.asset.ident))
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['text'] = {
            'text': markup,
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['assignedRepositoryIds'] = [str(self.repo.ident)]
        obj_map['genusTypeId'] = 'fake.Genus%3Adiscussion%40ODL.MIT.EDU'
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.repo._catalog._runtime)
        asset_content = edXAssetContentRecord(osid_object)

        olx = asset_content.get_edxml_with_aws_urls()

        xml_soup = BeautifulSoup(olx, 'xml')
        assert xml_soup.discussion is not None
