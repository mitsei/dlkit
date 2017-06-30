"""Unit tests of commenting searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("comment_search_class_fixture", "comment_search_test_fixture")
class TestCommentSearch(object):
    """Tests for CommentSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_comments(self):
        """Tests search_among_comments"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_comment_results(self):
        """Tests order_comment_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_comment_search_record(self):
        """Tests get_comment_search_record"""
        pass


@pytest.mark.usefixtures("comment_search_results_class_fixture", "comment_search_results_test_fixture")
class TestCommentSearchResults(object):
    """Tests for CommentSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_comments(self):
        """Tests get_comments"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_comment_query_inspector(self):
        """Tests get_comment_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_comment_search_results_record(self):
        """Tests get_comment_search_results_record"""
        pass


@pytest.mark.usefixtures("book_search_class_fixture", "book_search_test_fixture")
class TestBookSearch(object):
    """Tests for BookSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_books(self):
        """Tests search_among_books"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_book_results(self):
        """Tests order_book_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_book_search_record(self):
        """Tests get_book_search_record"""
        pass


@pytest.mark.usefixtures("book_search_results_class_fixture", "book_search_results_test_fixture")
class TestBookSearchResults(object):
    """Tests for BookSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_books(self):
        """Tests get_books"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_book_query_inspector(self):
        """Tests get_book_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_book_search_results_record(self):
        """Tests get_book_search_results_record"""
        pass
