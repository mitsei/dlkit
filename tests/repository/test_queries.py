"""Unit tests of repository queries."""


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


class TestAssetQuery(unittest.TestCase):
    """Tests for AssetQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        cls.query = cls.catalog.get_asset_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_title(self):
        """Tests match_title"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_title(self):
        """Tests match_any_title"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_title_terms(self):
        """Tests clear_title_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_public_domain(self):
        """Tests match_public_domain"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_public_domain(self):
        """Tests match_any_public_domain"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_public_domain_terms(self):
        """Tests clear_public_domain_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_copyright(self):
        """Tests match_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_copyright(self):
        """Tests match_any_copyright"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_copyright_terms(self):
        """Tests clear_copyright_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_copyright_registration(self):
        """Tests match_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_copyright_registration(self):
        """Tests match_any_copyright_registration"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_copyright_registration_terms(self):
        """Tests clear_copyright_registration_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_distribute_verbatim(self):
        """Tests match_distribute_verbatim"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_distribute_verbatim_terms(self):
        """Tests clear_distribute_verbatim_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_distribute_alterations(self):
        """Tests match_distribute_alterations"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_distribute_alterations_terms(self):
        """Tests clear_distribute_alterations_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_distribute_compositions(self):
        """Tests match_distribute_compositions"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_distribute_compositions_terms(self):
        """Tests clear_distribute_compositions_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_source_id(self):
        """Tests match_source_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_source_id_terms(self):
        """Tests clear_source_id_terms"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_clear_source_terms(self):
        """Tests clear_source_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_created_date(self):
        """Tests match_created_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_created_date(self):
        """Tests match_any_created_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_created_date_terms(self):
        """Tests clear_created_date_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_published(self):
        """Tests match_published"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_published_terms(self):
        """Tests clear_published_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_published_date(self):
        """Tests match_published_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_published_date(self):
        """Tests match_any_published_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_published_date_terms(self):
        """Tests clear_published_date_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_principal_credit_string(self):
        """Tests match_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_principal_credit_string(self):
        """Tests match_any_principal_credit_string"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_principal_credit_string_terms(self):
        """Tests clear_principal_credit_string_terms"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_match_location_id(self):
        """Tests match_location_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_location_id_terms(self):
        """Tests clear_location_id_terms"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_match_asset_content_id(self):
        """Tests match_asset_content_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_content_id_terms(self):
        """Tests clear_asset_content_id_terms"""
        pass

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
    def test_match_repository_id(self):
        """Tests match_repository_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_repository_id_terms(self):
        """Tests clear_repository_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query(self):
        """Tests get_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_repository_terms(self):
        """Tests clear_repository_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_query_record(self):
        """Tests get_asset_query_record"""
        pass


class TestAssetContentQuery(unittest.TestCase):
    """Tests for AssetContentQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        cls.query = cls.catalog.get_asset_content_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_accessibility_type(self):
        """Tests match_accessibility_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_accessibility_type(self):
        """Tests match_any_accessibility_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_accessibility_type_terms(self):
        """Tests clear_accessibility_type_terms"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_clear_data_terms(self):
        """Tests clear_data_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_url(self):
        """Tests match_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_url(self):
        """Tests match_any_url"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_url_terms(self):
        """Tests clear_url_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_content_query_record(self):
        """Tests get_asset_content_query_record"""
        pass


class TestCompositionQuery(unittest.TestCase):
    """Tests for CompositionQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        cls.query = cls.catalog.get_composition_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_repository(cls.catalog.ident)

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
    def test_match_containing_composition_id(self):
        """Tests match_containing_composition_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_containing_composition_id_terms(self):
        """Tests clear_containing_composition_id_terms"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_match_contained_composition_id(self):
        """Tests match_contained_composition_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_contained_composition_id_terms(self):
        """Tests clear_contained_composition_id_terms"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_match_repository_id(self):
        """Tests match_repository_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_repository_id_terms(self):
        """Tests clear_repository_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query(self):
        """Tests get_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_repository_terms(self):
        """Tests clear_repository_terms"""
        pass

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
