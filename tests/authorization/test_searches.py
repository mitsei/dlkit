"""Unit tests of authorization searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
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
def authorization_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_vault_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_authorization_search()


@pytest.mark.usefixtures("authorization_search_class_fixture", "authorization_search_test_fixture")
class TestAuthorizationSearch(object):
    """Tests for AuthorizationSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_authorizations(self):
        """Tests search_among_authorizations"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_authorization_results(self):
        """Tests order_authorization_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_authorization_search_record(self):
        """Tests get_authorization_search_record"""
        pass


@pytest.mark.usefixtures("authorization_search_results_class_fixture", "authorization_search_results_test_fixture")
class TestAuthorizationSearchResults(object):
    """Tests for AuthorizationSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_authorizations(self):
        """Tests get_authorizations"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_authorization_query_inspector(self):
        """Tests get_authorization_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_authorization_search_results_record(self):
        """Tests get_authorization_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_vault_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_vault_search()


@pytest.mark.usefixtures("vault_search_class_fixture", "vault_search_test_fixture")
class TestVaultSearch(object):
    """Tests for VaultSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_vaults(self):
        """Tests search_among_vaults"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_vault_results(self):
        """Tests order_vault_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_vault_search_record(self):
        """Tests get_vault_search_record"""
        pass


@pytest.mark.usefixtures("vault_search_results_class_fixture", "vault_search_results_test_fixture")
class TestVaultSearchResults(object):
    """Tests for VaultSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_vaults(self):
        """Tests get_vaults"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_vault_query_inspector(self):
        """Tests get_vault_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_vault_search_results_record(self):
        """Tests get_vault_search_results_record"""
        pass
