"""TestAuthZ implementations of authorization.Authorization"""

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

LOOKUP_AUTHORIZATION_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'authorization.Authorization', 'authority': 'ODL.MIT.EDU'})
SEARCH_AUTHORIZATION_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'authorization.Authorization', 'authority': 'ODL.MIT.EDU'})
CREATE_AUTHORIZATION_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'authorization.Authorization', 'authority': 'ODL.MIT.EDU'})
DELETE_AUTHORIZATION_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'authorization.Authorization', 'authority': 'ODL.MIT.EDU'})
ASSIGN_AUTHORIZATION_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'authorization.AuthorizationVault', 'authority': 'ODL.MIT.EDU'})
CREATE_VAULT_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'authorization.Vault', 'authority': 'ODL.MIT.EDU'})
DELETE_VAULT_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'authorization.Vault', 'authority': 'ODL.MIT.EDU'})
LOOKUP_VAULT_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'authorization.Vault', 'authority': 'ODL.MIT.EDU'})
ACCESS_VAULT_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'authorization.Vault', 'authority': 'ODL.MIT.EDU'})
MODIFY_VAULT_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'authorization.Vault', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('authorization.Vault%3AROOT%40ODL.MIT.EDU')
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

        request.cls.vault_list = list()
        request.cls.vault_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.authorization_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.authorization_mgr.get_vault_form_for_create([])
            create_form.display_name = 'Test Vault ' + str(num)
            create_form.description = 'Test Vault for Testing Authorization Number: ' + str(num)
            vault = request.cls.authorization_mgr.create_vault(create_form)
            request.cls.vault_list.append(vault)
            request.cls.vault_id_list.append(vault.ident)

        request.cls.authorization_mgr.add_root_vault(request.cls.vault_id_list[0])
        request.cls.authorization_mgr.add_child_vault(request.cls.vault_id_list[0], request.cls.vault_id_list[1])
        request.cls.authorization_mgr.add_child_vault(request.cls.vault_id_list[0], request.cls.vault_id_list[2])
        request.cls.authorization_mgr.add_child_vault(request.cls.vault_id_list[1], request.cls.vault_id_list[3])
        request.cls.authorization_mgr.add_child_vault(request.cls.vault_id_list[1], request.cls.vault_id_list[4])
        request.cls.authorization_mgr.add_child_vault(request.cls.vault_id_list[2], request.cls.vault_id_list[5])

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' authorization in vault 2 is also assigned to vault 7)

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up Vault lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_VAULT_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up Authorization lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_AUTHORIZATION_FUNCTION_ID,
                request.cls.vault_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Authorization lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_AUTHORIZATION_FUNCTION_ID,
                request.cls.vault_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Authorization search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_AUTHORIZATION_FUNCTION_ID,
                request.cls.vault_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Authorization search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_AUTHORIZATION_FUNCTION_ID,
                request.cls.vault_id_list[num],
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
            for catalog in request.cls.authorization_mgr.get_vaults():
                for obj in catalog.get_authorizations():
                    catalog.delete_authorization(obj.ident)
                request.cls.authorization_mgr.delete_vault(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authz_adapter_test_fixture(request):
    request.cls.authorization_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        agent_id = Id(authority='TEST', namespace='authentication.Agent', identifier='A_USER')
        for vault_ in request.cls.vault_list:
            request.cls.authorization_id_lists.append([])
            for color in ['Red', 'Blue', 'Another Red']:
                # Note that the json authorization service seems picky about ids.  Need to review.
                func_namespace = 'resource.Resource'
                func_authority = 'TEST'
                if color == 'Red':
                    func_identifier = 'lookup'
                elif color == 'Blue':
                    func_identifier = 'query'
                else:
                    func_identifier = 'admin'
                function_id = Id(authority=func_authority, namespace=func_namespace, identifier=func_identifier)
                qualifier_id = Id(authority='TEST', namespace='authorization.Qualifier', identifier='TEST' + str(count) + color)
                create_form = vault_.get_authorization_form_for_create_for_agent(agent_id, function_id, qualifier_id, [])
                create_form.display_name = color + ' ' + str(count) + ' Authorization'
                create_form.description = color + ' authorization for authz adapter tests from Vault number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                authorization = vault_.create_authorization(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.authorization_mgr.assign_authorization_to_vault(
                        authorization.ident,
                        request.cls.vault_id_list[7])
                request.cls.authorization_id_lists[count].append(authorization.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, vault_ in enumerate(request.cls.vault_list):
                for authorization_id in request.cls.authorization_id_lists[index]:
                    vault_.delete_authorization(authorization_id)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture", "authz_adapter_test_fixture")
class TestAuthorizationAuthzAdapter(object):

    def test_lookup_vault_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[0])
            vault.use_isolated_vault_view()
            vault.use_plenary_authorization_view()
            # with pytest.raises(errors.NotFound):
            #     authorizations = vault.get_authorizations()
            # with pytest.raises(errors.NotFound):
            #     authorizations = vault.get_authorizations_by_genus_type(BLUE_TYPE)
            # for authorization_id in self.authorization_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         authorization = vault.get_authorization(authorization_id)
            # with pytest.raises(errors.NotFound):
            #     authorizations = vault.get_authorizations_by_ids(self.authorization_id_lists[0])

    def test_lookup_vault_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[0])
            vault.use_federated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.can_lookup_authorizations()
            assert vault.get_authorizations().available() == 1
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).next().ident == self.authorization_id_lists[2][1]
            vault.get_authorization(self.authorization_id_lists[2][1])
            for authorization_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    authorization = vault.get_authorization(self.authorization_id_lists[2][authorization_num])

    def test_lookup_vault_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[0])
            vault.use_federated_vault_view()
            vault.use_comparative_authorization_view()
            # print "START"
            assert vault.get_authorizations().available() == 13
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 5
            for authorization in vault.get_authorizations():
                vault.get_authorization(authorization.ident)
            authorization_ids = [authorization.ident for authorization in vault.get_authorizations()]
            vault.get_authorizations_by_ids(authorization_ids)
            for authorization_id in self.authorization_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    authorization = vault.get_authorization(authorization_id)
            authorization = vault.get_authorization(self.authorization_id_lists[2][1])
            for authorization_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    authorization = vault.get_authorization(self.authorization_id_lists[2][authorization_num])
            for authorization_id in self.authorization_id_lists[1]:
                    authorization = vault.get_authorization(authorization_id)
            for authorization_id in self.authorization_id_lists[3]:
                    authorization = vault.get_authorization(authorization_id)
            for authorization_id in self.authorization_id_lists[4]:
                    authorization = vault.get_authorization(authorization_id)
            for authorization_id in self.authorization_id_lists[5]:
                    authorization = vault.get_authorization(authorization_id)

    def test_lookup_vault_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[0])
            vault.use_isolated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 0
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_vault_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[1])
            vault.use_isolated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.get_authorizations().available() == 3
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_vault_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[1])
            vault.use_federated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.get_authorizations().available() == 9
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_vault_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[1])
            vault.use_federated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 9
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_vault_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[1])
            vault.use_isolated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 3
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_vault_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[2])
            vault.use_isolated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.get_authorizations().available() == 1
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     authorizations = vault.get_authorizations()
            # with pytest.raises(errors.PermissionDenied):
            #     authorizations = vault.get_authorizations_by_genus_type(BLUE_TYPE)

    def test_lookup_vault_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[2])
            vault.use_federated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.get_authorizations().available() == 1
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     authorizations = vault.get_authorizations()
            # with pytest.raises(errors.PermissionDenied):
            #     authorizations = vault.get_authorizations_by_genus_type(BLUE_TYPE)

    def test_lookup_vault_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[2])
            vault.use_federated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 4
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(vault.get_authorizations().available(), 3)
            # self.assertEqual(vault.get_authorizations_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_vault_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[2])
            vault.use_isolated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 1
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     authorizations = vault.get_authorizations()
            # with pytest.raises(errors.PermissionDenied):
            #     authorizations = vault.get_authorizations_by_genus_type(BLUE_TYPE)

    def test_lookup_vault_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[3])
            vault.use_isolated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.get_authorizations().available() == 3
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_vault_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[3])
            vault.use_federated_vault_view()
            vault.use_plenary_authorization_view()
            assert vault.get_authorizations().available() == 3
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_vault_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[3])
            vault.use_federated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 3
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_vault_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[3])
            vault.use_isolated_vault_view()
            vault.use_comparative_authorization_view()
            assert vault.get_authorizations().available() == 3
            assert vault.get_authorizations_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_vault_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[0])
            vault.use_isolated_vault_view()
            with pytest.raises(errors.PermissionDenied):
                query = vault.get_authorization_query()

    def test_query_vault_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[0])
            vault.use_federated_vault_view()
            query = vault.get_authorization_query()
            query.match_display_name('red')
            assert vault.get_authorizations_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert vault.get_authorizations_by_query(query).available() == 5

    def test_query_vault_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[1])
            vault.use_isolated_vault_view()
            query = vault.get_authorization_query()
            query.match_display_name('red')
            assert vault.get_authorizations_by_query(query).available() == 2

    def test_query_vault_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_authorization_mgr = Runtime().get_service_manager(
                'AUTHORIZATION',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            vault = janes_authorization_mgr.get_vault(self.vault_id_list[1])
            vault.use_federated_vault_view()
            query = vault.get_authorization_query()
            query.match_display_name('red')
            assert vault.get_authorizations_by_query(query).available() == 6
