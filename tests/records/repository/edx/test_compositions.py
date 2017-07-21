import datetime
import json
import pytest
import tarfile

from bson import ObjectId
from copy import deepcopy
from six import BytesIO

from dlkit.abstract_osid.assessment.objects import Item
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.repository.objects import Asset, Composition
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.json_.osid.queries import OsidObjectQuery
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type
from dlkit.records.registry import COMPOSITION_RECORD_TYPES,\
    COMPOSITION_GENUS_TYPES,\
    ASSET_RECORD_TYPES,\
    ASSET_CONTENT_RECORD_TYPES,\
    ASSET_CONTENT_GENUS_TYPES,\
    ASSESSMENT_RECORD_TYPES
from dlkit.records.repository.edx.compositions import *
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.primordium import Id
from dlkit.runtime.proxy_example import SimpleRequest

from ... import utilities


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


def get_repository_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('REPOSITORY',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


class DummyThing(object):
    @valid_for(['chapter'])
    def chapter_method(self):
        return True


@pytest.fixture(scope="class")
def decorator_class_fixture(request):
    obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
    request.cls.dummy_object = OsidObject(object_name='TEST_OBJECT',
                                          osid_object_map=obj_map)


@pytest.mark.usefixtures('decorator_class_fixture')
class TestDecorator(object):
    def test_valid_for_works_for_forms(self):
        test_form = DummyThing()
        test_form.my_osid_object_form = self.dummy_object
        test_form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Achapter%40ODL.MIT.EDU'

        assert test_form.chapter_method()

        test_form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Avertical%40ODL.MIT.EDU'

        with pytest.raises(errors.IllegalState):
            test_form.chapter_method()

    def test_valid_form_works_for_objects(self):
        test_object = DummyThing()
        test_object.my_osid_object = self.dummy_object
        test_object.my_osid_object._my_map['genusTypeId'] = 'fake.Genus%3Achapter%40ODL.MIT.EDU'

        assert test_object.chapter_method()

        test_object.my_osid_object._my_map['genusTypeId'] = 'fake.Genus%3Avertical%40ODL.MIT.EDU'

        with pytest.raises(errors.IllegalState):
            test_object.chapter_method()


@pytest.fixture(scope="function")
def edx_composition_form_test_fixture(request):
    request.cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
    request.cls.osid_object_form._authority = 'TESTING.MIT.EDU'
    request.cls.osid_object_form._namespace = 'records.Testing'
    request.cls.osid_object_form._my_map = {
        'texts': {
            'fileName': {
                'text': ''
            }
        }
    }


@pytest.mark.usefixtures('edx_composition_form_test_fixture')
class TestEdXCompositionFormRecord(object):
    def test_can_set_file_name(self):
        """Tests set_file_name"""
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Acourse%40ODL.MIT.EDU'
        assert form.my_osid_object_form._my_map['texts']['fileName']['text'] == ''
        form.set_file_name('foo')
        assert form.my_osid_object_form._my_map['texts']['fileName']['text'] == 'course.xml'

        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU',
                           'fake.Genus%3Avertical%40ODL.MIT.EDU',
                           'fake.Genus%3Asplit_test%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type
            assert form.my_osid_object_form._my_map['texts']['fileName']['text'] == ''
            form.set_file_name('foo.xml')
            assert form.my_osid_object_form._my_map['texts']['fileName']['text'] == 'foo.xml'

    def test_can_clear_file_name(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        for genus_type in ['fake.Genus%3Acourse%40ODL.MIT.EDU',
                           'fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU',
                           'fake.Genus%3Avertical%40ODL.MIT.EDU',
                           'fake.Genus%3Asplit_test%40ODL.MIT.EDU']:
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type
            form.set_file_name('foo.xml')
            assert form.my_osid_object_form._my_map['texts']['fileName']['text'] != ''
            form.clear_file_name()
            assert form.my_osid_object_form._my_map['texts']['fileName']['text'] == ''

    def test_chapter_sequential_can_set_start_date(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type
            future_date = datetime.datetime.utcnow() + datetime.timedelta(days=4)
            start_date = DateTime(year=future_date.year,
                                  month=future_date.month,
                                  day=future_date.day,
                                  hour=future_date.hour,
                                  minute=future_date.minute,
                                  second=future_date.second,
                                  microsecond=future_date.microsecond)

            assert isinstance(form.my_osid_object_form._my_map['startDate'],
                              DateTime)
            assert start_date != form.my_osid_object_form._my_map['startDate']

            form.set_start_date(start_date)
            assert form.my_osid_object_form._my_map['startDate'] == start_date

    def test_chapter_sequential_can_clear_start_date(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type

            default_start_date = form._start_date_metadata['default_date_time_values'][0]
            default_start_date = DateTime(year=default_start_date.year,
                                          month=default_start_date.month,
                                          day=default_start_date.day,
                                          hour=default_start_date.hour,
                                          minute=default_start_date.minute,
                                          second=default_start_date.second,
                                          microsecond=default_start_date.microsecond)
            future_date = datetime.datetime.utcnow() + datetime.timedelta(days=4)
            start_date = DateTime(year=future_date.year,
                                  month=future_date.month,
                                  day=future_date.day,
                                  hour=future_date.hour,
                                  minute=future_date.minute,
                                  second=future_date.second,
                                  microsecond=future_date.microsecond)
            form.set_start_date(start_date)
            assert form.my_osid_object_form._my_map['startDate'] == start_date
            form.clear_start_date()
            assert form.my_osid_object_form._my_map['startDate'] == default_start_date

    def test_chapter_sequential_can_set_visible_to_students(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type

            assert isinstance(form.my_osid_object_form._my_map['visibleToStudents'],
                              bool)
            assert form.my_osid_object_form._my_map['visibleToStudents']
            form.set_visible_to_students(False)
            assert not form.my_osid_object_form._my_map['visibleToStudents']

    def test_chapter_sequential_can_clear_visible_to_students(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type

            form.set_visible_to_students(False)
            assert not form.my_osid_object_form._my_map['visibleToStudents']
            form.clear_visible_to_students()
            assert form.my_osid_object_form._my_map['visibleToStudents']

    def test_course_can_set_org(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Acourse%40ODL.MIT.EDU'
        assert form.my_osid_object_form._my_map['texts']['org']['text'] == ''
        form.set_org('FooX')
        assert form.my_osid_object_form._my_map['texts']['org']['text'] == 'FooX'

    def test_course_can_clear_org(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Acourse%40ODL.MIT.EDU'
        form.set_org('FooX')
        assert form.my_osid_object_form._my_map['texts']['org']['text'] == 'FooX'
        form.clear_org()
        assert form.my_osid_object_form._my_map['texts']['org']['text'] == ''

    def test_vertical_can_set_draft(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Avertical%40ODL.MIT.EDU'
        assert isinstance(form.my_osid_object_form._my_map['draft'],
                          bool)
        assert not form.my_osid_object_form._my_map['draft']
        form.set_draft(True)
        assert form.my_osid_object_form._my_map['draft']

    def test_vertical_can_clear_draft(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Avertical%40ODL.MIT.EDU'
        form.set_draft(True)
        assert form.my_osid_object_form._my_map['draft']
        form.clear_draft()
        assert not form.my_osid_object_form._my_map['draft']

    def test_split_test_can_set_user_partition_id(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Asplit_test%40ODL.MIT.EDU'
        assert form.my_osid_object_form._my_map['texts']['userPartitionId']['text'] == ''
        form.set_user_partition_id('foo123')
        assert form.my_osid_object_form._my_map['texts']['userPartitionId']['text'] == 'foo123'

    def test_split_test_can_clear_user_partition_id(self):
        form = EdXCompositionFormRecord(self.osid_object_form)
        form.my_osid_object_form._my_map['genusTypeId'] = 'fake.Genus%3Asplit_test%40ODL.MIT.EDU'
        form.set_user_partition_id('foo123')
        assert form.my_osid_object_form._my_map['texts']['userPartitionId']['text'] == 'foo123'
        form.clear_user_partition_id()
        assert form.my_osid_object_form._my_map['texts']['userPartitionId']['text'] == ''

    def test_chapter_sequential_vertical_split_test_can_set_learning_objective_ids(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU',
                           'fake.Genus%3Avertical%40ODL.MIT.EDU',
                           'fake.Genus%3Asplit_test%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type
            assert form.my_osid_object_form._my_map['learningObjectiveIds'] == []
            form.set_learning_objective_ids([1, 2, 3])
            assert form.my_osid_object_form._my_map['learningObjectiveIds'] == ['1', '2', '3']

    def test_chapter_sequential_vertical_split_test_can_clear_learning_objective_ids(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU',
                           'fake.Genus%3Avertical%40ODL.MIT.EDU',
                           'fake.Genus%3Asplit_test%40ODL.MIT.EDU']:
            form = EdXCompositionFormRecord(self.osid_object_form)
            form.my_osid_object_form._my_map['genusTypeId'] = genus_type
            form.set_learning_objective_ids([1, 2, 3])
            assert form.my_osid_object_form._my_map['learningObjectiveIds'] == ['1', '2', '3']
            form.clear_learning_objective_ids()
            assert form.my_osid_object_form._my_map['learningObjectiveIds'] == []


class QueryWrapper(OsidObjectQuery):
    def __init__(self, runtime=None):
        self._all_supported_record_type_ids = []
        super(QueryWrapper, self).__init__(runtime)


@pytest.fixture(scope="function")
def edx_composition_query_test_fixture(request):
    request.cls.osid_query = QueryWrapper()
    request.cls.composition_query = EdXCompositionQueryRecord(request.cls.osid_query)


@pytest.mark.usefixtures('edx_composition_query_test_fixture')
class TestEdXCompositionQueryRecord(object):
    def test_can_match_learning_objective(self):
        assert self.composition_query._my_osid_query._query_terms == {}

        self.composition_query.match_learning_objective('foo', True)
        assert 'learningObjectiveIds' in self.composition_query._my_osid_query._query_terms
        assert self.composition_query._my_osid_query._query_terms['learningObjectiveIds'] == {'$in': ['foo']}

    def test_can_clear_match_learning_objective(self):
        self.composition_query.match_learning_objective('foo', True)
        assert 'learningObjectiveIds' in self.composition_query._my_osid_query._query_terms
        assert self.composition_query._my_osid_query._query_terms['learningObjectiveIds'] == {'$in': ['foo']}

        self.composition_query.clear_match_learning_objective()
        assert self.composition_query._my_osid_query._query_terms == {}

    def test_match_any_learning_objective(self):
        assert self.composition_query._my_osid_query._query_terms == {}

        self.composition_query.match_any_learning_objective(True)
        assert 'learningObjectiveIds' in self.composition_query._my_osid_query._query_terms
        assert self.composition_query._my_osid_query._query_terms['learningObjectiveIds'] == {
            '$nin': [[], ['']],
            '$exists': 'true'
        }

    def test_clear_learning_objective_terms(self):
        self.composition_query.match_any_learning_objective(True)
        assert 'learningObjectiveIds' in self.composition_query._my_osid_query._query_terms
        assert self.composition_query._my_osid_query._query_terms['learningObjectiveIds'] == {
            '$nin': [[], ['']],
            '$exists': 'true'
        }

        self.composition_query.clear_learning_objective_terms()
        assert self.composition_query._my_osid_query._query_terms == {}

    def test_match_composition_descendants(self):
        rm = get_repository_manager()
        form = rm.get_repository_form_for_create([])
        form.display_name = 'test repo'
        repo = rm.create_repository(form)

        composition_id = Id('package.Resource%3A000000000000000000000000%40ODL.MIT.EDU')

        query = QueryWrapper(runtime=rm._provider_manager._runtime)
        composition_query = EdXCompositionQueryRecord(query)

        assert '_id' not in composition_query._my_osid_query._query_terms
        composition_query.match_composition_descendants(composition_id, repo.ident, True)

        assert '_id' in composition_query._my_osid_query._query_terms
        assert composition_query._my_osid_query._query_terms['_id'] == {
            '$in': [ObjectId('000000000000000000000000')]
        }

        rm.delete_repository(repo.ident)

    def test_clear_match_composition_descendants(self):
        rm = get_repository_manager()
        form = rm.get_repository_form_for_create([])
        form.display_name = 'test repo'
        repo = rm.create_repository(form)

        composition_id = Id('package.Resource%3A000000000000000000000000%40ODL.MIT.EDU')

        query = QueryWrapper(runtime=rm._provider_manager._runtime)
        composition_query = EdXCompositionQueryRecord(query)

        composition_query.match_composition_descendants(composition_id, repo.ident, True)

        assert '_id' in composition_query._my_osid_query._query_terms
        assert composition_query._my_osid_query._query_terms['_id'] == {
            '$in': [ObjectId('000000000000000000000000')]
        }

        composition_query.clear_match_composition_descendants()

        assert '_id' not in composition_query._my_osid_query._query_terms

        rm.delete_repository(repo.ident)


@pytest.fixture(scope="function")
def edx_composition_test_fixture(request):
    request.cls.obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
    request.cls.rm = get_repository_manager()

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


@pytest.mark.usefixtures('edx_composition_test_fixture')
class TestEdXCompositionRecord(object):
    def _set_up_simple_structure(self):
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])
        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])
        edx_asset_content_record = Type(**ASSET_CONTENT_RECORD_TYPES['edx-asset-content-text-files'])
        edx_asset_content_genus = Type(**ASSET_CONTENT_GENUS_TYPES['html'])

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo'
        test_repo = self.rm.create_repository(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        self.vertical = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A (non-) vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_sequestered(True)
        sequestered_vertical = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A sequential!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['sequential']))
        form.set_file_name('sequential/a-sequential.xml')
        form.set_children([self.vertical.ident, sequestered_vertical.ident])
        sequential = test_repo.create_composition(form)

        form = test_repo.get_asset_form_for_create([edx_asset_record])
        form.display_name = 'Introduction to Python'
        asset = test_repo.create_asset(form)

        form = test_repo.get_asset_content_form_for_create(asset.ident, [edx_asset_content_record])
        form.set_text('<html><body><div>foo!</div></body></html>')
        form.set_genus_type(edx_asset_content_genus)
        test_repo.create_asset_content(form)
        self.asset = test_repo.get_asset(asset.ident)

        test_repo.add_asset(self.asset.ident, sequestered_vertical.ident)

        return sequential

    def test_chapter_and_sequential_can_get_start_date(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU']:
            utcnow = DateTime.utcnow()
            self.obj_map['startDate'] = utcnow
            self.obj_map['genusTypeId'] = genus_type

            osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=self.obj_map,
                                     runtime=self.rm._provider_manager._runtime)
            composition = EdXCompositionRecord(osid_object)

            result = composition.start_date
            assert isinstance(result, DateTime)
            assert result == utcnow

    def test_can_get_filename(self):
        for genus_type in ['fake.Genus%3Acourse40ODL.MIT.EDU',
                           'fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU',
                           'fake.Genus%3Avertical%40ODL.MIT.EDU',
                           'fake.Genus%3Asplit_test%40ODL.MIT.EDU']:
            obj_map = deepcopy(self.obj_map)
            obj_map['texts'] = {
                'fileName': {
                    'text': 'foo-{0}.xml'.format(genus_type),
                    'languageTypeId': '639-2%3AENG%40ISO',
                    'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                    'scriptTypeId': '15924%3ALATN%40ISO'
                }
            }
            obj_map['genusTypeId'] = genus_type

            osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=obj_map,
                                     runtime=self.rm._provider_manager._runtime)
            composition = EdXCompositionRecord(osid_object)
            assert isinstance(composition.filename, DisplayText)
            assert composition.filename.text == 'foo-{0}.xml'.format(genus_type)

    def test_chapter_and_sequential_can_get_visible_to_students(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU']:
            self.obj_map['visibleToStudents'] = False
            self.obj_map['genusTypeId'] = genus_type

            osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=self.obj_map,
                                     runtime=self.rm._provider_manager._runtime)
            composition = EdXCompositionRecord(osid_object)

            result = composition.visible_to_students
            assert isinstance(result, bool)
            assert not result

    def test_vertical_can_get_draft(self):
        self.obj_map['draft'] = False
        self.obj_map['genusTypeId'] = 'fake.Genus%3Avertical%40ODL.MIT.EDU'

        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=self.obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        composition = EdXCompositionRecord(osid_object)

        result = composition.draft
        assert isinstance(result, bool)
        assert not result

    def test_course_can_get_org(self):
        self.obj_map['texts'] = {
            'org': {
                'text': 'FooX',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        }
        self.obj_map['genusTypeId'] = 'fake.Genus%3Acourse%40ODL.MIT.EDU'

        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=self.obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        composition = EdXCompositionRecord(osid_object)

        result = composition.org
        assert isinstance(result, DisplayText)
        assert result.text == 'FooX'

    def test_split_test_can_get_user_partition_id(self):
        self.obj_map['texts'] = {
            'userPartitionId': {
                'text': '12345',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        }
        self.obj_map['genusTypeId'] = 'fake.Genus%3Asplit_test%40ODL.MIT.EDU'

        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=self.obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        composition = EdXCompositionRecord(osid_object)

        result = composition.user_partition_id
        assert isinstance(result, DisplayText)
        assert result.text == '12345'

    def test_split_test_can_get_group_id_to_child(self):
        """ At a minimum need a course composition parent and two children to the split test

            course composition
                    |
            split_test composition
                |           |
            vertical     vertical

        And the expected output is a URL-safe (&quot; instead of ") JSON string, of this object
            {
                0: "i4x://<org>/<course-name-slug>/<child-tag>/<child-name-slug>,
                1: "i4x://<org>/<course-name-slug>/<tag>/<child-name-slug>
            }
        """
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo'
        test_repo = self.rm.create_repository(form)

        # start by making the verticals, so that when we set children, we have the IDs available
        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical 1!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical-1.xml')
        vertical_1 = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical 2!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical-2.xml')
        vertical_2 = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A split_test!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['split_test']))
        form.set_file_name('split_test/a-split-test.xml')
        form.set_children([vertical_1.ident, vertical_2.ident])
        split_test = test_repo.create_composition(form)

        null_result = split_test.group_id_to_child
        assert null_result == ''  # because not attached to a course

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = '6.001, 2017_Fall'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['course']))
        form.set_org('FooX')
        form.set_children([split_test.ident])
        course = test_repo.create_composition(form)

        result = split_test.group_id_to_child
        expected_result = {
            0: 'i4x://FooX/6001 2017_Fall/vertical/a-vertical-1',
            1: 'i4x://FooX/6001 2017_Fall/vertical/a-vertical-2'
        }
        assert result == json.dumps(expected_result).replace('"', '&quot;')

    def test_non_course_can_get_learning_objective_ids(self):
        for genus_type in ['fake.Genus%3Achapter%40ODL.MIT.EDU',
                           'fake.Genus%3Asequential%40ODL.MIT.EDU',
                           'fake.Genus%3Avertical%40ODL.MIT.EDU',
                           'fake.Genus%3Asplit_test%40ODL.MIT.EDU']:
            obj_map = deepcopy(self.obj_map)
            obj_map['learningObjectiveIds'] = ['package.One%3A1%40ODL.MIT.EDU',
                                               'package.Two%3A2%40ODL.MIT.EDU']
            obj_map['genusTypeId'] = genus_type

            osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=obj_map,
                                     runtime=self.rm._provider_manager._runtime)
            composition = EdXCompositionRecord(osid_object)
            result = composition.learning_objective_ids
            assert isinstance(result, IdList)
            assert result.available() == 2
            assert str(next(result)) == 'package.One%3A1%40ODL.MIT.EDU'
            assert str(next(result)) == 'package.Two%3A2%40ODL.MIT.EDU'

    def test_can_get_assets(self):
        """
        Set up a container with two assets, one enclosing an assessment or item, and the other a regular asset
        :return:
        """
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])
        edx_asset_record = Type(**ASSET_RECORD_TYPES['edx-asset'])
        edx_asset_content_record = Type(**ASSET_CONTENT_RECORD_TYPES['edx-asset-content-text-files'])
        simple_assessment_record = Type(**ASSESSMENT_RECORD_TYPES['simple-child-sequencing'])

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo'
        test_repo = self.rm.create_repository(form)
        am = get_assessment_manager()
        test_bank = am.get_bank(test_repo.ident)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical = test_repo.create_composition(form)

        form = test_repo.get_asset_form_for_create([edx_asset_record])
        asset = test_repo.create_asset(form)

        form = test_repo.get_asset_content_form_for_create(asset.ident, [edx_asset_content_record])
        form.set_text('<html><body><div>foo!</div></body></html>')
        test_repo.create_asset_content(form)
        asset = test_repo.get_asset(asset.ident)

        test_repo.add_asset(asset.ident, vertical.ident)

        form = test_bank.get_item_form_for_create([])
        item = test_bank.create_item(form)

        test_repo.add_asset(item.ident, vertical.ident)

        form = test_bank.get_assessment_form_for_create([simple_assessment_record])
        assessment = test_bank.create_assessment(form)

        form = test_bank.get_item_form_for_create([])
        item_2 = test_bank.create_item(form)

        test_bank.add_item(assessment.ident, item_2.ident)

        test_repo.add_asset(assessment.ident, vertical.ident)

        result = vertical.assets

        assert isinstance(result, list)
        assert len(result) == 3

        first_result = result[0]
        assert isinstance(first_result, Asset)
        assert str(first_result.ident) == str(asset.ident)

        second_result = result[1]
        assert isinstance(second_result, Item)
        assert str(second_result.ident) == str(item.ident)

        third_result = result[2]
        assert isinstance(third_result, Item)
        assert str(third_result.ident) == str(item_2.ident)

        for assessment in test_bank.get_assessments():
            test_bank.delete_assessment(assessment.ident)
        for item in test_bank.get_items():
            test_bank.delete_item(item.ident)
        am.delete_bank(test_bank.ident)

    def test_can_get_all_children(self):
        """
        Returns all children compositions or, if the child composition is sequestered, its assets
        :return:
        """
        sequential = self._set_up_simple_structure()

        result = sequential.all_children()

        assert isinstance(result, list)
        assert len(result) == 2

        assert isinstance(result[0], tuple)
        assert isinstance(result[1], tuple)

        assert len(result[0]) == 2
        assert len(result[1]) == 2

        assert isinstance(result[0][0], Composition)
        assert isinstance(result[0][1], bool)
        assert isinstance(result[1][0], Asset)
        assert isinstance(result[1][1], bool)

        assert str(result[0][0].ident) == str(self.vertical.ident)
        assert result[0][1]
        assert str(result[1][0].ident) == str(self.asset.ident)
        assert not result[1][1]

    def test_can_clone_to_new_repo(self):
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo 1'
        test_repo_1 = self.rm.create_repository(form)

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo 2'
        test_repo_2 = self.rm.create_repository(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical = test_repo_1.create_composition(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A sequential!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['sequential']))
        form.set_file_name('sequential/a-sequential.xml')
        form.set_children([vertical.ident])
        sequential = test_repo_1.create_composition(form)

        form = test_repo_2.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A chapter!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['chapter']))
        form.set_file_name('chapter/a-chapter.xml')
        form.set_children([sequential.ident])
        chapter = test_repo_2.create_composition(form)

        assert test_repo_2.get_compositions().available() == 1
        assert chapter.get_child_ids().available() == 1
        assert str(next(chapter.get_child_ids())) == str(sequential.ident)

        updated_sequential = sequential.clone_to(test_repo_2, chapter)

        assert updated_sequential._my_map['provenanceId'] == str(sequential.ident)

        assert test_repo_2.get_compositions().available() == 2
        assert str(updated_sequential.ident) != str(sequential.ident)

        chapter = test_repo_2.get_composition(chapter.ident)
        assert chapter.get_child_ids().available() == 1
        assert str(next(chapter.get_child_ids())) == str(updated_sequential.ident)

    def test_can_export_olx(self):
        # This is a really slimmed down test and should probably include more of the branching logic
        sequential = self._set_up_simple_structure()

        olx = BytesIO()
        tarball = tarfile.open(fileobj=olx, mode='w')

        sequential.export_olx(tarball, '')

        olx.seek(0)
        tarball_reader = tarfile.open(fileobj=olx, mode='r')
        included_files = tarball_reader.getnames()

        assert 'sequential/a-sequential.xml' in included_files
        assert 'vertical/a-vertical.xml' in included_files
        assert 'html/introduction-to-python.xml' in included_files
        assert 'html/introduction-to-python.html' in included_files

    def test_export_olx_handles_identical_display_names(self):
        """The method should make sure that the output file name is unique, i.e. if you have
             two verticals both having displayName "Introduction", there should be two
             files output, with the parent sequentials pointing to the appropriate vertical.
        """
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo 1'
        test_repo_1 = self.rm.create_repository(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical_1 = test_repo_1.create_composition(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical_2 = test_repo_1.create_composition(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A sequential!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['sequential']))
        form.set_file_name('sequential/a-sequential.xml')
        form.set_children([vertical_1.ident])
        sequential_1 = test_repo_1.create_composition(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A sequential!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['sequential']))
        form.set_file_name('sequential/a-sequential.xml')
        form.set_children([vertical_2.ident])
        sequential_2 = test_repo_1.create_composition(form)

        form = test_repo_1.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A chapter!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['chapter']))
        form.set_file_name('chapter/a-chapter.xml')
        form.set_children([sequential_1.ident, sequential_2.ident])
        chapter = test_repo_1.create_composition(form)

        olx = BytesIO()
        tarball = tarfile.open(fileobj=olx, mode='w')

        chapter.export_olx(tarball, '')

        olx.seek(0)
        tarball_reader = tarfile.open(fileobj=olx, mode='r')
        included_files = tarball_reader.getnames()

        assert len(included_files) == 5
        assert 'vertical/a-vertical.xml' in included_files
        assert 'vertical/a-vertical-1.xml' in included_files
        assert 'sequential/a-sequential.xml' in included_files
        assert 'sequential/a-sequential-1.xml' in included_files

        sequential_1_xml = tarball_reader.extractfile('sequential/a-sequential.xml')
        assert '"a-vertical"' in sequential_1_xml.read().decode('utf-8')

        sequential_2_xml = tarball_reader.extractfile('sequential/a-sequential-1.xml')
        assert '"a-vertical-1"' in sequential_2_xml.read().decode('utf-8')

    def test_can_export_standalone_olx(self):
        # This is a really slimmed down test and should probably include more of the branching logic
        sequential = self._set_up_simple_structure()

        filename, olx = sequential.export_standalone_olx()
        assert 'A_sequential__' in filename
        assert '.tar.gz' in filename
        assert isinstance(olx, BytesIO)
        tarball = tarfile.open(fileobj=olx)
        included_files = tarball.getnames()
        assert 'sequential/a-sequential.xml' in included_files
        assert 'vertical/a-vertical.xml' in included_files
        assert 'html/introduction-to-python.xml' in included_files
        assert 'html/introduction-to-python.html' in included_files


@pytest.fixture(scope="function")
def course_run_composition_test_fixture(request):
    obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
    obj_map['texts'] = {
        'platform': {
            'text': 'SomeX',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        },
        'gradingPolicy': {
            'text': 'Everything is worth 100 points',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        },
        'policy': {
            'text': 'Stuff was due yesterday',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        },
    }
    obj_map['recordTypeIds'] = ['repository-record-type%3Arun-repo%40ODL.MIT.EDU']
    request.cls.rm = get_repository_manager()
    request.cls.osid_object = OsidObject(object_name='REPOSITORY',
                                         osid_object_map=obj_map,
                                         runtime=request.cls.rm._provider_manager._runtime)
    request.cls.composition = EdXCourseRunCompositionRecord(request.cls.osid_object)

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


@pytest.mark.usefixtures('course_run_composition_test_fixture')
class TestEdXCourseRunCompositionRecord(object):
    def _set_up_course_run(self, with_policy=True, with_grading_policy=True):
        """ Create a simple edX course with course, run, and a set of chapter -> sequential -> vertical
              compositions."""
        # Make sure to set the run_repo as my_osid_object, with a course_repo as parent
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])
        course_run_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-course-run'])

        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'Test Repo'
        test_repo = self.rm.create_repository(form)

        # start by making the vertical, so that when we set children, we have the IDs available
        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A sequential!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['sequential']))
        form.set_file_name('sequential/a-sequential.xml')
        form.set_children([vertical.ident])
        sequential = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A chapter!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['chapter']))
        form.set_file_name('chapter/a-chapter.xml')
        form.set_children([sequential.ident])
        chapter = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([course_run_composition_record])
        form.display_name = '2017_Fall'
        form.set_children([chapter.ident])
        run_composition = test_repo.create_composition(form)

        form = test_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = '6.001x'
        form.set_children([run_composition.ident])
        course_composition = test_repo.create_composition(form)

        return course_composition, run_composition

    def test_can_get_grading_policy(self):
        """Tests grading_policy"""
        assert isinstance(self.composition.grading_policy, DisplayText)
        assert self.composition.grading_policy.text == 'Everything is worth 100 points'

    def test_getting_grading_policy_if_not_present_raises_illegal_state(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['texts'] = {}
        obj_map['recordTypeIds'] = ['repository-composition%3Aedx-course-run%40EDX.ORG']
        osid_object = OsidObject(object_name='COMPOSITION',
                                 osid_object_map=obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        composition = EdXCourseRunCompositionRecord(osid_object)
        with pytest.raises(errors.IllegalState):
            composition.grading_policy

    def test_can_get_policy(self):
        """Tests policy"""
        assert isinstance(self.composition.policy, DisplayText)
        assert self.composition.policy.text == 'Stuff was due yesterday'

    def test_getting_policy_if_not_present_raises_illegal_state(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['texts'] = {}
        obj_map['recordTypeIds'] = ['repository-composition%3Aedx-course-run%40EDX.ORG']
        osid_object = OsidObject(object_name='COMPOSITION',
                                 osid_object_map=obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        composition = EdXCourseRunCompositionRecord(osid_object)
        with pytest.raises(errors.IllegalState):
            composition.policy

    def test_can_export_run_olx(self):
        course_composition, run_composition = self._set_up_course_run()
        self.composition.my_osid_object = run_composition
        filename, olx = self.composition.export_run_olx()

        assert '6_001x_2017_Fall' in filename
        assert '.tar.gz' in filename
        assert isinstance(olx, BytesIO)
        tarball = tarfile.open(fileobj=olx)
        included_files = tarball.getnames()
        assert '2017_Fall/course.xml' in included_files
        assert '2017_Fall/roots/2017_Fall.xml' in included_files
        assert '2017_Fall/vertical/a-vertical.xml' in included_files
        assert '2017_Fall/sequential/a-sequential.xml' in included_files
        assert '2017_Fall/chapter/a-chapter.xml' in included_files
        assert '2017_Fall/course/2017_Fall.xml' in included_files
        assert '2017_Fall/errors.xml' in included_files

        # TODO: add static file check here? Make sure they are generated into /static
        # TODO: add in html / problems check here?


@pytest.fixture(scope="function")
def course_run_composition_form_test_fixture(request):
    request.cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
    request.cls.osid_object_form._authority = 'TESTING.MIT.EDU'
    request.cls.osid_object_form._namespace = 'records.Testing'


@pytest.mark.usefixtures('course_run_composition_form_test_fixture')
class TestEdXCourseRunCompositionFormRecord(object):
    def test_can_set_policy(self):
        form = EdXCourseRunCompositionFormRecord(self.osid_object_form)
        assert 'policy' not in form.my_osid_object_form._my_map['texts']
        form.set_policy('Stuff was due yesterday')
        assert 'policy' in form.my_osid_object_form._my_map['texts']
        assert form.my_osid_object_form._my_map['texts']['policy']['text'] == 'Stuff was due yesterday'

    def test_can_clear_policy(self):
        form = EdXCourseRunCompositionFormRecord(self.osid_object_form)
        form.set_policy('Stuff was due yesterday')
        assert form.my_osid_object_form._my_map['texts']['policy']['text'] == 'Stuff was due yesterday'
        form.clear_policy()
        assert 'policy' not in form.my_osid_object_form._my_map['texts']

    def test_clearing_policy_before_set_raises_not_found(self):
        form = EdXCourseRunCompositionFormRecord(self.osid_object_form)
        with pytest.raises(errors.NotFound):
            form.clear_policy()

    def test_can_set_grading_policy(self):
        form = EdXCourseRunCompositionFormRecord(self.osid_object_form)
        assert 'gradingPolicy' not in form.my_osid_object_form._my_map['texts']
        form.set_grading_policy('Everything is worth 100 points')
        assert 'gradingPolicy' in form.my_osid_object_form._my_map['texts']
        assert form.my_osid_object_form._my_map['texts']['gradingPolicy']['text'] == 'Everything is worth 100 points'

    def test_can_clear_grading_policy(self):
        form = EdXCourseRunCompositionFormRecord(self.osid_object_form)
        form.set_grading_policy('Everything is worth 100 points')
        assert form.my_osid_object_form._my_map['texts']['gradingPolicy']['text'] == 'Everything is worth 100 points'
        form.clear_grading_policy()
        assert 'gradingPolicy' not in form.my_osid_object_form._my_map['texts']

    def test_clearing_grading_policy_before_set_raises_not_found(self):
        form = EdXCourseRunCompositionFormRecord(self.osid_object_form)
        with pytest.raises(errors.NotFound):
            form.clear_grading_policy()
