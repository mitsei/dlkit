"""Unit tests of resource searches."""


import unittest


class TestResourceSearch(unittest.TestCase):
    """Tests for ResourceSearch"""

    def test_search_among_resources(self):
        """Tests search_among_resources"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_resources(True)

    def test_order_resource_results(self):
        """Tests order_resource_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_resource_results(True)

    def test_get_resource_search_record(self):
        """Tests get_resource_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_resource_search_record(True)


class TestResourceSearchResults(unittest.TestCase):
    """Tests for ResourceSearchResults"""

    def test_get_resources(self):
        """Tests get_resources"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_resources()

    def test_get_resource_query_inspector(self):
        """Tests get_resource_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_resource_query_inspector()

    def test_get_resource_search_results_record(self):
        """Tests get_resource_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_resource_search_results_record(True)


class TestBinSearch(unittest.TestCase):
    """Tests for BinSearch"""

    def test_search_among_bins(self):
        """Tests search_among_bins"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_bins(True)

    def test_order_bin_results(self):
        """Tests order_bin_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_bin_results(True)

    def test_get_bin_search_record(self):
        """Tests get_bin_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_bin_search_record(True)


class TestBinSearchResults(unittest.TestCase):
    """Tests for BinSearchResults"""

    def test_get_bins(self):
        """Tests get_bins"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_bins()

    def test_get_bin_query_inspector(self):
        """Tests get_bin_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_bin_query_inspector()

    def test_get_bin_search_results_record(self):
        """Tests get_bin_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_bin_search_results_record(True)
