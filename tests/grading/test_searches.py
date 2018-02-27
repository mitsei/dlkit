"""Unit tests of grading searches."""


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
def grade_system_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_system_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_grade_system_search()


@pytest.mark.usefixtures("grade_system_search_class_fixture", "grade_system_search_test_fixture")
class TestGradeSystemSearch(object):
    """Tests for GradeSystemSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_grade_systems(self):
        """Tests search_among_grade_systems"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_grade_system_results(self):
        """Tests order_grade_system_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_system_search_record(self):
        """Tests get_grade_system_search_record"""
        pass


@pytest.mark.usefixtures("grade_system_search_results_class_fixture", "grade_system_search_results_test_fixture")
class TestGradeSystemSearchResults(object):
    """Tests for GradeSystemSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_grade_systems(self):
        """Tests get_grade_systems"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_system_query_inspector(self):
        """Tests get_grade_system_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_system_search_results_record(self):
        """Tests get_grade_system_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grade_entry_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grade_entry_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_grade_entry_search()


@pytest.mark.usefixtures("grade_entry_search_class_fixture", "grade_entry_search_test_fixture")
class TestGradeEntrySearch(object):
    """Tests for GradeEntrySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_grade_entries(self):
        """Tests search_among_grade_entries"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_grade_entry_results(self):
        """Tests order_grade_entry_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entry_search_record(self):
        """Tests get_grade_entry_search_record"""
        pass


@pytest.mark.usefixtures("grade_entry_search_results_class_fixture", "grade_entry_search_results_test_fixture")
class TestGradeEntrySearchResults(object):
    """Tests for GradeEntrySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entry_query_inspector(self):
        """Tests get_grade_entry_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_grade_entry_search_results_record(self):
        """Tests get_grade_entry_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_column_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_column_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_gradebook_column_search()


@pytest.mark.usefixtures("gradebook_column_search_class_fixture", "gradebook_column_search_test_fixture")
class TestGradebookColumnSearch(object):
    """Tests for GradebookColumnSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_gradebook_columns(self):
        """Tests search_among_gradebook_columns"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_gradebook_column_results(self):
        """Tests order_gradebook_column_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_column_search_record(self):
        """Tests get_gradebook_column_search_record"""
        pass


@pytest.mark.usefixtures("gradebook_column_search_results_class_fixture", "gradebook_column_search_results_test_fixture")
class TestGradebookColumnSearchResults(object):
    """Tests for GradebookColumnSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_columns(self):
        """Tests get_gradebook_columns"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_column_query_inspector(self):
        """Tests get_gradebook_column_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_column_search_results_record(self):
        """Tests get_gradebook_column_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def gradebook_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_gradebook(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_gradebook(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def gradebook_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_gradebook_search()


@pytest.mark.usefixtures("gradebook_search_class_fixture", "gradebook_search_test_fixture")
class TestGradebookSearch(object):
    """Tests for GradebookSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_gradebooks(self):
        """Tests search_among_gradebooks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_gradebook_results(self):
        """Tests order_gradebook_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_search_record(self):
        """Tests get_gradebook_search_record"""
        pass


@pytest.mark.usefixtures("gradebook_search_results_class_fixture", "gradebook_search_results_test_fixture")
class TestGradebookSearchResults(object):
    """Tests for GradebookSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_gradebooks(self):
        """Tests get_gradebooks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_query_inspector(self):
        """Tests get_gradebook_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_gradebook_search_results_record(self):
        """Tests get_gradebook_search_results_record"""
        pass
