"""Unit tests of repository objects."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
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

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_asset_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_title_metadata(self):
        """Tests get_title_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_title_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_title(self):
        """Tests set_title"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_title(self):
        """Tests clear_title"""
        pass

    def test_get_public_domain_metadata(self):
        """Tests get_public_domain_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_public_domain_metadata(), Metadata))

    def test_set_public_domain(self):
        """Tests set_public_domain"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_public_domain(True)
        self.assertTrue(self.form._my_map['publicDomain'])

    def test_clear_public_domain(self):
        """Tests clear_public_domain"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_public_domain(True)
        self.assertTrue(self.form._my_map['publicDomain'])
        self.form.clear_public_domain()
        self.assertIsNone(self.form._my_map['publicDomain'])

    def test_get_copyright_metadata(self):
        """Tests get_copyright_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_copyright_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_copyright(self):
        """Tests set_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_copyright(self):
        """Tests clear_copyright"""
        pass

    def test_get_copyright_registration_metadata(self):
        """Tests get_copyright_registration_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_copyright_registration_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_copyright_registration(self):
        """Tests set_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_copyright_registration(self):
        """Tests clear_copyright_registration"""
        pass

    def test_get_distribute_verbatim_metadata(self):
        """Tests get_distribute_verbatim_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_distribute_verbatim_metadata(), Metadata))

    def test_set_distribute_verbatim(self):
        """Tests set_distribute_verbatim"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_distribute_verbatim(True)
        self.assertTrue(self.form._my_map['distributeVerbatim'])

    def test_clear_distribute_verbatim(self):
        """Tests clear_distribute_verbatim"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_distribute_verbatim(True)
        self.assertTrue(self.form._my_map['distributeVerbatim'])
        self.form.clear_distribute_verbatim()
        self.assertIsNone(self.form._my_map['distributeVerbatim'])

    def test_get_distribute_alterations_metadata(self):
        """Tests get_distribute_alterations_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_distribute_alterations_metadata(), Metadata))

    def test_set_distribute_alterations(self):
        """Tests set_distribute_alterations"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_distribute_alterations(True)
        self.assertTrue(self.form._my_map['distributeAlterations'])

    def test_clear_distribute_alterations(self):
        """Tests clear_distribute_alterations"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_distribute_alterations(True)
        self.assertTrue(self.form._my_map['distributeAlterations'])
        self.form.clear_distribute_alterations()
        self.assertIsNone(self.form._my_map['distributeAlterations'])

    def test_get_distribute_compositions_metadata(self):
        """Tests get_distribute_compositions_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_distribute_compositions_metadata(), Metadata))

    def test_set_distribute_compositions(self):
        """Tests set_distribute_compositions"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_distribute_compositions(True)
        self.assertTrue(self.form._my_map['distributeCompositions'])

    def test_clear_distribute_compositions(self):
        """Tests clear_distribute_compositions"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_distribute_compositions(True)
        self.assertTrue(self.form._my_map['distributeCompositions'])
        self.form.clear_distribute_compositions()
        self.assertIsNone(self.form._my_map['distributeCompositions'])

    def test_get_source_metadata(self):
        """Tests get_source_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_source_metadata(), Metadata))

    def test_set_source(self):
        """Tests set_source"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['sourceId'], '')
        self.form.set_source(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['sourceId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_source(self):
        """Tests clear_source"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_source(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['sourceId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_source()
        self.assertEqual(self.form._my_map['sourceId'], '')

    def test_get_provider_links_metadata(self):
        """Tests get_provider_links_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        self.assertTrue(isinstance(self.form.get_provider_links_metadata(), Metadata))

    def test_set_provider_links(self):
        """Tests set_provider_links"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_provider_links([test_id])
        self.assertTrue(len(self.form._my_map['providerLinkIds']), 1)
        self.assertEqual(self.form._my_map['providerLinkIds'][0],
                         str(test_id))
        # reset this for other tests
        self.form._my_map['providerLinkIds'] = list()

    def test_clear_provider_links(self):
        """Tests clear_provider_links"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_provider_links([test_id])
        self.assertTrue(len(self.form._my_map['providerLinkIds']), 1)
        self.assertEqual(self.form._my_map['providerLinkIds'][0],
                         str(test_id))
        self.form.clear_provider_links()
        self.assertEqual(self.form._my_map['providerLinkIds'], [])

    def test_get_created_date_metadata(self):
        """Tests get_created_date_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_created_date_metadata(), Metadata))

    def test_set_created_date(self):
        """Tests set_created_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_start_time_template
        test_time = DateTime.utcnow()
        self.assertIsNone(self.form._my_map['createdDate'])
        self.form.set_created_date(test_time)
        self.assertEqual(self.form._my_map['createdDate'],
                         test_time)
        # reset this for other tests
        self.form._my_map['createdDate'] = None

    def test_clear_created_date(self):
        """Tests clear_created_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_start_time_template
        test_time = DateTime.utcnow()
        self.assertIsNone(self.form._my_map['createdDate'])
        self.form.set_created_date(test_time)
        self.assertEqual(self.form._my_map['createdDate'],
                         test_time)
        self.form.clear_created_date()
        self.assertIsNone(self.form._my_map['createdDate'])

    def test_get_published_metadata(self):
        """Tests get_published_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_published_metadata(), Metadata))

    def test_set_published(self):
        """Tests set_published"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_published(True)
        self.assertTrue(self.form._my_map['published'])

    def test_clear_published(self):
        """Tests clear_published"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_published(True)
        self.assertTrue(self.form._my_map['published'])
        self.form.clear_published()
        self.assertIsNone(self.form._my_map['published'])

    def test_get_published_date_metadata(self):
        """Tests get_published_date_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_published_date_metadata(), Metadata))

    def test_set_published_date(self):
        """Tests set_published_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_start_time_template
        test_time = DateTime.utcnow()
        self.assertIsNone(self.form._my_map['publishedDate'])
        self.form.set_published_date(test_time)
        self.assertEqual(self.form._my_map['publishedDate'],
                         test_time)
        # reset this for other tests
        self.form._my_map['publishedDate'] = None

    def test_clear_published_date(self):
        """Tests clear_published_date"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_start_time_template
        test_time = DateTime.utcnow()
        self.assertIsNone(self.form._my_map['publishedDate'])
        self.form.set_published_date(test_time)
        self.assertEqual(self.form._my_map['publishedDate'],
                         test_time)
        self.form.clear_published_date()
        self.assertIsNone(self.form._my_map['publishedDate'])

    def test_get_principal_credit_string_metadata(self):
        """Tests get_principal_credit_string_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_principal_credit_string_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_principal_credit_string(self):
        """Tests set_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_principal_credit_string(self):
        """Tests clear_principal_credit_string"""
        pass

    def test_get_composition_metadata(self):
        """Tests get_composition_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_composition_metadata(), Metadata))

    def test_set_composition(self):
        """Tests set_composition"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['compositionId'], '')
        self.form.set_composition(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['compositionId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_composition(self):
        """Tests clear_composition"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_composition(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['compositionId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_composition()
        self.assertEqual(self.form._my_map['compositionId'], '')

    def test_get_asset_form_record(self):
        """Tests get_asset_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_asset_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssetList(unittest.TestCase):
    """Tests for AssetList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetList tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.repository.objects import AssetList
        self.asset_list = list()
        self.asset_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetList tests'
            obj = self.catalog.create_asset(create_form)
            self.asset_list.append(obj)
            self.asset_ids.append(obj.ident)
        self.asset_list = AssetList(self.asset_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_next_asset(self):
        """Tests get_next_asset"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import Asset
        self.assertTrue(isinstance(self.asset_list.get_next_asset(), Asset))

    def test_get_next_assets(self):
        """Tests get_next_assets"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import AssetList, Asset
        new_list = self.asset_list.get_next_assets(2)
        self.assertTrue(isinstance(new_list, AssetList))
        for item in new_list:
            self.assertTrue(isinstance(item, Asset))


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
        form.set_url('https://www.google.com')
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

    def test_has_url(self):
        """Tests has_url"""
        # From test_templates/repository.py::AssetContent::has_url_template
        self.assertTrue(self.object.has_url())

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

        cls.form = cls.catalog.get_asset_content_form_for_create(cls.asset.ident,
                                                                 [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_accessibility_type_metadata(self):
        """Tests get_accessibility_type_metadata"""
        # From test_templates/logging.py::LogEntryForm::get_priority_metadata_template
        self.assertTrue(isinstance(self.form.get_accessibility_type_metadata(), Metadata))

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

    def test_get_data_metadata(self):
        """Tests get_data_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_data_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_data(self):
        """Tests set_data"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_data(self):
        """Tests clear_data"""
        pass

    def test_get_url_metadata(self):
        """Tests get_url_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_url_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_url(self):
        """Tests set_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_url(self):
        """Tests clear_url"""
        pass

    def test_get_asset_content_form_record(self):
        """Tests get_asset_content_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_asset_content_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssetContentList(unittest.TestCase):
    """Tests for AssetContentList"""

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

        cls.form = cls.catalog.get_asset_content_form_for_create(cls.asset.ident,
                                                                 [])

    def setUp(self):
        from dlkit.json_.repository.objects import AssetContentList
        self.asset_content_list = list()
        self.asset_content_ids = list()
        for num in [0, 1]:
            form = self.catalog.get_asset_content_form_for_create(self.asset.ident,
                                                                  [])
            form.display_name = 'Test AssetContent ' + str(num)
            form.description = 'Test AssetContent for AssetContentList tests'
            obj = self.catalog.create_asset_content(form)

            self.asset_content_list.append(obj)
            self.asset_content_ids.append(obj.ident)
        self.asset_content_list = AssetContentList(self.asset_content_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_next_asset_content(self):
        """Tests get_next_asset_content"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import AssetContent
        self.assertTrue(isinstance(self.asset_content_list.get_next_asset_content(), AssetContent))

    def test_get_next_asset_contents(self):
        """Tests get_next_asset_contents"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import AssetContentList, AssetContent
        new_list = self.asset_content_list.get_next_asset_contents(2)
        self.assertTrue(isinstance(new_list, AssetContentList))
        for item in new_list:
            self.assertTrue(isinstance(item, AssetContent))


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

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_composition_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_composition_form_record(self):
        """Tests get_composition_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_composition_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestCompositionList(unittest.TestCase):
    """Tests for CompositionList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionList tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.repository.objects import CompositionList
        self.composition_list = list()
        self.composition_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionList tests'
            obj = self.catalog.create_composition(create_form)
            self.composition_list.append(obj)
            self.composition_ids.append(obj.ident)
        self.composition_list = CompositionList(self.composition_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_compositions():
            cls.catalog.delete_composition(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_next_composition(self):
        """Tests get_next_composition"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import Composition
        self.assertTrue(isinstance(self.composition_list.get_next_composition(), Composition))

    def test_get_next_compositions(self):
        """Tests get_next_compositions"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import CompositionList, Composition
        new_list = self.composition_list.get_next_compositions(2)
        self.assertTrue(isinstance(new_list, CompositionList))
        for item in new_list:
            self.assertTrue(isinstance(item, Composition))


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

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryList tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        cls.repository_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.repository.objects import RepositoryList
        self.repository_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test Repository ' + str(num)
            create_form.description = 'Test Repository for RepositoryList tests'
            obj = self.svc_mgr.create_repository(create_form)
            self.repository_list.append(obj)
            self.repository_ids.append(obj.ident)
        self.repository_list = RepositoryList(self.repository_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.repository_ids:
            cls.svc_mgr.delete_repository(obj)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_next_repository(self):
        """Tests get_next_repository"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import Repository
        self.assertTrue(isinstance(self.repository_list.get_next_repository(), Repository))

    def test_get_next_repositories(self):
        """Tests get_next_repositories"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import RepositoryList, Repository
        new_list = self.repository_list.get_next_repositories(2)
        self.assertTrue(isinstance(new_list, RepositoryList))
        for item in new_list:
            self.assertTrue(isinstance(item, Repository))


class TestRepositoryNode(unittest.TestCase):
    """Tests for RepositoryNode"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNode
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryNode tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        cls.repository_ids = list()

    def setUp(self):
        # Implemented from init template for BinNode
        from dlkit.json_.repository.objects import RepositoryNode
        self.repository_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test Repository ' + str(num)
            create_form.description = 'Test Repository for RepositoryNode tests'
            obj = self.svc_mgr.create_repository(create_form)
            self.repository_list.append(RepositoryNode(
                obj.object_map,
                runtime=self.svc_mgr._runtime,
                proxy=self.svc_mgr._proxy))
            self.repository_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_repository(self.repository_list[0].ident)
        self.svc_mgr.add_child_repository(
            self.repository_list[0].ident,
            self.repository_list[1].ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNode
        for obj in cls.repository_ids:
            cls.svc_mgr.delete_repository(obj)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.repository.objects import Repository
        self.assertTrue(isinstance(self.repository_list[0].get_repository(), Repository))
        self.assertEqual(str(self.repository_list[0].get_repository().ident),
                         str(self.repository_list[0].ident))

    def test_get_parent_repository_nodes(self):
        """Tests get_parent_repository_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.repository.objects import RepositoryNodeList
        node = self.svc_mgr.get_repository_nodes(
            self.repository_list[1].ident,
            1,
            0,
            False)
        self.assertTrue(isinstance(node.get_parent_repository_nodes(), RepositoryNodeList))
        self.assertEqual(node.get_parent_repository_nodes().available(),
                         1)
        self.assertEqual(str(node.get_parent_repository_nodes().next().ident),
                         str(self.repository_list[0].ident))

    def test_get_child_repository_nodes(self):
        """Tests get_child_repository_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.repository.objects import RepositoryNodeList
        node = self.svc_mgr.get_repository_nodes(
            self.repository_list[0].ident,
            0,
            1,
            False)
        self.assertTrue(isinstance(node.get_child_repository_nodes(), RepositoryNodeList))
        self.assertEqual(node.get_child_repository_nodes().available(),
                         1)
        self.assertEqual(str(node.get_child_repository_nodes().next().ident),
                         str(self.repository_list[1].ident))


class TestRepositoryNodeList(unittest.TestCase):
    """Tests for RepositoryNodeList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNodeList
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryNodeList tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        cls.repository_node_ids = list()

    def setUp(self):
        # Implemented from init template for BinNodeList
        from dlkit.json_.repository.objects import RepositoryNodeList, RepositoryNode
        self.repository_node_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test RepositoryNode ' + str(num)
            create_form.description = 'Test RepositoryNode for RepositoryNodeList tests'
            obj = self.svc_mgr.create_repository(create_form)
            self.repository_node_list.append(RepositoryNode(obj.object_map))
            self.repository_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_repository(self.repository_node_list[0].ident)
        self.svc_mgr.add_child_repository(
            self.repository_node_list[0].ident,
            self.repository_node_list[1].ident)
        self.repository_node_list = RepositoryNodeList(self.repository_node_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNodeList
        for obj in cls.repository_node_ids:
            cls.svc_mgr.delete_repository(obj)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_next_repository_node(self):
        """Tests get_next_repository_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.repository.objects import RepositoryNode
        self.assertTrue(isinstance(self.repository_node_list.get_next_repository_node(), RepositoryNode))

    def test_get_next_repository_nodes(self):
        """Tests get_next_repository_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.repository.objects import RepositoryNodeList, RepositoryNode
        new_list = self.repository_node_list.get_next_repository_nodes(2)
        self.assertTrue(isinstance(new_list, RepositoryNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, RepositoryNode))
