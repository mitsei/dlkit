"""Unit tests of commenting objects."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestComment(unittest.TestCase):
    """Tests for Comment"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_book(create_form)

        form = cls.catalog.get_comment_form_for_create(
            Id('resource.Resource%3A1%40ODL.MIT.EDU'),
            [])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_comment(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_comments():
            cls.catalog.delete_comment(obj.ident)
        cls.svc_mgr.delete_book(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_reference_id(self):
        """Tests get_reference_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commentor_id(self):
        """Tests get_commentor_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commentor(self):
        """Tests get_commentor"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commenting_agent_id(self):
        """Tests get_commenting_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commenting_agent(self):
        """Tests get_commenting_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_text(self):
        """Tests get_text"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_rating(self):
        """Tests has_rating"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rating_id(self):
        """Tests get_rating_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rating(self):
        """Tests get_rating"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comment_record(self):
        """Tests get_comment_record"""
        pass


class TestCommentForm(unittest.TestCase):
    """Tests for CommentForm"""

    @unittest.skip('unimplemented test')
    def test_get_text_metadata(self):
        """Tests get_text_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_text(self):
        """Tests set_text"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_text(self):
        """Tests clear_text"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rating_metadata(self):
        """Tests get_rating_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_rating(self):
        """Tests set_rating"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rating(self):
        """Tests clear_rating"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comment_form_record(self):
        """Tests get_comment_form_record"""
        pass


class TestCommentList(unittest.TestCase):
    """Tests for CommentList"""

    @unittest.skip('unimplemented test')
    def test_get_next_comment(self):
        """Tests get_next_comment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_comments(self):
        """Tests get_next_comments"""
        pass


class TestBook(unittest.TestCase):
    """Tests for Book"""

    @unittest.skip('unimplemented test')
    def test_get_book_record(self):
        """Tests get_book_record"""
        pass


class TestBookForm(unittest.TestCase):
    """Tests for BookForm"""

    @unittest.skip('unimplemented test')
    def test_get_book_form_record(self):
        """Tests get_book_form_record"""
        pass


class TestBookList(unittest.TestCase):
    """Tests for BookList"""

    @unittest.skip('unimplemented test')
    def test_get_next_book(self):
        """Tests get_next_book"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_books(self):
        """Tests get_next_books"""
        pass


class TestBookNode(unittest.TestCase):
    """Tests for BookNode"""

    @unittest.skip('unimplemented test')
    def test_get_book(self):
        """Tests get_book"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_book_nodes(self):
        """Tests get_parent_book_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_book_nodes(self):
        """Tests get_child_book_nodes"""
        pass


class TestBookNodeList(unittest.TestCase):
    """Tests for BookNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_book_node(self):
        """Tests get_next_book_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_book_nodes(self):
        """Tests get_next_book_nodes"""
        pass
