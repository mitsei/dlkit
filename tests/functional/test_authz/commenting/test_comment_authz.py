"""TestAuthZ implementations of commenting.Comment"""

import datetime
import pytest
from tests.utilities.general import is_never_authz, is_no_authz, uses_cataloging
from dlkit.abstract_osid.authorization import objects as ABCObjects
from dlkit.abstract_osid.authorization import queries as ABCQueries
from dlkit.abstract_osid.authorization.objects import Authorization
from dlkit.abstract_osid.authorization.objects import AuthorizationList
from dlkit.abstract_osid.authorization.objects import Vault as ABCVault
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

JANE_REQUEST = proxy_example.SimpleRequest(username='jane_doe')
JANE_CONDITION = PROXY_SESSION.get_proxy_condition()
JANE_CONDITION.set_http_request(JANE_REQUEST)
JANE_PROXY = PROXY_SESSION.get_proxy(JANE_CONDITION)

LOOKUP_COMMENT_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'commenting.Comment', 'authority': 'ODL.MIT.EDU'})
SEARCH_COMMENT_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'commenting.Comment', 'authority': 'ODL.MIT.EDU'})
CREATE_COMMENT_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'commenting.Comment', 'authority': 'ODL.MIT.EDU'})
DELETE_COMMENT_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'commenting.Comment', 'authority': 'ODL.MIT.EDU'})
ASSIGN_COMMENT_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'commenting.CommentBook', 'authority': 'ODL.MIT.EDU'})
CREATE_BOOK_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'commenting.Book', 'authority': 'ODL.MIT.EDU'})
DELETE_BOOK_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'commenting.Book', 'authority': 'ODL.MIT.EDU'})
LOOKUP_BOOK_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'commenting.Book', 'authority': 'ODL.MIT.EDU'})
ACCESS_BOOK_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'commenting.Book', 'authority': 'ODL.MIT.EDU'})
MODIFY_BOOK_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'commenting.Book', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('commenting.Book%3AROOT%40ODL.MIT.EDU')
BOOTSTRAP_VAULT_TYPE = Type(authority='ODL.MIT.EDU', namespace='authorization.Vault', identifier='bootstrap_vault')
OVERRIDE_VAULT_TYPE = Type(authority='ODL.MIT.EDU', namespace='authorization.Vault', identifier='override_vault')
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
BLUE_TYPE = Type(authority='BLUE', namespace='BLUE', identifier='BLUE')


@pytest.fixture(scope="class",
                params=['TEST_SERVICE'])
def authz_adapter_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.authz_mgr = Runtime().get_manager(
        'AUTHORIZATION',
        implementation='TEST_SERVICE')
    if not is_never_authz(request.cls.service_config):
        request.cls.vault_admin_session = request.cls.authz_mgr.get_vault_admin_session()
        request.cls.vault_lookup_session = request.cls.authz_mgr.get_vault_lookup_session()

        create_form = request.cls.vault_admin_session.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationSession tests'
        create_form.genus_type = BOOTSTRAP_VAULT_TYPE
        request.cls.vault = request.cls.vault_admin_session.create_vault(create_form)

        create_form = request.cls.vault_admin_session.get_vault_form_for_create([])
        create_form.display_name = 'Test Override Vault'
        create_form.description = 'Test Override Vault for AuthorizationSession tests'
        create_form.genus_type = OVERRIDE_VAULT_TYPE
        request.cls.override_vault = request.cls.vault_admin_session.create_vault(create_form)

        request.cls.authz_admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(request.cls.vault.ident)
        request.cls.override_authz_admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(request.cls.override_vault.ident)
        request.cls.authz_lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(request.cls.vault.ident)

        request.cls.book_list = list()
        request.cls.book_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.commenting_mgr = Runtime().get_service_manager(
            'COMMENTING',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.commenting_mgr.get_book_form_for_create([])
            create_form.display_name = 'Test Book ' + str(num)
            create_form.description = 'Test Book for Testing Authorization Number: ' + str(num)
            book = request.cls.commenting_mgr.create_book(create_form)
            request.cls.book_list.append(book)
            request.cls.book_id_list.append(book.ident)

        request.cls.commenting_mgr.add_root_book(request.cls.book_id_list[0])
        request.cls.commenting_mgr.add_child_book(request.cls.book_id_list[0], request.cls.book_id_list[1])
        request.cls.commenting_mgr.add_child_book(request.cls.book_id_list[0], request.cls.book_id_list[2])
        request.cls.commenting_mgr.add_child_book(request.cls.book_id_list[1], request.cls.book_id_list[3])
        request.cls.commenting_mgr.add_child_book(request.cls.book_id_list[1], request.cls.book_id_list[4])
        request.cls.commenting_mgr.add_child_book(request.cls.book_id_list[2], request.cls.book_id_list[5])

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' comment in book 2 is also assigned to book 7)

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up Book lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_BOOK_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up Comment lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_COMMENT_FUNCTION_ID,
                request.cls.book_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Comment lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_COMMENT_FUNCTION_ID,
                request.cls.book_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Comment search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_COMMENT_FUNCTION_ID,
                request.cls.book_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Comment search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_COMMENT_FUNCTION_ID,
                request.cls.book_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

    else:
        request.cls.catalog = request.cls.svc_mgr.get_authorization_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.commenting_mgr.get_books():
                for obj in catalog.get_comments():
                    catalog.delete_comment(obj.ident)
                request.cls.commenting_mgr.delete_book(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authz_adapter_test_fixture(request):
    request.cls.comment_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        resource_id = Id(authority='TEST', namespace='resource.Resource', identifier='TEST')
        for book_ in request.cls.book_list:
            request.cls.comment_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = book_.get_comment_form_for_create(resource_id, [])
                create_form.display_name = color + ' ' + str(count) + ' Comment'
                create_form.description = color + ' comment for authz adapter tests from Book number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                comment = book_.create_comment(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.commenting_mgr.assign_comment_to_book(
                        comment.ident,
                        request.cls.book_id_list[7])
                request.cls.comment_id_lists[count].append(comment.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, book_ in enumerate(request.cls.book_list):
                for comment_id in request.cls.comment_id_lists[index]:
                    book_.delete_comment(comment_id)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture", "authz_adapter_test_fixture")
class TestCommentAuthzAdapter(object):

    def test_lookup_book_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[0])
            book.use_isolated_book_view()
            book.use_plenary_comment_view()
            # with pytest.raises(errors.NotFound):
            #     comments = book.get_comments()
            # with pytest.raises(errors.NotFound):
            #     comments = book.get_comments_by_genus_type(BLUE_TYPE)
            # for comment_id in self.comment_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         comment = book.get_comment(comment_id)
            # with pytest.raises(errors.NotFound):
            #     comments = book.get_comments_by_ids(self.comment_id_lists[0])

    def test_lookup_book_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[0])
            book.use_federated_book_view()
            book.use_plenary_comment_view()
            assert book.can_lookup_comments()
            assert book.get_comments().available() == 1
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1
            assert book.get_comments_by_genus_type(BLUE_TYPE).next().ident == self.comment_id_lists[2][1]
            book.get_comment(self.comment_id_lists[2][1])
            for comment_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    comment = book.get_comment(self.comment_id_lists[2][comment_num])

    def test_lookup_book_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[0])
            book.use_federated_book_view()
            book.use_comparative_comment_view()
            # print "START"
            assert book.get_comments().available() == 13
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 5
            for comment in book.get_comments():
                book.get_comment(comment.ident)
            comment_ids = [comment.ident for comment in book.get_comments()]
            book.get_comments_by_ids(comment_ids)
            for comment_id in self.comment_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    comment = book.get_comment(comment_id)
            comment = book.get_comment(self.comment_id_lists[2][1])
            for comment_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    comment = book.get_comment(self.comment_id_lists[2][comment_num])
            for comment_id in self.comment_id_lists[1]:
                    comment = book.get_comment(comment_id)
            for comment_id in self.comment_id_lists[3]:
                    comment = book.get_comment(comment_id)
            for comment_id in self.comment_id_lists[4]:
                    comment = book.get_comment(comment_id)
            for comment_id in self.comment_id_lists[5]:
                    comment = book.get_comment(comment_id)

    def test_lookup_book_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[0])
            book.use_isolated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 0
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_book_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[1])
            book.use_isolated_book_view()
            book.use_plenary_comment_view()
            assert book.get_comments().available() == 3
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_book_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[1])
            book.use_federated_book_view()
            book.use_plenary_comment_view()
            assert book.get_comments().available() == 9
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_book_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[1])
            book.use_federated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 9
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_book_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[1])
            book.use_isolated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 3
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_book_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[2])
            book.use_isolated_book_view()
            book.use_plenary_comment_view()
            assert book.get_comments().available() == 1
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     comments = book.get_comments()
            # with pytest.raises(errors.PermissionDenied):
            #     comments = book.get_comments_by_genus_type(BLUE_TYPE)

    def test_lookup_book_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[2])
            book.use_federated_book_view()
            book.use_plenary_comment_view()
            assert book.get_comments().available() == 1
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     comments = book.get_comments()
            # with pytest.raises(errors.PermissionDenied):
            #     comments = book.get_comments_by_genus_type(BLUE_TYPE)

    def test_lookup_book_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[2])
            book.use_federated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 4
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(book.get_comments().available(), 3)
            # self.assertEqual(book.get_comments_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_book_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[2])
            book.use_isolated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 1
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     comments = book.get_comments()
            # with pytest.raises(errors.PermissionDenied):
            #     comments = book.get_comments_by_genus_type(BLUE_TYPE)

    def test_lookup_book_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[3])
            book.use_isolated_book_view()
            book.use_plenary_comment_view()
            assert book.get_comments().available() == 3
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_book_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[3])
            book.use_federated_book_view()
            book.use_plenary_comment_view()
            assert book.get_comments().available() == 3
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_book_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[3])
            book.use_federated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 3
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_book_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[3])
            book.use_isolated_book_view()
            book.use_comparative_comment_view()
            assert book.get_comments().available() == 3
            assert book.get_comments_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_book_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[0])
            book.use_isolated_book_view()
            with pytest.raises(errors.PermissionDenied):
                query = book.get_comment_query()

    def test_query_book_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[0])
            book.use_federated_book_view()
            query = book.get_comment_query()
            query.match_display_name('red')
            assert book.get_comments_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert book.get_comments_by_query(query).available() == 5

    def test_query_book_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[1])
            book.use_isolated_book_view()
            query = book.get_comment_query()
            query.match_display_name('red')
            assert book.get_comments_by_query(query).available() == 2

    def test_query_book_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_commenting_mgr = Runtime().get_service_manager(
                'COMMENTING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            book = janes_commenting_mgr.get_book(self.book_id_list[1])
            book.use_federated_book_view()
            query = book.get_comment_query()
            query.match_display_name('red')
            assert book.get_comments_by_query(query).available() == 6
