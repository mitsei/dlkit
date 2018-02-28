"""Unit tests of cataloging sessions."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.cataloging import objects as ABCObjects
from dlkit.abstract_osid.cataloging import queries as ABCQueries
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
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
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'Test Catalog ' + str(num)
            create_form.description = 'Test Catalog for cataloging proxy manager tests'
            catalog = request.cls.svc_mgr.create_catalog(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_catalogs():
                request.cls.svc_mgr.delete_catalog(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("catalog_lookup_session_class_fixture", "catalog_lookup_session_test_fixture")
class TestCatalogLookupSession(object):
    """Tests for CatalogLookupSession"""
    def test_can_lookup_catalogs(self):
        """Tests can_lookup_catalogs"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_catalogs(), bool)

    def test_use_comparative_catalog_view(self):
        """Tests use_comparative_catalog_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_catalog_view()

    def test_use_plenary_catalog_view(self):
        """Tests use_plenary_catalog_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_catalog_view()

    def test_get_catalog(self):
        """Tests get_catalog"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_catalog(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog(self.fake_id)

    def test_get_catalogs_by_ids(self):
        """Tests get_catalogs_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_catalogs_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.CatalogList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalogs_by_ids([self.fake_id])

    def test_get_catalogs_by_genus_type(self):
        """Tests get_catalogs_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_catalogs_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.CatalogList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalogs_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_catalogs_by_parent_genus_type(self):
        """Tests get_catalogs_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_catalogs_by_parent_genus_type(True)

    def test_get_catalogs_by_record_type(self):
        """Tests get_catalogs_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_catalogs_by_record_type(True)

    def test_get_catalogs_by_provider(self):
        """Tests get_catalogs_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_catalogs_by_provider(True)

    def test_get_catalogs(self):
        """Tests get_catalogs"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_catalogs()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.CatalogList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalogs()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_query_session_class_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_catalog(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_query_session_test_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("catalog_query_session_class_fixture", "catalog_query_session_test_fixture")
class TestCatalogQuerySession(object):
    """Tests for CatalogQuerySession"""
    def test_can_search_catalogs(self):
        """Tests can_search_catalogs"""
        # From test_templates/resource.py::BinQuerySession::can_search_bins_template
        assert isinstance(self.session.can_search_catalogs(), bool)

    def test_get_catalog_query(self):
        """Tests get_catalog_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_catalog_query()
            assert isinstance(query, ABCQueries.CatalogQuery)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_catalog_query()

    def test_get_catalogs_by_query(self):
        """Tests get_catalogs_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_catalog_query()
            query.match_display_name('Test catalog')
            assert self.session.get_catalogs_by_query(query).available() == 1
            query.clear_display_name_terms()
            query.match_display_name('Test catalog', match=False)
            assert self.session.get_catalogs_by_query(query).available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_catalogs_by_query('foo')


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def catalog_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog'
        create_form.description = 'Test Catalog for CatalogAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_catalog(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog For Deletion'
        create_form.description = 'Test Catalog for CatalogAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_catalog(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_catalogs():
                request.cls.svc_mgr.delete_catalog(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("catalog_admin_session_class_fixture", "catalog_admin_session_test_fixture")
class TestCatalogAdminSession(object):
    """Tests for CatalogAdminSession"""
    def test_can_create_catalogs(self):
        """Tests can_create_catalogs"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_catalogs(), bool)

    def test_can_create_catalog_with_record_types(self):
        """Tests can_create_catalog_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_catalog_with_record_types(DEFAULT_TYPE), bool)

    def test_get_catalog_form_for_create(self):
        """Tests get_catalog_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.cataloging.objects import CatalogForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_catalog_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_catalog_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog_form_for_create([])

    def test_create_catalog(self):
        """Tests create_catalog"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.cataloging.objects import Catalog
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_catalog_form_for_create([])
            catalog_form.display_name = 'Test Catalog'
            catalog_form.description = 'Test Catalog for CatalogAdminSession.create_catalog tests'
            new_catalog = self.svc_mgr.create_catalog(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_catalog(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_catalog('I Will Break You!')
            update_form = self.svc_mgr.get_catalog_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_catalog(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_catalog('foo')

    def test_can_update_catalogs(self):
        """Tests can_update_catalogs"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_catalogs(), bool)

    def test_get_catalog_form_for_update(self):
        """Tests get_catalog_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.cataloging.objects import CatalogForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_catalog_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog_form_for_update(self.fake_id)

    def test_update_catalog(self):
        """Tests update_catalog"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_catalog_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_catalog(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_catalog('foo')

    def test_can_delete_catalogs(self):
        """Tests can_delete_catalogs"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_catalogs(), bool)

    def test_delete_catalog(self):
        """Tests delete_catalog"""
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_catalog(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_catalog(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_catalog(self.fake_id)

    def test_can_manage_catalog_aliases(self):
        """Tests can_manage_catalog_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_catalog_aliases(), bool)

    def test_alias_catalog(self):
        """Tests alias_catalog"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('cataloging.Catalog%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_catalog(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_catalog(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_catalog(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Catalog ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.svc_mgr.add_root_catalog(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_catalog(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_catalog(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_catalog(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_catalog(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_catalogs(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_catalog(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_catalog(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("catalog_hierarchy_session_class_fixture", "catalog_hierarchy_session_test_fixture")
class TestCatalogHierarchySession(object):
    """Tests for CatalogHierarchySession"""
    def test_get_catalog_hierarchy_id(self):
        """Tests get_catalog_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_catalog_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_catalog_hierarchy(self):
        """Tests get_catalog_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_catalog_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog_hierarchy()

    def test_can_access_catalog_hierarchy(self):
        """Tests can_access_catalog_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_catalog_hierarchy(), bool)

    def test_use_comparative_catalog_view(self):
        """Tests use_comparative_catalog_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_catalog_view()

    def test_use_plenary_catalog_view(self):
        """Tests use_plenary_catalog_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_catalog_view()

    def test_get_root_catalog_ids(self):
        """Tests get_root_catalog_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_catalog_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_catalog_ids()

    def test_get_root_catalogs(self):
        """Tests get_root_catalogs"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.cataloging.objects import CatalogList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_catalogs()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_catalogs()

    def test_has_parent_catalogs(self):
        """Tests has_parent_catalogs"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_catalogs(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_catalogs(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_catalogs(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_catalogs(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_catalogs(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_catalogs(self.fake_id)

    def test_is_parent_of_catalog(self):
        """Tests is_parent_of_catalog"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_catalog(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_catalog(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_catalog(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_catalog(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_catalog(self.fake_id, self.fake_id)

    def test_get_parent_catalog_ids(self):
        """Tests get_parent_catalog_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_catalog_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_catalog_ids(self.fake_id)

    def test_get_parent_catalogs(self):
        """Tests get_parent_catalogs"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_catalogs(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_catalogs(self.fake_id)

    def test_is_ancestor_of_catalog(self):
        """Tests is_ancestor_of_catalog"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_catalog,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_catalog(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_catalog(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_catalog(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_catalog(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_catalog(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_catalogs(self):
        """Tests has_child_catalogs"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_catalogs(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_catalogs(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_catalogs(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_catalogs(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_catalogs(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_catalogs(self.fake_id)

    def test_is_child_of_catalog(self):
        """Tests is_child_of_catalog"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_catalog(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_catalog(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_catalog(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_catalog(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_catalog(self.fake_id, self.fake_id)

    def test_get_child_catalog_ids(self):
        """Tests get_child_catalog_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_catalog_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_catalog_ids(self.fake_id)

    def test_get_child_catalogs(self):
        """Tests get_child_catalogs"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_catalogs(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_catalogs(self.fake_id)

    def test_is_descendant_of_catalog(self):
        """Tests is_descendant_of_catalog"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_catalog,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_catalog(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_catalog(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_catalog(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_catalog(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_catalog(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_catalog_node_ids(self):
        """Tests get_catalog_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_catalog_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog_node_ids(self.fake_id, 1, 2, False)

    def test_get_catalog_nodes(self):
        """Tests get_catalog_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_catalog_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Catalog ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.svc_mgr.add_root_catalog(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_catalog(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_catalog(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_catalog(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_catalog(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_catalogs(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_catalog(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("catalog_hierarchy_design_session_class_fixture", "catalog_hierarchy_design_session_test_fixture")
class TestCatalogHierarchyDesignSession(object):
    """Tests for CatalogHierarchyDesignSession"""
    def test_get_catalog_hierarchy_id(self):
        """Tests get_catalog_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_catalog_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_catalog_hierarchy(self):
        """Tests get_catalog_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_catalog_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_catalog_hierarchy()

    def test_can_modify_catalog_hierarchy(self):
        """Tests can_modify_catalog_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_catalog_hierarchy(), bool)

    def test_add_root_catalog(self):
        """Tests add_root_catalog"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_catalogs()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_catalog(self.fake_id)

    def test_remove_root_catalog(self):
        """Tests remove_root_catalog"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_catalogs()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Catalog root'
            new_catalog = self.svc_mgr.create_catalog(create_form)
            self.svc_mgr.add_root_catalog(new_catalog.ident)

            roots = self.session.get_root_catalogs()
            assert roots.available() == 2

            self.session.remove_root_catalog(new_catalog.ident)

            roots = self.session.get_root_catalogs()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_catalog(self.fake_id)

    def test_add_child_catalog(self):
        """Tests add_child_catalog"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_catalogs(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_catalog(self.fake_id, self.fake_id)

    def test_remove_child_catalog(self):
        """Tests remove_child_catalog"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_catalogs(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Catalog child'
            new_catalog = self.svc_mgr.create_catalog(create_form)
            self.svc_mgr.add_child_catalog(
                self.catalogs['Root'].ident,
                new_catalog.ident)

            children = self.session.get_child_catalogs(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_catalog(
                self.catalogs['Root'].ident,
                new_catalog.ident)

            children = self.session.get_child_catalogs(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_catalog(self.fake_id, self.fake_id)

    def test_remove_child_catalogs(self):
        """Tests remove_child_catalogs"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_catalogs(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Catalog child'
            new_catalog = self.svc_mgr.create_catalog(create_form)
            self.svc_mgr.add_child_catalog(
                self.catalogs['Grandchild 1'].ident,
                new_catalog.ident)

            children = self.session.get_child_catalogs(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_catalogs(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_catalogs(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_catalogs(self.fake_id)
