"""Unit tests of learning searches."""


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
def objective_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_objective_search()


@pytest.mark.usefixtures("objective_search_class_fixture", "objective_search_test_fixture")
class TestObjectiveSearch(object):
    """Tests for ObjectiveSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_objectives(self):
        """Tests search_among_objectives"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_objective_results(self):
        """Tests order_objective_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_search_record(self):
        """Tests get_objective_search_record"""
        pass


@pytest.mark.usefixtures("objective_search_results_class_fixture", "objective_search_results_test_fixture")
class TestObjectiveSearchResults(object):
    """Tests for ObjectiveSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_objectives(self):
        """Tests get_objectives"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_query_inspector(self):
        """Tests get_objective_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_search_results_record(self):
        """Tests get_objective_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def activity_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def activity_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_activity_search()


@pytest.mark.usefixtures("activity_search_class_fixture", "activity_search_test_fixture")
class TestActivitySearch(object):
    """Tests for ActivitySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_activities(self):
        """Tests search_among_activities"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_activity_results(self):
        """Tests order_activity_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_activity_search_record(self):
        """Tests get_activity_search_record"""
        pass


@pytest.mark.usefixtures("activity_search_results_class_fixture", "activity_search_results_test_fixture")
class TestActivitySearchResults(object):
    """Tests for ActivitySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_activities(self):
        """Tests get_activities"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_activity_query_inspector(self):
        """Tests get_activity_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_activity_search_results_record(self):
        """Tests get_activity_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def proficiency_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def proficiency_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_proficiency_search()


@pytest.mark.usefixtures("proficiency_search_class_fixture", "proficiency_search_test_fixture")
class TestProficiencySearch(object):
    """Tests for ProficiencySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_proficiencies(self):
        """Tests search_among_proficiencies"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_proficiency_results(self):
        """Tests order_proficiency_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiency_search_record(self):
        """Tests get_proficiency_search_record"""
        pass


@pytest.mark.usefixtures("proficiency_search_results_class_fixture", "proficiency_search_results_test_fixture")
class TestProficiencySearchResults(object):
    """Tests for ProficiencySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_proficiencies(self):
        """Tests get_proficiencies"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiency_query_inspector(self):
        """Tests get_proficiency_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_proficiency_search_results_record(self):
        """Tests get_proficiency_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def objective_bank_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LEARNING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_objective_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_objective_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_objective_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def objective_bank_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_objective_bank_search()


@pytest.mark.usefixtures("objective_bank_search_class_fixture", "objective_bank_search_test_fixture")
class TestObjectiveBankSearch(object):
    """Tests for ObjectiveBankSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_objective_banks(self):
        """Tests search_among_objective_banks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_objective_bank_results(self):
        """Tests order_objective_bank_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_bank_search_record(self):
        """Tests get_objective_bank_search_record"""
        pass


@pytest.mark.usefixtures("objective_bank_search_results_class_fixture", "objective_bank_search_results_test_fixture")
class TestObjectiveBankSearchResults(object):
    """Tests for ObjectiveBankSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_objective_banks(self):
        """Tests get_objective_banks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_bank_query_inspector(self):
        """Tests get_objective_bank_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_objective_bank_search_results_record(self):
        """Tests get_objective_bank_search_results_record"""
        pass
