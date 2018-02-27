"""Unit tests of commenting sessions."""


import datetime
import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.commenting import objects as ABCObjects
from dlkit.abstract_osid.commenting import queries as ABCQueries
from dlkit.abstract_osid.commenting.objects import Book as ABCBook
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidList
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.json_.id.objects import IdList
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_lookup_session_class_fixture(request):
    # From test_templates/commenting.py::CommentLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def comment_lookup_session_test_fixture(request):
    # From test_templates/commenting.py::CommentLookupSession::init_template
    request.cls.comment_list = list()
    request.cls.comment_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + str(num)
            create_form.description = 'Test Comment for CommentLookupSession tests'
            object = request.cls.catalog.create_comment(create_form)
            request.cls.comment_list.append(object)
            request.cls.comment_ids.append(object.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_comment_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                for obj in catalog.get_comments():
                    catalog.delete_comment(obj.ident)
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("comment_lookup_session_class_fixture", "comment_lookup_session_test_fixture")
class TestCommentLookupSession(object):
    """Tests for CommentLookupSession"""
    def test_get_book_id(self):
        """Tests get_book_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_book_id() == self.catalog.ident

    def test_get_book(self):
        """Tests get_book"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_book(), ABCBook)

    def test_can_lookup_comments(self):
        """Tests can_lookup_comments"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_comments(), bool)

    def test_use_comparative_comment_view(self):
        """Tests use_comparative_comment_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_comment_view()

    def test_use_plenary_comment_view(self):
        """Tests use_plenary_comment_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_comment_view()

    def test_use_federated_book_view(self):
        """Tests use_federated_book_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_book_view()

    def test_use_isolated_book_view(self):
        """Tests use_isolated_book_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_book_view()

    def test_use_effective_comment_view(self):
        """Tests use_effective_comment_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_effective_comment_view()

    def test_use_any_effective_comment_view(self):
        """Tests use_any_effective_comment_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_any_effective_comment_view()

    def test_get_comment(self):
        """Tests get_comment"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_comment_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_book_view()
                obj = self.catalog.get_comment(self.comment_list[0].ident)
                assert obj.ident == self.comment_list[0].ident
                self.catalog.use_federated_book_view()
                obj = self.catalog.get_comment(self.comment_list[0].ident)
                assert obj.ident == self.comment_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_comment(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_book_view()
                obj = self.catalog.get_comment(self.comment_list[0].ident)
                assert obj.ident == self.comment_list[0].ident
                self.catalog.use_federated_book_view()
                obj = self.catalog.get_comment(self.comment_list[0].ident)
                assert obj.ident == self.comment_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_comment(self.fake_id)

    def test_get_comments_by_ids(self):
        """Tests get_comments_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        if self.svc_mgr.supports_comment_query():
            objects = self.catalog.get_comments_by_ids(self.comment_ids)
            assert isinstance(objects, CommentList)
            self.catalog.use_federated_book_view()
            objects = self.catalog.get_comments_by_ids(self.comment_ids)
            assert isinstance(objects, CommentList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_comments_by_ids(self.comment_ids)
                assert isinstance(objects, CommentList)
                self.catalog.use_federated_book_view()
                objects = self.catalog.get_comments_by_ids(self.comment_ids)
                assert objects.available() > 0
                assert isinstance(objects, CommentList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_comments_by_ids(self.comment_ids)

    def test_get_comments_by_genus_type(self):
        """Tests get_comments_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        if self.svc_mgr.supports_comment_query():
            objects = self.catalog.get_comments_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, CommentList)
            self.catalog.use_federated_book_view()
            objects = self.catalog.get_comments_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, CommentList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_comments_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, CommentList)
                self.catalog.use_federated_book_view()
                objects = self.catalog.get_comments_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, CommentList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_comments_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_comments_by_parent_genus_type(self):
        """Tests get_comments_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        if self.svc_mgr.supports_comment_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_comments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, CommentList)
                self.catalog.use_federated_book_view()
                objects = self.catalog.get_comments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, CommentList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_comments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_comments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, CommentList)
                self.catalog.use_federated_book_view()
                objects = self.catalog.get_comments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, CommentList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_comments_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_comments_by_record_type(self):
        """Tests get_comments_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        if self.svc_mgr.supports_comment_query():
            objects = self.catalog.get_comments_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, CommentList)
            self.catalog.use_federated_book_view()
            objects = self.catalog.get_comments_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, CommentList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_comments_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, CommentList)
                self.catalog.use_federated_book_view()
                objects = self.catalog.get_comments_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, CommentList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_comments_by_record_type(DEFAULT_TYPE)

    def test_get_comments_on_date(self):
        """Tests get_comments_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_on_date(True, True)

    def test_get_comments_by_genus_type_on_date(self):
        """Tests get_comments_by_genus_type_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_by_genus_type_on_date(True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_comments_for_commentor(self):
        """Tests get_comments_for_commentor"""
        pass

    def test_get_comments_for_commentor_on_date(self):
        """Tests get_comments_for_commentor_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_for_commentor_on_date(True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_commentor(self):
        """Tests get_comments_by_genus_type_for_commentor"""
        pass

    def test_get_comments_by_genus_type_for_commentor_on_date(self):
        """Tests get_comments_by_genus_type_for_commentor_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_by_genus_type_for_commentor_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_comments_for_reference(self):
        """Tests get_comments_for_reference"""
        pass

    def test_get_comments_for_reference_on_date(self):
        """Tests get_comments_for_reference_on_date"""
        # From test_templates/relationship.py::RelationshipLookupSession::get_relationships_for_source_on_date_template
        if not is_never_authz(self.service_config):
            end_date = DateTime.utcnow() + datetime.timedelta(days=5)
            end_date = DateTime(**{
                'year': end_date.year,
                'month': end_date.month,
                'day': end_date.day,
                'hour': end_date.hour,
                'minute': end_date.minute,
                'second': end_date.second,
                'microsecond': end_date.microsecond
            })

            # NOTE: this first argument will probably break in many of the other methods,
            #   since it's not clear they always use something like AGENT_ID
            # i.e. in get_grade_entries_for_gradebook_column_on_date it needs to be
            #   a gradebookColumnId.
            results = self.session.get_comments_for_reference_on_date(AGENT_ID, DateTime.utcnow(), end_date)
            assert isinstance(results, ABCObjects.CommentList)
            assert results.available() == 2

    @pytest.mark.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_reference(self):
        """Tests get_comments_by_genus_type_for_reference"""
        pass

    def test_get_comments_by_genus_type_for_reference_on_date(self):
        """Tests get_comments_by_genus_type_for_reference_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_by_genus_type_for_reference_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_comments_for_commentor_and_reference(self):
        """Tests get_comments_for_commentor_and_reference"""
        pass

    def test_get_comments_for_commentor_and_reference_on_date(self):
        """Tests get_comments_for_commentor_and_reference_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_for_commentor_and_reference_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_comments_by_genus_type_for_commentor_and_reference(self):
        """Tests get_comments_by_genus_type_for_commentor_and_reference"""
        pass

    def test_get_comments_by_genus_type_for_commentor_and_reference_on_date(self):
        """Tests get_comments_by_genus_type_for_commentor_and_reference_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_comments_by_genus_type_for_commentor_and_reference_on_date(True, True, True, True, True)

    def test_get_comments(self):
        """Tests get_comments"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.commenting.objects import CommentList
        if self.svc_mgr.supports_comment_query():
            objects = self.catalog.get_comments()
            assert isinstance(objects, CommentList)
            self.catalog.use_federated_book_view()
            objects = self.catalog.get_comments()
            assert isinstance(objects, CommentList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_comments()
                assert isinstance(objects, CommentList)
                self.catalog.use_federated_book_view()
                objects = self.catalog.get_comments()
                assert objects.available() > 0
                assert isinstance(objects, CommentList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_comments()

    def test_get_comment_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_comment(self.comment_ids[0], ALIAS_ID)
            obj = self.catalog.get_comment(ALIAS_ID)
            assert obj.get_id() == self.comment_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.comment_list = list()
    request.cls.comment_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def comment_query_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + color
            create_form.description = (
                'Test Comment for CommentQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_comment(create_form)
            request.cls.comment_list.append(obj)
            request.cls.comment_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_comment_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                for obj in catalog.get_comments():
                    catalog.delete_comment(obj.ident)
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("comment_query_session_class_fixture", "comment_query_session_test_fixture")
class TestCommentQuerySession(object):
    """Tests for CommentQuerySession"""
    def test_get_book_id(self):
        """Tests get_book_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_book_id() == self.catalog.ident

    def test_get_book(self):
        """Tests get_book"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_book(), ABCBook)

    def test_can_search_comments(self):
        """Tests can_search_comments"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_comments(), bool)

    def test_use_federated_book_view(self):
        """Tests use_federated_book_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_book_view()

    def test_use_isolated_book_view(self):
        """Tests use_isolated_book_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_book_view()

    def test_get_comment_query(self):
        """Tests get_comment_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_comment_query()
        assert isinstance(query, ABCQueries.CommentQuery)

    def test_get_comments_by_query(self):
        """Tests get_comments_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_comment_query()
            query.match_display_name('orange')
            assert self.catalog.get_comments_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_comments_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_comments_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.comment_list = list()
    request.cls.comment_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + str(num)
            create_form.description = 'Test Comment for CommentAdminSession tests'
            object = request.cls.catalog.create_comment(create_form)
            request.cls.comment_list.append(object)
            request.cls.comment_ids.append(object.ident)
        request.cls.form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])
        request.cls.form.display_name = 'new Comment'
        request.cls.form.description = 'description of Comment'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_comment(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_comment_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                for obj in catalog.get_comments():
                    catalog.delete_comment(obj.ident)
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_admin_session_test_fixture(request):
    pass


@pytest.mark.usefixtures("comment_admin_session_class_fixture", "comment_admin_session_test_fixture")
class TestCommentAdminSession(object):
    """Tests for CommentAdminSession"""
    def test_get_book_id(self):
        """Tests get_book_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_book_id() == self.catalog.ident

    def test_get_book(self):
        """Tests get_book"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_book(), ABCBook)

    def test_can_create_comments(self):
        """Tests can_create_comments"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_comments(), bool)

    def test_can_create_comment_with_record_types(self):
        """Tests can_create_comment_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_comment_with_record_types(DEFAULT_TYPE), bool)

    def test_get_comment_form_for_create(self):
        """Tests get_comment_form_for_create"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_comment_form_for_create(AGENT_ID, [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_comment_form_for_create(AGENT_ID, [])

    def test_create_comment(self):
        """Tests create_comment"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.commenting.objects import Comment
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Comment)
            assert self.osid_object.display_name.text == 'new Comment'
            assert self.osid_object.description.text == 'description of Comment'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_comment(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_comment('I Will Break You!')
            update_form = self.catalog.get_comment_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_comment(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_comment('foo')

    def test_can_update_comments(self):
        """Tests can_update_comments"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_comments(), bool)

    def test_get_comment_form_for_update(self):
        """Tests get_comment_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_comment_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_comment_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_comment_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='commenting.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_comment_form_for_update(self.fake_id)

    def test_update_comment(self):
        """Tests update_comment"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        if not is_never_authz(self.service_config):
            from dlkit.abstract_osid.commenting.objects import Comment
            form = self.catalog.get_comment_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_comment(form)
            assert isinstance(updated_object, Comment)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
            with pytest.raises(errors.IllegalState):
                self.catalog.update_comment(form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_comment('I Will Break You!')
            with pytest.raises(errors.InvalidArgument):
                self.catalog.update_comment(self.form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_comment('foo')

    def test_can_delete_comments(self):
        """Tests can_delete_comments"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_comments(), bool)

    def test_delete_comment(self):
        """Tests delete_comment"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_comment_form_for_create(AGENT_ID, [])
            form.display_name = 'new Comment'
            form.description = 'description of Comment'
            form.set_genus_type(NEW_TYPE)
            osid_object = self.catalog.create_comment(form)
            self.catalog.delete_comment(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_comment(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_comment(AGENT_ID)

    def test_can_manage_comment_aliases(self):
        """Tests can_manage_comment_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_comment_aliases(), bool)

    def test_alias_comment(self):
        """Tests alias_comment"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_comment(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_comment(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_comment(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_book_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.comment_list = list()
    request.cls.comment_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentBookSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book for Assignment'
        create_form.description = 'Test Book for CommentBookSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_book(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + str(num)
            create_form.description = 'Test Comment for CommentBookSession tests'
            obj = request.cls.catalog.create_comment(create_form)
            request.cls.comment_list.append(obj)
            request.cls.comment_ids.append(obj.ident)
        request.cls.svc_mgr.assign_comment_to_book(
            request.cls.comment_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_comment_to_book(
            request.cls.comment_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_comment_from_book(
                request.cls.comment_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_comment_from_book(
                request.cls.comment_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_comments():
                request.cls.catalog.delete_comment(obj.ident)
            request.cls.svc_mgr.delete_book(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_book_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("comment_book_session_class_fixture", "comment_book_session_test_fixture")
class TestCommentBookSession(object):
    """Tests for CommentBookSession"""
    def test_can_lookup_comment_book_mappings(self):
        """Tests can_lookup_comment_book_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_comment_book_mappings()
        assert isinstance(result, bool)

    def test_use_comparative_book_view(self):
        """Tests use_comparative_book_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_book_view()

    def test_use_plenary_book_view(self):
        """Tests use_plenary_book_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_book_view()

    def test_get_comment_ids_by_book(self):
        """Tests get_comment_ids_by_book"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_comment_ids_by_book(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_comment_ids_by_book(self.fake_id)

    def test_get_comments_by_book(self):
        """Tests get_comments_by_book"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_comments_by_book(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.CommentList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_comments_by_book(self.fake_id)

    def test_get_comment_ids_by_books(self):
        """Tests get_comment_ids_by_books"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            object_ids = self.session.get_comment_ids_by_books(catalog_ids)
            assert isinstance(object_ids, IdList)
            # Currently our impl does not remove duplicate objectIds
            assert object_ids.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_comment_ids_by_books([self.fake_id])

    def test_get_comments_by_books(self):
        """Tests get_comments_by_books"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        if not is_never_authz(self.service_config):
            catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
            results = self.session.get_comments_by_books(catalog_ids)
            assert isinstance(results, ABCObjects.CommentList)
            # Currently our impl does not remove duplicate objects
            assert results.available() == 5
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_comments_by_books([self.fake_id])

    def test_get_book_ids_by_comment(self):
        """Tests get_book_ids_by_comment"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_book_ids_by_comment(self.comment_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_ids_by_comment(self.fake_id)

    def test_get_books_by_comment(self):
        """Tests get_books_by_comment"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_books_by_comment(self.comment_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_books_by_comment(self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def comment_book_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.comment_list = list()
    request.cls.comment_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for CommentBookAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book for Assignment'
        create_form.description = 'Test Book for CommentBookAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_book(create_form)
        for num in [0, 1, 2]:
            create_form = request.cls.catalog.get_comment_form_for_create(AGENT_ID, [])
            create_form.display_name = 'Test Comment ' + str(num)
            create_form.description = 'Test Comment for CommentBookAssignmentSession tests'
            obj = request.cls.catalog.create_comment(create_form)
            request.cls.comment_list.append(obj)
            request.cls.comment_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_comments():
                request.cls.catalog.delete_comment(obj.ident)
            request.cls.svc_mgr.delete_book(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_book(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def comment_book_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("comment_book_assignment_session_class_fixture", "comment_book_assignment_session_test_fixture")
class TestCommentBookAssignmentSession(object):
    """Tests for CommentBookAssignmentSession"""
    def test_can_assign_comments(self):
        """Tests can_assign_comments"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_comments()
        assert isinstance(result, bool)

    def test_can_assign_comments_to_book(self):
        """Tests can_assign_comments_to_book"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_comments_to_book(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_book_ids(self):
        """Tests get_assignable_book_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_book_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_book_ids(self.fake_id)

    def test_get_assignable_book_ids_for_comment(self):
        """Tests get_assignable_book_ids_for_comment"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_book_ids_for_comment(self.catalog.ident, self.comment_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_book_ids_for_comment(self.fake_id, self.fake_id)

    def test_assign_comment_to_book(self):
        """Tests assign_comment_to_book"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_comments()
            assert results.available() == 0
            self.session.assign_comment_to_book(self.comment_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_comments()
            assert results.available() == 1
            self.session.unassign_comment_from_book(
                self.comment_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_comment_to_book(self.fake_id, self.fake_id)

    def test_unassign_comment_from_book(self):
        """Tests unassign_comment_from_book"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_comments()
            assert results.available() == 0
            self.session.assign_comment_to_book(
                self.comment_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_comments()
            assert results.available() == 1
            self.session.unassign_comment_from_book(
                self.comment_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_comments()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_comment_from_book(self.fake_id, self.fake_id)

    def test_reassign_comment_to_book(self):
        """Tests reassign_comment_to_book"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_comment_to_book(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for commenting proxy manager tests'
            catalog = request.cls.svc_mgr.create_book(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("book_lookup_session_class_fixture", "book_lookup_session_test_fixture")
class TestBookLookupSession(object):
    """Tests for BookLookupSession"""
    def test_can_lookup_books(self):
        """Tests can_lookup_books"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_books(), bool)

    def test_use_comparative_book_view(self):
        """Tests use_comparative_book_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_book_view()

    def test_use_plenary_book_view(self):
        """Tests use_plenary_book_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_book_view()

    def test_get_book(self):
        """Tests get_book"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_book(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book(self.fake_id)

    def test_get_books_by_ids(self):
        """Tests get_books_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_books_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.BookList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_books_by_ids([self.fake_id])

    def test_get_books_by_genus_type(self):
        """Tests get_books_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_books_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.BookList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_books_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_books_by_parent_genus_type(self):
        """Tests get_books_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_books_by_parent_genus_type(True)

    def test_get_books_by_record_type(self):
        """Tests get_books_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_books_by_record_type(True)

    def test_get_books_by_provider(self):
        """Tests get_books_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_books_by_provider(True)

    def test_get_books(self):
        """Tests get_books"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_books()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.BookList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_books()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def book_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book'
        create_form.description = 'Test Book for BookAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_book(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_book_form_for_create([])
        create_form.display_name = 'Test Book For Deletion'
        create_form.description = 'Test Book for BookAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_book(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_books():
                request.cls.svc_mgr.delete_book(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("book_admin_session_class_fixture", "book_admin_session_test_fixture")
class TestBookAdminSession(object):
    """Tests for BookAdminSession"""
    def test_can_create_books(self):
        """Tests can_create_books"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_books(), bool)

    def test_can_create_book_with_record_types(self):
        """Tests can_create_book_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_book_with_record_types(DEFAULT_TYPE), bool)

    def test_get_book_form_for_create(self):
        """Tests get_book_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.commenting.objects import BookForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_book_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_book_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_form_for_create([])

    def test_create_book(self):
        """Tests create_book"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.commenting.objects import Book
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_book_form_for_create([])
            catalog_form.display_name = 'Test Book'
            catalog_form.description = 'Test Book for BookAdminSession.create_book tests'
            new_catalog = self.svc_mgr.create_book(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_book(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_book('I Will Break You!')
            update_form = self.svc_mgr.get_book_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_book(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_book('foo')

    def test_can_update_books(self):
        """Tests can_update_books"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_books(), bool)

    def test_get_book_form_for_update(self):
        """Tests get_book_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.commenting.objects import BookForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_book_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_form_for_update(self.fake_id)

    def test_update_book(self):
        """Tests update_book"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_book_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_book(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_book('foo')

    def test_can_delete_books(self):
        """Tests can_delete_books"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_books(), bool)

    def test_delete_book(self):
        """Tests delete_book"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_book(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_book(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_book(self.fake_id)

    def test_can_manage_book_aliases(self):
        """Tests can_manage_book_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_book_aliases(), bool)

    def test_alias_book(self):
        """Tests alias_book"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('commenting.Book%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_book(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_book(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_book(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Book ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_book(create_form)
        request.cls.svc_mgr.add_root_book(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_book(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_book(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_book(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_book(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_books(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_book(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_book(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("book_hierarchy_session_class_fixture", "book_hierarchy_session_test_fixture")
class TestBookHierarchySession(object):
    """Tests for BookHierarchySession"""
    def test_get_book_hierarchy_id(self):
        """Tests get_book_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_book_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_book_hierarchy(self):
        """Tests get_book_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_book_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_hierarchy()

    def test_can_access_book_hierarchy(self):
        """Tests can_access_book_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_book_hierarchy(), bool)

    def test_use_comparative_book_view(self):
        """Tests use_comparative_book_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_book_view()

    def test_use_plenary_book_view(self):
        """Tests use_plenary_book_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_book_view()

    def test_get_root_book_ids(self):
        """Tests get_root_book_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_book_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_book_ids()

    def test_get_root_books(self):
        """Tests get_root_books"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.commenting.objects import BookList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_books()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_books()

    def test_has_parent_books(self):
        """Tests has_parent_books"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_books(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_books(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_books(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_books(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_books(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_books(self.fake_id)

    def test_is_parent_of_book(self):
        """Tests is_parent_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_book(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_book(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_book(self.fake_id, self.fake_id)

    def test_get_parent_book_ids(self):
        """Tests get_parent_book_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_book_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_book_ids(self.fake_id)

    def test_get_parent_books(self):
        """Tests get_parent_books"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_books(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_books(self.fake_id)

    def test_is_ancestor_of_book(self):
        """Tests is_ancestor_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_book,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_book(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_book(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_books(self):
        """Tests has_child_books"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_books(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_books(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_books(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_books(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_books(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_books(self.fake_id)

    def test_is_child_of_book(self):
        """Tests is_child_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_book(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_book(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_book(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_book(self.fake_id, self.fake_id)

    def test_get_child_book_ids(self):
        """Tests get_child_book_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_book_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_book_ids(self.fake_id)

    def test_get_child_books(self):
        """Tests get_child_books"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_books(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_books(self.fake_id)

    def test_is_descendant_of_book(self):
        """Tests is_descendant_of_book"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_book,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_book(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_book(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_book_node_ids(self):
        """Tests get_book_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_book_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_node_ids(self.fake_id, 1, 2, False)

    def test_get_book_nodes(self):
        """Tests get_book_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_book_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def book_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'COMMENTING',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_book_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Book ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_book(create_form)
        request.cls.svc_mgr.add_root_book(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_book(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_book(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_book(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_book(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_books(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_book(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def book_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("book_hierarchy_design_session_class_fixture", "book_hierarchy_design_session_test_fixture")
class TestBookHierarchyDesignSession(object):
    """Tests for BookHierarchyDesignSession"""
    def test_get_book_hierarchy_id(self):
        """Tests get_book_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_book_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_book_hierarchy(self):
        """Tests get_book_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_book_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_book_hierarchy()

    def test_can_modify_book_hierarchy(self):
        """Tests can_modify_book_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_book_hierarchy(), bool)

    def test_add_root_book(self):
        """Tests add_root_book"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_books()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_book(self.fake_id)

    def test_remove_root_book(self):
        """Tests remove_root_book"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_books()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Book root'
            new_book = self.svc_mgr.create_book(create_form)
            self.svc_mgr.add_root_book(new_book.ident)

            roots = self.session.get_root_books()
            assert roots.available() == 2

            self.session.remove_root_book(new_book.ident)

            roots = self.session.get_root_books()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_book(self.fake_id)

    def test_add_child_book(self):
        """Tests add_child_book"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_books(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_book(self.fake_id, self.fake_id)

    def test_remove_child_book(self):
        """Tests remove_child_book"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_books(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Book child'
            new_book = self.svc_mgr.create_book(create_form)
            self.svc_mgr.add_child_book(
                self.catalogs['Root'].ident,
                new_book.ident)

            children = self.session.get_child_books(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_book(
                self.catalogs['Root'].ident,
                new_book.ident)

            children = self.session.get_child_books(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_book(self.fake_id, self.fake_id)

    def test_remove_child_books(self):
        """Tests remove_child_books"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_books(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_book_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Book child'
            new_book = self.svc_mgr.create_book(create_form)
            self.svc_mgr.add_child_book(
                self.catalogs['Grandchild 1'].ident,
                new_book.ident)

            children = self.session.get_child_books(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_books(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_books(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_books(self.fake_id)
