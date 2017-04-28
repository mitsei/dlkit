"""Unit tests of repository managers."""


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


class TestRepositoryProfile(unittest.TestCase):
    """Tests for RepositoryProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_asset_lookup(self):
        """Tests supports_asset_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_asset_lookup(), bool))

    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        self.assertTrue(isinstance(self.mgr.supports_asset_query(), bool))

    def test_supports_asset_search(self):
        """Tests supports_asset_search"""
        self.assertTrue(isinstance(self.mgr.supports_asset_search(), bool))

    def test_supports_asset_admin(self):
        """Tests supports_asset_admin"""
        self.assertTrue(isinstance(self.mgr.supports_asset_admin(), bool))

    def test_supports_asset_notification(self):
        """Tests supports_asset_notification"""
        self.assertTrue(isinstance(self.mgr.supports_asset_notification(), bool))

    def test_supports_asset_repository(self):
        """Tests supports_asset_repository"""
        self.assertTrue(isinstance(self.mgr.supports_asset_repository(), bool))

    def test_supports_asset_repository_assignment(self):
        """Tests supports_asset_repository_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_asset_repository_assignment(), bool))

    def test_supports_asset_composition(self):
        """Tests supports_asset_composition"""
        self.assertTrue(isinstance(self.mgr.supports_asset_composition(), bool))

    def test_supports_asset_composition_design(self):
        """Tests supports_asset_composition_design"""
        self.assertTrue(isinstance(self.mgr.supports_asset_composition_design(), bool))

    def test_supports_composition_lookup(self):
        """Tests supports_composition_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_composition_lookup(), bool))

    def test_supports_composition_query(self):
        """Tests supports_composition_query"""
        self.assertTrue(isinstance(self.mgr.supports_composition_query(), bool))

    def test_supports_composition_search(self):
        """Tests supports_composition_search"""
        self.assertTrue(isinstance(self.mgr.supports_composition_search(), bool))

    def test_supports_composition_admin(self):
        """Tests supports_composition_admin"""
        self.assertTrue(isinstance(self.mgr.supports_composition_admin(), bool))

    def test_supports_composition_repository(self):
        """Tests supports_composition_repository"""
        self.assertTrue(isinstance(self.mgr.supports_composition_repository(), bool))

    def test_supports_composition_repository_assignment(self):
        """Tests supports_composition_repository_assignment"""
        self.assertTrue(isinstance(self.mgr.supports_composition_repository_assignment(), bool))

    def test_supports_repository_lookup(self):
        """Tests supports_repository_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_repository_lookup(), bool))

    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        self.assertTrue(isinstance(self.mgr.supports_repository_query(), bool))

    def test_supports_repository_admin(self):
        """Tests supports_repository_admin"""
        self.assertTrue(isinstance(self.mgr.supports_repository_admin(), bool))

    def test_supports_repository_hierarchy(self):
        """Tests supports_repository_hierarchy"""
        self.assertTrue(isinstance(self.mgr.supports_repository_hierarchy(), bool))

    def test_supports_repository_hierarchy_design(self):
        """Tests supports_repository_hierarchy_design"""
        self.assertTrue(isinstance(self.mgr.supports_repository_hierarchy_design(), bool))

    def test_get_asset_record_types(self):
        """Tests get_asset_record_types"""
        self.assertTrue(isinstance(self.mgr.get_asset_record_types(), abc_type_list))

    def test_get_asset_search_record_types(self):
        """Tests get_asset_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_asset_search_record_types(), abc_type_list))

    def test_get_asset_content_record_types(self):
        """Tests get_asset_content_record_types"""
        self.assertTrue(isinstance(self.mgr.get_asset_content_record_types(), abc_type_list))

    def test_get_composition_record_types(self):
        """Tests get_composition_record_types"""
        self.assertTrue(isinstance(self.mgr.get_composition_record_types(), abc_type_list))

    def test_get_composition_search_record_types(self):
        """Tests get_composition_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_composition_search_record_types(), abc_type_list))

    def test_get_repository_record_types(self):
        """Tests get_repository_record_types"""
        self.assertTrue(isinstance(self.mgr.get_repository_record_types(), abc_type_list))

    def test_get_repository_search_record_types(self):
        """Tests get_repository_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_repository_search_record_types(), abc_type_list))

    def test_get_spatial_unit_record_types(self):
        """Tests get_spatial_unit_record_types"""
        self.assertTrue(isinstance(self.mgr.get_spatial_unit_record_types(), abc_type_list))

    def test_get_coordinate_types(self):
        """Tests get_coordinate_types"""
        self.assertTrue(isinstance(self.mgr.get_coordinate_types(), abc_type_list))


class TestRepositoryManager(unittest.TestCase):
    """Tests for RepositoryManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for repository manager tests'
        catalog = cls.svc_mgr.create_repository(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('REPOSITORY', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog_id)

    def test_get_asset_lookup_session(self):
        """Tests get_asset_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session()

    def test_get_asset_lookup_session_for_repository(self):
        """Tests get_asset_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_lookup_session_for_repository()

    def test_get_asset_query_session(self):
        """Tests get_asset_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session()

    def test_get_asset_query_session_for_repository(self):
        """Tests get_asset_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_query_session_for_repository()

    def test_get_asset_search_session(self):
        """Tests get_asset_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session()

    def test_get_asset_search_session_for_repository(self):
        """Tests get_asset_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_search_session_for_repository()

    def test_get_asset_admin_session(self):
        """Tests get_asset_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session()

    def test_get_asset_admin_session_for_repository(self):
        """Tests get_asset_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_admin_session_for_repository()

    def test_get_asset_notification_session(self):
        """Tests get_asset_notification_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session(self.receiver)

    def test_get_asset_notification_session_for_repository(self):
        """Tests get_asset_notification_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session_for_repository(self.receiver, self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_notification_session_for_repository()

    def test_get_asset_repository_session(self):
        """Tests get_asset_repository_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository():
            self.svc_mgr.get_asset_repository_session()

    def test_get_asset_repository_assignment_session(self):
        """Tests get_asset_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository_assignment():
            self.svc_mgr.get_asset_repository_assignment_session()

    def test_get_asset_composition_session(self):
        """Tests get_asset_composition_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition():
            self.svc_mgr.get_asset_composition_session()

    def test_get_asset_composition_design_session(self):
        """Tests get_asset_composition_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition_design():
            self.svc_mgr.get_asset_composition_design_session()

    def test_get_composition_lookup_session(self):
        """Tests get_composition_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session()

    def test_get_composition_lookup_session_for_repository(self):
        """Tests get_composition_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_lookup_session_for_repository()

    def test_get_composition_query_session(self):
        """Tests get_composition_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session()

    def test_get_composition_query_session_for_repository(self):
        """Tests get_composition_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_query_session_for_repository()

    def test_get_composition_search_session(self):
        """Tests get_composition_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session()

    def test_get_composition_search_session_for_repository(self):
        """Tests get_composition_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_search_session_for_repository()

    def test_get_composition_admin_session(self):
        """Tests get_composition_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session()

    def test_get_composition_admin_session_for_repository(self):
        """Tests get_composition_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_admin_session_for_repository()

    def test_get_composition_repository_session(self):
        """Tests get_composition_repository_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository():
            self.svc_mgr.get_composition_repository_session()

    def test_get_composition_repository_assignment_session(self):
        """Tests get_composition_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository_assignment():
            self.svc_mgr.get_composition_repository_assignment_session()

    def test_get_repository_lookup_session(self):
        """Tests get_repository_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_lookup():
            self.svc_mgr.get_repository_lookup_session()

    def test_get_repository_query_session(self):
        """Tests get_repository_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_query():
            self.svc_mgr.get_repository_query_session()

    def test_get_repository_admin_session(self):
        """Tests get_repository_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_admin():
            self.svc_mgr.get_repository_admin_session()

    def test_get_repository_hierarchy_session(self):
        """Tests get_repository_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy():
            self.svc_mgr.get_repository_hierarchy_session()

    def test_get_repository_hierarchy_design_session(self):
        """Tests get_repository_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy_design():
            self.svc_mgr.get_repository_hierarchy_design_session()

    def test_get_repository_batch_manager(self):
        """Tests get_repository_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_repository_batch():
            self.svc_mgr.get_repository_batch_manager()

    def test_get_repository_rules_manager(self):
        """Tests get_repository_rules_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_repository_rules():
            self.svc_mgr.get_repository_rules_manager()


class TestRepositoryProxyManager(unittest.TestCase):
    """Tests for RepositoryProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for repository proxy manager tests'
        catalog = cls.svc_mgr.create_repository(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('REPOSITORY', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog_id)

    def test_get_asset_lookup_session(self):
        """Tests get_asset_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_lookup_session()

    def test_get_asset_lookup_session_for_repository(self):
        """Tests get_asset_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_lookup_session_for_repository()

    def test_get_asset_query_session(self):
        """Tests get_asset_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_query_session()

    def test_get_asset_query_session_for_repository(self):
        """Tests get_asset_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_query_session_for_repository()

    def test_get_asset_search_session(self):
        """Tests get_asset_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_search_session()

    def test_get_asset_search_session_for_repository(self):
        """Tests get_asset_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_search_session_for_repository()

    def test_get_asset_admin_session(self):
        """Tests get_asset_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_admin_session()

    def test_get_asset_admin_session_for_repository(self):
        """Tests get_asset_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_admin_session_for_repository()

    def test_get_asset_notification_session(self):
        """Tests get_asset_notification_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session(self.receiver, proxy=PROXY)

    def test_get_asset_notification_session_for_repository(self):
        """Tests get_asset_notification_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session_for_repository(self.receiver, self.catalog_id, proxy=PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_notification_session_for_repository()

    def test_get_asset_repository_session(self):
        """Tests get_asset_repository_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository():
            self.svc_mgr.get_asset_repository_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_repository_session()

    def test_get_asset_repository_assignment_session(self):
        """Tests get_asset_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository_assignment():
            self.svc_mgr.get_asset_repository_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_repository_assignment_session()

    def test_get_asset_composition_session(self):
        """Tests get_asset_composition_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition():
            self.svc_mgr.get_asset_composition_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_composition_session()

    def test_get_asset_composition_design_session(self):
        """Tests get_asset_composition_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition_design():
            self.svc_mgr.get_asset_composition_design_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_asset_composition_design_session()

    def test_get_composition_lookup_session(self):
        """Tests get_composition_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_lookup_session()

    def test_get_composition_lookup_session_for_repository(self):
        """Tests get_composition_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_lookup_session_for_repository()

    def test_get_composition_query_session(self):
        """Tests get_composition_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_query_session()

    def test_get_composition_query_session_for_repository(self):
        """Tests get_composition_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_query_session_for_repository()

    def test_get_composition_search_session(self):
        """Tests get_composition_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_search_session()

    def test_get_composition_search_session_for_repository(self):
        """Tests get_composition_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_search_session_for_repository()

    def test_get_composition_admin_session(self):
        """Tests get_composition_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_admin_session()

    def test_get_composition_admin_session_for_repository(self):
        """Tests get_composition_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_admin_session_for_repository()

    def test_get_composition_repository_session(self):
        """Tests get_composition_repository_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository():
            self.svc_mgr.get_composition_repository_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_repository_session()

    def test_get_composition_repository_assignment_session(self):
        """Tests get_composition_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository_assignment():
            self.svc_mgr.get_composition_repository_assignment_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_composition_repository_assignment_session()

    def test_get_repository_lookup_session(self):
        """Tests get_repository_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_lookup():
            self.svc_mgr.get_repository_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_repository_lookup_session()

    def test_get_repository_query_session(self):
        """Tests get_repository_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_query():
            self.svc_mgr.get_repository_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_repository_query_session()

    def test_get_repository_admin_session(self):
        """Tests get_repository_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_admin():
            self.svc_mgr.get_repository_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_repository_admin_session()

    def test_get_repository_hierarchy_session(self):
        """Tests get_repository_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy():
            self.svc_mgr.get_repository_hierarchy_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_repository_hierarchy_session()

    def test_get_repository_hierarchy_design_session(self):
        """Tests get_repository_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy_design():
            self.svc_mgr.get_repository_hierarchy_design_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_repository_hierarchy_design_session()

    def test_get_repository_batch_proxy_manager(self):
        """Tests get_repository_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_repository_batch():
            self.svc_mgr.get_repository_batch_proxy_manager()

    def test_get_repository_rules_proxy_manager(self):
        """Tests get_repository_rules_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_repository_rules():
            self.svc_mgr.get_repository_rules_proxy_manager()
