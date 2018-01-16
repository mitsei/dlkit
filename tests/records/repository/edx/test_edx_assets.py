import os
import pytest
import tarfile

from bs4 import BeautifulSoup
from bson import ObjectId
from copy import deepcopy
from six import BytesIO

from dlkit.abstract_osid.osid import errors
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.objects import OsidObject
from dlkit.json_.osid.queries import OsidObjectQuery
from dlkit.records.repository.edx.edx_assets import *
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest
from dlkit.runtime.primitives import DataInputStream, DisplayText, Id, Type
from dlkit.records.registry import COMPOSITION_RECORD_TYPES,\
    COMPOSITION_GENUS_TYPES,\
    ASSET_RECORD_TYPES,\
    ASSET_CONTENT_RECORD_TYPES,\
    ASSET_CONTENT_GENUS_TYPES,\
    ASSESSMENT_RECORD_TYPES

from ... import utilities

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
                                       implementation='TEST_SERVICE_FILESYSTEM',
                                       proxy=proxy)


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
              above, so the asset_content URL is something like /api/v1/repository..../stream
              That is why all of the replacement URL assertions look for ``/static/stream``, since
              the record extension logic assumes the "filename" is the last part of the
              returned assetContent URL (``stream`` in this case).
    """
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


class TestedXAssetContentFormRecord(object):
    # Don't write new tests, since there are no non-inherited methods.
    # The tests should all be covered in osid.base_records.py tests
    pass


@pytest.fixture(scope="function")
def edx_asset_test_fixture(request):
    request.cls.stream = BytesIO()
    request.cls.tarball = tarfile.open(fileobj=request.cls.stream, mode='w')

    request.cls.rm = get_repository_manager()

    edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])
    edx_asset_content_record = Type(**ASSET_CONTENT_RECORD_TYPES['edx-asset-content-text-files'])
    edx_asset_content_genus = Type(**ASSET_CONTENT_GENUS_TYPES['html'])

    form = request.cls.rm.get_repository_form_for_create([])
    form.display_name = 'Test Repo 1'
    request.cls.repo_1 = request.cls.rm.create_repository(form)

    form = request.cls.rm.get_repository_form_for_create([])
    form.display_name = 'Test Repo 2'
    request.cls.repo_2 = request.cls.rm.create_repository(form)

    form = request.cls.repo_1.get_asset_form_for_create([edx_asset_record])
    form.display_name = 'Introduction to Python'
    request.cls.asset = request.cls.repo_1.create_asset(form)

    form = request.cls.repo_1.get_asset_content_form_for_create(request.cls.asset.ident, [edx_asset_content_record])
    form.set_text('<html><body><div>foo!</div></body></html>')
    form.set_genus_type(edx_asset_content_genus)
    request.cls.repo_1.create_asset_content(form)
    request.cls.asset = request.cls.repo_1.get_asset(request.cls.asset.ident)

    def test_tear_down():
        for repository in request.cls.rm.get_repositories():
            repository.use_unsequestered_composition_view()
            for asset in repository.get_assets():
                repository.delete_asset(asset.ident)
            while repository.get_compositions().available() > 0:
                for composition in repository.get_compositions():
                    try:
                        repository.delete_composition(composition.ident)
                    except errors.IllegalState:
                        pass
            request.cls.rm.delete_repository(repository.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures('edx_asset_test_fixture')
class TestedXAssetRecord(object):
    def test_can_clone_asset_to_new_repository(self):
        assert self.repo_2.get_assets().available() == 0

        new_asset = self.asset.clone_to(self.repo_2)

        assert self.repo_2.get_assets().available() == 1
        assert str(new_asset.ident) != str(self.asset.ident)
        assert new_asset._my_map['provenanceId'] == str(self.asset.ident)

    def test_cloning_asset_with_enclosed_assessment_also_clones_assessment(self):
        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])
        enclosure_record_type = Type(**ASSET_RECORD_TYPES['enclosure'])

        am = get_assessment_manager()
        bank_1 = am.get_bank(self.repo_1.ident)
        form = bank_1.get_assessment_form_for_create([])
        assessment = bank_1.create_assessment(form)

        create_form = self.repo_1.get_asset_form_for_create([edx_asset_record, enclosure_record_type])
        create_form.set_enclosed_object(assessment.ident)
        asset = self.repo_1.create_asset(create_form)

        bank_2 = am.get_bank(self.repo_2.ident)

        assert bank_2.get_assessments().available() == 0

        new_asset = asset.clone_to(self.repo_2)

        assert bank_2.get_assessments().available() == 1

        assert new_asset._my_map['enclosedObjectId'] != asset._my_map['enclosedObjectId']

        for bank in am.get_banks():
            for assessment in bank.get_assessments():
                bank.delete_assessment(assessment.ident)
            am.delete_bank(bank.ident)

    def test_cloning_asset_with_enclosed_item_also_clones_item(self):
        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])
        enclosure_record_type = Type(**ASSET_RECORD_TYPES['enclosure'])

        am = get_assessment_manager()
        bank_1 = am.get_bank(self.repo_1.ident)
        form = bank_1.get_item_form_for_create([])
        item = bank_1.create_item(form)

        create_form = self.repo_1.get_asset_form_for_create([edx_asset_record, enclosure_record_type])
        create_form.set_enclosed_object(item.ident)
        asset = self.repo_1.create_asset(create_form)

        bank_2 = am.get_bank(self.repo_2.ident)

        assert bank_2.get_items().available() == 0

        new_asset = asset.clone_to(self.repo_2)

        assert bank_2.get_items().available() == 1

        assert new_asset._my_map['enclosedObjectId'] != asset._my_map['enclosedObjectId']

        for bank in am.get_banks():
            for item in bank.get_items():
                bank.delete_item(item.ident)
            am.delete_bank(bank.ident)

    def test_can_export_olx(self):
        result = self.asset.export_olx(self.tarball, '')

        self.stream.seek(0)
        reader = tarfile.open(fileobj=self.stream, mode='r')

        assert reader.getnames() == ['html/introduction-to-python.html',
                                     'html/introduction-to-python.xml']

        assert result == ['html/introduction-to-python.xml']

    def test_export_olx_handles_identical_display_names(self):
        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])
        edx_asset_content_record = Type(**ASSET_CONTENT_RECORD_TYPES['edx-asset-content-text-files'])
        edx_asset_content_genus = Type(**ASSET_CONTENT_GENUS_TYPES['html'])
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])

        form = self.repo_1.get_asset_form_for_create([edx_asset_record])
        form.display_name = 'Introduction to Python'
        asset_2 = self.repo_1.create_asset(form)

        form = self.repo_1.get_asset_content_form_for_create(asset_2.ident, [edx_asset_content_record])
        form.set_text('<html><body><div>foo2!</div></body></html>')
        form.set_genus_type(edx_asset_content_genus)
        self.repo_1.create_asset_content(form)
        asset_2 = self.repo_1.get_asset(asset_2.ident)

        form = self.repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical = self.repo_1.create_composition(form)

        self.repo_1.add_asset(self.asset.ident, vertical.ident)
        self.repo_1.add_asset(asset_2.ident, vertical.ident)

        vertical = self.repo_1.get_composition(vertical.ident)

        vertical.export_olx(self.tarball, '')

        self.stream.seek(0)
        reader = tarfile.open(fileobj=self.stream, mode='r')

        included_files = reader.getnames()
        assert len(included_files) == 5

        for expected_file in ['html/introduction-to-python.html',
                              'html/introduction-to-python.xml',
                              'html/introduction-to-python-1.html',
                              'html/introduction-to-python-1.xml',
                              'vertical/a-vertical.xml']:
            assert expected_file in included_files

        html_1 = reader.extractfile('html/introduction-to-python.html')
        assert 'foo!' in html_1.read().decode('utf-8')

        html_2 = reader.extractfile('html/introduction-to-python-1.html')
        assert 'foo2!' in html_2.read().decode('utf-8')

        vertical_xml = reader.extractfile('vertical/a-vertical.xml').read().decode('utf-8')
        assert '"introduction-to-python"' in vertical_xml
        assert '"introduction-to-python-1"' in vertical_xml

    def test_can_export_standalone_olx(self):
        filename, olx = self.asset.export_standalone_olx()

        assert 'Introduction_to_Python' in filename
        assert '.tar.gz' in filename

        reader = tarfile.open(fileobj=olx, mode='r')

        assert reader.getnames() == ['html/introduction-to-python.html',
                                     'html/introduction-to-python.xml']

    def test_can_get_learning_objective_ids(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['learningObjectiveIds'] = ['package.One%3A1%40ODL.MIT.EDU',
                                           'package.Two%3A2%40ODL.MIT.EDU']
        osid_object = OsidObject(object_name='ASSET_CONTENT',
                                 osid_object_map=obj_map)
        asset = edXAssetRecord(osid_object)

        result = asset.get_learning_objective_ids()
        assert isinstance(result, IdList)
        assert result.available() == 2
        assert str(next(result)) == 'package.One%3A1%40ODL.MIT.EDU'
        assert str(next(result)) == 'package.Two%3A2%40ODL.MIT.EDU'


class QueryWrapper(OsidObjectQuery):
    def __init__(self, runtime=None):
        self._all_supported_record_type_ids = []
        super(QueryWrapper, self).__init__(runtime)


@pytest.fixture(scope="function")
def edx_asset_query_test_fixture(request):
    request.cls.osid_query = QueryWrapper()
    request.cls.query = edXAssetQueryRecord(request.cls.osid_query)


@pytest.mark.usefixtures('edx_asset_query_test_fixture')
class TestedXAssetQueryRecord(object):
    def test_match_asset_content_genus_type(self):
        assert self.query._my_osid_query._query_terms == {}

        self.query.match_asset_content_genus_type(Type('fake%3Agenus%40MIT'), True)
        assert 'assetContents.0.genusTypeId' in self.query._my_osid_query._query_terms
        assert self.query._my_osid_query._query_terms['assetContents.0.genusTypeId'] == {'$in': ['fake%3Agenus%40MIT']}

    def test_clear_match_asset_content_genus_type(self):
        self.query.match_asset_content_genus_type(Type('fake%3Agenus%40MIT'), True)
        assert 'assetContents.0.genusTypeId' in self.query._my_osid_query._query_terms
        assert self.query._my_osid_query._query_terms['assetContents.0.genusTypeId'] == {'$in': ['fake%3Agenus%40MIT']}

        self.query.clear_match_asset_content_genus_type()

        assert self.query._my_osid_query._query_terms == {}

    def test_match_learning_objective(self):
        assert self.query._my_osid_query._query_terms == {}

        self.query.match_learning_objective(Id('fake%3Aidentifier%40MIT'), True)
        assert 'learningObjectiveIds' in self.query._my_osid_query._query_terms
        assert self.query._my_osid_query._query_terms['learningObjectiveIds'] == {'$in': ['fake%3Aidentifier%40MIT']}

    def test_clear_match_learning_objective(self):
        self.query.match_learning_objective(Id('fake%3Aidentifier%40MIT'), True)
        assert 'learningObjectiveIds' in self.query._my_osid_query._query_terms
        assert self.query._my_osid_query._query_terms['learningObjectiveIds'] == {'$in': ['fake%3Aidentifier%40MIT']}

        self.query.clear_match_learning_objective()

        assert self.query._my_osid_query._query_terms == {}

    def test_match_any_learning_objective(self):
        assert self.query._my_osid_query._query_terms == {}

        self.query.match_any_learning_objective(True)
        assert 'learningObjectiveIds' in self.query._my_osid_query._query_terms
        assert self.query._my_osid_query._query_terms['learningObjectiveIds'] == {
            '$nin': [[], ['']],
            '$exists': 'true'
        }

    def test_clear_learning_objective_terms(self):
        self.query.match_any_learning_objective(True)
        assert 'learningObjectiveIds' in self.query._my_osid_query._query_terms
        assert self.query._my_osid_query._query_terms['learningObjectiveIds'] == {
            '$nin': [[], ['']],
            '$exists': 'true'
        }

        self.query.clear_learning_objective_terms()

        assert self.query._my_osid_query._query_terms == {}

    def test_match_composition_descendants(self):
        rm = get_repository_manager()

        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])

        form = rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo'
        repo = rm.create_repository(form)

        form = repo.get_asset_form_for_create([edx_asset_record])
        form.display_name = 'Introduction to Python'
        asset = repo.create_asset(form)

        form = repo.get_composition_form_for_create([])
        child = repo.create_composition(form)

        repo.add_asset(asset.ident, child.ident)

        form = repo.get_composition_form_for_create([])
        form.set_children([child.ident])
        composition = repo.create_composition(form)

        query = QueryWrapper(runtime=repo._catalog._runtime)
        query = edXAssetQueryRecord(query)

        assert '_id' not in query._my_osid_query._query_terms
        query.match_composition_descendants(composition.ident, repo.ident, True)

        assert '_id' in query._my_osid_query._query_terms
        assert query._my_osid_query._query_terms['_id'] == {
            '$in': [ObjectId(asset.ident.identifier)]
        }

        for asset in repo.get_assets():
            repo.delete_asset(asset.ident)
        for composition in repo.get_compositions():
            repo.delete_composition(composition.ident)
        rm.delete_repository(repo.ident)

    def test_clear_match_composition_descendants(self):
        rm = get_repository_manager()

        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])

        form = rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo'
        repo = rm.create_repository(form)

        form = repo.get_asset_form_for_create([edx_asset_record])
        form.display_name = 'Introduction to Python'
        asset = repo.create_asset(form)

        form = repo.get_composition_form_for_create([])
        child = repo.create_composition(form)

        repo.add_asset(asset.ident, child.ident)

        form = repo.get_composition_form_for_create([])
        form.set_children([child.ident])
        composition = repo.create_composition(form)

        query = QueryWrapper(runtime=repo._catalog._runtime)
        query = edXAssetQueryRecord(query)

        query.match_composition_descendants(composition.ident, repo.ident, True)

        assert '_id' in query._my_osid_query._query_terms
        assert query._my_osid_query._query_terms['_id'] == {
            '$in': [ObjectId(asset.ident.identifier)]
        }

        query.clear_match_composition_descendants()

        assert '_id' not in query._my_osid_query._query_terms

        for asset in repo.get_assets():
            repo.delete_asset(asset.ident)
        for composition in repo.get_compositions():
            repo.delete_composition(composition.ident)
        rm.delete_repository(repo.ident)
