"""Unit tests of resource searches."""


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
def resource_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_bin_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_resource_search()


@pytest.mark.usefixtures("resource_search_class_fixture", "resource_search_test_fixture")
class TestResourceSearch(object):
    """Tests for ResourceSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_resources(self):
        """Tests search_among_resources"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_resource_results(self):
        """Tests order_resource_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_resource_search_record(self):
        """Tests get_resource_search_record"""
        pass


@pytest.mark.usefixtures("resource_search_results_class_fixture", "resource_search_results_test_fixture")
class TestResourceSearchResults(object):
    """Tests for ResourceSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_resources(self):
        """Tests get_resources"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_resource_query_inspector(self):
        """Tests get_resource_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_resource_search_results_record(self):
        """Tests get_resource_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_bin_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_bin_search()


@pytest.mark.usefixtures("bin_search_class_fixture", "bin_search_test_fixture")
class TestBinSearch(object):
    """Tests for BinSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_bins(self):
        """Tests search_among_bins"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_bin_results(self):
        """Tests order_bin_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bin_search_record(self):
        """Tests get_bin_search_record"""
        pass


@pytest.mark.usefixtures("bin_search_results_class_fixture", "bin_search_results_test_fixture")
class TestBinSearchResults(object):
    """Tests for BinSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_bins(self):
        """Tests get_bins"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bin_query_inspector(self):
        """Tests get_bin_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bin_search_results_record(self):
        """Tests get_bin_search_results_record"""
        pass
