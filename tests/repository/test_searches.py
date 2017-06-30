"""Unit tests of repository searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("asset_search_class_fixture", "asset_search_test_fixture")
class TestAssetSearch(object):
    """Tests for AssetSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assets(self):
        """Tests search_among_assets"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_asset_results(self):
        """Tests order_asset_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_asset_search_record(self):
        """Tests get_asset_search_record"""
        pass


@pytest.mark.usefixtures("asset_search_results_class_fixture", "asset_search_results_test_fixture")
class TestAssetSearchResults(object):
    """Tests for AssetSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assets(self):
        """Tests get_assets"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_asset_query_inspector(self):
        """Tests get_asset_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_asset_search_results_record(self):
        """Tests get_asset_search_results_record"""
        pass


@pytest.mark.usefixtures("composition_search_class_fixture", "composition_search_test_fixture")
class TestCompositionSearch(object):
    """Tests for CompositionSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_compositions(self):
        """Tests search_among_compositions"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_composition_results(self):
        """Tests order_composition_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_composition_search_record(self):
        """Tests get_composition_search_record"""
        pass


@pytest.mark.usefixtures("composition_search_results_class_fixture", "composition_search_results_test_fixture")
class TestCompositionSearchResults(object):
    """Tests for CompositionSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_compositions(self):
        """Tests get_compositions"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_composition_query_inspector(self):
        """Tests get_composition_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_composition_search_results_record(self):
        """Tests get_composition_search_results_record"""
        pass


@pytest.mark.usefixtures("repository_search_class_fixture", "repository_search_test_fixture")
class TestRepositorySearch(object):
    """Tests for RepositorySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_repositories(self):
        """Tests search_among_repositories"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_repository_results(self):
        """Tests order_repository_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_repository_search_record(self):
        """Tests get_repository_search_record"""
        pass


@pytest.mark.usefixtures("repository_search_results_class_fixture", "repository_search_results_test_fixture")
class TestRepositorySearchResults(object):
    """Tests for RepositorySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_repositories(self):
        """Tests get_repositories"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_repository_query_inspector(self):
        """Tests get_repository_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_repository_search_results_record(self):
        """Tests get_repository_search_results_record"""
        pass
