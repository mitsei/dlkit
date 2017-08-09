"""TestAuthZ implementations of resource.Resource"""

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

LOOKUP_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
SEARCH_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
CREATE_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
DELETE_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
ASSIGN_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': 'resource.ResourceBin', 'authority': 'ODL.MIT.EDU'})
CREATE_BIN_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
DELETE_BIN_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
LOOKUP_BIN_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
ACCESS_BIN_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
MODIFY_BIN_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': 'resource.Bin', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('resource.Bin%3AROOT%40ODL.MIT.EDU')
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

        request.cls.bin_list = list()
        request.cls.bin_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.resource_mgr = Runtime().get_service_manager(
            'RESOURCE',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.resource_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for Testing Authorization Number: ' + str(num)
            bin = request.cls.resource_mgr.create_bin(create_form)
            request.cls.bin_list.append(bin)
            request.cls.bin_id_list.append(bin.ident)

        request.cls.resource_mgr.add_root_bin(request.cls.bin_id_list[0])
        request.cls.resource_mgr.add_child_bin(request.cls.bin_id_list[0], request.cls.bin_id_list[1])
        request.cls.resource_mgr.add_child_bin(request.cls.bin_id_list[0], request.cls.bin_id_list[2])
        request.cls.resource_mgr.add_child_bin(request.cls.bin_id_list[1], request.cls.bin_id_list[3])
        request.cls.resource_mgr.add_child_bin(request.cls.bin_id_list[1], request.cls.bin_id_list[4])
        request.cls.resource_mgr.add_child_bin(request.cls.bin_id_list[2], request.cls.bin_id_list[5])

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' resource in bin 2 is also assigned to bin 7)

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up Bin lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up Resource lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                request.cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Resource lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                request.cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Resource search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_RESOURCE_FUNCTION_ID,
                request.cls.bin_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up Resource search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_RESOURCE_FUNCTION_ID,
                request.cls.bin_id_list[num],
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
            for catalog in request.cls.resource_mgr.get_bins():
                for obj in catalog.get_resources():
                    catalog.delete_resource(obj.ident)
                request.cls.resource_mgr.delete_bin(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authz_adapter_test_fixture(request):
    request.cls.resource_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        for bin_ in request.cls.bin_list:
            request.cls.resource_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = bin_.get_resource_form_for_create([])
                create_form.display_name = color + ' ' + str(count) + ' Resource'
                create_form.description = color + ' resource for authz adapter tests from Bin number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                resource = bin_.create_resource(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.resource_mgr.assign_resource_to_bin(
                        resource.ident,
                        request.cls.bin_id_list[7])
                request.cls.resource_id_lists[count].append(resource.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, bin_ in enumerate(request.cls.bin_list):
                for resource_id in request.cls.resource_id_lists[index]:
                    bin_.delete_resource(resource_id)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture", "authz_adapter_test_fixture")
class TestResourceAuthzAdapter(object):

    def test_lookup_bin_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            # with pytest.raises(errors.NotFound):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.NotFound):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)
            # for resource_id in self.resource_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         resource = bin.get_resource(resource_id)
            # with pytest.raises(errors.NotFound):
            #     resources = bin.get_resources_by_ids(self.resource_id_lists[0])

    def test_lookup_bin_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.can_lookup_resources()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).next().ident == self.resource_id_lists[2][1]
            bin.get_resource(self.resource_id_lists[2][1])
            for resource_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    resource = bin.get_resource(self.resource_id_lists[2][resource_num])

    def test_lookup_bin_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            # print "START"
            assert bin.get_resources().available() == 13
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 5
            for resource in bin.get_resources():
                bin.get_resource(resource.ident)
            resource_ids = [resource.ident for resource in bin.get_resources()]
            bin.get_resources_by_ids(resource_ids)
            for resource_id in self.resource_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    resource = bin.get_resource(resource_id)
            resource = bin.get_resource(self.resource_id_lists[2][1])
            for resource_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    resource = bin.get_resource(self.resource_id_lists[2][resource_num])
            for resource_id in self.resource_id_lists[1]:
                    resource = bin.get_resource(resource_id)
            for resource_id in self.resource_id_lists[3]:
                    resource = bin.get_resource(resource_id)
            for resource_id in self.resource_id_lists[4]:
                    resource = bin.get_resource(resource_id)
            for resource_id in self.resource_id_lists[5]:
                    resource = bin.get_resource(resource_id)

    def test_lookup_bin_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 0
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_bin_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bin_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 9
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_bin_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 9
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_bin_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bin_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)

    def test_lookup_bin_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)

    def test_lookup_bin_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 4
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(bin.get_resources().available(), 3)
            # self.assertEqual(bin.get_resources_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_bin_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[2])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 1
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources()
            # with pytest.raises(errors.PermissionDenied):
            #     resources = bin.get_resources_by_genus_type(BLUE_TYPE)

    def test_lookup_bin_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_isolated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bin_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_federated_bin_view()
            bin.use_plenary_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bin_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_federated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_bin_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[3])
            bin.use_isolated_bin_view()
            bin.use_comparative_resource_view()
            assert bin.get_resources().available() == 3
            assert bin.get_resources_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_bin_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_isolated_bin_view()
            with pytest.raises(errors.PermissionDenied):
                query = bin.get_resource_query()

    def test_query_bin_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[0])
            bin.use_federated_bin_view()
            query = bin.get_resource_query()
            query.match_display_name('red')
            assert bin.get_resources_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert bin.get_resources_by_query(query).available() == 5

    def test_query_bin_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_isolated_bin_view()
            query = bin.get_resource_query()
            query.match_display_name('red')
            assert bin.get_resources_by_query(query).available() == 2

    def test_query_bin_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_resource_mgr = Runtime().get_service_manager(
                'RESOURCE',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            bin = janes_resource_mgr.get_bin(self.bin_id_list[1])
            bin.use_federated_bin_view()
            query = bin.get_resource_query()
            query.match_display_name('red')
            assert bin.get_resources_by_query(query).available() == 6
