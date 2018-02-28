"""Unit tests of repository sessions."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.abstract_osid.repository import objects as ABCObjects
from dlkit.abstract_osid.repository import queries as ABCQueries
from dlkit.abstract_osid.repository import searches
from dlkit.abstract_osid.repository import searches as ABCSearches
from dlkit.abstract_osid.repository.objects import Repository as ABCRepository
from dlkit.json_.id.objects import IdList
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.types.string import get_type_data as get_string_type_data
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
DEFAULT_STRING_MATCH_TYPE = Type(**get_string_type_data("WORDIGNORECASE"))
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_lookup_session_class_fixture(request):
    # Implemented from init template for ResourceLookupSession
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def asset_lookup_session_test_fixture(request):
    request.cls.asset_list = list()
    request.cls.asset_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetLookupSession tests'
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("asset_lookup_session_class_fixture", "asset_lookup_session_test_fixture")
class TestAssetLookupSession(object):
    """Tests for AssetLookupSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_lookup_assets(self):
        """Tests can_lookup_assets"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_assets(), bool)

    def test_use_comparative_asset_view(self):
        """Tests use_comparative_asset_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_asset_view()

    def test_use_plenary_asset_view(self):
        """Tests use_plenary_asset_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_asset_view()

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_repository_view()

    def test_get_asset(self):
        """Tests get_asset"""
        if not is_never_authz(self.service_config):
            self.catalog.use_isolated_repository_view()
            obj = self.catalog.get_asset(self.asset_list[0].ident)
            assert obj.ident == self.asset_list[0].ident
            self.catalog.use_federated_repository_view()
            obj = self.catalog.get_asset(self.asset_list[0].ident)
            assert obj.ident == self.asset_list[0].ident
        else:
            with pytest.raises(errors.NotFound):
                self.catalog.get_asset(self.fake_id)

    def test_get_assets_by_ids(self):
        """Tests get_assets_by_ids"""
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_ids(self.asset_ids)
        assert isinstance(objects, AssetList)
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_ids(self.asset_ids)
        assert isinstance(objects, AssetList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assets_by_genus_type(self):
        """Tests get_assets_by_genus_type"""
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, AssetList)
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_genus_type(DEFAULT_GENUS_TYPE)
        assert isinstance(objects, AssetList)
        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_assets_by_parent_genus_type(self):
        """Tests get_assets_by_parent_genus_type"""
        from dlkit.abstract_osid.repository.objects import AssetList
        if not is_never_authz(self.service_config):
            objects = self.catalog.get_assets_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AssetList)
            self.catalog.use_federated_repository_view()
            objects = self.catalog.get_assets_by_parent_genus_type(DEFAULT_GENUS_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, AssetList)
        else:
            with pytest.raises(errors.Unimplemented):
                # because the never_authz "tries harder" and runs the actual query...
                #    whereas above the method itself in JSON returns an empty list
                self.catalog.get_assets_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_assets_by_record_type(self):
        """Tests get_assets_by_record_type"""
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_record_type(DEFAULT_TYPE)
        assert isinstance(objects, AssetList)
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_record_type(DEFAULT_TYPE)
        assert objects.available() == 0
        assert isinstance(objects, AssetList)

    def test_get_assets_by_provider(self):
        """Tests get_assets_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_assets_by_provider(True)

    def test_get_assets(self):
        """Tests get_assets"""
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets()
        assert isinstance(objects, AssetList)
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets()
        assert isinstance(objects, AssetList)

        if not is_never_authz(self.service_config):
            assert objects.available() > 0
        else:
            assert objects.available() == 0

    def test_get_asset_with_alias(self):
        if not is_never_authz(self.service_config):
            self.catalog.alias_asset(self.asset_ids[0], ALIAS_ID)
            obj = self.catalog.get_asset(ALIAS_ID)
            assert obj.get_id() == self.asset_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def asset_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.asset_list = list()
    request.cls.asset_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + color
            create_form.description = (
                'Test Asset for AssetQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("asset_query_session_class_fixture", "asset_query_session_test_fixture")
class TestAssetQuerySession(object):
    """Tests for AssetQuerySession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_search_assets(self):
        """Tests can_search_assets"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_assets(), bool)

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_repository_view()

    def test_get_asset_query(self):
        """Tests get_asset_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_asset_query()
        assert isinstance(query, ABCQueries.AssetQuery)

    def test_get_assets_by_query(self):
        """Tests get_assets_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_asset_query()
            query.match_display_name('orange')
            assert self.catalog.get_assets_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_assets_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assets_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_search_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_search_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_search_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("asset_search_session_class_fixture", "asset_search_session_test_fixture")
class TestAssetSearchSession(object):
    """Tests for AssetSearchSession"""
    def test_get_asset_search(self):
        """Tests get_asset_search"""
        if not is_never_authz(self.service_config):
            search = self.session.get_asset_search()
            assert isinstance(search, searches.AssetSearch)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_asset_search()

    def test_get_asset_search_order(self):
        """Tests get_asset_search_order"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_asset_search_order()

    def test_get_assets_by_search(self):
        """Tests get_assets_by_search"""
        if not is_never_authz(self.service_config):
            query = self.session.get_asset_query()
            query.match_display_name('zxy', DEFAULT_STRING_MATCH_TYPE, True)
            search = self.session.get_asset_search()
            results = self.session.get_assets_by_search(query, search)
            assert isinstance(results, searches.AssetSearchResults)
            assert results.get_result_size() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assets_by_search(FakeQuery(), 'foo')

    def test_get_asset_query_from_inspector(self):
        """Tests get_asset_query_from_inspector"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_asset_query_from_inspector(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_admin_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_asset_form_for_create([])
        request.cls.form.display_name = 'new Asset'
        request.cls.form.description = 'description of Asset'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_asset(request.cls.form)
        request.cls.parent_object = request.cls.osid_object
    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_asset(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("asset_admin_session_class_fixture", "asset_admin_session_test_fixture")
class TestAssetAdminSession(object):
    """Tests for AssetAdminSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_create_assets(self):
        """Tests can_create_assets"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_assets(), bool)

    def test_can_create_asset_with_record_types(self):
        """Tests can_create_asset_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_asset_with_record_types(DEFAULT_TYPE), bool)

    def test_get_asset_form_for_create(self):
        """Tests get_asset_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_asset_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_asset_form_for_create([])

    def test_create_asset(self):
        """Tests create_asset"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.repository.objects import Asset
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Asset)
            assert self.osid_object.display_name.text == 'new Asset'
            assert self.osid_object.description.text == 'description of Asset'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_asset(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_asset('I Will Break You!')
            update_form = self.catalog.get_asset_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_asset(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_asset('foo')

    def test_can_update_assets(self):
        """Tests can_update_assets"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_assets(), bool)

    def test_get_asset_form_for_update(self):
        """Tests get_asset_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_asset_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_asset_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='repository.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_asset_form_for_update(self.fake_id)

    def test_update_asset(self):
        """Tests update_asset"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.repository.objects import Asset
            form = self.catalog.get_asset_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_asset(form)
            assert isinstance(updated_object, Asset)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_asset(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_asset('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_asset(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_asset('foo')

    def test_can_delete_assets(self):
        """Tests can_delete_assets"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_assets(), bool)

    def test_delete_asset(self):
        """Tests delete_asset"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_form_for_create([])
            form.display_name = 'new Asset'
            form.description = 'description of Asset'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_asset(form)
            self.catalog.delete_asset(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_asset(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_asset(self.fake_id)

    def test_can_manage_asset_aliases(self):
        """Tests can_manage_asset_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_asset_aliases(), bool)

    def test_alias_asset(self):
        """Tests alias_asset"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_asset(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_asset(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_asset(self.fake_id, self.fake_id)

    def test_can_create_asset_content(self):
        """Tests can_create_asset_content"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_asset_content(), bool)

    def test_can_create_asset_content_with_record_types(self):
        """Tests can_create_asset_content_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_asset_content_with_record_types(DEFAULT_TYPE), bool)

    def test_get_asset_content_form_for_create(self):
        """Tests get_asset_content_form_for_create"""
        # From test_templates/learning.py::ActivityAdminSession::get_activity_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_content_form_for_create(self.parent_object.ident, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_asset_content_form_for_create(self.fake_id, [])

    def test_create_asset_content(self):
        """Tests create_asset_content"""
        if not is_never_authz(self.service_config):
            results = self.parent_object.get_asset_contents()
            assert isinstance(results, ABCObjects.AssetContentList)
            assert results.available() == 0

            form = self.catalog.get_asset_content_form_for_create(self.parent_object.ident, [])
            result = self.catalog.create_asset_content(form)
            assert isinstance(result, ABCObjects.AssetContent)

            updated_parent = self.catalog.get_asset(self.parent_object.ident)
            results = updated_parent.get_asset_contents()
            assert results.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_asset_content('foo')

    def test_can_update_asset_contents(self):
        """Tests can_update_asset_contents"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_asset_contents(), bool)

    def test_get_asset_content_form_for_update(self):
        """Tests get_asset_content_form_for_update"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_content_form_for_create(self.parent_object.ident, [])
            new_aggregated_object = self.catalog.create_asset_content(form)

            form = self.catalog.get_asset_content_form_for_update(new_aggregated_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_asset_content_form_for_update(self.fake_id)

    def test_update_asset_content(self):
        """Tests update_asset_content"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_content_form_for_create(self.parent_object.ident, [])
            form.display_name = 'old name'
            new_aggregated_object = self.catalog.create_asset_content(form)

            assert new_aggregated_object.display_name.text == 'old name'

            form = self.catalog.get_asset_content_form_for_update(new_aggregated_object.ident)
            form.display_name = 'new name'
            result = self.catalog.update_asset_content(form)
            assert isinstance(result, ABCObjects.AssetContent)
            assert result.display_name.text == 'new name'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_asset_content('foo')

    def test_can_delete_asset_contents(self):
        """Tests can_delete_asset_contents"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_asset_contents(), bool)

    def test_delete_asset_content(self):
        """Tests delete_asset_content"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_asset_content_form_for_create(self.parent_object.ident, [])
            result = self.catalog.create_asset_content(form)

            updated_parent = self.catalog.get_asset(self.parent_object.ident)
            results = updated_parent.get_asset_contents()
            assert results.available() == 1

            self.catalog.delete_asset_content(result.ident)

            results = self.parent_object.get_asset_contents()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_asset_content(self.fake_id)


class NotificationReceiver(object):
    # Implemented from resource.ResourceNotificationSession
    pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_notification_session_class_fixture(request):
    # Implemented from init template for ResourceNotificationSession
    request.cls.service_config = request.param
    request.cls.asset_list = list()
    request.cls.asset_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetNotificationSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetNotificationSession tests'
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)

    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_notification_session(NotificationReceiver(), proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_notification_session_test_fixture(request):
    # From test_templates/resource.py::ResourceNotificationSession::init_template
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("asset_notification_session_class_fixture", "asset_notification_session_test_fixture")
class TestAssetNotificationSession(object):
    """Tests for AssetNotificationSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_register_for_asset_notifications(self):
        """Tests can_register_for_asset_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::can_register_for_resource_notifications_template
        if is_no_authz(self.service_config):
            with pytest.raises(errors.Unimplemented):
                self.session.can_register_for_asset_notifications()
        else:
            assert isinstance(self.session.can_register_for_asset_notifications(), bool)

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_repository_view()

    def test_register_for_new_assets(self):
        """Tests register_for_new_assets"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_new_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_new_assets()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_new_assets()

    def test_register_for_new_assets_by_genus_type(self):
        """Tests register_for_new_assets_by_genus_type"""
        if not is_never_authz(self.service_config):
            self.session.register_for_new_assets_by_genus_type(Id('package.Catalog%3Afake%40DLKIT.MIT.EDU'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_new_assets_by_genus_type(Id('package.Catalog%3Afake%40DLKIT.MIT.EDU'))

    def test_register_for_changed_assets(self):
        """Tests register_for_changed_assets"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_assets()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_assets()

    def test_register_for_changed_assets_by_genus_type(self):
        """Tests register_for_changed_assets_by_genus_type"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_assets_by_genus_type(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_assets_by_genus_type(self.fake_id)

    def test_register_for_changed_asset(self):
        """Tests register_for_changed_asset"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_changed_asset(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_changed_asset(self.fake_id)

    def test_register_for_deleted_assets(self):
        """Tests register_for_deleted_assets"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_deleted_resources_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_assets()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_assets()

    def test_register_for_deleted_assets_by_genus_type(self):
        """Tests register_for_deleted_assets_by_genus_type"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_changed_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_assets_by_genus_type(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_assets_by_genus_type(self.fake_id)

    def test_register_for_deleted_asset(self):
        """Tests register_for_deleted_asset"""
        # From test_templates/resource.py::ResourceNotificationSession::register_for_deleted_resource_template
        if not is_never_authz(self.service_config):
            self.session.register_for_deleted_asset(self.fake_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.register_for_deleted_asset(self.fake_id)

    def test_reliable_asset_notifications(self):
        """Tests reliable_asset_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::reliable_resource_notifications_template
        self.session.reliable_asset_notifications()

    def test_unreliable_asset_notifications(self):
        """Tests unreliable_asset_notifications"""
        # From test_templates/resource.py::ResourceNotificationSession::unreliable_resource_notifications_template
        self.session.unreliable_asset_notifications()

    def test_acknowledge_asset_notification(self):
        """Tests acknowledge_asset_notification"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.acknowledge_asset_notification(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_repository_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.asset_list = list()
    request.cls.asset_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetRepositorySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository for Assignment'
        create_form.description = 'Test Repository for AssetRepositorySession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetRepositorySession tests'
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)
        request.cls.svc_mgr.assign_asset_to_repository(
            request.cls.asset_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_asset_to_repository(
            request.cls.asset_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_asset_from_repository(
                request.cls.asset_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_asset_from_repository(
                request.cls.asset_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_repository_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("asset_repository_session_class_fixture", "asset_repository_session_test_fixture")
class TestAssetRepositorySession(object):
    """Tests for AssetRepositorySession"""
    def test_can_lookup_asset_repository_mappings(self):
        """Tests can_lookup_asset_repository_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_asset_repository_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_repository_view(self):
        """Tests use_comparative_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_repository_view()

    def test_use_plenary_repository_view(self):
        """Tests use_plenary_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_repository_view()

    def test_get_asset_ids_by_repository(self):
        """Tests get_asset_ids_by_repository"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_asset_ids_by_repository(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_asset_ids_by_repository(self.fake_id)

    def test_get_assets_by_repository(self):
        """Tests get_assets_by_repository"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_assets_by_repository(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AssetList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assets_by_repository(self.fake_id)

    def test_get_asset_ids_by_repositories(self):
        """Tests get_asset_ids_by_repositories"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_asset_ids_by_repositories(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_asset_ids_by_repositories([self.fake_id])

    def test_get_assets_by_repositories(self):
        """Tests get_assets_by_repositories"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_assets_by_repositories(catalog_ids)
            assert isinstance(results, ABCObjects.AssetList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assets_by_repositories([self.fake_id])

    def test_get_repository_ids_by_asset(self):
        """Tests get_repository_ids_by_asset"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_repository_ids_by_asset(self.asset_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_ids_by_asset(self.fake_id)

    def test_get_repositories_by_asset(self):
        """Tests get_repositories_by_asset"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_repositories_by_asset(self.asset_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repositories_by_asset(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_repository_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.asset_list = list()
    request.cls.asset_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetRepositoryAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository for Assignment'
        create_form.description = 'Test Repository for AssetRepositoryAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetRepositoryAssignmentSession tests'
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_assets():
                request.cls.catalog.delete_asset(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_repository_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("asset_repository_assignment_session_class_fixture", "asset_repository_assignment_session_test_fixture")
class TestAssetRepositoryAssignmentSession(object):
    """Tests for AssetRepositoryAssignmentSession"""
    def test_can_assign_assets(self):
        """Tests can_assign_assets"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assets()
        assert isinstance(result, bool)

    def test_can_assign_assets_to_repository(self):
        """Tests can_assign_assets_to_repository"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assets_to_repository(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_repository_ids(self):
        """Tests get_assignable_repository_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_repository_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_repository_ids(self.fake_id)

    def test_get_assignable_repository_ids_for_asset(self):
        """Tests get_assignable_repository_ids_for_asset"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_repository_ids_for_asset(self.catalog.ident, self.asset_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_repository_ids_for_asset(self.fake_id, self.fake_id)

    def test_assign_asset_to_repository(self):
        """Tests assign_asset_to_repository"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assets()
            assert results.available() == 0
            self.session.assign_asset_to_repository(self.asset_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assets()
            assert results.available() == 1
            self.session.unassign_asset_from_repository(
                self.asset_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_asset_to_repository(self.fake_id, self.fake_id)

    def test_unassign_asset_from_repository(self):
        """Tests unassign_asset_from_repository"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_assets()
            assert results.available() == 0
            self.session.assign_asset_to_repository(
                self.asset_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assets()
            assert results.available() == 1
            self.session.unassign_asset_from_repository(
                self.asset_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_assets()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_asset_from_repository(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_composition_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.asset_list = list()
    request.cls.asset_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        create_form = request.cls.catalog.get_composition_form_for_create([])
        create_form.display_name = 'Test Composition for AssetCompositionSession tests'
        create_form.description = 'Test Compposion for AssetCompositionSession tests'
        request.cls.composition = request.cls.catalog.create_composition(create_form)
        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetLookupSession tests'
            obj = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(obj)
            request.cls.asset_ids.append(obj.ident)
            request.cls.catalog.add_asset(obj.ident, request.cls.composition.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_composition_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_repositories():
                catalog.use_unsequestered_composition_view()
                for obj in catalog.get_assets():
                    catalog.delete_asset(obj.ident)
                for obj in catalog.get_compositions():
                    catalog.delete_composition(obj.ident)
                request.cls.svc_mgr.delete_repository(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_composition_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("asset_composition_session_class_fixture", "asset_composition_session_test_fixture")
class TestAssetCompositionSession(object):
    """Tests for AssetCompositionSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_access_asset_compositions(self):
        """Tests can_access_asset_compositions"""
        # From test_templates/repository.py::AssetCompositionSession::can_access_asset_compositions_template
        assert isinstance(self.session.can_access_asset_compositions(), bool)

    def test_use_comparative_asset_composition_view(self):
        """Tests use_comparative_asset_composition_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_asset_composition_view()

    def test_use_plenary_asset_composition_view(self):
        """Tests use_plenary_asset_composition_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_asset_composition_view()

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_repository_view()

    def test_get_composition_assets(self):
        """Tests get_composition_assets"""
        # From test_templates/repository.py::AssetCompositionSession::get_composition_assets_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_composition_assets(self.composition.ident).available() == 4
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_composition_assets(self.fake_id)

    def test_get_compositions_by_asset(self):
        """Tests get_compositions_by_asset"""
        # From test_templates/repository.py::AssetCompositionSession::get_compositions_by_asset_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_compositions_by_asset(self.asset_ids[0]).available() == 1
            assert self.catalog.get_compositions_by_asset(self.asset_ids[0]).next().ident == self.composition.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_compositions_by_asset(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_composition_design_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.asset_list = list()
    request.cls.asset_ids = list()
    request.cls.composition_list = list()
    request.cls.composition_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetCompositionDesignSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetCompositionDesignSession tests' + str(num)
            asset = request.cls.catalog.create_asset(create_form)
            request.cls.asset_list.append(asset)
            request.cls.asset_ids.append(asset.ident)
        for num in [0, 1, 2, 3, 4]:
            create_form = request.cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Compposion for AssetCompositionDesignSession tests ' + str(num)
            composition = request.cls.catalog.create_composition(create_form)
            request.cls.composition_list.append(composition)
            request.cls.composition_ids.append(composition.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_asset_composition_design_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_repositories():
                for obj in catalog.get_compositions():
                    catalog.delete_composition(obj.ident)
                for obj in catalog.get_assets():
                    catalog.delete_asset(obj.ident)
                request.cls.svc_mgr.delete_repository(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_composition_design_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("asset_composition_design_session_class_fixture", "asset_composition_design_session_test_fixture")
class TestAssetCompositionDesignSession(object):
    """Tests for AssetCompositionDesignSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_compose_assets(self):
        """Tests can_compose_assets"""
        # From test_templates/repository.py::AssetCompositionDesignSession::can_compose_assets_template
        assert isinstance(self.session.can_compose_assets(), bool)

    def test_add_asset(self):
        """Tests add_asset"""
        if not is_never_authz(self.service_config):
            for asset_id in self.asset_ids:
                self.catalog.add_asset(asset_id, self.composition_ids[0])
            assert self.catalog.get_composition_assets(self.composition_ids[0]).available() == 4
            assert self.catalog.get_composition_assets(self.composition_ids[0]).next().display_name.text == 'Test Asset 0'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.add_asset(self.fake_id, self.fake_id)

    def test_move_asset_ahead(self):
        """Tests move_asset_ahead"""
        if not is_never_authz(self.service_config):
            for asset_id in self.asset_ids:
                self.catalog.add_asset(asset_id, self.composition_ids[1])
            self.catalog.move_asset_ahead(self.asset_ids[2], self.composition_ids[1], self.asset_ids[0])
            first_asset = self.catalog.get_composition_assets(self.composition_ids[1]).next()
            assert first_asset.ident == self.asset_ids[2]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.move_asset_ahead(self.fake_id, self.fake_id, self.fake_id)

    def test_move_asset_behind(self):
        """Tests move_asset_behind"""
        if not is_never_authz(self.service_config):
            for asset_id in self.asset_ids:
                self.catalog.add_asset(asset_id, self.composition_ids[2])
            self.catalog.move_asset_behind(self.asset_ids[0], self.composition_ids[2], self.asset_ids[3])
            last_asset = list(self.catalog.get_composition_assets(self.composition_ids[2]))[-1]
            assert last_asset.ident == self.asset_ids[0]
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.move_asset_behind(self.fake_id, self.fake_id, self.fake_id)

    def test_order_assets(self):
        """Tests order_assets"""
        if not is_never_authz(self.service_config):
            for asset_id in self.asset_ids:
                self.catalog.add_asset(asset_id, self.composition_ids[3])
            new_order = [self.asset_ids[2], self.asset_ids[3], self.asset_ids[1], self.asset_ids[0]]
            self.catalog.order_assets(new_order, self.composition_ids[3])
            asset_list = list(self.catalog.get_composition_assets(self.composition_ids[3]))
            for num in [0, 1, 2, 3]:
                assert new_order[num] == asset_list[num].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.order_assets([self.fake_id], self.fake_id)

    def test_remove_asset(self):
        """Tests remove_asset"""
        if not is_never_authz(self.service_config):
            for asset_id in self.asset_ids:
                self.catalog.add_asset(asset_id, self.composition_ids[4])
            self.catalog.remove_asset(self.asset_ids[1], self.composition_ids[4])
            assert self.catalog.get_composition_assets(self.composition_ids[4]).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.remove_asset(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_lookup_session_class_fixture(request):
    # From test_templates/repository.py::CompositionLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def composition_lookup_session_test_fixture(request):
    # From test_templates/repository.py::CompositionLookupSession::init_template
    request.cls.composition_list = list()
    request.cls.composition_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2, 3]:
            create_form = request.cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionLookupSession tests'
            if num > 1:
                create_form.sequestered = True
            obj = request.cls.catalog.create_composition(create_form)
            request.cls.composition_list.append(obj)
            request.cls.composition_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_composition_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_repositories():
                catalog.use_unsequestered_composition_view()
                for obj in catalog.get_compositions():
                    catalog.delete_composition(obj.ident)
                request.cls.svc_mgr.delete_repository(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("composition_lookup_session_class_fixture", "composition_lookup_session_test_fixture")
class TestCompositionLookupSession(object):
    """Tests for CompositionLookupSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_lookup_compositions(self):
        """Tests can_lookup_compositions"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_compositions(), bool)

    def test_use_comparative_composition_view(self):
        """Tests use_comparative_composition_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_composition_view()

    def test_use_plenary_composition_view(self):
        """Tests use_plenary_composition_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_composition_view()

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_repository_view()

    def test_use_active_composition_view(self):
        """Tests use_active_composition_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_active_composition_view_template
        # Ideally also verify the value is set...
        self.catalog.use_active_composition_view()

    def test_use_any_status_composition_view(self):
        """Tests use_any_status_composition_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_any_status_composition_view_template
        # Ideally also verify the value is set...
        self.catalog.use_any_status_composition_view()

    def test_use_sequestered_composition_view(self):
        """Tests use_sequestered_composition_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_sequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_sequestered_composition_view()

    def test_use_unsequestered_composition_view(self):
        """Tests use_unsequestered_composition_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_unsequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_unsequestered_composition_view()

    def test_get_composition(self):
        """Tests get_composition"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_composition_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_repository_view()
                obj = self.catalog.get_composition(self.composition_list[0].ident)
                assert obj.ident == self.composition_list[0].ident
                self.catalog.use_federated_repository_view()
                obj = self.catalog.get_composition(self.composition_list[0].ident)
                assert obj.ident == self.composition_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_composition(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_repository_view()
                obj = self.catalog.get_composition(self.composition_list[0].ident)
                assert obj.ident == self.composition_list[0].ident
                self.catalog.use_federated_repository_view()
                obj = self.catalog.get_composition(self.composition_list[0].ident)
                assert obj.ident == self.composition_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_composition(self.fake_id)

    def test_get_compositions_by_ids(self):
        """Tests get_compositions_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        if self.svc_mgr.supports_composition_query():
            objects = self.catalog.get_compositions_by_ids(self.composition_ids)
            assert isinstance(objects, CompositionList)
            self.catalog.use_federated_repository_view()
            objects = self.catalog.get_compositions_by_ids(self.composition_ids)
            assert isinstance(objects, CompositionList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_compositions_by_ids(self.composition_ids)
                assert isinstance(objects, CompositionList)
                self.catalog.use_federated_repository_view()
                objects = self.catalog.get_compositions_by_ids(self.composition_ids)
                assert objects.available() > 0
                assert isinstance(objects, CompositionList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_compositions_by_ids(self.composition_ids)

    def test_get_compositions_by_genus_type(self):
        """Tests get_compositions_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        if self.svc_mgr.supports_composition_query():
            objects = self.catalog.get_compositions_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, CompositionList)
            self.catalog.use_federated_repository_view()
            objects = self.catalog.get_compositions_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, CompositionList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_compositions_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, CompositionList)
                self.catalog.use_federated_repository_view()
                objects = self.catalog.get_compositions_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, CompositionList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_compositions_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_compositions_by_parent_genus_type(self):
        """Tests get_compositions_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        if self.svc_mgr.supports_composition_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_compositions_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, CompositionList)
                self.catalog.use_federated_repository_view()
                objects = self.catalog.get_compositions_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, CompositionList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_compositions_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_compositions_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, CompositionList)
                self.catalog.use_federated_repository_view()
                objects = self.catalog.get_compositions_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, CompositionList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_compositions_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_compositions_by_record_type(self):
        """Tests get_compositions_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        if self.svc_mgr.supports_composition_query():
            objects = self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, CompositionList)
            self.catalog.use_federated_repository_view()
            objects = self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, CompositionList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, CompositionList)
                self.catalog.use_federated_repository_view()
                objects = self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, CompositionList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)

    def test_get_compositions_by_provider(self):
        """Tests get_compositions_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_compositions_by_provider(True)

    def test_get_compositions(self):
        """Tests get_compositions"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        if self.svc_mgr.supports_composition_query():
            objects = self.catalog.get_compositions()
            assert isinstance(objects, CompositionList)
            self.catalog.use_federated_repository_view()
            objects = self.catalog.get_compositions()
            assert isinstance(objects, CompositionList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_compositions()
                assert isinstance(objects, CompositionList)
                self.catalog.use_federated_repository_view()
                objects = self.catalog.get_compositions()
                assert objects.available() > 0
                assert isinstance(objects, CompositionList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_compositions()

    def test_get_composition_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_composition(self.composition_ids[0], ALIAS_ID)
            obj = self.catalog.get_composition(ALIAS_ID)
            assert obj.get_id() == self.composition_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_query_session_class_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def composition_query_session_test_fixture(request):
    # From test_templates/resource.py::ResourceQuerySession::init_template
    request.cls.composition_list = list()
    request.cls.composition_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + color
            create_form.description = (
                'Test Composition for CompositionQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_composition(create_form)
            request.cls.composition_list.append(obj)
            request.cls.composition_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_composition_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_compositions():
                request.cls.catalog.delete_composition(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("composition_query_session_class_fixture", "composition_query_session_test_fixture")
class TestCompositionQuerySession(object):
    """Tests for CompositionQuerySession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_search_compositions(self):
        """Tests can_search_compositions"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_compositions(), bool)

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_repository_view()

    def test_use_sequestered_composition_view(self):
        """Tests use_sequestered_composition_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_sequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_sequestered_composition_view()

    def test_use_unsequestered_composition_view(self):
        """Tests use_unsequestered_composition_view"""
        # From test_templates/repository.py::CompositionLookupSession::use_unsequestered_composition_view
        # Ideally also verify the value is set...
        self.catalog.use_unsequestered_composition_view()

    def test_get_composition_query(self):
        """Tests get_composition_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_composition_query()
        assert isinstance(query, ABCQueries.CompositionQuery)

    def test_get_compositions_by_query(self):
        """Tests get_compositions_by_query"""
        if not is_never_authz(self.service_config):
            cfu = self.catalog.get_composition_form_for_update(self.composition_list[3].ident)
            cfu.set_sequestered(True)
            self.catalog.update_composition(cfu)
            query = self.catalog.get_composition_query()
            query.match_display_name('orange')
            assert self.catalog.get_compositions_by_query(query).available() == 1
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.catalog.get_compositions_by_query(query).available() == 2
            cfu = self.catalog.get_composition_form_for_update(self.composition_list[3].ident)
            cfu.set_sequestered(False)
            self.catalog.update_composition(cfu)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_compositions_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_search_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionSearchSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_search_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("composition_search_session_class_fixture", "composition_search_session_test_fixture")
class TestCompositionSearchSession(object):
    """Tests for CompositionSearchSession"""
    def test_get_composition_search(self):
        """Tests get_composition_search"""
        # From test_templates/resource.py::ResourceSearchSession::get_resource_search_template
        result = self.session.get_composition_search()
        assert isinstance(result, ABCSearches.CompositionSearch)

    def test_get_composition_search_order(self):
        """Tests get_composition_search_order"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_composition_search_order()

    def test_get_compositions_by_search(self):
        """Tests get_compositions_by_search"""
        # From test_templates/resource.py::ResourceSearchSession::get_resources_by_search_template
        query = self.catalog.get_composition_query()
        search = self.session.get_composition_search()
        results = self.session.get_compositions_by_search(query, search)
        assert isinstance(results, ABCSearches.CompositionSearchResults)

    def test_get_composition_query_from_inspector(self):
        """Tests get_composition_query_from_inspector"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_composition_query_from_inspector(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_admin_session_class_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.assessment_mgr = Runtime().get_service_manager(
        'ASSESSMENT',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_composition_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_compositions():
                request.cls.catalog.delete_composition(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_admin_session_test_fixture(request):
    # From test_templates/resource.py::ResourceAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_composition_form_for_create([])
        request.cls.form.display_name = 'new Composition'
        request.cls.form.description = 'description of Composition'
        request.cls.form.set_genus_type(NEW_TYPE)
        request.cls.osid_object = request.cls.catalog.create_composition(request.cls.form)
    request.cls.session = request.cls.catalog

    def test_tear_down():
        # From test_templates/resource.py::ResourceAdminSession::init_template
        if not is_never_authz(request.cls.service_config):
            request.cls.catalog.delete_composition(request.cls.osid_object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("composition_admin_session_class_fixture", "composition_admin_session_test_fixture")
class TestCompositionAdminSession(object):
    """Tests for CompositionAdminSession"""
    def test_get_repository_id(self):
        """Tests get_repository_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_repository_id() == self.catalog.ident

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_repository(), ABCRepository)

    def test_can_create_compositions(self):
        """Tests can_create_compositions"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_compositions(), bool)

    def test_can_create_composition_with_record_types(self):
        """Tests can_create_composition_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_composition_with_record_types(DEFAULT_TYPE), bool)

    def test_get_composition_form_for_create(self):
        """Tests get_composition_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_composition_form_for_create([])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_composition_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_composition_form_for_create([])

    def test_create_composition(self):
        """Tests create_composition"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.repository.objects import Composition
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Composition)
            assert self.osid_object.display_name.text == 'new Composition'
            assert self.osid_object.description.text == 'description of Composition'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_composition(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_composition('I Will Break You!')
            update_form = self.catalog.get_composition_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_composition(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_composition('foo')

    def test_can_update_compositions(self):
        """Tests can_update_compositions"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_compositions(), bool)

    def test_get_composition_form_for_update(self):
        """Tests get_composition_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_composition_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_composition_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_composition_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='repository.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_composition_form_for_update(self.fake_id)

    def test_update_composition(self):
        """Tests update_composition"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.repository.objects import Composition
            form = self.catalog.get_composition_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_composition(form)
            assert isinstance(updated_object, Composition)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_composition(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_composition('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_composition(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_composition('foo')

    def test_can_delete_compositions(self):
        """Tests can_delete_compositions"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_compositions(), bool)

    def test_delete_composition(self):
        """Tests delete_composition"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_composition_form_for_create([])
            form.display_name = 'new Composition'
            form.description = 'description of Composition'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_composition(form)
            self.catalog.delete_composition(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_composition(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_composition(self.fake_id)

    def test_delete_composition_node(self):
        """Tests delete_composition_node"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.delete_composition_node(True)

    def test_add_composition_child(self):
        """Tests add_composition_child"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.add_composition_child(True, True)

    def test_remove_composition_child(self):
        """Tests remove_composition_child"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.remove_composition_child(True, True)

    def test_can_manage_composition_aliases(self):
        """Tests can_manage_composition_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_composition_aliases(), bool)

    def test_alias_composition(self):
        """Tests alias_composition"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_composition(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_composition(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_composition(self.fake_id, self.fake_id)

    def test_composition_assignment(self):
        if not is_never_authz(self.service_config):
            composition_list = list()
            composition_ids = list()
            for num in [0, 1, 2, 3]:
                create_form = self.catalog.get_composition_form_for_create([])
                create_form.display_name = 'Test Composition ' + str(num)
                create_form.description = 'Test Composition for CompositionLookupSession tests'
                obj = self.catalog.create_composition(create_form)
                composition_list.append(obj)
                composition_ids.append(obj.ident)
            update_form = self.catalog.get_composition_form_for_update(composition_ids[0])
            update_form.set_children(composition_ids[1:])
            self.catalog.update_composition(update_form)
            composition = self.catalog.get_composition(composition_ids[0])
            assert composition.get_children_ids().available() == 3
            assert composition.get_child_ids().available() == 3
            assert composition.get_children().available() == 3


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_repository_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.composition_list = list()
    request.cls.composition_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionRepositorySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository for Assignment'
        create_form.description = 'Test Repository for CompositionRepositorySession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionRepositorySession tests'
            obj = request.cls.catalog.create_composition(create_form)
            request.cls.composition_list.append(obj)
            request.cls.composition_ids.append(obj.ident)
        request.cls.svc_mgr.assign_composition_to_repository(
            request.cls.composition_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_composition_to_repository(
            request.cls.composition_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_composition_from_repository(
                request.cls.composition_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_composition_from_repository(
                request.cls.composition_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_compositions():
                request.cls.catalog.delete_composition(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_repository_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("composition_repository_session_class_fixture", "composition_repository_session_test_fixture")
class TestCompositionRepositorySession(object):
    """Tests for CompositionRepositorySession"""
    def test_use_comparative_composition_repository_view(self):
        """Tests use_comparative_composition_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_composition_repository_view()

    def test_use_plenary_composition_repository_view(self):
        """Tests use_plenary_composition_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_composition_repository_view()

    def test_can_lookup_composition_repository_mappings(self):
        """Tests can_lookup_composition_repository_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_composition_repository_mappings()
        assert isinstance(result, bool)

    def test_get_composition_ids_by_repository(self):
        """Tests get_composition_ids_by_repository"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_composition_ids_by_repository(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_composition_ids_by_repository(self.fake_id)

    def test_get_compositions_by_repository(self):
        """Tests get_compositions_by_repository"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_compositions_by_repository(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.CompositionList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_compositions_by_repository(self.fake_id)

    def test_get_composition_ids_by_repositories(self):
        """Tests get_composition_ids_by_repositories"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_composition_ids_by_repositories(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_composition_ids_by_repositories([self.fake_id])

    def test_get_compositions_by_repositories(self):
        """Tests get_compositions_by_repositories"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_compositions_by_repositories(catalog_ids)
            assert isinstance(results, ABCObjects.CompositionList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_compositions_by_repositories([self.fake_id])

    def test_get_repository_ids_by_composition(self):
        """Tests get_repository_ids_by_composition"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_repository_ids_by_composition(self.composition_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_ids_by_composition(self.fake_id)

    def test_get_repositories_by_composition(self):
        """Tests get_repositories_by_composition"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_repositories_by_composition(self.composition_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repositories_by_composition(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_repository_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.composition_list = list()
    request.cls.composition_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionRepositoryAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository for Assignment'
        create_form.description = 'Test Repository for CompositionRepositoryAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionRepositoryAssignmentSession tests'
            obj = request.cls.catalog.create_composition(create_form)
            request.cls.composition_list.append(obj)
            request.cls.composition_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_compositions():
                request.cls.catalog.delete_composition(obj.ident)
            request.cls.svc_mgr.delete_repository(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_repository_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("composition_repository_assignment_session_class_fixture", "composition_repository_assignment_session_test_fixture")
class TestCompositionRepositoryAssignmentSession(object):
    """Tests for CompositionRepositoryAssignmentSession"""
    def test_can_assign_compositions(self):
        """Tests can_assign_compositions"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_compositions()
        assert isinstance(result, bool)

    def test_can_assign_compositions_to_repository(self):
        """Tests can_assign_compositions_to_repository"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_compositions_to_repository(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_repository_ids(self):
        """Tests get_assignable_repository_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_repository_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_repository_ids(self.fake_id)

    def test_get_assignable_repository_ids_for_composition(self):
        """Tests get_assignable_repository_ids_for_composition"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_repository_ids_for_composition(self.catalog.ident, self.composition_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_repository_ids_for_composition(self.fake_id, self.fake_id)

    def test_assign_composition_to_repository(self):
        """Tests assign_composition_to_repository"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_compositions()
            assert results.available() == 0
            self.session.assign_composition_to_repository(self.composition_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_compositions()
            assert results.available() == 1
            self.session.unassign_composition_from_repository(
                self.composition_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_composition_to_repository(self.fake_id, self.fake_id)

    def test_unassign_composition_from_repository(self):
        """Tests unassign_composition_from_repository"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_compositions()
            assert results.available() == 0
            self.session.assign_composition_to_repository(
                self.composition_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_compositions()
            assert results.available() == 1
            self.session.unassign_composition_from_repository(
                self.composition_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_compositions()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_composition_from_repository(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test Repository ' + str(num)
            create_form.description = 'Test Repository for repository proxy manager tests'
            catalog = request.cls.svc_mgr.create_repository(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_repositories():
                request.cls.svc_mgr.delete_repository(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("repository_lookup_session_class_fixture", "repository_lookup_session_test_fixture")
class TestRepositoryLookupSession(object):
    """Tests for RepositoryLookupSession"""
    def test_can_lookup_repositories(self):
        """Tests can_lookup_repositories"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_repositories(), bool)

    def test_use_comparative_repository_view(self):
        """Tests use_comparative_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_repository_view()

    def test_use_plenary_repository_view(self):
        """Tests use_plenary_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_repository_view()

    def test_get_repository(self):
        """Tests get_repository"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_repository(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository(self.fake_id)

    def test_get_repositories_by_ids(self):
        """Tests get_repositories_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_repositories_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.RepositoryList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repositories_by_ids([self.fake_id])

    def test_get_repositories_by_genus_type(self):
        """Tests get_repositories_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_repositories_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.RepositoryList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repositories_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_repositories_by_parent_genus_type(self):
        """Tests get_repositories_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_repositories_by_parent_genus_type(True)

    def test_get_repositories_by_record_type(self):
        """Tests get_repositories_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_repositories_by_record_type(True)

    def test_get_repositories_by_provider(self):
        """Tests get_repositories_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_repositories_by_provider(True)

    def test_get_repositories(self):
        """Tests get_repositories"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_repositories()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.RepositoryList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repositories()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_query_session_class_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_query_session_test_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("repository_query_session_class_fixture", "repository_query_session_test_fixture")
class TestRepositoryQuerySession(object):
    """Tests for RepositoryQuerySession"""
    def test_can_search_repositories(self):
        """Tests can_search_repositories"""
        # From test_templates/resource.py::BinQuerySession::can_search_bins_template
        assert isinstance(self.session.can_search_repositories(), bool)

    def test_get_repository_query(self):
        """Tests get_repository_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_repository_query()
            assert isinstance(query, ABCQueries.RepositoryQuery)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_repository_query()

    def test_get_repositories_by_query(self):
        """Tests get_repositories_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_repository_query()
            query.match_display_name('Test catalog')
            assert self.session.get_repositories_by_query(query).available() == 1
            query.clear_display_name_terms()
            query.match_display_name('Test catalog', match=False)
            assert self.session.get_repositories_by_query(query).available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_repositories_by_query('foo')


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def repository_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_repository(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository For Deletion'
        create_form.description = 'Test Repository for RepositoryAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_repository(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_repositories():
                request.cls.svc_mgr.delete_repository(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("repository_admin_session_class_fixture", "repository_admin_session_test_fixture")
class TestRepositoryAdminSession(object):
    """Tests for RepositoryAdminSession"""
    def test_can_create_repositories(self):
        """Tests can_create_repositories"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_repositories(), bool)

    def test_can_create_repository_with_record_types(self):
        """Tests can_create_repository_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_repository_with_record_types(DEFAULT_TYPE), bool)

    def test_get_repository_form_for_create(self):
        """Tests get_repository_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.repository.objects import RepositoryForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_repository_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_repository_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_form_for_create([])

    def test_create_repository(self):
        """Tests create_repository"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.repository.objects import Repository
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_repository_form_for_create([])
            catalog_form.display_name = 'Test Repository'
            catalog_form.description = 'Test Repository for RepositoryAdminSession.create_repository tests'
            new_catalog = self.svc_mgr.create_repository(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_repository(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_repository('I Will Break You!')
            update_form = self.svc_mgr.get_repository_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_repository(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_repository('foo')

    def test_can_update_repositories(self):
        """Tests can_update_repositories"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_repositories(), bool)

    def test_get_repository_form_for_update(self):
        """Tests get_repository_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.repository.objects import RepositoryForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_repository_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_form_for_update(self.fake_id)

    def test_update_repository(self):
        """Tests update_repository"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_repository_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_repository(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_repository('foo')

    def test_can_delete_repositories(self):
        """Tests can_delete_repositories"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_repositories(), bool)

    def test_delete_repository(self):
        """Tests delete_repository"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_repository(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_repository(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_repository(self.fake_id)

    def test_can_manage_repository_aliases(self):
        """Tests can_manage_repository_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_repository_aliases(), bool)

    def test_alias_repository(self):
        """Tests alias_repository"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('repository.Repository%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_repository(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_repository(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_repository(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Repository ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_repository(create_form)
        request.cls.svc_mgr.add_root_repository(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_repository(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_repository(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_repository(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_repository(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_repositories(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_repository(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_repository(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("repository_hierarchy_session_class_fixture", "repository_hierarchy_session_test_fixture")
class TestRepositoryHierarchySession(object):
    """Tests for RepositoryHierarchySession"""
    def test_get_repository_hierarchy_id(self):
        """Tests get_repository_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_repository_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_repository_hierarchy(self):
        """Tests get_repository_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_repository_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_hierarchy()

    def test_can_access_repository_hierarchy(self):
        """Tests can_access_repository_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_repository_hierarchy(), bool)

    def test_use_comparative_repository_view(self):
        """Tests use_comparative_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_repository_view()

    def test_use_plenary_repository_view(self):
        """Tests use_plenary_repository_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_repository_view()

    def test_get_root_repository_ids(self):
        """Tests get_root_repository_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_repository_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_repository_ids()

    def test_get_root_repositories(self):
        """Tests get_root_repositories"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.repository.objects import RepositoryList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_repositories()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_repositories()

    def test_has_parent_repositories(self):
        """Tests has_parent_repositories"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_repositories(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_repositories(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_repositories(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_repositories(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_repositories(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_repositories(self.fake_id)

    def test_is_parent_of_repository(self):
        """Tests is_parent_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_repository(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_repository(self.fake_id, self.fake_id)

    def test_get_parent_repository_ids(self):
        """Tests get_parent_repository_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_repository_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_repository_ids(self.fake_id)

    def test_get_parent_repositories(self):
        """Tests get_parent_repositories"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_repositories(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_repositories(self.fake_id)

    def test_is_ancestor_of_repository(self):
        """Tests is_ancestor_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_repository,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_repository(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_repositories(self):
        """Tests has_child_repositories"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_repositories(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_repositories(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_repositories(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_repositories(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_repositories(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_repositories(self.fake_id)

    def test_is_child_of_repository(self):
        """Tests is_child_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_repository(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_repository(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_repository(self.fake_id, self.fake_id)

    def test_get_child_repository_ids(self):
        """Tests get_child_repository_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_repository_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_repository_ids(self.fake_id)

    def test_get_child_repositories(self):
        """Tests get_child_repositories"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_repositories(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_repositories(self.fake_id)

    def test_is_descendant_of_repository(self):
        """Tests is_descendant_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_repository,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_repository(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_repository_node_ids(self):
        """Tests get_repository_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_repository_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_node_ids(self.fake_id, 1, 2, False)

    def test_get_repository_nodes(self):
        """Tests get_repository_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_repository_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'REPOSITORY',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Repository ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_repository(create_form)
        request.cls.svc_mgr.add_root_repository(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_repository(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_repository(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_repository(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_repository(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_repositories(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_repository(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def repository_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("repository_hierarchy_design_session_class_fixture", "repository_hierarchy_design_session_test_fixture")
class TestRepositoryHierarchyDesignSession(object):
    """Tests for RepositoryHierarchyDesignSession"""
    def test_get_repository_hierarchy_id(self):
        """Tests get_repository_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_repository_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_repository_hierarchy(self):
        """Tests get_repository_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_repository_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_repository_hierarchy()

    def test_can_modify_repository_hierarchy(self):
        """Tests can_modify_repository_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_repository_hierarchy(), bool)

    def test_add_root_repository(self):
        """Tests add_root_repository"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_repositories()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_repository(self.fake_id)

    def test_remove_root_repository(self):
        """Tests remove_root_repository"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_repositories()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Repository root'
            new_repository = self.svc_mgr.create_repository(create_form)
            self.svc_mgr.add_root_repository(new_repository.ident)

            roots = self.session.get_root_repositories()
            assert roots.available() == 2

            self.session.remove_root_repository(new_repository.ident)

            roots = self.session.get_root_repositories()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_repository(self.fake_id)

    def test_add_child_repository(self):
        """Tests add_child_repository"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_repositories(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_repository(self.fake_id, self.fake_id)

    def test_remove_child_repository(self):
        """Tests remove_child_repository"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_repositories(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Repository child'
            new_repository = self.svc_mgr.create_repository(create_form)
            self.svc_mgr.add_child_repository(
                self.catalogs['Root'].ident,
                new_repository.ident)

            children = self.session.get_child_repositories(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_repository(
                self.catalogs['Root'].ident,
                new_repository.ident)

            children = self.session.get_child_repositories(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_repository(self.fake_id, self.fake_id)

    def test_remove_child_repositories(self):
        """Tests remove_child_repositories"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_repositories(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Repository child'
            new_repository = self.svc_mgr.create_repository(create_form)
            self.svc_mgr.add_child_repository(
                self.catalogs['Grandchild 1'].ident,
                new_repository.ident)

            children = self.session.get_child_repositories(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_repositories(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_repositories(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_repositories(self.fake_id)
