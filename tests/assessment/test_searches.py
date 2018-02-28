"""Unit tests of assessment searches."""


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
def item_search_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_search_test_fixture(request):
    request.cls.search = request.cls.catalog.get_item_search()


@pytest.mark.usefixtures("item_search_class_fixture", "item_search_test_fixture")
class TestItemSearch(object):
    """Tests for ItemSearch"""
    def test_search_among_items(self):
        """Tests search_among_items"""
        if not is_never_authz(self.service_config):
            assert self.search._id_list is None
            fake_list = [self.catalog.ident]
            self.search.search_among_items(fake_list)
            assert self.search._id_list == fake_list

    @pytest.mark.skip('unimplemented test')
    def test_order_item_results(self):
        """Tests order_item_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_item_search_record(self):
        """Tests get_item_search_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def item_search_results_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def item_search_results_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.catalog.get_item_query()
        request.cls.search_obj = request.cls.catalog.get_item_search()
        request.cls.search = request.cls.catalog.get_items_by_search(request.cls.query, request.cls.search_obj)


@pytest.mark.usefixtures("item_search_results_class_fixture", "item_search_results_test_fixture")
class TestItemSearchResults(object):
    """Tests for ItemSearchResults"""
    def test_get_items(self):
        """Tests get_items"""
        from dlkit.abstract_osid.assessment.objects import ItemList
        if not is_never_authz(self.service_config):
            items = self.search.get_items()
            assert isinstance(items, ItemList)
            assert items.available() == 0

    @pytest.mark.skip('unimplemented test')
    def test_get_item_query_inspector(self):
        """Tests get_item_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_item_search_results_record(self):
        """Tests get_item_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_assessment_search()


@pytest.mark.usefixtures("assessment_search_class_fixture", "assessment_search_test_fixture")
class TestAssessmentSearch(object):
    """Tests for AssessmentSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assessments(self):
        """Tests search_among_assessments"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_assessment_results(self):
        """Tests order_assessment_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_search_record(self):
        """Tests get_assessment_search_record"""
        pass


@pytest.mark.usefixtures("assessment_search_results_class_fixture", "assessment_search_results_test_fixture")
class TestAssessmentSearchResults(object):
    """Tests for AssessmentSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assessments(self):
        """Tests get_assessments"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_query_inspector(self):
        """Tests get_assessment_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_search_results_record(self):
        """Tests get_assessment_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_offered_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_offered_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_assessment_offered_search()


@pytest.mark.usefixtures("assessment_offered_search_class_fixture", "assessment_offered_search_test_fixture")
class TestAssessmentOfferedSearch(object):
    """Tests for AssessmentOfferedSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assessments_offered(self):
        """Tests search_among_assessments_offered"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_assessment_offered_results(self):
        """Tests order_assessment_offered_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_offered_search_record(self):
        """Tests get_assessment_offered_search_record"""
        pass


@pytest.mark.usefixtures("assessment_offered_search_results_class_fixture", "assessment_offered_search_results_test_fixture")
class TestAssessmentOfferedSearchResults(object):
    """Tests for AssessmentOfferedSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assessments_offered(self):
        """Tests get_assessments_offered"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_offered_query_inspector(self):
        """Tests get_assessment_offered_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_offered_search_results_record(self):
        """Tests get_assessment_offered_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_taken_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_taken_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_assessment_taken_search()


@pytest.mark.usefixtures("assessment_taken_search_class_fixture", "assessment_taken_search_test_fixture")
class TestAssessmentTakenSearch(object):
    """Tests for AssessmentTakenSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assessments_taken(self):
        """Tests search_among_assessments_taken"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_assessment_taken_results(self):
        """Tests order_assessment_taken_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_taken_search_record(self):
        """Tests get_assessment_taken_search_record"""
        pass


@pytest.mark.usefixtures("assessment_taken_search_results_class_fixture", "assessment_taken_search_results_test_fixture")
class TestAssessmentTakenSearchResults(object):
    """Tests for AssessmentTakenSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assessments_taken(self):
        """Tests get_assessments_taken"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_taken_query_inspector(self):
        """Tests get_assessment_taken_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_taken_search_results_record(self):
        """Tests get_assessment_taken_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bank_search_class_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    create_form = request.cls.svc_mgr.get_bank_form_for_create([])
    create_form.display_name = 'Test catalog'
    create_form.description = 'Test catalog description'
    request.cls.catalog = request.cls.svc_mgr.create_bank(create_form)

    def class_tear_down():
        request.cls.svc_mgr.delete_bank(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bank_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_bank_search()


@pytest.mark.usefixtures("bank_search_class_fixture", "bank_search_test_fixture")
class TestBankSearch(object):
    """Tests for BankSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_banks(self):
        """Tests search_among_banks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_bank_results(self):
        """Tests order_bank_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bank_search_record(self):
        """Tests get_bank_search_record"""
        pass


@pytest.mark.usefixtures("bank_search_results_class_fixture", "bank_search_results_test_fixture")
class TestBankSearchResults(object):
    """Tests for BankSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_banks(self):
        """Tests get_banks"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bank_query_inspector(self):
        """Tests get_bank_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bank_search_results_record(self):
        """Tests get_bank_search_results_record"""
        pass
