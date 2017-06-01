"""Unit tests of repository queries."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAssetQuery(unittest.TestCase):
    """Tests for AssetQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_asset_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_title(self):
        """Tests match_title"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_title(self):
        """Tests match_any_title"""
        pass

    def test_clear_title_terms(self):
        """Tests clear_title_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['title'] = 'foo'
        self.query.clear_title_terms()
        self.assertNotIn('title',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_public_domain(self):
        """Tests match_public_domain"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_public_domain(self):
        """Tests match_any_public_domain"""
        pass

    def test_clear_public_domain_terms(self):
        """Tests clear_public_domain_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['publicDomain'] = 'foo'
        self.query.clear_public_domain_terms()
        self.assertNotIn('publicDomain',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_copyright(self):
        """Tests match_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_copyright(self):
        """Tests match_any_copyright"""
        pass

    def test_clear_copyright_terms(self):
        """Tests clear_copyright_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['copyright'] = 'foo'
        self.query.clear_copyright_terms()
        self.assertNotIn('copyright',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_copyright_registration(self):
        """Tests match_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_copyright_registration(self):
        """Tests match_any_copyright_registration"""
        pass

    def test_clear_copyright_registration_terms(self):
        """Tests clear_copyright_registration_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['copyrightRegistration'] = 'foo'
        self.query.clear_copyright_registration_terms()
        self.assertNotIn('copyrightRegistration',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_distribute_verbatim(self):
        """Tests match_distribute_verbatim"""
        pass

    def test_clear_distribute_verbatim_terms(self):
        """Tests clear_distribute_verbatim_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['distributeVerbatim'] = 'foo'
        self.query.clear_distribute_verbatim_terms()
        self.assertNotIn('distributeVerbatim',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_distribute_alterations(self):
        """Tests match_distribute_alterations"""
        pass

    def test_clear_distribute_alterations_terms(self):
        """Tests clear_distribute_alterations_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['distributeAlterations'] = 'foo'
        self.query.clear_distribute_alterations_terms()
        self.assertNotIn('distributeAlterations',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_distribute_compositions(self):
        """Tests match_distribute_compositions"""
        pass

    def test_clear_distribute_compositions_terms(self):
        """Tests clear_distribute_compositions_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['distributeCompositions'] = 'foo'
        self.query.clear_distribute_compositions_terms()
        self.assertNotIn('distributeCompositions',
                         self.query._query_terms)

    def test_match_source_id(self):
        """Tests match_source_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_source_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['sourceId'], {
            '$in': [str(test_id)]
        })

    def test_clear_source_id_terms(self):
        """Tests clear_source_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_source_id(test_id, match=True)
        self.assertIn('sourceId',
                      self.query._query_terms)
        self.query.clear_source_id_terms()
        self.assertNotIn('sourceId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_source_query(self):
        """Tests supports_source_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_source_query(self):
        """Tests get_source_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_source(self):
        """Tests match_any_source"""
        pass

    def test_clear_source_terms(self):
        """Tests clear_source_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['source'] = 'foo'
        self.query.clear_source_terms()
        self.assertNotIn('source',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_created_date(self):
        """Tests match_created_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_created_date(self):
        """Tests match_any_created_date"""
        pass

    def test_clear_created_date_terms(self):
        """Tests clear_created_date_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['createdDate'] = 'foo'
        self.query.clear_created_date_terms()
        self.assertNotIn('createdDate',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_published(self):
        """Tests match_published"""
        pass

    def test_clear_published_terms(self):
        """Tests clear_published_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['published'] = 'foo'
        self.query.clear_published_terms()
        self.assertNotIn('published',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_published_date(self):
        """Tests match_published_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_published_date(self):
        """Tests match_any_published_date"""
        pass

    def test_clear_published_date_terms(self):
        """Tests clear_published_date_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['publishedDate'] = 'foo'
        self.query.clear_published_date_terms()
        self.assertNotIn('publishedDate',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_principal_credit_string(self):
        """Tests match_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_principal_credit_string(self):
        """Tests match_any_principal_credit_string"""
        pass

    def test_clear_principal_credit_string_terms(self):
        """Tests clear_principal_credit_string_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['principalCreditString'] = 'foo'
        self.query.clear_principal_credit_string_terms()
        self.assertNotIn('principalCreditString',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_temporal_coverage(self):
        """Tests match_temporal_coverage"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_temporal_coverage(self):
        """Tests match_any_temporal_coverage"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_temporal_coverage_terms(self):
        """Tests clear_temporal_coverage_terms"""
        pass

    def test_match_location_id(self):
        """Tests match_location_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_location_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['locationId'], {
            '$in': [str(test_id)]
        })

    def test_clear_location_id_terms(self):
        """Tests clear_location_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_location_id(test_id, match=True)
        self.assertIn('locationId',
                      self.query._query_terms)
        self.query.clear_location_id_terms()
        self.assertNotIn('locationId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_location_query(self):
        """Tests supports_location_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_location_query(self):
        """Tests get_location_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_location(self):
        """Tests match_any_location"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_location_terms(self):
        """Tests clear_location_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_spatial_coverage(self):
        """Tests match_spatial_coverage"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_spatial_coverage_terms(self):
        """Tests clear_spatial_coverage_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_spatial_coverage_overlap(self):
        """Tests match_spatial_coverage_overlap"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_spatial_coverage(self):
        """Tests match_any_spatial_coverage"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_spatial_coverage_overlap_terms(self):
        """Tests clear_spatial_coverage_overlap_terms"""
        pass

    def test_match_asset_content_id(self):
        """Tests match_asset_content_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_content_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assetContentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_asset_content_id_terms(self):
        """Tests clear_asset_content_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_content_id(test_id, match=True)
        self.assertIn('assetContentId',
                      self.query._query_terms)
        self.query.clear_asset_content_id_terms()
        self.assertNotIn('assetContentId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_asset_content_query(self):
        """Tests supports_asset_content_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_content_query(self):
        """Tests get_asset_content_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_asset_content(self):
        """Tests match_any_asset_content"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_content_terms(self):
        """Tests clear_asset_content_terms"""
        pass

    def test_match_composition_id(self):
        """Tests match_composition_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_composition_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['compositionId'], {
            '$in': [str(test_id)]
        })

    def test_clear_composition_id_terms(self):
        """Tests clear_composition_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_composition_id(test_id, match=True)
        self.assertIn('compositionId',
                      self.query._query_terms)
        self.query.clear_composition_id_terms()
        self.assertNotIn('compositionId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_composition_query(self):
        """Tests supports_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_query(self):
        """Tests get_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_composition(self):
        """Tests match_any_composition"""
        pass

    def test_clear_composition_terms(self):
        """Tests clear_composition_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['composition'] = 'foo'
        self.query.clear_composition_terms()
        self.assertNotIn('composition',
                         self.query._query_terms)

    def test_match_repository_id(self):
        """Tests match_repository_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedRepositoryIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_repository_id_terms(self):
        """Tests clear_repository_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)
        self.assertIn('assignedRepositoryIds',
                      self.query._query_terms)
        self.query.clear_repository_id_terms()
        self.assertNotIn('assignedRepositoryIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query(self):
        """Tests get_repository_query"""
        pass

    def test_clear_repository_terms(self):
        """Tests clear_repository_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['repository'] = 'foo'
        self.query.clear_repository_terms()
        self.assertNotIn('repository',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_asset_query_record(self):
        """Tests get_asset_query_record"""
        pass


class TestAssetContentQuery(unittest.TestCase):
    """Tests for AssetContentQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_asset_content_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_accessibility_type(self):
        """Tests match_accessibility_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_accessibility_type(self):
        """Tests match_any_accessibility_type"""
        pass

    def test_clear_accessibility_type_terms(self):
        """Tests clear_accessibility_type_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['accessibilityType'] = 'foo'
        self.query.clear_accessibility_type_terms()
        self.assertNotIn('accessibilityType',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_data_length(self):
        """Tests match_data_length"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_data_length(self):
        """Tests match_any_data_length"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_data_length_terms(self):
        """Tests clear_data_length_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_data(self):
        """Tests match_data"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_data(self):
        """Tests match_any_data"""
        pass

    def test_clear_data_terms(self):
        """Tests clear_data_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['data'] = 'foo'
        self.query.clear_data_terms()
        self.assertNotIn('data',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_url(self):
        """Tests match_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_url(self):
        """Tests match_any_url"""
        pass

    def test_clear_url_terms(self):
        """Tests clear_url_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['url'] = 'foo'
        self.query.clear_url_terms()
        self.assertNotIn('url',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_asset_content_query_record(self):
        """Tests get_asset_content_query_record"""
        pass


class TestCompositionQuery(unittest.TestCase):
    """Tests for CompositionQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_composition_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_match_asset_id(self):
        """Tests match_asset_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assetIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_asset_id_terms(self):
        """Tests clear_asset_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_id(test_id, match=True)
        self.assertIn('assetIds',
                      self.query._query_terms)
        self.query.clear_asset_id_terms()
        self.assertNotIn('assetIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_query(self):
        """Tests get_asset_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_asset(self):
        """Tests match_any_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_terms(self):
        """Tests clear_asset_terms"""
        pass

    def test_match_containing_composition_id(self):
        """Tests match_containing_composition_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_containing_composition_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['_id'], {
            '$in': [test_id.identifier]
        })

    def test_clear_containing_composition_id_terms(self):
        """Tests clear_containing_composition_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_containing_composition_id(test_id, match=True)
        self.assertIn('_id',
                      self.query._query_terms)
        self.query.clear_containing_composition_id_terms()
        self.assertNotIn('_id',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_containing_composition_query(self):
        """Tests supports_containing_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_containing_composition_query(self):
        """Tests get_containing_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_containing_composition(self):
        """Tests match_any_containing_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_containing_composition_terms(self):
        """Tests clear_containing_composition_terms"""
        pass

    def test_match_contained_composition_id(self):
        """Tests match_contained_composition_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_contained_composition_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['childIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_contained_composition_id_terms(self):
        """Tests clear_contained_composition_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_contained_composition_id(test_id, match=True)
        self.assertIn('childIds',
                      self.query._query_terms)
        self.query.clear_contained_composition_id_terms()
        self.assertNotIn('childIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_contained_composition_query(self):
        """Tests supports_contained_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_contained_composition_query(self):
        """Tests get_contained_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_contained_composition(self):
        """Tests match_any_contained_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_contained_composition_terms(self):
        """Tests clear_contained_composition_terms"""
        pass

    def test_match_repository_id(self):
        """Tests match_repository_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedRepositoryIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_repository_id_terms(self):
        """Tests clear_repository_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)
        self.assertIn('assignedRepositoryIds',
                      self.query._query_terms)
        self.query.clear_repository_id_terms()
        self.assertNotIn('assignedRepositoryIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query(self):
        """Tests get_repository_query"""
        pass

    def test_clear_repository_terms(self):
        """Tests clear_repository_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['repository'] = 'foo'
        self.query.clear_repository_terms()
        self.assertNotIn('repository',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_composition_query_record(self):
        """Tests get_composition_query_record"""
        pass


class TestRepositoryQuery(unittest.TestCase):
    """Tests for RepositoryQuery"""

    @unittest.skip('unimplemented test')
    def test_match_asset_id(self):
        """Tests match_asset_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_id_terms(self):
        """Tests clear_asset_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_query(self):
        """Tests get_asset_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_asset(self):
        """Tests match_any_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_terms(self):
        """Tests clear_asset_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_composition_id(self):
        """Tests match_composition_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_composition_id_terms(self):
        """Tests clear_composition_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_composition_query(self):
        """Tests supports_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_query(self):
        """Tests get_composition_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_composition(self):
        """Tests match_any_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_composition_terms(self):
        """Tests clear_composition_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_repository_id(self):
        """Tests match_ancestor_repository_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_repository_id_terms(self):
        """Tests clear_ancestor_repository_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_repository_query(self):
        """Tests supports_ancestor_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_repository_query(self):
        """Tests get_ancestor_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_repository(self):
        """Tests match_any_ancestor_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_repository_terms(self):
        """Tests clear_ancestor_repository_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_repository_id(self):
        """Tests match_descendant_repository_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_repository_id_terms(self):
        """Tests clear_descendant_repository_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_repository_query(self):
        """Tests supports_descendant_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_repository_query(self):
        """Tests get_descendant_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_repository(self):
        """Tests match_any_descendant_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_repository_terms(self):
        """Tests clear_descendant_repository_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query_record(self):
        """Tests get_repository_query_record"""
        pass
