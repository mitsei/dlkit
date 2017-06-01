"""Unit tests of logging queries."""


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


class TestLogEntryQuery(unittest.TestCase):
    """Tests for LogEntryQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_log(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_log_entry_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_log(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_priority(self):
        """Tests match_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_priority(self):
        """Tests match_any_priority"""
        pass

    def test_clear_priority_terms(self):
        """Tests clear_priority_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['priority'] = 'foo'
        self.query.clear_priority_terms()
        self.assertNotIn('priority',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_minimum_priority(self):
        """Tests match_minimum_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_priority_terms(self):
        """Tests clear_minimum_priority_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_timestamp(self):
        """Tests match_timestamp"""
        pass

    def test_clear_timestamp_terms(self):
        """Tests clear_timestamp_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['timestamp'] = 'foo'
        self.query.clear_timestamp_terms()
        self.assertNotIn('timestamp',
                         self.query._query_terms)

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
    def test_clear_resource_terms(self):
        """Tests clear_resource_terms"""
        pass

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

    def test_clear_agent_terms(self):
        """Tests clear_agent_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['agent'] = 'foo'
        self.query.clear_agent_terms()
        self.assertNotIn('agent',
                         self.query._query_terms)

    def test_match_log_id(self):
        """Tests match_log_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_log_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedLogIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_log_id_terms(self):
        """Tests clear_log_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_log_id(test_id, match=True)
        self.assertIn('assignedLogIds',
                      self.query._query_terms)
        self.query.clear_log_id_terms()
        self.assertNotIn('assignedLogIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_log_query(self):
        """Tests supports_log_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_query(self):
        """Tests get_log_query"""
        pass

    def test_clear_log_terms(self):
        """Tests clear_log_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['log'] = 'foo'
        self.query.clear_log_terms()
        self.assertNotIn('log',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_log_entry_query_record(self):
        """Tests get_log_entry_query_record"""
        pass


class TestLogQuery(unittest.TestCase):
    """Tests for LogQuery"""

    @unittest.skip('unimplemented test')
    def test_match_log_entry_id(self):
        """Tests match_log_entry_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_log_entry_id_terms(self):
        """Tests clear_log_entry_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_log_entry_query(self):
        """Tests supports_log_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entry_query(self):
        """Tests get_log_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_log_entry(self):
        """Tests match_any_log_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_log_entry_terms(self):
        """Tests clear_log_entry_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_log_id(self):
        """Tests match_ancestor_log_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_log_id_terms(self):
        """Tests clear_ancestor_log_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_log_query(self):
        """Tests supports_ancestor_log_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_log_query(self):
        """Tests get_ancestor_log_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_log(self):
        """Tests match_any_ancestor_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_log_terms(self):
        """Tests clear_ancestor_log_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_log_id(self):
        """Tests match_descendant_log_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_log_id_terms(self):
        """Tests clear_descendant_log_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_log_query(self):
        """Tests supports_descendant_log_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_log_query(self):
        """Tests get_descendant_log_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_log(self):
        """Tests match_any_descendant_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_log_terms(self):
        """Tests clear_descendant_log_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_query_record(self):
        """Tests get_log_query_record"""
        pass
