from __future__ import unicode_literals

import datetime
import unittest

from copy import deepcopy

try:
    from mock import patch, MagicMock
except ImportError:
    from unittest.mock import patch, MagickMock

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.records.assessment.basic.base_records import *

from dlkit.json_.assessment.objects import AssessmentTaken, AssessmentTakenList
from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.json_.osid.queries import OsidObjectQuery
from dlkit.json_.osid.metadata import Metadata
from dlkit.records import registry
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest

from ... import utilities


ASSESSMENT_TAKEN_PROVENANCE = Type(**registry.ASSESSMENT_TAKEN_RECORD_TYPES['provenance'])


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


class TestProvenanceAssessmentTakenRecord(unittest.TestCase):
    """Tests for ProvenanceAssessmentTakenRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        cls.provenance_id = 'my-fake%3A000000000000000000000000%40ODL.MIT.EDU'
        obj_map['provenanceId'] = cls.provenance_id
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)

    def setUp(self):
        self.taken_object = ProvenanceAssessmentTakenRecord(self.osid_object)
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['provenanceId'] = ''
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        self.taken_object_no_provenance = ProvenanceAssessmentTakenRecord(osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_provenance_id(self):
        self.assertEqual(str(self.taken_object.get_provenance_id()), self.provenance_id)
        with self.assertRaises(errors.IllegalState):
            self.taken_object_no_provenance.get_provenance_id()

    def test_can_call_has_provenance(self):
        self.assertTrue(self.taken_object.has_provenance())
        self.assertFalse(self.taken_object_no_provenance.has_provenance())

    @patch('dlkit.json_.utilities.JSON_CLIENT')
    def test_can_call_has_provenance_children_no_children(self, MockJSON_CLIENT):
        class FakeResults:
            def count(self):
                return 0

        class FakeClient(MagicMock):
            def __get_item__(self):
                return self

            def find(self, *args):
                return FakeResults()

        MockJSON_CLIENT.json_client = FakeClient()

        self.assertFalse(self.taken_object.has_provenance_children())
        self.assertFalse(self.taken_object_no_provenance.has_provenance_children())

    @patch('dlkit.json_.utilities.JSON_CLIENT')
    def test_can_call_has_provenance_children_mocked(self, MockJSON_CLIENT):
        class FakeResults:
            def count(self):
                return 1

        class FakeClient(MagicMock):
            def __get_item__(self):
                return self

            def find(self, *args):
                return FakeResults()

        MockJSON_CLIENT.json_client = FakeClient()

        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        taken_id = 'taken%3A123%40ODL.MIT.EDU'
        obj_map['id'] = taken_id
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        taken_object = ProvenanceAssessmentTakenRecord(osid_object)

        self.assertTrue(taken_object.has_provenance_children())

    @patch('dlkit.json_.utilities.JSON_CLIENT')
    def test_can_get_provenance_children_no_children(self, MockJSON_CLIENT):
        class FakeResults:
            def count(self):
                return 0

        class FakeClient(MagicMock):
            def __get_item__(self):
                return self

            def find(self, *args):
                return FakeResults()

        MockJSON_CLIENT.json_client = FakeClient()

        with self.assertRaises(errors.IllegalState):
            self.taken_object.get_provenance_children()

    @patch('dlkit.json_.utilities.JSON_CLIENT')
    def test_can_get_provenance_children_mocked(self, MockJSON_CLIENT):
        class FakeClient(MagicMock):
            def __get_item__(self):
                return self

            def find(self, *args):
                fake_taken = deepcopy(utilities.TEST_OBJECT_MAP)
                fake_taken['_id'] = 'foo'
                return [fake_taken]

        MockJSON_CLIENT.json_client = FakeClient()

        with patch.object(self.taken_object, 'has_provenance_children', return_value=True) as mocked_method:
            children = self.taken_object.get_provenance_children()
            self.assertTrue(isinstance(children, AssessmentTakenList))
            self.assertEqual(children.available(), 1)
            self.assertEqual(str(children.next().ident), 'assessment.AssessmentTaken%3Afoo%40ODL.MIT.EDU')

    def test_can_get_provenance_parent(self):
        with self.assertRaises(errors.IllegalState):
            self.taken_object_no_provenance.get_provenance_parent()

    @patch('dlkit.json_.utilities.JSON_CLIENT')
    def test_can_get_provenance_parent_mocked(self, MockJSON_CLIENT):
        class FakeClient(MagicMock):
            def __get_item__(self):
                return self

            def find_one(self, *args):
                fake_taken = deepcopy(utilities.TEST_OBJECT_MAP)
                fake_taken['_id'] = 'foo'
                return fake_taken

        MockJSON_CLIENT.json_client = FakeClient()

        with patch.object(self.taken_object, 'has_provenance_children', return_value=True) as mocked_method:
            parent = self.taken_object.get_provenance_parent()
            self.assertTrue(isinstance(parent, AssessmentTaken))
            self.assertEqual(str(parent.ident), 'assessment.AssessmentTaken%3Afoo%40ODL.MIT.EDU')


class TestProvenanceAssessmentTakenFormRecord(unittest.TestCase):
    """Tests for ProvenanceAssessmentTakenFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    def setUp(self):
        self.form = ProvenanceAssessmentTakenFormRecord(self.osid_object_form)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_provenance_metadata(self):
        self.assertTrue(isinstance(self.form.get_provenance_metadata(), Metadata))

    def test_can_set_provenance(self):
        self.assertEqual(self.form.my_osid_object_form._my_map['provenanceId'], '')
        self.form.set_provenance('foo-bar')
        self.assertEqual(self.form.my_osid_object_form._my_map['provenanceId'], 'foo-bar')

    def test_can_clear_provenance(self):
        self.form.set_provenance('bim-baz')
        self.assertEqual(self.form.my_osid_object_form._my_map['provenanceId'], 'bim-baz')
        self.form.clear_provenance()
        self.assertEqual(self.form.my_osid_object_form._my_map['provenanceId'], '')
