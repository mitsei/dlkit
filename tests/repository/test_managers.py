"""Unit tests of repository managers."""


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
def repository_profile_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def repository_profile_test_fixture(request):
    pass


@pytest.mark.usefixtures("repository_profile_class_fixture", "repository_profile_test_fixture")
class TestRepositoryProfile(object):
    """Tests for RepositoryProfile"""
    def test_supports_asset_lookup(self):
        """Tests supports_asset_lookup"""
        assert isinstance(self.mgr.supports_asset_lookup(), bool)

    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        assert isinstance(self.mgr.supports_asset_query(), bool)

    def test_supports_asset_search(self):
        """Tests supports_asset_search"""
        assert isinstance(self.mgr.supports_asset_search(), bool)

    def test_supports_asset_admin(self):
        """Tests supports_asset_admin"""
        assert isinstance(self.mgr.supports_asset_admin(), bool)

    def test_supports_asset_notification(self):
        """Tests supports_asset_notification"""
        assert isinstance(self.mgr.supports_asset_notification(), bool)

    def test_supports_asset_repository(self):
        """Tests supports_asset_repository"""
        assert isinstance(self.mgr.supports_asset_repository(), bool)

    def test_supports_asset_repository_assignment(self):
        """Tests supports_asset_repository_assignment"""
        assert isinstance(self.mgr.supports_asset_repository_assignment(), bool)

    def test_supports_asset_composition(self):
        """Tests supports_asset_composition"""
        assert isinstance(self.mgr.supports_asset_composition(), bool)

    def test_supports_asset_composition_design(self):
        """Tests supports_asset_composition_design"""
        assert isinstance(self.mgr.supports_asset_composition_design(), bool)

    def test_supports_composition_lookup(self):
        """Tests supports_composition_lookup"""
        assert isinstance(self.mgr.supports_composition_lookup(), bool)

    def test_supports_composition_query(self):
        """Tests supports_composition_query"""
        assert isinstance(self.mgr.supports_composition_query(), bool)

    def test_supports_composition_search(self):
        """Tests supports_composition_search"""
        assert isinstance(self.mgr.supports_composition_search(), bool)

    def test_supports_composition_admin(self):
        """Tests supports_composition_admin"""
        assert isinstance(self.mgr.supports_composition_admin(), bool)

    def test_supports_composition_repository(self):
        """Tests supports_composition_repository"""
        assert isinstance(self.mgr.supports_composition_repository(), bool)

    def test_supports_composition_repository_assignment(self):
        """Tests supports_composition_repository_assignment"""
        assert isinstance(self.mgr.supports_composition_repository_assignment(), bool)

    def test_supports_repository_lookup(self):
        """Tests supports_repository_lookup"""
        assert isinstance(self.mgr.supports_repository_lookup(), bool)

    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        assert isinstance(self.mgr.supports_repository_query(), bool)

    def test_supports_repository_admin(self):
        """Tests supports_repository_admin"""
        assert isinstance(self.mgr.supports_repository_admin(), bool)

    def test_supports_repository_hierarchy(self):
        """Tests supports_repository_hierarchy"""
        assert isinstance(self.mgr.supports_repository_hierarchy(), bool)

    def test_supports_repository_hierarchy_design(self):
        """Tests supports_repository_hierarchy_design"""
        assert isinstance(self.mgr.supports_repository_hierarchy_design(), bool)

    def test_get_asset_record_types(self):
        """Tests get_asset_record_types"""
        assert isinstance(self.mgr.get_asset_record_types(), abc_type_list)

    def test_get_asset_search_record_types(self):
        """Tests get_asset_search_record_types"""
        assert isinstance(self.mgr.get_asset_search_record_types(), abc_type_list)

    def test_get_asset_content_record_types(self):
        """Tests get_asset_content_record_types"""
        assert isinstance(self.mgr.get_asset_content_record_types(), abc_type_list)

    def test_get_composition_record_types(self):
        """Tests get_composition_record_types"""
        assert isinstance(self.mgr.get_composition_record_types(), abc_type_list)

    def test_get_composition_search_record_types(self):
        """Tests get_composition_search_record_types"""
        assert isinstance(self.mgr.get_composition_search_record_types(), abc_type_list)

    def test_get_repository_record_types(self):
        """Tests get_repository_record_types"""
        assert isinstance(self.mgr.get_repository_record_types(), abc_type_list)

    def test_get_repository_search_record_types(self):
        """Tests get_repository_search_record_types"""
        assert isinstance(self.mgr.get_repository_search_record_types(), abc_type_list)

    def test_get_spatial_unit_record_types(self):
        """Tests get_spatial_unit_record_types"""
        assert isinstance(self.mgr.get_spatial_unit_record_types(), abc_type_list)

    def test_get_coordinate_types(self):
        """Tests get_coordinate_types"""
        assert isinstance(self.mgr.get_coordinate_types(), abc_type_list)


class NotificationReceiver(object):
    # Implemented from resource.ResourceManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_manager_class_fixture(request):
    # Implemented from resource.ResourceManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for repository manager tests'
        catalog = request.cls.svc_mgr.create_repository(create_form)
        request.cls.catalog_id = catalog.get_id()
        request.cls.receiver = NotificationReceiver()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_manager_test_fixture(request):
    # Implemented from resource.ResourceManager
    pass


@pytest.mark.usefixtures("repository_manager_class_fixture", "repository_manager_test_fixture")
class TestRepositoryManager(object):
    """Tests for RepositoryManager"""
    def test_get_asset_lookup_session(self):
        """Tests get_asset_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session()

    def test_get_asset_lookup_session_for_repository(self):
        """Tests get_asset_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_lookup_session_for_repository()

    def test_get_asset_query_session(self):
        """Tests get_asset_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session()

    def test_get_asset_query_session_for_repository(self):
        """Tests get_asset_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_query_session_for_repository()

    def test_get_asset_search_session(self):
        """Tests get_asset_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session()

    def test_get_asset_search_session_for_repository(self):
        """Tests get_asset_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_search_session_for_repository()

    def test_get_asset_admin_session(self):
        """Tests get_asset_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session()

    def test_get_asset_admin_session_for_repository(self):
        """Tests get_asset_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_admin_session_for_repository()

    def test_get_asset_notification_session(self):
        """Tests get_asset_notification_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session(self.receiver)

    def test_get_asset_notification_session_for_repository(self):
        """Tests get_asset_notification_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session_for_repository(self.receiver, self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_notification_session_for_repository()

    def test_get_asset_repository_session(self):
        """Tests get_asset_repository_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository():
            self.svc_mgr.get_asset_repository_session()

    def test_get_asset_repository_assignment_session(self):
        """Tests get_asset_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository_assignment():
            self.svc_mgr.get_asset_repository_assignment_session()

    def test_get_asset_composition_session(self):
        """Tests get_asset_composition_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition():
            self.svc_mgr.get_asset_composition_session()

    def test_get_asset_composition_design_session(self):
        """Tests get_asset_composition_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition_design():
            self.svc_mgr.get_asset_composition_design_session()

    def test_get_composition_lookup_session(self):
        """Tests get_composition_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session()

    def test_get_composition_lookup_session_for_repository(self):
        """Tests get_composition_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_lookup_session_for_repository()

    def test_get_composition_query_session(self):
        """Tests get_composition_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session()

    def test_get_composition_query_session_for_repository(self):
        """Tests get_composition_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_query_session_for_repository()

    def test_get_composition_search_session(self):
        """Tests get_composition_search_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session()

    def test_get_composition_search_session_for_repository(self):
        """Tests get_composition_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_search_session_for_repository()

    def test_get_composition_admin_session(self):
        """Tests get_composition_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session()

    def test_get_composition_admin_session_for_repository(self):
        """Tests get_composition_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session_for_repository(self.catalog_id)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_admin_session_for_repository()

    def test_get_composition_repository_session(self):
        """Tests get_composition_repository_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository():
            self.svc_mgr.get_composition_repository_session()

    def test_get_composition_repository_assignment_session(self):
        """Tests get_composition_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository_assignment():
            self.svc_mgr.get_composition_repository_assignment_session()

    def test_get_repository_lookup_session(self):
        """Tests get_repository_lookup_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_lookup():
            self.svc_mgr.get_repository_lookup_session()

    def test_get_repository_query_session(self):
        """Tests get_repository_query_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_query():
            self.svc_mgr.get_repository_query_session()

    def test_get_repository_admin_session(self):
        """Tests get_repository_admin_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_admin():
            self.svc_mgr.get_repository_admin_session()

    def test_get_repository_hierarchy_session(self):
        """Tests get_repository_hierarchy_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy():
            self.svc_mgr.get_repository_hierarchy_session()

    def test_get_repository_hierarchy_design_session(self):
        """Tests get_repository_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy_design():
            self.svc_mgr.get_repository_hierarchy_design_session()

    def test_get_repository_batch_manager(self):
        """Tests get_repository_batch_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_repository_batch():
            self.svc_mgr.get_repository_batch_manager()

    def test_get_repository_rules_manager(self):
        """Tests get_repository_rules_manager"""
        # From tests_templates/resource.py::ResourceManager::get_resource_batch_manager_template
        if self.svc_mgr.supports_repository_rules():
            self.svc_mgr.get_repository_rules_manager()


class NotificationReceiver(object):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_proxy_manager_class_fixture(request):
    # Implemented from resource.ResourceProxyManager
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for repository proxy manager tests'
        catalog = request.cls.svc_mgr.create_repository(create_form)
        request.cls.catalog_id = catalog.get_id()
    else:
        request.cls.catalog_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')
    request.cls.receiver = NotificationReceiver()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog_id)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_proxy_manager_test_fixture(request):
    # Implemented from resource.ResourceProxyManager
    pass


@pytest.mark.usefixtures("repository_proxy_manager_class_fixture", "repository_proxy_manager_test_fixture")
class TestRepositoryProxyManager(object):
    """Tests for RepositoryProxyManager"""
    def test_get_asset_lookup_session(self):
        """Tests get_asset_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_lookup_session()

    def test_get_asset_lookup_session_for_repository(self):
        """Tests get_asset_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_lookup():
            self.svc_mgr.get_asset_lookup_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_lookup_session_for_repository()

    def test_get_asset_query_session(self):
        """Tests get_asset_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_query_session()

    def test_get_asset_query_session_for_repository(self):
        """Tests get_asset_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_asset_query():
            self.svc_mgr.get_asset_query_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_query_session_for_repository()

    def test_get_asset_search_session(self):
        """Tests get_asset_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_search_session()

    def test_get_asset_search_session_for_repository(self):
        """Tests get_asset_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_search():
            self.svc_mgr.get_asset_search_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_search_session_for_repository()

    def test_get_asset_admin_session(self):
        """Tests get_asset_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_admin_session()

    def test_get_asset_admin_session_for_repository(self):
        """Tests get_asset_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_asset_admin():
            self.svc_mgr.get_asset_admin_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_admin_session_for_repository()

    def test_get_asset_notification_session(self):
        """Tests get_asset_notification_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session(self.receiver, proxy=PROXY)

    def test_get_asset_notification_session_for_repository(self):
        """Tests get_asset_notification_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_notification_session_for_bin_template
        if self.svc_mgr.supports_asset_notification():
            self.svc_mgr.get_asset_notification_session_for_repository(self.receiver, self.catalog_id, proxy=PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_notification_session_for_repository()

    def test_get_asset_repository_session(self):
        """Tests get_asset_repository_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository():
            self.svc_mgr.get_asset_repository_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_repository_session()

    def test_get_asset_repository_assignment_session(self):
        """Tests get_asset_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_repository_assignment():
            self.svc_mgr.get_asset_repository_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_repository_assignment_session()

    def test_get_asset_composition_session(self):
        """Tests get_asset_composition_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition():
            self.svc_mgr.get_asset_composition_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_composition_session()

    def test_get_asset_composition_design_session(self):
        """Tests get_asset_composition_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_asset_composition_design():
            self.svc_mgr.get_asset_composition_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_asset_composition_design_session()

    def test_get_composition_lookup_session(self):
        """Tests get_composition_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_lookup_session()

    def test_get_composition_lookup_session_for_repository(self):
        """Tests get_composition_lookup_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_lookup():
            self.svc_mgr.get_composition_lookup_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_lookup_session_for_repository()

    def test_get_composition_query_session(self):
        """Tests get_composition_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_query_session()

    def test_get_composition_query_session_for_repository(self):
        """Tests get_composition_query_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_lookup_session_for_bin_template
        if self.svc_mgr.supports_composition_query():
            self.svc_mgr.get_composition_query_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_query_session_for_repository()

    def test_get_composition_search_session(self):
        """Tests get_composition_search_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_search_session()

    def test_get_composition_search_session_for_repository(self):
        """Tests get_composition_search_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_search():
            self.svc_mgr.get_composition_search_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_search_session_for_repository()

    def test_get_composition_admin_session(self):
        """Tests get_composition_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_admin_session()

    def test_get_composition_admin_session_for_repository(self):
        """Tests get_composition_admin_session_for_repository"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_for_bin_template
        if self.svc_mgr.supports_composition_admin():
            self.svc_mgr.get_composition_admin_session_for_repository(self.catalog_id, PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_admin_session_for_repository()

    def test_get_composition_repository_session(self):
        """Tests get_composition_repository_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository():
            self.svc_mgr.get_composition_repository_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_repository_session()

    def test_get_composition_repository_assignment_session(self):
        """Tests get_composition_repository_assignment_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_composition_repository_assignment():
            self.svc_mgr.get_composition_repository_assignment_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_composition_repository_assignment_session()

    def test_get_repository_lookup_session(self):
        """Tests get_repository_lookup_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_lookup():
            self.svc_mgr.get_repository_lookup_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_repository_lookup_session()

    def test_get_repository_query_session(self):
        """Tests get_repository_query_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_query():
            self.svc_mgr.get_repository_query_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_repository_query_session()

    def test_get_repository_admin_session(self):
        """Tests get_repository_admin_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_admin():
            self.svc_mgr.get_repository_admin_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_repository_admin_session()

    def test_get_repository_hierarchy_session(self):
        """Tests get_repository_hierarchy_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy():
            self.svc_mgr.get_repository_hierarchy_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_repository_hierarchy_session()

    def test_get_repository_hierarchy_design_session(self):
        """Tests get_repository_hierarchy_design_session"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_admin_session_template
        if self.svc_mgr.supports_repository_hierarchy_design():
            self.svc_mgr.get_repository_hierarchy_design_session(PROXY)
        with pytest.raises(errors.NullArgument):
            self.svc_mgr.get_repository_hierarchy_design_session()

    def test_get_repository_batch_proxy_manager(self):
        """Tests get_repository_batch_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_repository_batch():
            self.svc_mgr.get_repository_batch_proxy_manager()

    def test_get_repository_rules_proxy_manager(self):
        """Tests get_repository_rules_proxy_manager"""
        # From tests_templates/resource.py::ResourceProxyManager::get_resource_batch_proxy_manager_template
        if self.svc_mgr.supports_repository_rules():
            self.svc_mgr.get_repository_rules_proxy_manager()
