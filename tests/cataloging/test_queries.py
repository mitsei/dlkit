"""Unit tests of cataloging queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
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


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def catalog_query_class_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
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
def catalog_query_test_fixture(request):
    # From test_templates/resource.py::BinQuery::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.query = request.cls.svc_mgr.get_catalog_query()


@pytest.mark.usefixtures("catalog_query_class_fixture", "catalog_query_test_fixture")
class TestCatalogQuery(object):
    """Tests for CatalogQuery"""
    def test_match_id(self):
        """Tests match_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_id(True, True)

    def test_match_any_id(self):
        """Tests match_any_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_id(True)

    def test_clear_id_terms(self):
        """Tests clear_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['id'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_id_terms()

        if is_no_authz(self.service_config):
            assert 'id' not in self.query._query_terms

    def test_match_ancestor_catalog_id(self):
        """Tests match_ancestor_catalog_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_catalog_id(True, True)

    def test_clear_ancestor_catalog_id_terms(self):
        """Tests clear_ancestor_catalog_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorCatalogId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_catalog_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorCatalogId' not in self.query._query_terms

    def test_supports_ancestor_catalog_query(self):
        """Tests supports_ancestor_catalog_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_catalog_query()

    def test_get_ancestor_catalog_query(self):
        """Tests get_ancestor_catalog_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_catalog_query()

    def test_match_any_ancestor_catalog(self):
        """Tests match_any_ancestor_catalog"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_catalog(True)

    def test_clear_ancestor_catalog_terms(self):
        """Tests clear_ancestor_catalog_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorCatalog'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_catalog_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorCatalog' not in self.query._query_terms

    def test_match_descendant_catalog_id(self):
        """Tests match_descendant_catalog_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_catalog_id(True, True)

    def test_clear_descendant_catalog_id_terms(self):
        """Tests clear_descendant_catalog_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantCatalogId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_catalog_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantCatalogId' not in self.query._query_terms

    def test_supports_descendant_catalog_query(self):
        """Tests supports_descendant_catalog_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_catalog_query()

    def test_get_descendant_catalog_query(self):
        """Tests get_descendant_catalog_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_catalog_query()

    def test_match_any_descendant_catalog(self):
        """Tests match_any_descendant_catalog"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_catalog(True)

    def test_clear_descendant_catalog_terms(self):
        """Tests clear_descendant_catalog_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantCatalog'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_catalog_terms()

        if is_no_authz(self.service_config):
            assert 'descendantCatalog' not in self.query._query_terms

    def test_get_catalog_query_record(self):
        """Tests get_catalog_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_catalog_query_record(True)
