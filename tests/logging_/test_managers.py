"""Unit tests of logging managers."""


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


class TestLoggingProfile(unittest.TestCase):
    """Tests for LoggingProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_logging(self):
        """Tests supports_logging"""
        self.assertTrue(isinstance(self.mgr.supports_logging(), bool))

    def test_supports_log_entry_lookup(self):
        """Tests supports_log_entry_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_log_entry_lookup(), bool))

    def test_supports_log_entry_query(self):
        """Tests supports_log_entry_query"""
        self.assertTrue(isinstance(self.mgr.supports_log_entry_query(), bool))

    def test_supports_log_lookup(self):
        """Tests supports_log_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_log_lookup(), bool))

    def test_supports_log_admin(self):
        """Tests supports_log_admin"""
        self.assertTrue(isinstance(self.mgr.supports_log_admin(), bool))

    def test_get_log_entry_record_types(self):
        """Tests get_log_entry_record_types"""
        self.assertTrue(isinstance(self.mgr.get_log_entry_record_types(), abc_type_list))

    def test_get_log_entry_search_record_types(self):
        """Tests get_log_entry_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_log_entry_search_record_types(), abc_type_list))

    def test_get_log_record_types(self):
        """Tests get_log_record_types"""
        self.assertTrue(isinstance(self.mgr.get_log_record_types(), abc_type_list))

    def test_get_log_search_record_types(self):
        """Tests get_log_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_log_search_record_types(), abc_type_list))

    def test_get_priority_types(self):
        """Tests get_priority_types"""
        self.assertTrue(isinstance(self.mgr.get_priority_types(), abc_type_list))

    def test_get_content_types(self):
        """Tests get_content_types"""
        self.assertTrue(isinstance(self.mgr.get_content_types(), abc_type_list))

    def test_supports_log_entry_admin(self):
        """Tests supports_log_entry_admin"""
        self.assertTrue(isinstance(self.mgr.supports_log_entry_admin(), bool))


class TestLoggingManager(unittest.TestCase):
    """Tests for LoggingManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for logging manager tests'
        catalog = cls.svc_mgr.create_log(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('LOGGING', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_log(cls.catalog_id)

    def test_get_logging_session(self):
        """Tests get_logging_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session()

    def test_get_logging_session_for_log(self):
        """Tests get_logging_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session_for_log(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_logging_session_for_log()

    def test_get_log_entry_lookup_session(self):
        """Tests get_log_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session()

    def test_get_log_entry_lookup_session_for_log(self):
        """Tests get_log_entry_lookup_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session_for_log(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_lookup_session_for_log()

    def test_get_log_entry_query_session(self):
        """Tests get_log_entry_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session()

    def test_get_log_entry_query_session_for_log(self):
        """Tests get_log_entry_query_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session_for_log(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_query_session_for_log()

    def test_get_log_entry_admin_session(self):
        """Tests get_log_entry_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session()

    def test_get_log_entry_admin_session_for_log(self):
        """Tests get_log_entry_admin_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session_for_log(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_admin_session_for_log()

    def test_get_log_lookup_session(self):
        """Tests get_log_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_lookup():
            self.svc_mgr.get_log_lookup_session()

    def test_get_log_admin_session(self):
        """Tests get_log_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_admin():
            self.svc_mgr.get_log_admin_session()

    def test_get_logging_batch_manager(self):
        """Tests get_logging_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_logging_batch():
            self.svc_mgr.get_logging_batch_manager()


class TestLoggingProxyManager(unittest.TestCase):
    """Tests for LoggingProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for logging proxy manager tests'
        catalog = cls.svc_mgr.create_log(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('LOGGING', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_log(cls.catalog_id)

    def test_get_logging_session(self):
        """Tests get_logging_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_logging_session()

    def test_get_logging_session_for_log(self):
        """Tests get_logging_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session_for_log(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_logging_session_for_log()

    def test_get_log_entry_lookup_session(self):
        """Tests get_log_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_lookup_session()

    def test_get_log_entry_lookup_session_for_log(self):
        """Tests get_log_entry_lookup_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session_for_log(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_lookup_session_for_log()

    def test_get_log_entry_query_session(self):
        """Tests get_log_entry_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_query_session()

    def test_get_log_entry_query_session_for_log(self):
        """Tests get_log_entry_query_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session_for_log(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_query_session_for_log()

    def test_get_log_entry_admin_session(self):
        """Tests get_log_entry_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_admin_session()

    def test_get_log_entry_admin_session_for_log(self):
        """Tests get_log_entry_admin_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session_for_log(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_entry_admin_session_for_log()

    def test_get_log_lookup_session(self):
        """Tests get_log_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_lookup():
            self.svc_mgr.get_log_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_lookup_session()

    def test_get_log_admin_session(self):
        """Tests get_log_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_admin():
            self.svc_mgr.get_log_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_log_admin_session()

    def test_get_logging_batch_proxy_manager(self):
        """Tests get_logging_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_logging_batch():
            self.svc_mgr.get_logging_batch_proxy_manager()
