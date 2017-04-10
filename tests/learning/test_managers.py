"""Unit tests of learning managers."""

import unittest
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

from dlkit.primordium.type.primitives import Type
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT',})

from dlkit.abstract_osid.type.objects import TypeList as abc_type_list
from dlkit.abstract_osid.osid import errors


class TestLearningProfile(unittest.TestCase):
    """Tests for LearningProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')


    def test_supports_objective_lookup(self):
        """Tests supports_objective_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_objective_lookup(), bool))

    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        self.assertTrue(isinstance(self.mgr.supports_objective_query(), bool))

    def test_supports_objective_admin(self):
        """Tests supports_objective_admin"""
        self.assertTrue(isinstance(self.mgr.supports_objective_admin(), bool))

    def test_supports_objective_hierarchy(self):
        """Tests supports_objective_hierarchy"""
        self.assertTrue(isinstance(self.mgr.supports_objective_hierarchy(), bool))

    def test_supports_objective_hierarchy_design(self):
        """Tests supports_objective_hierarchy_design"""
        self.assertTrue(isinstance(self.mgr.supports_objective_hierarchy_design(), bool))

    def test_supports_objective_sequencing(self):
        """Tests supports_objective_sequencing"""
        self.assertTrue(isinstance(self.mgr.supports_objective_sequencing(), bool))

    def test_supports_objective_objective_bank(self):
        """Tests supports_objective_objective_bank"""
        self.assertTrue(isinstance(self.mgr.supports_objective_objective_bank(), bool))

    def test_supports_objective_objective_bank_assignment(self):
        """Tests supports_objective_objective_bank_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_objective_objective_bank_assignment(), bool))

    def test_supports_objective_requisite(self):
        """Tests supports_objective_requisite"""
        self.assertTrue(isinstance(self.mgr.supports_objective_requisite(), bool))

    def test_supports_objective_requisite_assignment(self):
        """Tests supports_objective_requisite_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_objective_requisite_assignment(), bool))

    def test_supports_activity_lookup(self):
        """Tests supports_activity_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_activity_lookup(), bool))

    def test_supports_activity_admin(self):
        """Tests supports_activity_admin"""
        self.assertTrue(isinstance(self.mgr.supports_activity_admin(), bool))

    def test_supports_activity_objective_bank(self):
        """Tests supports_activity_objective_bank"""
        self.assertTrue(isinstance(self.mgr.supports_activity_objective_bank(), bool))

    def test_supports_activity_objective_bank_assignment(self):
        """Tests supports_activity_objective_bank_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_activity_objective_bank_assignment(), bool))

    def test_supports_proficiency_lookup(self):
        """Tests supports_proficiency_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_proficiency_lookup(), bool))

    def test_supports_proficiency_query(self):
        """Tests supports_proficiency_query"""
        self.assertTrue(isinstance(self.mgr.supports_proficiency_query(), bool))

    def test_supports_proficiency_admin(self):
        """Tests supports_proficiency_admin"""
        self.assertTrue(isinstance(self.mgr.supports_proficiency_admin(), bool))

    def test_supports_objective_bank_lookup(self):
        """Tests supports_objective_bank_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_objective_bank_lookup(), bool))

    def test_supports_objective_bank_admin(self):
        """Tests supports_objective_bank_admin"""
        self.assertTrue(isinstance(self.mgr.supports_objective_bank_admin(), bool))

    def test_supports_objective_bank_hierarchy(self):
        """Tests supports_objective_bank_hierarchy"""
        self.assertTrue(isinstance(self.mgr.supports_objective_bank_hierarchy(), bool))

    def test_supports_objective_bank_hierarchy_design(self):
        """Tests supports_objective_bank_hierarchy_design"""
        self.assertTrue(isinstance(self.mgr.supports_objective_bank_hierarchy_design(), bool))

    def test_get_objective_record_types(self):
        """Tests get_objective_record_types"""
        self.assertTrue(isinstance(self.mgr.get_objective_record_types(), abc_type_list))

    def test_get_objective_search_record_types(self):
        """Tests get_objective_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_objective_search_record_types(), abc_type_list))

    def test_get_activity_record_types(self):
        """Tests get_activity_record_types"""
        self.assertTrue(isinstance(self.mgr.get_activity_record_types(), abc_type_list))

    def test_get_activity_search_record_types(self):
        """Tests get_activity_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_activity_search_record_types(), abc_type_list))

    def test_get_proficiency_record_types(self):
        """Tests get_proficiency_record_types"""
        self.assertTrue(isinstance(self.mgr.get_proficiency_record_types(), abc_type_list))

    def test_get_proficiency_search_record_types(self):
        """Tests get_proficiency_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_proficiency_search_record_types(), abc_type_list))

    def test_get_objective_bank_record_types(self):
        """Tests get_objective_bank_record_types"""
        self.assertTrue(isinstance(self.mgr.get_objective_bank_record_types(), abc_type_list))

    def test_get_objective_bank_search_record_types(self):
        """Tests get_objective_bank_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_objective_bank_search_record_types(), abc_type_list))


class TestLearningManager(unittest.TestCase):
    """Tests for LearningManager"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for learning manager tests'
        catalog = cls.svc_mgr.create_objective_bank(create_form)
        cls.catalog_id = catalog.get_id()
        cls.mgr = Runtime().get_manager('LEARNING', 'TEST_JSON_1', (3, 0, 0))

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_objective_bank(cls.catalog_id)


    def test_get_objective_lookup_session(self):
        """Tests get_objective_lookup_session"""
        if self.mgr.supports_objective_lookup():
            self.mgr.get_objective_lookup_session()

    def test_get_objective_lookup_session_for_objective_bank(self):
        """Tests get_objective_lookup_session_for_objective_bank"""
        if self.mgr.supports_objective_lookup():
            self.mgr.get_objective_lookup_session_for_objective_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_objective_lookup_session_for_objective_bank()

    def test_get_objective_query_session(self):
        """Tests get_objective_query_session"""
        if self.mgr.supports_objective_query():
            self.mgr.get_objective_query_session()

    def test_get_objective_query_session_for_objective_bank(self):
        """Tests get_objective_query_session_for_objective_bank"""
        if self.mgr.supports_objective_query():
            self.mgr.get_objective_query_session_for_objective_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_objective_query_session_for_objective_bank()

    @unittest.skip('unimplemented test')
    def test_get_objective_admin_session(self):
        """Tests get_objective_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_admin_session_for_objective_bank(self):
        """Tests get_objective_admin_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_session(self):
        """Tests get_objective_hierarchy_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_session_for_objective_bank(self):
        """Tests get_objective_hierarchy_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_design_session(self):
        """Tests get_objective_hierarchy_design_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_design_session_for_objective_bank(self):
        """Tests get_objective_hierarchy_design_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_sequencing_session(self):
        """Tests get_objective_sequencing_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_sequencing_session_for_objective_bank(self):
        """Tests get_objective_sequencing_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_objective_bank_session(self):
        """Tests get_objective_objective_bank_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_objective_bank_assignment_session(self):
        """Tests get_objective_objective_bank_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_session(self):
        """Tests get_objective_requisite_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_session_for_objective_bank(self):
        """Tests get_objective_requisite_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_assignment_session(self):
        """Tests get_objective_requisite_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_assignment_session_for_objective_bank(self):
        """Tests get_objective_requisite_assignment_session_for_objective_bank"""
        pass

    def test_get_activity_lookup_session(self):
        """Tests get_activity_lookup_session"""
        if self.mgr.supports_activity_lookup():
            self.mgr.get_activity_lookup_session()

    def test_get_activity_lookup_session_for_objective_bank(self):
        """Tests get_activity_lookup_session_for_objective_bank"""
        if self.mgr.supports_activity_lookup():
            self.mgr.get_activity_lookup_session_for_objective_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_activity_lookup_session_for_objective_bank()

    @unittest.skip('unimplemented test')
    def test_get_activity_admin_session(self):
        """Tests get_activity_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_admin_session_for_objective_bank(self):
        """Tests get_activity_admin_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_objective_bank_session(self):
        """Tests get_activity_objective_bank_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_objective_bank_assignment_session(self):
        """Tests get_activity_objective_bank_assignment_session"""
        pass

    def test_get_proficiency_lookup_session(self):
        """Tests get_proficiency_lookup_session"""
        if self.mgr.supports_proficiency_lookup():
            self.mgr.get_proficiency_lookup_session()

    def test_get_proficiency_lookup_session_for_objective_bank(self):
        """Tests get_proficiency_lookup_session_for_objective_bank"""
        if self.mgr.supports_proficiency_lookup():
            self.mgr.get_proficiency_lookup_session_for_objective_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_proficiency_lookup_session_for_objective_bank()

    def test_get_proficiency_query_session(self):
        """Tests get_proficiency_query_session"""
        if self.mgr.supports_proficiency_query():
            self.mgr.get_proficiency_query_session()

    def test_get_proficiency_query_session_for_objective_bank(self):
        """Tests get_proficiency_query_session_for_objective_bank"""
        if self.mgr.supports_proficiency_query():
            self.mgr.get_proficiency_query_session_for_objective_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_proficiency_query_session_for_objective_bank()

    @unittest.skip('unimplemented test')
    def test_get_proficiency_admin_session(self):
        """Tests get_proficiency_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiency_admin_session_for_objective_bank(self):
        """Tests get_proficiency_admin_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_lookup_session(self):
        """Tests get_objective_bank_lookup_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_admin_session(self):
        """Tests get_objective_bank_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_hierarchy_session(self):
        """Tests get_objective_bank_hierarchy_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_hierarchy_design_session(self):
        """Tests get_objective_bank_hierarchy_design_session"""
        pass

    def test_get_learning_batch_manager(self):
        """Tests get_learning_batch_manager"""
        if self.mgr.supports_learning_batch():
            self.mgr.get_learning_batch_manager()


class TestLearningProxyManager(unittest.TestCase):
    """Tests for LearningProxyManager"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for learning proxy manager tests'
        catalog = cls.svc_mgr.create_objective_bank(create_form)
        cls.catalog_id = catalog.get_id()
        cls.mgr = Runtime().get_proxy_manager('LEARNING', 'TEST_JSON_1', (3, 0, 0))

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_objective_bank(cls.catalog_id)


    def test_get_objective_lookup_session(self):
        """Tests get_objective_lookup_session"""
        if self.mgr.supports_objective_lookup():
            self.mgr.get_objective_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_objective_lookup_session()

    def test_get_objective_lookup_session_for_objective_bank(self):
        """Tests get_objective_lookup_session_for_objective_bank"""
        if self.mgr.supports_objective_lookup():
            self.mgr.get_objective_lookup_session_for_objective_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_objective_lookup_session_for_objective_bank()

    def test_get_objective_query_session(self):
        """Tests get_objective_query_session"""
        if self.mgr.supports_objective_query():
            self.mgr.get_objective_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_objective_query_session()

    def test_get_objective_query_session_for_objective_bank(self):
        """Tests get_objective_query_session_for_objective_bank"""
        if self.mgr.supports_objective_query():
            self.mgr.get_objective_query_session_for_objective_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_objective_query_session_for_objective_bank()

    @unittest.skip('unimplemented test')
    def test_get_objective_admin_session(self):
        """Tests get_objective_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_admin_session_for_objective_bank(self):
        """Tests get_objective_admin_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_session(self):
        """Tests get_objective_hierarchy_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_session_for_objective_bank(self):
        """Tests get_objective_hierarchy_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_design_session(self):
        """Tests get_objective_hierarchy_design_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_hierarchy_design_session_for_objective_bank(self):
        """Tests get_objective_hierarchy_design_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_sequencing_session(self):
        """Tests get_objective_sequencing_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_sequencing_session_for_objective_bank(self):
        """Tests get_objective_sequencing_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_objective_bank_session(self):
        """Tests get_objective_objective_bank_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_objective_bank_assignment_session(self):
        """Tests get_objective_objective_bank_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_session(self):
        """Tests get_objective_requisite_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_session_for_objective_bank(self):
        """Tests get_objective_requisite_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_assignment_session(self):
        """Tests get_objective_requisite_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_requisite_assignment_session_for_objective_bank(self):
        """Tests get_objective_requisite_assignment_session_for_objective_bank"""
        pass

    def test_get_activity_lookup_session(self):
        """Tests get_activity_lookup_session"""
        if self.mgr.supports_activity_lookup():
            self.mgr.get_activity_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_activity_lookup_session()

    def test_get_activity_lookup_session_for_objective_bank(self):
        """Tests get_activity_lookup_session_for_objective_bank"""
        if self.mgr.supports_activity_lookup():
            self.mgr.get_activity_lookup_session_for_objective_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_activity_lookup_session_for_objective_bank()

    @unittest.skip('unimplemented test')
    def test_get_activity_admin_session(self):
        """Tests get_activity_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_admin_session_for_objective_bank(self):
        """Tests get_activity_admin_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_objective_bank_session(self):
        """Tests get_activity_objective_bank_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_objective_bank_assignment_session(self):
        """Tests get_activity_objective_bank_assignment_session"""
        pass

    def test_get_proficiency_lookup_session(self):
        """Tests get_proficiency_lookup_session"""
        if self.mgr.supports_proficiency_lookup():
            self.mgr.get_proficiency_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_proficiency_lookup_session()

    def test_get_proficiency_lookup_session_for_objective_bank(self):
        """Tests get_proficiency_lookup_session_for_objective_bank"""
        if self.mgr.supports_proficiency_lookup():
            self.mgr.get_proficiency_lookup_session_for_objective_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_proficiency_lookup_session_for_objective_bank()

    def test_get_proficiency_query_session(self):
        """Tests get_proficiency_query_session"""
        if self.mgr.supports_proficiency_query():
            self.mgr.get_proficiency_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_proficiency_query_session()

    def test_get_proficiency_query_session_for_objective_bank(self):
        """Tests get_proficiency_query_session_for_objective_bank"""
        if self.mgr.supports_proficiency_query():
            self.mgr.get_proficiency_query_session_for_objective_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_proficiency_query_session_for_objective_bank()

    @unittest.skip('unimplemented test')
    def test_get_proficiency_admin_session(self):
        """Tests get_proficiency_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiency_admin_session_for_objective_bank(self):
        """Tests get_proficiency_admin_session_for_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_lookup_session(self):
        """Tests get_objective_bank_lookup_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_admin_session(self):
        """Tests get_objective_bank_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_hierarchy_session(self):
        """Tests get_objective_bank_hierarchy_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_hierarchy_design_session(self):
        """Tests get_objective_bank_hierarchy_design_session"""
        pass

    def test_get_learning_batch_proxy_manager(self):
        """Tests get_learning_batch_proxy_manager"""
        if self.mgr.supports_learning_batch():
            self.mgr.get_learning_batch_proxy_manager()


