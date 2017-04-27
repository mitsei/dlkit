"""Unit tests of resource managers."""


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


class TestResourceProfile(unittest.TestCase):
    """Tests for ResourceProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_resource_lookup(self):
        """Tests supports_resource_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_resource_lookup(), bool))

    def test_supports_resource_query(self):
        """Tests supports_resource_query"""
        self.assertTrue(isinstance(self.mgr.supports_resource_query(), bool))

    def test_supports_resource_search(self):
        """Tests supports_resource_search"""
        self.assertTrue(isinstance(self.mgr.supports_resource_search(), bool))

    def test_supports_resource_admin(self):
        """Tests supports_resource_admin"""
        self.assertTrue(isinstance(self.mgr.supports_resource_admin(), bool))

    def test_supports_resource_notification(self):
        """Tests supports_resource_notification"""
        self.assertTrue(isinstance(self.mgr.supports_resource_notification(), bool))

    def test_supports_resource_bin(self):
        """Tests supports_resource_bin"""
        self.assertTrue(isinstance(self.mgr.supports_resource_bin(), bool))

    def test_supports_resource_bin_assignment(self):
        """Tests supports_resource_bin_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_resource_bin_assignment(), bool))

    def test_supports_resource_agent(self):
        """Tests supports_resource_agent"""
        self.assertTrue(isinstance(self.mgr.supports_resource_agent(), bool))

    def test_supports_resource_agent_assignment(self):
        """Tests supports_resource_agent_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_resource_agent_assignment(), bool))

    def test_supports_bin_lookup(self):
        """Tests supports_bin_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_bin_lookup(), bool))

    def test_supports_bin_query(self):
        """Tests supports_bin_query"""
        self.assertTrue(isinstance(self.mgr.supports_bin_query(), bool))

    def test_supports_bin_admin(self):
        """Tests supports_bin_admin"""
        self.assertTrue(isinstance(self.mgr.supports_bin_admin(), bool))

    def test_supports_bin_hierarchy(self):
        """Tests supports_bin_hierarchy"""
        self.assertTrue(isinstance(self.mgr.supports_bin_hierarchy(), bool))

    def test_supports_bin_hierarchy_design(self):
        """Tests supports_bin_hierarchy_design"""
        self.assertTrue(isinstance(self.mgr.supports_bin_hierarchy_design(), bool))

    def test_get_resource_record_types(self):
        """Tests get_resource_record_types"""
        self.assertTrue(isinstance(self.mgr.get_resource_record_types(), abc_type_list))

    def test_get_resource_search_record_types(self):
        """Tests get_resource_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_resource_search_record_types(), abc_type_list))

    def test_get_resource_relationship_record_types(self):
        """Tests get_resource_relationship_record_types"""
        self.assertTrue(isinstance(self.mgr.get_resource_relationship_record_types(), abc_type_list))

    def test_get_resource_relationship_search_record_types(self):
        """Tests get_resource_relationship_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_resource_relationship_search_record_types(), abc_type_list))

    def test_get_bin_record_types(self):
        """Tests get_bin_record_types"""
        self.assertTrue(isinstance(self.mgr.get_bin_record_types(), abc_type_list))

    def test_get_bin_search_record_types(self):
        """Tests get_bin_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_bin_search_record_types(), abc_type_list))


class TestResourceManager(unittest.TestCase):
    """Tests for ResourceManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for resource manager tests'
        catalog = cls.svc_mgr.create_bin(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('RESOURCE', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bin(cls.catalog_id)

    def test_get_resource_lookup_session(self):
        """Tests get_resource_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session()

    def test_get_resource_lookup_session_for_bin(self):
        """Tests get_resource_lookup_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session_for_bin(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_lookup_session_for_bin()

    def test_get_resource_query_session(self):
        """Tests get_resource_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session()

    def test_get_resource_query_session_for_bin(self):
        """Tests get_resource_query_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session_for_bin(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_query_session_for_bin()

    def test_get_resource_search_session(self):
        """Tests get_resource_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session()

    def test_get_resource_search_session_for_bin(self):
        """Tests get_resource_search_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session_for_bin(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_search_session_for_bin()

    def test_get_resource_admin_session(self):
        """Tests get_resource_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session()

    def test_get_resource_admin_session_for_bin(self):
        """Tests get_resource_admin_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session_for_bin(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_admin_session_for_bin()

    def test_get_resource_notification_session(self):
        """Tests get_resource_notification_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session(self.receiver)

    def test_get_resource_notification_session_for_bin(self):
        """Tests get_resource_notification_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session_for_bin(self.receiver, self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_notification_session_for_bin()

    def test_get_resource_bin_session(self):
        """Tests get_resource_bin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin():
            self.svc_mgr.get_resource_bin_session()

    def test_get_resource_bin_assignment_session(self):
        """Tests get_resource_bin_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin_assignment():
            self.svc_mgr.get_resource_bin_assignment_session()

    def test_get_resource_agent_session(self):
        """Tests get_resource_agent_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session()

    def test_get_resource_agent_session_for_bin(self):
        """Tests get_resource_agent_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session_for_bin(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_session_for_bin()

    def test_get_resource_agent_assignment_session(self):
        """Tests get_resource_agent_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session()

    def test_get_resource_agent_assignment_session_for_bin(self):
        """Tests get_resource_agent_assignment_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session_for_bin(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_assignment_session_for_bin()

    def test_get_bin_lookup_session(self):
        """Tests get_bin_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_lookup():
            self.svc_mgr.get_bin_lookup_session()

    def test_get_bin_query_session(self):
        """Tests get_bin_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_query():
            self.svc_mgr.get_bin_query_session()

    def test_get_bin_admin_session(self):
        """Tests get_bin_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_admin():
            self.svc_mgr.get_bin_admin_session()

    def test_get_bin_hierarchy_session(self):
        """Tests get_bin_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy():
            self.svc_mgr.get_bin_hierarchy_session()

    def test_get_bin_hierarchy_design_session(self):
        """Tests get_bin_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy_design():
            self.svc_mgr.get_bin_hierarchy_design_session()

    def test_get_resource_batch_manager(self):
        """Tests get_resource_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_resource_batch():
            self.svc_mgr.get_resource_batch_manager()

    def test_get_resource_demographic_manager(self):
        """Tests get_resource_demographic_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_resource_demographic():
            self.svc_mgr.get_resource_demographic_manager()


class TestResourceProxyManager(unittest.TestCase):
    """Tests for ResourceProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for resource proxy manager tests'
        catalog = cls.svc_mgr.create_bin(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('RESOURCE', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bin(cls.catalog_id)

    def test_get_resource_lookup_session(self):
        """Tests get_resource_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_lookup_session()

    def test_get_resource_lookup_session_for_bin(self):
        """Tests get_resource_lookup_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session_for_bin(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_lookup_session_for_bin()

    def test_get_resource_query_session(self):
        """Tests get_resource_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_query_session()

    def test_get_resource_query_session_for_bin(self):
        """Tests get_resource_query_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session_for_bin(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_query_session_for_bin()

    def test_get_resource_search_session(self):
        """Tests get_resource_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_search_session()

    def test_get_resource_search_session_for_bin(self):
        """Tests get_resource_search_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session_for_bin(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_search_session_for_bin()

    def test_get_resource_admin_session(self):
        """Tests get_resource_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_admin_session()

    def test_get_resource_admin_session_for_bin(self):
        """Tests get_resource_admin_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session_for_bin(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_admin_session_for_bin()

    def test_get_resource_notification_session(self):
        """Tests get_resource_notification_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session(self.receiver, proxy=PROXY)

    def test_get_resource_notification_session_for_bin(self):
        """Tests get_resource_notification_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session_for_bin(self.receiver, self.catalog_id, proxy=PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_notification_session_for_bin()

    def test_get_resource_bin_session(self):
        """Tests get_resource_bin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin():
            self.svc_mgr.get_resource_bin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_bin_session()

    def test_get_resource_bin_assignment_session(self):
        """Tests get_resource_bin_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin_assignment():
            self.svc_mgr.get_resource_bin_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_bin_assignment_session()

    def test_get_group_hierarchy_session(self):
        """Tests get_group_hierarchy_session"""
        if self.svc_mgr.supports_group_hierarchy():
            self.svc_mgr.get_group_hierarchy_session(PROXY)
        with self.assertRaises(errors.Unimplemented):
            self.svc_mgr.get_group_hierarchy_session()

    def test_get_resource_agent_session(self):
        """Tests get_resource_agent_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_session()

    def test_get_resource_agent_session_for_bin(self):
        """Tests get_resource_agent_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session_for_bin(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_session_for_bin()

    def test_get_resource_agent_assignment_session(self):
        """Tests get_resource_agent_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_assignment_session()

    def test_get_resource_agent_assignment_session_for_bin(self):
        """Tests get_resource_agent_assignment_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session_for_bin(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_assignment_session_for_bin()

    def test_get_bin_lookup_session(self):
        """Tests get_bin_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_lookup():
            self.svc_mgr.get_bin_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bin_lookup_session()

    def test_get_bin_query_session(self):
        """Tests get_bin_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_query():
            self.svc_mgr.get_bin_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bin_query_session()

    def test_get_bin_admin_session(self):
        """Tests get_bin_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_admin():
            self.svc_mgr.get_bin_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bin_admin_session()

    def test_get_bin_hierarchy_session(self):
        """Tests get_bin_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy():
            self.svc_mgr.get_bin_hierarchy_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bin_hierarchy_session()

    def test_get_bin_hierarchy_design_session(self):
        """Tests get_bin_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy_design():
            self.svc_mgr.get_bin_hierarchy_design_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_bin_hierarchy_design_session()

    def test_get_resource_batch_proxy_manager(self):
        """Tests get_resource_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_resource_batch():
            self.svc_mgr.get_resource_batch_proxy_manager()

    def test_get_resource_demographic_proxy_manager(self):
        """Tests get_resource_demographic_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_resource_demographic():
            self.svc_mgr.get_resource_demographic_proxy_manager()
