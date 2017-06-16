"""Unit tests of logging searches."""


import unittest


class TestLogEntrySearch(unittest.TestCase):
    """Tests for LogEntrySearch"""

    def test_search_among_log_entries(self):
        """Tests search_among_log_entries"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_log_entries(True)

    def test_order_log_entry_results(self):
        """Tests order_log_entry_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_log_entry_results(True)

    def test_get_log_entry_search_record(self):
        """Tests get_log_entry_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_entry_search_record(True)


class TestLogEntrySearchResults(unittest.TestCase):
    """Tests for LogEntrySearchResults"""

    def test_get_log_entries(self):
        """Tests get_log_entries"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_entries()

    def test_get_log_entry_query_inspector(self):
        """Tests get_log_entry_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_entry_query_inspector()

    def test_get_log_entry_search_results_record(self):
        """Tests get_log_entry_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_entry_search_results_record(True)


class TestLogSearch(unittest.TestCase):
    """Tests for LogSearch"""

    def test_search_among_logs(self):
        """Tests search_among_logs"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_logs(True)

    def test_order_log_results(self):
        """Tests order_log_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_log_results(True)

    def test_get_log_search_record(self):
        """Tests get_log_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_search_record(True)


class TestLogSearchResults(unittest.TestCase):
    """Tests for LogSearchResults"""

    def test_get_logs(self):
        """Tests get_logs"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_logs()

    def test_get_log_query_inspector(self):
        """Tests get_log_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_query_inspector()

    def test_get_log_search_results_record(self):
        """Tests get_log_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_log_search_results_record(True)
