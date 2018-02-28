"""Unit tests of resource objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.osid.metadata import Metadata
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
def resource_class_fixture(request):
    # From test_templates/resource.py::Resource::init_template
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

        form = request.cls.catalog.get_resource_form_for_create([])
        form.display_name = 'Test object'
        request.cls.object = request.cls.catalog.create_resource(form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_test_fixture(request):
    pass


@pytest.mark.usefixtures("resource_class_fixture", "resource_test_fixture")
class TestResource(object):
    """Tests for Resource"""
    def test_is_group(self):
        """Tests is_group"""
        # From test_templates/resources.py::Resource::is_group_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_group(), bool)

    def test_is_demographic(self):
        """Tests is_demographic"""
        if not is_never_authz(self.service_config):
            with pytest.raises(AttributeError):
                self.object.is_demographic()

    def test_has_avatar(self):
        """Tests has_avatar"""
        # From test_templates/resources.py::Resource::has_avatar_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_avatar(), bool)

    def test_get_avatar_id(self):
        """Tests get_avatar_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_avatar_id)

    def test_get_avatar(self):
        """Tests get_avatar"""
        # From test_templates/resources.py::Resource::get_avatar_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.IllegalState,
                          self.object.get_avatar)

    def test_get_resource_record(self):
        """Tests get_resource_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_resource_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_form_class_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
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

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def resource_form_test_fixture(request):
    # From test_templates/resource.py::ResourceForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.form = request.cls.catalog.get_resource_form_for_create([])


@pytest.mark.usefixtures("resource_form_class_fixture", "resource_form_test_fixture")
class TestResourceForm(object):
    """Tests for ResourceForm"""
    def test_get_group_metadata(self):
        """Tests get_group_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_group_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'BOOLEAN'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_group(self):
        """Tests set_group"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_group(True)
        assert self.form._my_map['group']
        with pytest.raises(errors.InvalidArgument):
            self.form.set_group('false')

    def test_clear_group(self):
        """Tests clear_group"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_group(True)
        assert self.form._my_map['group']
        self.form.clear_group()
        assert self.form._my_map['group'] is None

    def test_get_avatar_metadata(self):
        """Tests get_avatar_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_avatar_metadata()
        assert isinstance(mdata, Metadata)
        assert isinstance(mdata.get_element_id(), ABC_Id)
        assert isinstance(mdata.get_element_label(), ABC_DisplayText)
        assert isinstance(mdata.get_instructions(), ABC_DisplayText)
        assert mdata.get_syntax() == 'ID'
        assert not mdata.is_array()
        assert isinstance(mdata.is_required(), bool)
        assert isinstance(mdata.is_read_only(), bool)
        assert isinstance(mdata.is_linked(), bool)

    def test_set_avatar(self):
        """Tests set_avatar"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        assert self.form._my_map['avatarId'] == ''
        self.form.set_avatar(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['avatarId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        with pytest.raises(errors.InvalidArgument):
            self.form.set_avatar(True)

    def test_clear_avatar(self):
        """Tests clear_avatar"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_avatar(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        assert self.form._my_map['avatarId'] == 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.form.clear_avatar()
        assert self.form._my_map['avatarId'] == self.form.get_avatar_metadata().get_default_id_values()[0]

    def test_get_resource_form_record(self):
        """Tests get_resource_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_resource_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def resource_list_class_fixture(request):
    # Implemented from init template for ResourceList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_resources():
                request.cls.catalog.delete_resource(obj.ident)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def resource_list_test_fixture(request):
    # Implemented from init template for ResourceList
    from dlkit.json_.resource.objects import ResourceList
    request.cls.resource_list = list()
    request.cls.resource_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceList tests'
            obj = request.cls.catalog.create_resource(create_form)
            request.cls.resource_list.append(obj)
            request.cls.resource_ids.append(obj.ident)
    request.cls.resource_list = ResourceList(request.cls.resource_list)
    request.cls.object = request.cls.resource_list


@pytest.mark.usefixtures("resource_list_class_fixture", "resource_list_test_fixture")
class TestResourceList(object):
    """Tests for ResourceList"""
    def test_get_next_resource(self):
        """Tests get_next_resource"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.resource.objects import Resource
        if not is_never_authz(self.service_config):
            assert isinstance(self.resource_list.get_next_resource(), Resource)

    def test_get_next_resources(self):
        """Tests get_next_resources"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.resource.objects import ResourceList, Resource
        if not is_never_authz(self.service_config):
            new_list = self.resource_list.get_next_resources(2)
            assert isinstance(new_list, ResourceList)
            for item in new_list:
                assert isinstance(item, Resource)


@pytest.mark.usefixtures("resource_node_class_fixture", "resource_node_test_fixture")
class TestResourceNode(object):
    """Tests for ResourceNode"""
    @pytest.mark.skip('unimplemented test')
    def test_get_resource(self):
        """Tests get_resource"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_parent_resource_nodes(self):
        """Tests get_parent_resource_nodes"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_child_resource_nodes(self):
        """Tests get_child_resource_nodes"""
        pass


@pytest.mark.usefixtures("resource_node_list_class_fixture", "resource_node_list_test_fixture")
class TestResourceNodeList(object):
    """Tests for ResourceNodeList"""
    @pytest.mark.skip('unimplemented test')
    def test_get_next_resource_node(self):
        """Tests get_next_resource_node"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_next_resource_nodes(self):
        """Tests get_next_resource_nodes"""
        pass


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_bin_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_bin(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bin_class_fixture", "bin_test_fixture")
class TestBin(object):
    """Tests for Bin"""
    def test_get_bin_record(self):
        """Tests get_bin_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_bin_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_bin_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bin_form_class_fixture", "bin_form_test_fixture")
class TestBinForm(object):
    """Tests for BinForm"""
    def test_get_bin_form_record(self):
        """Tests get_bin_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_bin_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.bin_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.bin_ids:
                request.cls.svc_mgr.delete_bin(obj)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.resource.objects import BinList
    request.cls.bin_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for BinList tests'
            obj = request.cls.svc_mgr.create_bin(create_form)
            request.cls.bin_list.append(obj)
            request.cls.bin_ids.append(obj.ident)
    request.cls.bin_list = BinList(request.cls.bin_list)


@pytest.mark.usefixtures("bin_list_class_fixture", "bin_list_test_fixture")
class TestBinList(object):
    """Tests for BinList"""
    def test_get_next_bin(self):
        """Tests get_next_bin"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.resource.objects import Bin
        if not is_never_authz(self.service_config):
            assert isinstance(self.bin_list.get_next_bin(), Bin)

    def test_get_next_bins(self):
        """Tests get_next_bins"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.resource.objects import BinList, Bin
        if not is_never_authz(self.service_config):
            new_list = self.bin_list.get_next_bins(2)
            assert isinstance(new_list, BinList)
            for item in new_list:
                assert isinstance(item, Bin)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_node_class_fixture(request):
    # Implemented from init template for BinNode
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinNode tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.bin_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def bin_node_test_fixture(request):
    # Implemented from init template for BinNode
    from dlkit.json_.resource.objects import BinNode
    request.cls.bin_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for BinNode tests'
            obj = request.cls.svc_mgr.create_bin(create_form)
            request.cls.bin_list.append(BinNode(
                obj.object_map,
                runtime=request.cls.svc_mgr._runtime,
                proxy=request.cls.svc_mgr._proxy))
            request.cls.bin_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_bin(request.cls.bin_list[0].ident)
        request.cls.svc_mgr.add_child_bin(
            request.cls.bin_list[0].ident,
            request.cls.bin_list[1].ident)

        request.cls.object = request.cls.svc_mgr.get_bin_nodes(
            request.cls.bin_list[0].ident, 0, 5, False)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_bin(
                request.cls.bin_list[0].ident,
                request.cls.bin_list[1].ident)
            request.cls.svc_mgr.remove_root_bin(request.cls.bin_list[0].ident)
            for node in request.cls.bin_list:
                request.cls.svc_mgr.delete_bin(node.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("bin_node_class_fixture", "bin_node_test_fixture")
class TestBinNode(object):
    """Tests for BinNode"""
    def test_get_bin(self):
        """Tests get_bin"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.resource.objects import Bin
        if not is_never_authz(self.service_config):
            assert isinstance(self.bin_list[0].get_bin(), OsidCatalog)
            assert str(self.bin_list[0].get_bin().ident) == str(self.bin_list[0].ident)

    def test_get_parent_bin_nodes(self):
        """Tests get_parent_bin_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.resource.objects import BinNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bin_nodes(
                self.bin_list[1].ident,
                1,
                0,
                False)
            assert isinstance(node.get_parent_bin_nodes(), BinNodeList)
            assert node.get_parent_bin_nodes().available() == 1
            assert str(node.get_parent_bin_nodes().next().ident) == str(self.bin_list[0].ident)

    def test_get_child_bin_nodes(self):
        """Tests get_child_bin_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.resource.objects import BinNodeList
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_bin_nodes(
                self.bin_list[0].ident,
                0,
                1,
                False)
            assert isinstance(node.get_child_bin_nodes(), BinNodeList)
            assert node.get_child_bin_nodes().available() == 1
            assert str(node.get_child_bin_nodes().next().ident) == str(self.bin_list[1].ident)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def bin_node_list_class_fixture(request):
    # Implemented from init template for BinNodeList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'RESOURCE',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinNodeList tests'
        request.cls.catalog = request.cls.svc_mgr.create_bin(create_form)
        request.cls.bin_node_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.bin_node_ids:
                request.cls.svc_mgr.delete_bin(obj)
            request.cls.svc_mgr.delete_bin(request.cls.catalog.ident)


@pytest.fixture(scope="function")
def bin_node_list_test_fixture(request):
    # Implemented from init template for BinNodeList
    from dlkit.json_.resource.objects import BinNodeList, BinNode
    request.cls.bin_node_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test BinNode ' + str(num)
            create_form.description = 'Test BinNode for BinNodeList tests'
            obj = request.cls.svc_mgr.create_bin(create_form)
            request.cls.bin_node_list.append(BinNode(obj.object_map))
            request.cls.bin_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        request.cls.svc_mgr.add_root_bin(request.cls.bin_node_list[0].ident)
        request.cls.svc_mgr.add_child_bin(
            request.cls.bin_node_list[0].ident,
            request.cls.bin_node_list[1].ident)
    request.cls.bin_node_list = BinNodeList(request.cls.bin_node_list)


@pytest.mark.usefixtures("bin_node_list_class_fixture", "bin_node_list_test_fixture")
class TestBinNodeList(object):
    """Tests for BinNodeList"""
    def test_get_next_bin_node(self):
        """Tests get_next_bin_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.resource.objects import BinNode
        if not is_never_authz(self.service_config):
            assert isinstance(self.bin_node_list.get_next_bin_node(), BinNode)

    def test_get_next_bin_nodes(self):
        """Tests get_next_bin_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.resource.objects import BinNodeList, BinNode
        if not is_never_authz(self.service_config):
            new_list = self.bin_node_list.get_next_bin_nodes(2)
            assert isinstance(new_list, BinNodeList)
            for item in new_list:
                assert isinstance(item, BinNode)
