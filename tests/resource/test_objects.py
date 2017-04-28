"""Unit tests of resource objects."""


import unittest


from dlkit.abstract_osid.osid import errors
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

    @unittest.skip('unimplemented test')
    def test_is_demographic(self):
        """Tests is_demographic"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_get_group_metadata(self):
        """Tests get_group_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_group(self):
        """Tests set_group"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_group(self):
        """Tests clear_group"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_avatar_metadata(self):
        """Tests get_avatar_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_avatar(self):
        """Tests set_avatar"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_avatar(self):
        """Tests clear_avatar"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource_form_record(self):
        """Tests get_resource_form_record"""
        pass


class TestResourceList(unittest.TestCase):
    """Tests for ResourceList"""

    @unittest.skip('unimplemented test')
    def test_get_next_resource(self):
        """Tests get_next_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_resources(self):
        """Tests get_next_resources"""
        pass


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

    @unittest.skip('unimplemented test')
    def test_get_next_bin(self):
        """Tests get_next_bin"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_bins(self):
        """Tests get_next_bins"""
        pass


class TestBinNode(unittest.TestCase):
    """Tests for BinNode"""

    @unittest.skip('unimplemented test')
    def test_get_bin(self):
        """Tests get_bin"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_bin_nodes(self):
        """Tests get_parent_bin_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_bin_nodes(self):
        """Tests get_child_bin_nodes"""
        pass


class TestBinNodeList(unittest.TestCase):
    """Tests for BinNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_bin_node(self):
        """Tests get_next_bin_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_bin_nodes(self):
        """Tests get_next_bin_nodes"""
        pass
