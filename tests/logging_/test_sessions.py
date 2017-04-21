"""Unit tests of logging sessions."""


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
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})


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

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_logs():
            cls.svc_mgr.delete_log(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_log_id(self):
        """Tests get_log_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log(self):
        """Tests get_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_log(self):
        """Tests can_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_log(self):
        """Tests log"""
        pass

    @unittest.skip('unimplemented test')
    def test_log_at_priority(self):
        """Tests log_at_priority"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entry_form(self):
        """Tests get_log_entry_form"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_log_entry(self):
        """Tests create_log_entry"""
        pass


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

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for catalog in cls.svc_mgr.get_logs():
            for obj in catalog.get_log_entries():
                catalog.delete_log_entry(obj.ident)
            cls.svc_mgr.delete_log(catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_log(self):
        """Tests get_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_read_log(self):
        """Tests can_read_log"""
        pass

    def test_use_comparative_log_entry_view(self):
        """Tests use_comparative_log_entry_view"""
        self.catalog.use_comparative_log_entry_view()

    def test_use_plenary_log_entry_view(self):
        """Tests use_plenary_log_entry_view"""
        self.catalog.use_plenary_log_entry_view()

    def test_use_federated_log_view(self):
        """Tests use_federated_log_view"""
        self.catalog.use_federated_log_view()

    def test_use_isolated_log_view(self):
        """Tests use_isolated_log_view"""
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

    def test_get_log_entries_by_genus_type(self):
        """Tests get_log_entries_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_genus_type(DEFAULT_TYPE)

    def test_get_log_entries_by_parent_genus_type(self):
        """Tests get_log_entries_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_log_entries_by_record_type(self):
        """Tests get_log_entries_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_log_entries_by_priority_type(self):
        """Tests get_log_entries_by_priority_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entries_by_date(self):
        """Tests get_log_entries_by_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entries_by_priority_type_and_date(self):
        """Tests get_log_entries_by_priority_type_and_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entries_for_resource(self):
        """Tests get_log_entries_for_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entries_by_date_for_resource(self):
        """Tests get_log_entries_by_date_for_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entries_by_priority_type_and_date_for_resource(self):
        """Tests get_log_entries_by_priority_type_and_date_for_resource"""
        pass

    def test_get_log_entries(self):
        """Tests get_log_entries"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.logging_.objects import LogEntryList
        objects = self.catalog.get_log_entries()
        self.assertTrue(isinstance(objects, LogEntryList))
        self.catalog.use_federated_log_view()
        objects = self.catalog.get_log_entries()

    def test_get_log_entry_with_alias(self):
        self.catalog.alias_log_entry(self.log_entry_ids[0], ALIAS_ID)
        obj = self.catalog.get_log_entry(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.log_entry_ids[0])


class TestLogEntryQuerySession(unittest.TestCase):
    """Tests for LogEntryQuerySession"""

    @classmethod
    def setUpClass(cls):
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

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_logs():
            for obj in catalog.get_log_entries():
                catalog.delete_log_entry(obj.ident)
            cls.svc_mgr.delete_log(catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_log(self):
        """Tests get_log"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_search_log_entries(self):
        """Tests can_search_log_entries"""
        pass

    def test_use_federated_log_view(self):
        """Tests use_federated_log_view"""
        self.catalog.use_federated_log_view()

    def test_use_isolated_log_view(self):
        """Tests use_isolated_log_view"""
        self.catalog.use_isolated_log_view()

    def test_get_log_entry_query(self):
        """Tests get_log_entry_query"""
        query = self.catalog.get_log_entry_query()

    def test_get_log_entries_by_query(self):
        """Tests get_log_entries_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_log_entry_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_log_entries_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_log_entries_by_query(query).available(), 3)


class TestLogEntryAdminSession(unittest.TestCase):
    """Tests for LogEntryAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LOGGING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_log_form_for_create([])
        create_form.display_name = 'Test Log'
        create_form.description = 'Test Log for LogEntryAdminSession tests'
        cls.catalog = cls.svc_mgr.create_log(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_log_entries():
            cls.catalog.delete_log_entry(obj.ident)
        cls.svc_mgr.delete_log(cls.catalog.ident)

    def test_get_log_id(self):
        """Tests get_log_id"""
        self.assertEqual(self.catalog.get_log_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_log(self):
        """Tests get_log"""
        pass

    def test_can_create_log_entries(self):
        """Tests can_create_log_entries"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.catalog.can_create_log_entries(), bool))

    def test_can_create_log_entry_with_record_types(self):
        """Tests can_create_log_entry_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_log_entry_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_log_entry_form_for_create(self):
        """Tests get_log_entry_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_log_entry(self):
        """Tests create_log_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_log_entries(self):
        """Tests can_update_log_entries"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_log_entry_form_for_update(self):
        """Tests get_log_entry_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_log_entry(self):
        """Tests update_log_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_log_entries(self):
        """Tests can_delete_log_entries"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_log_entry(self):
        """Tests delete_log_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_manage_log_entry_aliases(self):
        """Tests can_manage_log_entry_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_log_entry(self):
        """Tests alias_log_entry"""
        pass


class TestLogLookupSession(unittest.TestCase):
    """Tests for LogLookupSession"""

    @classmethod
    def setUpClass(cls):
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

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_logs():
            cls.svc_mgr.delete_log(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_logs(self):
        """Tests can_lookup_logs"""
        pass

    def test_use_comparative_log_view(self):
        """Tests use_comparative_log_view"""
        self.svc_mgr.use_comparative_log_view()

    def test_use_plenary_log_view(self):
        """Tests use_plenary_log_view"""
        self.svc_mgr.use_plenary_log_view()

    def test_get_log(self):
        """Tests get_log"""
        catalog = self.svc_mgr.get_log(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_logs_by_ids(self):
        """Tests get_logs_by_ids"""
        catalogs = self.svc_mgr.get_logs_by_ids(self.catalog_ids)

    @unittest.skip('unimplemented test')
    def test_get_logs_by_genus_type(self):
        """Tests get_logs_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_logs_by_parent_genus_type(self):
        """Tests get_logs_by_parent_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_logs_by_record_type(self):
        """Tests get_logs_by_record_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_logs_by_provider(self):
        """Tests get_logs_by_provider"""
        pass

    def test_get_logs(self):
        """Tests get_logs"""
        catalogs = self.svc_mgr.get_logs()


class TestLogAdminSession(unittest.TestCase):
    """Tests for LogAdminSession"""

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

    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip('unimplemented test')
    def test_can_update_logs(self):
        """Tests can_update_logs"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_can_delete_logs(self):
        """Tests can_delete_logs"""
        pass

    def test_delete_log(self):
        """Tests delete_log"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_log(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_log(cat_id)

    @unittest.skip('unimplemented test')
    def test_can_manage_log_aliases(self):
        """Tests can_manage_log_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_log(self):
        """Tests alias_log"""
        pass
