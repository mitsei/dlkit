"""Unit tests of cataloging objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
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
def catalog_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_catalog_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_catalog(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_catalog(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("catalog_class_fixture", "catalog_test_fixture")
class TestCatalog(object):
    """Tests for Catalog"""
    def test_get_catalog_record(self):
        """Tests get_catalog_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_catalog_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_catalog_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("catalog_form_class_fixture", "catalog_form_test_fixture")
class TestCatalogForm(object):
    """Tests for CatalogForm"""
    def test_get_catalog_form_record(self):
        """Tests get_catalog_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_catalog_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog'
        create_form.description = 'Test Catalog for CatalogList tests'
        request.cls.catalog = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.catalog_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog_ids:
                request.cls.svc_mgr.delete_catalog(obj)
            request.cls.svc_mgr.delete_catalog(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.cataloging.objects import CatalogList
    request.cls.catalog_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'Test Catalog ' + str(num)
            create_form.description = 'Test Catalog for CatalogList tests'
            obj = request.cls.svc_mgr.create_catalog(create_form)
            request.cls.catalog_list.append(obj)
            request.cls.catalog_ids.append(obj.ident)
    request.cls.catalog_list = CatalogList(request.cls.catalog_list)


@pytest.mark.usefixtures("catalog_list_class_fixture", "catalog_list_test_fixture")
class TestCatalogList(object):
    """Tests for CatalogList"""
    def test_get_next_catalog(self):
        """Tests get_next_catalog"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.cataloging.objects import Catalog
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog_list.get_next_catalog(), Catalog)

    def test_get_next_catalogs(self):
        """Tests get_next_catalogs"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.cataloging.objects import CatalogList, Catalog
        if not is_never_authz(self.service_config):
            new_list = self.catalog_list.get_next_catalogs(2)
            assert isinstance(new_list, CatalogList)
            for item in new_list:
                assert isinstance(item, Catalog)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog'
        create_form.description = 'Test Catalog for CatalogNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.catalog_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_catalog(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def catalog_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.cataloging.objects import CatalogNode
    request.cls.catalog_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'Test Catalog ' + str(num)
            create_form.description = 'Test Catalog for CatalogNode tests'
            obj = request.cls.svc_mgr.create_catalog(create_form)
            request.cls.catalog_list.append(CatalogNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.catalog_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_catalog(request.cls.catalog_list[0].ident)
        request.cls.svc_mgr.add_child_catalog(
            request.cls.catalog_list[0].ident,
            request.cls.catalog_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_catalog_nodes(
            request.cls.catalog_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_catalog(
                request.cls.catalog_list[0].ident,
                request.cls.catalog_list[1].ident)
            request.cls.svc_mgr.remove_root_catalog(request.cls.catalog_list[0].ident)
            for node in request.cls.catalog_list:
                request.cls.svc_mgr.delete_catalog(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("catalog_node_class_fixture", "catalog_node_test_fixture")
class TestCatalogNode(object):
    """Tests for CatalogNode"""
    def test_get_catalog(self):
        """Tests get_catalog"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.cataloging.objects import Catalog
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog_list[0].get_catalog(), OsidCatalog)
            assert str(self.catalog_list[0].get_catalog().ident) == str(self.catalog_list[0].ident)

    def test_get_parent_catalog_nodes(self):
        """Tests get_parent_catalog_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.cataloging.objects import CatalogNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_catalog_nodes(
                self.catalog_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_catalog_nodes(), CatalogNodeList)
            assert node.get_parent_catalog_nodes().available() == 1
            assert str(node.get_parent_catalog_nodes().next().ident) == str(self.catalog_list[0].ident)

    def test_get_child_catalog_nodes(self):
        """Tests get_child_catalog_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.cataloging.objects import CatalogNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_catalog_nodes(
                self.catalog_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_catalog_nodes(), CatalogNodeList)
            assert node.get_child_catalog_nodes().available() == 1
            assert str(node.get_child_catalog_nodes().next().ident) == str(self.catalog_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'CATALOGING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
        create_form.display_name = 'Test Catalog'
        create_form.description = 'Test Catalog for CatalogNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_catalog(create_form)
        request.cls.catalog_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog_node_ids:
                request.cls.svc_mgr.delete_catalog(obj)
            request.cls.svc_mgr.delete_catalog(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def catalog_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.cataloging.objects import CatalogNodeList, CatalogNode
    request.cls.catalog_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_catalog_form_for_create([])
            create_form.display_name = 'Test CatalogNode ' + str(num)
            create_form.description = 'Test CatalogNode for CatalogNodeList tests'
            obj = request.cls.svc_mgr.create_catalog(create_form)
            request.cls.catalog_node_list.append(CatalogNode(obj.object_map))
            request.cls.catalog_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_catalog(request.cls.catalog_node_list[0].ident)
        request.cls.svc_mgr.add_child_catalog(
            request.cls.catalog_node_list[0].ident,
            request.cls.catalog_node_list[1].ident)
    request.cls.catalog_node_list = CatalogNodeList(request.cls.catalog_node_list)


@pytest.mark.usefixtures("catalog_node_list_class_fixture", "catalog_node_list_test_fixture")
class TestCatalogNodeList(object):
    """Tests for CatalogNodeList"""
    def test_get_next_catalog_node(self):
        """Tests get_next_catalog_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.cataloging.objects import CatalogNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog_node_list.get_next_catalog_node(), CatalogNode)

    def test_get_next_catalog_nodes(self):
        """Tests get_next_catalog_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.cataloging.objects import CatalogNodeList, CatalogNode
        if not is_never_authz(self.service_config):
            new_list = self.catalog_node_list.get_next_catalog_nodes(2)
            assert isinstance(new_list, CatalogNodeList)
            for item in new_list:
                assert isinstance(item, CatalogNode)
