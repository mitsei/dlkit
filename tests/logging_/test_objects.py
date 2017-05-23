"""Unit tests of logging objects."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
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

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_log(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_log_entry_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_priority_metadata(self):
        """Tests get_priority_metadata"""
        # From test_templates/logging.py::LogEntryForm::get_priority_metadata_template
        self.assertTrue(isinstance(self.form.get_priority_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_priority(self):
        """Tests set_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_priority(self):
        """Tests clear_priority"""
        pass

    def test_get_timestamp_metadata(self):
        """Tests get_timestamp_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_timestamp_metadata(), Metadata))

    def test_set_timestamp(self):
        """Tests set_timestamp"""
        test_time = DateTime.utcnow()
        # By default log entries have this set, so can't use the templated test
        self.assertIsNotNone(self.form._my_map['timestamp'])
        self.form.set_timestamp(test_time)
        self.assertEqual(self.form._my_map['timestamp'],
                         test_time)

    def test_get_agent_metadata(self):
        """Tests get_agent_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_agent_metadata(), Metadata))

    def test_set_agent(self):
        """Tests set_agent"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['agentId'], '')
        self.form.set_agent(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['agentId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_get_log_entry_form_record(self):
        """Tests get_log_entry_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_log_entry_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestLogEntryList(unittest.TestCase):
    """Tests for LogEntryList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryList tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.logging_.objects import LogEntryList
        self.log_entry_list = list()
        self.log_entry_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + str(num)
            create_form.description = 'Test LogEntry for LogEntryList tests'
            obj = self.catalog.create_log_entry(create_form)
            self.log_entry_list.append(obj)
            self.log_entry_ids.append(obj.ident)
        self.log_entry_list = LogEntryList(self.log_entry_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_next_log_entry(self):
        """Tests get_next_log_entry"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.logging_.objects import LogEntry
        self.assertTrue(isinstance(self.log_entry_list.get_next_log_entry(), LogEntry))

    def test_get_next_log_entries(self):
        """Tests get_next_log_entries"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList, LogEntry
        new_list = self.log_entry_list.get_next_log_entries(2)
        self.assertTrue(isinstance(new_list, LogEntryList))
        for item in new_list:
            self.assertTrue(isinstance(item, LogEntry))


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

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogList tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)
        cls.log_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.logging_.objects import LogList
        self.log_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'Test Log ' + str(num)
            create_form.description = 'Test Log for LogList tests'
            obj = self.svc_mgr.create_log(create_form)
            self.log_list.append(obj)
            self.log_ids.append(obj.ident)
        self.log_list = LogList(self.log_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.log_ids:
            cls.svc_mgr.delete_log(obj)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_next_log(self):
        """Tests get_next_log"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.logging_.objects import Log
        self.assertTrue(isinstance(self.log_list.get_next_log(), Log))

    def test_get_next_logs(self):
        """Tests get_next_logs"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.logging_.objects import LogList, Log
        new_list = self.log_list.get_next_logs(2)
        self.assertTrue(isinstance(new_list, LogList))
        for item in new_list:
            self.assertTrue(isinstance(item, Log))


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
