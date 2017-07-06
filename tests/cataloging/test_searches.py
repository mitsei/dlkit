"""Unit tests of cataloging searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("catalog_search_class_fixture", "catalog_search_test_fixture")
class TestCatalogSearch(object):
    """Tests for CatalogSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_catalogs(self):
        """Tests search_among_catalogs"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_catalog_results(self):
        """Tests order_catalog_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_catalog_search_record(self):
        """Tests get_catalog_search_record"""
        pass


@pytest.mark.usefixtures("catalog_search_results_class_fixture", "catalog_search_results_test_fixture")
class TestCatalogSearchResults(object):
    """Tests for CatalogSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_catalogs(self):
        """Tests get_catalogs"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_catalog_query_inspector(self):
        """Tests get_catalog_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_catalog_search_results_record(self):
        """Tests get_catalog_search_results_record"""
        pass
