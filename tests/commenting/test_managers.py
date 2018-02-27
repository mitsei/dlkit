"""Unit tests of commenting managers."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.type.objects import TypeList as abc_type_list
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def commenting_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def commenting_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("commenting_profile_class_fixture", "commenting_profile_test_fixture")
class TestCommentingProfile(object):
    """Tests for CommentingProfile"""
    def test_supports_comment_lookup(self):
        """Tests supports_comment_lookup"""
        assert isinstance(self.mgr.supports_comment_lookup(), bool)

    def test_supports_comment_query(self):
        """Tests supports_comment_query"""
        assert isinstance(self.mgr.supports_comment_query(), bool)

    def test_supports_comment_admin(self):
        """Tests supports_comment_admin"""
        assert isinstance(self.mgr.supports_comment_admin(), bool)

    def test_supports_comment_book(self):
        """Tests supports_comment_book"""
        assert isinstance(self.mgr.supports_comment_book(), bool)

    def test_supports_comment_book_assignment(self):
        """Tests supports_comment_book_assignment"""
        assert isinstance(self.mgr.supports_comment_book_assignment(), bool)

    def test_supports_book_lookup(self):
        """Tests supports_book_lookup"""
        assert isinstance(self.mgr.supports_book_lookup(), bool)

    def test_supports_book_admin(self):
        """Tests supports_book_admin"""
        assert isinstance(self.mgr.supports_book_admin(), bool)

    def test_supports_book_hierarchy(self):
        """Tests supports_book_hierarchy"""
        assert isinstance(self.mgr.supports_book_hierarchy(), bool)

    def test_supports_book_hierarchy_design(self):
        """Tests supports_book_hierarchy_design"""
        assert isinstance(self.mgr.supports_book_hierarchy_design(), bool)

    def test_get_comment_record_types(self):
        """Tests get_comment_record_types"""
        assert isinstance(self.mgr.get_comment_record_types(), abc_type_list)

    def test_get_comment_search_record_types(self):
        """Tests get_comment_search_record_types"""
        assert isinstance(self.mgr.get_comment_search_record_types(), abc_type_list)

    def test_get_book_record_types(self):
        """Tests get_book_record_types"""
        assert isinstance(self.mgr.get_book_record_types(), abc_type_list)

    def test_get_book_search_record_types(self):
        """Tests get_book_search_record_types"""
        assert isinstance(self.mgr.get_book_search_record_types(), abc_type_list)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def commenting_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for commenting manager tests'
        catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_book(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def commenting_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("commenting_manager_class_fixture", "commenting_manager_test_fixture")
class TestCommentingManager(object):
    """Tests for CommentingManager"""
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
        with pytest.raises(errors.NullArgument):
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
        with pytest.raises(errors.NullArgument):
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
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_admin_session_for_book()

    def test_get_comment_book_session(self):
        """Tests get_comment_book_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_book():
            self.svc_mgr.get_comment_book_session()

    def test_get_comment_book_assignment_session(self):
        """Tests get_comment_book_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_book_assignment():
            self.svc_mgr.get_comment_book_assignment_session()

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


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def commenting_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for commenting proxy manager tests'
        catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_book(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def commenting_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("commenting_proxy_manager_class_fixture", "commenting_proxy_manager_test_fixture")
class TestCommentingProxyManager(object):
    """Tests for CommentingProxyManager"""
    def test_get_comment_lookup_session(self):
        """Tests get_comment_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_comment_lookup():
            self.svc_mgr.get_comment_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_lookup_session()

    def test_get_comment_lookup_session_for_book(self):
        """Tests get_comment_lookup_session_for_book"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_comment_lookup():
            self.svc_mgr.get_comment_lookup_session_for_book(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_lookup_session_for_book()

    def test_get_comment_query_session(self):
        """Tests get_comment_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_comment_query():
            self.svc_mgr.get_comment_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_query_session()

    def test_get_comment_query_session_for_book(self):
        """Tests get_comment_query_session_for_book"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_comment_query():
            self.svc_mgr.get_comment_query_session_for_book(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_query_session_for_book()

    def test_get_comment_admin_session(self):
        """Tests get_comment_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_admin():
            self.svc_mgr.get_comment_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_admin_session()

    def test_get_comment_admin_session_for_book(self):
        """Tests get_comment_admin_session_for_book"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_comment_admin():
            self.svc_mgr.get_comment_admin_session_for_book(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_admin_session_for_book()

    def test_get_comment_book_session(self):
        """Tests get_comment_book_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_book():
            self.svc_mgr.get_comment_book_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_book_session()

    def test_get_comment_book_assignment_session(self):
        """Tests get_comment_book_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_comment_book_assignment():
            self.svc_mgr.get_comment_book_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_comment_book_assignment_session()

    def test_get_book_lookup_session(self):
        """Tests get_book_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_lookup():
            self.svc_mgr.get_book_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_book_lookup_session()

    def test_get_book_admin_session(self):
        """Tests get_book_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_admin():
            self.svc_mgr.get_book_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_book_admin_session()

    def test_get_book_hierarchy_session(self):
        """Tests get_book_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_hierarchy():
            self.svc_mgr.get_book_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_book_hierarchy_session()

    def test_get_book_hierarchy_design_session(self):
        """Tests get_book_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_book_hierarchy_design():
            self.svc_mgr.get_book_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_book_hierarchy_design_session()

    def test_get_commenting_batch_proxy_manager(self):
        """Tests get_commenting_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_commenting_batch():
            self.svc_mgr.get_commenting_batch_proxy_manager()
