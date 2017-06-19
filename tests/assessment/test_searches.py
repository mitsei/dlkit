"""Unit tests of assessment searches."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestItemSearch(unittest.TestCase):
    """Tests for ItemSearch"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        self.search = self.catalog.get_item_search()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_search_among_items(self):
        """Tests search_among_items"""
        # This is implementation dependent...find some other way?
        self.assertIsNone(self.search._id_list)
        fake_list = [self.catalog.ident]
        self.search.search_among_items(fake_list)
        self.assertEqual(self.search._id_list, fake_list)

    @unittest.skip('unimplemented test')
    def test_order_item_results(self):
        """Tests order_item_results"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_search_record(self):
        """Tests get_item_search_record"""
        pass


class TestItemSearchResults(unittest.TestCase):
    """Tests for ItemSearchResults"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        self.query = self.catalog.get_item_query()
        self.search_obj = self.catalog.get_item_search()
        self.search = self.catalog.get_items_by_search(self.query, self.search_obj)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_items(self):
        """Tests get_items"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        items = self.search.get_items()
        self.assertTrue(isinstance(items, ItemList))
        self.assertEqual(items.available(), 0)

    @unittest.skip('unimplemented test')
    def test_get_item_query_inspector(self):
        """Tests get_item_query_inspector"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_search_results_record(self):
        """Tests get_item_search_results_record"""
        pass


class TestAssessmentSearch(unittest.TestCase):
    """Tests for AssessmentSearch"""

    @unittest.skip('unimplemented test')
    def test_search_among_assessments(self):
        """Tests search_among_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_order_assessment_results(self):
        """Tests order_assessment_results"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_search_record(self):
        """Tests get_assessment_search_record"""
        pass


class TestAssessmentSearchResults(unittest.TestCase):
    """Tests for AssessmentSearchResults"""

    @unittest.skip('unimplemented test')
    def test_get_assessments(self):
        """Tests get_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query_inspector(self):
        """Tests get_assessment_query_inspector"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_search_results_record(self):
        """Tests get_assessment_search_results_record"""
        pass


class TestAssessmentOfferedSearch(unittest.TestCase):
    """Tests for AssessmentOfferedSearch"""

    @unittest.skip('unimplemented test')
    def test_search_among_assessments_offered(self):
        """Tests search_among_assessments_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_order_assessment_offered_results(self):
        """Tests order_assessment_offered_results"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_search_record(self):
        """Tests get_assessment_offered_search_record"""
        pass


class TestAssessmentOfferedSearchResults(unittest.TestCase):
    """Tests for AssessmentOfferedSearchResults"""

    @unittest.skip('unimplemented test')
    def test_get_assessments_offered(self):
        """Tests get_assessments_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_query_inspector(self):
        """Tests get_assessment_offered_query_inspector"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_search_results_record(self):
        """Tests get_assessment_offered_search_results_record"""
        pass


class TestAssessmentTakenSearch(unittest.TestCase):
    """Tests for AssessmentTakenSearch"""

    @unittest.skip('unimplemented test')
    def test_search_among_assessments_taken(self):
        """Tests search_among_assessments_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_order_assessment_taken_results(self):
        """Tests order_assessment_taken_results"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_search_record(self):
        """Tests get_assessment_taken_search_record"""
        pass


class TestAssessmentTakenSearchResults(unittest.TestCase):
    """Tests for AssessmentTakenSearchResults"""

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken(self):
        """Tests get_assessments_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_query_inspector(self):
        """Tests get_assessment_taken_query_inspector"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_search_results_record(self):
        """Tests get_assessment_taken_search_results_record"""
        pass


class TestBankSearch(unittest.TestCase):
    """Tests for BankSearch"""

    @unittest.skip('unimplemented test')
    def test_search_among_banks(self):
        """Tests search_among_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_order_bank_results(self):
        """Tests order_bank_results"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_search_record(self):
        """Tests get_bank_search_record"""
        pass


class TestBankSearchResults(unittest.TestCase):
    """Tests for BankSearchResults"""

    @unittest.skip('unimplemented test')
    def test_get_banks(self):
        """Tests get_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query_inspector(self):
        """Tests get_bank_query_inspector"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_search_results_record(self):
        """Tests get_bank_search_results_record"""
        pass
