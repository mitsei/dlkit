"""Unit tests of authorization queries."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAuthorizationQuery(unittest.TestCase):
    """Tests for AuthorizationQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_vault(create_form)

        cls.query = cls.catalog.get_authorization_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_vault(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_explicit_authorizations(self):
        """Tests match_explicit_authorizations"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_explicit_authorizations_terms(self):
        """Tests clear_explicit_authorizations_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_related_authorization_id(self):
        """Tests match_related_authorization_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_related_authorization_id_terms(self):
        """Tests clear_related_authorization_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_related_authorization_query(self):
        """Tests supports_related_authorization_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_related_authorization_query(self):
        """Tests get_related_authorization_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_related_authorization_terms(self):
        """Tests clear_related_authorization_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_resource_id(self):
        """Tests match_resource_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_resource_id_terms(self):
        """Tests clear_resource_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_resource_query(self):
        """Tests supports_resource_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource_query(self):
        """Tests get_resource_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_resource(self):
        """Tests match_any_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_resource_terms(self):
        """Tests clear_resource_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_trust_id(self):
        """Tests match_trust_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_trust_id(self):
        """Tests match_any_trust_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_trust_id_terms(self):
        """Tests clear_trust_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_agent_id(self):
        """Tests match_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_agent_id_terms(self):
        """Tests clear_agent_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_agent_query(self):
        """Tests supports_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_agent_query(self):
        """Tests get_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_agent(self):
        """Tests match_any_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_agent_terms(self):
        """Tests clear_agent_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_function_id(self):
        """Tests match_function_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_function_id_terms(self):
        """Tests clear_function_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_function_query(self):
        """Tests supports_function_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_function_query(self):
        """Tests get_function_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_function_terms(self):
        """Tests clear_function_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_qualifier_id(self):
        """Tests match_qualifier_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_qualifier_id_terms(self):
        """Tests clear_qualifier_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_qualifier_query(self):
        """Tests supports_qualifier_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_qualifier_query(self):
        """Tests get_qualifier_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_qualifier_terms(self):
        """Tests clear_qualifier_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_vault_id(self):
        """Tests match_vault_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_vault_id_terms(self):
        """Tests clear_vault_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_vault_query(self):
        """Tests supports_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vault_query(self):
        """Tests get_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_vault_terms(self):
        """Tests clear_vault_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorization_query_record(self):
        """Tests get_authorization_query_record"""
        pass


class TestVaultQuery(unittest.TestCase):
    """Tests for VaultQuery"""

    @unittest.skip('unimplemented test')
    def test_match_function_id(self):
        """Tests match_function_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_function_id_terms(self):
        """Tests clear_function_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_function_query(self):
        """Tests supports_function_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_function_query(self):
        """Tests get_function_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_function(self):
        """Tests match_any_function"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_function_terms(self):
        """Tests clear_function_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_qualifier_id(self):
        """Tests match_qualifier_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_qualifier_id_terms(self):
        """Tests clear_qualifier_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_qualifier_query(self):
        """Tests supports_qualifier_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_qualifier_query(self):
        """Tests get_qualifier_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_qualifier(self):
        """Tests match_any_qualifier"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_qualifier_terms(self):
        """Tests clear_qualifier_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_authorization_id(self):
        """Tests match_authorization_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_authorization_id_terms(self):
        """Tests clear_authorization_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_authorization_query(self):
        """Tests supports_authorization_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_authorization_query(self):
        """Tests get_authorization_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_authorization(self):
        """Tests match_any_authorization"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_authorization_terms(self):
        """Tests clear_authorization_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_vault_id(self):
        """Tests match_ancestor_vault_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_vault_id_terms(self):
        """Tests clear_ancestor_vault_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_vault_query(self):
        """Tests supports_ancestor_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_vault_query(self):
        """Tests get_ancestor_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_vault(self):
        """Tests match_any_ancestor_vault"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_vault_terms(self):
        """Tests clear_ancestor_vault_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_vault_id(self):
        """Tests match_descendant_vault_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_vault_id_terms(self):
        """Tests clear_descendant_vault_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_vault_query(self):
        """Tests supports_descendant_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_vault_query(self):
        """Tests get_descendant_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_vault(self):
        """Tests match_any_descendant_vault"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_vault_terms(self):
        """Tests clear_descendant_vault_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vault_query_record(self):
        """Tests get_vault_query_record"""
        pass
