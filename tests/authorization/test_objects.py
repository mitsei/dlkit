"""Unit tests of authorization objects."""


import unittest


from dlkit.abstract_osid.osid import errors
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


class TestAuthorization(unittest.TestCase):
    """Tests for Authorization"""

    @classmethod
    def setUpClass(cls):
        cls.authorization_list = list()
        cls.authorization_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationQuerySession tests'
        cls.catalog = cls.svc_mgr.create_vault(create_form)
        create_form = cls.catalog.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_RESOURCE_FUNCTION_ID,
            Id(**{'identifier': str('foo'), 'namespace': 'resource.Resource', 'authority': 'ODL.MIT.EDU'}),
            [])
        create_form.display_name = 'Test Authorization'
        create_form.description = (
            'Test Authorization for Authorization tests')
        obj = cls.catalog.create_authorization(create_form)
        cls.object = obj

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_vaults():
            for obj in catalog.get_authorizations():
                catalog.delete_authorization(obj.ident)
            cls.svc_mgr.delete_vault(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_is_implicit(self):
        """Tests is_implicit"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_resource(self):
        """Tests has_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource_id(self):
        """Tests get_resource_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource(self):
        """Tests get_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_trust(self):
        """Tests has_trust"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_trust_id(self):
        """Tests get_trust_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_trust(self):
        """Tests get_trust"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_agent(self):
        """Tests has_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_agent_id(self):
        """Tests get_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_agent(self):
        """Tests get_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_function_id(self):
        """Tests get_function_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_function(self):
        """Tests get_function"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_qualifier_id(self):
        """Tests get_qualifier_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_qualifier(self):
        """Tests get_qualifier"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorization_record(self):
        """Tests get_authorization_record"""
        pass


class TestAuthorizationForm(unittest.TestCase):
    """Tests for AuthorizationForm"""

    @unittest.skip('unimplemented test')
    def test_get_authorization_form_record(self):
        """Tests get_authorization_form_record"""
        pass


class TestAuthorizationList(unittest.TestCase):
    """Tests for AuthorizationList"""

    @unittest.skip('unimplemented test')
    def test_get_next_authorization(self):
        """Tests get_next_authorization"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_authorizations(self):
        """Tests get_next_authorizations"""
        pass


class TestVault(unittest.TestCase):
    """Tests for Vault"""

    @unittest.skip('unimplemented test')
    def test_get_vault_record(self):
        """Tests get_vault_record"""
        pass


class TestVaultForm(unittest.TestCase):
    """Tests for VaultForm"""

    @unittest.skip('unimplemented test')
    def test_get_vault_form_record(self):
        """Tests get_vault_form_record"""
        pass


class TestVaultList(unittest.TestCase):
    """Tests for VaultList"""

    @unittest.skip('unimplemented test')
    def test_get_next_vault(self):
        """Tests get_next_vault"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_vaults(self):
        """Tests get_next_vaults"""
        pass


class TestVaultNode(unittest.TestCase):
    """Tests for VaultNode"""

    @unittest.skip('unimplemented test')
    def test_get_vault(self):
        """Tests get_vault"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_vault_nodes(self):
        """Tests get_parent_vault_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_vault_nodes(self):
        """Tests get_child_vault_nodes"""
        pass


class TestVaultNodeList(unittest.TestCase):
    """Tests for VaultNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_vault_node(self):
        """Tests get_next_vault_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_vault_nodes(self):
        """Tests get_next_vault_nodes"""
        pass
