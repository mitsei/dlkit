"""Unit tests of commenting records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("comment_record_class_fixture", "comment_record_test_fixture")
class TestCommentRecord(object):
    """Tests for CommentRecord"""


@pytest.mark.usefixtures("comment_query_record_class_fixture", "comment_query_record_test_fixture")
class TestCommentQueryRecord(object):
    """Tests for CommentQueryRecord"""


@pytest.mark.usefixtures("comment_form_record_class_fixture", "comment_form_record_test_fixture")
class TestCommentFormRecord(object):
    """Tests for CommentFormRecord"""


@pytest.mark.usefixtures("comment_search_record_class_fixture", "comment_search_record_test_fixture")
class TestCommentSearchRecord(object):
    """Tests for CommentSearchRecord"""


@pytest.mark.usefixtures("book_record_class_fixture", "book_record_test_fixture")
class TestBookRecord(object):
    """Tests for BookRecord"""


@pytest.mark.usefixtures("book_query_record_class_fixture", "book_query_record_test_fixture")
class TestBookQueryRecord(object):
    """Tests for BookQueryRecord"""


@pytest.mark.usefixtures("book_form_record_class_fixture", "book_form_record_test_fixture")
class TestBookFormRecord(object):
    """Tests for BookFormRecord"""


@pytest.mark.usefixtures("book_search_record_class_fixture", "book_search_record_test_fixture")
class TestBookSearchRecord(object):
    """Tests for BookSearchRecord"""
