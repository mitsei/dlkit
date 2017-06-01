"""Unit tests of assessment.authoring managers."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.objects import TypeList as abc_type_list
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAssessmentAuthoringProfile(unittest.TestCase):
    """Tests for AssessmentAuthoringProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_assessment_part_lookup(self):
        """Tests supports_assessment_part_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_part_lookup(), bool))

    def test_supports_assessment_part_query(self):
        """Tests supports_assessment_part_query"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_part_query(), bool))

    def test_supports_assessment_part_admin(self):
        """Tests supports_assessment_part_admin"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_part_admin(), bool))

    def test_supports_assessment_part_item(self):
        """Tests supports_assessment_part_item"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_part_item(), bool))

    def test_supports_assessment_part_item_design(self):
        """Tests supports_assessment_part_item_design"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_part_item_design(), bool))

    def test_supports_sequence_rule_lookup(self):
        """Tests supports_sequence_rule_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_sequence_rule_lookup(), bool))

    def test_supports_sequence_rule_admin(self):
        """Tests supports_sequence_rule_admin"""
        self.assertTrue(isinstance(self.mgr.supports_sequence_rule_admin(), bool))

    def test_get_assessment_part_record_types(self):
        """Tests get_assessment_part_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_part_record_types(), abc_type_list))

    def test_get_assessment_part_search_record_types(self):
        """Tests get_assessment_part_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_part_search_record_types(), abc_type_list))

    def test_get_sequence_rule_record_types(self):
        """Tests get_sequence_rule_record_types"""
        self.assertTrue(isinstance(self.mgr.get_sequence_rule_record_types(), abc_type_list))

    def test_get_sequence_rule_search_record_types(self):
        """Tests get_sequence_rule_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_sequence_rule_search_record_types(), abc_type_list))

    def test_get_sequence_rule_enabler_record_types(self):
        """Tests get_sequence_rule_enabler_record_types"""
        self.assertTrue(isinstance(self.mgr.get_sequence_rule_enabler_record_types(), abc_type_list))

    def test_get_sequence_rule_enabler_search_record_types(self):
        """Tests get_sequence_rule_enabler_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_sequence_rule_enabler_search_record_types(), abc_type_list))


class TestAssessmentAuthoringManager(unittest.TestCase):
    """Tests for AssessmentAuthoringManager"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for assessment.authoring manager tests'
        catalog = cls.svc_mgr.create_bank(create_form)
        cls.catalog_id = catalog.get_id()
        cls.mgr = Runtime().get_manager('ASSESSMENT_AUTHORING', 'TEST_JSON_1', (3, 0, 0))

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog_id)

    def test_get_assessment_part_lookup_session(self):
        """Tests get_assessment_part_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session()

    def test_get_assessment_part_lookup_session_for_bank(self):
        """Tests get_assessment_part_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_lookup_session_for_bank()

    def test_get_assessment_part_query_session(self):
        """Tests get_assessment_part_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session()

    def test_get_assessment_part_query_session_for_bank(self):
        """Tests get_assessment_part_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_query_session_for_bank()

    def test_get_assessment_part_admin_session(self):
        """Tests get_assessment_part_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session()

    def test_get_assessment_part_admin_session_for_bank(self):
        """Tests get_assessment_part_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_admin_session_for_bank()

    def test_get_sequence_rule_lookup_session(self):
        """Tests get_sequence_rule_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session()

    def test_get_sequence_rule_lookup_session_for_bank(self):
        """Tests get_sequence_rule_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank()

    def test_get_sequence_rule_admin_session(self):
        """Tests get_sequence_rule_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session()

    def test_get_sequence_rule_admin_session_for_bank(self):
        """Tests get_sequence_rule_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_admin_session_for_bank()


class TestAssessmentAuthoringProxyManager(unittest.TestCase):
    """Tests for AssessmentAuthoringProxyManager"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for assessment.authoring manager tests'
        catalog = cls.svc_mgr.create_bank(create_form)
        cls.catalog_id = catalog.get_id()
        cls.mgr = Runtime().get_manager('ASSESSMENT_AUTHORING', 'TEST_JSON_1', (3, 0, 0))

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog_id)

    def test_get_assessment_part_lookup_session(self):
        """Tests get_assessment_part_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_lookup_session()

    def test_get_assessment_part_lookup_session_for_bank(self):
        """Tests get_assessment_part_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_lookup_session_for_bank()

    def test_get_assessment_part_query_session(self):
        """Tests get_assessment_part_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_query_session()

    def test_get_assessment_part_query_session_for_bank(self):
        """Tests get_assessment_part_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_query_session_for_bank()

    def test_get_assessment_part_admin_session(self):
        """Tests get_assessment_part_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_admin_session()

    def test_get_assessment_part_admin_session_for_bank(self):
        """Tests get_assessment_part_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_admin_session_for_bank()

    def test_get_sequence_rule_lookup_session(self):
        """Tests get_sequence_rule_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_lookup_session()

    def test_get_sequence_rule_lookup_session_for_bank(self):
        """Tests get_sequence_rule_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank()

    def test_get_sequence_rule_admin_session(self):
        """Tests get_sequence_rule_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_admin_session()

    def test_get_sequence_rule_admin_session_for_bank(self):
        """Tests get_sequence_rule_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_admin_session_for_bank()
