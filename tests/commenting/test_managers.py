"""Unit tests of commenting managers."""


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


class TestCommentingProfile(unittest.TestCase):
    """Tests for CommentingProfile"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')

    def test_supports_comment_lookup(self):
        """Tests supports_comment_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_comment_lookup(), bool))

    def test_supports_comment_query(self):
        """Tests supports_comment_query"""
        self.assertTrue(isinstance(self.mgr.supports_comment_query(), bool))

    def test_supports_comment_admin(self):
        """Tests supports_comment_admin"""
        self.assertTrue(isinstance(self.mgr.supports_comment_admin(), bool))

    def test_supports_book_lookup(self):
        """Tests supports_book_lookup"""
        self.assertTrue(isinstance(self.mgr.supports_book_lookup(), bool))

    def test_supports_book_admin(self):
        """Tests supports_book_admin"""
        self.assertTrue(isinstance(self.mgr.supports_book_admin(), bool))

    def test_supports_book_hierarchy(self):
        """Tests supports_book_hierarchy"""
        self.assertTrue(isinstance(self.mgr.supports_book_hierarchy(), bool))

    def test_supports_book_hierarchy_design(self):
        """Tests supports_book_hierarchy_design"""
        self.assertTrue(isinstance(self.mgr.supports_book_hierarchy_design(), bool))

    def test_get_comment_record_types(self):
        """Tests get_comment_record_types"""
        self.assertTrue(isinstance(self.mgr.get_comment_record_types(), abc_type_list))

    def test_get_comment_search_record_types(self):
        """Tests get_comment_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_comment_search_record_types(), abc_type_list))

    def test_get_book_record_types(self):
        """Tests get_book_record_types"""
        self.assertTrue(isinstance(self.mgr.get_book_record_types(), abc_type_list))

    def test_get_book_search_record_types(self):
        """Tests get_book_search_record_types"""
        self.assertTrue(isinstance(self.mgr.get_book_search_record_types(), abc_type_list))


class TestCommentingManager(unittest.TestCase):
    """Tests for CommentingManager"""

    # Implemented from resource.ResourceManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for commenting manager tests'
        catalog = cls.svc_mgr.create_book(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_manager('COMMENTING', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_book(cls.catalog_id)

    def test_get_comment_lookup_session(self):
        """Tests get_comment_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_comment_lookup():
            self.svc_mgr.get_comment_lookup_session()

    def test_get_comment_lookup_session_for_book(self):
        """Tests get_comment_lookup_session_for_book"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_comment_lookup():
            self.svc_mgr.get_comment_lookup_session_for_book(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_lookup_session_for_book()

    def test_get_comment_query_session(self):
        """Tests get_comment_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_comment_query():
            self.svc_mgr.get_comment_query_session()

    def test_get_comment_query_session_for_book(self):
        """Tests get_comment_query_session_for_book"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_comment_query():
            self.svc_mgr.get_comment_query_session_for_book(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_query_session_for_book()

    def test_get_comment_admin_session(self):
        """Tests get_comment_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_admin():
            self.svc_mgr.get_comment_admin_session()

    def test_get_comment_admin_session_for_book(self):
        """Tests get_comment_admin_session_for_book"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_comment_admin():
            self.svc_mgr.get_comment_admin_session_for_book(self.catalog_id)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_admin_session_for_book()

    def test_get_book_lookup_session(self):
        """Tests get_book_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_lookup():
            self.svc_mgr.get_book_lookup_session()

    def test_get_book_admin_session(self):
        """Tests get_book_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_admin():
            self.svc_mgr.get_book_admin_session()

    def test_get_book_hierarchy_session(self):
        """Tests get_book_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_hierarchy():
            self.svc_mgr.get_book_hierarchy_session()

    def test_get_book_hierarchy_design_session(self):
        """Tests get_book_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_hierarchy_design():
            self.svc_mgr.get_book_hierarchy_design_session()

    def test_get_commenting_batch_manager(self):
        """Tests get_commenting_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_commenting_batch():
            self.svc_mgr.get_commenting_batch_manager()


class TestCommentingProxyManager(unittest.TestCase):
    """Tests for CommentingProxyManager"""

    # Implemented from resource.ResourceProxyManager
    class NotificationReceiver(object):
        pass

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for commenting proxy manager tests'
        catalog = cls.svc_mgr.create_book(create_form)
        cls.catalog_id = catalog.get_id()
        # cls.mgr = Runtime().get_proxy_manager('COMMENTING', 'TEST_JSON_1', (3, 0, 0))
        cls.receiver = cls.NotificationReceiver()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_book(cls.catalog_id)

    def test_get_comment_lookup_session(self):
        """Tests get_comment_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_comment_lookup():
            self.svc_mgr.get_comment_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_lookup_session()

    def test_get_comment_lookup_session_for_book(self):
        """Tests get_comment_lookup_session_for_book"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_comment_lookup():
            self.svc_mgr.get_comment_lookup_session_for_book(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_lookup_session_for_book()

    def test_get_comment_query_session(self):
        """Tests get_comment_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_comment_query():
            self.svc_mgr.get_comment_query_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_query_session()

    def test_get_comment_query_session_for_book(self):
        """Tests get_comment_query_session_for_book"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_comment_query():
            self.svc_mgr.get_comment_query_session_for_book(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_query_session_for_book()

    def test_get_comment_admin_session(self):
        """Tests get_comment_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_admin():
            self.svc_mgr.get_comment_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_admin_session()

    def test_get_comment_admin_session_for_book(self):
        """Tests get_comment_admin_session_for_book"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_comment_admin():
            self.svc_mgr.get_comment_admin_session_for_book(self.catalog_id, PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_comment_admin_session_for_book()

    def test_get_book_lookup_session(self):
        """Tests get_book_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_lookup():
            self.svc_mgr.get_book_lookup_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_book_lookup_session()

    def test_get_book_admin_session(self):
        """Tests get_book_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_admin():
            self.svc_mgr.get_book_admin_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_book_admin_session()

    def test_get_book_hierarchy_session(self):
        """Tests get_book_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_hierarchy():
            self.svc_mgr.get_book_hierarchy_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_book_hierarchy_session()

    def test_get_book_hierarchy_design_session(self):
        """Tests get_book_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_hierarchy_design():
            self.svc_mgr.get_book_hierarchy_design_session(PROXY)
        with self.assertRaises(errors.NullArgument):
            self.svc_mgr.get_book_hierarchy_design_session()

    def test_get_commenting_batch_proxy_manager(self):
        """Tests get_commenting_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_commenting_batch():
            self.svc_mgr.get_commenting_batch_proxy_manager()
