"""Unit tests of logging searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("log_entry_search_class_fixture", "log_entry_search_test_fixture")
class TestLogEntrySearch(object):
    """Tests for LogEntrySearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_log_entries(self):
        """Tests search_among_log_entries"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_log_entry_results(self):
        """Tests order_log_entry_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_log_entry_search_record(self):
        """Tests get_log_entry_search_record"""
        pass


@pytest.mark.usefixtures("log_entry_search_results_class_fixture", "log_entry_search_results_test_fixture")
class TestLogEntrySearchResults(object):
    """Tests for LogEntrySearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_log_entries(self):
        """Tests get_log_entries"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_log_entry_query_inspector(self):
        """Tests get_log_entry_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_log_entry_search_results_record(self):
        """Tests get_log_entry_search_results_record"""
        pass


@pytest.mark.usefixtures("log_search_class_fixture", "log_search_test_fixture")
class TestLogSearch(object):
    """Tests for LogSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_logs(self):
        """Tests search_among_logs"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_log_results(self):
        """Tests order_log_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_log_search_record(self):
        """Tests get_log_search_record"""
        pass


@pytest.mark.usefixtures("log_search_results_class_fixture", "log_search_results_test_fixture")
class TestLogSearchResults(object):
    """Tests for LogSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_logs(self):
        """Tests get_logs"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_log_query_inspector(self):
        """Tests get_log_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_log_search_results_record(self):
        """Tests get_log_search_results_record"""
        pass
