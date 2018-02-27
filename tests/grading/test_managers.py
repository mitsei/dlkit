"""Unit tests of grading managers."""


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
def grading_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def grading_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("grading_profile_class_fixture", "grading_profile_test_fixture")
class TestGradingProfile(object):
    """Tests for GradingProfile"""
    def test_supports_grade_system_lookup(self):
        """Tests supports_grade_system_lookup"""
        assert isinstance(self.mgr.supports_grade_system_lookup(), bool)

    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        assert isinstance(self.mgr.supports_grade_system_query(), bool)

    def test_supports_grade_system_admin(self):
        """Tests supports_grade_system_admin"""
        assert isinstance(self.mgr.supports_grade_system_admin(), bool)

    def test_supports_grade_system_gradebook(self):
        """Tests supports_grade_system_gradebook"""
        assert isinstance(self.mgr.supports_grade_system_gradebook(), bool)

    def test_supports_grade_system_gradebook_assignment(self):
        """Tests supports_grade_system_gradebook_assignment"""
        assert isinstance(self.mgr.supports_grade_system_gradebook_assignment(), bool)

    def test_supports_grade_entry_lookup(self):
        """Tests supports_grade_entry_lookup"""
        assert isinstance(self.mgr.supports_grade_entry_lookup(), bool)

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        assert isinstance(self.mgr.supports_grade_entry_query(), bool)

    def test_supports_grade_entry_admin(self):
        """Tests supports_grade_entry_admin"""
        assert isinstance(self.mgr.supports_grade_entry_admin(), bool)

    def test_supports_gradebook_column_lookup(self):
        """Tests supports_gradebook_column_lookup"""
        assert isinstance(self.mgr.supports_gradebook_column_lookup(), bool)

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        assert isinstance(self.mgr.supports_gradebook_column_query(), bool)

    def test_supports_gradebook_column_admin(self):
        """Tests supports_gradebook_column_admin"""
        assert isinstance(self.mgr.supports_gradebook_column_admin(), bool)

    def test_supports_gradebook_column_gradebook(self):
        """Tests supports_gradebook_column_gradebook"""
        assert isinstance(self.mgr.supports_gradebook_column_gradebook(), bool)

    def test_supports_gradebook_column_gradebook_assignment(self):
        """Tests supports_gradebook_column_gradebook_assignment"""
        assert isinstance(self.mgr.supports_gradebook_column_gradebook_assignment(), bool)

    def test_supports_gradebook_lookup(self):
        """Tests supports_gradebook_lookup"""
        assert isinstance(self.mgr.supports_gradebook_lookup(), bool)

    def test_supports_gradebook_admin(self):
        """Tests supports_gradebook_admin"""
        assert isinstance(self.mgr.supports_gradebook_admin(), bool)

    def test_supports_gradebook_hierarchy(self):
        """Tests supports_gradebook_hierarchy"""
        assert isinstance(self.mgr.supports_gradebook_hierarchy(), bool)

    def test_supports_gradebook_hierarchy_design(self):
        """Tests supports_gradebook_hierarchy_design"""
        assert isinstance(self.mgr.supports_gradebook_hierarchy_design(), bool)

    def test_get_grade_record_types(self):
        """Tests get_grade_record_types"""
        assert isinstance(self.mgr.get_grade_record_types(), abc_type_list)

    def test_get_grade_system_record_types(self):
        """Tests get_grade_system_record_types"""
        assert isinstance(self.mgr.get_grade_system_record_types(), abc_type_list)

    def test_get_grade_system_search_record_types(self):
        """Tests get_grade_system_search_record_types"""
        assert isinstance(self.mgr.get_grade_system_search_record_types(), abc_type_list)

    def test_get_grade_entry_record_types(self):
        """Tests get_grade_entry_record_types"""
        assert isinstance(self.mgr.get_grade_entry_record_types(), abc_type_list)

    def test_get_grade_entry_search_record_types(self):
        """Tests get_grade_entry_search_record_types"""
        assert isinstance(self.mgr.get_grade_entry_search_record_types(), abc_type_list)

    def test_get_gradebook_column_record_types(self):
        """Tests get_gradebook_column_record_types"""
        assert isinstance(self.mgr.get_gradebook_column_record_types(), abc_type_list)

    def test_get_gradebook_column_search_record_types(self):
        """Tests get_gradebook_column_search_record_types"""
        assert isinstance(self.mgr.get_gradebook_column_search_record_types(), abc_type_list)

    def test_get_gradebook_column_summary_record_types(self):
        """Tests get_gradebook_column_summary_record_types"""
        assert isinstance(self.mgr.get_gradebook_column_summary_record_types(), abc_type_list)

    def test_get_gradebook_record_types(self):
        """Tests get_gradebook_record_types"""
        assert isinstance(self.mgr.get_gradebook_record_types(), abc_type_list)

    def test_get_gradebook_search_record_types(self):
        """Tests get_gradebook_search_record_types"""
        assert isinstance(self.mgr.get_gradebook_search_record_types(), abc_type_list)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grading_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for grading manager tests'
        catalog = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grading_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("grading_manager_class_fixture", "grading_manager_test_fixture")
class TestGradingManager(object):
    """Tests for GradingManager"""
    def test_get_grade_system_lookup_session(self):
        """Tests get_grade_system_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session()

    def test_get_grade_system_lookup_session_for_gradebook(self):
        """Tests get_grade_system_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook()

    def test_get_grade_system_query_session(self):
        """Tests get_grade_system_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session()

    def test_get_grade_system_query_session_for_gradebook(self):
        """Tests get_grade_system_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_query_session_for_gradebook()

    def test_get_grade_system_admin_session(self):
        """Tests get_grade_system_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session()

    def test_get_grade_system_admin_session_for_gradebook(self):
        """Tests get_grade_system_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_admin_session_for_gradebook()

    def test_get_grade_system_gradebook_session(self):
        """Tests get_grade_system_gradebook_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_gradebook():
            self.svc_mgr.get_grade_system_gradebook_session()

    def test_get_grade_system_gradebook_assignment_session(self):
        """Tests get_grade_system_gradebook_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_gradebook_assignment():
            self.svc_mgr.get_grade_system_gradebook_assignment_session()

    def test_get_grade_entry_lookup_session(self):
        """Tests get_grade_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session()

    def test_get_grade_entry_lookup_session_for_gradebook(self):
        """Tests get_grade_entry_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook()

    def test_get_grade_entry_query_session(self):
        """Tests get_grade_entry_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session()

    def test_get_grade_entry_query_session_for_gradebook(self):
        """Tests get_grade_entry_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_query_session_for_gradebook()

    def test_get_grade_entry_admin_session(self):
        """Tests get_grade_entry_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session()

    def test_get_grade_entry_admin_session_for_gradebook(self):
        """Tests get_grade_entry_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook()

    def test_get_gradebook_column_lookup_session(self):
        """Tests get_gradebook_column_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session()

    def test_get_gradebook_column_lookup_session_for_gradebook(self):
        """Tests get_gradebook_column_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook()

    def test_get_gradebook_column_query_session(self):
        """Tests get_gradebook_column_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session()

    def test_get_gradebook_column_query_session_for_gradebook(self):
        """Tests get_gradebook_column_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook()

    def test_get_gradebook_column_admin_session(self):
        """Tests get_gradebook_column_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session()

    def test_get_gradebook_column_admin_session_for_gradebook(self):
        """Tests get_gradebook_column_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook()

    def test_get_gradebook_column_gradebook_session(self):
        """Tests get_gradebook_column_gradebook_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_gradebook():
            self.svc_mgr.get_gradebook_column_gradebook_session()

    def test_get_gradebook_column_gradebook_assignment_session(self):
        """Tests get_gradebook_column_gradebook_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_gradebook_assignment():
            self.svc_mgr.get_gradebook_column_gradebook_assignment_session()

    def test_get_gradebook_lookup_session(self):
        """Tests get_gradebook_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_lookup():
            self.svc_mgr.get_gradebook_lookup_session()

    def test_get_gradebook_admin_session(self):
        """Tests get_gradebook_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_admin():
            self.svc_mgr.get_gradebook_admin_session()

    def test_get_gradebook_hierarchy_session(self):
        """Tests get_gradebook_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_hierarchy():
            self.svc_mgr.get_gradebook_hierarchy_session()

    def test_get_gradebook_hierarchy_design_session(self):
        """Tests get_gradebook_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_hierarchy_design():
            self.svc_mgr.get_gradebook_hierarchy_design_session()

    def test_get_grading_batch_manager(self):
        """Tests get_grading_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_grading_batch():
            self.svc_mgr.get_grading_batch_manager()

    def test_get_grading_calculation_manager(self):
        """Tests get_grading_calculation_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_grading_calculation():
            self.svc_mgr.get_grading_calculation_manager()

    def test_get_grading_transform_manager(self):
        """Tests get_grading_transform_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_grading_transform():
            self.svc_mgr.get_grading_transform_manager()


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def grading_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'GRADING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for grading proxy manager tests'
        catalog = request.cls.svc_mgr.create_gradebook(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_gradebook(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def grading_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("grading_proxy_manager_class_fixture", "grading_proxy_manager_test_fixture")
class TestGradingProxyManager(object):
    """Tests for GradingProxyManager"""
    def test_get_grade_system_lookup_session(self):
        """Tests get_grade_system_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_lookup_session()

    def test_get_grade_system_lookup_session_for_gradebook(self):
        """Tests get_grade_system_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_lookup():
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_lookup_session_for_gradebook()

    def test_get_grade_system_query_session(self):
        """Tests get_grade_system_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_query_session()

    def test_get_grade_system_query_session_for_gradebook(self):
        """Tests get_grade_system_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_system_query():
            self.svc_mgr.get_grade_system_query_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_query_session_for_gradebook()

    def test_get_grade_system_admin_session(self):
        """Tests get_grade_system_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_admin_session()

    def test_get_grade_system_admin_session_for_gradebook(self):
        """Tests get_grade_system_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_system_admin():
            self.svc_mgr.get_grade_system_admin_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_admin_session_for_gradebook()

    def test_get_grade_system_gradebook_session(self):
        """Tests get_grade_system_gradebook_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_gradebook():
            self.svc_mgr.get_grade_system_gradebook_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_gradebook_session()

    def test_get_grade_system_gradebook_assignment_session(self):
        """Tests get_grade_system_gradebook_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_system_gradebook_assignment():
            self.svc_mgr.get_grade_system_gradebook_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_system_gradebook_assignment_session()

    def test_get_grade_entry_lookup_session(self):
        """Tests get_grade_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_lookup_session()

    def test_get_grade_entry_lookup_session_for_gradebook(self):
        """Tests get_grade_entry_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_lookup():
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_lookup_session_for_gradebook()

    def test_get_grade_entry_query_session(self):
        """Tests get_grade_entry_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_query_session()

    def test_get_grade_entry_query_session_for_gradebook(self):
        """Tests get_grade_entry_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_query():
            self.svc_mgr.get_grade_entry_query_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_query_session_for_gradebook()

    def test_get_grade_entry_admin_session(self):
        """Tests get_grade_entry_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_admin_session()

    def test_get_grade_entry_admin_session_for_gradebook(self):
        """Tests get_grade_entry_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_grade_entry_admin():
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_grade_entry_admin_session_for_gradebook()

    def test_get_gradebook_column_lookup_session(self):
        """Tests get_gradebook_column_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_lookup_session()

    def test_get_gradebook_column_lookup_session_for_gradebook(self):
        """Tests get_gradebook_column_lookup_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_lookup():
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_lookup_session_for_gradebook()

    def test_get_gradebook_column_query_session(self):
        """Tests get_gradebook_column_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_query_session()

    def test_get_gradebook_column_query_session_for_gradebook(self):
        """Tests get_gradebook_column_query_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_query():
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_query_session_for_gradebook()

    def test_get_gradebook_column_admin_session(self):
        """Tests get_gradebook_column_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_admin_session()

    def test_get_gradebook_column_admin_session_for_gradebook(self):
        """Tests get_gradebook_column_admin_session_for_gradebook"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_gradebook_column_admin():
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_admin_session_for_gradebook()

    def test_get_gradebook_column_gradebook_session(self):
        """Tests get_gradebook_column_gradebook_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_gradebook():
            self.svc_mgr.get_gradebook_column_gradebook_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_gradebook_session()

    def test_get_gradebook_column_gradebook_assignment_session(self):
        """Tests get_gradebook_column_gradebook_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_column_gradebook_assignment():
            self.svc_mgr.get_gradebook_column_gradebook_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_column_gradebook_assignment_session()

    def test_get_gradebook_lookup_session(self):
        """Tests get_gradebook_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_lookup():
            self.svc_mgr.get_gradebook_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_lookup_session()

    def test_get_gradebook_admin_session(self):
        """Tests get_gradebook_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_admin():
            self.svc_mgr.get_gradebook_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_admin_session()

    def test_get_gradebook_hierarchy_session(self):
        """Tests get_gradebook_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_hierarchy():
            self.svc_mgr.get_gradebook_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_hierarchy_session()

    def test_get_gradebook_hierarchy_design_session(self):
        """Tests get_gradebook_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_gradebook_hierarchy_design():
            self.svc_mgr.get_gradebook_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_gradebook_hierarchy_design_session()

    def test_get_grading_batch_proxy_manager(self):
        """Tests get_grading_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_grading_batch():
            self.svc_mgr.get_grading_batch_proxy_manager()

    def test_get_grading_calculation_proxy_manager(self):
        """Tests get_grading_calculation_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_grading_calculation():
            self.svc_mgr.get_grading_calculation_proxy_manager()

    def test_get_grading_transform_proxy_manager(self):
        """Tests get_grading_transform_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_grading_transform():
            self.svc_mgr.get_grading_transform_proxy_manager()
