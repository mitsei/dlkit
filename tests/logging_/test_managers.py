"""Unit tests of logging managers."""


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
def logging_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def logging_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("logging_profile_class_fixture", "logging_profile_test_fixture")
class TestLoggingProfile(object):
    """Tests for LoggingProfile"""
    def test_supports_logging(self):
        """Tests supports_logging"""
        assert isinstance(self.mgr.supports_logging(), bool)

    def test_supports_log_entry_lookup(self):
        """Tests supports_log_entry_lookup"""
        assert isinstance(self.mgr.supports_log_entry_lookup(), bool)

    def test_supports_log_entry_query(self):
        """Tests supports_log_entry_query"""
        assert isinstance(self.mgr.supports_log_entry_query(), bool)

    def test_supports_log_entry_log(self):
        """Tests supports_log_entry_log"""
        assert isinstance(self.mgr.supports_log_entry_log(), bool)

    def test_supports_log_entry_log_assignment(self):
        """Tests supports_log_entry_log_assignment"""
        assert isinstance(self.mgr.supports_log_entry_log_assignment(), bool)

    def test_supports_log_lookup(self):
        """Tests supports_log_lookup"""
        assert isinstance(self.mgr.supports_log_lookup(), bool)

    def test_supports_log_admin(self):
        """Tests supports_log_admin"""
        assert isinstance(self.mgr.supports_log_admin(), bool)

    def test_supports_log_hierarchy(self):
        """Tests supports_log_hierarchy"""
        assert isinstance(self.mgr.supports_log_hierarchy(), bool)

    def test_supports_log_hierarchy_design(self):
        """Tests supports_log_hierarchy_design"""
        assert isinstance(self.mgr.supports_log_hierarchy_design(), bool)

    def test_get_log_entry_record_types(self):
        """Tests get_log_entry_record_types"""
        assert isinstance(self.mgr.get_log_entry_record_types(), abc_type_list)

    def test_get_log_entry_search_record_types(self):
        """Tests get_log_entry_search_record_types"""
        assert isinstance(self.mgr.get_log_entry_search_record_types(), abc_type_list)

    def test_get_log_record_types(self):
        """Tests get_log_record_types"""
        assert isinstance(self.mgr.get_log_record_types(), abc_type_list)

    def test_get_log_search_record_types(self):
        """Tests get_log_search_record_types"""
        assert isinstance(self.mgr.get_log_search_record_types(), abc_type_list)

    def test_get_priority_types(self):
        """Tests get_priority_types"""
        assert isinstance(self.mgr.get_priority_types(), abc_type_list)

    def test_get_content_types(self):
        """Tests get_content_types"""
        assert isinstance(self.mgr.get_content_types(), abc_type_list)

    def test_supports_log_entry_admin(self):
        """Tests supports_log_entry_admin"""
        assert isinstance(self.mgr.supports_log_entry_admin(), bool)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def logging_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for logging manager tests'
        catalog = request.cls.svc_mgr.create_log(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_log(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def logging_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("logging_manager_class_fixture", "logging_manager_test_fixture")
class TestLoggingManager(object):
    """Tests for LoggingManager"""
    def test_get_logging_session(self):
        """Tests get_logging_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session()

    def test_get_logging_session_for_log(self):
        """Tests get_logging_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session_for_log(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_logging_session_for_log()

    def test_get_log_entry_lookup_session(self):
        """Tests get_log_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session()

    def test_get_log_entry_lookup_session_for_log(self):
        """Tests get_log_entry_lookup_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session_for_log(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_lookup_session_for_log()

    def test_get_log_entry_query_session(self):
        """Tests get_log_entry_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session()

    def test_get_log_entry_query_session_for_log(self):
        """Tests get_log_entry_query_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session_for_log(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_query_session_for_log()

    def test_get_log_entry_admin_session(self):
        """Tests get_log_entry_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session()

    def test_get_log_entry_admin_session_for_log(self):
        """Tests get_log_entry_admin_session_for_log"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session_for_log(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_admin_session_for_log()

    def test_get_log_entry_log_session(self):
        """Tests get_log_entry_log_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_log():
            self.svc_mgr.get_log_entry_log_session()

    def test_get_log_entry_log_assignment_session(self):
        """Tests get_log_entry_log_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_log_assignment():
            self.svc_mgr.get_log_entry_log_assignment_session()

    def test_get_log_lookup_session(self):
        """Tests get_log_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_lookup():
            self.svc_mgr.get_log_lookup_session()

    def test_get_log_admin_session(self):
        """Tests get_log_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_admin():
            self.svc_mgr.get_log_admin_session()

    def test_get_log_hierarchy_session(self):
        """Tests get_log_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_hierarchy():
            self.svc_mgr.get_log_hierarchy_session()

    def test_get_log_hierarchy_design_session(self):
        """Tests get_log_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_hierarchy_design():
            self.svc_mgr.get_log_hierarchy_design_session()

    def test_get_logging_batch_manager(self):
        """Tests get_logging_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_logging_batch():
            self.svc_mgr.get_logging_batch_manager()


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def logging_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'LOGGING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for logging proxy manager tests'
        catalog = request.cls.svc_mgr.create_log(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_log(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def logging_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("logging_proxy_manager_class_fixture", "logging_proxy_manager_test_fixture")
class TestLoggingProxyManager(object):
    """Tests for LoggingProxyManager"""
    def test_get_logging_session(self):
        """Tests get_logging_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_logging_session()

    def test_get_logging_session_for_log(self):
        """Tests get_logging_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_logging():
            self.svc_mgr.get_logging_session_for_log(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_logging_session_for_log()

    def test_get_log_entry_lookup_session(self):
        """Tests get_log_entry_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_lookup_session()

    def test_get_log_entry_lookup_session_for_log(self):
        """Tests get_log_entry_lookup_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_log_entry_lookup():
            self.svc_mgr.get_log_entry_lookup_session_for_log(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_lookup_session_for_log()

    def test_get_log_entry_query_session(self):
        """Tests get_log_entry_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_query_session()

    def test_get_log_entry_query_session_for_log(self):
        """Tests get_log_entry_query_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_log_entry_query():
            self.svc_mgr.get_log_entry_query_session_for_log(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_query_session_for_log()

    def test_get_log_entry_admin_session(self):
        """Tests get_log_entry_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_admin_session()

    def test_get_log_entry_admin_session_for_log(self):
        """Tests get_log_entry_admin_session_for_log"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_log_entry_admin():
            self.svc_mgr.get_log_entry_admin_session_for_log(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_admin_session_for_log()

    def test_get_log_entry_log_session(self):
        """Tests get_log_entry_log_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_log():
            self.svc_mgr.get_log_entry_log_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_log_session()

    def test_get_log_entry_log_assignment_session(self):
        """Tests get_log_entry_log_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_entry_log_assignment():
            self.svc_mgr.get_log_entry_log_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_entry_log_assignment_session()

    def test_get_log_lookup_session(self):
        """Tests get_log_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_lookup():
            self.svc_mgr.get_log_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_lookup_session()

    def test_get_log_admin_session(self):
        """Tests get_log_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_admin():
            self.svc_mgr.get_log_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_admin_session()

    def test_get_log_hierarchy_session(self):
        """Tests get_log_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_hierarchy():
            self.svc_mgr.get_log_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_hierarchy_session()

    def test_get_log_hierarchy_design_session(self):
        """Tests get_log_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_log_hierarchy_design():
            self.svc_mgr.get_log_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_log_hierarchy_design_session()

    def test_get_logging_batch_proxy_manager(self):
        """Tests get_logging_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_logging_batch():
            self.svc_mgr.get_logging_batch_proxy_manager()
