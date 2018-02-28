"""Unit tests of resource managers."""


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
def resource_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def resource_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("resource_profile_class_fixture", "resource_profile_test_fixture")
class TestResourceProfile(object):
    """Tests for ResourceProfile"""
    def test_supports_resource_lookup(self):
        """Tests supports_resource_lookup"""
        assert isinstance(self.mgr.supports_resource_lookup(), bool)

    def test_supports_resource_query(self):
        """Tests supports_resource_query"""
        assert isinstance(self.mgr.supports_resource_query(), bool)

    def test_supports_resource_search(self):
        """Tests supports_resource_search"""
        assert isinstance(self.mgr.supports_resource_search(), bool)

    def test_supports_resource_admin(self):
        """Tests supports_resource_admin"""
        assert isinstance(self.mgr.supports_resource_admin(), bool)

    def test_supports_resource_notification(self):
        """Tests supports_resource_notification"""
        assert isinstance(self.mgr.supports_resource_notification(), bool)

    def test_supports_resource_bin(self):
        """Tests supports_resource_bin"""
        assert isinstance(self.mgr.supports_resource_bin(), bool)

    def test_supports_resource_bin_assignment(self):
        """Tests supports_resource_bin_assignment"""
        assert isinstance(self.mgr.supports_resource_bin_assignment(), bool)

    def test_supports_resource_agent(self):
        """Tests supports_resource_agent"""
        assert isinstance(self.mgr.supports_resource_agent(), bool)

    def test_supports_resource_agent_assignment(self):
        """Tests supports_resource_agent_assignment"""
        assert isinstance(self.mgr.supports_resource_agent_assignment(), bool)

    def test_supports_bin_lookup(self):
        """Tests supports_bin_lookup"""
        assert isinstance(self.mgr.supports_bin_lookup(), bool)

    def test_supports_bin_query(self):
        """Tests supports_bin_query"""
        assert isinstance(self.mgr.supports_bin_query(), bool)

    def test_supports_bin_admin(self):
        """Tests supports_bin_admin"""
        assert isinstance(self.mgr.supports_bin_admin(), bool)

    def test_supports_bin_hierarchy(self):
        """Tests supports_bin_hierarchy"""
        assert isinstance(self.mgr.supports_bin_hierarchy(), bool)

    def test_supports_bin_hierarchy_design(self):
        """Tests supports_bin_hierarchy_design"""
        assert isinstance(self.mgr.supports_bin_hierarchy_design(), bool)

    def test_get_resource_record_types(self):
        """Tests get_resource_record_types"""
        assert isinstance(self.mgr.get_resource_record_types(), abc_type_list)

    def test_get_resource_search_record_types(self):
        """Tests get_resource_search_record_types"""
        assert isinstance(self.mgr.get_resource_search_record_types(), abc_type_list)

    def test_get_resource_relationship_record_types(self):
        """Tests get_resource_relationship_record_types"""
        assert isinstance(self.mgr.get_resource_relationship_record_types(), abc_type_list)

    def test_get_resource_relationship_search_record_types(self):
        """Tests get_resource_relationship_search_record_types"""
        assert isinstance(self.mgr.get_resource_relationship_search_record_types(), abc_type_list)

    def test_get_bin_record_types(self):
        """Tests get_bin_record_types"""
        assert isinstance(self.mgr.get_bin_record_types(), abc_type_list)

    def test_get_bin_search_record_types(self):
        """Tests get_bin_search_record_types"""
        assert isinstance(self.mgr.get_bin_search_record_types(), abc_type_list)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for resource manager tests'
        catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("resource_manager_class_fixture", "resource_manager_test_fixture")
class TestResourceManager(object):
    """Tests for ResourceManager"""
    def test_get_resource_lookup_session(self):
        """Tests get_resource_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session()

    def test_get_resource_lookup_session_for_bin(self):
        """Tests get_resource_lookup_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session_for_bin(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_lookup_session_for_bin()

    def test_get_resource_query_session(self):
        """Tests get_resource_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session()

    def test_get_resource_query_session_for_bin(self):
        """Tests get_resource_query_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session_for_bin(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_query_session_for_bin()

    def test_get_resource_search_session(self):
        """Tests get_resource_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session()

    def test_get_resource_search_session_for_bin(self):
        """Tests get_resource_search_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session_for_bin(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_search_session_for_bin()

    def test_get_resource_admin_session(self):
        """Tests get_resource_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session()

    def test_get_resource_admin_session_for_bin(self):
        """Tests get_resource_admin_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session_for_bin(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_admin_session_for_bin()

    def test_get_resource_notification_session(self):
        """Tests get_resource_notification_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session(self.receiver)

    def test_get_resource_notification_session_for_bin(self):
        """Tests get_resource_notification_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session_for_bin(self.receiver, self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_notification_session_for_bin()

    def test_get_resource_bin_session(self):
        """Tests get_resource_bin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin():
            self.svc_mgr.get_resource_bin_session()

    def test_get_resource_bin_assignment_session(self):
        """Tests get_resource_bin_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin_assignment():
            self.svc_mgr.get_resource_bin_assignment_session()

    def test_get_resource_agent_session(self):
        """Tests get_resource_agent_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session()

    def test_get_resource_agent_session_for_bin(self):
        """Tests get_resource_agent_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session_for_bin(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_session_for_bin()

    def test_get_resource_agent_assignment_session(self):
        """Tests get_resource_agent_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session()

    def test_get_resource_agent_assignment_session_for_bin(self):
        """Tests get_resource_agent_assignment_session_for_bin"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session_for_bin(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_assignment_session_for_bin()

    def test_get_bin_lookup_session(self):
        """Tests get_bin_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_lookup():
            self.svc_mgr.get_bin_lookup_session()

    def test_get_bin_query_session(self):
        """Tests get_bin_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_query():
            self.svc_mgr.get_bin_query_session()

    def test_get_bin_admin_session(self):
        """Tests get_bin_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_admin():
            self.svc_mgr.get_bin_admin_session()

    def test_get_bin_hierarchy_session(self):
        """Tests get_bin_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy():
            self.svc_mgr.get_bin_hierarchy_session()

    def test_get_bin_hierarchy_design_session(self):
        """Tests get_bin_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy_design():
            self.svc_mgr.get_bin_hierarchy_design_session()

    def test_get_resource_batch_manager(self):
        """Tests get_resource_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_resource_batch():
            self.svc_mgr.get_resource_batch_manager()

    def test_get_resource_demographic_manager(self):
        """Tests get_resource_demographic_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_resource_demographic():
            self.svc_mgr.get_resource_demographic_manager()


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for resource proxy manager tests'
        catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("resource_proxy_manager_class_fixture", "resource_proxy_manager_test_fixture")
class TestResourceProxyManager(object):
    """Tests for ResourceProxyManager"""
    def test_get_resource_lookup_session(self):
        """Tests get_resource_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_lookup_session()

    def test_get_resource_lookup_session_for_bin(self):
        """Tests get_resource_lookup_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_lookup():
            self.svc_mgr.get_resource_lookup_session_for_bin(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_lookup_session_for_bin()

    def test_get_resource_query_session(self):
        """Tests get_resource_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_query_session()

    def test_get_resource_query_session_for_bin(self):
        """Tests get_resource_query_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_resource_query():
            self.svc_mgr.get_resource_query_session_for_bin(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_query_session_for_bin()

    def test_get_resource_search_session(self):
        """Tests get_resource_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_search_session()

    def test_get_resource_search_session_for_bin(self):
        """Tests get_resource_search_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_search():
            self.svc_mgr.get_resource_search_session_for_bin(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_search_session_for_bin()

    def test_get_resource_admin_session(self):
        """Tests get_resource_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_admin_session()

    def test_get_resource_admin_session_for_bin(self):
        """Tests get_resource_admin_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_admin():
            self.svc_mgr.get_resource_admin_session_for_bin(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_admin_session_for_bin()

    def test_get_resource_notification_session(self):
        """Tests get_resource_notification_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session(self.receiver, proxy=PROXY)

    def test_get_resource_notification_session_for_bin(self):
        """Tests get_resource_notification_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_resource_notification():
            self.svc_mgr.get_resource_notification_session_for_bin(self.receiver, self.catalog_id, proxy=PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_notification_session_for_bin()

    def test_get_resource_bin_session(self):
        """Tests get_resource_bin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin():
            self.svc_mgr.get_resource_bin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_bin_session()

    def test_get_resource_bin_assignment_session(self):
        """Tests get_resource_bin_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_bin_assignment():
            self.svc_mgr.get_resource_bin_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_bin_assignment_session()

    def test_get_group_hierarchy_session(self):
        """Tests get_group_hierarchy_session"""
        if self.svc_mgr.supports_group_hierarchy():
            self.svc_mgr.get_group_hierarchy_session(PROXY)
        with pytest.raises(errors.Unimplemented):
            self.svc_mgr.get_group_hierarchy_session()

    def test_get_resource_agent_session(self):
        """Tests get_resource_agent_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_session()

    def test_get_resource_agent_session_for_bin(self):
        """Tests get_resource_agent_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent():
            self.svc_mgr.get_resource_agent_session_for_bin(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_session_for_bin()

    def test_get_resource_agent_assignment_session(self):
        """Tests get_resource_agent_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_assignment_session()

    def test_get_resource_agent_assignment_session_for_bin(self):
        """Tests get_resource_agent_assignment_session_for_bin"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_resource_agent_assignment():
            self.svc_mgr.get_resource_agent_assignment_session_for_bin(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_resource_agent_assignment_session_for_bin()

    def test_get_bin_lookup_session(self):
        """Tests get_bin_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_lookup():
            self.svc_mgr.get_bin_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_bin_lookup_session()

    def test_get_bin_query_session(self):
        """Tests get_bin_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_query():
            self.svc_mgr.get_bin_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_bin_query_session()

    def test_get_bin_admin_session(self):
        """Tests get_bin_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_admin():
            self.svc_mgr.get_bin_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_bin_admin_session()

    def test_get_bin_hierarchy_session(self):
        """Tests get_bin_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy():
            self.svc_mgr.get_bin_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_bin_hierarchy_session()

    def test_get_bin_hierarchy_design_session(self):
        """Tests get_bin_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_bin_hierarchy_design():
            self.svc_mgr.get_bin_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_bin_hierarchy_design_session()

    def test_get_resource_batch_proxy_manager(self):
        """Tests get_resource_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_resource_batch():
            self.svc_mgr.get_resource_batch_proxy_manager()

    def test_get_resource_demographic_proxy_manager(self):
        """Tests get_resource_demographic_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_resource_demographic():
            self.svc_mgr.get_resource_demographic_proxy_manager()
