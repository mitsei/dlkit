"""Unit tests of repository searches."""


import unittest


class TestAssetSearch(unittest.TestCase):
    """Tests for AssetSearch"""

    def test_search_among_assets(self):
        """Tests search_among_assets"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_assets(True)

    def test_order_asset_results(self):
        """Tests order_asset_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_asset_results(True)

    def test_get_asset_search_record(self):
        """Tests get_asset_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_asset_search_record(True)


class TestAssetSearchResults(unittest.TestCase):
    """Tests for AssetSearchResults"""

    def test_get_assets(self):
        """Tests get_assets"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_assets()

    def test_get_asset_query_inspector(self):
        """Tests get_asset_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_asset_query_inspector()

    def test_get_asset_search_results_record(self):
        """Tests get_asset_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_asset_search_results_record(True)


class TestCompositionSearch(unittest.TestCase):
    """Tests for CompositionSearch"""

    def test_search_among_compositions(self):
        """Tests search_among_compositions"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_compositions(True)

    def test_order_composition_results(self):
        """Tests order_composition_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_composition_results(True)

    def test_get_composition_search_record(self):
        """Tests get_composition_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_composition_search_record(True)


class TestCompositionSearchResults(unittest.TestCase):
    """Tests for CompositionSearchResults"""

    def test_get_compositions(self):
        """Tests get_compositions"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_compositions()

    def test_get_composition_query_inspector(self):
        """Tests get_composition_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_composition_query_inspector()

    def test_get_composition_search_results_record(self):
        """Tests get_composition_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_composition_search_results_record(True)


class TestRepositorySearch(unittest.TestCase):
    """Tests for RepositorySearch"""

    def test_search_among_repositories(self):
        """Tests search_among_repositories"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_repositories(True)

    def test_order_repository_results(self):
        """Tests order_repository_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_repository_results(True)

    def test_get_repository_search_record(self):
        """Tests get_repository_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_repository_search_record(True)


class TestRepositorySearchResults(unittest.TestCase):
    """Tests for RepositorySearchResults"""

    def test_get_repositories(self):
        """Tests get_repositories"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_repositories()

    def test_get_repository_query_inspector(self):
        """Tests get_repository_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_repository_query_inspector()

    def test_get_repository_search_results_record(self):
        """Tests get_repository_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_repository_search_results_record(True)
