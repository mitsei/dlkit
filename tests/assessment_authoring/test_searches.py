"""Unit tests of assessment.authoring searches."""


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
def assessment_part_search_class_fixture(request):
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
def assessment_part_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_assessment_part_search()


@pytest.mark.usefixtures("assessment_part_search_class_fixture", "assessment_part_search_test_fixture")
class TestAssessmentPartSearch(object):
    """Tests for AssessmentPartSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assessment_parts(self):
        """Tests search_among_assessment_parts"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_assessment_part_results(self):
        """Tests order_assessment_part_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_part_search_record(self):
        """Tests get_assessment_part_search_record"""
        pass


@pytest.mark.usefixtures("assessment_part_search_results_class_fixture", "assessment_part_search_results_test_fixture")
class TestAssessmentPartSearchResults(object):
    """Tests for AssessmentPartSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_parts(self):
        """Tests get_assessment_parts"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_part_query_inspector(self):
        """Tests get_assessment_part_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_part_search_results_record(self):
        """Tests get_assessment_part_search_results_record"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def sequence_rule_search_class_fixture(request):
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
def sequence_rule_search_test_fixture(request):
    # From test_templates/resource.py::ResourceSearch::init_template
    request.cls.search = request.cls.catalog.get_sequence_rule_search()


@pytest.mark.usefixtures("sequence_rule_search_class_fixture", "sequence_rule_search_test_fixture")
class TestSequenceRuleSearch(object):
    """Tests for SequenceRuleSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_sequence_rules(self):
        """Tests search_among_sequence_rules"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_sequence_rule_results(self):
        """Tests order_sequence_rule_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rule_search_record(self):
        """Tests get_sequence_rule_search_record"""
        pass


@pytest.mark.usefixtures("sequence_rule_search_results_class_fixture", "sequence_rule_search_results_test_fixture")
class TestSequenceRuleSearchResults(object):
    """Tests for SequenceRuleSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rules(self):
        """Tests get_sequence_rules"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rule_query_inspector(self):
        """Tests get_sequence_rule_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rule_search_results_record(self):
        """Tests get_sequence_rule_search_results_record"""
        pass
