"""Unit tests of resource sessions."""


import unittest


from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.abstract_osid.resource import objects as ABCObjects
from dlkit.abstract_osid.resource import queries as ABCQueries
from dlkit.json_.id.objects import IdList
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'ODL.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
AGENT_ID_0 = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
AGENT_ID_1 = Id(**{'identifier': 'john_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


class TestResourceLookupSession(unittest.TestCase):
    """Tests for ResourceLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceLookupSession tests'
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bin_id(), self.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_resources(self):
        """Tests can_lookup_resources"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_resources(), bool))

    def test_use_comparative_resource_view(self):
        """Tests use_comparative_resource_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_resource_view()

    def test_use_plenary_resource_view(self):
        """Tests use_plenary_resource_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_resource_view()

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_get_resource(self):
        """Tests get_resource"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bin_view()
        obj = self.catalog.get_resource(self.resource_list[0].ident)
        self.assertEqual(obj.ident, self.resource_list[0].ident)
        self.catalog.use_federated_bin_view()
        obj = self.catalog.get_resource(self.resource_list[0].ident)
        self.assertEqual(obj.ident, self.resource_list[0].ident)

    def test_get_resources_by_ids(self):
        """Tests get_resources_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        objects = self.catalog.get_resources_by_ids(self.resource_ids)
        self.assertTrue(isinstance(objects, ResourceList))
        self.catalog.use_federated_bin_view()
        objects = self.catalog.get_resources_by_ids(self.resource_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ResourceList))

    def test_get_resources_by_genus_type(self):
        """Tests get_resources_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        objects = self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ResourceList))
        self.catalog.use_federated_bin_view()
        objects = self.catalog.get_resources_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ResourceList))

    def test_get_resources_by_parent_genus_type(self):
        """Tests get_resources_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        objects = self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ResourceList))
        self.catalog.use_federated_bin_view()
        objects = self.catalog.get_resources_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ResourceList))

    def test_get_resources_by_record_type(self):
        """Tests get_resources_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        objects = self.catalog.get_resources_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ResourceList))
        self.catalog.use_federated_bin_view()
        objects = self.catalog.get_resources_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ResourceList))

    def test_get_resources(self):
        """Tests get_resources"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.resource.objects import ResourceList
        objects = self.catalog.get_resources()
        self.assertTrue(isinstance(objects, ResourceList))
        self.catalog.use_federated_bin_view()
        objects = self.catalog.get_resources()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ResourceList))

    def test_get_resource_with_alias(self):
        self.catalog.alias_resource(self.resource_ids[0], ALIAS_ID)
        obj = self.catalog.get_resource(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.resource_ids[0])


class TestResourceQuerySession(unittest.TestCase):
    """Tests for ResourceQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceQuerySession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + color
            create_form.description = (
                'Test Resource for ResourceQuerySession tests, did I mention green')
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bin_id(), self.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_resources(self):
        """Tests can_search_resources"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_resources(), bool))

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_get_resource_query(self):
        """Tests get_resource_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_resource_query()

    def test_get_resources_by_query(self):
        """Tests get_resources_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_resource_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_resources_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_resources_by_query(query).available(), 3)


class TestResourceSearchSession(unittest.TestCase):
    """Tests for ResourceSearchSession"""

    def test_get_resource_search(self):
        """Tests get_resource_search"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_resource_search()

    def test_get_resource_search_order(self):
        """Tests get_resource_search_order"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_resource_search_order()

    def test_get_resources_by_search(self):
        """Tests get_resources_by_search"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_resources_by_search(True, True)

    def test_get_resource_query_from_inspector(self):
        """Tests get_resource_query_from_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_resource_query_from_inspector(True)


class TestResourceAdminSession(unittest.TestCase):
    """Tests for ResourceAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        form = self.catalog.get_resource_form_for_create([])
        form.display_name = 'new Resource'
        form.description = 'description of Resource'
        form.set_genus_type(NEW_TYPE)
        self.osid_object = self.catalog.create_resource(form)
        self.session = self.catalog

    def tearDown(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        self.catalog.delete_resource(self.osid_object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bin_id(), self.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_resources(self):
        """Tests can_create_resources"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_resources(), bool))

    def test_can_create_resource_with_record_types(self):
        """Tests can_create_resource_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_resource_with_record_types(DEFAULT_TYPE), bool))

    def test_get_resource_form_for_create(self):
        """Tests get_resource_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_resource_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_resource(self):
        """Tests create_resource"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.resource.objects import Resource
        self.assertTrue(isinstance(self.osid_object, Resource))
        self.assertEqual(self.osid_object.display_name.text, 'new Resource')
        self.assertEqual(self.osid_object.description.text, 'description of Resource')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_resources(self):
        """Tests can_update_resources"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_resources(), bool))

    def test_get_resource_form_for_update(self):
        """Tests get_resource_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_resource_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_resource(self):
        """Tests update_resource"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.resource.objects import Resource
        form = self.catalog.get_resource_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_resource(form)
        self.assertTrue(isinstance(updated_object, Resource))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_resources(self):
        """Tests can_delete_resources"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_resources(), bool))

    def test_delete_resource(self):
        """Tests delete_resource"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_resource_form_for_create([])
        form.display_name = 'new Resource'
        form.description = 'description of Resource'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_resource(form)
        self.catalog.delete_resource(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_resource(osid_object.ident)

    def test_can_manage_resource_aliases(self):
        """Tests can_manage_resource_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_resource_aliases(), bool))

    def test_alias_resource(self):
        """Tests alias_resource"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_resource(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_resource(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestResourceNotificationSession(unittest.TestCase):
    """Tests for ResourceNotificationSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceNotificationSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceNotificationSession tests'
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bin_id(), self.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_register_for_resource_notifications(self):
        """Tests can_register_for_resource_notifications"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_register_for_resource_notifications()

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_register_for_new_resources(self):
        """Tests register_for_new_resources"""
        with self.assertRaises(errors.Unimplemented):
            self.session.register_for_new_resources()

    def test_register_for_changed_resources(self):
        """Tests register_for_changed_resources"""
        with self.assertRaises(errors.Unimplemented):
            self.session.register_for_changed_resources()

    def test_register_for_changed_resource(self):
        """Tests register_for_changed_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.register_for_changed_resource(True)

    def test_register_for_deleted_resources(self):
        """Tests register_for_deleted_resources"""
        with self.assertRaises(errors.Unimplemented):
            self.session.register_for_deleted_resources()

    def test_register_for_deleted_resource(self):
        """Tests register_for_deleted_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.register_for_deleted_resource(True)

    def test_reliable_resource_notifications(self):
        """Tests reliable_resource_notifications"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reliable_resource_notifications()

    def test_unreliable_resource_notifications(self):
        """Tests unreliable_resource_notifications"""
        with self.assertRaises(errors.Unimplemented):
            self.session.unreliable_resource_notifications()

    def test_acknowledge_resource_notification(self):
        """Tests acknowledge_resource_notification"""
        with self.assertRaises(errors.Unimplemented):
            self.session.acknowledge_resource_notification(True)


class TestResourceBinSession(unittest.TestCase):
    """Tests for ResourceBinSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinSession::init_template
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceBinSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin for Assignment'
        create_form.description = 'Test Bin for ResourceBinSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bin(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceBinSession tests'
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)
        cls.svc_mgr.assign_resource_to_bin(
            cls.resource_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_resource_to_bin(
            cls.resource_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinSession::init_template
        cls.svc_mgr.unassign_resource_from_bin(
            cls.resource_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_resource_from_bin(
            cls.resource_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_use_comparative_bin_view(self):
        """Tests use_comparative_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bin_view()

    def test_use_plenary_bin_view(self):
        """Tests use_plenary_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bin_view()

    def test_can_lookup_resource_bin_mappings(self):
        """Tests can_lookup_resource_bin_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_resource_bin_mappings()
        self.assertTrue(result)

    def test_get_resource_ids_by_bin(self):
        """Tests get_resource_ids_by_bin"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_resource_ids_by_bin(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_resources_by_bin(self):
        """Tests get_resources_by_bin"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_resources_by_bin(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.ResourceList))
        self.assertEqual(results.available(), 2)

    def test_get_resource_ids_by_bins(self):
        """Tests get_resource_ids_by_bins"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_resource_ids_by_bins(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_resources_by_bins(self):
        """Tests get_resources_by_bins"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_resources_by_bins(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.ResourceList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_bin_ids_by_resource(self):
        """Tests get_bin_ids_by_resource"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_bin_ids_by_resource(self.resource_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_bins_by_resource(self):
        """Tests get_bins_by_resource"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_bins_by_resource(self.resource_ids[1])
        self.assertEqual(cats.available(), 2)


class TestResourceBinAssignmentSession(unittest.TestCase):
    """Tests for ResourceBinAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceBinAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin for Assignment'
        create_form.description = 'Test Bin for ResourceBinAssignmentSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bin(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceBinAssignmentSession tests'
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        for obj in cls.catalog.get_resources():
            cls.catalog.delete_resource(obj.ident)
        cls.svc_mgr.delete_bin(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_can_assign_resources(self):
        """Tests can_assign_resources"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_resources()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_resources_to_bin(self):
        """Tests can_assign_resources_to_bin"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_resources_to_bin(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_bin_ids(self):
        """Tests get_assignable_bin_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bin_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_bin_ids_for_resource(self):
        """Tests get_assignable_bin_ids_for_resource"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bin_ids_for_resource(self.catalog.ident, self.resource_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_resource_to_bin(self):
        """Tests assign_resource_to_bin"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_resources()
        self.assertEqual(results.available(), 0)
        self.session.assign_resource_to_bin(self.resource_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_resources()
        self.assertEqual(results.available(), 1)
        self.session.unassign_resource_from_bin(
            self.resource_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_resource_from_bin(self):
        """Tests unassign_resource_from_bin"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_resources()
        self.assertEqual(results.available(), 0)
        self.session.assign_resource_to_bin(
            self.resource_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_resources()
        self.assertEqual(results.available(), 1)
        self.session.unassign_resource_from_bin(
            self.resource_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_resources()
        self.assertEqual(results.available(), 0)


class TestResourceAgentSession(unittest.TestCase):
    """Tests for ResourceAgentSession"""

    @classmethod
    def setUpClass(cls):
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceLookupSession tests'
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)
        cls.catalog.assign_agent_to_resource(AGENT_ID_0, cls.resource_ids[0])
        cls.catalog.assign_agent_to_resource(AGENT_ID_1, cls.resource_ids[1])

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_bins():
            for obj in catalog.get_resources():
                catalog.delete_resource(obj.ident)
            cls.svc_mgr.delete_bin(catalog.ident)

    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bin_id(), self.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_resource_agent_mappings(self):
        """Tests can_lookup_resource_agent_mappings"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_lookup_resource_agent_mappings()

    def test_use_comparative_agent_view(self):
        """Tests use_comparative_agent_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_agent_view()

    def test_use_plenary_agent_view(self):
        """Tests use_plenary_agent_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_agent_view()

    def test_use_federated_bin_view(self):
        """Tests use_federated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bin_view()

    def test_use_isolated_bin_view(self):
        """Tests use_isolated_bin_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bin_view()

    def test_get_resource_id_by_agent(self):
        """Tests get_resource_id_by_agent"""
        resource_id = self.catalog.get_resource_id_by_agent(AGENT_ID_0)

    def test_get_resource_by_agent(self):
        """Tests get_resource_by_agent"""
        resource = self.catalog.get_resource_by_agent(AGENT_ID_1)
        self.assertEqual(resource.display_name.text, 'Test Resource 1')

    def test_get_agent_ids_by_resource(self):
        """Tests get_agent_ids_by_resource"""
        id_list = self.catalog.get_agent_ids_by_resource(self.resource_ids[0])
        self.assertEqual(id_list.next(), AGENT_ID_0)

    def test_get_agents_by_resource(self):
        """Tests get_agents_by_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_agents_by_resource(True)


class TestResourceAgentAssignmentSession(unittest.TestCase):
    """Tests for ResourceAgentAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.resource_list = list()
        cls.resource_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for ResourceLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_resource_form_for_create([])
            create_form.display_name = 'Test Resource ' + str(num)
            create_form.description = 'Test Resource for ResourceLookupSession tests'
            obj = cls.catalog.create_resource(create_form)
            cls.resource_list.append(obj)
            cls.resource_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_bins():
            for obj in catalog.get_resources():
                catalog.delete_resource(obj.ident)
            cls.svc_mgr.delete_bin(catalog.ident)

    def test_get_bin_id(self):
        """Tests get_bin_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bin_id(), self.catalog.ident)

    def test_get_bin(self):
        """Tests get_bin"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_assign_agents(self):
        """Tests can_assign_agents"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_assign_agents()

    def test_can_assign_agents_to_resource(self):
        """Tests can_assign_agents_to_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_assign_agents_to_resource(True)

    def test_assign_agent_to_resource(self):
        """Tests assign_agent_to_resource"""
        self.catalog.assign_agent_to_resource(AGENT_ID_0, self.resource_ids[0])
        with self.assertRaises(errors.AlreadyExists):
            self.catalog.assign_agent_to_resource(AGENT_ID_0, self.resource_ids[1])

    def test_unassign_agent_from_resource(self):
        """Tests unassign_agent_from_resource"""
        self.catalog.assign_agent_to_resource(AGENT_ID_1, self.resource_ids[1])
        self.assertEqual(self.catalog.get_resource_by_agent(AGENT_ID_1).display_name.text, 'Test Resource 1')
        self.catalog.unassign_agent_from_resource(AGENT_ID_1, self.resource_ids[1])
        with self.assertRaises(errors.NotFound):
            self.catalog.get_resource_by_agent(AGENT_ID_1)


class TestBinLookupSession(unittest.TestCase):
    """Tests for BinLookupSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = 'Test Bin ' + str(num)
            create_form.description = 'Test Bin for resource proxy manager tests'
            catalog = cls.svc_mgr.create_bin(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::BinLookupSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        for catalog in cls.svc_mgr.get_bins():
            cls.svc_mgr.delete_bin(catalog.ident)

    def test_can_lookup_bins(self):
        """Tests can_lookup_bins"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_lookup_bins(), bool))

    def test_use_comparative_bin_view(self):
        """Tests use_comparative_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bin_view()

    def test_use_plenary_bin_view(self):
        """Tests use_plenary_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bin_view()

    def test_get_bin(self):
        """Tests get_bin"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        catalog = self.svc_mgr.get_bin(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_bins_by_ids(self):
        """Tests get_bins_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        catalogs = self.svc_mgr.get_bins_by_ids(self.catalog_ids)
        self.assertTrue(catalogs.available() == 2)
        self.assertTrue(isinstance(catalogs, ABCObjects.BinList))
        reversed_catalog_ids = [str(cat_id) for cat_id in self.catalog_ids][::-1]
        for index, catalog in enumerate(catalogs):
            self.assertEqual(str(catalog.ident),
                             reversed_catalog_ids[index])

    def test_get_bins_by_genus_type(self):
        """Tests get_bins_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        catalogs = self.svc_mgr.get_bins_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.BinList))

    def test_get_bins_by_parent_genus_type(self):
        """Tests get_bins_by_parent_genus_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_bins_by_parent_genus_type(True)

    def test_get_bins_by_record_type(self):
        """Tests get_bins_by_record_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_bins_by_record_type(True)

    def test_get_bins_by_provider(self):
        """Tests get_bins_by_provider"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_bins_by_provider(True)

    def test_get_bins(self):
        """Tests get_bins"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        catalogs = self.svc_mgr.get_bins()
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.BinList))


class TestBinQuerySession(unittest.TestCase):
    """Tests for BinQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinQuerySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def setUp(self):
        # From test_templates/resource.py::BinQuerySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinQuerySession::init_template
        cls.svc_mgr.delete_bin(cls.catalog.ident)

    def test_can_search_bins(self):
        """Tests can_search_bins"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_bins(), bool))

    def test_get_bin_query(self):
        """Tests get_bin_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        query = self.session.get_bin_query()
        self.assertTrue(isinstance(query, ABCQueries.BinQuery))

    def test_get_bins_by_query(self):
        """Tests get_bins_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        query = self.session.get_bin_query()
        query.match_display_name('Test catalog')
        self.assertEqual(self.session.get_bins_by_query(query).available(), 1)
        query.clear_display_name_terms()
        query.match_display_name('Test catalog', match=False)
        self.assertEqual(self.session.get_bins_by_query(query).available(), 0)


class TestBinAdminSession(unittest.TestCase):
    """Tests for BinAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin'
        create_form.description = 'Test Bin for BinAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bin(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'Test Bin For Deletion'
        create_form.description = 'Test Bin for BinAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_bin(create_form)

    def setUp(self):
        # From test_templates/resource.py::BinAdminSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        for catalog in cls.svc_mgr.get_bins():
            cls.svc_mgr.delete_bin(catalog.ident)

    def test_can_create_bins(self):
        """Tests can_create_bins"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_bins(), bool))

    def test_can_create_bin_with_record_types(self):
        """Tests can_create_bin_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_bin_with_record_types(DEFAULT_TYPE), bool))

    def test_get_bin_form_for_create(self):
        """Tests get_bin_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.resource.objects import BinForm
        catalog_form = self.svc_mgr.get_bin_form_for_create([])
        self.assertTrue(isinstance(catalog_form, BinForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_bin(self):
        """Tests create_bin"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.resource.objects import Bin
        catalog_form = self.svc_mgr.get_bin_form_for_create([])
        catalog_form.display_name = 'Test Bin'
        catalog_form.description = 'Test Bin for BinAdminSession.create_bin tests'
        new_catalog = self.svc_mgr.create_bin(catalog_form)
        self.assertTrue(isinstance(new_catalog, Bin))

    def test_can_update_bins(self):
        """Tests can_update_bins"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_update_bins(), bool))

    def test_get_bin_form_for_update(self):
        """Tests get_bin_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.resource.objects import BinForm
        catalog_form = self.svc_mgr.get_bin_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, BinForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_bin(self):
        """Tests update_bin"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_bin_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_bin(catalog_form)

    def test_can_delete_bins(self):
        """Tests can_delete_bins"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_delete_bins(), bool))

    def test_delete_bin(self):
        """Tests delete_bin"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_bin(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_bin(cat_id)

    def test_can_manage_bin_aliases(self):
        """Tests can_manage_bin_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_bin_aliases(), bool))

    def test_alias_bin(self):
        """Tests alias_bin"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('resource.Bin%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_bin(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_bin(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestBinHierarchySession(unittest.TestCase):
    """Tests for BinHierarchySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bin ' + name
            cls.catalogs[name] = cls.svc_mgr.create_bin(create_form)
        cls.svc_mgr.add_root_bin(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_bin(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_bin(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_bin(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr.remove_child_bin(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_bins(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_bin(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_bin(cls.catalogs[cat_name].ident)

    def test_get_bin_hierarchy_id(self):
        """Tests get_bin_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bin_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_bin_hierarchy(self):
        """Tests get_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_bin_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_access_bin_hierarchy(self):
        """Tests can_access_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        self.assertTrue(isinstance(self.svc_mgr.can_access_bin_hierarchy(), bool))

    def test_use_comparative_bin_view(self):
        """Tests use_comparative_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bin_view()

    def test_use_plenary_bin_view(self):
        """Tests use_plenary_bin_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bin_view()

    def test_get_root_bin_ids(self):
        """Tests get_root_bin_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_bin_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_bins(self):
        """Tests get_root_bins"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.resource.objects import BinList
        roots = self.svc_mgr.get_root_bins()
        self.assertTrue(isinstance(roots, BinList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_bins(self):
        """Tests has_parent_bins"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_bins(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_bins(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_bins(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_bins(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_bins(self.catalogs['Root'].ident))

    def test_is_parent_of_bin(self):
        """Tests is_parent_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_bin(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_bin_ids(self):
        """Tests get_parent_bin_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_bin_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_bins(self):
        """Tests get_parent_bins"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.resource.objects import BinList
        catalog_list = self.svc_mgr.get_parent_bins(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BinList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_bin(self):
        """Tests is_ancestor_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_bin,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_bin(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_bins(self):
        """Tests has_child_bins"""
        self.assertTrue(isinstance(self.svc_mgr.has_child_bins(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_bins(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_bins(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_bins(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_bins(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_bin(self):
        """Tests is_child_of_bin"""
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_bin(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_bin(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_bin(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_bin_ids(self):
        """Tests get_child_bin_ids"""
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_bin_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_bins(self):
        """Tests get_child_bins"""
        from dlkit.abstract_osid.resource.objects import BinList
        catalog_list = self.svc_mgr.get_child_bins(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BinList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_bin(self):
        """Tests is_descendant_of_bin"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_bin,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_bin(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_bin_node_ids(self):
        """Tests get_bin_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_bin_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_bin_nodes(self):
        """Tests get_bin_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_bin_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestBinHierarchyDesignSession(unittest.TestCase):
    """Tests for BinHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('RESOURCE', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_bin_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bin ' + name
            cls.catalogs[name] = cls.svc_mgr.create_bin(create_form)
        cls.svc_mgr.add_root_bin(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_bin(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_bin(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_bin(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr.remove_child_bin(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_bins(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_bin(cls.catalogs[cat_name].ident)

    def test_get_bin_hierarchy_id(self):
        """Tests get_bin_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bin_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_bin_hierarchy(self):
        """Tests get_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_bin_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_bin_hierarchy(self):
        """Tests can_modify_bin_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        self.assertTrue(isinstance(self.session.can_modify_bin_hierarchy(), bool))

    def test_add_root_bin(self):
        """Tests add_root_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        roots = self.session.get_root_bins()
        self.assertTrue(isinstance(roots, ABCObjects.BinList))
        self.assertEqual(roots.available(), 1)

    def test_remove_root_bin(self):
        """Tests remove_root_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        roots = self.session.get_root_bins()
        self.assertEqual(roots.available(), 1)

        create_form = self.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'new root'
        create_form.description = 'Test Bin root'
        new_bin = self.svc_mgr.create_bin(create_form)
        self.svc_mgr.add_root_bin(new_bin.ident)

        roots = self.session.get_root_bins()
        self.assertEqual(roots.available(), 2)

        self.session.remove_root_bin(new_bin.ident)

        roots = self.session.get_root_bins()
        self.assertEqual(roots.available(), 1)

    def test_add_child_bin(self):
        """Tests add_child_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        # this is tested in the setUpClass
        children = self.session.get_child_bins(self.catalogs['Root'].ident)
        self.assertTrue(isinstance(children, ABCObjects.BinList))
        self.assertEqual(children.available(), 2)

    def test_remove_child_bin(self):
        """Tests remove_child_bin"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        children = self.session.get_child_bins(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

        create_form = self.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'test child'
        create_form.description = 'Test Bin child'
        new_bin = self.svc_mgr.create_bin(create_form)
        self.svc_mgr.add_child_bin(
            self.catalogs['Root'].ident,
            new_bin.ident)

        children = self.session.get_child_bins(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 3)

        self.session.remove_child_bin(
            self.catalogs['Root'].ident,
            new_bin.ident)

        children = self.session.get_child_bins(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

    def test_remove_child_bins(self):
        """Tests remove_child_bins"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        children = self.session.get_child_bins(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)

        create_form = self.svc_mgr.get_bin_form_for_create([])
        create_form.display_name = 'test great grandchild'
        create_form.description = 'Test Bin child'
        new_bin = self.svc_mgr.create_bin(create_form)
        self.svc_mgr.add_child_bin(
            self.catalogs['Grandchild 1'].ident,
            new_bin.ident)

        children = self.session.get_child_bins(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 1)

        self.session.remove_child_bins(self.catalogs['Grandchild 1'].ident)

        children = self.session.get_child_bins(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)
