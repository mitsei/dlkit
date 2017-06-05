"""Unit tests of authorization queries."""


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

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAuthorizationQuery(unittest.TestCase):
    """Tests for AuthorizationQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('AUTHORIZATION', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_vault_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_vault(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_authorization_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_vault(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_explicit_authorizations(self):
        """Tests match_explicit_authorizations"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_explicit_authorizations_terms(self):
        """Tests clear_explicit_authorizations_terms"""
        pass

    def test_match_related_authorization_id(self):
        """Tests match_related_authorization_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_related_authorization_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['relatedAuthorizationId'], {
            '$in': [str(test_id)]
        })

    def test_clear_related_authorization_id_terms(self):
        """Tests clear_related_authorization_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_related_authorization_id(test_id, match=True)
        self.assertIn('relatedAuthorizationId',
                      self.query._query_terms)
        self.query.clear_related_authorization_id_terms()
        self.assertNotIn('relatedAuthorizationId',
                         self.query._query_terms)

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

    def test_match_resource_id(self):
        """Tests match_resource_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_resource_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['resourceId'], {
            '$in': [str(test_id)]
        })

    def test_clear_resource_id_terms(self):
        """Tests clear_resource_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_resource_id(test_id, match=True)
        self.assertIn('resourceId',
                      self.query._query_terms)
        self.query.clear_resource_id_terms()
        self.assertNotIn('resourceId',
                         self.query._query_terms)

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

    def test_match_trust_id(self):
        """Tests match_trust_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_trust_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['trustId'], {
            '$in': [str(test_id)]
        })

    @unittest.skip('unimplemented test')
    def test_match_any_trust_id(self):
        """Tests match_any_trust_id"""
        pass

    def test_clear_trust_id_terms(self):
        """Tests clear_trust_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_trust_id(test_id, match=True)
        self.assertIn('trustId',
                      self.query._query_terms)
        self.query.clear_trust_id_terms()
        self.assertNotIn('trustId',
                         self.query._query_terms)

    def test_match_agent_id(self):
        """Tests match_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_agent_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['agentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_agent_id_terms(self):
        """Tests clear_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_agent_id(test_id, match=True)
        self.assertIn('agentId',
                      self.query._query_terms)
        self.query.clear_agent_id_terms()
        self.assertNotIn('agentId',
                         self.query._query_terms)

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

    def test_match_function_id(self):
        """Tests match_function_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_function_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['functionId'], {
            '$in': [str(test_id)]
        })

    def test_clear_function_id_terms(self):
        """Tests clear_function_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_function_id(test_id, match=True)
        self.assertIn('functionId',
                      self.query._query_terms)
        self.query.clear_function_id_terms()
        self.assertNotIn('functionId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_function_query(self):
        """Tests supports_function_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_function_query(self):
        """Tests get_function_query"""
        pass

    def test_clear_function_terms(self):
        """Tests clear_function_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['function'] = 'foo'
        self.query.clear_function_terms()
        self.assertNotIn('function',
                         self.query._query_terms)

    def test_match_qualifier_id(self):
        """Tests match_qualifier_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_qualifier_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['qualifierId'], {
            '$in': [str(test_id)]
        })

    def test_clear_qualifier_id_terms(self):
        """Tests clear_qualifier_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_qualifier_id(test_id, match=True)
        self.assertIn('qualifierId',
                      self.query._query_terms)
        self.query.clear_qualifier_id_terms()
        self.assertNotIn('qualifierId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_qualifier_query(self):
        """Tests supports_qualifier_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_qualifier_query(self):
        """Tests get_qualifier_query"""
        pass

    def test_clear_qualifier_terms(self):
        """Tests clear_qualifier_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['qualifier'] = 'foo'
        self.query.clear_qualifier_terms()
        self.assertNotIn('qualifier',
                         self.query._query_terms)

    def test_match_vault_id(self):
        """Tests match_vault_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_vault_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedVaultIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_vault_id_terms(self):
        """Tests clear_vault_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_vault_id(test_id, match=True)
        self.assertIn('assignedVaultIds',
                      self.query._query_terms)
        self.query.clear_vault_id_terms()
        self.assertNotIn('assignedVaultIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_vault_query(self):
        """Tests supports_vault_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_vault_query(self):
        """Tests get_vault_query"""
        pass

    def test_clear_vault_terms(self):
        """Tests clear_vault_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['vault'] = 'foo'
        self.query.clear_vault_terms()
        self.assertNotIn('vault',
                         self.query._query_terms)

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
