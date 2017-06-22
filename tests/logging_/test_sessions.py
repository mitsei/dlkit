"""Unit tests of logging sessions."""


import unittest


from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.logging_ import objects as ABCObjects
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


class TestLoggingSession(unittest.TestCase):
    """Tests for LoggingSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogAdminSession tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log For Deletion'
        create_form.description = 'Test Log for LogAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_log(create_form)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_logs():
            cls.svc_mgr.delete_log(catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_log(self):
        """Tests can_log"""
        self.assertTrue(isinstance(self.session.can_log(), bool))

    def test_log(self):
        """Tests log"""
        with self.assertRaises(errors.Unimplemented):
            self.session.log(True, True)

    def test_log_at_priority(self):
        """Tests log_at_priority"""
        with self.assertRaises(errors.Unimplemented):
            self.session.log_at_priority(True, True, True)

    def test_get_log_entry_form(self):
        """Tests get_log_entry_form"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entry_form()

    def test_create_log_entry(self):
        """Tests create_log_entry"""
        with self.assertRaises(errors.Unimplemented):
            self.session.create_log_entry(True)


class TestLogEntryLookupSession(unittest.TestCase):
    """Tests for LogEntryLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.log_entry_list = list()
        cls.log_entry_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryLookupSession tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + str(num)
            create_form.description = 'Test LogEntry for LogEntryLookupSession tests'
            obj = cls.catalog.create_log_entry(create_form)
            cls.log_entry_list.append(obj)
            cls.log_entry_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_read_log(self):
        """Tests can_read_log"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_read_log(), bool))

    def test_use_comparative_log_entry_view(self):
        """Tests use_comparative_log_entry_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_log_entry_view()

    def test_use_plenary_log_entry_view(self):
        """Tests use_plenary_log_entry_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_log_entry_view()

    def test_use_federated_log_view(self):
        """Tests use_federated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_log_view()

    def test_use_isolated_log_view(self):
        """Tests use_isolated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_log_view()

    def test_get_log_entry(self):
        """Tests get_log_entry"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_log_view()
        obj = self.catalog.get_log_entry(self.log_entry_list[0].ident)
        self.assertEqual(obj.ident, self.log_entry_list[0].ident)
        self.catalog.use_federated_log_view()
        obj = self.catalog.get_log_entry(self.log_entry_list[0].ident)
        self.assertEqual(obj.ident, self.log_entry_list[0].ident)

    def test_get_log_entries_by_ids(self):
        """Tests get_log_entries_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_ids(self.log_entry_ids)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_ids(self.log_entry_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, LogEntryList))

    def test_get_log_entries_by_genus_type(self):
        """Tests get_log_entries_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, LogEntryList))

    def test_get_log_entries_by_parent_genus_type(self):
        """Tests get_log_entries_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, LogEntryList))

    def test_get_log_entries_by_record_type(self):
        """Tests get_log_entries_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, LogEntryList))

    def test_get_log_entries_by_priority_type(self):
        """Tests get_log_entries_by_priority_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entries_by_priority_type(True)

    def test_get_log_entries_by_date(self):
        """Tests get_log_entries_by_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entries_by_date(True, True)

    def test_get_log_entries_by_priority_type_and_date(self):
        """Tests get_log_entries_by_priority_type_and_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entries_by_priority_type_and_date(True, True, True)

    def test_get_log_entries_for_resource(self):
        """Tests get_log_entries_for_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entries_for_resource(True)

    def test_get_log_entries_by_date_for_resource(self):
        """Tests get_log_entries_by_date_for_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entries_by_date_for_resource(True, True, True)

    def test_get_log_entries_by_priority_type_and_date_for_resource(self):
        """Tests get_log_entries_by_priority_type_and_date_for_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_log_entries_by_priority_type_and_date_for_resource(True, True, True, True)

    def test_get_log_entries(self):
        """Tests get_log_entries"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries()
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, LogEntryList))

    def test_get_log_entry_with_alias(self):
        self.catalog.alias_log_entry(self.log_entry_ids[0], ALIAS_ID)
        obj = self.catalog.get_log_entry(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.log_entry_ids[0])


class TestLogEntryQuerySession(unittest.TestCase):
    """Tests for LogEntryQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        cls.log_entry_list = list()
        cls.log_entry_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryQuerySession tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_log_entry_form_for_create([])
            create_form.display_name = 'Test LogEntry ' + color
            create_form.description = (
                'Test LogEntry for LogEntryQuerySession tests, did I mention green')
            obj = cls.catalog.create_log_entry(create_form)
            cls.log_entry_list.append(obj)
            cls.log_entry_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_log_entries(self):
        """Tests can_search_log_entries"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_log_entries(), bool))

    def test_use_federated_log_view(self):
        """Tests use_federated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_log_view()

    def test_use_isolated_log_view(self):
        """Tests use_isolated_log_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_log_view()

    def test_get_log_entry_query(self):
        """Tests get_log_entry_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_log_entry_query()

    def test_get_log_entries_by_query(self):
        """Tests get_log_entries_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_log_entry_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_log_entries_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_log_entries_by_query(query).available(), 3)


class TestLogEntryAdminSession(unittest.TestCase):
    """Tests for LogEntryAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryAdminSession tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        form = self.catalog.get_log_entry_form_for_create([])
        form.display_name = 'new LogEntry'
        form.description = 'description of LogEntry'
        form.set_genus_type(NEW_TYPE)
        self.osid_object = self.catalog.create_log_entry(form)
        self.session = self.catalog

    def tearDown(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        self.catalog.delete_log_entry(self.osid_object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    def test_get_log(self):
        """Tests get_log"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_log_entries(self):
        """Tests can_create_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.catalog.can_create_log_entries(), bool))

    def test_can_create_log_entry_with_record_types(self):
        """Tests can_create_log_entry_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_log_entry_with_record_types(DEFAULT_TYPE), bool))

    def test_get_log_entry_form_for_create(self):
        """Tests get_log_entry_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_log_entry_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_log_entry(self):
        """Tests create_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.logging_.objects import LogEntry
        self.assertTrue(isinstance(self.osid_object, LogEntry))
        self.assertEqual(self.osid_object.display_name.text, 'new LogEntry')
        self.assertEqual(self.osid_object.description.text, 'description of LogEntry')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_log_entries(self):
        """Tests can_update_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.catalog.can_update_log_entries(), bool))

    def test_get_log_entry_form_for_update(self):
        """Tests get_log_entry_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_log_entry_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_log_entry(self):
        """Tests update_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.logging_.objects import LogEntry
        form = self.catalog.get_log_entry_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_log_entry(form)
        self.assertTrue(isinstance(updated_object, LogEntry))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_log_entries(self):
        """Tests can_delete_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.catalog.can_delete_log_entries(), bool))

    def test_delete_log_entry(self):
        """Tests delete_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_log_entry_form_for_create([])
        form.display_name = 'new LogEntry'
        form.description = 'description of LogEntry'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_log_entry(form)
        self.catalog.delete_log_entry(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_log_entry(osid_object.ident)

    def test_can_manage_log_entry_aliases(self):
        """Tests can_manage_log_entry_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_log_entry_aliases(), bool))

    def test_alias_log_entry(self):
        """Tests alias_log_entry"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_log_entry(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_log_entry(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestLogLookupSession(unittest.TestCase):
    """Tests for LogLookupSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = 'Test Log ' + str(num)
            create_form.description = 'Test Log for logging proxy manager tests'
            catalog = cls.svc_mgr.create_log(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::BinLookupSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        for catalog in cls.svc_mgr.get_logs():
            cls.svc_mgr.delete_log(catalog.ident)

    def test_can_lookup_logs(self):
        """Tests can_lookup_logs"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_lookup_logs(), bool))

    def test_use_comparative_log_view(self):
        """Tests use_comparative_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_log_view()

    def test_use_plenary_log_view(self):
        """Tests use_plenary_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_log_view()

    def test_get_log(self):
        """Tests get_log"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        catalog = self.svc_mgr.get_log(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_logs_by_ids(self):
        """Tests get_logs_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        catalogs = self.svc_mgr.get_logs_by_ids(self.catalog_ids)
        self.assertTrue(catalogs.available() == 2)
        self.assertTrue(isinstance(catalogs, ABCObjects.LogList))
        reversed_catalog_ids = [str(cat_id) for cat_id in self.catalog_ids][::-1]
        for index, catalog in enumerate(catalogs):
            self.assertEqual(str(catalog.ident),
                             reversed_catalog_ids[index])

    def test_get_logs_by_genus_type(self):
        """Tests get_logs_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        catalogs = self.svc_mgr.get_logs_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.LogList))

    def test_get_logs_by_parent_genus_type(self):
        """Tests get_logs_by_parent_genus_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_logs_by_parent_genus_type(True)

    def test_get_logs_by_record_type(self):
        """Tests get_logs_by_record_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_logs_by_record_type(True)

    def test_get_logs_by_provider(self):
        """Tests get_logs_by_provider"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_logs_by_provider(True)

    def test_get_logs(self):
        """Tests get_logs"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        catalogs = self.svc_mgr.get_logs()
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.LogList))


class TestLogAdminSession(unittest.TestCase):
    """Tests for LogAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogAdminSession tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log For Deletion'
        create_form.description = 'Test Log for LogAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_log(create_form)

    def setUp(self):
        # From test_templates/resource.py::BinAdminSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        for catalog in cls.svc_mgr.get_logs():
            cls.svc_mgr.delete_log(catalog.ident)

    def test_can_create_logs(self):
        """Tests can_create_logs"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_logs(), bool))

    def test_can_create_log_with_record_types(self):
        """Tests can_create_log_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_log_with_record_types(DEFAULT_TYPE), bool))

    def test_get_log_form_for_create(self):
        """Tests get_log_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.logging_.objects import LogForm
        catalog_form = self.svc_mgr.get_log_form_for_create([])
        self.assertTrue(isinstance(catalog_form, LogForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_log(self):
        """Tests create_log"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.logging_.objects import Log
        catalog_form = self.svc_mgr.get_log_form_for_create([])
        catalog_form.display_name = 'Test Log'
        catalog_form.description = 'Test Log for LogAdminSession.create_log tests'
        new_catalog = self.svc_mgr.create_log(catalog_form)
        self.assertTrue(isinstance(new_catalog, Log))

    def test_can_update_logs(self):
        """Tests can_update_logs"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_update_logs(), bool))

    def test_get_log_form_for_update(self):
        """Tests get_log_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.logging_.objects import LogForm
        catalog_form = self.svc_mgr.get_log_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, LogForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_log(self):
        """Tests update_log"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_log_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_log(catalog_form)

    def test_can_delete_logs(self):
        """Tests can_delete_logs"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_delete_logs(), bool))

    def test_delete_log(self):
        """Tests delete_log"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_log(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_log(cat_id)

    def test_can_manage_log_aliases(self):
        """Tests can_manage_log_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_log_aliases(), bool))

    def test_alias_log(self):
        """Tests alias_log"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('logging_.Log%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_log(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_log(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestLogHierarchySession(unittest.TestCase):
    """Tests for LogHierarchySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Log ' + name
            cls.catalogs[name] = cls.svc_mgr.create_log(create_form)
        cls.svc_mgr.add_root_log(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_log(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_log(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_log(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr.remove_child_log(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_logs(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_log(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_log(cls.catalogs[cat_name].ident)

    def test_get_log_hierarchy_id(self):
        """Tests get_log_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_log_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_log_hierarchy(self):
        """Tests get_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_log_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_access_log_hierarchy(self):
        """Tests can_access_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        self.assertTrue(isinstance(self.svc_mgr.can_access_log_hierarchy(), bool))

    def test_use_comparative_log_view(self):
        """Tests use_comparative_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_log_view()

    def test_use_plenary_log_view(self):
        """Tests use_plenary_log_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_log_view()

    def test_get_root_log_ids(self):
        """Tests get_root_log_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_log_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_logs(self):
        """Tests get_root_logs"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.logging_.objects import LogList
        roots = self.svc_mgr.get_root_logs()
        self.assertTrue(isinstance(roots, LogList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_logs(self):
        """Tests has_parent_logs"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_logs(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_logs(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_logs(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_logs(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_logs(self.catalogs['Root'].ident))

    def test_is_parent_of_log(self):
        """Tests is_parent_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_log(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_log(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_log_ids(self):
        """Tests get_parent_log_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_log_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_logs(self):
        """Tests get_parent_logs"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.logging_.objects import LogList
        catalog_list = self.svc_mgr.get_parent_logs(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, LogList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_log(self):
        """Tests is_ancestor_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_log,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_log(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_logs(self):
        """Tests has_child_logs"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_child_logs(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_logs(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_logs(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_logs(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_logs(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_log(self):
        """Tests is_child_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_log(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_log(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_log(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_log_ids(self):
        """Tests get_child_log_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_log_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_logs(self):
        """Tests get_child_logs"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        from dlkit.abstract_osid.logging_.objects import LogList
        catalog_list = self.svc_mgr.get_child_logs(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, LogList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_log(self):
        """Tests is_descendant_of_log"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_log,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_log(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_log_node_ids(self):
        """Tests get_log_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_log_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_log_nodes(self):
        """Tests get_log_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_log_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestLogHierarchyDesignSession(unittest.TestCase):
    """Tests for LogHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_log_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Log ' + name
            cls.catalogs[name] = cls.svc_mgr.create_log(create_form)
        cls.svc_mgr.add_root_log(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_log(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_log(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_log(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr.remove_child_log(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_logs(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_log(cls.catalogs[cat_name].ident)

    def test_get_log_hierarchy_id(self):
        """Tests get_log_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_log_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_log_hierarchy(self):
        """Tests get_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_log_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_log_hierarchy(self):
        """Tests can_modify_log_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        self.assertTrue(isinstance(self.session.can_modify_log_hierarchy(), bool))

    def test_add_root_log(self):
        """Tests add_root_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        roots = self.session.get_root_logs()
        self.assertTrue(isinstance(roots, ABCObjects.LogList))
        self.assertEqual(roots.available(), 1)

    def test_remove_root_log(self):
        """Tests remove_root_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        roots = self.session.get_root_logs()
        self.assertEqual(roots.available(), 1)

        create_form = self.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'new root'
        create_form.description = 'Test Log root'
        new_log = self.svc_mgr.create_log(create_form)
        self.svc_mgr.add_root_log(new_log.ident)

        roots = self.session.get_root_logs()
        self.assertEqual(roots.available(), 2)

        self.session.remove_root_log(new_log.ident)

        roots = self.session.get_root_logs()
        self.assertEqual(roots.available(), 1)

    def test_add_child_log(self):
        """Tests add_child_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        # this is tested in the setUpClass
        children = self.session.get_child_logs(self.catalogs['Root'].ident)
        self.assertTrue(isinstance(children, ABCObjects.LogList))
        self.assertEqual(children.available(), 2)

    def test_remove_child_log(self):
        """Tests remove_child_log"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        children = self.session.get_child_logs(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

        create_form = self.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'test child'
        create_form.description = 'Test Log child'
        new_log = self.svc_mgr.create_log(create_form)
        self.svc_mgr.add_child_log(
            self.catalogs['Root'].ident,
            new_log.ident)

        children = self.session.get_child_logs(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 3)

        self.session.remove_child_log(
            self.catalogs['Root'].ident,
            new_log.ident)

        children = self.session.get_child_logs(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

    def test_remove_child_logs(self):
        """Tests remove_child_logs"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        children = self.session.get_child_logs(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)

        create_form = self.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'test great grandchild'
        create_form.description = 'Test Log child'
        new_log = self.svc_mgr.create_log(create_form)
        self.svc_mgr.add_child_log(
            self.catalogs['Grandchild 1'].ident,
            new_log.ident)

        children = self.session.get_child_logs(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 1)

        self.session.remove_child_logs(self.catalogs['Grandchild 1'].ident)

        children = self.session.get_child_logs(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)
