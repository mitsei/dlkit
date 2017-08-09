"""TestAuthZ implementations of logging_.LogEntry"""

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

LOOKUP_LOG_ENTRY_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'logging.LogEntry', 'authority': 'ODL.MIT.EDU'})
SEARCH_LOG_ENTRY_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'logging.LogEntry', 'authority': 'ODL.MIT.EDU'})
CREATE_LOG_ENTRY_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'logging.LogEntry', 'authority': 'ODL.MIT.EDU'})
DELETE_LOG_ENTRY_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'logging.LogEntry', 'authority': 'ODL.MIT.EDU'})
ASSIGN_LOG_ENTRY_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'logging.LogEntryLog', 'authority': 'ODL.MIT.EDU'})
CREATE_LOG_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'logging.Log', 'authority': 'ODL.MIT.EDU'})
DELETE_LOG_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'logging.Log', 'authority': 'ODL.MIT.EDU'})
LOOKUP_LOG_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'logging.Log', 'authority': 'ODL.MIT.EDU'})
ACCESS_LOG_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'logging.Log', 'authority': 'ODL.MIT.EDU'})
MODIFY_LOG_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'logging.Log', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('logging.Log%3AROOT%40ODL.MIT.EDU')
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

        request.cls.log_list = list()
        request.cls.log_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.logging_mgr = Runtime().get_service_manager(
            'LOGGING',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.logging_mgr.get_log_form_for_create([])
            create_form.display_name = 'Test Log ' + str(num)
            create_form.description = 'Test Log for Testing Authorization Number: ' + str(num)
            log = request.cls.logging_mgr.create_log(create_form)
            request.cls.log_list.append(log)
            request.cls.log_id_list.append(log.ident)

        request.cls.logging_mgr.add_root_log(request.cls.log_id_list[0])
        request.cls.logging_mgr.add_child_log(request.cls.log_id_list[0], request.cls.log_id_list[1])
        request.cls.logging_mgr.add_child_log(request.cls.log_id_list[0], request.cls.log_id_list[2])
        request.cls.logging_mgr.add_child_log(request.cls.log_id_list[1], request.cls.log_id_list[3])
        request.cls.logging_mgr.add_child_log(request.cls.log_id_list[1], request.cls.log_id_list[4])
        request.cls.logging_mgr.add_child_log(request.cls.log_id_list[2], request.cls.log_id_list[5])

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' log_entry in log 2 is also assigned to log 7)

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up Log lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_LOG_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up LogEntry lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_LOG_ENTRY_FUNCTION_ID,
                request.cls.log_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up LogEntry lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_LOG_ENTRY_FUNCTION_ID,
                request.cls.log_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up LogEntry search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_LOG_ENTRY_FUNCTION_ID,
                request.cls.log_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up LogEntry search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_LOG_ENTRY_FUNCTION_ID,
                request.cls.log_id_list[num],
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
            for catalog in request.cls.logging_mgr.get_logs():
                for obj in catalog.get_log_entries():
                    catalog.delete_log_entry(obj.ident)
                request.cls.logging_mgr.delete_log(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authz_adapter_test_fixture(request):
    request.cls.log_entry_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        for log_ in request.cls.log_list:
            request.cls.log_entry_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = log_.get_log_entry_form_for_create([])
                create_form.display_name = color + ' ' + str(count) + ' LogEntry'
                create_form.description = color + ' log_entry for authz adapter tests from Log number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                log_entry = log_.create_log_entry(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.logging_mgr.assign_log_entry_to_log(
                        log_entry.ident,
                        request.cls.log_id_list[7])
                request.cls.log_entry_id_lists[count].append(log_entry.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, log_ in enumerate(request.cls.log_list):
                for log_entry_id in request.cls.log_entry_id_lists[index]:
                    log_.delete_log_entry(log_entry_id)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture", "authz_adapter_test_fixture")
class TestLogEntryAuthzAdapter(object):

    def test_lookup_log_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[0])
            log.use_isolated_log_view()
            log.use_plenary_log_entry_view()
            # with pytest.raises(errors.NotFound):
            #     log_entries = log.get_log_entries()
            # with pytest.raises(errors.NotFound):
            #     log_entries = log.get_log_entries_by_genus_type(BLUE_TYPE)
            # for log_entry_id in self.log_entry_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         log_entry = log.get_log_entry(log_entry_id)
            # with pytest.raises(errors.NotFound):
            #     log_entries = log.get_log_entries_by_ids(self.log_entry_id_lists[0])

    def test_lookup_log_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[0])
            log.use_federated_log_view()
            log.use_plenary_log_entry_view()
            assert log.can_lookup_log_entries()
            assert log.get_log_entries().available() == 1
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).next().ident == self.log_entry_id_lists[2][1]
            log.get_log_entry(self.log_entry_id_lists[2][1])
            for log_entry_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    log_entry = log.get_log_entry(self.log_entry_id_lists[2][log_entry_num])

    def test_lookup_log_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[0])
            log.use_federated_log_view()
            log.use_comparative_log_entry_view()
            # print "START"
            assert log.get_log_entries().available() == 13
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 5
            for log_entry in log.get_log_entries():
                log.get_log_entry(log_entry.ident)
            log_entry_ids = [log_entry.ident for log_entry in log.get_log_entries()]
            log.get_log_entries_by_ids(log_entry_ids)
            for log_entry_id in self.log_entry_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    log_entry = log.get_log_entry(log_entry_id)
            log_entry = log.get_log_entry(self.log_entry_id_lists[2][1])
            for log_entry_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    log_entry = log.get_log_entry(self.log_entry_id_lists[2][log_entry_num])
            for log_entry_id in self.log_entry_id_lists[1]:
                    log_entry = log.get_log_entry(log_entry_id)
            for log_entry_id in self.log_entry_id_lists[3]:
                    log_entry = log.get_log_entry(log_entry_id)
            for log_entry_id in self.log_entry_id_lists[4]:
                    log_entry = log.get_log_entry(log_entry_id)
            for log_entry_id in self.log_entry_id_lists[5]:
                    log_entry = log.get_log_entry(log_entry_id)

    def test_lookup_log_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[0])
            log.use_isolated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 0
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_log_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[1])
            log.use_isolated_log_view()
            log.use_plenary_log_entry_view()
            assert log.get_log_entries().available() == 3
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_log_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[1])
            log.use_federated_log_view()
            log.use_plenary_log_entry_view()
            assert log.get_log_entries().available() == 9
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_log_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[1])
            log.use_federated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 9
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_log_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[1])
            log.use_isolated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 3
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_log_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[2])
            log.use_isolated_log_view()
            log.use_plenary_log_entry_view()
            assert log.get_log_entries().available() == 1
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     log_entries = log.get_log_entries()
            # with pytest.raises(errors.PermissionDenied):
            #     log_entries = log.get_log_entries_by_genus_type(BLUE_TYPE)

    def test_lookup_log_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[2])
            log.use_federated_log_view()
            log.use_plenary_log_entry_view()
            assert log.get_log_entries().available() == 1
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     log_entries = log.get_log_entries()
            # with pytest.raises(errors.PermissionDenied):
            #     log_entries = log.get_log_entries_by_genus_type(BLUE_TYPE)

    def test_lookup_log_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[2])
            log.use_federated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 4
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(log.get_log_entries().available(), 3)
            # self.assertEqual(log.get_log_entries_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_log_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[2])
            log.use_isolated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 1
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     log_entries = log.get_log_entries()
            # with pytest.raises(errors.PermissionDenied):
            #     log_entries = log.get_log_entries_by_genus_type(BLUE_TYPE)

    def test_lookup_log_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[3])
            log.use_isolated_log_view()
            log.use_plenary_log_entry_view()
            assert log.get_log_entries().available() == 3
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_log_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[3])
            log.use_federated_log_view()
            log.use_plenary_log_entry_view()
            assert log.get_log_entries().available() == 3
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_log_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[3])
            log.use_federated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 3
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_log_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[3])
            log.use_isolated_log_view()
            log.use_comparative_log_entry_view()
            assert log.get_log_entries().available() == 3
            assert log.get_log_entries_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_log_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[0])
            log.use_isolated_log_view()
            with pytest.raises(errors.PermissionDenied):
                query = log.get_log_entry_query()

    def test_query_log_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[0])
            log.use_federated_log_view()
            query = log.get_log_entry_query()
            query.match_display_name('red')
            assert log.get_log_entries_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert log.get_log_entries_by_query(query).available() == 5

    def test_query_log_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[1])
            log.use_isolated_log_view()
            query = log.get_log_entry_query()
            query.match_display_name('red')
            assert log.get_log_entries_by_query(query).available() == 2

    def test_query_log_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_logging_mgr = Runtime().get_service_manager(
                'LOGGING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            log = janes_logging_mgr.get_log(self.log_id_list[1])
            log.use_federated_log_view()
            query = log.get_log_entry_query()
            query.match_display_name('red')
            assert log.get_log_entries_by_query(query).available() == 6
