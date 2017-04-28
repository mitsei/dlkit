"""Unit tests of authorization managers."""


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


class TestAuthorizationProfile(unittest.TestCase):
    """Tests for AuthorizationProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_authorization(self):
        """Tests supports_authorization"""
        self.assertTrue(isinstance(self.mgr.supports_authorization(), bool))

    def test_supports_authorization_lookup(self):
        """Tests supports_authorization_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_authorization_lookup(), bool))

    def test_supports_authorization_query(self):
        """Tests supports_authorization_query"""
        self.assertTrue(isinstance(self.mgr.supports_authorization_query(), bool))

    def test_supports_authorization_admin(self):
        """Tests supports_authorization_admin"""
        self.assertTrue(isinstance(self.mgr.supports_authorization_admin(), bool))

    def test_supports_vault_lookup(self):
        """Tests supports_vault_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_vault_lookup(), bool))

    def test_supports_vault_query(self):
        """Tests supports_vault_query"""
        self.assertTrue(isinstance(self.mgr.supports_vault_query(), bool))

    def test_supports_vault_admin(self):
        """Tests supports_vault_admin"""
        self.assertTrue(isinstance(self.mgr.supports_vault_admin(), bool))

    def test_get_authorization_record_types(self):
        """Tests get_authorization_record_types"""
        self.assertTrue(isinstance(self.mgr.get_authorization_record_types(), abc_type_list))

    def test_get_authorization_search_record_types(self):
        """Tests get_authorization_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_authorization_search_record_types(), abc_type_list))

    def test_get_function_record_types(self):
        """Tests get_function_record_types"""
        self.assertTrue(isinstance(self.mgr.get_function_record_types(), abc_type_list))

    def test_get_function_search_record_types(self):
        """Tests get_function_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_function_search_record_types(), abc_type_list))

    def test_get_qualifier_record_types(self):
        """Tests get_qualifier_record_types"""
        self.assertTrue(isinstance(self.mgr.get_qualifier_record_types(), abc_type_list))

    def test_get_qualifier_search_record_types(self):
        """Tests get_qualifier_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_qualifier_search_record_types(), abc_type_list))

    def test_get_vault_record_types(self):
        """Tests get_vault_record_types"""
        self.assertTrue(isinstance(self.mgr.get_vault_record_types(), abc_type_list))

    def test_get_vault_search_record_types(self):
        """Tests get_vault_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_vault_search_record_types(), abc_type_list))

    def test_get_authorization_condition_record_types(self):
        """Tests get_authorization_condition_record_types"""
        self.assertTrue(isinstance(self.mgr.get_authorization_condition_record_types(), abc_type_list))


class TestAuthorizationManager(unittest.TestCase):
    """Tests for AuthorizationManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for authorization manager tests'
        catalog = cls.svc_mgr.create_vault(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('AUTHORIZATION', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_vault(cls.catalog_id)

    def test_get_authorization_session(self):
        """Tests get_authorization_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization():
            self.svc_mgr.get_authorization_session()

    def test_get_authorization_session_for_vault(self):
        """Tests get_authorization_session_for_vault"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_authorization():
            self.svc_mgr.get_authorization_session_for_vault(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_session_for_vault()

    def test_get_authorization_lookup_session(self):
        """Tests get_authorization_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_authorization_lookup():
            self.svc_mgr.get_authorization_lookup_session()

    def test_get_authorization_lookup_session_for_vault(self):
        """Tests get_authorization_lookup_session_for_vault"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_authorization_lookup():
            self.svc_mgr.get_authorization_lookup_session_for_vault(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_lookup_session_for_vault()

    def test_get_authorization_query_session(self):
        """Tests get_authorization_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_authorization_query():
            self.svc_mgr.get_authorization_query_session()

    def test_get_authorization_query_session_for_vault(self):
        """Tests get_authorization_query_session_for_vault"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_authorization_query():
            self.svc_mgr.get_authorization_query_session_for_vault(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_query_session_for_vault()

    def test_get_authorization_admin_session(self):
        """Tests get_authorization_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_admin():
            self.svc_mgr.get_authorization_admin_session()

    def test_get_authorization_admin_session_for_vault(self):
        """Tests get_authorization_admin_session_for_vault"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_authorization_admin():
            self.svc_mgr.get_authorization_admin_session_for_vault(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_admin_session_for_vault()

    def test_get_vault_lookup_session(self):
        """Tests get_vault_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_lookup():
            self.svc_mgr.get_vault_lookup_session()

    def test_get_vault_query_session(self):
        """Tests get_vault_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_query():
            self.svc_mgr.get_vault_query_session()

    def test_get_vault_admin_session(self):
        """Tests get_vault_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_admin():
            self.svc_mgr.get_vault_admin_session()

    def test_get_authorization_batch_manager(self):
        """Tests get_authorization_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_authorization_batch():
            self.svc_mgr.get_authorization_batch_manager()

    def test_get_authorization_rules_manager(self):
        """Tests get_authorization_rules_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_authorization_rules():
            self.svc_mgr.get_authorization_rules_manager()


class TestAuthorizationProxyManager(unittest.TestCase):
    """Tests for AuthorizationProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for authorization proxy manager tests'
        catalog = cls.svc_mgr.create_vault(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('AUTHORIZATION', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_vault(cls.catalog_id)

    def test_get_authorization_session(self):
        """Tests get_authorization_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization():
            self.svc_mgr.get_authorization_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_session()

    def test_get_authorization_session_for_vault(self):
        """Tests get_authorization_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_authorization():
            self.svc_mgr.get_authorization_session_for_vault(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_session_for_vault()

    def test_get_authorization_lookup_session(self):
        """Tests get_authorization_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_authorization_lookup():
            self.svc_mgr.get_authorization_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_lookup_session()

    def test_get_authorization_lookup_session_for_vault(self):
        """Tests get_authorization_lookup_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_authorization_lookup():
            self.svc_mgr.get_authorization_lookup_session_for_vault(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_lookup_session_for_vault()

    def test_get_authorization_query_session(self):
        """Tests get_authorization_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_authorization_query():
            self.svc_mgr.get_authorization_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_query_session()

    def test_get_authorization_query_session_for_vault(self):
        """Tests get_authorization_query_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_authorization_query():
            self.svc_mgr.get_authorization_query_session_for_vault(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_query_session_for_vault()

    def test_get_authorization_admin_session(self):
        """Tests get_authorization_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_admin():
            self.svc_mgr.get_authorization_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_admin_session()

    def test_get_authorization_admin_session_for_vault(self):
        """Tests get_authorization_admin_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_authorization_admin():
            self.svc_mgr.get_authorization_admin_session_for_vault(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_authorization_admin_session_for_vault()

    def test_get_vault_lookup_session(self):
        """Tests get_vault_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_lookup():
            self.svc_mgr.get_vault_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_vault_lookup_session()

    def test_get_vault_query_session(self):
        """Tests get_vault_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_query():
            self.svc_mgr.get_vault_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_vault_query_session()

    def test_get_vault_admin_session(self):
        """Tests get_vault_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_admin():
            self.svc_mgr.get_vault_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_vault_admin_session()

    def test_get_authorization_batch_proxy_manager(self):
        """Tests get_authorization_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_authorization_batch():
            self.svc_mgr.get_authorization_batch_proxy_manager()

    def test_get_authorization_rules_proxy_manager(self):
        """Tests get_authorization_rules_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_authorization_rules():
            self.svc_mgr.get_authorization_rules_proxy_manager()
