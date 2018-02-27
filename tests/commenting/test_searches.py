"""Unit tests of commenting searches."""


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
def comment_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_book_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_book(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_comment_search()


@pytest.mark.usefixtures("comment_search_class_fixture", "comment_search_test_fixture")
class TestCommentSearch(object):
    """Tests for CommentSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_comments(self):
        """Tests search_among_comments"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_comment_results(self):
        """Tests order_comment_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_comment_search_record(self):
        """Tests get_comment_search_record"""
        pass


@pytest.mark.usefixtures("comment_search_results_class_fixture", "comment_search_results_test_fixture")
class TestCommentSearchResults(object):
    """Tests for CommentSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_comments(self):
        """Tests get_comments"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_comment_query_inspector(self):
        """Tests get_comment_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_comment_search_results_record(self):
        """Tests get_comment_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_book_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_book(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_book_search()


@pytest.mark.usefixtures("book_search_class_fixture", "book_search_test_fixture")
class TestBookSearch(object):
    """Tests for BookSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_books(self):
        """Tests search_among_books"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_book_results(self):
        """Tests order_book_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_book_search_record(self):
        """Tests get_book_search_record"""
        pass


@pytest.mark.usefixtures("book_search_results_class_fixture", "book_search_results_test_fixture")
class TestBookSearchResults(object):
    """Tests for BookSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_books(self):
        """Tests get_books"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_book_query_inspector(self):
        """Tests get_book_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_book_search_results_record(self):
        """Tests get_book_search_results_record"""
        pass
