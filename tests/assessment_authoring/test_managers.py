"""Unit tests of assessment.authoring managers."""


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
def assessment_authoring_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def assessment_authoring_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_authoring_profile_class_fixture", "assessment_authoring_profile_test_fixture")
class TestAssessmentAuthoringProfile(object):
    """Tests for AssessmentAuthoringProfile"""
    def test_supports_assessment_part_lookup(self):
        """Tests supports_assessment_part_lookup"""
        assert isinstance(self.mgr.supports_assessment_part_lookup(), bool)

    def test_supports_assessment_part_query(self):
        """Tests supports_assessment_part_query"""
        assert isinstance(self.mgr.supports_assessment_part_query(), bool)

    def test_supports_assessment_part_admin(self):
        """Tests supports_assessment_part_admin"""
        assert isinstance(self.mgr.supports_assessment_part_admin(), bool)

    def test_supports_assessment_part_bank(self):
        """Tests supports_assessment_part_bank"""
        assert isinstance(self.mgr.supports_assessment_part_bank(), bool)

    def test_supports_assessment_part_bank_assignment(self):
        """Tests supports_assessment_part_bank_assignment"""
        assert isinstance(self.mgr.supports_assessment_part_bank_assignment(), bool)

    def test_supports_assessment_part_item(self):
        """Tests supports_assessment_part_item"""
        assert isinstance(self.mgr.supports_assessment_part_item(), bool)

    def test_supports_assessment_part_item_design(self):
        """Tests supports_assessment_part_item_design"""
        assert isinstance(self.mgr.supports_assessment_part_item_design(), bool)

    def test_supports_sequence_rule_lookup(self):
        """Tests supports_sequence_rule_lookup"""
        assert isinstance(self.mgr.supports_sequence_rule_lookup(), bool)

    def test_supports_sequence_rule_admin(self):
        """Tests supports_sequence_rule_admin"""
        assert isinstance(self.mgr.supports_sequence_rule_admin(), bool)

    def test_get_assessment_part_record_types(self):
        """Tests get_assessment_part_record_types"""
        assert isinstance(self.mgr.get_assessment_part_record_types(), abc_type_list)

    def test_get_assessment_part_search_record_types(self):
        """Tests get_assessment_part_search_record_types"""
        assert isinstance(self.mgr.get_assessment_part_search_record_types(), abc_type_list)

    def test_get_sequence_rule_record_types(self):
        """Tests get_sequence_rule_record_types"""
        assert isinstance(self.mgr.get_sequence_rule_record_types(), abc_type_list)

    def test_get_sequence_rule_search_record_types(self):
        """Tests get_sequence_rule_search_record_types"""
        assert isinstance(self.mgr.get_sequence_rule_search_record_types(), abc_type_list)

    def test_get_sequence_rule_enabler_record_types(self):
        """Tests get_sequence_rule_enabler_record_types"""
        assert isinstance(self.mgr.get_sequence_rule_enabler_record_types(), abc_type_list)

    def test_get_sequence_rule_enabler_search_record_types(self):
        """Tests get_sequence_rule_enabler_search_record_types"""
        assert isinstance(self.mgr.get_sequence_rule_enabler_search_record_types(), abc_type_list)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_authoring_manager_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for assessment.authoring manager tests'
        catalog = request.cls.svc_mgr.create_bank(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.mgr = Runtime().get_manager('ASSESSMENT_AUTHORING', 'TEST_JSON_1', (3, 0, 0))
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_authoring_manager_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_authoring_manager_class_fixture", "assessment_authoring_manager_test_fixture")
class TestAssessmentAuthoringManager(object):
    """Tests for AssessmentAuthoringManager"""
    def test_get_assessment_part_lookup_session(self):
        """Tests get_assessment_part_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session()

    def test_get_assessment_part_lookup_session_for_bank(self):
        """Tests get_assessment_part_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session_for_bank(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_lookup_session_for_bank()

    def test_get_assessment_part_query_session(self):
        """Tests get_assessment_part_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session()

    def test_get_assessment_part_query_session_for_bank(self):
        """Tests get_assessment_part_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session_for_bank(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_query_session_for_bank()

    def test_get_assessment_part_admin_session(self):
        """Tests get_assessment_part_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session()

    def test_get_assessment_part_admin_session_for_bank(self):
        """Tests get_assessment_part_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session_for_bank(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_admin_session_for_bank()

    def test_get_assessment_part_bank_session(self):
        """Tests get_assessment_part_bank_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_bank():
            self.svc_mgr.get_assessment_part_bank_session()

    def test_get_assessment_part_bank_assignment_session(self):
        """Tests get_assessment_part_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_bank_assignment():
            self.svc_mgr.get_assessment_part_bank_assignment_session()

    def test_get_sequence_rule_lookup_session(self):
        """Tests get_sequence_rule_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session()

    def test_get_sequence_rule_lookup_session_for_bank(self):
        """Tests get_sequence_rule_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank()

    def test_get_sequence_rule_admin_session(self):
        """Tests get_sequence_rule_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session()

    def test_get_sequence_rule_admin_session_for_bank(self):
        """Tests get_sequence_rule_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session_for_bank(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_admin_session_for_bank()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def assessment_authoring_proxy_manager_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for assessment.authoring manager tests'
        catalog = request.cls.svc_mgr.create_bank(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.mgr = Runtime().get_manager('ASSESSMENT_AUTHORING', 'TEST_JSON_1', (3, 0, 0))
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bank(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def assessment_authoring_proxy_manager_test_fixture(request):
    pass


@pytest.mark.usefixtures("assessment_authoring_proxy_manager_class_fixture", "assessment_authoring_proxy_manager_test_fixture")
class TestAssessmentAuthoringProxyManager(object):
    """Tests for AssessmentAuthoringProxyManager"""
    def test_get_assessment_part_lookup_session(self):
        """Tests get_assessment_part_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_lookup_session()

    def test_get_assessment_part_lookup_session_for_bank(self):
        """Tests get_assessment_part_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_lookup():
            self.svc_mgr.get_assessment_part_lookup_session_for_bank(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_lookup_session_for_bank()

    def test_get_assessment_part_query_session(self):
        """Tests get_assessment_part_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_query_session()

    def test_get_assessment_part_query_session_for_bank(self):
        """Tests get_assessment_part_query_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_query():
            self.svc_mgr.get_assessment_part_query_session_for_bank(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_query_session_for_bank()

    def test_get_assessment_part_admin_session(self):
        """Tests get_assessment_part_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_admin_session()

    def test_get_assessment_part_admin_session_for_bank(self):
        """Tests get_assessment_part_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_assessment_part_admin():
            self.svc_mgr.get_assessment_part_admin_session_for_bank(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_admin_session_for_bank()

    def test_get_assessment_part_bank_session(self):
        """Tests get_assessment_part_bank_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_bank():
            self.svc_mgr.get_assessment_part_bank_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_bank_session()

    def test_get_assessment_part_bank_assignment_session(self):
        """Tests get_assessment_part_bank_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_assessment_part_bank_assignment():
            self.svc_mgr.get_assessment_part_bank_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_assessment_part_bank_assignment_session()

    def test_get_sequence_rule_lookup_session(self):
        """Tests get_sequence_rule_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_lookup_session()

    def test_get_sequence_rule_lookup_session_for_bank(self):
        """Tests get_sequence_rule_lookup_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_lookup():
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_lookup_session_for_bank()

    def test_get_sequence_rule_admin_session(self):
        """Tests get_sequence_rule_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_admin_session()

    def test_get_sequence_rule_admin_session_for_bank(self):
        """Tests get_sequence_rule_admin_session_for_bank"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_sequence_rule_admin():
            self.svc_mgr.get_sequence_rule_admin_session_for_bank(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_sequence_rule_admin_session_for_bank()
