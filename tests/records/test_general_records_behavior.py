# This set of tests is to make sure that the new record schema (manipulating __class__.__bases__)
#   does not have unexpected consequences...like changing in memory the class inheritance for all
#   instances of an OsidObject. i.e. if I use ``add_item_record`` to an ItemForm, do all subsequent
#   ItemForms have that record class in the MRO?

import unittest

from dlkit.primordium.type.primitives import Type

from dlkit.records import registry
from dlkit.records.assessment.basic.base_records import ItemWithSolutionFormRecord
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest


ITEM_FORM_WITH_SOLUTION = Type(**registry.ITEM_RECORD_TYPES['with-solution'])
PROVENANCE_ITEM = Type(**registry.ITEM_RECORD_TYPES['provenance'])


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
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
