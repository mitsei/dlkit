"""Unit tests of commenting searches."""


import unittest


class TestCommentSearch(unittest.TestCase):
    """Tests for CommentSearch"""

    def test_search_among_comments(self):
        """Tests search_among_comments"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_comments(True)

    def test_order_comment_results(self):
        """Tests order_comment_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_comment_results(True)

    def test_get_comment_search_record(self):
        """Tests get_comment_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_comment_search_record(True)


class TestCommentSearchResults(unittest.TestCase):
    """Tests for CommentSearchResults"""

    def test_get_comments(self):
        """Tests get_comments"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_comments()

    def test_get_comment_query_inspector(self):
        """Tests get_comment_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_comment_query_inspector()

    def test_get_comment_search_results_record(self):
        """Tests get_comment_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_comment_search_results_record(True)


class TestBookSearch(unittest.TestCase):
    """Tests for BookSearch"""

    def test_search_among_books(self):
        """Tests search_among_books"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_books(True)

    def test_order_book_results(self):
        """Tests order_book_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_book_results(True)

    def test_get_book_search_record(self):
        """Tests get_book_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_book_search_record(True)


class TestBookSearchResults(unittest.TestCase):
    """Tests for BookSearchResults"""

    def test_get_books(self):
        """Tests get_books"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_books()

    def test_get_book_query_inspector(self):
        """Tests get_book_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_book_query_inspector()

    def test_get_book_search_results_record(self):
        """Tests get_book_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_book_search_results_record(True)
