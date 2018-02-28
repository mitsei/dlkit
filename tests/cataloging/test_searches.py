"""Unit tests of cataloging searches."""


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
def catalog_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_catalog(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_catalog(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_catalog_search()


@pytest.mark.usefixtures("catalog_search_class_fixture", "catalog_search_test_fixture")
class TestCatalogSearch(object):
    """Tests for CatalogSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_catalogs(self):
        """Tests search_among_catalogs"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_catalog_results(self):
        """Tests order_catalog_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_catalog_search_record(self):
        """Tests get_catalog_search_record"""
        pass


@pytest.mark.usefixtures("catalog_search_results_class_fixture", "catalog_search_results_test_fixture")
class TestCatalogSearchResults(object):
    """Tests for CatalogSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_catalogs(self):
        """Tests get_catalogs"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_catalog_query_inspector(self):
        """Tests get_catalog_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_catalog_search_results_record(self):
        """Tests get_catalog_search_results_record"""
        pass
