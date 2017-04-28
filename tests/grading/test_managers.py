"""Unit tests of grading managers."""


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


class TestGradingProfile(unittest.TestCase):
    """Tests for GradingProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_grade_system_lookup(self):
        """Tests supports_grade_system_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_grade_system_lookup(), bool))

    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        self.assertTrue(isinstance(self.mgr.supports_grade_system_query(), bool))

    def test_supports_grade_system_admin(self):
        """Tests supports_grade_system_admin"""
        self.assertTrue(isinstance(self.mgr.supports_grade_system_admin(), bool))

    def test_supports_grade_entry_lookup(self):
        """Tests supports_grade_entry_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_grade_entry_lookup(), bool))

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        self.assertTrue(isinstance(self.mgr.supports_grade_entry_query(), bool))

    def test_supports_grade_entry_admin(self):
        """Tests supports_grade_entry_admin"""
        self.assertTrue(isinstance(self.mgr.supports_grade_entry_admin(), bool))

    def test_supports_gradebook_column_lookup(self):
        """Tests supports_gradebook_column_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_gradebook_column_lookup(), bool))

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        self.assertTrue(isinstance(self.mgr.supports_gradebook_column_query(), bool))

    def test_supports_gradebook_column_admin(self):
        """Tests supports_gradebook_column_admin"""
        self.assertTrue(isinstance(self.mgr.supports_gradebook_column_admin(), bool))

    def test_supports_gradebook_lookup(self):
        """Tests supports_gradebook_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_gradebook_lookup(), bool))

    def test_supports_gradebook_admin(self):
        """Tests supports_gradebook_admin"""
        self.assertTrue(isinstance(self.mgr.supports_gradebook_admin(), bool))

    def test_get_grade_record_types(self):
        """Tests get_grade_record_types"""
        self.assertTrue(isinstance(self.mgr.get_grade_record_types(), abc_type_list))

    def test_get_grade_system_record_types(self):
        """Tests get_grade_system_record_types"""
        self.assertTrue(isinstance(self.mgr.get_grade_system_record_types(), abc_type_list))

    def test_get_grade_system_search_record_types(self):
        """Tests get_grade_system_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_grade_system_search_record_types(), abc_type_list))

    def test_get_grade_entry_record_types(self):
        """Tests get_grade_entry_record_types"""
        self.assertTrue(isinstance(self.mgr.get_grade_entry_record_types(), abc_type_list))

    def test_get_grade_entry_search_record_types(self):
        """Tests get_grade_entry_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_grade_entry_search_record_types(), abc_type_list))

    def test_get_gradebook_column_record_types(self):
        """Tests get_gradebook_column_record_types"""
        self.assertTrue(isinstance(self.mgr.get_gradebook_column_record_types(), abc_type_list))

    def test_get_gradebook_column_search_record_types(self):
        """Tests get_gradebook_column_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_gradebook_column_search_record_types(), abc_type_list))

    def test_get_gradebook_column_summary_record_types(self):
        """Tests get_gradebook_column_summary_record_types"""
        self.assertTrue(isinstance(self.mgr.get_gradebook_column_summary_record_types(), abc_type_list))

    def test_get_gradebook_record_types(self):
        """Tests get_gradebook_record_types"""
        self.assertTrue(isinstance(self.mgr.get_gradebook_record_types(), abc_type_list))

    def test_get_gradebook_search_record_types(self):
        """Tests get_gradebook_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_gradebook_search_record_types(), abc_type_list))


class TestGradingManager(unittest.TestCase):
    """Tests for GradingManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for grading manager tests'
        catalog = cls.svc_mgr.create_gradebook(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('GRADING', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_gradebook(cls.catalog_id)

    def test_get_grade_system_lookup_session(self):
        """Tests get_grade_system_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session()

    def test_get_grade_system_lookup_session_for_gradebook(self):
        """Tests get_grade_system_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook()

    def test_get_grade_system_query_session(self):
        """Tests get_grade_system_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session()

    def test_get_grade_system_query_session_for_gradebook(self):
        """Tests get_grade_system_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_query_session_for_gradebook()

    def test_get_grade_system_admin_session(self):
        """Tests get_grade_system_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session()

    def test_get_grade_system_admin_session_for_gradebook(self):
        """Tests get_grade_system_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_admin_session_for_gradebook()

    def test_get_grade_entry_lookup_session(self):
        """Tests get_grade_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session()

    def test_get_grade_entry_lookup_session_for_gradebook(self):
        """Tests get_grade_entry_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook()

    def test_get_grade_entry_query_session(self):
        """Tests get_grade_entry_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session()

    def test_get_grade_entry_query_session_for_gradebook(self):
        """Tests get_grade_entry_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_query_session_for_gradebook()

    def test_get_grade_entry_admin_session(self):
        """Tests get_grade_entry_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session()

    def test_get_grade_entry_admin_session_for_gradebook(self):
        """Tests get_grade_entry_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook()

    def test_get_gradebook_column_lookup_session(self):
        """Tests get_gradebook_column_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session()

    def test_get_gradebook_column_lookup_session_for_gradebook(self):
        """Tests get_gradebook_column_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook()

    def test_get_gradebook_column_query_session(self):
        """Tests get_gradebook_column_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session()

    def test_get_gradebook_column_query_session_for_gradebook(self):
        """Tests get_gradebook_column_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook()

    def test_get_gradebook_column_admin_session(self):
        """Tests get_gradebook_column_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session()

    def test_get_gradebook_column_admin_session_for_gradebook(self):
        """Tests get_gradebook_column_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook()

    def test_get_gradebook_lookup_session(self):
        """Tests get_gradebook_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_lookup():
            self.svc_mgr.get_gradebook_lookup_session()

    def test_get_gradebook_admin_session(self):
        """Tests get_gradebook_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_admin():
            self.svc_mgr.get_gradebook_admin_session()

    def test_get_grading_batch_manager(self):
        """Tests get_grading_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_grading_batch():
            self.svc_mgr.get_grading_batch_manager()

    def test_get_grading_calculation_manager(self):
        """Tests get_grading_calculation_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_grading_calculation():
            self.svc_mgr.get_grading_calculation_manager()

    def test_get_grading_transform_manager(self):
        """Tests get_grading_transform_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_grading_transform():
            self.svc_mgr.get_grading_transform_manager()


class TestGradingProxyManager(unittest.TestCase):
    """Tests for GradingProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for grading proxy manager tests'
        catalog = cls.svc_mgr.create_gradebook(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('GRADING', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_gradebook(cls.catalog_id)

    def test_get_grade_system_lookup_session(self):
        """Tests get_grade_system_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_lookup_session()

    def test_get_grade_system_lookup_session_for_gradebook(self):
        """Tests get_grade_system_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook()

    def test_get_grade_system_query_session(self):
        """Tests get_grade_system_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_query_session()

    def test_get_grade_system_query_session_for_gradebook(self):
        """Tests get_grade_system_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_query_session_for_gradebook()

    def test_get_grade_system_admin_session(self):
        """Tests get_grade_system_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_admin_session()

    def test_get_grade_system_admin_session_for_gradebook(self):
        """Tests get_grade_system_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_system_admin_session_for_gradebook()

    def test_get_grade_entry_lookup_session(self):
        """Tests get_grade_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_lookup_session()

    def test_get_grade_entry_lookup_session_for_gradebook(self):
        """Tests get_grade_entry_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook()

    def test_get_grade_entry_query_session(self):
        """Tests get_grade_entry_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_query_session()

    def test_get_grade_entry_query_session_for_gradebook(self):
        """Tests get_grade_entry_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_query_session_for_gradebook()

    def test_get_grade_entry_admin_session(self):
        """Tests get_grade_entry_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_admin_session()

    def test_get_grade_entry_admin_session_for_gradebook(self):
        """Tests get_grade_entry_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook()

    def test_get_gradebook_column_lookup_session(self):
        """Tests get_gradebook_column_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_lookup_session()

    def test_get_gradebook_column_lookup_session_for_gradebook(self):
        """Tests get_gradebook_column_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook()

    def test_get_gradebook_column_query_session(self):
        """Tests get_gradebook_column_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_query_session()

    def test_get_gradebook_column_query_session_for_gradebook(self):
        """Tests get_gradebook_column_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook()

    def test_get_gradebook_column_admin_session(self):
        """Tests get_gradebook_column_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_admin_session()

    def test_get_gradebook_column_admin_session_for_gradebook(self):
        """Tests get_gradebook_column_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook()

    def test_get_gradebook_lookup_session(self):
        """Tests get_gradebook_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_lookup():
            self.svc_mgr.get_gradebook_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_lookup_session()

    def test_get_gradebook_admin_session(self):
        """Tests get_gradebook_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_admin():
            self.svc_mgr.get_gradebook_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_gradebook_admin_session()

    def test_get_grading_batch_proxy_manager(self):
        """Tests get_grading_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_grading_batch():
            self.svc_mgr.get_grading_batch_proxy_manager()

    def test_get_grading_calculation_proxy_manager(self):
        """Tests get_grading_calculation_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_grading_calculation():
            self.svc_mgr.get_grading_calculation_proxy_manager()

    def test_get_grading_transform_proxy_manager(self):
        """Tests get_grading_transform_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_grading_transform():
            self.svc_mgr.get_grading_transform_proxy_manager()
