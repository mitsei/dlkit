"""Unit tests of authorization sessions."""


import datetime
import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.authorization import objects as ABCObjects
from dlkit.abstract_osid.authorization import queries as ABCQueries
from dlkit.abstract_osid.authorization.objects import Authorization
from dlkit.abstract_osid.authorization.objects import AuthorizationList
from dlkit.abstract_osid.authorization.objects import Vault as ABCVault
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


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.authz_mgr = Runtime().get_manager(
        'AUTHORIZATION',
        implementation='JSON_1')
    if not is_never_authz(request.cls.service_config) and not uses_filesystem_only(request.cls.service_config):
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

        # Set up Bin create authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            CREATE_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Create for Test Authorizations'
        create_form.description = 'Bin Create Authorization for AuthorizationSession tests'
        bin_create_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin delete authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            DELETE_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Delete for Test Authorizations'
        create_form.description = 'Bin Delete Authorization for AuthorizationSession tests'
        bin_delete_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin lookup authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            LOOKUP_BIN_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Lookup for Test Authorizations'
        create_form.description = 'Bin Lookup Authorization for AuthorizationSession tests'
        bin_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin hierarchy access authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            ACCESS_BIN_HIERARCHY_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Hierarchy Access for Test Authorizations'
        create_form.description = 'Bin Hierarchy Access Authorization for AuthorizationSession tests'
        bin_hierarchy_modify_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Bin hierarchy modify authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            MODIFY_BIN_HIERARCHY_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Bin Hierarchy Modify for Test Authorizations'
        create_form.description = 'Bin Hierarchy Modify Authorization for AuthorizationSession tests'
        bin_hierarchy_modify_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource create authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            CREATE_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource create for Test Authorizations'
        create_form.description = 'Resource create Authorization for AuthorizationSession tests'
        resource_create_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource delete authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            DELETE_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource Delete for Test Authorizations'
        create_form.description = 'Resource Delete Authorization for AuthorizationSession tests'
        resource_delete_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource - Bin assignment authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            ASSIGN_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource Delete for Test Authorizations'
        create_form.description = 'Resource Delete Authorization for AuthorizationSession tests'
        resource_delete_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up Resource lookup authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            LOOKUP_RESOURCE_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Resource Lookup for Test Authorizations'
        create_form.description = 'Resource Lookup Authorization for AuthorizationSession tests'
        resource_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)

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

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' resource in bin 2 is also assigned to bin 7)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("authorization_session_class_fixture", "authorization_session_test_fixture")
class TestAuthorizationSession(object):
    """Tests for AuthorizationSession"""
    def test_get_vault_id(self):
        """Tests get_vault_id"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert self.catalog.get_vault_id() == self.catalog.ident

    def test_get_vault(self):
        """Tests get_vault"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert isinstance(self.catalog.get_vault(), ABCVault)

    def test_can_access_authorizations(self):
        """Tests can_access_authorizations"""
        if is_never_authz(self.service_config) or uses_filesystem_only(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_access_authorizations()

    def test_is_authorized(self):
        """Tests is_authorized"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert not self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[0])

    def test_is_authorized_1(self):
        """Tests is_authorized 1"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[1])

    def test_is_authorized_3(self):
        """Tests is_authorized 3"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[3])

    def test_is_authorized_4(self):
        """Tests is_authorized 4"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[4])

    def test_is_authorized_2(self):
        """Tests is_authorized 2"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert not self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[2])

    def test_is_authorized_5(self):
        """Tests is_authorized 5"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[5])

    def test_is_authorized_6(self):
        """Tests is_authorized 5"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert not self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[6])

    def test_is_authorized_7(self):
        """Tests is_authorized 5"""
        if not is_never_authz(self.service_config) and not uses_filesystem_only(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_RESOURCE_FUNCTION_ID, self.bin_id_list[7])

    def test_get_authorization_condition(self):
        """Tests get_authorization_condition"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorization_condition(True)

    def test_is_authorized_on_condition(self):
        """Tests is_authorized_on_condition"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_authorized_on_condition(True, True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_lookup_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3A000000000000000000000000%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def authorization_lookup_session_test_fixture(request):
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()

    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(num), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            object = request.cls.catalog.create_authorization(create_form)
            request.cls.authorization_list.append(object)
            request.cls.authorization_ids.append(object.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_authorization_lookup_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                for obj in catalog.get_authorizations():
                    catalog.delete_authorization(obj.ident)
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authorization_lookup_session_class_fixture", "authorization_lookup_session_test_fixture")
class TestAuthorizationLookupSession(object):
    """Tests for AuthorizationLookupSession"""
    def test_get_vault_id(self):
        """Tests get_vault_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_vault_id() == self.catalog.ident

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_vault(), ABCVault)

    def test_can_lookup_authorizations(self):
        """Tests can_lookup_authorizations"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        assert isinstance(self.catalog.can_lookup_authorizations(), bool)

    def test_use_comparative_authorization_view(self):
        """Tests use_comparative_authorization_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_authorization_view()

    def test_use_plenary_authorization_view(self):
        """Tests use_plenary_authorization_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_authorization_view()

    def test_use_federated_vault_view(self):
        """Tests use_federated_vault_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_vault_view()

    def test_use_isolated_vault_view(self):
        """Tests use_isolated_vault_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_vault_view()

    def test_use_effective_authorization_view(self):
        """Tests use_effective_authorization_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_effective_authorization_view()

    def test_use_any_effective_authorization_view(self):
        """Tests use_any_effective_authorization_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_any_effective_authorization_view()

    def test_use_implicit_authorization_view(self):
        """Tests use_implicit_authorization_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_implicit_authorization_view()

    def test_use_explicit_authorization_view(self):
        """Tests use_explicit_authorization_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_explicit_authorization_view()

    def test_get_authorization(self):
        """Tests get_authorization"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        if self.svc_mgr.supports_authorization_query():
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_vault_view()
                obj = self.catalog.get_authorization(self.authorization_list[0].ident)
                assert obj.ident == self.authorization_list[0].ident
                self.catalog.use_federated_vault_view()
                obj = self.catalog.get_authorization(self.authorization_list[0].ident)
                assert obj.ident == self.authorization_list[0].ident
            else:
                with pytest.raises(errors.NotFound):
                    self.catalog.get_authorization(self.fake_id)
        else:
            if not is_never_authz(self.service_config):
                self.catalog.use_isolated_vault_view()
                obj = self.catalog.get_authorization(self.authorization_list[0].ident)
                assert obj.ident == self.authorization_list[0].ident
                self.catalog.use_federated_vault_view()
                obj = self.catalog.get_authorization(self.authorization_list[0].ident)
                assert obj.ident == self.authorization_list[0].ident
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_authorization(self.fake_id)

    def test_get_authorizations_by_ids(self):
        """Tests get_authorizations_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        if self.svc_mgr.supports_authorization_query():
            objects = self.catalog.get_authorizations_by_ids(self.authorization_ids)
            assert isinstance(objects, AuthorizationList)
            self.catalog.use_federated_vault_view()
            objects = self.catalog.get_authorizations_by_ids(self.authorization_ids)
            assert isinstance(objects, AuthorizationList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_authorizations_by_ids(self.authorization_ids)
                assert isinstance(objects, AuthorizationList)
                self.catalog.use_federated_vault_view()
                objects = self.catalog.get_authorizations_by_ids(self.authorization_ids)
                assert objects.available() > 0
                assert isinstance(objects, AuthorizationList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_authorizations_by_ids(self.authorization_ids)

    def test_get_authorizations_by_genus_type(self):
        """Tests get_authorizations_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        if self.svc_mgr.supports_authorization_query():
            objects = self.catalog.get_authorizations_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AuthorizationList)
            self.catalog.use_federated_vault_view()
            objects = self.catalog.get_authorizations_by_genus_type(DEFAULT_GENUS_TYPE)
            assert isinstance(objects, AuthorizationList)
            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_authorizations_by_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AuthorizationList)
                self.catalog.use_federated_vault_view()
                objects = self.catalog.get_authorizations_by_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() > 0
                assert isinstance(objects, AuthorizationList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_authorizations_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_authorizations_by_parent_genus_type(self):
        """Tests get_authorizations_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        if self.svc_mgr.supports_authorization_query():
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AuthorizationList)
                self.catalog.use_federated_vault_view()
                objects = self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AuthorizationList)
            else:
                with pytest.raises(errors.Unimplemented):
                    # because the never_authz "tries harder" and runs the actual query...
                    #    whereas above the method itself in JSON returns an empty list
                    self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert isinstance(objects, AuthorizationList)
                self.catalog.use_federated_vault_view()
                objects = self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_GENUS_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AuthorizationList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_authorizations_by_parent_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_authorizations_by_record_type(self):
        """Tests get_authorizations_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        if self.svc_mgr.supports_authorization_query():
            objects = self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)
            assert isinstance(objects, AuthorizationList)
            self.catalog.use_federated_vault_view()
            objects = self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)
            assert objects.available() == 0
            assert isinstance(objects, AuthorizationList)
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)
                assert isinstance(objects, AuthorizationList)
                self.catalog.use_federated_vault_view()
                objects = self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)
                assert objects.available() == 0
                assert isinstance(objects, AuthorizationList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_authorizations_by_record_type(DEFAULT_TYPE)

    def test_get_authorizations_on_date(self):
        """Tests get_authorizations_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_on_date(True, True)

    def test_get_authorizations_for_resource(self):
        """Tests get_authorizations_for_resource"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_resource(True)

    def test_get_authorizations_for_resource_on_date(self):
        """Tests get_authorizations_for_resource_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_resource_on_date(True, True, True)

    def test_get_authorizations_for_agent(self):
        """Tests get_authorizations_for_agent"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_agent(True)

    def test_get_authorizations_for_agent_on_date(self):
        """Tests get_authorizations_for_agent_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_agent_on_date(True, True, True)

    def test_get_authorizations_for_function(self):
        """Tests get_authorizations_for_function"""
        results = self.session.get_authorizations_for_function(LOOKUP_RESOURCE_FUNCTION_ID)
        assert isinstance(results, AuthorizationList)
        if not is_never_authz(self.service_config):
            assert results.available() == 2
        else:
            assert results.available() == 0

    def test_get_authorizations_for_function_on_date(self):
        """Tests get_authorizations_for_function_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_function_on_date(True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_authorizations_for_resource_and_function(self):
        """Tests get_authorizations_for_resource_and_function"""
        pass

    def test_get_authorizations_for_resource_and_function_on_date(self):
        """Tests get_authorizations_for_resource_and_function_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_resource_and_function_on_date(True, True, True, True)

    @pytest.mark.skip('unimplemented test')
    def test_get_authorizations_for_agent_and_function(self):
        """Tests get_authorizations_for_agent_and_function"""
        pass

    def test_get_authorizations_for_agent_and_function_on_date(self):
        """Tests get_authorizations_for_agent_and_function_on_date"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_for_agent_and_function_on_date(True, True, True, True)

    def test_get_authorizations_by_qualifier(self):
        """Tests get_authorizations_by_qualifier"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorizations_by_qualifier(True)

    def test_get_explicit_authorization(self):
        """Tests get_explicit_authorization"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_explicit_authorization(True)

    def test_get_authorizations(self):
        """Tests get_authorizations"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList
        if self.svc_mgr.supports_authorization_query():
            objects = self.catalog.get_authorizations()
            assert isinstance(objects, AuthorizationList)
            self.catalog.use_federated_vault_view()
            objects = self.catalog.get_authorizations()
            assert isinstance(objects, AuthorizationList)

            if not is_never_authz(self.service_config):
                assert objects.available() > 0
            else:
                assert objects.available() == 0
        else:
            if not is_never_authz(self.service_config):
                objects = self.catalog.get_authorizations()
                assert isinstance(objects, AuthorizationList)
                self.catalog.use_federated_vault_view()
                objects = self.catalog.get_authorizations()
                assert objects.available() > 0
                assert isinstance(objects, AuthorizationList)
            else:
                with pytest.raises(errors.PermissionDenied):
                    self.catalog.get_authorizations()

    def test_get_authorization_with_alias(self):
        if not is_never_authz(self.service_config):
            # Because you can't create the alias with NEVER_AUTHZ
            self.catalog.alias_authorization(self.authorization_ids[0], ALIAS_ID)
            obj = self.catalog.get_authorization(ALIAS_ID)
            assert obj.get_id() == self.authorization_ids[0]


class FakeQuery:
    _cat_id_args_list = []


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_query_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)


@pytest.fixture(scope="function")
def authorization_query_session_test_fixture(request):
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = request.cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(color), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            create_form.display_name = 'Test Authorization ' + color
            create_form.description = (
                'Test Authorization for AuthorizationQuerySession tests, did I mention green')
            obj = request.cls.catalog.create_authorization(create_form)
            request.cls.authorization_list.append(obj)
            request.cls.authorization_ids.append(obj.ident)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_authorization_query_session(proxy=PROXY)

    request.cls.session = request.cls.catalog

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                for obj in catalog.get_authorizations():
                    catalog.delete_authorization(obj.ident)
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authorization_query_session_class_fixture", "authorization_query_session_test_fixture")
class TestAuthorizationQuerySession(object):
    """Tests for AuthorizationQuerySession"""
    def test_get_vault_id(self):
        """Tests get_vault_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_vault_id() == self.catalog.ident

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_vault(), ABCVault)

    def test_can_search_authorizations(self):
        """Tests can_search_authorizations"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        assert isinstance(self.session.can_search_authorizations(), bool)

    def test_use_federated_vault_view(self):
        """Tests use_federated_vault_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_vault_view()

    def test_use_isolated_vault_view(self):
        """Tests use_isolated_vault_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_vault_view()

    def test_use_implicit_authorization_view(self):
        """Tests use_implicit_authorization_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_implicit_authorization_view()

    def test_use_explicit_authorization_view(self):
        """Tests use_explicit_authorization_view"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.use_explicit_authorization_view()

    def test_get_authorization_query(self):
        """Tests get_authorization_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_authorization_query()
        assert isinstance(query, ABCQueries.AuthorizationQuery)

    def test_get_authorizations_by_query(self):
        """Tests get_authorizations_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        if not is_never_authz(self.service_config):
            query = self.session.get_authorization_query()
            query.match_display_name('orange')
            assert self.catalog.get_authorizations_by_query(query).available() == 2
            query.clear_display_name_terms()
            query.match_display_name('blue', match=False)
            assert self.session.get_authorizations_by_query(query).available() == 3
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_authorizations_by_query(FakeQuery())


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_admin_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        for num in [0, 1]:
            create_form = request.cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(num), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationLookupSession tests'
            object = request.cls.catalog.create_authorization(create_form)
            request.cls.authorization_list.append(object)
            request.cls.authorization_ids.append(object.ident)

        request.cls.form = request.cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': 'foo', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])
        request.cls.form.display_name = 'new Authorization'
        request.cls.form.description = 'description of Authorization'
        request.cls.form.genus_type = NEW_TYPE
        request.cls.osid_object = request.cls.catalog.create_authorization(request.cls.form)
    else:
        request.cls.catalog = request.cls.svc_mgr.get_authorization_admin_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                for obj in catalog.get_authorizations():
                    catalog.delete_authorization(obj.ident)
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_admin_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("authorization_admin_session_class_fixture", "authorization_admin_session_test_fixture")
class TestAuthorizationAdminSession(object):
    """Tests for AuthorizationAdminSession"""
    def test_get_vault_id(self):
        """Tests get_vault_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        if not is_never_authz(self.service_config):
            assert self.catalog.get_vault_id() == self.catalog.ident

    def test_get_vault(self):
        """Tests get_vault"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_vault(), ABCVault)

    def test_can_create_authorizations(self):
        """Tests can_create_authorizations"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        assert isinstance(self.catalog.can_create_authorizations(), bool)

    def test_can_create_authorization_with_record_types(self):
        """Tests can_create_authorization_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        assert isinstance(self.catalog.can_create_authorization_with_record_types(DEFAULT_TYPE), bool)

    def test_get_authorization_form_for_create_for_agent(self):
        """Tests get_authorization_form_for_create_for_agent"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': 'foo', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_authorization_form_for_create_for_agent(
                    AGENT_ID,
                    LOOKUP_RESOURCE_FUNCTION_ID,
                    Id(**{'identifier': 'foo', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                    [])

    def test_get_authorization_form_for_create_for_resource(self):
        """Tests get_authorization_form_for_create_for_resource"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_authorization_form_for_create_for_resource(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': 'foo', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            assert isinstance(form, OsidForm)
            assert not form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_authorization_form_for_create_for_resource(
                    AGENT_ID,
                    LOOKUP_RESOURCE_FUNCTION_ID,
                    Id(**{'identifier': 'foo', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                    [])

    def test_get_authorization_form_for_create_for_resource_and_trust(self):
        """Tests get_authorization_form_for_create_for_resource_and_trust"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorization_form_for_create_for_resource_and_trust(True, True, True, True, True)

    def test_create_authorization(self):
        """Tests create_authorization"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.authorization.objects import Authorization
        if not is_never_authz(self.service_config):
            assert isinstance(self.osid_object, Authorization)
            assert self.osid_object.display_name.text == 'new Authorization'
            assert self.osid_object.description.text == 'description of Authorization'
            assert self.osid_object.genus_type == NEW_TYPE
            with pytest.raises(errors.IllegalState):
                self.catalog.create_authorization(self.form)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_authorization('I Will Break You!')
            update_form = self.catalog.get_authorization_form_for_update(self.osid_object.ident)
            with pytest.raises(errors.InvalidArgument):
                self.catalog.create_authorization(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.create_authorization('foo')

    def test_can_update_authorizations(self):
        """Tests can_update_authorizations"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        assert isinstance(self.catalog.can_update_authorizations(), bool)

    def test_get_authorization_form_for_update(self):
        """Tests get_authorization_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        if not is_never_authz(self.service_config):
            form = self.catalog.get_authorization_form_for_update(self.osid_object.ident)
            assert isinstance(form, OsidForm)
            assert form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_authorization_form_for_update(['This is Doomed!'])
            with pytest.raises(errors.InvalidArgument):
                self.catalog.get_authorization_form_for_update(
                    Id(authority='Respect my Authoritay!',
                       namespace='authorization.{object_name}',
                       identifier='1'))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.get_authorization_form_for_update(self.fake_id)

    def test_update_authorization(self):
        """Tests update_authorization"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_authorization_form_for_update(self.osid_object.ident)
            form.display_name = 'new name'
            form.description = 'new description'
            form.set_genus_type(NEW_TYPE_2)
            updated_object = self.catalog.update_authorization(form)
            assert isinstance(updated_object, Authorization)
            assert updated_object.ident == self.osid_object.ident
            assert updated_object.display_name.text == 'new name'
            assert updated_object.description.text == 'new description'
            assert updated_object.genus_type == NEW_TYPE_2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.update_authorization('foo')

    def test_can_delete_authorizations(self):
        """Tests can_delete_authorizations"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        assert isinstance(self.catalog.can_delete_authorizations(), bool)

    def test_delete_authorization(self):
        """Tests delete_authorization"""
        if not is_never_authz(self.service_config):
            form = self.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': 'foo2', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            form.display_name = 'new Authorization'
            form.description = 'description of Authorization'
            form.genus_type = NEW_TYPE
            osid_object = self.catalog.create_authorization(form)
            self.catalog.delete_authorization(osid_object.ident)
            with pytest.raises(errors.NotFound):
                self.catalog.get_authorization(osid_object.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.delete_authorization(self.fake_id)

    def test_can_manage_authorization_aliases(self):
        """Tests can_manage_authorization_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.catalog.can_manage_authorization_aliases(), bool)

    def test_alias_authorization(self):
        """Tests alias_authorization"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        if not is_never_authz(self.service_config):
            alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
            self.catalog.alias_authorization(self.osid_object.ident, alias_id)
            aliased_object = self.catalog.get_authorization(alias_id)
            assert aliased_object.ident == self.osid_object.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.catalog.alias_authorization(self.fake_id, self.fake_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING'])
def authorization_vault_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.service_config = request.param
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationVaultSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault for Assignment'
        create_form.description = 'Test Vault for AuthorizationVaultSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_vault(create_form)
        agent_id = Id(authority='TEST', namespace='authentication.Agent', identifier='A_USER')
        for num in [0, 1, 2]:
            # Note that the json authorization service seems picky about ids.  Need to review.
            func_namespace = 'resource.Resource'
            func_authority = 'TEST'
            if num == 1:
                func_identifier = 'lookup'
            elif num == 2:
                func_identifier = 'query'
            else:
                func_identifier = 'admin'
            function_id = Id(authority=func_authority, namespace=func_namespace, identifier=func_identifier)
            qualifier_id = Id(authority='TEST', namespace='authorization.Qualifier', identifier='TEST_' + str(num))
            create_form = request.cls.catalog.get_authorization_form_for_create_for_agent(agent_id, function_id, qualifier_id, [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationVaultSession tests'
            obj = request.cls.catalog.create_authorization(create_form)
            request.cls.authorization_list.append(obj)
            request.cls.authorization_ids.append(obj.ident)
        request.cls.svc_mgr.assign_authorization_to_vault(
            request.cls.authorization_ids[1], request.cls.assigned_catalog.ident)
        request.cls.svc_mgr.assign_authorization_to_vault(
            request.cls.authorization_ids[2], request.cls.assigned_catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.unassign_authorization_from_vault(
                request.cls.authorization_ids[1], request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.unassign_authorization_from_vault(
                request.cls.authorization_ids[2], request.cls.assigned_catalog.ident)
            for obj in request.cls.catalog.get_authorizations():
                request.cls.catalog.delete_authorization(obj.ident)
            request.cls.svc_mgr.delete_vault(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_vault_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("authorization_vault_session_class_fixture", "authorization_vault_session_test_fixture")
class TestAuthorizationVaultSession(object):
    """Tests for AuthorizationVaultSession"""
    def test_use_comparative_vault_view(self):
        """Tests use_comparative_vault_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_vault_view()

    def test_use_plenary_vault_view(self):
        """Tests use_plenary_vault_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_vault_view()

    def test_can_lookup_authorization_vault_mappings(self):
        """Tests can_lookup_authorization_vault_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_authorization_vault_mappings()
        assert isinstance(result, bool)

    def test_get_authorization_ids_by_vault(self):
        """Tests get_authorization_ids_by_vault"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_authorization_ids_by_vault(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_authorization_ids_by_vault(self.fake_id)

    def test_get_authorizations_by_vault(self):
        """Tests get_authorizations_by_vault"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_authorizations_by_vault(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AuthorizationList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_authorizations_by_vault(self.fake_id)

    def test_get_authorizations_ids_by_vault(self):
        """Tests get_authorizations_ids_by_vault"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        if not is_never_authz(self.service_config):
            objects = self.svc_mgr.get_authorizations_ids_by_vault(self.assigned_catalog.ident)
            assert objects.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_authorizations_ids_by_vault(self.fake_id)

    def test_get_authorizations_by_vault(self):
        """Tests get_authorizations_by_vault"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        if not is_never_authz(self.service_config):
            results = self.session.get_authorizations_by_vault(self.assigned_catalog.ident)
            assert isinstance(results, ABCObjects.AuthorizationList)
            assert results.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_authorizations_by_vault(self.fake_id)

    def test_get_vault_ids_by_authorization(self):
        """Tests get_vault_ids_by_authorization"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        if not is_never_authz(self.service_config):
            cats = self.svc_mgr.get_vault_ids_by_authorization(self.authorization_ids[1])
            assert cats.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_ids_by_authorization(self.fake_id)

    def test_get_vault_by_authorization(self):
        """Tests get_vault_by_authorization"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_vault_by_authorization(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING'])
def authorization_vault_assignment_session_class_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.service_config = request.param
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationVaultAssignmentSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault for Assignment'
        create_form.description = 'Test Vault for AuthorizationVaultAssignmentSession tests assignment'
        request.cls.assigned_catalog = request.cls.svc_mgr.create_vault(create_form)
        agent_id = Id(authority='TEST', namespace='authentication.Agent', identifier='A_USER')
        for num in [0, 1, 2]:
            # Note that the json authorization service seems picky about ids.  Need to review.
            func_namespace = 'resource.Resource'
            func_authority = 'TEST'
            if num == 1:
                func_identifier = 'lookup'
            elif num == 2:
                func_identifier = 'query'
            else:
                func_identifier = 'admin'
            function_id = Id(authority=func_authority, namespace=func_namespace, identifier=func_identifier)
            qualifier_id = Id(authority='TEST', namespace='authorization.Qualifier', identifier='TEST_' + str(num))
            create_form = request.cls.catalog.get_authorization_form_for_create_for_agent(agent_id, function_id, qualifier_id, [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationVaultAssignmentSession tests'
            obj = request.cls.catalog.create_authorization(create_form)
            request.cls.authorization_list.append(obj)
            request.cls.authorization_ids.append(obj.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.catalog.get_authorizations():
                request.cls.catalog.delete_authorization(obj.ident)
            request.cls.svc_mgr.delete_vault(request.cls.assigned_catalog.ident)
            request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_vault_assignment_session_test_fixture(request):
    # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("authorization_vault_assignment_session_class_fixture", "authorization_vault_assignment_session_test_fixture")
class TestAuthorizationVaultAssignmentSession(object):
    """Tests for AuthorizationVaultAssignmentSession"""
    def test_can_assign_authorizations(self):
        """Tests can_assign_authorizations"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_authorizations()
        assert isinstance(result, bool)

    def test_can_assign_authorizations_to_vault(self):
        """Tests can_assign_authorizations_to_vault"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_authorizations_to_vault(self.assigned_catalog.ident)
        assert isinstance(result, bool)

    def test_get_assignable_vault_ids(self):
        """Tests get_assignable_vault_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_vault_ids(self.catalog.ident)
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_vault_ids(self.fake_id)

    def test_get_assignable_vault_ids_for_authorization(self):
        """Tests get_assignable_vault_ids_for_authorization"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_resource_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        if not is_never_authz(self.service_config):
            results = self.session.get_assignable_vault_ids_for_authorization(self.catalog.ident, self.authorization_ids[0])
            assert isinstance(results, IdList)

            # Because we're not deleting all banks from all tests, we might
            #   have some crufty banks here...but there should be at least 2.
            assert results.available() >= 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_assignable_vault_ids_for_authorization(self.fake_id, self.fake_id)

    def test_assign_authorization_to_vault(self):
        """Tests assign_authorization_to_vault"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_authorizations()
            assert results.available() == 0
            self.session.assign_authorization_to_vault(self.authorization_ids[1], self.assigned_catalog.ident)
            results = self.assigned_catalog.get_authorizations()
            assert results.available() == 1
            self.session.unassign_authorization_from_vault(
                self.authorization_ids[1],
                self.assigned_catalog.ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.assign_authorization_to_vault(self.fake_id, self.fake_id)

    def test_unassign_authorization_from_vault(self):
        """Tests unassign_authorization_from_vault"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        if not is_never_authz(self.service_config):
            results = self.assigned_catalog.get_authorizations()
            assert results.available() == 0
            self.session.assign_authorization_to_vault(
                self.authorization_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_authorizations()
            assert results.available() == 1
            self.session.unassign_authorization_from_vault(
                self.authorization_ids[1],
                self.assigned_catalog.ident)
            results = self.assigned_catalog.get_authorizations()
            assert results.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.unassign_authorization_from_vault(self.fake_id, self.fake_id)

    def test_reassign_authorization_to_vault(self):
        """Tests reassign_authorization_to_vault"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.reassign_authorization_to_vault(True, True, True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_lookup_session_class_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.service_config = request.param
    request.cls.catalogs = list()
    request.cls.catalog_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'Test Vault ' + str(num)
            create_form.description = 'Test Vault for authorization proxy manager tests'
            catalog = request.cls.svc_mgr.create_vault(create_form)
            request.cls.catalogs.append(catalog)
            request.cls.catalog_ids.append(catalog.ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_lookup_session_test_fixture(request):
    # From test_templates/resource.py::BinLookupSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("vault_lookup_session_class_fixture", "vault_lookup_session_test_fixture")
class TestVaultLookupSession(object):
    """Tests for VaultLookupSession"""
    def test_can_lookup_vaults(self):
        """Tests can_lookup_vaults"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        assert isinstance(self.session.can_lookup_vaults(), bool)

    def test_use_comparative_vault_view(self):
        """Tests use_comparative_vault_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_vault_view()

    def test_use_plenary_vault_view(self):
        """Tests use_plenary_vault_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_vault_view()

    def test_get_vault(self):
        """Tests get_vault"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        if not is_never_authz(self.service_config):
            catalog = self.svc_mgr.get_vault(self.catalogs[0].ident)
            assert catalog.ident == self.catalogs[0].ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault(self.fake_id)

    def test_get_vaults_by_ids(self):
        """Tests get_vaults_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_vaults_by_ids(self.catalog_ids)
            assert catalogs.available() == 2
            assert isinstance(catalogs, ABCObjects.VaultList)
            catalog_id_strs = [str(cat_id) for cat_id in self.catalog_ids]
            for index, catalog in enumerate(catalogs):
                assert str(catalog.ident) in catalog_id_strs
                catalog_id_strs.remove(str(catalog.ident))
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vaults_by_ids([self.fake_id])

    def test_get_vaults_by_genus_type(self):
        """Tests get_vaults_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_vaults_by_genus_type(DEFAULT_GENUS_TYPE)
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.VaultList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vaults_by_genus_type(DEFAULT_GENUS_TYPE)

    def test_get_vaults_by_parent_genus_type(self):
        """Tests get_vaults_by_parent_genus_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_vaults_by_parent_genus_type(True)

    def test_get_vaults_by_record_type(self):
        """Tests get_vaults_by_record_type"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_vaults_by_record_type(True)

    def test_get_vaults_by_provider(self):
        """Tests get_vaults_by_provider"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_vaults_by_provider(True)

    def test_get_vaults(self):
        """Tests get_vaults"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        if not is_never_authz(self.service_config):
            catalogs = self.svc_mgr.get_vaults()
            assert catalogs.available() > 0
            assert isinstance(catalogs, ABCObjects.VaultList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vaults()


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_query_session_class_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_query_session_test_fixture(request):
    # From test_templates/resource.py::BinQuerySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("vault_query_session_class_fixture", "vault_query_session_test_fixture")
class TestVaultQuerySession(object):
    """Tests for VaultQuerySession"""
    def test_can_search_vaults(self):
        """Tests can_search_vaults"""
        # From test_templates/resource.py::BinQuerySession::can_search_bins_template
        assert isinstance(self.session.can_search_vaults(), bool)

    def test_get_vault_query(self):
        """Tests get_vault_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_vault_query()
            assert isinstance(query, ABCQueries.VaultQuery)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_vault_query()

    def test_get_vaults_by_query(self):
        """Tests get_vaults_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        if not is_never_authz(self.service_config):
            query = self.session.get_vault_query()
            query.match_display_name('Test catalog')
            assert self.session.get_vaults_by_query(query).available() == 1
            query.clear_display_name_terms()
            query.match_display_name('Test catalog', match=False)
            assert self.session.get_vaults_by_query(query).available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.get_vaults_by_query('foo')


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_admin_session_class_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')


@pytest.fixture(scope="function")
def vault_admin_session_test_fixture(request):
    # From test_templates/resource.py::BinAdminSession::init_template
    if not is_never_authz(request.cls.service_config):
        # Initialize test catalog:
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for VaultAdminSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        # Initialize catalog to be deleted:
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault For Deletion'
        create_form.description = 'Test Vault for VaultAdminSession deletion test'
        request.cls.catalog_to_delete = request.cls.svc_mgr.create_vault(create_form)

    request.cls.session = request.cls.svc_mgr

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("vault_admin_session_class_fixture", "vault_admin_session_test_fixture")
class TestVaultAdminSession(object):
    """Tests for VaultAdminSession"""
    def test_can_create_vaults(self):
        """Tests can_create_vaults"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        assert isinstance(self.svc_mgr.can_create_vaults(), bool)

    def test_can_create_vault_with_record_types(self):
        """Tests can_create_vault_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        assert isinstance(self.svc_mgr.can_create_vault_with_record_types(DEFAULT_TYPE), bool)

    def test_get_vault_form_for_create(self):
        """Tests get_vault_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.authorization.objects import VaultForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_vault_form_for_create([])
            assert isinstance(catalog_form, OsidCatalogForm)
            assert not catalog_form.is_for_update()
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.get_vault_form_for_create([1])
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_form_for_create([])

    def test_create_vault(self):
        """Tests create_vault"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.authorization.objects import Vault
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_vault_form_for_create([])
            catalog_form.display_name = 'Test Vault'
            catalog_form.description = 'Test Vault for VaultAdminSession.create_vault tests'
            new_catalog = self.svc_mgr.create_vault(catalog_form)
            assert isinstance(new_catalog, OsidCatalog)
            with pytest.raises(errors.IllegalState):
                self.svc_mgr.create_vault(catalog_form)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_vault('I Will Break You!')
            update_form = self.svc_mgr.get_vault_form_for_update(new_catalog.ident)
            with pytest.raises(errors.InvalidArgument):
                self.svc_mgr.create_vault(update_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.create_vault('foo')

    def test_can_update_vaults(self):
        """Tests can_update_vaults"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        assert isinstance(self.svc_mgr.can_update_vaults(), bool)

    def test_get_vault_form_for_update(self):
        """Tests get_vault_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.authorization.objects import VaultForm
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_vault_form_for_update(self.catalog.ident)
            assert isinstance(catalog_form, OsidCatalogForm)
            assert catalog_form.is_for_update()
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_form_for_update(self.fake_id)

    def test_update_vault(self):
        """Tests update_vault"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        if not is_never_authz(self.service_config):
            catalog_form = self.svc_mgr.get_vault_form_for_update(self.catalog.ident)
            # Update some elements here?
            self.svc_mgr.update_vault(catalog_form)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.update_vault('foo')

    def test_can_delete_vaults(self):
        """Tests can_delete_vaults"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        assert isinstance(self.svc_mgr.can_delete_vaults(), bool)

    def test_delete_vault(self):
        """Tests delete_vault"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        if not is_never_authz(self.service_config):
            cat_id = self.catalog_to_delete.ident
            self.svc_mgr.delete_vault(cat_id)
            with pytest.raises(errors.NotFound):
                self.svc_mgr.get_vault(cat_id)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.delete_vault(self.fake_id)

    def test_can_manage_vault_aliases(self):
        """Tests can_manage_vault_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        assert isinstance(self.svc_mgr.can_manage_vault_aliases(), bool)

    def test_alias_vault(self):
        """Tests alias_vault"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('authorization.Vault%3Amy-alias%40ODL.MIT.EDU')

        if not is_never_authz(self.service_config):
            self.svc_mgr.alias_vault(self.catalog_to_delete.ident, alias_id)
            aliased_catalog = self.svc_mgr.get_vault(alias_id)
            assert self.catalog_to_delete.ident == aliased_catalog.ident
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.alias_vault(self.fake_id, alias_id)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_hierarchy_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Vault ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_vault(create_form)
        request.cls.svc_mgr.add_root_vault(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_vault(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_vault(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_vault(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_vault(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_vaults(request.cls.catalogs['Root'].ident)
            request.cls.svc_mgr.remove_root_vault(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_vault(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_hierarchy_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchySession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("vault_hierarchy_session_class_fixture", "vault_hierarchy_session_test_fixture")
class TestVaultHierarchySession(object):
    """Tests for VaultHierarchySession"""
    def test_get_vault_hierarchy_id(self):
        """Tests get_vault_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_vault_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_vault_hierarchy(self):
        """Tests get_vault_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_vault_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_hierarchy()

    def test_can_access_vault_hierarchy(self):
        """Tests can_access_vault_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        assert isinstance(self.svc_mgr.can_access_vault_hierarchy(), bool)

    def test_use_comparative_vault_view(self):
        """Tests use_comparative_vault_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_vault_view()

    def test_use_plenary_vault_view(self):
        """Tests use_plenary_vault_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_vault_view()

    def test_get_root_vault_ids(self):
        """Tests get_root_vault_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        if not is_never_authz(self.service_config):
            root_ids = self.svc_mgr.get_root_vault_ids()
            assert isinstance(root_ids, IdList)
            # probably should be == 1, but we seem to be getting test cruft,
            # and I can't pinpoint where it's being introduced.
            assert root_ids.available() >= 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_vault_ids()

    def test_get_root_vaults(self):
        """Tests get_root_vaults"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.authorization.objects import VaultList
        if not is_never_authz(self.service_config):
            roots = self.svc_mgr.get_root_vaults()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_root_vaults()

    def test_has_parent_vaults(self):
        """Tests has_parent_vaults"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_parent_vaults(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_parent_vaults(self.catalogs['Child 1'].ident)
            assert self.svc_mgr.has_parent_vaults(self.catalogs['Child 2'].ident)
            assert self.svc_mgr.has_parent_vaults(self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.has_parent_vaults(self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_parent_vaults(self.fake_id)

    def test_is_parent_of_vault(self):
        """Tests is_parent_of_vault"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_parent_of_vault(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_parent_of_vault(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
            assert self.svc_mgr.is_parent_of_vault(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident)
            assert not self.svc_mgr.is_parent_of_vault(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_parent_of_vault(self.fake_id, self.fake_id)

    def test_get_parent_vault_ids(self):
        """Tests get_parent_vault_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_vault_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_vault_ids(self.fake_id)

    def test_get_parent_vaults(self):
        """Tests get_parent_vaults"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_parent_vaults(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Root'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_parent_vaults(self.fake_id)

    def test_is_ancestor_of_vault(self):
        """Tests is_ancestor_of_vault"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_vault,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_ancestor_of_vault(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_vault(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_vault(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_vault(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_vault(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_vaults(self):
        """Tests has_child_vaults"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.has_child_vaults(self.catalogs['Child 1'].ident), bool)
            assert self.svc_mgr.has_child_vaults(self.catalogs['Root'].ident)
            assert self.svc_mgr.has_child_vaults(self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.has_child_vaults(self.catalogs['Child 2'].ident)
            assert not self.svc_mgr.has_child_vaults(self.catalogs['Grandchild 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.has_child_vaults(self.fake_id)

    def test_is_child_of_vault(self):
        """Tests is_child_of_vault"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        if not is_never_authz(self.service_config):
            assert isinstance(self.svc_mgr.is_child_of_vault(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool)
            assert self.svc_mgr.is_child_of_vault(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident)
            assert self.svc_mgr.is_child_of_vault(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident)
            assert not self.svc_mgr.is_child_of_vault(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_child_of_vault(self.fake_id, self.fake_id)

    def test_get_child_vault_ids(self):
        """Tests get_child_vault_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_vault_ids(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, IdList)
            assert catalog_list.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_vault_ids(self.fake_id)

    def test_get_child_vaults(self):
        """Tests get_child_vaults"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        if not is_never_authz(self.service_config):
            catalog_list = self.svc_mgr.get_child_vaults(self.catalogs['Child 1'].ident)
            assert isinstance(catalog_list, OsidList)
            assert catalog_list.available() == 1
            assert catalog_list.next().display_name.text == 'Grandchild 1'
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_child_vaults(self.fake_id)

    def test_is_descendant_of_vault(self):
        """Tests is_descendant_of_vault"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        if not is_never_authz(self.service_config):
            pytest.raises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_vault,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.is_descendant_of_vault(self.fake_id, self.fake_id)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_vault(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_vault(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_vault(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_vault(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_vault_node_ids(self):
        """Tests get_vault_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_vault_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_node_ids(self.fake_id, 1, 2, False)

    def test_get_vault_nodes(self):
        """Tests get_vault_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        if not is_never_authz(self.service_config):
            node = self.svc_mgr.get_vault_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
            assert isinstance(node, OsidNode)
            assert not node.is_root()
            assert not node.is_leaf()
            assert node.get_child_ids().available() == 1
            assert isinstance(node.get_child_ids(), IdList)
            assert node.get_parent_ids().available() == 1
            assert isinstance(node.get_parent_ids(), IdList)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_nodes(self.fake_id, 1, 2, False)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_hierarchy_design_session_class_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    request.cls.catalogs = dict()
    request.cls.fake_id = Id('resource.Resource%3Afake%40DLKIT.MIT.EDU')
    if not is_never_authz(request.cls.service_config):
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = request.cls.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Vault ' + name
            request.cls.catalogs[name] = request.cls.svc_mgr.create_vault(create_form)
        request.cls.svc_mgr.add_root_vault(request.cls.catalogs['Root'].ident)
        request.cls.svc_mgr.add_child_vault(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 1'].ident)
        request.cls.svc_mgr.add_child_vault(request.cls.catalogs['Root'].ident, request.cls.catalogs['Child 2'].ident)
        request.cls.svc_mgr.add_child_vault(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.remove_child_vault(request.cls.catalogs['Child 1'].ident, request.cls.catalogs['Grandchild 1'].ident)
            request.cls.svc_mgr.remove_child_vaults(request.cls.catalogs['Root'].ident)
            for cat_name in request.cls.catalogs:
                request.cls.svc_mgr.delete_vault(request.cls.catalogs[cat_name].ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_hierarchy_design_session_test_fixture(request):
    # From test_templates/resource.py::BinHierarchyDesignSession::init_template
    request.cls.session = request.cls.svc_mgr


@pytest.mark.usefixtures("vault_hierarchy_design_session_class_fixture", "vault_hierarchy_design_session_test_fixture")
class TestVaultHierarchyDesignSession(object):
    """Tests for VaultHierarchyDesignSession"""
    def test_get_vault_hierarchy_id(self):
        """Tests get_vault_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_vault_hierarchy_id()
        assert isinstance(hierarchy_id, Id)

    def test_get_vault_hierarchy(self):
        """Tests get_vault_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        if not is_never_authz(self.service_config):
            hierarchy = self.svc_mgr.get_vault_hierarchy()
            assert isinstance(hierarchy, Hierarchy)
        else:
            with pytest.raises(errors.PermissionDenied):
                self.svc_mgr.get_vault_hierarchy()

    def test_can_modify_vault_hierarchy(self):
        """Tests can_modify_vault_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        assert isinstance(self.session.can_modify_vault_hierarchy(), bool)

    def test_add_root_vault(self):
        """Tests add_root_vault"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_vaults()
            assert isinstance(roots, OsidList)
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_root_vault(self.fake_id)

    def test_remove_root_vault(self):
        """Tests remove_root_vault"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        if not is_never_authz(self.service_config):
            roots = self.session.get_root_vaults()
            assert roots.available() == 1

            create_form = self.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'new root'
            create_form.description = 'Test Vault root'
            new_vault = self.svc_mgr.create_vault(create_form)
            self.svc_mgr.add_root_vault(new_vault.ident)

            roots = self.session.get_root_vaults()
            assert roots.available() == 2

            self.session.remove_root_vault(new_vault.ident)

            roots = self.session.get_root_vaults()
            assert roots.available() == 1
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_root_vault(self.fake_id)

    def test_add_child_vault(self):
        """Tests add_child_vault"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        if not is_never_authz(self.service_config):
            # this is tested in the setUpClass
            children = self.session.get_child_vaults(self.catalogs['Root'].ident)
            assert isinstance(children, OsidList)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.add_child_vault(self.fake_id, self.fake_id)

    def test_remove_child_vault(self):
        """Tests remove_child_vault"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_vaults(self.catalogs['Root'].ident)
            assert children.available() == 2

            create_form = self.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'test child'
            create_form.description = 'Test Vault child'
            new_vault = self.svc_mgr.create_vault(create_form)
            self.svc_mgr.add_child_vault(
                self.catalogs['Root'].ident,
                new_vault.ident)

            children = self.session.get_child_vaults(self.catalogs['Root'].ident)
            assert children.available() == 3

            self.session.remove_child_vault(
                self.catalogs['Root'].ident,
                new_vault.ident)

            children = self.session.get_child_vaults(self.catalogs['Root'].ident)
            assert children.available() == 2
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_vault(self.fake_id, self.fake_id)

    def test_remove_child_vaults(self):
        """Tests remove_child_vaults"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        if not is_never_authz(self.service_config):
            children = self.session.get_child_vaults(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0

            create_form = self.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'test great grandchild'
            create_form.description = 'Test Vault child'
            new_vault = self.svc_mgr.create_vault(create_form)
            self.svc_mgr.add_child_vault(
                self.catalogs['Grandchild 1'].ident,
                new_vault.ident)

            children = self.session.get_child_vaults(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 1

            self.session.remove_child_vaults(self.catalogs['Grandchild 1'].ident)

            children = self.session.get_child_vaults(self.catalogs['Grandchild 1'].ident)
            assert children.available() == 0
        else:
            with pytest.raises(errors.PermissionDenied):
                self.session.remove_child_vaults(self.fake_id)
