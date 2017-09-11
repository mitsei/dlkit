"""TestAuthZ implementations of learning.Proficiency"""

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

LOOKUP_PROFICIENCY_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'learning.Proficiency', 'authority': 'ODL.MIT.EDU'})
SEARCH_PROFICIENCY_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'learning.Proficiency', 'authority': 'ODL.MIT.EDU'})
CREATE_PROFICIENCY_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'learning.Proficiency', 'authority': 'ODL.MIT.EDU'})
DELETE_PROFICIENCY_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'learning.Proficiency', 'authority': 'ODL.MIT.EDU'})
ASSIGN_PROFICIENCY_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'learning.ProficiencyObjectiveBank', 'authority': 'ODL.MIT.EDU'})
CREATE_OBJECTIVEBANK_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'learning.ObjectiveBank', 'authority': 'ODL.MIT.EDU'})
DELETE_OBJECTIVEBANK_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'learning.ObjectiveBank', 'authority': 'ODL.MIT.EDU'})
LOOKUP_OBJECTIVEBANK_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'learning.ObjectiveBank', 'authority': 'ODL.MIT.EDU'})
ACCESS_OBJECTIVEBANK_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'learning.ObjectiveBank', 'authority': 'ODL.MIT.EDU'})
MODIFY_OBJECTIVEBANK_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'learning.ObjectiveBank', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('learning.ObjectiveBank%3AROOT%40ODL.MIT.EDU')
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

        request.cls.objective_bank_list = list()
        request.cls.objective_bank_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.learning_mgr = Runtime().get_service_manager(
            'LEARNING',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.learning_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for Testing Authorization Number: ' + str(num)
            objective_bank = request.cls.learning_mgr.create_objective_bank(create_form)
            request.cls.objective_bank_list.append(objective_bank)
            request.cls.objective_bank_id_list.append(objective_bank.ident)

        request.cls.learning_mgr.add_root_objective_bank(request.cls.objective_bank_id_list[0])
        request.cls.learning_mgr.add_child_objective_bank(request.cls.objective_bank_id_list[0], request.cls.objective_bank_id_list[1])
        request.cls.learning_mgr.add_child_objective_bank(request.cls.objective_bank_id_list[0], request.cls.objective_bank_id_list[2])
        request.cls.learning_mgr.add_child_objective_bank(request.cls.objective_bank_id_list[1], request.cls.objective_bank_id_list[3])
        request.cls.learning_mgr.add_child_objective_bank(request.cls.objective_bank_id_list[1], request.cls.objective_bank_id_list[4])
        request.cls.learning_mgr.add_child_objective_bank(request.cls.objective_bank_id_list[2], request.cls.objective_bank_id_list[5])

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' proficiency in objective_bank 2 is also assigned to objective_bank 7)

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up ObjectiveBank lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_OBJECTIVEBANK_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up Proficiency lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_PROFICIENCY_FUNCTION_ID,
                request.cls.objective_bank_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Proficiency lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_PROFICIENCY_FUNCTION_ID,
                request.cls.objective_bank_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Proficiency search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_PROFICIENCY_FUNCTION_ID,
                request.cls.objective_bank_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Proficiency search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_PROFICIENCY_FUNCTION_ID,
                request.cls.objective_bank_id_list[num],
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
            for catalog in request.cls.learning_mgr.get_objective_banks():
                for obj in catalog.get_proficiencies():
                    catalog.delete_proficiency(obj.ident)
                request.cls.learning_mgr.delete_objective_bank(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authz_adapter_test_fixture(request):
    request.cls.proficiency_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        resource_id = Id(authority='TEST', namespace='resource.Resource', identifier='TEST')
        create_form = request.cls.objective_bank_list[0].get_objective_form_for_create([])
        create_form.display_name = 'Objective for Proficiency Tests'
        create_form.description = 'Objective for authz adapter tests for Proficiency'
        request.cls.objective = request.cls.objective_bank_list[0].create_objective(create_form)
        for objective_bank_ in request.cls.objective_bank_list:
            request.cls.proficiency_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = objective_bank_.get_proficiency_form_for_create(resource_id, request.cls.objective.ident, [])
                create_form.display_name = color + ' ' + str(count) + ' Proficiency'
                create_form.description = color + ' proficiency for authz adapter tests from ObjectiveBank number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                proficiency = objective_bank_.create_proficiency(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.learning_mgr.assign_proficiency_to_objective_bank(
                        proficiency.ident,
                        request.cls.objective_bank_id_list[7])
                request.cls.proficiency_id_lists[count].append(proficiency.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, objective_bank_ in enumerate(request.cls.objective_bank_list):
                for proficiency_id in request.cls.proficiency_id_lists[index]:
                    objective_bank_.delete_proficiency(proficiency_id)
            request.cls.objective_bank_list[0].delete_objective(request.cls.objective.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture", "authz_adapter_test_fixture")
class TestProficiencyAuthzAdapter(object):

    def test_lookup_objective_bank_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[0])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            # with pytest.raises(errors.NotFound):
            #     proficiencies = objective_bank.get_proficiencies()
            # with pytest.raises(errors.NotFound):
            #     proficiencies = objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE)
            # for proficiency_id in self.proficiency_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         proficiency = objective_bank.get_proficiency(proficiency_id)
            # with pytest.raises(errors.NotFound):
            #     proficiencies = objective_bank.get_proficiencies_by_ids(self.proficiency_id_lists[0])

    def test_lookup_objective_bank_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[0])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.can_lookup_proficiencies()
            assert objective_bank.get_proficiencies().available() == 1
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).next().ident == self.proficiency_id_lists[2][1]
            objective_bank.get_proficiency(self.proficiency_id_lists[2][1])
            for proficiency_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    proficiency = objective_bank.get_proficiency(self.proficiency_id_lists[2][proficiency_num])

    def test_lookup_objective_bank_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[0])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            # print "START"
            assert objective_bank.get_proficiencies().available() == 13
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 5
            for proficiency in objective_bank.get_proficiencies():
                objective_bank.get_proficiency(proficiency.ident)
            proficiency_ids = [proficiency.ident for proficiency in objective_bank.get_proficiencies()]
            objective_bank.get_proficiencies_by_ids(proficiency_ids)
            for proficiency_id in self.proficiency_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    proficiency = objective_bank.get_proficiency(proficiency_id)
            proficiency = objective_bank.get_proficiency(self.proficiency_id_lists[2][1])
            for proficiency_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    proficiency = objective_bank.get_proficiency(self.proficiency_id_lists[2][proficiency_num])
            for proficiency_id in self.proficiency_id_lists[1]:
                    proficiency = objective_bank.get_proficiency(proficiency_id)
            for proficiency_id in self.proficiency_id_lists[3]:
                    proficiency = objective_bank.get_proficiency(proficiency_id)
            for proficiency_id in self.proficiency_id_lists[4]:
                    proficiency = objective_bank.get_proficiency(proficiency_id)
            for proficiency_id in self.proficiency_id_lists[5]:
                    proficiency = objective_bank.get_proficiency(proficiency_id)

    def test_lookup_objective_bank_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[0])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 0
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_objective_bank_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[1])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 3
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_objective_bank_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[1])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 9
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_objective_bank_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[1])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 9
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_objective_bank_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[1])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 3
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_objective_bank_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[2])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 1
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     proficiencies = objective_bank.get_proficiencies()
            # with pytest.raises(errors.PermissionDenied):
            #     proficiencies = objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE)

    def test_lookup_objective_bank_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[2])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 1
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     proficiencies = objective_bank.get_proficiencies()
            # with pytest.raises(errors.PermissionDenied):
            #     proficiencies = objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE)

    def test_lookup_objective_bank_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[2])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 4
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(objective_bank.get_proficiencies().available(), 3)
            # self.assertEqual(objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_objective_bank_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[2])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 1
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     proficiencies = objective_bank.get_proficiencies()
            # with pytest.raises(errors.PermissionDenied):
            #     proficiencies = objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE)

    def test_lookup_objective_bank_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[3])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 3
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_objective_bank_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[3])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_plenary_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 3
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_objective_bank_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[3])
            objective_bank.use_federated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 3
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_objective_bank_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[3])
            objective_bank.use_isolated_objective_bank_view()
            objective_bank.use_comparative_proficiency_view()
            assert objective_bank.get_proficiencies().available() == 3
            assert objective_bank.get_proficiencies_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_objective_bank_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[0])
            objective_bank.use_isolated_objective_bank_view()
            with pytest.raises(errors.PermissionDenied):
                query = objective_bank.get_proficiency_query()

    def test_query_objective_bank_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[0])
            objective_bank.use_federated_objective_bank_view()
            query = objective_bank.get_proficiency_query()
            query.match_display_name('red')
            assert objective_bank.get_proficiencies_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert objective_bank.get_proficiencies_by_query(query).available() == 5

    def test_query_objective_bank_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[1])
            objective_bank.use_isolated_objective_bank_view()
            query = objective_bank.get_proficiency_query()
            query.match_display_name('red')
            assert objective_bank.get_proficiencies_by_query(query).available() == 2

    def test_query_objective_bank_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_learning_mgr = Runtime().get_service_manager(
                'LEARNING',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            objective_bank = janes_learning_mgr.get_objective_bank(self.objective_bank_id_list[1])
            objective_bank.use_federated_objective_bank_view()
            query = objective_bank.get_proficiency_query()
            query.match_display_name('red')
            assert objective_bank.get_proficiencies_by_query(query).available() == 6
