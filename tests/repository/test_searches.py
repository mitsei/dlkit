"""Unit tests of repository searches."""


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
def asset_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_repository_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_asset_search()


@pytest.mark.usefixtures("asset_search_class_fixture", "asset_search_test_fixture")
class TestAssetSearch(object):
    """Tests for AssetSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assets(self):
        """Tests search_among_assets"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_asset_results(self):
        """Tests order_asset_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_asset_search_record(self):
        """Tests get_asset_search_record"""
        pass


@pytest.mark.usefixtures("asset_search_results_class_fixture", "asset_search_results_test_fixture")
class TestAssetSearchResults(object):
    """Tests for AssetSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assets(self):
        """Tests get_assets"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_asset_query_inspector(self):
        """Tests get_asset_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_asset_search_results_record(self):
        """Tests get_asset_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_repository_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_composition_search()


@pytest.mark.usefixtures("composition_search_class_fixture", "composition_search_test_fixture")
class TestCompositionSearch(object):
    """Tests for CompositionSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_compositions(self):
        """Tests search_among_compositions"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_composition_results(self):
        """Tests order_composition_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_composition_search_record(self):
        """Tests get_composition_search_record"""
        pass


@pytest.mark.usefixtures("composition_search_results_class_fixture", "composition_search_results_test_fixture")
class TestCompositionSearchResults(object):
    """Tests for CompositionSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_compositions(self):
        """Tests get_compositions"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_composition_query_inspector(self):
        """Tests get_composition_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_composition_search_results_record(self):
        """Tests get_composition_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_repository_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_repository_search()


@pytest.mark.usefixtures("repository_search_class_fixture", "repository_search_test_fixture")
class TestRepositorySearch(object):
    """Tests for RepositorySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_repositories(self):
        """Tests search_among_repositories"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_repository_results(self):
        """Tests order_repository_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_repository_search_record(self):
        """Tests get_repository_search_record"""
        pass


@pytest.mark.usefixtures("repository_search_results_class_fixture", "repository_search_results_test_fixture")
class TestRepositorySearchResults(object):
    """Tests for RepositorySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_repositories(self):
        """Tests get_repositories"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_repository_query_inspector(self):
        """Tests get_repository_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_repository_search_results_record(self):
        """Tests get_repository_search_results_record"""
        pass
