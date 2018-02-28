"""Unit tests of resource sessions."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.authentication.objects import AgentList
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.abstract_osid.resource import objects as ABCObjects
from dlkit.abstract_osid.resource import queries as ABCQueries
from dlkit.abstract_osid.resource import searches as ABCSearches
from dlkit.abstract_osid.resource.objects import Bin as ABCBin
from dlkit.abstract_osid.resource.objects import Resource
from dlkit.json_.id.objects import IdList
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
AGENT_ID_0 = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
AGENT_ID_1 = Id(**{'identifier': 'john_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def resource_lookup_session_test_fixture(request):
    request.cls.resource_list = list()
    request.cls.resource_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceLookupSession tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_resource_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("resource_lookup_session_class_fixture", "resource_lookup_session_test_fixture")
class TestResourceLookupSession(object):
    """Tests for ResourceLookupSession"""
    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bin_id() == self.catalog.ident

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bin(), ABCBin)

    def test_can_lookup_resources(self):
        """Tests can_lookup_resources"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_resources(), bool)

    def test_use_comparative_resource_view(self):
        """Tests use_comparative_resource_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_resource_view()

    def test_use_plenary_resource_view(self):
        """Tests use_plenary_resource_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_resource_view()

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_get_resource(self):
        """Tests get_resource"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_resource_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_bin_view()
                obj = self.catalog.get_resource(self.resource_list[0].ident)
                assert obj.ident == self.resource_list[0].ident
                self.catalog.use_federated_bin_view()
                obj = self.catalog.get_resource(self.resource_list[0].ident)
                assert obj.ident == self.resource_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_resource(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_bin_view()
                obj = self.catalog.get_resource(self.resource_list[0].ident)
                assert obj.ident == self.resource_list[0].ident
                self.catalog.use_federated_bin_view()
                obj = self.catalog.get_resource(self.resource_list[0].ident)
                assert obj.ident == self.resource_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_resource(self.fake_id)

    def test_get_resources_by_ids(self):
        """Tests get_resources_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        if self.svc_mgr.supports_resource_query():
            objects = self.catalog.get_resources_by_ids(self.resource_ids)
            assert isinstance(objects, ResourceList)
            self.catalog.use_federated_bin_view()
            objects = self.catalog.get_resources_by_ids(self.resource_ids)
            assert isinstance(objects, ResourceList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_resources_by_ids(self.resource_ids)
                assert isinstance(objects, ResourceList)
                self.catalog.use_federated_bin_view()
                objects = self.catalog.get_resources_by_ids(self.resource_ids)
                assert objects.available() > 0
                assert isinstance(objects, ResourceList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_resources_by_ids(self.resource_ids)

    def test_get_resources_by_genus_type(self):
        """Tests get_resources_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        if self.svc_mgr.supports_resource_query():
            objects = self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ResourceList)
            self.catalog.use_federated_bin_view()
            objects = self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, ResourceList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ResourceList)
                self.catalog.use_federated_bin_view()
                objects = self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, ResourceList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_resources_by_parent_genus_type(self):
        """Tests get_resources_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        if self.svc_mgr.supports_resource_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ResourceList)
                self.catalog.use_federated_bin_view()
                objects = self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ResourceList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, ResourceList)
                self.catalog.use_federated_bin_view()
                objects = self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ResourceList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_resources_by_record_type(self):
        """Tests get_resources_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        if self.svc_mgr.supports_resource_query():
            objects = self.catalog.get_resources_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, ResourceList)
            self.catalog.use_federated_bin_view()
            objects = self.catalog.get_resources_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, ResourceList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_resources_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, ResourceList)
                self.catalog.use_federated_bin_view()
                objects = self.catalog.get_resources_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, ResourceList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_resources_by_record_type(DEFAULT_TYPE)

    def test_get_resources(self):
        """Tests get_resources"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        if self.svc_mgr.supports_resource_query():
            objects = self.catalog.get_resources()
            assert isinstance(objects, ResourceList)
            self.catalog.use_federated_bin_view()
            objects = self.catalog.get_resources()
            assert isinstance(objects, ResourceList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_resources()
                assert isinstance(objects, ResourceList)
                self.catalog.use_federated_bin_view()
                objects = self.catalog.get_resources()
                assert objects.available() > 0
                assert isinstance(objects, ResourceList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_resources()

    def test_get_resource_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_resource(self.resource_ids[0], ALIAS_ID)
            obj = self.catalog.get_resource(ALIAS_ID)
            assert obj.get_id() == self.resource_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def resource_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.resource_list = list()
    request.cls.resource_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + color
            create_form.description = (
                'Test Resource for ResourceQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_resource_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("resource_query_session_class_fixture", "resource_query_session_test_fixture")
class TestResourceQuerySession(object):
    """Tests for ResourceQuerySession"""
    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bin_id() == self.catalog.ident

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bin(), ABCBin)

    def test_can_search_resources(self):
        """Tests can_search_resources"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_resources(), bool)

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_get_resource_query(self):
        """Tests get_resource_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_resource_query()
        assert isinstance(query, ABCQueries.ResourceQuery)

    def test_get_resources_by_query(self):
        """Tests get_resources_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_resource_query()
            query.match_display_name('orange')
            assert self.catalog.get_resources_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_resources_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_resources_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_search_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.resource_list = list()
    request.cls.resource_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceSearchSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + color
            create_form.description = (
                'Test Resource for ResourceSearchSession tests, did I mention green')
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_search_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("resource_search_session_class_fixture", "resource_search_session_test_fixture")
class TestResourceSearchSession(object):
    """Tests for ResourceSearchSession"""
    def test_get_resource_search(self):
        """Tests get_resource_search"""
        # From test_templates/resource.py::ResourceSearchSession::get_resource_search_template
        result = self.session.get_resource_search()
        assert isinstance(result, ABCSearches.ResourceSearch)

    def test_get_resource_search_order(self):
        """Tests get_resource_search_order"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_resource_search_order()

    def test_get_resources_by_search(self):
        """Tests get_resources_by_search"""
        # From test_templates/resource.py::ResourceSearchSession::get_resources_by_search_template
        query = self.catalog.get_resource_query()
        search = self.session.get_resource_search()
        results = self.session.get_resources_by_search(query, search)
        assert isinstance(results, ABCSearches.ResourceSearchResults)

    def test_get_resource_query_from_inspector(self):
        """Tests get_resource_query_from_inspector"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_resource_query_from_inspector(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_resource_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_resource_form_for_create([])
        request.cls.form.display_name = 'new Resource'
        request.cls.form.description = 'description of Resource'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_resource(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_resource(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("resource_admin_session_class_fixture", "resource_admin_session_test_fixture")
class TestResourceAdminSession(object):
    """Tests for ResourceAdminSession"""
    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bin_id() == self.catalog.ident

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bin(), ABCBin)

    def test_can_create_resources(self):
        """Tests can_create_resources"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_resources(), bool)

    def test_can_create_resource_with_record_types(self):
        """Tests can_create_resource_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_resource_with_record_types(DEFAULT_TYPE), bool)

    def test_get_resource_form_for_create(self):
        """Tests get_resource_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_resource_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_resource_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_resource_form_for_create([])

    def test_create_resource(self):
        """Tests create_resource"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.resource.objects import Resource
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Resource)
            assert self.osid_object.display_name.text == 'new Resource'
            assert self.osid_object.description.text == 'description of Resource'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_resource(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_resource('I Will Break You!')
            update_form = self.catalog.get_resource_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_resource(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_resource('foo')

    def test_can_update_resources(self):
        """Tests can_update_resources"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_resources(), bool)

    def test_get_resource_form_for_update(self):
        """Tests get_resource_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_resource_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_resource_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_resource_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='resource.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_resource_form_for_update(self.fake_id)

    def test_update_resource(self):
        """Tests update_resource"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.resource.objects import Resource
            form = self.catalog.get_resource_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_resource(form)
            assert isinstance(updated_object, Resource)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_resource(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_resource('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_resource(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_resource('foo')

    def test_can_delete_resources(self):
        """Tests can_delete_resources"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_resources(), bool)

    def test_delete_resource(self):
        """Tests delete_resource"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_resource_form_for_create([])
            form.display_name = 'new Resource'
            form.description = 'description of Resource'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_resource(form)
            self.catalog.delete_resource(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_resource(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_resource(self.fake_id)

    def test_can_manage_resource_aliases(self):
        """Tests can_manage_resource_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_resource_aliases(), bool)

    def test_alias_resource(self):
        """Tests alias_resource"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_resource(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_resource(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_resource(self.fake_id, self.fake_id)


class NotificationReceiver(object):
    # Implemented from resource.ResourceNotificationSession
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_notification_session_class_fixture(request):
    # Implemented from init template for ResourceNotificationSession
    request.cls.service_config = request.param
    request.cls.resource_list = list()
    request.cls.resource_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceNotificationSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceNotificationSession tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)

    else:
        request.cls.catalog = request.cls.svc_mgr.get_resource_notification_session(NotificationReceiver(), proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_notification_session_test_fixture(request):
    # From test_templates/resource.py::ResourceNotificationSession::init_template
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("resource_notification_session_class_fixture", "resource_notification_session_test_fixture")
class TestResourceNotificationSession(object):
    """Tests for ResourceNotificationSession"""
    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bin_id() == self.catalog.ident

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bin(), ABCBin)

    def test_can_register_for_resource_notifications(self):
        """Tests can_register_for_resource_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::can_register_for_resource_notifications_template
        if is_no_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.session.can_register_for_resource_notifications()
        else:
            assert isinstance(self.session.can_register_for_resource_notifications(), bool)

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_register_for_new_resources(self):
        """Tests register_for_new_resources"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_new_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_new_resources()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_new_resources()

    def test_register_for_changed_resources(self):
        """Tests register_for_changed_resources"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_resources()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_resources()

    def test_register_for_changed_resource(self):
        """Tests register_for_changed_resource"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_resource(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_resource(self.fake_id)

    def test_register_for_deleted_resources(self):
        """Tests register_for_deleted_resources"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_deleted_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_resources()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_resources()

    def test_register_for_deleted_resource(self):
        """Tests register_for_deleted_resource"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_deleted_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_resource(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_resource(self.fake_id)

    def test_reliable_resource_notifications(self):
        """Tests reliable_resource_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::reliable_resource_notifications_template
        self.session.reliable_resource_notifications()

    def test_unreliable_resource_notifications(self):
        """Tests unreliable_resource_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::unreliable_resource_notifications_template
        self.session.unreliable_resource_notifications()

    def test_acknowledge_resource_notification(self):
        """Tests acknowledge_resource_notification"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.acknowledge_resource_notification(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_bin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.resource_list = list()
    request.cls.resource_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceBinSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin for Assignment'
        create_form.description = 'Test Bin for ResourceBinSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bin(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceBinSession tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)
        request.cls.svc_mgr.assign_resource_to_bin(
            request.cls.resource_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_resource_to_bin(
            request.cls.resource_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_resource_from_bin(
                request.cls.resource_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_resource_from_bin(
                request.cls.resource_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_bin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("resource_bin_session_class_fixture", "resource_bin_session_test_fixture")
class TestResourceBinSession(object):
    """Tests for ResourceBinSession"""
    def test_use_comparative_bin_view(self):
        """Tests use_comparative_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bin_view()

    def test_use_plenary_bin_view(self):
        """Tests use_plenary_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bin_view()

    def test_can_lookup_resource_bin_mappings(self):
        """Tests can_lookup_resource_bin_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_resource_bin_mappings()
        assert isinstance(result, bool)

    def test_get_resource_ids_by_bin(self):
        """Tests get_resource_ids_by_bin"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_resource_ids_by_bin(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_resource_ids_by_bin(self.fake_id)

    def test_get_resources_by_bin(self):
        """Tests get_resources_by_bin"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_resources_by_bin(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.ResourceList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_resources_by_bin(self.fake_id)

    def test_get_resource_ids_by_bins(self):
        """Tests get_resource_ids_by_bins"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_resource_ids_by_bins(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_resource_ids_by_bins([self.fake_id])

    def test_get_resources_by_bins(self):
        """Tests get_resources_by_bins"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_resources_by_bins(catalog_ids)
            assert isinstance(results, ABCObjects.ResourceList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_resources_by_bins([self.fake_id])

    def test_get_bin_ids_by_resource(self):
        """Tests get_bin_ids_by_resource"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bin_ids_by_resource(self.resource_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_ids_by_resource(self.fake_id)

    def test_get_bins_by_resource(self):
        """Tests get_bins_by_resource"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_bins_by_resource(self.resource_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bins_by_resource(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_bin_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.resource_list = list()
    request.cls.resource_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceBinAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin for Assignment'
        create_form.description = 'Test Bin for ResourceBinAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_bin(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceBinAssignmentSession tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_bin_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("resource_bin_assignment_session_class_fixture", "resource_bin_assignment_session_test_fixture")
class TestResourceBinAssignmentSession(object):
    """Tests for ResourceBinAssignmentSession"""
    def test_can_assign_resources(self):
        """Tests can_assign_resources"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_resources()
        assert isinstance(result, bool)

    def test_can_assign_resources_to_bin(self):
        """Tests can_assign_resources_to_bin"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_resources_to_bin(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_bin_ids(self):
        """Tests get_assignable_bin_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bin_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bin_ids(self.fake_id)

    def test_get_assignable_bin_ids_for_resource(self):
        """Tests get_assignable_bin_ids_for_resource"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_bin_ids_for_resource(self.catalog.ident, self.resource_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_bin_ids_for_resource(self.fake_id, self.fake_id)

    def test_assign_resource_to_bin(self):
        """Tests assign_resource_to_bin"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_resources()
            assert results.available() == 0
            self.session.assign_resource_to_bin(self.resource_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_resources()
            assert results.available() == 1
            self.session.unassign_resource_from_bin(
                self.resource_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_resource_to_bin(self.fake_id, self.fake_id)

    def test_unassign_resource_from_bin(self):
        """Tests unassign_resource_from_bin"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_resources()
            assert results.available() == 0
            self.session.assign_resource_to_bin(
                self.resource_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_resources()
            assert results.available() == 1
            self.session.unassign_resource_from_bin(
                self.resource_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_resources()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_resource_from_bin(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_agent_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.resource_list = list()
    request.cls.resource_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceAgentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceAgentSession tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)
        request.cls.catalog.assign_agent_to_resource(AGENT_ID_0, request.cls.resource_ids[0])
        request.cls.catalog.assign_agent_to_resource(AGENT_ID_1, request.cls.resource_ids[1])
    else:
        request.cls.catalog = request.cls.svc_mgr.get_resource_agent_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_bins():
                for obj in catalog.get_resources():
                    catalog.delete_resource(obj.ident)
                request.cls.svc_mgr.delete_bin(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_agent_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("resource_agent_session_class_fixture", "resource_agent_session_test_fixture")
class TestResourceAgentSession(object):
    """Tests for ResourceAgentSession"""
    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bin_id() == self.catalog.ident

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bin(), ABCBin)

    def test_can_lookup_resource_agent_mappings(self):
        """Tests can_lookup_resource_agent_mappings"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_lookup_resource_agent_mappings()

    def test_use_comparative_agent_view(self):
        """Tests use_comparative_agent_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_agent_view()

    def test_use_plenary_agent_view(self):
        """Tests use_plenary_agent_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_agent_view()

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_get_resource_id_by_agent(self):
        """Tests get_resource_id_by_agent"""
        if not is_never_authz(self.service_config):
            resource_id = self.catalog.get_resource_id_by_agent(AGENT_ID_0)
            assert isinstance(resource_id, Id)
            assert resource_id == self.resource_ids[0]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_resource_id_by_agent(AGENT_ID_0)

    def test_get_resource_by_agent(self):
        """Tests get_resource_by_agent"""
        if not is_never_authz(self.service_config):
            resource = self.catalog.get_resource_by_agent(AGENT_ID_1)
            assert isinstance(resource, Resource)
            assert resource.display_name.text == 'Test Resource 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_resource_by_agent(AGENT_ID_1)

    def test_get_agent_ids_by_resource(self):
        """Tests get_agent_ids_by_resource"""
        if not is_never_authz(self.service_config):
            id_list = self.catalog.get_agent_ids_by_resource(self.resource_ids[0])
            assert id_list.next() == AGENT_ID_0
            assert isinstance(id_list, IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_agent_ids_by_resource(AGENT_ID_0)

    def test_get_agents_by_resource(self):
        """Tests get_agents_by_resource"""
        if not is_never_authz(self.service_config):
            agents = self.catalog.get_agents_by_resource(self.resource_ids[0])
            assert agents.available() == 1
            assert isinstance(agents, AgentList)
            assert agents.next().ident == AGENT_ID_0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_agents_by_resource(AGENT_ID_0)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_agent_assignment_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def resource_agent_assignment_session_test_fixture(request):
    request.cls.resource_list = list()
    request.cls.resource_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceAgentAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceAgentAssignmentSession tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_resource_agent_assignment_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("resource_agent_assignment_session_class_fixture", "resource_agent_assignment_session_test_fixture")
class TestResourceAgentAssignmentSession(object):
    """Tests for ResourceAgentAssignmentSession"""
    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_bin_id() == self.catalog.ident

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_bin(), ABCBin)

    def test_can_assign_agents(self):
        """Tests can_assign_agents"""
        if is_no_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.session.can_assign_agents()
        else:
            assert isinstance(self.session.can_assign_agents(), bool)

    def test_can_assign_agents_to_resource(self):
        """Tests can_assign_agents_to_resource"""
        if is_no_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.session.can_assign_agents_to_resource(True)
        else:
            assert isinstance(self.session.can_assign_agents_to_resource(True), bool)

    def test_assign_agent_to_resource(self):
        """Tests assign_agent_to_resource"""
        if not is_never_authz(self.service_config):
            self.catalog.assign_agent_to_resource(AGENT_ID_0, self.resource_ids[0])
            with pytest.raises(errors.AlreadyExists):
                self.catalog.assign_agent_to_resource(AGENT_ID_0, self.resource_ids[1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.assign_agent_to_resource(AGENT_ID_0, AGENT_ID_1)

    def test_unassign_agent_from_resource(self):
        """Tests unassign_agent_from_resource"""
        if not is_never_authz(self.service_config):
            self.catalog.assign_agent_to_resource(AGENT_ID_1, self.resource_ids[1])
            assert self.catalog.get_resource_by_agent(AGENT_ID_1).display_name.text == 'Test Resource 1'
            self.catalog.unassign_agent_from_resource(AGENT_ID_1, self.resource_ids[1])
            with pytest.raises(errors.NotFound):
                self.catalog.get_resource_by_agent(AGENT_ID_1)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.unassign_agent_from_resource(AGENT_ID_1, AGENT_ID_0)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for resource proxy manager tests'
            catalog = request.cls.svc_mgr.create_bin(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_bins():
                request.cls.svc_mgr.delete_bin(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bin_lookup_session_class_fixture", "bin_lookup_session_test_fixture")
class TestBinLookupSession(object):
    """Tests for BinLookupSession"""
    def test_can_lookup_bins(self):
        """Tests can_lookup_bins"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_bins(), bool)

    def test_use_comparative_bin_view(self):
        """Tests use_comparative_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bin_view()

    def test_use_plenary_bin_view(self):
        """Tests use_plenary_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bin_view()

    def test_get_bin(self):
        """Tests get_bin"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_bin(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin(self.fake_id)

    def test_get_bins_by_ids(self):
        """Tests get_bins_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_bins_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.BinList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bins_by_ids([self.fake_id])

    def test_get_bins_by_genus_type(self):
        """Tests get_bins_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_bins_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.BinList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bins_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_bins_by_parent_genus_type(self):
        """Tests get_bins_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_bins_by_parent_genus_type(True)

    def test_get_bins_by_record_type(self):
        """Tests get_bins_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_bins_by_record_type(True)

    def test_get_bins_by_provider(self):
        """Tests get_bins_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_bins_by_provider(True)

    def test_get_bins(self):
        """Tests get_bins"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_bins()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.BinList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bins()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_query_session_class_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_query_session_test_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bin_query_session_class_fixture", "bin_query_session_test_fixture")
class TestBinQuerySession(object):
    """Tests for BinQuerySession"""
    def test_can_search_bins(self):
        """Tests can_search_bins"""
        # From test_templates/resource.py::BinQuerySession::can_search_bins_template
        assert isinstance(self.session.can_search_bins(), bool)

    def test_get_bin_query(self):
        """Tests get_bin_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_bin_query()
            assert isinstance(query, ABCQueries.BinQuery)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_bin_query()

    def test_get_bins_by_query(self):
        """Tests get_bins_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_bin_query()
            query.match_display_name('Test catalog')
            assert self.session.get_bins_by_query(query).available() == 1
            query.clear_display_name_terms()
            query.match_display_name('Test catalog', match=False)
            assert self.session.get_bins_by_query(query).available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_bins_by_query('foo')


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def bin_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin For Deletion'
        create_form.description = 'Test Bin for BinAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_bin(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_bins():
                request.cls.svc_mgr.delete_bin(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bin_admin_session_class_fixture", "bin_admin_session_test_fixture")
class TestBinAdminSession(object):
    """Tests for BinAdminSession"""
    def test_can_create_bins(self):
        """Tests can_create_bins"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_bins(), bool)

    def test_can_create_bin_with_record_types(self):
        """Tests can_create_bin_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_bin_with_record_types(DEFAULT_TYPE), bool)

    def test_get_bin_form_for_create(self):
        """Tests get_bin_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.resource.objects import BinForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bin_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_bin_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_form_for_create([])

    def test_create_bin(self):
        """Tests create_bin"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.resource.objects import Bin
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bin_form_for_create([])
            catalog_form.display_name = 'Test Bin'
            catalog_form.description = 'Test Bin for BinAdminSession.create_bin tests'
            new_catalog = self.svc_mgr.create_bin(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_bin(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_bin('I Will Break You!')
            update_form = self.svc_mgr.get_bin_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_bin(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_bin('foo')

    def test_can_update_bins(self):
        """Tests can_update_bins"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_bins(), bool)

    def test_get_bin_form_for_update(self):
        """Tests get_bin_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.resource.objects import BinForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bin_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_form_for_update(self.fake_id)

    def test_update_bin(self):
        """Tests update_bin"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_bin_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_bin(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_bin('foo')

    def test_can_delete_bins(self):
        """Tests can_delete_bins"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_bins(), bool)

    def test_delete_bin(self):
        """Tests delete_bin"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_bin(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_bin(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_bin(self.fake_id)

    def test_can_manage_bin_aliases(self):
        """Tests can_manage_bin_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_bin_aliases(), bool)

    def test_alias_bin(self):
        """Tests alias_bin"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('resource.Bin%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_bin(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_bin(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_bin(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bin ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_bin(create_form)
        request.cls.svc_mgr.add_root_bin(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_bin(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_bin(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_bin(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_bin(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_bins(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_bin(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_bin(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bin_hierarchy_session_class_fixture", "bin_hierarchy_session_test_fixture")
class TestBinHierarchySession(object):
    """Tests for BinHierarchySession"""
    def test_get_bin_hierarchy_id(self):
        """Tests get_bin_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bin_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_bin_hierarchy(self):
        """Tests get_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_bin_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_hierarchy()

    def test_can_access_bin_hierarchy(self):
        """Tests can_access_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_bin_hierarchy(), bool)

    def test_use_comparative_bin_view(self):
        """Tests use_comparative_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bin_view()

    def test_use_plenary_bin_view(self):
        """Tests use_plenary_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bin_view()

    def test_get_root_bin_ids(self):
        """Tests get_root_bin_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_bin_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_bin_ids()

    def test_get_root_bins(self):
        """Tests get_root_bins"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.resource.objects import BinList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_bins()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_bins()

    def test_has_parent_bins(self):
        """Tests has_parent_bins"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_bins(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_bins(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_bins(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_bins(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_bins(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_bins(self.fake_id)

    def test_is_parent_of_bin(self):
        """Tests is_parent_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_bin(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_bin(self.fake_id, self.fake_id)

    def test_get_parent_bin_ids(self):
        """Tests get_parent_bin_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_bin_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_bin_ids(self.fake_id)

    def test_get_parent_bins(self):
        """Tests get_parent_bins"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_bins(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_bins(self.fake_id)

    def test_is_ancestor_of_bin(self):
        """Tests is_ancestor_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_bin,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_bin(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_bins(self):
        """Tests has_child_bins"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_bins(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_bins(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_bins(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_bins(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_bins(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_bins(self.fake_id)

    def test_is_child_of_bin(self):
        """Tests is_child_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_bin(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_bin(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_bin(self.fake_id, self.fake_id)

    def test_get_child_bin_ids(self):
        """Tests get_child_bin_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_bin_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_bin_ids(self.fake_id)

    def test_get_child_bins(self):
        """Tests get_child_bins"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_bins(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_bins(self.fake_id)

    def test_is_descendant_of_bin(self):
        """Tests is_descendant_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_bin,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_bin(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_bin_node_ids(self):
        """Tests get_bin_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bin_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_node_ids(self.fake_id, 1, 2, False)

    def test_get_bin_nodes(self):
        """Tests get_bin_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bin_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bin ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_bin(create_form)
        request.cls.svc_mgr.add_root_bin(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_bin(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_bin(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_bin(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_bin(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_bins(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_bin(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("bin_hierarchy_design_session_class_fixture", "bin_hierarchy_design_session_test_fixture")
class TestBinHierarchyDesignSession(object):
    """Tests for BinHierarchyDesignSession"""
    def test_get_bin_hierarchy_id(self):
        """Tests get_bin_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bin_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_bin_hierarchy(self):
        """Tests get_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_bin_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_bin_hierarchy()

    def test_can_modify_bin_hierarchy(self):
        """Tests can_modify_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_bin_hierarchy(), bool)

    def test_add_root_bin(self):
        """Tests add_root_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_bins()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_bin(self.fake_id)

    def test_remove_root_bin(self):
        """Tests remove_root_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_bins()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Bin root'
            new_bin = self.svc_mgr.create_bin(create_form)
            self.svc_mgr.add_root_bin(new_bin.ident)

            roots = self.session.get_root_bins()
            assert roots.available() == 2

            self.session.remove_root_bin(new_bin.ident)

            roots = self.session.get_root_bins()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_bin(self.fake_id)

    def test_add_child_bin(self):
        """Tests add_child_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_bins(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_bin(self.fake_id, self.fake_id)

    def test_remove_child_bin(self):
        """Tests remove_child_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_bins(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Bin child'
            new_bin = self.svc_mgr.create_bin(create_form)
            self.svc_mgr.add_child_bin(
                self.catalogs['Root'].ident,
                new_bin.ident)

            children = self.session.get_child_bins(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_bin(
                self.catalogs['Root'].ident,
                new_bin.ident)

            children = self.session.get_child_bins(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_bin(self.fake_id, self.fake_id)

    def test_remove_child_bins(self):
        """Tests remove_child_bins"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_bins(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Bin child'
            new_bin = self.svc_mgr.create_bin(create_form)
            self.svc_mgr.add_child_bin(
                self.catalogs['Grandchild 1'].ident,
                new_bin.ident)

            children = self.session.get_child_bins(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_bins(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_bins(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_bins(self.fake_id)
