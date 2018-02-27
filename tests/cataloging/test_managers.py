"""Unit tests of cataloging managers."""


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
def cataloging_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def cataloging_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("cataloging_profile_class_fixture", "cataloging_profile_test_fixture")
class TestCatalogingProfile(object):
    """Tests for CatalogingProfile"""
    def test_supports_catalog_lookup(self):
        """Tests supports_catalog_lookup"""
        assert isinstance(self.mgr.supports_catalog_lookup(), bool)

    def test_supports_catalog_query(self):
        """Tests supports_catalog_query"""
        assert isinstance(self.mgr.supports_catalog_query(), bool)

    def test_supports_catalog_admin(self):
        """Tests supports_catalog_admin"""
        assert isinstance(self.mgr.supports_catalog_admin(), bool)

    def test_supports_catalog_hierarchy(self):
        """Tests supports_catalog_hierarchy"""
        assert isinstance(self.mgr.supports_catalog_hierarchy(), bool)

    def test_supports_catalog_hierarchy_design(self):
        """Tests supports_catalog_hierarchy_design"""
        assert isinstance(self.mgr.supports_catalog_hierarchy_design(), bool)

    def test_get_catalog_record_types(self):
        """Tests get_catalog_record_types"""
        assert isinstance(self.mgr.get_catalog_record_types(), abc_type_list)

    def test_get_catalog_search_record_types(self):
        """Tests get_catalog_search_record_types"""
        assert isinstance(self.mgr.get_catalog_search_record_types(), abc_type_list)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def cataloging_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog'
        create_form.description = 'Test Catalog for cataloging manager tests'
        catalog = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_catalog(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def cataloging_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("cataloging_manager_class_fixture", "cataloging_manager_test_fixture")
class TestCatalogingManager(object):
    """Tests for CatalogingManager"""
    def test_get_catalog_lookup_session(self):
        """Tests get_catalog_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_lookup():
            self.svc_mgr.get_catalog_lookup_session()

    def test_get_catalog_query_session(self):
        """Tests get_catalog_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_query():
            self.svc_mgr.get_catalog_query_session()

    def test_get_catalog_admin_session(self):
        """Tests get_catalog_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_admin():
            self.svc_mgr.get_catalog_admin_session()

    def test_get_catalog_hierarchy_session(self):
        """Tests get_catalog_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_hierarchy():
            self.svc_mgr.get_catalog_hierarchy_session()

    def test_get_catalog_hierarchy_design_session(self):
        """Tests get_catalog_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_hierarchy_design():
            self.svc_mgr.get_catalog_hierarchy_design_session()

    def test_get_cataloging_rules_manager(self):
        """Tests get_cataloging_rules_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_cataloging_rules():
            self.svc_mgr.get_cataloging_rules_manager()


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def cataloging_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog'
        create_form.description = 'Test Catalog for cataloging proxy manager tests'
        catalog = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_catalog(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def cataloging_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("cataloging_proxy_manager_class_fixture", "cataloging_proxy_manager_test_fixture")
class TestCatalogingProxyManager(object):
    """Tests for CatalogingProxyManager"""
    def test_get_catalog_lookup_session(self):
        """Tests get_catalog_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_lookup():
            self.svc_mgr.get_catalog_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_catalog_lookup_session()

    def test_get_catalog_query_session(self):
        """Tests get_catalog_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_query():
            self.svc_mgr.get_catalog_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_catalog_query_session()

    def test_get_catalog_admin_session(self):
        """Tests get_catalog_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_admin():
            self.svc_mgr.get_catalog_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_catalog_admin_session()

    def test_get_catalog_hierarchy_session(self):
        """Tests get_catalog_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_hierarchy():
            self.svc_mgr.get_catalog_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_catalog_hierarchy_session()

    def test_get_catalog_hierarchy_design_session(self):
        """Tests get_catalog_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_catalog_hierarchy_design():
            self.svc_mgr.get_catalog_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_catalog_hierarchy_design_session()

    def test_get_cataloging_rules_proxy_manager(self):
        """Tests get_cataloging_rules_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_cataloging_rules():
            self.svc_mgr.get_cataloging_rules_proxy_manager()
