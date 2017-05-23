"""Unit tests of resource objects."""


import unittest


from dlkit.abstract_osid.osid import errors
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


class TestResource(unittest.TestCase):
    """Tests for Resource"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bin(create_form)

        form = cls.catalog.get_resource_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_resource(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_is_group(self):
        """Tests is_group"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_group(), bool))
        self.assertFalse(self.object.is_group())

    def test_is_demographic(self):
        """Tests is_demographic"""
        with self.assertRaises(AttributeError):
            self.object.is_demographic()

    def test_has_avatar(self):
        """Tests has_avatar"""
        # From test_templates/resources.py::Resource::has_avatar_template
        self.assertTrue(isinstance(self.object.has_avatar(), bool))
        self.assertFalse(self.object.has_avatar())

    def test_get_avatar_id(self):
        """Tests get_avatar_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_avatar_id)

    def test_get_avatar(self):
        """Tests get_avatar"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_avatar)

    @unittest.skip('unimplemented test')
    def test_get_resource_record(self):
        """Tests get_resource_record"""
        pass


class TestResourceForm(unittest.TestCase):
    """Tests for ResourceForm"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bin(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_resource_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_group_metadata(self):
        """Tests get_group_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_group_metadata(), Metadata))

    def test_set_group(self):
        """Tests set_group"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_group(True)
        self.assertTrue(self.form._my_map['group'])

    def test_clear_group(self):
        """Tests clear_group"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_group(True)
        self.assertTrue(self.form._my_map['group'])
        self.form.clear_group()
        self.assertIsNone(self.form._my_map['group'])

    def test_get_avatar_metadata(self):
        """Tests get_avatar_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_avatar_metadata(), Metadata))

    def test_set_avatar(self):
        """Tests set_avatar"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['avatarId'], '')
        self.form.set_avatar(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['avatarId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_avatar(self):
        """Tests clear_avatar"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_avatar(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['avatarId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_avatar()
        self.assertEqual(self.form._my_map['avatarId'], '')

    def test_get_resource_form_record(self):
        """Tests get_resource_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_resource_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestResourceList(unittest.TestCase):
    """Tests for ResourceList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceList tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.resource.objects import ResourceList
        self.resource_list = list()
        self.resource_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceList tests'
            obj = self.catalog.create_resource(create_form)
            self.resource_list.append(obj)
            self.resource_ids.append(obj.ident)
        self.resource_list = ResourceList(self.resource_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_next_resource(self):
        """Tests get_next_resource"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.resource.objects import Resource
        self.assertTrue(isinstance(self.resource_list.get_next_resource(), Resource))

    def test_get_next_resources(self):
        """Tests get_next_resources"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.resource.objects import ResourceList, Resource
        new_list = self.resource_list.get_next_resources(2)
        self.assertTrue(isinstance(new_list, ResourceList))
        for item in new_list:
            self.assertTrue(isinstance(item, Resource))


class TestResourceNode(unittest.TestCase):
    """Tests for ResourceNode"""

    @unittest.skip('unimplemented test')
    def test_get_resource(self):
        """Tests get_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_resource_nodes(self):
        """Tests get_parent_resource_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_resource_nodes(self):
        """Tests get_child_resource_nodes"""
        pass


class TestResourceNodeList(unittest.TestCase):
    """Tests for ResourceNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_resource_node(self):
        """Tests get_next_resource_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_resource_nodes(self):
        """Tests get_next_resource_nodes"""
        pass


class TestBin(unittest.TestCase):
    """Tests for Bin"""

    @unittest.skip('unimplemented test')
    def test_get_bin_record(self):
        """Tests get_bin_record"""
        pass


class TestBinForm(unittest.TestCase):
    """Tests for BinForm"""

    @unittest.skip('unimplemented test')
    def test_get_bin_form_record(self):
        """Tests get_bin_form_record"""
        pass


class TestBinList(unittest.TestCase):
    """Tests for BinList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinList tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        cls.bin_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.resource.objects import BinList
        self.bin_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for BinList tests'
            obj = self.svc_mgr.create_bin(create_form)
            self.bin_list.append(obj)
            self.bin_ids.append(obj.ident)
        self.bin_list = BinList(self.bin_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.bin_ids:
            cls.svc_mgr.delete_bin(obj)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_next_bin(self):
        """Tests get_next_bin"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.resource.objects import Bin
        self.assertTrue(isinstance(self.bin_list.get_next_bin(), Bin))

    def test_get_next_bins(self):
        """Tests get_next_bins"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.resource.objects import BinList, Bin
        new_list = self.bin_list.get_next_bins(2)
        self.assertTrue(isinstance(new_list, BinList))
        for item in new_list:
            self.assertTrue(isinstance(item, Bin))


class TestBinNode(unittest.TestCase):
    """Tests for BinNode"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNode
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinNode tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        cls.bin_ids = list()

    def setUp(self):
        # Implemented from init template for BinNode
        from dlkit.json_.resource.objects import BinNode
        self.bin_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for BinNode tests'
            obj = self.svc_mgr.create_bin(create_form)
            self.bin_list.append(BinNode(
                obj.object_map,
                runtime=self.svc_mgr._runtime,
                proxy=self.svc_mgr._proxy))
            self.bin_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_bin(self.bin_list[0].ident)
        self.svc_mgr.add_child_bin(
            self.bin_list[0].ident,
            self.bin_list[1].ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNode
        for obj in cls.bin_ids:
            cls.svc_mgr.delete_bin(obj)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.resource.objects import Bin
        self.assertTrue(isinstance(self.bin_list[0].get_bin(), Bin))
        self.assertEqual(str(self.bin_list[0].get_bin().ident),
                         str(self.bin_list[0].ident))

    def test_get_parent_bin_nodes(self):
        """Tests get_parent_bin_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.resource.objects import BinNodeList
        node = self.svc_mgr.get_bin_nodes(
            self.bin_list[1].ident,
            1,
            0,
            False)
        self.assertTrue(isinstance(node.get_parent_bin_nodes(), BinNodeList))
        self.assertEqual(node.get_parent_bin_nodes().available(),
                         1)
        self.assertEqual(str(node.get_parent_bin_nodes().next().ident),
                         str(self.bin_list[0].ident))

    def test_get_child_bin_nodes(self):
        """Tests get_child_bin_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.resource.objects import BinNodeList
        node = self.svc_mgr.get_bin_nodes(
            self.bin_list[0].ident,
            0,
            1,
            False)
        self.assertTrue(isinstance(node.get_child_bin_nodes(), BinNodeList))
        self.assertEqual(node.get_child_bin_nodes().available(),
                         1)
        self.assertEqual(str(node.get_child_bin_nodes().next().ident),
                         str(self.bin_list[1].ident))


class TestBinNodeList(unittest.TestCase):
    """Tests for BinNodeList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNodeList
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinNodeList tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        cls.bin_node_ids = list()

    def setUp(self):
        # Implemented from init template for BinNodeList
        from dlkit.json_.resource.objects import BinNodeList, BinNode
        self.bin_node_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test BinNode ' + str(num)
            create_form.description = 'Test BinNode for BinNodeList tests'
            obj = self.svc_mgr.create_bin(create_form)
            self.bin_node_list.append(BinNode(obj.object_map))
            self.bin_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_bin(self.bin_node_list[0].ident)
        self.svc_mgr.add_child_bin(
            self.bin_node_list[0].ident,
            self.bin_node_list[1].ident)
        self.bin_node_list = BinNodeList(self.bin_node_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNodeList
        for obj in cls.bin_node_ids:
            cls.svc_mgr.delete_bin(obj)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_next_bin_node(self):
        """Tests get_next_bin_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.resource.objects import BinNode
        self.assertTrue(isinstance(self.bin_node_list.get_next_bin_node(), BinNode))

    def test_get_next_bin_nodes(self):
        """Tests get_next_bin_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.resource.objects import BinNodeList, BinNode
        new_list = self.bin_node_list.get_next_bin_nodes(2)
        self.assertTrue(isinstance(new_list, BinNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, BinNode))
