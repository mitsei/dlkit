"""Unit tests of repository objects."""


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


class TestAsset(unittest.TestCase):
    """Tests for Asset"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        form = cls.catalog.get_asset_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_asset(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_title(self):
        """Tests get_title"""
        pass

    def test_is_copyright_status_known(self):
        """Tests is_copyright_status_known"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_copyright_status_known(), bool))
        self.assertFalse(self.object.is_copyright_status_known())

    def test_is_public_domain(self):
        """Tests is_public_domain"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_public_domain(), bool))
        self.assertFalse(self.object.is_public_domain())

    @unittest.skip('unimplemented test')
    def test_get_copyright(self):
        """Tests get_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_copyright_registration(self):
        """Tests get_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_distribute_verbatim(self):
        """Tests can_distribute_verbatim"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_distribute_alterations(self):
        """Tests can_distribute_alterations"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_distribute_compositions(self):
        """Tests can_distribute_compositions"""
        pass

    def test_get_source_id(self):
        """Tests get_source_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_source_id)

    def test_get_source(self):
        """Tests get_source"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_source)

    @unittest.skip('unimplemented test')
    def test_get_provider_link_ids(self):
        """Tests get_provider_link_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_provider_links(self):
        """Tests get_provider_links"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_created_date(self):
        """Tests get_created_date"""
        pass

    def test_is_published(self):
        """Tests is_published"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_published(), bool))
        self.assertFalse(self.object.is_published())

    @unittest.skip('unimplemented test')
    def test_get_published_date(self):
        """Tests get_published_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_principal_credit_string(self):
        """Tests get_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_content_ids(self):
        """Tests get_asset_content_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_contents(self):
        """Tests get_asset_contents"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_composition(self):
        """Tests is_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_id(self):
        """Tests get_composition_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition(self):
        """Tests get_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_record(self):
        """Tests get_asset_record"""
        pass


class TestAssetForm(unittest.TestCase):
    """Tests for AssetForm"""

    @unittest.skip('unimplemented test')
    def test_get_title_metadata(self):
        """Tests get_title_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_title(self):
        """Tests set_title"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_title(self):
        """Tests clear_title"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_public_domain_metadata(self):
        """Tests get_public_domain_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_public_domain(self):
        """Tests set_public_domain"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_public_domain(self):
        """Tests clear_public_domain"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_copyright_metadata(self):
        """Tests get_copyright_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_copyright(self):
        """Tests set_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_copyright(self):
        """Tests clear_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_copyright_registration_metadata(self):
        """Tests get_copyright_registration_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_copyright_registration(self):
        """Tests set_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_copyright_registration(self):
        """Tests clear_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_distribute_verbatim_metadata(self):
        """Tests get_distribute_verbatim_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_distribute_verbatim(self):
        """Tests set_distribute_verbatim"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_distribute_verbatim(self):
        """Tests clear_distribute_verbatim"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_distribute_alterations_metadata(self):
        """Tests get_distribute_alterations_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_distribute_alterations(self):
        """Tests set_distribute_alterations"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_distribute_alterations(self):
        """Tests clear_distribute_alterations"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_distribute_compositions_metadata(self):
        """Tests get_distribute_compositions_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_distribute_compositions(self):
        """Tests set_distribute_compositions"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_distribute_compositions(self):
        """Tests clear_distribute_compositions"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_source_metadata(self):
        """Tests get_source_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_source(self):
        """Tests set_source"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_source(self):
        """Tests clear_source"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_provider_links_metadata(self):
        """Tests get_provider_links_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_provider_links(self):
        """Tests set_provider_links"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_provider_links(self):
        """Tests clear_provider_links"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_created_date_metadata(self):
        """Tests get_created_date_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_created_date(self):
        """Tests set_created_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_created_date(self):
        """Tests clear_created_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_published_metadata(self):
        """Tests get_published_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_published(self):
        """Tests set_published"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_published(self):
        """Tests clear_published"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_published_date_metadata(self):
        """Tests get_published_date_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_published_date(self):
        """Tests set_published_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_published_date(self):
        """Tests clear_published_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_principal_credit_string_metadata(self):
        """Tests get_principal_credit_string_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_principal_credit_string(self):
        """Tests set_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_principal_credit_string(self):
        """Tests clear_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_metadata(self):
        """Tests get_composition_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_composition(self):
        """Tests set_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_composition(self):
        """Tests clear_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_form_record(self):
        """Tests get_asset_form_record"""
        pass


class TestAssetList(unittest.TestCase):
    """Tests for AssetList"""

    @unittest.skip('unimplemented test')
    def test_get_next_asset(self):
        """Tests get_next_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assets(self):
        """Tests get_next_assets"""
        pass


class TestAssetContent(unittest.TestCase):
    """Tests for AssetContent"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        form = cls.catalog.get_asset_form_for_create([])
        form.display_name = 'Asset'
        cls.asset = cls.catalog.create_asset(form)

        form = cls.catalog.get_asset_content_form_for_create(cls.asset.ident,
                                                             [])
        form.display_name = 'Test asset content'
        cls.object = cls.catalog.create_asset_content(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_asset_id(self):
        """Tests get_asset_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset(self):
        """Tests get_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_accessibility_types(self):
        """Tests get_accessibility_types"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_data_length(self):
        """Tests has_data_length"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_data_length(self):
        """Tests get_data_length"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_data(self):
        """Tests get_data"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_url(self):
        """Tests has_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_url(self):
        """Tests get_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_content_record(self):
        """Tests get_asset_content_record"""
        pass


class TestAssetContentForm(unittest.TestCase):
    """Tests for AssetContentForm"""

    @unittest.skip('unimplemented test')
    def test_get_accessibility_type_metadata(self):
        """Tests get_accessibility_type_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_add_accessibility_type(self):
        """Tests add_accessibility_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_remove_accessibility_type(self):
        """Tests remove_accessibility_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_accessibility_types(self):
        """Tests clear_accessibility_types"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_data_metadata(self):
        """Tests get_data_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_data(self):
        """Tests set_data"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_data(self):
        """Tests clear_data"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_url_metadata(self):
        """Tests get_url_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_url(self):
        """Tests set_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_url(self):
        """Tests clear_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_content_form_record(self):
        """Tests get_asset_content_form_record"""
        pass


class TestAssetContentList(unittest.TestCase):
    """Tests for AssetContentList"""

    @unittest.skip('unimplemented test')
    def test_get_next_asset_content(self):
        """Tests get_next_asset_content"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_asset_contents(self):
        """Tests get_next_asset_contents"""
        pass


class TestComposition(unittest.TestCase):
    """Tests for Composition"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        form = cls.catalog.get_composition_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_composition(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_compositions():
            cls.catalog.delete_composition(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_children_ids(self):
        """Tests get_children_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_children(self):
        """Tests get_children"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_record(self):
        """Tests get_composition_record"""
        pass


class TestCompositionForm(unittest.TestCase):
    """Tests for CompositionForm"""

    @unittest.skip('unimplemented test')
    def test_get_composition_form_record(self):
        """Tests get_composition_form_record"""
        pass


class TestCompositionList(unittest.TestCase):
    """Tests for CompositionList"""

    @unittest.skip('unimplemented test')
    def test_get_next_composition(self):
        """Tests get_next_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_compositions(self):
        """Tests get_next_compositions"""
        pass


class TestRepository(unittest.TestCase):
    """Tests for Repository"""

    @unittest.skip('unimplemented test')
    def test_get_repository_record(self):
        """Tests get_repository_record"""
        pass


class TestRepositoryForm(unittest.TestCase):
    """Tests for RepositoryForm"""

    @unittest.skip('unimplemented test')
    def test_get_repository_form_record(self):
        """Tests get_repository_form_record"""
        pass


class TestRepositoryList(unittest.TestCase):
    """Tests for RepositoryList"""

    @unittest.skip('unimplemented test')
    def test_get_next_repository(self):
        """Tests get_next_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_repositories(self):
        """Tests get_next_repositories"""
        pass


class TestRepositoryNode(unittest.TestCase):
    """Tests for RepositoryNode"""

    @unittest.skip('unimplemented test')
    def test_get_repository(self):
        """Tests get_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_repository_nodes(self):
        """Tests get_parent_repository_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_repository_nodes(self):
        """Tests get_child_repository_nodes"""
        pass


class TestRepositoryNodeList(unittest.TestCase):
    """Tests for RepositoryNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_repository_node(self):
        """Tests get_next_repository_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_repository_nodes(self):
        """Tests get_next_repository_nodes"""
        pass
