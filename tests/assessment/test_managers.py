"""Unit tests of assessment managers."""


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


class TestAssessmentProfile(unittest.TestCase):
    """Tests for AssessmentProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_assessment(self):
        """Tests supports_assessment"""
        self.assertTrue(isinstance(self.mgr.supports_assessment(), bool))

    def test_supports_assessment_results(self):
        """Tests supports_assessment_results"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_results(), bool))

    def test_supports_item_lookup(self):
        """Tests supports_item_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_item_lookup(), bool))

    def test_supports_item_query(self):
        """Tests supports_item_query"""
        self.assertTrue(isinstance(self.mgr.supports_item_query(), bool))

    def test_supports_item_search(self):
        """Tests supports_item_search"""
        self.assertTrue(isinstance(self.mgr.supports_item_search(), bool))

    def test_supports_item_admin(self):
        """Tests supports_item_admin"""
        self.assertTrue(isinstance(self.mgr.supports_item_admin(), bool))

    def test_supports_item_notification(self):
        """Tests supports_item_notification"""
        self.assertTrue(isinstance(self.mgr.supports_item_notification(), bool))

    def test_supports_item_bank(self):
        """Tests supports_item_bank"""
        self.assertTrue(isinstance(self.mgr.supports_item_bank(), bool))

    def test_supports_item_bank_assignment(self):
        """Tests supports_item_bank_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_item_bank_assignment(), bool))

    def test_supports_assessment_lookup(self):
        """Tests supports_assessment_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_lookup(), bool))

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_query(), bool))

    def test_supports_assessment_admin(self):
        """Tests supports_assessment_admin"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_admin(), bool))

    def test_supports_assessment_bank(self):
        """Tests supports_assessment_bank"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_bank(), bool))

    def test_supports_assessment_bank_assignment(self):
        """Tests supports_assessment_bank_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_bank_assignment(), bool))

    def test_supports_assessment_basic_authoring(self):
        """Tests supports_assessment_basic_authoring"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_basic_authoring(), bool))

    def test_supports_assessment_offered_lookup(self):
        """Tests supports_assessment_offered_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_offered_lookup(), bool))

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_offered_query(), bool))

    def test_supports_assessment_offered_admin(self):
        """Tests supports_assessment_offered_admin"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_offered_admin(), bool))

    def test_supports_assessment_offered_bank(self):
        """Tests supports_assessment_offered_bank"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_offered_bank(), bool))

    def test_supports_assessment_offered_bank_assignment(self):
        """Tests supports_assessment_offered_bank_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_offered_bank_assignment(), bool))

    def test_supports_assessment_taken_lookup(self):
        """Tests supports_assessment_taken_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_taken_lookup(), bool))

    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_taken_query(), bool))

    def test_supports_assessment_taken_admin(self):
        """Tests supports_assessment_taken_admin"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_taken_admin(), bool))

    def test_supports_assessment_taken_bank(self):
        """Tests supports_assessment_taken_bank"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_taken_bank(), bool))

    def test_supports_assessment_taken_bank_assignment(self):
        """Tests supports_assessment_taken_bank_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_assessment_taken_bank_assignment(), bool))

    def test_supports_bank_lookup(self):
        """Tests supports_bank_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_bank_lookup(), bool))

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        self.assertTrue(isinstance(self.mgr.supports_bank_query(), bool))

    def test_supports_bank_admin(self):
        """Tests supports_bank_admin"""
        self.assertTrue(isinstance(self.mgr.supports_bank_admin(), bool))

    def test_supports_bank_hierarchy(self):
        """Tests supports_bank_hierarchy"""
        self.assertTrue(isinstance(self.mgr.supports_bank_hierarchy(), bool))

    def test_supports_bank_hierarchy_design(self):
        """Tests supports_bank_hierarchy_design"""
        self.assertTrue(isinstance(self.mgr.supports_bank_hierarchy_design(), bool))

    def test_get_item_record_types(self):
        """Tests get_item_record_types"""
        self.assertTrue(isinstance(self.mgr.get_item_record_types(), abc_type_list))

    def test_get_item_search_record_types(self):
        """Tests get_item_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_item_search_record_types(), abc_type_list))

    def test_get_assessment_record_types(self):
        """Tests get_assessment_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_record_types(), abc_type_list))

    def test_get_assessment_search_record_types(self):
        """Tests get_assessment_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_search_record_types(), abc_type_list))

    def test_get_assessment_offered_record_types(self):
        """Tests get_assessment_offered_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_offered_record_types(), abc_type_list))

    def test_get_assessment_offered_search_record_types(self):
        """Tests get_assessment_offered_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_offered_search_record_types(), abc_type_list))

    def test_get_assessment_taken_record_types(self):
        """Tests get_assessment_taken_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_taken_record_types(), abc_type_list))

    def test_get_assessment_taken_search_record_types(self):
        """Tests get_assessment_taken_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_taken_search_record_types(), abc_type_list))

    def test_get_assessment_section_record_types(self):
        """Tests get_assessment_section_record_types"""
        self.assertTrue(isinstance(self.mgr.get_assessment_section_record_types(), abc_type_list))

    def test_get_bank_record_types(self):
        """Tests get_bank_record_types"""
        self.assertTrue(isinstance(self.mgr.get_bank_record_types(), abc_type_list))

    def test_get_bank_search_record_types(self):
        """Tests get_bank_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_bank_search_record_types(), abc_type_list))


class TestAssessmentManager(unittest.TestCase):
    """Tests for AssessmentManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for assessment manager tests'
        catalog = cls.svc_mgr.create_bank(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('ASSESSMENT', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog_id)

    def test_get_assessment_session(self):
        """Tests get_assessment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment():
            self.svc_mgr.get_assessment_session()

    def test_get_assessment_session_for_bank(self):
        """Tests get_assessment_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment():
            self.svc_mgr.get_assessment_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_session_for_bank()

    def test_get_assessment_results_session(self):
        """Tests get_assessment_results_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_results():
            self.svc_mgr.get_assessment_results_session()

    def test_get_assessment_results_session_for_bank(self):
        """Tests get_assessment_results_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_results():
            self.svc_mgr.get_assessment_results_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_results_session_for_bank()

    def test_get_item_lookup_session(self):
        """Tests get_item_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_item_lookup():
            self.svc_mgr.get_item_lookup_session()

    def test_get_item_lookup_session_for_bank(self):
        """Tests get_item_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_item_lookup():
            self.svc_mgr.get_item_lookup_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_lookup_session_for_bank()

    def test_get_item_query_session(self):
        """Tests get_item_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_item_query():
            self.svc_mgr.get_item_query_session()

    def test_get_item_query_session_for_bank(self):
        """Tests get_item_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_item_query():
            self.svc_mgr.get_item_query_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_query_session_for_bank()

    def test_get_item_search_session(self):
        """Tests get_item_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_search():
            self.svc_mgr.get_item_search_session()

    def test_get_item_search_session_for_bank(self):
        """Tests get_item_search_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_item_search():
            self.svc_mgr.get_item_search_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_search_session_for_bank()

    def test_get_item_admin_session(self):
        """Tests get_item_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_admin():
            self.svc_mgr.get_item_admin_session()

    def test_get_item_admin_session_for_bank(self):
        """Tests get_item_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_item_admin():
            self.svc_mgr.get_item_admin_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_admin_session_for_bank()

    def test_get_item_notification_session(self):
        """Tests get_item_notification_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_template
        if self.svc_mgr.supports_item_notification():
            self.svc_mgr.get_item_notification_session(self.receiver)

    def test_get_item_bank_session(self):
        """Tests get_item_bank_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_bank():
            self.svc_mgr.get_item_bank_session()

    def test_get_item_bank_assignment_session(self):
        """Tests get_item_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_bank_assignment():
            self.svc_mgr.get_item_bank_assignment_session()

    def test_get_assessment_lookup_session(self):
        """Tests get_assessment_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_lookup():
            self.svc_mgr.get_assessment_lookup_session()

    def test_get_assessment_lookup_session_for_bank(self):
        """Tests get_assessment_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_lookup():
            self.svc_mgr.get_assessment_lookup_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_lookup_session_for_bank()

    def test_get_assessment_query_session(self):
        """Tests get_assessment_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_query():
            self.svc_mgr.get_assessment_query_session()

    def test_get_assessment_query_session_for_bank(self):
        """Tests get_assessment_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_query():
            self.svc_mgr.get_assessment_query_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_query_session_for_bank()

    def test_get_assessment_admin_session(self):
        """Tests get_assessment_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_admin():
            self.svc_mgr.get_assessment_admin_session()

    def test_get_assessment_admin_session_for_bank(self):
        """Tests get_assessment_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_admin():
            self.svc_mgr.get_assessment_admin_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_admin_session_for_bank()

    def test_get_assessment_bank_session(self):
        """Tests get_assessment_bank_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_bank():
            self.svc_mgr.get_assessment_bank_session()

    def test_get_assessment_bank_assignment_session(self):
        """Tests get_assessment_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_bank_assignment():
            self.svc_mgr.get_assessment_bank_assignment_session()

    def test_get_assessment_basic_authoring_session(self):
        """Tests get_assessment_basic_authoring_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_basic_authoring():
            self.svc_mgr.get_assessment_basic_authoring_session()

    def test_get_assessment_basic_authoring_session_for_bank(self):
        """Tests get_assessment_basic_authoring_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_basic_authoring():
            self.svc_mgr.get_assessment_basic_authoring_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_basic_authoring_session_for_bank()

    def test_get_assessment_offered_lookup_session(self):
        """Tests get_assessment_offered_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_offered_lookup():
            self.svc_mgr.get_assessment_offered_lookup_session()

    def test_get_assessment_offered_lookup_session_for_bank(self):
        """Tests get_assessment_offered_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_offered_lookup():
            self.svc_mgr.get_assessment_offered_lookup_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_lookup_session_for_bank()

    def test_get_assessment_offered_query_session(self):
        """Tests get_assessment_offered_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_offered_query():
            self.svc_mgr.get_assessment_offered_query_session()

    def test_get_assessment_offered_query_session_for_bank(self):
        """Tests get_assessment_offered_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_offered_query():
            self.svc_mgr.get_assessment_offered_query_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_query_session_for_bank()

    def test_get_assessment_offered_admin_session(self):
        """Tests get_assessment_offered_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_offered_admin():
            self.svc_mgr.get_assessment_offered_admin_session()

    def test_get_assessment_offered_admin_session_for_bank(self):
        """Tests get_assessment_offered_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_offered_admin():
            self.svc_mgr.get_assessment_offered_admin_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_admin_session_for_bank()

    def test_get_assessment_offered_bank_session(self):
        """Tests get_assessment_offered_bank_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_offered_bank():
            self.svc_mgr.get_assessment_offered_bank_session()

    def test_get_assessment_offered_bank_assignment_session(self):
        """Tests get_assessment_offered_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_offered_bank_assignment():
            self.svc_mgr.get_assessment_offered_bank_assignment_session()

    def test_get_assessment_taken_lookup_session(self):
        """Tests get_assessment_taken_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_taken_lookup():
            self.svc_mgr.get_assessment_taken_lookup_session()

    def test_get_assessment_taken_lookup_session_for_bank(self):
        """Tests get_assessment_taken_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_taken_lookup():
            self.svc_mgr.get_assessment_taken_lookup_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_lookup_session_for_bank()

    def test_get_assessment_taken_query_session(self):
        """Tests get_assessment_taken_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_taken_query():
            self.svc_mgr.get_assessment_taken_query_session()

    def test_get_assessment_taken_query_session_for_bank(self):
        """Tests get_assessment_taken_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_taken_query():
            self.svc_mgr.get_assessment_taken_query_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_query_session_for_bank()

    def test_get_assessment_taken_admin_session(self):
        """Tests get_assessment_taken_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_taken_admin():
            self.svc_mgr.get_assessment_taken_admin_session()

    def test_get_assessment_taken_admin_session_for_bank(self):
        """Tests get_assessment_taken_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_taken_admin():
            self.svc_mgr.get_assessment_taken_admin_session_for_bank(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_admin_session_for_bank()

    def test_get_assessment_taken_bank_session(self):
        """Tests get_assessment_taken_bank_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_taken_bank():
            self.svc_mgr.get_assessment_taken_bank_session()

    def test_get_assessment_taken_bank_assignment_session(self):
        """Tests get_assessment_taken_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_taken_bank_assignment():
            self.svc_mgr.get_assessment_taken_bank_assignment_session()

    def test_get_bank_lookup_session(self):
        """Tests get_bank_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_lookup():
            self.svc_mgr.get_bank_lookup_session()

    def test_get_bank_query_session(self):
        """Tests get_bank_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_query():
            self.svc_mgr.get_bank_query_session()

    def test_get_bank_admin_session(self):
        """Tests get_bank_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_admin():
            self.svc_mgr.get_bank_admin_session()

    def test_get_bank_hierarchy_session(self):
        """Tests get_bank_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_hierarchy():
            self.svc_mgr.get_bank_hierarchy_session()

    def test_get_bank_hierarchy_design_session(self):
        """Tests get_bank_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_hierarchy_design():
            self.svc_mgr.get_bank_hierarchy_design_session()

    def test_get_assessment_authoring_manager(self):
        """Tests get_assessment_authoring_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_assessment_authoring():
            self.svc_mgr.get_assessment_authoring_manager()

    def test_get_assessment_batch_manager(self):
        """Tests get_assessment_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_assessment_batch():
            self.svc_mgr.get_assessment_batch_manager()


class TestAssessmentProxyManager(unittest.TestCase):
    """Tests for AssessmentProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for assessment proxy manager tests'
        catalog = cls.svc_mgr.create_bank(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('ASSESSMENT', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog_id)

    def test_get_assessment_session(self):
        """Tests get_assessment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment():
            self.svc_mgr.get_assessment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_session()

    def test_get_assessment_session_for_bank(self):
        """Tests get_assessment_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment():
            self.svc_mgr.get_assessment_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_session_for_bank()

    def test_get_assessment_results_session(self):
        """Tests get_assessment_results_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_results():
            self.svc_mgr.get_assessment_results_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_results_session()

    def test_get_assessment_results_session_for_bank(self):
        """Tests get_assessment_results_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_results():
            self.svc_mgr.get_assessment_results_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_results_session_for_bank()

    def test_get_item_lookup_session(self):
        """Tests get_item_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_item_lookup():
            self.svc_mgr.get_item_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_lookup_session()

    def test_get_item_lookup_session_for_bank(self):
        """Tests get_item_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_item_lookup():
            self.svc_mgr.get_item_lookup_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_lookup_session_for_bank()

    def test_get_item_query_session(self):
        """Tests get_item_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_item_query():
            self.svc_mgr.get_item_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_query_session()

    def test_get_item_query_session_for_bank(self):
        """Tests get_item_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_item_query():
            self.svc_mgr.get_item_query_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_query_session_for_bank()

    def test_get_item_search_session(self):
        """Tests get_item_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_search():
            self.svc_mgr.get_item_search_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_search_session()

    def test_get_item_search_session_for_bank(self):
        """Tests get_item_search_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_item_search():
            self.svc_mgr.get_item_search_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_search_session_for_bank()

    def test_get_item_admin_session(self):
        """Tests get_item_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_admin():
            self.svc_mgr.get_item_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_admin_session()

    def test_get_item_admin_session_for_bank(self):
        """Tests get_item_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_item_admin():
            self.svc_mgr.get_item_admin_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_admin_session_for_bank()

    def test_get_item_notification_session(self):
        """Tests get_item_notification_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_template
        if self.svc_mgr.supports_item_notification():
            self.svc_mgr.get_item_notification_session(self.receiver, proxy=PROXY)

    def test_get_item_bank_session(self):
        """Tests get_item_bank_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_bank():
            self.svc_mgr.get_item_bank_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_bank_session()

    def test_get_item_bank_assignment_session(self):
        """Tests get_item_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_item_bank_assignment():
            self.svc_mgr.get_item_bank_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_item_bank_assignment_session()

    def test_get_assessment_lookup_session(self):
        """Tests get_assessment_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_lookup():
            self.svc_mgr.get_assessment_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_lookup_session()

    def test_get_assessment_lookup_session_for_bank(self):
        """Tests get_assessment_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_lookup():
            self.svc_mgr.get_assessment_lookup_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_lookup_session_for_bank()

    def test_get_assessment_query_session(self):
        """Tests get_assessment_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_query():
            self.svc_mgr.get_assessment_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_query_session()

    def test_get_assessment_query_session_for_bank(self):
        """Tests get_assessment_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_query():
            self.svc_mgr.get_assessment_query_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_query_session_for_bank()

    def test_get_assessment_admin_session(self):
        """Tests get_assessment_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_admin():
            self.svc_mgr.get_assessment_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_admin_session()

    def test_get_assessment_admin_session_for_bank(self):
        """Tests get_assessment_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_admin():
            self.svc_mgr.get_assessment_admin_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_admin_session_for_bank()

    def test_get_assessment_bank_session(self):
        """Tests get_assessment_bank_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_bank():
            self.svc_mgr.get_assessment_bank_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_bank_session()

    def test_get_assessment_bank_assignment_session(self):
        """Tests get_assessment_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_bank_assignment():
            self.svc_mgr.get_assessment_bank_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_bank_assignment_session()

    def test_get_assessment_basic_authoring_session(self):
        """Tests get_assessment_basic_authoring_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_basic_authoring():
            self.svc_mgr.get_assessment_basic_authoring_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_basic_authoring_session()

    def test_get_assessment_basic_authoring_session_for_bank(self):
        """Tests get_assessment_basic_authoring_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_basic_authoring():
            self.svc_mgr.get_assessment_basic_authoring_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_basic_authoring_session_for_bank()

    def test_get_assessment_offered_lookup_session(self):
        """Tests get_assessment_offered_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_offered_lookup():
            self.svc_mgr.get_assessment_offered_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_lookup_session()

    def test_get_assessment_offered_lookup_session_for_bank(self):
        """Tests get_assessment_offered_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_offered_lookup():
            self.svc_mgr.get_assessment_offered_lookup_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_lookup_session_for_bank()

    def test_get_assessment_offered_query_session(self):
        """Tests get_assessment_offered_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_offered_query():
            self.svc_mgr.get_assessment_offered_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_query_session()

    def test_get_assessment_offered_query_session_for_bank(self):
        """Tests get_assessment_offered_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_offered_query():
            self.svc_mgr.get_assessment_offered_query_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_query_session_for_bank()

    def test_get_assessment_offered_admin_session(self):
        """Tests get_assessment_offered_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_offered_admin():
            self.svc_mgr.get_assessment_offered_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_admin_session()

    def test_get_assessment_offered_admin_session_for_bank(self):
        """Tests get_assessment_offered_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_offered_admin():
            self.svc_mgr.get_assessment_offered_admin_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_admin_session_for_bank()

    def test_get_assessment_offered_bank_session(self):
        """Tests get_assessment_offered_bank_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_offered_bank():
            self.svc_mgr.get_assessment_offered_bank_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_bank_session()

    def test_get_assessment_offered_bank_assignment_session(self):
        """Tests get_assessment_offered_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_offered_bank_assignment():
            self.svc_mgr.get_assessment_offered_bank_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_offered_bank_assignment_session()

    def test_get_assessment_taken_lookup_session(self):
        """Tests get_assessment_taken_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_taken_lookup():
            self.svc_mgr.get_assessment_taken_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_lookup_session()

    def test_get_assessment_taken_lookup_session_for_bank(self):
        """Tests get_assessment_taken_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_taken_lookup():
            self.svc_mgr.get_assessment_taken_lookup_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_lookup_session_for_bank()

    def test_get_assessment_taken_query_session(self):
        """Tests get_assessment_taken_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_taken_query():
            self.svc_mgr.get_assessment_taken_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_query_session()

    def test_get_assessment_taken_query_session_for_bank(self):
        """Tests get_assessment_taken_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_taken_query():
            self.svc_mgr.get_assessment_taken_query_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_query_session_for_bank()

    def test_get_assessment_taken_admin_session(self):
        """Tests get_assessment_taken_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_taken_admin():
            self.svc_mgr.get_assessment_taken_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_admin_session()

    def test_get_assessment_taken_admin_session_for_bank(self):
        """Tests get_assessment_taken_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_taken_admin():
            self.svc_mgr.get_assessment_taken_admin_session_for_bank(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_admin_session_for_bank()

    def test_get_assessment_taken_bank_session(self):
        """Tests get_assessment_taken_bank_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_taken_bank():
            self.svc_mgr.get_assessment_taken_bank_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_bank_session()

    def test_get_assessment_taken_bank_assignment_session(self):
        """Tests get_assessment_taken_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_taken_bank_assignment():
            self.svc_mgr.get_assessment_taken_bank_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_assessment_taken_bank_assignment_session()

    def test_get_bank_lookup_session(self):
        """Tests get_bank_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_lookup():
            self.svc_mgr.get_bank_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bank_lookup_session()

    def test_get_bank_query_session(self):
        """Tests get_bank_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_query():
            self.svc_mgr.get_bank_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bank_query_session()

    def test_get_bank_admin_session(self):
        """Tests get_bank_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_admin():
            self.svc_mgr.get_bank_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bank_admin_session()

    def test_get_bank_hierarchy_session(self):
        """Tests get_bank_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_hierarchy():
            self.svc_mgr.get_bank_hierarchy_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bank_hierarchy_session()

    def test_get_bank_hierarchy_design_session(self):
        """Tests get_bank_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bank_hierarchy_design():
            self.svc_mgr.get_bank_hierarchy_design_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bank_hierarchy_design_session()

    def test_get_assessment_authoring_proxy_manager(self):
        """Tests get_assessment_authoring_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_assessment_authoring():
            self.svc_mgr.get_assessment_authoring_proxy_manager()

    def test_get_assessment_batch_proxy_manager(self):
        """Tests get_assessment_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_assessment_batch():
            self.svc_mgr.get_assessment_batch_proxy_manager()
