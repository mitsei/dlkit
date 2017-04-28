"""Unit tests of logging objects."""


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


class TestLogEntry(unittest.TestCase):
    """Tests for LogEntry"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_log(create_form)

        form = cls.catalog.get_log_entry_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_log_entry(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_priority(self):
        """Tests get_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_timestamp(self):
        """Tests get_timestamp"""
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
    def test_get_agent_id(self):
        """Tests get_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_agent(self):
        """Tests get_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entry_record(self):
        """Tests get_log_entry_record"""
        pass


class TestLogEntryForm(unittest.TestCase):
    """Tests for LogEntryForm"""

    @unittest.skip('unimplemented test')
    def test_get_priority_metadata(self):
        """Tests get_priority_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_priority(self):
        """Tests set_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_priority(self):
        """Tests clear_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_timestamp_metadata(self):
        """Tests get_timestamp_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_timestamp(self):
        """Tests set_timestamp"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_agent_metadata(self):
        """Tests get_agent_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_agent(self):
        """Tests set_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entry_form_record(self):
        """Tests get_log_entry_form_record"""
        pass


class TestLogEntryList(unittest.TestCase):
    """Tests for LogEntryList"""

    @unittest.skip('unimplemented test')
    def test_get_next_log_entry(self):
        """Tests get_next_log_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_log_entries(self):
        """Tests get_next_log_entries"""
        pass


class TestLog(unittest.TestCase):
    """Tests for Log"""

    @unittest.skip('unimplemented test')
    def test_get_log_record(self):
        """Tests get_log_record"""
        pass


class TestLogForm(unittest.TestCase):
    """Tests for LogForm"""

    @unittest.skip('unimplemented test')
    def test_get_log_form_record(self):
        """Tests get_log_form_record"""
        pass


class TestLogList(unittest.TestCase):
    """Tests for LogList"""

    @unittest.skip('unimplemented test')
    def test_get_next_log(self):
        """Tests get_next_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_logs(self):
        """Tests get_next_logs"""
        pass


class TestLogNode(unittest.TestCase):
    """Tests for LogNode"""

    @unittest.skip('unimplemented test')
    def test_get_log(self):
        """Tests get_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_log_nodes(self):
        """Tests get_parent_log_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_log_nodes(self):
        """Tests get_child_log_nodes"""
        pass


class TestLogNodeList(unittest.TestCase):
    """Tests for LogNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_log_node(self):
        """Tests get_next_log_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_log_nodes(self):
        """Tests get_next_log_nodes"""
        pass
