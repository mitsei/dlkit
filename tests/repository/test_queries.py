"""Unit tests of repository queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.types.string import get_type_data as get_string_type_data
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


DEFAULT_STRING_MATCH_TYPE = Type(**get_string_type_data("WORDIGNORECASE"))
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_query_class_fixture(request):
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

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_query_test_fixture(request):
    request.cls.query = request.cls.catalog.get_asset_query()
    request.cls.start_date = DateTime.utcnow()
    request.cls.end_date = DateTime.utcnow()


@pytest.mark.usefixtures("asset_query_class_fixture", "asset_query_test_fixture")
class TestAssetQuery(object):
    """Tests for AssetQuery"""
    def test_match_title(self):
        """Tests match_title"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_title(True, True, True)

    def test_match_any_title(self):
        """Tests match_any_title"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_title(True)

    def test_clear_title_terms(self):
        """Tests clear_title_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['title'] = 'foo'
        self.query.clear_title_terms()
        if is_no_authz(self.service_config):
            assert 'title' not in self.query._query_terms

    def test_match_public_domain(self):
        """Tests match_public_domain"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_public_domain(True)

    def test_match_any_public_domain(self):
        """Tests match_any_public_domain"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_public_domain(True)

    def test_clear_public_domain_terms(self):
        """Tests clear_public_domain_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['publicDomain'] = 'foo'
        self.query.clear_public_domain_terms()
        if is_no_authz(self.service_config):
            assert 'publicDomain' not in self.query._query_terms

    def test_match_copyright(self):
        """Tests match_copyright"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_copyright(True, True, True)

    def test_match_any_copyright(self):
        """Tests match_any_copyright"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_copyright(True)

    def test_clear_copyright_terms(self):
        """Tests clear_copyright_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['copyright'] = 'foo'
        self.query.clear_copyright_terms()
        if is_no_authz(self.service_config):
            assert 'copyright' not in self.query._query_terms

    def test_match_copyright_registration(self):
        """Tests match_copyright_registration"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_copyright_registration(True, True, True)

    def test_match_any_copyright_registration(self):
        """Tests match_any_copyright_registration"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_copyright_registration(True)

    def test_clear_copyright_registration_terms(self):
        """Tests clear_copyright_registration_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['copyrightRegistration'] = 'foo'
        self.query.clear_copyright_registration_terms()
        if is_no_authz(self.service_config):
            assert 'copyrightRegistration' not in self.query._query_terms

    def test_match_distribute_verbatim(self):
        """Tests match_distribute_verbatim"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_distribute_verbatim(True)

    def test_clear_distribute_verbatim_terms(self):
        """Tests clear_distribute_verbatim_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['distributeVerbatim'] = 'foo'
        self.query.clear_distribute_verbatim_terms()
        if is_no_authz(self.service_config):
            assert 'distributeVerbatim' not in self.query._query_terms

    def test_match_distribute_alterations(self):
        """Tests match_distribute_alterations"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_distribute_alterations(True)

    def test_clear_distribute_alterations_terms(self):
        """Tests clear_distribute_alterations_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['distributeAlterations'] = 'foo'
        self.query.clear_distribute_alterations_terms()
        if is_no_authz(self.service_config):
            assert 'distributeAlterations' not in self.query._query_terms

    def test_match_distribute_compositions(self):
        """Tests match_distribute_compositions"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_distribute_compositions(True)

    def test_clear_distribute_compositions_terms(self):
        """Tests clear_distribute_compositions_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['distributeCompositions'] = 'foo'
        self.query.clear_distribute_compositions_terms()
        if is_no_authz(self.service_config):
            assert 'distributeCompositions' not in self.query._query_terms

    def test_match_source_id(self):
        """Tests match_source_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'sourceId' not in self.query._query_terms
        self.query.match_source_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['sourceId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_source_id_terms(self):
        """Tests clear_source_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_source_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'sourceId' in self.query._query_terms
        self.query.clear_source_id_terms()
        if is_no_authz(self.service_config):
            assert 'sourceId' not in self.query._query_terms

    def test_supports_source_query(self):
        """Tests supports_source_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_source_query()

    def test_get_source_query(self):
        """Tests get_source_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_source_query()

    def test_match_any_source(self):
        """Tests match_any_source"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_source(True)

    def test_clear_source_terms(self):
        """Tests clear_source_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['source'] = 'foo'
        self.query.clear_source_terms()
        if is_no_authz(self.service_config):
            assert 'source' not in self.query._query_terms

    def test_match_created_date(self):
        """Tests match_created_date"""
        if is_no_authz(self.service_config):
            assert 'createdDate' not in self.query._query_terms
        self.query.match_created_date(self.start_date, self.end_date, True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['createdDate'] == {
                '$gte': self.start_date,
                '$lte': self.end_date
            }

    def test_match_any_created_date(self):
        """Tests match_any_created_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_created_date(True)

    def test_clear_created_date_terms(self):
        """Tests clear_created_date_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['createdDate'] = 'foo'
        self.query.clear_created_date_terms()
        if is_no_authz(self.service_config):
            assert 'createdDate' not in self.query._query_terms

    def test_match_published(self):
        """Tests match_published"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_published(True)

    def test_clear_published_terms(self):
        """Tests clear_published_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['published'] = 'foo'
        self.query.clear_published_terms()
        if is_no_authz(self.service_config):
            assert 'published' not in self.query._query_terms

    def test_match_published_date(self):
        """Tests match_published_date"""
        if is_no_authz(self.service_config):
            assert 'publishedDate' not in self.query._query_terms
        self.query.match_published_date(self.start_date, self.end_date, True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['publishedDate'] == {
                '$gte': self.start_date,
                '$lte': self.end_date
            }

    def test_match_any_published_date(self):
        """Tests match_any_published_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_published_date(True)

    def test_clear_published_date_terms(self):
        """Tests clear_published_date_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['publishedDate'] = 'foo'
        self.query.clear_published_date_terms()
        if is_no_authz(self.service_config):
            assert 'publishedDate' not in self.query._query_terms

    def test_match_principal_credit_string(self):
        """Tests match_principal_credit_string"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_principal_credit_string(True, True, True)

    def test_match_any_principal_credit_string(self):
        """Tests match_any_principal_credit_string"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_principal_credit_string(True)

    def test_clear_principal_credit_string_terms(self):
        """Tests clear_principal_credit_string_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['principalCreditString'] = 'foo'
        self.query.clear_principal_credit_string_terms()
        if is_no_authz(self.service_config):
            assert 'principalCreditString' not in self.query._query_terms

    def test_match_temporal_coverage(self):
        """Tests match_temporal_coverage"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_temporal_coverage(True, True, True)

    def test_match_any_temporal_coverage(self):
        """Tests match_any_temporal_coverage"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_temporal_coverage(True)

    def test_clear_temporal_coverage_terms(self):
        """Tests clear_temporal_coverage_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_temporal_coverage_terms()

    def test_match_location_id(self):
        """Tests match_location_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'locationId' not in self.query._query_terms
        self.query.match_location_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['locationId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_location_id_terms(self):
        """Tests clear_location_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_location_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'locationId' in self.query._query_terms
        self.query.clear_location_id_terms()
        if is_no_authz(self.service_config):
            assert 'locationId' not in self.query._query_terms

    def test_supports_location_query(self):
        """Tests supports_location_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_location_query()

    def test_get_location_query(self):
        """Tests get_location_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_location_query()

    def test_match_any_location(self):
        """Tests match_any_location"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_location(True)

    def test_clear_location_terms(self):
        """Tests clear_location_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_location_terms()

    def test_match_spatial_coverage(self):
        """Tests match_spatial_coverage"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_spatial_coverage(True, True)

    def test_clear_spatial_coverage_terms(self):
        """Tests clear_spatial_coverage_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_spatial_coverage_terms()

    def test_match_spatial_coverage_overlap(self):
        """Tests match_spatial_coverage_overlap"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_spatial_coverage_overlap(True, True)

    def test_match_any_spatial_coverage(self):
        """Tests match_any_spatial_coverage"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_spatial_coverage(True)

    def test_clear_spatial_coverage_overlap_terms(self):
        """Tests clear_spatial_coverage_overlap_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_spatial_coverage_overlap_terms()

    def test_match_asset_content_id(self):
        """Tests match_asset_content_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'assetContentId' not in self.query._query_terms
        self.query.match_asset_content_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['assetContentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_asset_content_id_terms(self):
        """Tests clear_asset_content_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_content_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assetContentId' in self.query._query_terms
        self.query.clear_asset_content_id_terms()
        if is_no_authz(self.service_config):
            assert 'assetContentId' not in self.query._query_terms

    def test_supports_asset_content_query(self):
        """Tests supports_asset_content_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_asset_content_query()

    def test_get_asset_content_query(self):
        """Tests get_asset_content_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_asset_content_query()

    def test_match_any_asset_content(self):
        """Tests match_any_asset_content"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_asset_content(True)

    def test_clear_asset_content_terms(self):
        """Tests clear_asset_content_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_asset_content_terms()

    def test_match_composition_id(self):
        """Tests match_composition_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'compositionId' not in self.query._query_terms
        self.query.match_composition_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['compositionId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_composition_id_terms(self):
        """Tests clear_composition_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_composition_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'compositionId' in self.query._query_terms
        self.query.clear_composition_id_terms()
        if is_no_authz(self.service_config):
            assert 'compositionId' not in self.query._query_terms

    def test_supports_composition_query(self):
        """Tests supports_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_composition_query()

    def test_get_composition_query(self):
        """Tests get_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_composition_query()

    def test_match_any_composition(self):
        """Tests match_any_composition"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_composition(True)

    def test_clear_composition_terms(self):
        """Tests clear_composition_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['composition'] = 'foo'
        self.query.clear_composition_terms()
        if is_no_authz(self.service_config):
            assert 'composition' not in self.query._query_terms

    def test_match_repository_id(self):
        """Tests match_repository_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedRepositoryIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_repository_id_terms(self):
        """Tests clear_repository_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedRepositoryIds' in self.query._query_terms
        self.query.clear_repository_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedRepositoryIds' not in self.query._query_terms

    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_repository_query()

    def test_get_repository_query(self):
        """Tests get_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_repository_query()

    def test_clear_repository_terms(self):
        """Tests clear_repository_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['repository'] = 'foo'
        self.query.clear_repository_terms()
        if is_no_authz(self.service_config):
            assert 'repository' not in self.query._query_terms

    def test_get_asset_query_record(self):
        """Tests get_asset_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_asset_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def asset_content_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def asset_content_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_asset_content_query()


@pytest.mark.usefixtures("asset_content_query_class_fixture", "asset_content_query_test_fixture")
class TestAssetContentQuery(object):
    """Tests for AssetContentQuery"""
    def test_match_accessibility_type(self):
        """Tests match_accessibility_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_accessibility_type(True, True)

    def test_match_any_accessibility_type(self):
        """Tests match_any_accessibility_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_accessibility_type(True)

    def test_clear_accessibility_type_terms(self):
        """Tests clear_accessibility_type_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['accessibilityType'] = 'foo'
        self.query.clear_accessibility_type_terms()
        if is_no_authz(self.service_config):
            assert 'accessibilityType' not in self.query._query_terms

    def test_match_data_length(self):
        """Tests match_data_length"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_data_length(True, True, True)

    def test_match_any_data_length(self):
        """Tests match_any_data_length"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_data_length(True)

    def test_clear_data_length_terms(self):
        """Tests clear_data_length_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_data_length_terms()

    def test_match_data(self):
        """Tests match_data"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_data(True, True, True)

    def test_match_any_data(self):
        """Tests match_any_data"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_data(True)

    def test_clear_data_terms(self):
        """Tests clear_data_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['data'] = 'foo'
        self.query.clear_data_terms()
        if is_no_authz(self.service_config):
            assert 'data' not in self.query._query_terms

    def test_match_url(self):
        """Tests match_url"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_url(True, True, True)

    def test_match_any_url(self):
        """Tests match_any_url"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_url(True)

    def test_clear_url_terms(self):
        """Tests clear_url_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['url'] = 'foo'
        self.query.clear_url_terms()
        if is_no_authz(self.service_config):
            assert 'url' not in self.query._query_terms

    def test_get_asset_content_query_record(self):
        """Tests get_asset_content_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_asset_content_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def composition_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
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

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_repository(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def composition_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_composition_query()


@pytest.mark.usefixtures("composition_query_class_fixture", "composition_query_test_fixture")
class TestCompositionQuery(object):
    """Tests for CompositionQuery"""
    def test_match_asset_id(self):
        """Tests match_asset_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_id(test_id, match=True)
        assert self.query._query_terms['assetIds'] == {
            '$in': [str(test_id)]
        }

    def test_clear_asset_id_terms(self):
        """Tests clear_asset_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_asset_id(test_id, match=True)
        assert 'assetIds' in self.query._query_terms
        self.query.clear_asset_id_terms()
        assert 'assetIds' not in self.query._query_terms

    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_asset_query()

    def test_get_asset_query(self):
        """Tests get_asset_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_asset_query()

    def test_match_any_asset(self):
        """Tests match_any_asset"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_asset(True)

    def test_clear_asset_terms(self):
        """Tests clear_asset_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_asset_terms()

    def test_match_containing_composition_id(self):
        """Tests match_containing_composition_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_containing_composition_id(test_id, match=True)
        assert self.query._query_terms['_id'] == {
            '$in': [test_id.identifier]
        }

    def test_clear_containing_composition_id_terms(self):
        """Tests clear_containing_composition_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_containing_composition_id(test_id, match=True)
        assert '_id' in self.query._query_terms
        self.query.clear_containing_composition_id_terms()
        assert '_id' not in self.query._query_terms

    def test_supports_containing_composition_query(self):
        """Tests supports_containing_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_containing_composition_query()

    def test_get_containing_composition_query(self):
        """Tests get_containing_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_containing_composition_query()

    def test_match_any_containing_composition(self):
        """Tests match_any_containing_composition"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_containing_composition(True)

    def test_clear_containing_composition_terms(self):
        """Tests clear_containing_composition_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_containing_composition_terms()

    def test_match_contained_composition_id(self):
        """Tests match_contained_composition_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_contained_composition_id(test_id, match=True)
        assert self.query._query_terms['childIds'] == {
            '$in': [str(test_id)]
        }

    def test_clear_contained_composition_id_terms(self):
        """Tests clear_contained_composition_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_contained_composition_id(test_id, match=True)
        assert 'childIds' in self.query._query_terms
        self.query.clear_contained_composition_id_terms()
        assert 'childIds' not in self.query._query_terms

    def test_supports_contained_composition_query(self):
        """Tests supports_contained_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_contained_composition_query()

    def test_get_contained_composition_query(self):
        """Tests get_contained_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_contained_composition_query()

    def test_match_any_contained_composition(self):
        """Tests match_any_contained_composition"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_contained_composition(True)

    def test_clear_contained_composition_terms(self):
        """Tests clear_contained_composition_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_contained_composition_terms()

    def test_match_repository_id(self):
        """Tests match_repository_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedRepositoryIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_repository_id_terms(self):
        """Tests clear_repository_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_repository_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedRepositoryIds' in self.query._query_terms
        self.query.clear_repository_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedRepositoryIds' not in self.query._query_terms

    def test_supports_repository_query(self):
        """Tests supports_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_repository_query()

    def test_get_repository_query(self):
        """Tests get_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_repository_query()

    def test_clear_repository_terms(self):
        """Tests clear_repository_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['repository'] = 'foo'
        self.query.clear_repository_terms()
        if is_no_authz(self.service_config):
            assert 'repository' not in self.query._query_terms

    def test_get_composition_query_record(self):
        """Tests get_composition_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_composition_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def repository_query_class_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
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
def repository_query_test_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.svc_mgr.get_repository_query()


@pytest.mark.usefixtures("repository_query_class_fixture", "repository_query_test_fixture")
class TestRepositoryQuery(object):
    """Tests for RepositoryQuery"""
    def test_match_asset_id(self):
        """Tests match_asset_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_asset_id(True, True)

    def test_clear_asset_id_terms(self):
        """Tests clear_asset_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['assetId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_asset_id_terms()

        if is_no_authz(self.service_config):
            assert 'assetId' not in self.query._query_terms

    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_asset_query()

    def test_get_asset_query(self):
        """Tests get_asset_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_asset_query()

    def test_match_any_asset(self):
        """Tests match_any_asset"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_asset(True)

    def test_clear_asset_terms(self):
        """Tests clear_asset_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['asset'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_asset_terms()

        if is_no_authz(self.service_config):
            assert 'asset' not in self.query._query_terms

    def test_match_composition_id(self):
        """Tests match_composition_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_composition_id(True, True)

    def test_clear_composition_id_terms(self):
        """Tests clear_composition_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['compositionId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_composition_id_terms()

        if is_no_authz(self.service_config):
            assert 'compositionId' not in self.query._query_terms

    def test_supports_composition_query(self):
        """Tests supports_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_composition_query()

    def test_get_composition_query(self):
        """Tests get_composition_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_composition_query()

    def test_match_any_composition(self):
        """Tests match_any_composition"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_composition(True)

    def test_clear_composition_terms(self):
        """Tests clear_composition_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['composition'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_composition_terms()

        if is_no_authz(self.service_config):
            assert 'composition' not in self.query._query_terms

    def test_match_ancestor_repository_id(self):
        """Tests match_ancestor_repository_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_repository_id(True, True)

    def test_clear_ancestor_repository_id_terms(self):
        """Tests clear_ancestor_repository_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorRepositoryId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_repository_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorRepositoryId' not in self.query._query_terms

    def test_supports_ancestor_repository_query(self):
        """Tests supports_ancestor_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_repository_query()

    def test_get_ancestor_repository_query(self):
        """Tests get_ancestor_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_repository_query()

    def test_match_any_ancestor_repository(self):
        """Tests match_any_ancestor_repository"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_repository(True)

    def test_clear_ancestor_repository_terms(self):
        """Tests clear_ancestor_repository_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorRepository'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_repository_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorRepository' not in self.query._query_terms

    def test_match_descendant_repository_id(self):
        """Tests match_descendant_repository_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_repository_id(True, True)

    def test_clear_descendant_repository_id_terms(self):
        """Tests clear_descendant_repository_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantRepositoryId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_repository_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantRepositoryId' not in self.query._query_terms

    def test_supports_descendant_repository_query(self):
        """Tests supports_descendant_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_repository_query()

    def test_get_descendant_repository_query(self):
        """Tests get_descendant_repository_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_repository_query()

    def test_match_any_descendant_repository(self):
        """Tests match_any_descendant_repository"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_repository(True)

    def test_clear_descendant_repository_terms(self):
        """Tests clear_descendant_repository_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantRepository'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_repository_terms()

        if is_no_authz(self.service_config):
            assert 'descendantRepository' not in self.query._query_terms

    def test_get_repository_query_record(self):
        """Tests get_repository_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_repository_query_record(True)
