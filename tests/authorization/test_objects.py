"""Unit tests of authorization objects."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only
from dlkit.abstract_osid.authorization import objects as ABCObjects
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidCatalog
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)
LOOKUP_RESOURCE_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationQuerySession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        create_form = request.cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': str('foo'), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])
        create_form.display_name = 'Test Authorization'
        create_form.description = (
            'Test Authorization for Authorization tests')
        obj = request.cls.catalog.create_authorization(create_form)
        request.cls.object = obj

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                for obj in catalog.get_authorizations():
                    catalog.delete_authorization(obj.ident)
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_test_fixture(request):
    pass


@pytest.mark.usefixtures("authorization_class_fixture", "authorization_test_fixture")
class TestAuthorization(object):
    """Tests for Authorization"""
    def test_is_implicit(self):
        """Tests is_implicit"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.is_implicit(), bool)

    def test_has_resource(self):
        """Tests has_resource"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_resource(), bool)

    def test_get_resource_id(self):
        """Tests get_resource_id"""
        if not is_never_authz(self.service_config):
            # no resource, so throws IllegalState
            with pytest.raises(errors.IllegalState):
                self.object.get_resource_id()

    def test_get_resource(self):
        """Tests get_resource"""
        if not is_never_authz(self.service_config):
            # no resource, so throws IllegalState
            with pytest.raises(errors.IllegalState):
                self.object.get_resource()

    def test_has_trust(self):
        """Tests has_trust"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_trust(), bool)

    def test_get_trust_id(self):
        """Tests get_trust_id"""
        if not is_never_authz(self.service_config):
            # no trust, so throws IllegalState
            with pytest.raises(errors.IllegalState):
                self.object.get_trust_id()

    def test_get_trust(self):
        """Tests get_trust"""
        if not is_never_authz(self.service_config):
            # no trust, so throws IllegalState
            with pytest.raises(errors.IllegalState):
                self.object.get_trust()

    def test_has_agent(self):
        """Tests has_agent"""
        if not is_never_authz(self.service_config):
            assert isinstance(self.object.has_agent(), bool)

    def test_get_agent_id(self):
        """Tests get_agent_id"""
        if not is_never_authz(self.service_config):
            result = self.object.get_agent_id()
            assert isinstance(result, Id)
            assert str(result) == str(AGENT_ID)

    def test_get_agent(self):
        """Tests get_agent"""
        if not is_never_authz(self.service_config):
            # because we don't have Agency implemented in authentication
            with pytest.raises(AttributeError):
                self.object.get_agent()

    def test_get_function_id(self):
        """Tests get_function_id"""
        if not is_never_authz(self.service_config):
            result = self.object.get_function_id()
            assert isinstance(result, Id)
            assert str(result) == str(LOOKUP_RESOURCE_FUNCTION_ID)

    def test_get_function(self):
        """Tests get_function"""
        if not is_never_authz(self.service_config):
            # not supported
            with pytest.raises(errors.OperationFailed):
                self.object.get_function()

    def test_get_qualifier_id(self):
        """Tests get_qualifier_id"""
        if not is_never_authz(self.service_config):
            result = self.object.get_qualifier_id()
            assert isinstance(result, Id)
            assert str(result) == 'resource.Resource%3Afoo%40ODL.MIT.EDU'

    def test_get_qualifier(self):
        """Tests get_qualifier"""
        if not is_never_authz(self.service_config):
            # not supported
            with pytest.raises(errors.OperationFailed):
                self.object.get_qualifier()

    def test_get_authorization_record(self):
        """Tests get_authorization_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unsupported):
                self.object.get_authorization_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_form_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.form = request.cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': '1', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_form_test_fixture(request):
    pass


@pytest.mark.usefixtures("authorization_form_class_fixture", "authorization_form_test_fixture")
class TestAuthorizationForm(object):
    """Tests for AuthorizationForm"""
    def test_get_authorization_form_record(self):
        """Tests get_authorization_form_record"""
        with pytest.raises(errors.Unsupported):
            self.form.get_authorization_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def authorization_list_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationLookupSession tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.form = request.cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': '1', 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.svc_mgr.get_vaults():
                for authz in catalog.get_authorizations():
                    catalog.delete_authorization(authz.ident)
                request.cls.svc_mgr.delete_vault(catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_list_test_fixture(request):
    from dlkit.json_.authorization.objects import AuthorizationList
    request.cls.authorization_list = list()
    request.cls.authorization_ids = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            form = request.cls.catalog.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_RESOURCE_FUNCTION_ID,
                Id(**{'identifier': str(num), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
                [])
            obj = request.cls.catalog.create_authorization(form)

            request.cls.authorization_list.append(obj)
            request.cls.authorization_ids.append(obj.ident)
        request.cls.authorization_list = AuthorizationList(request.cls.authorization_list)


@pytest.mark.usefixtures("authorization_list_class_fixture", "authorization_list_test_fixture")
class TestAuthorizationList(object):
    """Tests for AuthorizationList"""
    def test_get_next_authorization(self):
        """Tests get_next_authorization"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.authorization.objects import Authorization
        if not is_never_authz(self.service_config):
            assert isinstance(self.authorization_list.get_next_authorization(), Authorization)

    def test_get_next_authorizations(self):
        """Tests get_next_authorizations"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.authorization.objects import AuthorizationList, Authorization
        if not is_never_authz(self.service_config):
            new_list = self.authorization_list.get_next_authorizations(2)
            assert isinstance(new_list, AuthorizationList)
            for item in new_list:
                assert isinstance(item, Authorization)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_class_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_test_fixture(request):
    # From test_templates/resource.py::Bin::init_template
    if not is_never_authz(request.cls.service_config):
        form = request.cls.svc_mgr.get_vault_form_for_create([])
        form.display_name = 'for testing'
        request.cls.object = request.cls.svc_mgr.create_vault(form)

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            request.cls.svc_mgr.delete_vault(request.cls.object.ident)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("vault_class_fixture", "vault_test_fixture")
class TestVault(object):
    """Tests for Vault"""
    def test_get_vault_record(self):
        """Tests get_vault_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_vault_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_form_class_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)

    def class_tear_down():
        pass

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_form_test_fixture(request):
    # From test_templates/resource.py::BinForm::init_template
    if not is_never_authz(request.cls.service_config):
        request.cls.object = request.cls.svc_mgr.get_vault_form_for_create([])

    def test_tear_down():
        pass

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("vault_form_class_fixture", "vault_form_test_fixture")
class TestVaultForm(object):
    """Tests for VaultForm"""
    def test_get_vault_form_record(self):
        """Tests get_vault_form_record"""
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.object.get_vault_form_record(True)


@pytest.fixture(scope="class",
                params=['TEST_SERVICE', 'TEST_SERVICE_ALWAYS_AUTHZ', 'TEST_SERVICE_NEVER_AUTHZ', 'TEST_SERVICE_CATALOGING', 'TEST_SERVICE_FILESYSTEM', 'TEST_SERVICE_MEMCACHE'])
def vault_list_class_fixture(request):
    # Implemented from init template for BinList
    request.cls.service_config = request.param
    request.cls.svc_mgr = Runtime().get_service_manager(
        'AUTHORIZATION',
        proxy=PROXY,
        implementation=request.cls.service_config)
    if not is_never_authz(request.cls.service_config):
        create_form = request.cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for VaultList tests'
        request.cls.catalog = request.cls.svc_mgr.create_vault(create_form)
        request.cls.vault_ids = list()

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for obj in request.cls.vault_ids:
                request.cls.svc_mgr.delete_vault(obj)
            request.cls.svc_mgr.delete_vault(request.cls.catalog.ident)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def vault_list_test_fixture(request):
    # Implemented from init template for BinList
    from dlkit.json_.authorization.objects import VaultList
    request.cls.vault_list = list()
    if not is_never_authz(request.cls.service_config):
        for num in [0, 1]:
            create_form = request.cls.svc_mgr.get_vault_form_for_create([])
            create_form.display_name = 'Test Vault ' + str(num)
            create_form.description = 'Test Vault for VaultList tests'
            obj = request.cls.svc_mgr.create_vault(create_form)
            request.cls.vault_list.append(obj)
            request.cls.vault_ids.append(obj.ident)
    request.cls.vault_list = VaultList(request.cls.vault_list)


@pytest.mark.usefixtures("vault_list_class_fixture", "vault_list_test_fixture")
class TestVaultList(object):
    """Tests for VaultList"""
    def test_get_next_vault(self):
        """Tests get_next_vault"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.authorization.objects import Vault
        if not is_never_authz(self.service_config):
            assert isinstance(self.vault_list.get_next_vault(), Vault)

    def test_get_next_vaults(self):
        """Tests get_next_vaults"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.authorization.objects import VaultList, Vault
        if not is_never_authz(self.service_config):
            new_list = self.vault_list.get_next_vaults(2)
            assert isinstance(new_list, VaultList)
            for item in new_list:
                assert isinstance(item, Vault)


@pytest.mark.usefixtures("vault_node_class_fixture", "vault_node_test_fixture")
class TestVaultNode(object):
    """Tests for VaultNode"""
    @pytest.mark.skip('unimplemented test')
    def test_get_vault(self):
        """Tests get_vault"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_parent_vault_nodes(self):
        """Tests get_parent_vault_nodes"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_child_vault_nodes(self):
        """Tests get_child_vault_nodes"""
        pass


@pytest.mark.usefixtures("vault_node_list_class_fixture", "vault_node_list_test_fixture")
class TestVaultNodeList(object):
    """Tests for VaultNodeList"""
    @pytest.mark.skip('unimplemented test')
    def test_get_next_vault_node(self):
        """Tests get_next_vault_node"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_next_vault_nodes(self):
        """Tests get_next_vault_nodes"""
        pass
