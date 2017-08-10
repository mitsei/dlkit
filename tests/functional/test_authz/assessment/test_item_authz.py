"""TestAuthZ implementations of assessment.Item"""

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

LOOKUP_ITEM_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'assessment.Item', 'authority': 'ODL.MIT.EDU'})
SEARCH_ITEM_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'assessment.Item', 'authority': 'ODL.MIT.EDU'})
CREATE_ITEM_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'assessment.Item', 'authority': 'ODL.MIT.EDU'})
DELETE_ITEM_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'assessment.Item', 'authority': 'ODL.MIT.EDU'})
ASSIGN_ITEM_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'assessment.ItemBank', 'authority': 'ODL.MIT.EDU'})
CREATE_BANK_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'assessment.Bank', 'authority': 'ODL.MIT.EDU'})
DELETE_BANK_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'assessment.Bank', 'authority': 'ODL.MIT.EDU'})
LOOKUP_BANK_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'assessment.Bank', 'authority': 'ODL.MIT.EDU'})
ACCESS_BANK_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'assessment.Bank', 'authority': 'ODL.MIT.EDU'})
MODIFY_BANK_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'assessment.Bank', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('assessment.Bank%3AROOT%40ODL.MIT.EDU')
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

        request.cls.bank_list = list()
        request.cls.bank_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.assessment_mgr = Runtime().get_service_manager(
            'ASSESSMENT',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.assessment_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for Testing Authorization Number: ' + str(num)
            bank = request.cls.assessment_mgr.create_bank(create_form)
            request.cls.bank_list.append(bank)
            request.cls.bank_id_list.append(bank.ident)

        request.cls.assessment_mgr.add_root_bank(request.cls.bank_id_list[0])
        request.cls.assessment_mgr.add_child_bank(request.cls.bank_id_list[0], request.cls.bank_id_list[1])
        request.cls.assessment_mgr.add_child_bank(request.cls.bank_id_list[0], request.cls.bank_id_list[2])
        request.cls.assessment_mgr.add_child_bank(request.cls.bank_id_list[1], request.cls.bank_id_list[3])
        request.cls.assessment_mgr.add_child_bank(request.cls.bank_id_list[1], request.cls.bank_id_list[4])
        request.cls.assessment_mgr.add_child_bank(request.cls.bank_id_list[2], request.cls.bank_id_list[5])

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' item in bank 2 is also assigned to bank 7)

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up Bank lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_BANK_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up Item lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_ITEM_FUNCTION_ID,
                request.cls.bank_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Item lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_ITEM_FUNCTION_ID,
                request.cls.bank_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Item search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_ITEM_FUNCTION_ID,
                request.cls.bank_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Item search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_ITEM_FUNCTION_ID,
                request.cls.bank_id_list[num],
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
            for catalog in request.cls.assessment_mgr.get_banks():
                for obj in catalog.get_items():
                    catalog.delete_item(obj.ident)
                request.cls.assessment_mgr.delete_bank(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authz_adapter_test_fixture(request):
    request.cls.item_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        for bank_ in request.cls.bank_list:
            request.cls.item_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = bank_.get_item_form_for_create([])
                create_form.display_name = color + ' ' + str(count) + ' Item'
                create_form.description = color + ' item for authz adapter tests from Bank number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                item = bank_.create_item(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.assessment_mgr.assign_item_to_bank(
                        item.ident,
                        request.cls.bank_id_list[7])
                request.cls.item_id_lists[count].append(item.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, bank_ in enumerate(request.cls.bank_list):
                for item_id in request.cls.item_id_lists[index]:
                    bank_.delete_item(item_id)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture", "authz_adapter_test_fixture")
class TestItemAuthzAdapter(object):

    def test_lookup_bank_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[0])
            bank.use_isolated_bank_view()
            bank.use_plenary_item_view()
            # with pytest.raises(errors.NotFound):
            #     items = bank.get_items()
            # with pytest.raises(errors.NotFound):
            #     items = bank.get_items_by_genus_type(BLUE_TYPE)
            # for item_id in self.item_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         item = bank.get_item(item_id)
            # with pytest.raises(errors.NotFound):
            #     items = bank.get_items_by_ids(self.item_id_lists[0])

    def test_lookup_bank_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[0])
            bank.use_federated_bank_view()
            bank.use_plenary_item_view()
            assert bank.can_lookup_items()
            assert bank.get_items().available() == 1
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1
            assert bank.get_items_by_genus_type(BLUE_TYPE).next().ident == self.item_id_lists[2][1]
            bank.get_item(self.item_id_lists[2][1])
            for item_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    item = bank.get_item(self.item_id_lists[2][item_num])

    def test_lookup_bank_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[0])
            bank.use_federated_bank_view()
            bank.use_comparative_item_view()
            # print "START"
            assert bank.get_items().available() == 13
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 5
            for item in bank.get_items():
                bank.get_item(item.ident)
            item_ids = [item.ident for item in bank.get_items()]
            bank.get_items_by_ids(item_ids)
            for item_id in self.item_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    item = bank.get_item(item_id)
            item = bank.get_item(self.item_id_lists[2][1])
            for item_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    item = bank.get_item(self.item_id_lists[2][item_num])
            for item_id in self.item_id_lists[1]:
                    item = bank.get_item(item_id)
            for item_id in self.item_id_lists[3]:
                    item = bank.get_item(item_id)
            for item_id in self.item_id_lists[4]:
                    item = bank.get_item(item_id)
            for item_id in self.item_id_lists[5]:
                    item = bank.get_item(item_id)

    def test_lookup_bank_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[0])
            bank.use_isolated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 0
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_bank_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[1])
            bank.use_isolated_bank_view()
            bank.use_plenary_item_view()
            assert bank.get_items().available() == 3
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[1])
            bank.use_federated_bank_view()
            bank.use_plenary_item_view()
            assert bank.get_items().available() == 9
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_bank_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[1])
            bank.use_federated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 9
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_bank_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[1])
            bank.use_isolated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 3
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[2])
            bank.use_isolated_bank_view()
            bank.use_plenary_item_view()
            assert bank.get_items().available() == 1
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     items = bank.get_items()
            # with pytest.raises(errors.PermissionDenied):
            #     items = bank.get_items_by_genus_type(BLUE_TYPE)

    def test_lookup_bank_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[2])
            bank.use_federated_bank_view()
            bank.use_plenary_item_view()
            assert bank.get_items().available() == 1
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     items = bank.get_items()
            # with pytest.raises(errors.PermissionDenied):
            #     items = bank.get_items_by_genus_type(BLUE_TYPE)

    def test_lookup_bank_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[2])
            bank.use_federated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 4
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(bank.get_items().available(), 3)
            # self.assertEqual(bank.get_items_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_bank_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[2])
            bank.use_isolated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 1
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     items = bank.get_items()
            # with pytest.raises(errors.PermissionDenied):
            #     items = bank.get_items_by_genus_type(BLUE_TYPE)

    def test_lookup_bank_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[3])
            bank.use_isolated_bank_view()
            bank.use_plenary_item_view()
            assert bank.get_items().available() == 3
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[3])
            bank.use_federated_bank_view()
            bank.use_plenary_item_view()
            assert bank.get_items().available() == 3
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[3])
            bank.use_federated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 3
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bank_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[3])
            bank.use_isolated_bank_view()
            bank.use_comparative_item_view()
            assert bank.get_items().available() == 3
            assert bank.get_items_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_bank_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[0])
            bank.use_isolated_bank_view()
            with pytest.raises(errors.PermissionDenied):
                query = bank.get_item_query()

    def test_query_bank_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[0])
            bank.use_federated_bank_view()
            query = bank.get_item_query()
            query.match_display_name('red')
            assert bank.get_items_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert bank.get_items_by_query(query).available() == 5

    def test_query_bank_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[1])
            bank.use_isolated_bank_view()
            query = bank.get_item_query()
            query.match_display_name('red')
            assert bank.get_items_by_query(query).available() == 2

    def test_query_bank_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_assessment_mgr = Runtime().get_service_manager(
                'ASSESSMENT',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bank = janes_assessment_mgr.get_bank(self.bank_id_list[1])
            bank.use_federated_bank_view()
            query = bank.get_item_query()
            query.match_display_name('red')
            assert bank.get_items_by_query(query).available() == 6