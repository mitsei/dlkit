"""Unit tests of commenting queries."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.osid import errors
from dlkit.json_.commenting.queries import BookQuery
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_query_class_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_query_test_fixture(request):
    # From test_templates/resource.py::ResourceQuery::init_template
    request.cls.query = request.cls.catalog.get_comment_query()


@pytest.mark.usefixtures("comment_query_class_fixture", "comment_query_test_fixture")
class TestCommentQuery(object):
    """Tests for CommentQuery"""
    def test_match_reference_id(self):
        """Tests match_reference_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'referenceId' not in self.query._query_terms
        self.query.match_reference_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['referenceId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_reference_id_terms(self):
        """Tests clear_reference_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_reference_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'referenceId' in self.query._query_terms
        self.query.clear_reference_id_terms()
        if is_no_authz(self.service_config):
            assert 'referenceId' not in self.query._query_terms

    def test_match_commentor_id(self):
        """Tests match_commentor_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'commentorId' not in self.query._query_terms
        self.query.match_commentor_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['commentorId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_commentor_id_terms(self):
        """Tests clear_commentor_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_commentor_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'commentorId' in self.query._query_terms
        self.query.clear_commentor_id_terms()
        if is_no_authz(self.service_config):
            assert 'commentorId' not in self.query._query_terms

    def test_supports_commentor_query(self):
        """Tests supports_commentor_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_commentor_query()

    def test_get_commentor_query(self):
        """Tests get_commentor_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_commentor_query()

    def test_clear_commentor_terms(self):
        """Tests clear_commentor_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['commentor'] = 'foo'
        self.query.clear_commentor_terms()
        if is_no_authz(self.service_config):
            assert 'commentor' not in self.query._query_terms

    def test_match_commenting_agent_id(self):
        """Tests match_commenting_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'commentingAgentId' not in self.query._query_terms
        self.query.match_commenting_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['commentingAgentId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_commenting_agent_id_terms(self):
        """Tests clear_commenting_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_commenting_agent_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'commentingAgentId' in self.query._query_terms
        self.query.clear_commenting_agent_id_terms()
        if is_no_authz(self.service_config):
            assert 'commentingAgentId' not in self.query._query_terms

    def test_supports_commenting_agent_query(self):
        """Tests supports_commenting_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_commenting_agent_query()

    def test_get_commenting_agent_query(self):
        """Tests get_commenting_agent_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_commenting_agent_query()

    def test_clear_commenting_agent_terms(self):
        """Tests clear_commenting_agent_terms"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.clear_commenting_agent_terms()

    def test_match_text(self):
        """Tests match_text"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_text(True, True, True)

    def test_match_any_text(self):
        """Tests match_any_text"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_text(True)

    def test_clear_text_terms(self):
        """Tests clear_text_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['text'] = 'foo'
        self.query.clear_text_terms()
        if is_no_authz(self.service_config):
            assert 'text' not in self.query._query_terms

    def test_match_rating_id(self):
        """Tests match_rating_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        if is_no_authz(self.service_config):
            assert 'ratingId' not in self.query._query_terms
        self.query.match_rating_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert self.query._query_terms['ratingId'] == {
                '$in': [str(test_id)]
            }

    def test_clear_rating_id_terms(self):
        """Tests clear_rating_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rating_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'ratingId' in self.query._query_terms
        self.query.clear_rating_id_terms()
        if is_no_authz(self.service_config):
            assert 'ratingId' not in self.query._query_terms

    def test_supports_rating_query(self):
        """Tests supports_rating_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_rating_query()

    def test_get_rating_query(self):
        """Tests get_rating_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_rating_query()

    def test_match_any_rating(self):
        """Tests match_any_rating"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_rating(True)

    def test_clear_rating_terms(self):
        """Tests clear_rating_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['rating'] = 'foo'
        self.query.clear_rating_terms()
        if is_no_authz(self.service_config):
            assert 'rating' not in self.query._query_terms

    def test_match_book_id(self):
        """Tests match_book_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_book_id(test_id, match=True)

        if is_no_authz(self.service_config):
            assert self.query._query_terms['assignedBookIds'] == {
                '$in': [str(test_id)]
            }

    def test_clear_book_id_terms(self):
        """Tests clear_book_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_book_id(test_id, match=True)
        if is_no_authz(self.service_config):
            assert 'assignedBookIds' in self.query._query_terms
        self.query.clear_book_id_terms()
        if is_no_authz(self.service_config):
            assert 'assignedBookIds' not in self.query._query_terms

    def test_supports_book_query(self):
        """Tests supports_book_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_book_query()

    def test_get_book_query(self):
        """Tests get_book_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_book_query()

    def test_clear_book_terms(self):
        """Tests clear_book_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['book'] = 'foo'
        self.query.clear_book_terms()
        if is_no_authz(self.service_config):
            assert 'book' not in self.query._query_terms

    def test_get_comment_query_record(self):
        """Tests get_comment_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_comment_query_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_query_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_query_test_fixture(request):
    # Since the session isn't implemented, we just construct an BookQuery directly
    if not is_never_authz(request.cls.service_config):
        request.cls.query = BookQuery(runtime=request.cls.catalog._runtime)


@pytest.mark.usefixtures("book_query_class_fixture", "book_query_test_fixture")
class TestBookQuery(object):
    """Tests for BookQuery"""
    def test_match_comment_id(self):
        """Tests match_comment_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_comment_id(True, True)

    def test_clear_comment_id_terms(self):
        """Tests clear_comment_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['commentId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_comment_id_terms()

        if is_no_authz(self.service_config):
            assert 'commentId' not in self.query._query_terms

    def test_supports_comment_query(self):
        """Tests supports_comment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_comment_query()

    def test_get_comment_query(self):
        """Tests get_comment_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_comment_query()

    def test_match_any_comment(self):
        """Tests match_any_comment"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_comment(True)

    def test_clear_comment_terms(self):
        """Tests clear_comment_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['comment'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_comment_terms()

        if is_no_authz(self.service_config):
            assert 'comment' not in self.query._query_terms

    def test_match_ancestor_book_id(self):
        """Tests match_ancestor_book_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_ancestor_book_id(True, True)

    def test_clear_ancestor_book_id_terms(self):
        """Tests clear_ancestor_book_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorBookId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_book_id_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorBookId' not in self.query._query_terms

    def test_supports_ancestor_book_query(self):
        """Tests supports_ancestor_book_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_ancestor_book_query()

    def test_get_ancestor_book_query(self):
        """Tests get_ancestor_book_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_ancestor_book_query()

    def test_match_any_ancestor_book(self):
        """Tests match_any_ancestor_book"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_ancestor_book(True)

    def test_clear_ancestor_book_terms(self):
        """Tests clear_ancestor_book_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['ancestorBook'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_ancestor_book_terms()

        if is_no_authz(self.service_config):
            assert 'ancestorBook' not in self.query._query_terms

    def test_match_descendant_book_id(self):
        """Tests match_descendant_book_id"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_descendant_book_id(True, True)

    def test_clear_descendant_book_id_terms(self):
        """Tests clear_descendant_book_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantBookId'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_book_id_terms()

        if is_no_authz(self.service_config):
            assert 'descendantBookId' not in self.query._query_terms

    def test_supports_descendant_book_query(self):
        """Tests supports_descendant_book_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.supports_descendant_book_query()

    def test_get_descendant_book_query(self):
        """Tests get_descendant_book_query"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_descendant_book_query()

    def test_match_any_descendant_book(self):
        """Tests match_any_descendant_book"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.match_any_descendant_book(True)

    def test_clear_descendant_book_terms(self):
        """Tests clear_descendant_book_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        if is_no_authz(self.service_config):
            self.query._query_terms['descendantBook'] = 'foo'

        if not is_never_authz(self.service_config):
            self.query.clear_descendant_book_terms()

        if is_no_authz(self.service_config):
            assert 'descendantBook' not in self.query._query_terms

    def test_get_book_query_record(self):
        """Tests get_book_query_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.query.get_book_query_record(True)
