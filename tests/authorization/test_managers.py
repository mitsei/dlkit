"""Unit tests of authorization managers."""


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
def authorization_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def authorization_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("authorization_profile_class_fixture", "authorization_profile_test_fixture")
class TestAuthorizationProfile(object):
    """Tests for AuthorizationProfile"""
    def test_supports_authorization(self):
        """Tests supports_authorization"""
        assert isinstance(self.mgr.supports_authorization(), bool)

    def test_supports_authorization_lookup(self):
        """Tests supports_authorization_lookup"""
        assert isinstance(self.mgr.supports_authorization_lookup(), bool)

    def test_supports_authorization_query(self):
        """Tests supports_authorization_query"""
        assert isinstance(self.mgr.supports_authorization_query(), bool)

    def test_supports_authorization_admin(self):
        """Tests supports_authorization_admin"""
        assert isinstance(self.mgr.supports_authorization_admin(), bool)

    def test_supports_authorization_vault(self):
        """Tests supports_authorization_vault"""
        assert isinstance(self.mgr.supports_authorization_vault(), bool)

    def test_supports_authorization_vault_assignment(self):
        """Tests supports_authorization_vault_assignment"""
        assert isinstance(self.mgr.supports_authorization_vault_assignment(), bool)

    def test_supports_vault_lookup(self):
        """Tests supports_vault_lookup"""
        assert isinstance(self.mgr.supports_vault_lookup(), bool)

    def test_supports_vault_query(self):
        """Tests supports_vault_query"""
        assert isinstance(self.mgr.supports_vault_query(), bool)

    def test_supports_vault_admin(self):
        """Tests supports_vault_admin"""
        assert isinstance(self.mgr.supports_vault_admin(), bool)

    def test_supports_vault_hierarchy(self):
        """Tests supports_vault_hierarchy"""
        assert isinstance(self.mgr.supports_vault_hierarchy(), bool)

    def test_supports_vault_hierarchy_design(self):
        """Tests supports_vault_hierarchy_design"""
        assert isinstance(self.mgr.supports_vault_hierarchy_design(), bool)

    def test_get_authorization_record_types(self):
        """Tests get_authorization_record_types"""
        assert isinstance(self.mgr.get_authorization_record_types(), abc_type_list)

    def test_get_authorization_search_record_types(self):
        """Tests get_authorization_search_record_types"""
        assert isinstance(self.mgr.get_authorization_search_record_types(), abc_type_list)

    def test_get_function_record_types(self):
        """Tests get_function_record_types"""
        assert isinstance(self.mgr.get_function_record_types(), abc_type_list)

    def test_get_function_search_record_types(self):
        """Tests get_function_search_record_types"""
        assert isinstance(self.mgr.get_function_search_record_types(), abc_type_list)

    def test_get_qualifier_record_types(self):
        """Tests get_qualifier_record_types"""
        assert isinstance(self.mgr.get_qualifier_record_types(), abc_type_list)

    def test_get_qualifier_search_record_types(self):
        """Tests get_qualifier_search_record_types"""
        assert isinstance(self.mgr.get_qualifier_search_record_types(), abc_type_list)

    def test_get_vault_record_types(self):
        """Tests get_vault_record_types"""
        assert isinstance(self.mgr.get_vault_record_types(), abc_type_list)

    def test_get_vault_search_record_types(self):
        """Tests get_vault_search_record_types"""
        assert isinstance(self.mgr.get_vault_search_record_types(), abc_type_list)

    def test_get_authorization_condition_record_types(self):
        """Tests get_authorization_condition_record_types"""
        assert isinstance(self.mgr.get_authorization_condition_record_types(), abc_type_list)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for authorization manager tests'
        catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_vault(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("authorization_manager_class_fixture", "authorization_manager_test_fixture")
class TestAuthorizationManager(object):
    """Tests for AuthorizationManager"""
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
        with pytest.raises(errors.NullArgument):
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
        with pytest.raises(errors.NullArgument):
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
        with pytest.raises(errors.NullArgument):
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
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_admin_session_for_vault()

    def test_get_authorization_vault_session(self):
        """Tests get_authorization_vault_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_vault():
            self.svc_mgr.get_authorization_vault_session()

    def test_get_authorization_vault_assignment_session(self):
        """Tests get_authorization_vault_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_vault_assignment():
            self.svc_mgr.get_authorization_vault_assignment_session()

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

    def test_get_vault_hierarchy_session(self):
        """Tests get_vault_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_hierarchy():
            self.svc_mgr.get_vault_hierarchy_session()

    def test_get_vault_hierarchy_design_session(self):
        """Tests get_vault_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_hierarchy_design():
            self.svc_mgr.get_vault_hierarchy_design_session()

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


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for authorization proxy manager tests'
        catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_vault(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("authorization_proxy_manager_class_fixture", "authorization_proxy_manager_test_fixture")
class TestAuthorizationProxyManager(object):
    """Tests for AuthorizationProxyManager"""
    def test_get_authorization_session(self):
        """Tests get_authorization_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization():
            self.svc_mgr.get_authorization_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_session()

    def test_get_authorization_session_for_vault(self):
        """Tests get_authorization_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_authorization():
            self.svc_mgr.get_authorization_session_for_vault(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_session_for_vault()

    def test_get_authorization_lookup_session(self):
        """Tests get_authorization_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_authorization_lookup():
            self.svc_mgr.get_authorization_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_lookup_session()

    def test_get_authorization_lookup_session_for_vault(self):
        """Tests get_authorization_lookup_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_authorization_lookup():
            self.svc_mgr.get_authorization_lookup_session_for_vault(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_lookup_session_for_vault()

    def test_get_authorization_query_session(self):
        """Tests get_authorization_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_authorization_query():
            self.svc_mgr.get_authorization_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_query_session()

    def test_get_authorization_query_session_for_vault(self):
        """Tests get_authorization_query_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_authorization_query():
            self.svc_mgr.get_authorization_query_session_for_vault(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_query_session_for_vault()

    def test_get_authorization_admin_session(self):
        """Tests get_authorization_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_admin():
            self.svc_mgr.get_authorization_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_admin_session()

    def test_get_authorization_admin_session_for_vault(self):
        """Tests get_authorization_admin_session_for_vault"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_authorization_admin():
            self.svc_mgr.get_authorization_admin_session_for_vault(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_admin_session_for_vault()

    def test_get_authorization_vault_session(self):
        """Tests get_authorization_vault_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_vault():
            self.svc_mgr.get_authorization_vault_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_vault_session()

    def test_get_authorization_vault_assignment_session(self):
        """Tests get_authorization_vault_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_authorization_vault_assignment():
            self.svc_mgr.get_authorization_vault_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_authorization_vault_assignment_session()

    def test_get_vault_lookup_session(self):
        """Tests get_vault_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_lookup():
            self.svc_mgr.get_vault_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_vault_lookup_session()

    def test_get_vault_query_session(self):
        """Tests get_vault_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_query():
            self.svc_mgr.get_vault_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_vault_query_session()

    def test_get_vault_admin_session(self):
        """Tests get_vault_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_admin():
            self.svc_mgr.get_vault_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_vault_admin_session()

    def test_get_vault_hierarchy_session(self):
        """Tests get_vault_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_hierarchy():
            self.svc_mgr.get_vault_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_vault_hierarchy_session()

    def test_get_vault_hierarchy_design_session(self):
        """Tests get_vault_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_vault_hierarchy_design():
            self.svc_mgr.get_vault_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_vault_hierarchy_design_session()

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
