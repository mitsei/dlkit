"""Unit tests of logging objects."""


import unittest


from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
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
        # From test_templates/resource.py::Resource::init_template
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
        # From test_templates/resource.py::Resource::init_template
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_priority(self):
        """Tests get_priority"""
        pass

    def test_get_timestamp(self):
        """Tests get_timestamp"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_timestamp()

    def test_get_resource_id(self):
        """Tests get_resource_id"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_resource_id()

    def test_get_resource(self):
        """Tests get_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_resource()

    def test_get_agent_id(self):
        """Tests get_agent_id"""
        result = self.object.get_agent_id()
        self.assertTrue(isinstance(result, Id))
        self.assertEqual(str(result),
                         str(self.catalog._proxy.get_effective_agent_id()))

    def test_get_agent(self):
        """Tests get_agent"""
        # because we don't have Agency implemented in authentication
        with self.assertRaises(AttributeError):
            self.object.get_agent()

    def test_get_log_entry_record(self):
        """Tests get_log_entry_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_log_entry_record(True)


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
        mdata = self.form.get_priority_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'TYPE')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_priority(self):
        """Tests set_priority"""
        # From test_templates/logging.py::LogEntryForm::set_priority_template
        self.form.set_priority(Type('type.Type%3Afake-type-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['priority'],
                         'type.Type%3Afake-type-id%40ODL.MIT.EDU')
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_priority(True)

    def test_clear_priority(self):
        """Tests clear_priority"""
        # From test_templates/logging.py::LogEntryForm::clear_priority_template
        self.form.set_priority(Type('type.Type%3Afake-type-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['priority'],
                         'type.Type%3Afake-type-id%40ODL.MIT.EDU')
        self.form.clear_priority()
        self.assertEqual(self.form._my_map['priorityId'], self.form.get_priority_metadata().get_default_type_values()[0])

    def test_get_timestamp_metadata(self):
        """Tests get_timestamp_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_timestamp_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DATETIME')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_timestamp(self):
        """Tests set_timestamp"""
        test_time = DateTime.utcnow()
        # By default log entries have this set, so can't use the templated test
        self.assertIsNotNone(self.form._my_map['timestamp'])
        self.form.set_timestamp(test_time)
        self.assertEqual(self.form._my_map['timestamp'],
                         test_time)
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_timestamp(True)

    def test_get_agent_metadata(self):
        """Tests get_agent_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_agent_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'ID')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_agent(self):
        """Tests set_agent"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['agentId'], '')
        self.form.set_agent(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['agentId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_agent(True)

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
        self.object = self.log_entry_list

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

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::Bin::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')

    def setUp(self):
        # From test_templates/resource.py::Bin::init_template
        form = self.svc_mgr.get_log_form_for_create([])
        form.display_name = 'for testing'
        self.object = self.svc_mgr.create_log(form)

    def tearDown(self):
        # From test_templates/resource.py::Bin::init_template
        self.svc_mgr.delete_log(self.object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::Bin::init_template
        pass

    def test_get_log_record(self):
        """Tests get_log_record"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_log_record(True)


class TestLogForm(unittest.TestCase):
    """Tests for LogForm"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')

    def setUp(self):
        # From test_templates/resource.py::BinForm::init_template
        self.object = self.svc_mgr.get_log_form_for_create([])

    def tearDown(self):
        # From test_templates/resource.py::BinForm::init_template
        pass

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinForm::init_template
        pass

    def test_get_log_form_record(self):
        """Tests get_log_form_record"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_log_form_record(True)


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
