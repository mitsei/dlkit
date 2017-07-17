"""Unit tests of osid base_records."""
from __future__ import unicode_literals

import tarfile
import unittest

from copy import deepcopy
from six import BytesIO

from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.repository.objects import Composition
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.records.repository.lore.repository_extensions import *
from dlkit.records.registry import COMPOSITION_GENUS_TYPES, REPOSITORY_RECORD_TYPES,\
    COMPOSITION_RECORD_TYPES, REPOSITORY_GENUS_TYPES

from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest

from ... import utilities


def get_repository_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('REPOSITORY',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


class TestLoreRepositoryRecord(unittest.TestCase):
    """Tests for LoreRepositoryRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['displayName'] = {
            'text': 'Fake Display Name, 123',
            'languageTypeId': '639-2%3AENG%40ISO',
            'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
            'scriptTypeId': '15924%3ALATN%40ISO'
        }
        obj_map['recordTypeIds'] = ['repository-record-type%3Alore-repo%40ODL.MIT.EDU']
        obj_map['_id'] = 'fake-id'
        rm = get_repository_manager()
        cls.osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=obj_map,
                                     runtime=rm._provider_manager._runtime)
        cls.lore_repository = LoreRepositoryRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_id(self):
        """Tests id"""
        self.assertTrue(isinstance(self.lore_repository.id, Id))
        self.assertEqual(str(self.lore_repository.id), 'osid.OsidObject%3Afake-id%40ODL.MIT.EDU')

    def test_can_get_name(self):
        self.assertTrue(isinstance(self.lore_repository.name, DisplayText))
        self.assertEqual(self.lore_repository.name.text, 'Fake Display Name, 123')

    def test_can_get_slug(self):
        self.assertEqual(self.lore_repository.slug, 'fake-display-name-123')

    def test_on_object_map_returns_slug(self):
        obj_map_to_test = {}
        self.lore_repository._update_object_map(obj_map_to_test)
        self.assertIn('slug', obj_map_to_test)
        self.assertEqual(obj_map_to_test['slug'], 'fake-display-name-123')


class TestLoreRepositoryFormRecord(unittest.TestCase):
    """ Don't need to test anything here because it inherits directly from TextsFormRecord """
    pass


class TestLoreCourseRepositoryRecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['texts'] = {
            'org': {
                'text': 'Fake University',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        }
        obj_map['recordTypeIds'] = ['repository-record-type%3Alore-repo%40ODL.MIT.EDU']
        obj_map['_id'] = 'fake-id'
        rm = get_repository_manager()
        cls.osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=obj_map,
                                     runtime=rm._provider_manager._runtime)
        cls.lore_repository = LoreCourseRepositoryRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_org(self):
        """Tests org"""
        self.assertTrue(isinstance(self.lore_repository.org, DisplayText))
        self.assertEqual(self.lore_repository.org.text, 'Fake University')


class TestLoreCourseRepositoryFormRecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_org(self):
        """Tests set_org"""
        form = LoreCourseRepositoryFormRecord(self.osid_object_form)
        self.assertNotIn('org', form.my_osid_object_form._my_map['texts'])
        form.set_org('foo')
        self.assertIn('org', form.my_osid_object_form._my_map['texts'])
        self.assertEqual(form.my_osid_object_form._my_map['texts']['org']['text'], 'foo')

    def test_can_clear_org(self):
        form = LoreCourseRepositoryFormRecord(self.osid_object_form)
        form.set_org('foo')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['org']['text'], 'foo')
        form.clear_org()
        self.assertNotIn('org', form.my_osid_object_form._my_map['texts'])

    def test_clearing_org_before_set_raises_not_found(self):
        form = LoreCourseRepositoryFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NotFound):
            form.clear_org()


class TestLoreCourseRunRepositoryRecord(unittest.TestCase):
    def _set_up_course_run(self, with_policy=True, with_grading_policy=True):
        """ Create a simple edX course with course, run, and a set of chapter -> sequential -> vertical
              compositions."""
        # Make sure to set the run_repo as my_osid_object, with a course_repo as parent
        course_genus = Type(**COMPOSITION_GENUS_TYPES['course'])
        course_repo_record = Type(**REPOSITORY_RECORD_TYPES['course-repo'])
        run_repo_record = Type(**REPOSITORY_RECORD_TYPES['run-repo'])
        run_repo_genus = Type(**REPOSITORY_GENUS_TYPES['course-run-repo'])
        lore_repo_record = Type(**REPOSITORY_RECORD_TYPES['lore-repo'])
        edx_composition_record = Type(**COMPOSITION_RECORD_TYPES['edx-composition'])

        form = self.rm.get_repository_form_for_create([lore_repo_record, course_repo_record])
        form.display_name = '6.001x'
        form.set_org('UniX')
        course_repo = self.rm.create_repository(form)

        form = self.rm.get_repository_form_for_create([lore_repo_record, run_repo_record])
        form.display_name = '2017_Fall'
        form.set_genus_type(run_repo_genus)

        if with_policy:
            form.set_policy('Stuff was due yesterday')

        if with_grading_policy:
            form.set_grading_policy('Everything is important')

        run_repo = self.rm.create_repository(form)

        self.rm.add_child_repository(course_repo.ident, run_repo.ident)

        # start by making the vertical, so that when we set children, we have the IDs available
        form = run_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A vertical!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['vertical']))
        form.set_file_name('vertical/a-vertical.xml')
        vertical = run_repo.create_composition(form)

        form = run_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A sequential!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['sequential']))
        form.set_file_name('sequential/a-sequential.xml')
        form.set_children([vertical.ident])
        sequential = run_repo.create_composition(form)

        form = run_repo.get_composition_form_for_create([edx_composition_record])
        form.display_name = 'A chapter!'
        form.set_genus_type(Type(**COMPOSITION_GENUS_TYPES['chapter']))
        form.set_file_name('chapter/a-chapter.xml')
        form.set_children([sequential.ident])
        chapter = run_repo.create_composition(form)

        form = run_repo.get_composition_form_for_create([edx_composition_record])
        form.set_genus_type(course_genus)
        form.set_file_name('course.xml')
        form.set_sequestered(True)
        form.set_children([chapter.ident])
        course_composition = run_repo.create_composition(form)

        return course_repo, run_repo

    @classmethod
    def setUpClass(cls):
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
        cls.rm = get_repository_manager()
        cls.osid_object = OsidObject(object_name='REPOSITORY',
                                     osid_object_map=obj_map,
                                     runtime=cls.rm._provider_manager._runtime)
        cls.lore_repository = LoreCourseRunRepositoryRecord(cls.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_platform(self):
        """Tests platform"""
        self.assertTrue(isinstance(self.lore_repository.platform, DisplayText))
        self.assertEqual(self.lore_repository.platform.text, 'SomeX')

    def test_getting_platform_if_not_present_raises_illegal_state(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['texts'] = {}
        obj_map['recordTypeIds'] = ['repository-record-type%3Arun-repo%40ODL.MIT.EDU']
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        lore_repository = LoreCourseRunRepositoryRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            lore_repository.platform

    def test_can_get_grading_policy(self):
        """Tests grading_policy"""
        self.assertTrue(isinstance(self.lore_repository.grading_policy, DisplayText))
        self.assertEqual(self.lore_repository.grading_policy.text, 'Everything is worth 100 points')

    def test_getting_grading_policy_if_not_present_raises_illegal_state(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['texts'] = {}
        obj_map['recordTypeIds'] = ['repository-record-type%3Arun-repo%40ODL.MIT.EDU']
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        lore_repository = LoreCourseRunRepositoryRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            lore_repository.grading_policy

    def test_can_get_policy(self):
        """Tests policy"""
        self.assertTrue(isinstance(self.lore_repository.policy, DisplayText))
        self.assertEqual(self.lore_repository.policy.text, 'Stuff was due yesterday')

    def test_getting_policy_if_not_present_raises_illegal_state(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['texts'] = {}
        obj_map['recordTypeIds'] = ['repository-record-type%3Arun-repo%40ODL.MIT.EDU']
        osid_object = OsidObject(object_name='REPOSITORY',
                                 osid_object_map=obj_map,
                                 runtime=self.rm._provider_manager._runtime)
        lore_repository = LoreCourseRunRepositoryRecord(osid_object)
        with self.assertRaises(errors.IllegalState):
            lore_repository.policy

    def test_can_get_course_node(self):
        """Tests course_node"""
        course_genus = Type(**COMPOSITION_GENUS_TYPES['course'])
        form = self.rm.get_repository_form_for_create([])
        form.display_name = 'test repo'
        repo = self.rm.create_repository(form)
        form = repo.get_composition_form_for_create([])
        form.set_genus_type(course_genus)
        composition = repo.create_composition(form)
        self.lore_repository.my_osid_object._my_map['_id'] = repo.ident.identifier
        self.assertTrue(isinstance(self.lore_repository.course_node, Composition))
        self.assertEqual(str(self.lore_repository.course_node.genus_type),
                         str(course_genus))

        repo.delete_composition(composition.ident)
        self.rm.delete_repository(repo.ident)

    def test_getting_course_node_if_none_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.lore_repository.course_node

    def test_can_export_olx(self):
        course_repo, run_repo = self._set_up_course_run()
        filename, olx = run_repo.export_olx()

        self.assertIn('6_001x_2017_Fall', filename)
        self.assertIn('.tar.gz', filename)
        self.assertTrue(isinstance(olx, BytesIO))
        tarball = tarfile.open(fileobj=olx)
        included_files = tarball.getnames()
        self.assertIn('2017_Fall/course.xml', included_files)
        self.assertIn('2017_Fall/roots/2017_Fall.xml', included_files)
        self.assertIn('2017_Fall/policies/2017_Fall/policy.json', included_files)
        self.assertIn('2017_Fall/policies/2017_Fall/grading_policy.json', included_files)
        self.assertIn('2017_Fall/vertical/a-vertical.xml', included_files)
        self.assertIn('2017_Fall/sequential/a-sequential.xml', included_files)
        self.assertIn('2017_Fall/chapter/a-chapter.xml', included_files)
        self.assertIn('2017_Fall/course/2017_Fall.xml', included_files)
        self.assertIn('2017_Fall/errors.xml', included_files)

        # TODO: add static file check here? Make sure they are generated into /static
        # TODO: add in html / problems check here?

    def test_can_export_olx_without_policy(self):
        course_repo, run_repo = self._set_up_course_run(with_policy=False)
        filename, olx = run_repo.export_olx()

        self.assertIn('6_001x_2017_Fall', filename)
        self.assertIn('.tar.gz', filename)
        self.assertTrue(isinstance(olx, BytesIO))
        tarball = tarfile.open(fileobj=olx)
        included_files = tarball.getnames()
        self.assertIn('2017_Fall/course.xml', included_files)
        self.assertIn('2017_Fall/roots/2017_Fall.xml', included_files)
        self.assertIn('2017_Fall/policies/2017_Fall/grading_policy.json', included_files)
        self.assertIn('2017_Fall/vertical/a-vertical.xml', included_files)
        self.assertIn('2017_Fall/sequential/a-sequential.xml', included_files)
        self.assertIn('2017_Fall/chapter/a-chapter.xml', included_files)
        self.assertIn('2017_Fall/course/2017_Fall.xml', included_files)
        self.assertIn('2017_Fall/errors.xml', included_files)

    def test_can_export_olx_without_grading_policy(self):
        course_repo, run_repo = self._set_up_course_run(with_grading_policy=False)
        filename, olx = run_repo.export_olx()

        self.assertIn('6_001x_2017_Fall', filename)
        self.assertIn('.tar.gz', filename)
        self.assertTrue(isinstance(olx, BytesIO))
        tarball = tarfile.open(fileobj=olx)
        included_files = tarball.getnames()
        self.assertIn('2017_Fall/course.xml', included_files)
        self.assertIn('2017_Fall/roots/2017_Fall.xml', included_files)
        self.assertIn('2017_Fall/policies/2017_Fall/policy.json', included_files)
        self.assertIn('2017_Fall/vertical/a-vertical.xml', included_files)
        self.assertIn('2017_Fall/sequential/a-sequential.xml', included_files)
        self.assertIn('2017_Fall/chapter/a-chapter.xml', included_files)
        self.assertIn('2017_Fall/course/2017_Fall.xml', included_files)
        self.assertIn('2017_Fall/errors.xml', included_files)

    def test_clean_up_removes_all_run_compositions_and_assets(self):
        course_repo, run_repo = self._set_up_course_run(with_policy=False)

        lore_repo_record = Type(**REPOSITORY_RECORD_TYPES['lore-repo'])
        form = self.rm.get_repository_form_for_create([lore_repo_record])
        form.display_name = 'test user repository'
        user_repo = self.rm.create_repository(form)

        run_repo.clean_up(user_repo)

        with self.assertRaises(errors.NotFound):
            self.rm.get_repository(run_repo.ident)

        self.assertEqual(self.rm.get_child_repositories(course_repo.ident).available(), 0)


class TestLoreCourseRunRepositoryFormRecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_set_platform(self):
        """Tests set_platform"""
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        self.assertNotIn('platform', form.my_osid_object_form._my_map['texts'])
        form.set_platform('FooX')
        self.assertIn('platform', form.my_osid_object_form._my_map['texts'])
        self.assertEqual(form.my_osid_object_form._my_map['texts']['platform']['text'], 'FooX')

    def test_can_clear_platform(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        form.set_platform('FooX')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['platform']['text'], 'FooX')
        form.clear_platform()
        self.assertNotIn('platform', form.my_osid_object_form._my_map['texts'])

    def test_clearing_platform_before_set_raises_not_found(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NotFound):
            form.clear_platform()

    def test_can_set_policy(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        self.assertNotIn('policy', form.my_osid_object_form._my_map['texts'])
        form.set_policy('Stuff was due yesterday')
        self.assertIn('policy', form.my_osid_object_form._my_map['texts'])
        self.assertEqual(form.my_osid_object_form._my_map['texts']['policy']['text'], 'Stuff was due yesterday')

    def test_can_clear_policy(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        form.set_policy('Stuff was due yesterday')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['policy']['text'], 'Stuff was due yesterday')
        form.clear_policy()
        self.assertNotIn('policy', form.my_osid_object_form._my_map['texts'])

    def test_clearing_policy_before_set_raises_not_found(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NotFound):
            form.clear_policy()

    def test_can_set_grading_policy(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        self.assertNotIn('gradingPolicy', form.my_osid_object_form._my_map['texts'])
        form.set_grading_policy('Everything is worth 100 points')
        self.assertIn('gradingPolicy', form.my_osid_object_form._my_map['texts'])
        self.assertEqual(form.my_osid_object_form._my_map['texts']['gradingPolicy']['text'],
                         'Everything is worth 100 points')

    def test_can_clear_grading_policy(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        form.set_grading_policy('Everything is worth 100 points')
        self.assertEqual(form.my_osid_object_form._my_map['texts']['gradingPolicy']['text'],
                         'Everything is worth 100 points')
        form.clear_grading_policy()
        self.assertNotIn('gradingPolicy', form.my_osid_object_form._my_map['texts'])

    def test_clearing_grading_policy_before_set_raises_not_found(self):
        form = LoreCourseRunRepositoryFormRecord(self.osid_object_form)
        with self.assertRaises(errors.NotFound):
            form.clear_grading_policy()
