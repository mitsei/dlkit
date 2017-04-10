"""Unit tests of repository managers."""

import unittest
from dlkit_runtime import PROXY_SESSION, proxy_example
from dlkit_runtime.managers import Runtime
REQUEST = proxy_example.TestRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

from dlkit.primordium.type.primitives import Type
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT',})

from dlkit.abstract_osid.type.objects import TypeList as abc_type_list
from dlkit.abstract_osid.osid import errors


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

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for repository manager tests'
        catalog = cls.svc_mgr.create_repository(create_form)
        cls.catalog_id = catalog.get_id()
        cls.mgr = Runtime().get_manager('REPOSITORY', 'TEST_MONGO_1', (3, 0, 0))

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog_id)


    def test_get_asset_lookup_session(self):
        """Tests get_asset_lookup_session"""
        if self.mgr.supports_asset_lookup():
            self.mgr.get_asset_lookup_session()

    def test_get_asset_lookup_session_for_repository(self):
        """Tests get_asset_lookup_session_for_repository"""
        if self.mgr.supports_asset_lookup():
            self.mgr.get_asset_lookup_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_asset_lookup_session_for_repository()

    def test_get_asset_query_session(self):
        """Tests get_asset_query_session"""
        if self.mgr.supports_asset_query():
            self.mgr.get_asset_query_session()

    def test_get_asset_query_session_for_repository(self):
        """Tests get_asset_query_session_for_repository"""
        if self.mgr.supports_asset_query():
            self.mgr.get_asset_query_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_asset_query_session_for_repository()

    @unittest.skip('unimplemented test')
    def test_get_asset_search_session(self):
        """Tests get_asset_search_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_search_session_for_repository(self):
        """Tests get_asset_search_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_admin_session(self):
        """Tests get_asset_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_admin_session_for_repository(self):
        """Tests get_asset_admin_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_notification_session(self):
        """Tests get_asset_notification_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_notification_session_for_repository(self):
        """Tests get_asset_notification_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_repository_session(self):
        """Tests get_asset_repository_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_repository_assignment_session(self):
        """Tests get_asset_repository_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_composition_session(self):
        """Tests get_asset_composition_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_composition_design_session(self):
        """Tests get_asset_composition_design_session"""
        pass

    def test_get_composition_lookup_session(self):
        """Tests get_composition_lookup_session"""
        if self.mgr.supports_composition_lookup():
            self.mgr.get_composition_lookup_session()

    def test_get_composition_lookup_session_for_repository(self):
        """Tests get_composition_lookup_session_for_repository"""
        if self.mgr.supports_composition_lookup():
            self.mgr.get_composition_lookup_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_composition_lookup_session_for_repository()

    def test_get_composition_query_session(self):
        """Tests get_composition_query_session"""
        if self.mgr.supports_composition_query():
            self.mgr.get_composition_query_session()

    def test_get_composition_query_session_for_repository(self):
        """Tests get_composition_query_session_for_repository"""
        if self.mgr.supports_composition_query():
            self.mgr.get_composition_query_session_for_repository(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_composition_query_session_for_repository()

    @unittest.skip('unimplemented test')
    def test_get_composition_search_session(self):
        """Tests get_composition_search_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_search_session_for_repository(self):
        """Tests get_composition_search_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_admin_session(self):
        """Tests get_composition_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_admin_session_for_repository(self):
        """Tests get_composition_admin_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_repository_session(self):
        """Tests get_composition_repository_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_repository_assignment_session(self):
        """Tests get_composition_repository_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_lookup_session(self):
        """Tests get_repository_lookup_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query_session(self):
        """Tests get_repository_query_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_admin_session(self):
        """Tests get_repository_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_hierarchy_session(self):
        """Tests get_repository_hierarchy_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_hierarchy_design_session(self):
        """Tests get_repository_hierarchy_design_session"""
        pass

    def test_get_repository_batch_manager(self):
        """Tests get_repository_batch_manager"""
        if self.mgr.supports_repository_batch():
            self.mgr.get_repository_batch_manager()

    def test_get_repository_rules_manager(self):
        """Tests get_repository_rules_manager"""
        if self.mgr.supports_repository_rules():
            self.mgr.get_repository_rules_manager()


class TestRepositoryProxyManager(unittest.TestCase):
    """Tests for RepositoryProxyManager"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for repository proxy manager tests'
        catalog = cls.svc_mgr.create_repository(create_form)
        cls.catalog_id = catalog.get_id()
        cls.mgr = Runtime().get_proxy_manager('REPOSITORY', 'TEST_MONGO_1', (3, 0, 0))

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog_id)


    def test_get_asset_lookup_session(self):
        """Tests get_asset_lookup_session"""
        if self.mgr.supports_asset_lookup():
            self.mgr.get_asset_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_asset_lookup_session()

    def test_get_asset_lookup_session_for_repository(self):
        """Tests get_asset_lookup_session_for_repository"""
        if self.mgr.supports_asset_lookup():
            self.mgr.get_asset_lookup_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_asset_lookup_session_for_repository()

    def test_get_asset_query_session(self):
        """Tests get_asset_query_session"""
        if self.mgr.supports_asset_query():
            self.mgr.get_asset_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_asset_query_session()

    def test_get_asset_query_session_for_repository(self):
        """Tests get_asset_query_session_for_repository"""
        if self.mgr.supports_asset_query():
            self.mgr.get_asset_query_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_asset_query_session_for_repository()

    @unittest.skip('unimplemented test')
    def test_get_asset_search_session(self):
        """Tests get_asset_search_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_search_session_for_repository(self):
        """Tests get_asset_search_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_admin_session(self):
        """Tests get_asset_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_admin_session_for_repository(self):
        """Tests get_asset_admin_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_notification_session(self):
        """Tests get_asset_notification_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_notification_session_for_repository(self):
        """Tests get_asset_notification_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_repository_session(self):
        """Tests get_asset_repository_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_repository_assignment_session(self):
        """Tests get_asset_repository_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_composition_session(self):
        """Tests get_asset_composition_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_composition_design_session(self):
        """Tests get_asset_composition_design_session"""
        pass

    def test_get_composition_lookup_session(self):
        """Tests get_composition_lookup_session"""
        if self.mgr.supports_composition_lookup():
            self.mgr.get_composition_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_composition_lookup_session()

    def test_get_composition_lookup_session_for_repository(self):
        """Tests get_composition_lookup_session_for_repository"""
        if self.mgr.supports_composition_lookup():
            self.mgr.get_composition_lookup_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_composition_lookup_session_for_repository()

    def test_get_composition_query_session(self):
        """Tests get_composition_query_session"""
        if self.mgr.supports_composition_query():
            self.mgr.get_composition_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_composition_query_session()

    def test_get_composition_query_session_for_repository(self):
        """Tests get_composition_query_session_for_repository"""
        if self.mgr.supports_composition_query():
            self.mgr.get_composition_query_session_for_repository(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.mgr.get_composition_query_session_for_repository()

    @unittest.skip('unimplemented test')
    def test_get_composition_search_session(self):
        """Tests get_composition_search_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_search_session_for_repository(self):
        """Tests get_composition_search_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_admin_session(self):
        """Tests get_composition_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_admin_session_for_repository(self):
        """Tests get_composition_admin_session_for_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_repository_session(self):
        """Tests get_composition_repository_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_repository_assignment_session(self):
        """Tests get_composition_repository_assignment_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_lookup_session(self):
        """Tests get_repository_lookup_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query_session(self):
        """Tests get_repository_query_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_admin_session(self):
        """Tests get_repository_admin_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_hierarchy_session(self):
        """Tests get_repository_hierarchy_session"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_hierarchy_design_session(self):
        """Tests get_repository_hierarchy_design_session"""
        pass

    def test_get_repository_batch_proxy_manager(self):
        """Tests get_repository_batch_proxy_manager"""
        if self.mgr.supports_repository_batch():
            self.mgr.get_repository_batch_proxy_manager()

    def test_get_repository_rules_proxy_manager(self):
        """Tests get_repository_rules_proxy_manager"""
        if self.mgr.supports_repository_rules():
            self.mgr.get_repository_rules_proxy_manager()


