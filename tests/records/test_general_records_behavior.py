# This set of tests is to make sure that the new record schema (manipulating __class__.__bases__)
#   does not have unexpected consequences...like changing in memory the class inheritance for all
#   instances of an OsidObject. i.e. if I use ``add_item_record`` to an ItemForm, do all subsequent
#   ItemForms have that record class in the MRO?

import os
import unittest

from copy import deepcopy

from dlkit.primordium.transport.objects import DataInputStream
from dlkit.primordium.type.primitives import Type

from dlkit.records import registry
from dlkit.records.assessment.basic.base_records import ItemWithSolutionFormRecord
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))

ITEM_FORM_WITH_SOLUTION = Type(**registry.ITEM_RECORD_TYPES['with-solution'])
PROVENANCE_ITEM = Type(**registry.ITEM_RECORD_TYPES['provenance'])
MULTI_CHOICE_RANDOMIZE_CHOICES_QUESTION_FORM_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-choice-randomized'])
MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD = Type(**registry.QUESTION_RECORD_TYPES['multi-language-ordered-choice'])

IMAGE_ASSET_GENUS_TYPE = Type(**registry.ASSET_GENUS_TYPES['image'])
PNG_ASSET_CONTENT_GENUS_TYPE = Type(**registry.ASSET_CONTENT_GENUS_TYPES['png'])

TIME_VALUE_RECORD = Type(**registry.OSID_OBJECT_RECORD_TYPES['time-value'])


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


class TestAddItemRecordMRO(unittest.TestCase):
    """ Make sure adding a record does not "permanently" affect a class's MRO. """

    @classmethod
    def setUpClass(cls):
        cls.mgr = get_assessment_manager()
        form = cls.mgr.get_bank_form_for_create([])
        form.display_name = 'Bank for testing'
        cls.bank = cls.mgr.create_bank(form)

        cls.test_display_name = 'my test item'
        form = cls.bank.get_item_form_for_create([])
        form.display_name = cls.test_display_name
        form.add_form_record(ITEM_FORM_WITH_SOLUTION)
        form.set_solution('hopefully isolated to this one item')
        cls.item_1 = cls.bank.create_item(form)

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for assessment in cls.bank.get_assessments():
            for assessment_offered in cls.bank.get_assessments_offered_for_assessment(assessment.ident):
                for assessment_taken in cls.bank.get_assessments_taken_for_assessment_offered(assessment_offered.ident):
                    cls.bank.delete_assessment_taken(assessment_taken.ident)
                cls.bank.delete_assessment_offered(assessment_offered.ident)
            cls.bank.delete_assessment(assessment.ident)
        for item in cls.bank.get_items():
            cls.bank.delete_item(item.ident)
        cls.mgr.delete_bank(cls.bank.ident)

    def test_new_items_do_not_have_the_same_inheritance(self):
        form = self.bank.get_item_form_for_create([])
        self.assertTrue(ItemWithSolutionFormRecord not in form.__class__.__bases__)

    def test_extended_item_maintains_attributes(self):
        """ Check that ``add_form_record`` does not overwrite attributes when changing the class. """
        self.assertTrue(self.item_1.display_name.text == self.test_display_name)


class TestNewItemWithRecordMRO(unittest.TestCase):
    """ Make sure creating an item with a record does not "permanently" affect a class's MRO. """

    @classmethod
    def setUpClass(cls):
        cls.mgr = get_assessment_manager()
        form = cls.mgr.get_bank_form_for_create([])
        form.display_name = 'Bank for testing'
        cls.bank = cls.mgr.create_bank(form)

        form = cls.bank.get_item_form_for_create([ITEM_FORM_WITH_SOLUTION])
        form.set_solution('hopefully isolated to this one item')
        cls.item_1 = cls.bank.create_item(form)

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for assessment in cls.bank.get_assessments():
            for assessment_offered in cls.bank.get_assessments_offered_for_assessment(assessment.ident):
                for assessment_taken in cls.bank.get_assessments_taken_for_assessment_offered(assessment_offered.ident):
                    cls.bank.delete_assessment_taken(assessment_taken.ident)
                cls.bank.delete_assessment_offered(assessment_offered.ident)
            cls.bank.delete_assessment(assessment.ident)
        for item in cls.bank.get_items():
            cls.bank.delete_item(item.ident)
        cls.mgr.delete_bank(cls.bank.ident)

    def test_new_items_do_not_have_the_same_inheritance(self):
        form = self.bank.get_item_form_for_create([])
        self.assertTrue(ItemWithSolutionFormRecord not in form.__class__.__bases__)


class TestUpdateObjectMapCalled(unittest.TestCase):
    """ This is to make sure that _update_object_map is called for every record. """

    @classmethod
    def setUpClass(cls):
        cls.mgr = get_assessment_manager()
        form = cls.mgr.get_bank_form_for_create([])
        form.display_name = 'Bank for testing'
        cls.bank = cls.mgr.create_bank(form)

        cls.test_display_name = 'my test item'
        form = cls.bank.get_item_form_for_create([])
        form.display_name = cls.test_display_name
        form.add_form_record(PROVENANCE_ITEM)
        cls.item_1 = cls.bank.create_item(form)

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for assessment in cls.bank.get_assessments():
            for assessment_offered in cls.bank.get_assessments_offered_for_assessment(assessment.ident):
                for assessment_taken in cls.bank.get_assessments_taken_for_assessment_offered(assessment_offered.ident):
                    cls.bank.delete_assessment_taken(assessment_taken.ident)
                cls.bank.delete_assessment_offered(assessment_offered.ident)
            cls.bank.delete_assessment(assessment.ident)
        for item in cls.bank.get_items():
            cls.bank.delete_item(item.ident)
        cls.mgr.delete_bank(cls.bank.ident)

    def test_first_record_should_be_called(self):
        self.assertTrue(isinstance(self.item_1.object_map['creationTime'], dict))


class TestRecordsOverwritingMap(unittest.TestCase):
    """ This makes sure that calling ``add_form_record`` does not override existing values in the map,
        by re-initializing previous records.

        Note that the ``MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD`` does NOT inherit from any
        ``FILES_FORM_RECORD``, so it should not touch the ``_my_map['fileIds']`` dictionary.

        However, currently its ``_init_map()`` does call super, which goes through every existing record
        and calls its ``_init_map()``, leading to the ``MultiChoiceRandomizeChoicesQuestionFormRecord``
        being re-initialized and wiping out the values.
        """

    @classmethod
    def setUpClass(cls):
        cls.mgr = get_assessment_manager()
        cls.rmgr = get_repository_manager()
        form = cls.mgr.get_bank_form_for_create([])
        form.display_name = 'Bank for testing'
        cls.bank = cls.mgr.create_bank(form)

    def setUp(self):
        self.test_display_name = 'my test item'
        form = self.bank.get_item_form_for_create([])
        form.display_name = self.test_display_name
        self.item = self.bank.create_item(form)
        self.file = open(os.path.join(ABS_PATH, 'records', 'files', 'test_image.png'), 'rb')

    @classmethod
    def tearDownClass(cls):
        for assessment in cls.bank.get_assessments():
            for assessment_offered in cls.bank.get_assessments_offered_for_assessment(assessment.ident):
                for assessment_taken in cls.bank.get_assessments_taken_for_assessment_offered(assessment_offered.ident):
                    cls.bank.delete_assessment_taken(assessment_taken.ident)
                cls.bank.delete_assessment_offered(assessment_offered.ident)
            cls.bank.delete_assessment(assessment.ident)
        for item in cls.bank.get_items():
            cls.bank.delete_item(item.ident)
        repo = cls.rmgr.get_repository(cls.bank.ident)
        for asset in repo.get_assets():
            repo.delete_asset(asset.ident)
        cls.rmgr.delete_repository(repo.ident)
        cls.mgr.delete_bank(cls.bank.ident)

    def tearDown(self):
        for item in self.bank.get_items():
            self.bank.delete_item(item.ident)
        self.file.close()

    def test_existing_files_should_remain_after_adding_record(self):
        form = self.bank.get_question_form_for_create(self.item.ident, [MULTI_CHOICE_RANDOMIZE_CHOICES_QUESTION_FORM_RECORD])
        form.add_file(DataInputStream(self.file),
                      label='test_file',
                      asset_type=IMAGE_ASSET_GENUS_TYPE,
                      asset_content_type=PNG_ASSET_CONTENT_GENUS_TYPE,
                      asset_content_record_types=[],
                      asset_name='test_file',
                      asset_description='QTI media file')
        self.assertNotEqual(form._my_map['fileIds'], {})
        expected_value = deepcopy(form._my_map['fileIds'])

        # form.add_form_record(MULTI_LANGUAGE_ORDERED_CHOICE_QUESTION_RECORD)
        form.add_form_record(TIME_VALUE_RECORD)

        self.assertNotEqual(form._my_map['fileIds'], {})
        self.assertEqual(form._my_map['fileIds'], expected_value)
