"""Unit tests of resource searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("resource_search_class_fixture", "resource_search_test_fixture")
class TestResourceSearch(object):
    """Tests for ResourceSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_resources(self):
        """Tests search_among_resources"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_resource_results(self):
        """Tests order_resource_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_resource_search_record(self):
        """Tests get_resource_search_record"""
        pass


@pytest.mark.usefixtures("resource_search_results_class_fixture", "resource_search_results_test_fixture")
class TestResourceSearchResults(object):
    """Tests for ResourceSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_resources(self):
        """Tests get_resources"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_resource_query_inspector(self):
        """Tests get_resource_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_resource_search_results_record(self):
        """Tests get_resource_search_results_record"""
        pass


@pytest.mark.usefixtures("bin_search_class_fixture", "bin_search_test_fixture")
class TestBinSearch(object):
    """Tests for BinSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_bins(self):
        """Tests search_among_bins"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_bin_results(self):
        """Tests order_bin_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bin_search_record(self):
        """Tests get_bin_search_record"""
        pass


@pytest.mark.usefixtures("bin_search_results_class_fixture", "bin_search_results_test_fixture")
class TestBinSearchResults(object):
    """Tests for BinSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_bins(self):
        """Tests get_bins"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bin_query_inspector(self):
        """Tests get_bin_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_bin_search_results_record(self):
        """Tests get_bin_search_results_record"""
        pass
