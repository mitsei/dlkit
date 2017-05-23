"""Unit tests of resource queries."""


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


class TestResourceQuery(unittest.TestCase):
    """Tests for ResourceQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bin(create_form)

        cls.query = cls.catalog.get_resource_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_group(self):
        """Tests match_group"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_group_terms(self):
        """Tests clear_group_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_demographic(self):
        """Tests match_demographic"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_demographic_terms(self):
        """Tests clear_demographic_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_containing_group_id(self):
        """Tests match_containing_group_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_containing_group_id_terms(self):
        """Tests clear_containing_group_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_containing_group_query(self):
        """Tests supports_containing_group_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_containing_group_query(self):
        """Tests get_containing_group_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_containing_group(self):
        """Tests match_any_containing_group"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_containing_group_terms(self):
        """Tests clear_containing_group_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_avatar_id(self):
        """Tests match_avatar_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_avatar_id_terms(self):
        """Tests clear_avatar_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_avatar_query(self):
        """Tests supports_avatar_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_avatar_query(self):
        """Tests get_avatar_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_avatar(self):
        """Tests match_any_avatar"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_avatar_terms(self):
        """Tests clear_avatar_terms"""
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
    def test_match_resource_relationship_id(self):
        """Tests match_resource_relationship_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_resource_relationship_id_terms(self):
        """Tests clear_resource_relationship_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_resource_relationship_query(self):
        """Tests supports_resource_relationship_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource_relationship_query(self):
        """Tests get_resource_relationship_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_resource_relationship(self):
        """Tests match_any_resource_relationship"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_resource_relationship_terms(self):
        """Tests clear_resource_relationship_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_bin_id(self):
        """Tests match_bin_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bin_id_terms(self):
        """Tests clear_bin_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_bin_query(self):
        """Tests supports_bin_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bin_query(self):
        """Tests get_bin_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bin_terms(self):
        """Tests clear_bin_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource_query_record(self):
        """Tests get_resource_query_record"""
        pass


class TestBinQuery(unittest.TestCase):
    """Tests for BinQuery"""

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
    def test_match_ancestor_bin_id(self):
        """Tests match_ancestor_bin_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_bin_id_terms(self):
        """Tests clear_ancestor_bin_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_bin_query(self):
        """Tests supports_ancestor_bin_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_bin_query(self):
        """Tests get_ancestor_bin_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_bin(self):
        """Tests match_any_ancestor_bin"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_bin_terms(self):
        """Tests clear_ancestor_bin_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_bin_id(self):
        """Tests match_descendant_bin_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_bin_id_terms(self):
        """Tests clear_descendant_bin_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_bin_query(self):
        """Tests supports_descendant_bin_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_bin_query(self):
        """Tests get_descendant_bin_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_bin(self):
        """Tests match_any_descendant_bin"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_bin_terms(self):
        """Tests clear_descendant_bin_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bin_query_record(self):
        """Tests get_bin_query_record"""
        pass
