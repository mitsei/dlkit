"""Unit tests of commenting queries."""


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


class TestCommentQuery(unittest.TestCase):
    """Tests for CommentQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('COMMENTING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_book(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_comment_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_book(cls.catalog.ident)

    def test_match_reference_id(self):
        """Tests match_reference_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_reference_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['referenceId'], {
            '$in': [str(test_id)]
        })

    def test_clear_reference_id_terms(self):
        """Tests clear_reference_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_reference_id(test_id, match=True)
        self.assertIn('referenceId',
                      self.query._query_terms)
        self.query.clear_reference_id_terms()
        self.assertNotIn('referenceId',
                         self.query._query_terms)

    def test_match_commentor_id(self):
        """Tests match_commentor_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_commentor_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['commentorId'], {
            '$in': [str(test_id)]
        })

    def test_clear_commentor_id_terms(self):
        """Tests clear_commentor_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_commentor_id(test_id, match=True)
        self.assertIn('commentorId',
                      self.query._query_terms)
        self.query.clear_commentor_id_terms()
        self.assertNotIn('commentorId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_commentor_query(self):
        """Tests supports_commentor_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commentor_query(self):
        """Tests get_commentor_query"""
        pass

    def test_clear_commentor_terms(self):
        """Tests clear_commentor_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['commentor'] = 'foo'
        self.query.clear_commentor_terms()
        self.assertNotIn('commentor',
                         self.query._query_terms)

    def test_match_commenting_agent_id(self):
        """Tests match_commenting_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_commenting_agent_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['commentingAgentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_commenting_agent_id_terms(self):
        """Tests clear_commenting_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_commenting_agent_id(test_id, match=True)
        self.assertIn('commentingAgentId',
                      self.query._query_terms)
        self.query.clear_commenting_agent_id_terms()
        self.assertNotIn('commentingAgentId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_commenting_agent_query(self):
        """Tests supports_commenting_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_commenting_agent_query(self):
        """Tests get_commenting_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_commenting_agent_terms(self):
        """Tests clear_commenting_agent_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_text(self):
        """Tests match_text"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_text(self):
        """Tests match_any_text"""
        pass

    def test_clear_text_terms(self):
        """Tests clear_text_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['text'] = 'foo'
        self.query.clear_text_terms()
        self.assertNotIn('text',
                         self.query._query_terms)

    def test_match_rating_id(self):
        """Tests match_rating_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rating_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['ratingId'], {
            '$in': [str(test_id)]
        })

    def test_clear_rating_id_terms(self):
        """Tests clear_rating_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rating_id(test_id, match=True)
        self.assertIn('ratingId',
                      self.query._query_terms)
        self.query.clear_rating_id_terms()
        self.assertNotIn('ratingId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_rating_query(self):
        """Tests supports_rating_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rating_query(self):
        """Tests get_rating_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_rating(self):
        """Tests match_any_rating"""
        pass

    def test_clear_rating_terms(self):
        """Tests clear_rating_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['rating'] = 'foo'
        self.query.clear_rating_terms()
        self.assertNotIn('rating',
                         self.query._query_terms)

    def test_match_book_id(self):
        """Tests match_book_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_book_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedBookIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_book_id_terms(self):
        """Tests clear_book_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_book_id(test_id, match=True)
        self.assertIn('assignedBookIds',
                      self.query._query_terms)
        self.query.clear_book_id_terms()
        self.assertNotIn('assignedBookIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_book_query(self):
        """Tests supports_book_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_book_query(self):
        """Tests get_book_query"""
        pass

    def test_clear_book_terms(self):
        """Tests clear_book_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['book'] = 'foo'
        self.query.clear_book_terms()
        self.assertNotIn('book',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_comment_query_record(self):
        """Tests get_comment_query_record"""
        pass


class TestBookQuery(unittest.TestCase):
    """Tests for BookQuery"""

    @unittest.skip('unimplemented test')
    def test_match_comment_id(self):
        """Tests match_comment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_comment_id_terms(self):
        """Tests clear_comment_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_comment_query(self):
        """Tests supports_comment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_comment_query(self):
        """Tests get_comment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_comment(self):
        """Tests match_any_comment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_comment_terms(self):
        """Tests clear_comment_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_book_id(self):
        """Tests match_ancestor_book_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_book_id_terms(self):
        """Tests clear_ancestor_book_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_book_query(self):
        """Tests supports_ancestor_book_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_book_query(self):
        """Tests get_ancestor_book_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_book(self):
        """Tests match_any_ancestor_book"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_book_terms(self):
        """Tests clear_ancestor_book_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_book_id(self):
        """Tests match_descendant_book_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_book_id_terms(self):
        """Tests clear_descendant_book_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_book_query(self):
        """Tests supports_descendant_book_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_book_query(self):
        """Tests get_descendant_book_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_book(self):
        """Tests match_any_descendant_book"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_book_terms(self):
        """Tests clear_descendant_book_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_book_query_record(self):
        """Tests get_book_query_record"""
        pass
