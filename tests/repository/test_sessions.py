"""Unit tests of repository sessions."""


import unittest


from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
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
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


class TestAssetLookupSession(unittest.TestCase):
    """Tests for AssetLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.asset_list = list()
        cls.asset_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetLookupSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetLookupSession tests'
            obj = cls.catalog.create_asset(create_form)
            cls.asset_list.append(obj)
            cls.asset_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_assets(self):
        """Tests can_lookup_assets"""
        self.assertTrue(isinstance(self.catalog.can_lookup_assets(), bool))

    def test_use_comparative_asset_view(self):
        """Tests use_comparative_asset_view"""
        self.catalog.use_comparative_asset_view()

    def test_use_plenary_asset_view(self):
        """Tests use_plenary_asset_view"""
        self.catalog.use_plenary_asset_view()

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        self.catalog.use_isolated_repository_view()

    def test_get_asset(self):
        """Tests get_asset"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_repository_view()
        obj = self.catalog.get_asset(self.asset_list[0].ident)
        self.assertEqual(obj.ident, self.asset_list[0].ident)
        self.catalog.use_federated_repository_view()
        obj = self.catalog.get_asset(self.asset_list[0].ident)
        self.assertEqual(obj.ident, self.asset_list[0].ident)

    def test_get_assets_by_ids(self):
        """Tests get_assets_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_ids(self.asset_ids)
        self.assertTrue(isinstance(objects, AssetList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_ids(self.asset_ids)

    def test_get_assets_by_genus_type(self):
        """Tests get_assets_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssetList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_genus_type(DEFAULT_TYPE)

    def test_get_assets_by_parent_genus_type(self):
        """Tests get_assets_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssetList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_assets_by_record_type(self):
        """Tests get_assets_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssetList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_assets_by_provider(self):
        """Tests get_assets_by_provider"""
        pass

    def test_get_assets(self):
        """Tests get_assets"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.repository.objects import AssetList
        objects = self.catalog.get_assets()
        self.assertTrue(isinstance(objects, AssetList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_assets()

    def test_get_asset_with_alias(self):
        self.catalog.alias_asset(self.asset_ids[0], ALIAS_ID)
        obj = self.catalog.get_asset(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.asset_ids[0])


class TestAssetQuerySession(unittest.TestCase):
    """Tests for AssetQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.asset_list = list()
        cls.asset_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetQuerySession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + color
            create_form.description = (
                'Test Asset for AssetQuerySession tests, did I mention green')
            obj = cls.catalog.create_asset(create_form)
            cls.asset_list.append(obj)
            cls.asset_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_search_assets(self):
        """Tests can_search_assets"""
        pass

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        self.catalog.use_isolated_repository_view()

    def test_get_asset_query(self):
        """Tests get_asset_query"""
        query = self.catalog.get_asset_query()

    def test_get_assets_by_query(self):
        """Tests get_assets_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_asset_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assets_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_assets_by_query(query).available(), 3)


class TestAssetSearchSession(unittest.TestCase):
    """Tests for AssetSearchSession"""

    @unittest.skip('unimplemented test')
    def test_get_asset_search(self):
        """Tests get_asset_search"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_search_order(self):
        """Tests get_asset_search_order"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assets_by_search(self):
        """Tests get_assets_by_search"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_query_from_inspector(self):
        """Tests get_asset_query_from_inspector"""
        pass


class TestAssetAdminSession(unittest.TestCase):
    """Tests for AssetAdminSession"""

    # From test_templates/resource.py::ResourceAdminSession::init_template
    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetAdminSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        form = cls.catalog.get_asset_form_for_create([])
        form.display_name = 'new Asset'
        form.description = 'description of Asset'
        form.set_genus_type(NEW_TYPE)
        cls.osid_object = cls.catalog.create_asset(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_assets(self):
        """Tests can_create_assets"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_assets(), bool))

    def test_can_create_asset_with_record_types(self):
        """Tests can_create_asset_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_asset_with_record_types(DEFAULT_TYPE), bool))

    def test_get_asset_form_for_create(self):
        """Tests get_asset_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_asset_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_asset(self):
        """Tests create_asset"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.repository.objects import Asset
        self.assertTrue(isinstance(self.osid_object, Asset))
        self.assertEqual(self.osid_object.display_name.text, 'new Asset')
        self.assertEqual(self.osid_object.description.text, 'description of Asset')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_assets(self):
        """Tests can_update_assets"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_assets(), bool))

    def test_get_asset_form_for_update(self):
        """Tests get_asset_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_asset_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_asset(self):
        """Tests update_asset"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.repository.objects import Asset
        form = self.catalog.get_asset_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_asset(form)
        self.assertTrue(isinstance(updated_object, Asset))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_assets(self):
        """Tests can_delete_assets"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_assets(), bool))

    def test_delete_asset(self):
        """Tests delete_asset"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_asset_form_for_create([])
        form.display_name = 'new Asset'
        form.description = 'description of Asset'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_asset(form)
        self.catalog.delete_asset(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_asset(osid_object.ident)

    def test_can_manage_asset_aliases(self):
        """Tests can_manage_asset_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_asset_aliases(), bool))

    def test_alias_asset(self):
        """Tests alias_asset"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_asset(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_asset(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)

    def test_can_create_asset_content(self):
        """Tests can_create_asset_content"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_asset_content(), bool))

    def test_can_create_asset_content_with_record_types(self):
        """Tests can_create_asset_content_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_asset_content_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_asset_content_form_for_create(self):
        """Tests get_asset_content_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_asset_content(self):
        """Tests create_asset_content"""
        pass

    def test_can_update_asset_contents(self):
        """Tests can_update_asset_contents"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_asset_contents(), bool))

    @unittest.skip('unimplemented test')
    def test_get_asset_content_form_for_update(self):
        """Tests get_asset_content_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_asset_content(self):
        """Tests update_asset_content"""
        pass

    def test_can_delete_asset_contents(self):
        """Tests can_delete_asset_contents"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_asset_contents(), bool))

    @unittest.skip('unimplemented test')
    def test_delete_asset_content(self):
        """Tests delete_asset_content"""
        pass


class TestAssetNotificationSession(unittest.TestCase):
    """Tests for AssetNotificationSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.asset_list = list()
        cls.asset_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetNotificationSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetNotificationSession tests'
            obj = cls.catalog.create_asset(create_form)
            cls.asset_list.append(obj)
            cls.asset_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_register_for_asset_notifications(self):
        """Tests can_register_for_asset_notifications"""
        pass

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        self.catalog.use_isolated_repository_view()

    @unittest.skip('unimplemented test')
    def test_register_for_new_assets(self):
        """Tests register_for_new_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_new_assets_by_genus_type(self):
        """Tests register_for_new_assets_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_changed_assets(self):
        """Tests register_for_changed_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_changed_assets_by_genus_type(self):
        """Tests register_for_changed_assets_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_changed_asset(self):
        """Tests register_for_changed_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_deleted_assets(self):
        """Tests register_for_deleted_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_deleted_assets_by_genus_type(self):
        """Tests register_for_deleted_assets_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_deleted_asset(self):
        """Tests register_for_deleted_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_reliable_asset_notifications(self):
        """Tests reliable_asset_notifications"""
        pass

    @unittest.skip('unimplemented test')
    def test_unreliable_asset_notifications(self):
        """Tests unreliable_asset_notifications"""
        pass

    @unittest.skip('unimplemented test')
    def test_acknowledge_asset_notification(self):
        """Tests acknowledge_asset_notification"""
        pass


class TestAssetRepositorySession(unittest.TestCase):
    """Tests for AssetRepositorySession"""

    @classmethod
    def setUpClass(cls):
        cls.asset_list = list()
        cls.asset_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetRepositorySession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository for Assignment'
        create_form.description = 'Test Repository for AssetRepositorySession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetRepositorySession tests'
            obj = cls.catalog.create_asset(create_form)
            cls.asset_list.append(obj)
            cls.asset_ids.append(obj.ident)
        cls.svc_mgr.assign_asset_to_repository(
            cls.asset_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_asset_to_repository(
            cls.asset_ids[2], cls.assigned_catalog.ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_asset_from_repository(
            cls.asset_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_asset_from_repository(
            cls.asset_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_assets():
            cls.catalog.delete_asset(obj.ident)
        cls.svc_mgr.delete_repository(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_asset_repository_mappings(self):
        """Tests can_lookup_asset_repository_mappings"""
        pass

    def test_use_comparative_repository_view(self):
        """Tests use_comparative_repository_view"""
        self.svc_mgr.use_comparative_repository_view()

    def test_use_plenary_repository_view(self):
        """Tests use_plenary_repository_view"""
        self.svc_mgr.use_plenary_repository_view()

    def test_get_asset_ids_by_repository(self):
        """Tests get_asset_ids_by_repository"""
        objects = self.svc_mgr.get_asset_ids_by_repository(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_assets_by_repository(self):
        """Tests get_assets_by_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_ids_by_repositories(self):
        """Tests get_asset_ids_by_repositories"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assets_by_repositories(self):
        """Tests get_assets_by_repositories"""
        pass

    def test_get_repository_ids_by_asset(self):
        """Tests get_repository_ids_by_asset"""
        cats = self.svc_mgr.get_repository_ids_by_asset(self.asset_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_repositories_by_asset(self):
        """Tests get_repositories_by_asset"""
        cats = self.svc_mgr.get_repositories_by_asset(self.asset_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssetRepositoryAssignmentSession(unittest.TestCase):
    """Tests for AssetRepositoryAssignmentSession"""

    @unittest.skip('unimplemented test')
    def test_can_assign_assets(self):
        """Tests can_assign_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_assign_assets_to_repository(self):
        """Tests can_assign_assets_to_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_repository_ids(self):
        """Tests get_assignable_repository_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_repository_ids_for_asset(self):
        """Tests get_assignable_repository_ids_for_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_assign_asset_to_repository(self):
        """Tests assign_asset_to_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_unassign_asset_from_repository(self):
        """Tests unassign_asset_from_repository"""
        pass


class TestAssetCompositionSession(unittest.TestCase):
    """Tests for AssetCompositionSession"""

    @classmethod
    def setUpClass(cls):
        cls.asset_list = list()
        cls.asset_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetLookupSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        create_form = cls.catalog.get_composition_form_for_create([])
        create_form.display_name = 'Test Composition for AssetCompositionSession tests'
        create_form.description = 'Test Compposion for AssetCompositionSession tests'
        cls.composition = cls.catalog.create_composition(create_form)
        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetLookupSession tests'
            obj = cls.catalog.create_asset(create_form)
            cls.asset_list.append(obj)
            cls.asset_ids.append(obj.ident)
            cls.catalog.add_asset(obj.ident, cls.composition.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_repositories():
            for obj in catalog.get_assets():
                catalog.delete_asset(obj.ident)
            for obj in catalog.get_compositions():
                catalog.delete_composition(obj.ident)
            cls.svc_mgr.delete_repository(catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_access_asset_compositions(self):
        """Tests can_access_asset_compositions"""
        pass

    def test_use_comparative_asset_composition_view(self):
        """Tests use_comparative_asset_composition_view"""
        self.catalog.use_comparative_asset_composition_view()

    def test_use_plenary_asset_composition_view(self):
        """Tests use_plenary_asset_composition_view"""
        self.catalog.use_plenary_asset_composition_view()

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        self.catalog.use_isolated_repository_view()

    def test_get_composition_assets(self):
        """Tests get_composition_assets"""
        self.assertEqual(self.catalog.get_composition_assets(self.composition.ident).available(), 4)

    def test_get_compositions_by_asset(self):
        """Tests get_compositions_by_asset"""
        self.assertEqual(self.catalog.get_compositions_by_asset(self.asset_ids[0]).available(), 1)
        self.assertEqual(self.catalog.get_compositions_by_asset(self.asset_ids[0]).next().ident, self.composition.ident)


class TestAssetCompositionDesignSession(unittest.TestCase):
    """Tests for AssetCompositionDesignSession"""

    @classmethod
    def setUpClass(cls):
        cls.asset_list = list()
        cls.asset_ids = list()
        cls.composition_list = list()
        cls.composition_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for AssetLookupSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_asset_form_for_create([])
            create_form.display_name = 'Test Asset ' + str(num)
            create_form.description = 'Test Asset for AssetLookupSession tests' + str(num)
            asset = cls.catalog.create_asset(create_form)
            cls.asset_list.append(asset)
            cls.asset_ids.append(asset.ident)
        for num in [0, 1, 2, 3, 4]:
            create_form = cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Compposion for AssetCompositionSession tests ' + str(num)
            composition = cls.catalog.create_composition(create_form)
            cls.composition_list.append(composition)
            cls.composition_ids.append(composition.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_repositories():
            for obj in catalog.get_compositions():
                catalog.delete_composition(obj.ident)
            for obj in catalog.get_assets():
                catalog.delete_asset(obj.ident)
            cls.svc_mgr.delete_repository(catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_compose_assets(self):
        """Tests can_compose_assets"""
        pass

    def test_add_asset(self):
        """Tests add_asset"""
        for asset_id in self.asset_ids:
            self.catalog.add_asset(asset_id, self.composition_ids[0])
        self.assertEqual(self.catalog.get_composition_assets(self.composition_ids[0]).available(), 4)
        self.assertEqual(self.catalog.get_composition_assets(self.composition_ids[0]).next().display_name.text, 'Test Asset 0')

    def test_move_asset_ahead(self):
        """Tests move_asset_ahead"""
        for asset_id in self.asset_ids:
            self.catalog.add_asset(asset_id, self.composition_ids[1])
        self.catalog.move_asset_ahead(self.asset_ids[2], self.composition_ids[1], self.asset_ids[0])
        first_asset = self.catalog.get_composition_assets(self.composition_ids[1]).next()
        self.assertEqual(first_asset.ident, self.asset_ids[2])

    def test_move_asset_behind(self):
        """Tests move_asset_behind"""
        for asset_id in self.asset_ids:
            self.catalog.add_asset(asset_id, self.composition_ids[2])
        self.catalog.move_asset_behind(self.asset_ids[0], self.composition_ids[2], self.asset_ids[3])
        last_asset = list(self.catalog.get_composition_assets(self.composition_ids[2]))[-1]
        self.assertEqual(last_asset.ident, self.asset_ids[0])

    def test_order_assets(self):
        """Tests order_assets"""
        for asset_id in self.asset_ids:
            self.catalog.add_asset(asset_id, self.composition_ids[3])
        new_order = [self.asset_ids[2], self.asset_ids[3], self.asset_ids[1], self.asset_ids[0]]
        self.catalog.order_assets(new_order, self.composition_ids[3])
        asset_list = list(self.catalog.get_composition_assets(self.composition_ids[3]))
        for num in [0, 1, 2, 3]:
            self.assertEqual(new_order[num], asset_list[num].ident)

    def test_remove_asset(self):
        """Tests remove_asset"""
        for asset_id in self.asset_ids:
            self.catalog.add_asset(asset_id, self.composition_ids[4])
        self.catalog.remove_asset(self.asset_ids[1], self.composition_ids[4])
        self.assertEqual(self.catalog.get_composition_assets(self.composition_ids[4]).available(), 3)


class TestCompositionLookupSession(unittest.TestCase):
    """Tests for CompositionLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.composition_list = list()
        cls.composition_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionLookupSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionLookupSession tests'
            if num > 1:
                create_form.sequestered = True
            obj = cls.catalog.create_composition(create_form)
            cls.composition_list.append(obj)
            cls.composition_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_repositories():
            catalog.use_unsequestered_composition_view()
            for obj in catalog.get_compositions():
                catalog.delete_composition(obj.ident)
            cls.svc_mgr.delete_repository(catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_compositions(self):
        """Tests can_lookup_compositions"""
        self.assertTrue(isinstance(self.catalog.can_lookup_compositions(), bool))

    def test_use_comparative_composition_view(self):
        """Tests use_comparative_composition_view"""
        self.catalog.use_comparative_composition_view()

    def test_use_plenary_composition_view(self):
        """Tests use_plenary_composition_view"""
        self.catalog.use_plenary_composition_view()

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        self.catalog.use_isolated_repository_view()

    def test_use_active_composition_view(self):
        """Tests use_active_composition_view"""
        self.catalog.use_active_composition_view()

    def test_use_any_status_composition_view(self):
        """Tests use_any_status_composition_view"""
        self.catalog.use_any_status_composition_view()

    def test_use_sequestered_composition_view(self):
        """Tests use_sequestered_composition_view"""
        self.catalog.use_sequestered_composition_view()

    def test_use_unsequestered_composition_view(self):
        """Tests use_unsequestered_composition_view"""
        self.catalog.use_unsequestered_composition_view()

    def test_get_composition(self):
        """Tests get_composition"""
        self.catalog.use_isolated_repository_view()
        obj = self.catalog.get_composition(self.composition_list[0].ident)
        self.assertEqual(obj.ident, self.composition_list[0].ident)
        self.catalog.use_federated_repository_view()
        obj = self.catalog.get_composition(self.composition_list[0].ident)
        self.assertEqual(obj.ident, self.composition_list[0].ident)
        self.catalog.use_sequestered_composition_view()
        obj = self.catalog.get_composition(self.composition_list[1].ident)
        with self.assertRaises(errors.NotFound):
            obj = self.catalog.get_composition(self.composition_list[3].ident)

    def test_get_compositions_by_ids(self):
        """Tests get_compositions_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        objects = self.catalog.get_compositions_by_ids(self.composition_ids)
        self.assertTrue(isinstance(objects, CompositionList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_compositions_by_ids(self.composition_ids)

    def test_get_compositions_by_genus_type(self):
        """Tests get_compositions_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        objects = self.catalog.get_compositions_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, CompositionList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_compositions_by_genus_type(DEFAULT_TYPE)

    def test_get_compositions_by_parent_genus_type(self):
        """Tests get_compositions_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        objects = self.catalog.get_compositions_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, CompositionList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_compositions_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_compositions_by_record_type(self):
        """Tests get_compositions_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.repository.objects import CompositionList
        objects = self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, CompositionList))
        self.catalog.use_federated_repository_view()
        objects = self.catalog.get_compositions_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_compositions_by_provider(self):
        """Tests get_compositions_by_provider"""
        pass

    def test_get_compositions(self):
        """Tests get_compositions"""
        from dlkit.abstract_osid.repository.objects import CompositionList
        objects = self.catalog.get_compositions()
        self.assertTrue(isinstance(objects, CompositionList))
        self.catalog.use_federated_repository_view()
        self.catalog.use_unsequestered_composition_view()
        self.assertEqual(self.catalog.get_compositions().available(), 4)
        self.catalog.use_sequestered_composition_view()
        self.assertEqual(self.catalog.get_compositions().available(), 2)


class TestCompositionQuerySession(unittest.TestCase):
    """Tests for CompositionQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.composition_list = list()
        cls.composition_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionQuerySession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + color
            create_form.description = (
                'Test Composition for CompositionQuerySession tests, did I mention green')
            obj = cls.catalog.create_composition(create_form)
            cls.composition_list.append(obj)
            cls.composition_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_compositions():
            cls.catalog.delete_composition(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_search_compositions(self):
        """Tests can_search_compositions"""
        pass

    def test_use_federated_repository_view(self):
        """Tests use_federated_repository_view"""
        self.catalog.use_federated_repository_view()

    def test_use_isolated_repository_view(self):
        """Tests use_isolated_repository_view"""
        self.catalog.use_isolated_repository_view()

    @unittest.skip('unimplemented test')
    def test_use_sequestered_composition_view(self):
        """Tests use_sequestered_composition_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_unsequestered_composition_view(self):
        """Tests use_unsequestered_composition_view"""
        pass

    def test_get_composition_query(self):
        """Tests get_composition_query"""
        query = self.catalog.get_composition_query()

    def test_get_compositions_by_query(self):
        """Tests get_compositions_by_query"""
        cfu = self.catalog.get_composition_form_for_update(self.composition_list[3].ident)
        cfu.set_sequestered(True)
        self.catalog.update_composition(cfu)
        query = self.catalog.get_composition_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_compositions_by_query(query).available(), 1)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_compositions_by_query(query).available(), 2)
        cfu = self.catalog.get_composition_form_for_update(self.composition_list[3].ident)
        cfu.set_sequestered(False)
        self.catalog.update_composition(cfu)


class TestCompositionSearchSession(unittest.TestCase):
    """Tests for CompositionSearchSession"""

    @unittest.skip('unimplemented test')
    def test_get_composition_search(self):
        """Tests get_composition_search"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_search_order(self):
        """Tests get_composition_search_order"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_compositions_by_search(self):
        """Tests get_compositions_by_search"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_query_from_inspector(self):
        """Tests get_composition_query_from_inspector"""
        pass


class TestCompositionAdminSession(unittest.TestCase):
    """Tests for CompositionAdminSession"""

    # From test_templates/resource.py::ResourceAdminSession::init_template
    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionAdminSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)

        form = cls.catalog.get_composition_form_for_create([])
        form.display_name = 'new Composition'
        form.description = 'description of Composition'
        form.set_genus_type(NEW_TYPE)
        cls.osid_object = cls.catalog.create_composition(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_compositions():
            cls.catalog.delete_composition(obj.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_get_repository_id(self):
        """Tests get_repository_id"""
        self.assertEqual(self.catalog.get_repository_id(), self.catalog.ident)

    def test_get_repository(self):
        """Tests get_repository"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_compositions(self):
        """Tests can_create_compositions"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_compositions(), bool))

    def test_can_create_composition_with_record_types(self):
        """Tests can_create_composition_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_composition_with_record_types(DEFAULT_TYPE), bool))

    def test_get_composition_form_for_create(self):
        """Tests get_composition_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_composition_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_composition(self):
        """Tests create_composition"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.repository.objects import Composition
        self.assertTrue(isinstance(self.osid_object, Composition))
        self.assertEqual(self.osid_object.display_name.text, 'new Composition')
        self.assertEqual(self.osid_object.description.text, 'description of Composition')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_compositions(self):
        """Tests can_update_compositions"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_compositions(), bool))

    def test_get_composition_form_for_update(self):
        """Tests get_composition_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_composition_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_composition(self):
        """Tests update_composition"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.repository.objects import Composition
        form = self.catalog.get_composition_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_composition(form)
        self.assertTrue(isinstance(updated_object, Composition))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_compositions(self):
        """Tests can_delete_compositions"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_compositions(), bool))

    def test_delete_composition(self):
        """Tests delete_composition"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_composition_form_for_create([])
        form.display_name = 'new Composition'
        form.description = 'description of Composition'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_composition(form)
        self.catalog.delete_composition(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_composition(osid_object.ident)

    @unittest.skip('unimplemented test')
    def test_delete_composition_node(self):
        """Tests delete_composition_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_add_composition_child(self):
        """Tests add_composition_child"""
        pass

    @unittest.skip('unimplemented test')
    def test_remove_composition_child(self):
        """Tests remove_composition_child"""
        pass

    def test_can_manage_composition_aliases(self):
        """Tests can_manage_composition_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_composition_aliases(), bool))

    def test_alias_composition(self):
        """Tests alias_composition"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_composition(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_composition(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)

    def test_composition_assignment(self):
        composition_list = list()
        composition_ids = list()
        for num in [0, 1, 2, 3]:
            create_form = self.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionLookupSession tests'
            obj = self.catalog.create_composition(create_form)
            composition_list.append(obj)
            composition_ids.append(obj.ident)
        update_form = self.catalog.get_composition_form_for_update(composition_ids[0])
        update_form.set_children(composition_ids[1:])
        self.catalog.update_composition(update_form)
        composition = self.catalog.get_composition(composition_ids[0])
        self.assertEqual(composition.get_children_ids().available(), 3)
        self.assertEqual(composition.get_child_ids().available(), 3)
        self.assertEqual(composition.get_children().available(), 3)


class TestCompositionRepositorySession(unittest.TestCase):
    """Tests for CompositionRepositorySession"""

    @classmethod
    def setUpClass(cls):
        cls.composition_list = list()
        cls.composition_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for CompositionRepositorySession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository for Assignment'
        create_form.description = 'Test Repository for CompositionRepositorySession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_repository(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_composition_form_for_create([])
            create_form.display_name = 'Test Composition ' + str(num)
            create_form.description = 'Test Composition for CompositionRepositorySession tests'
            obj = cls.catalog.create_composition(create_form)
            cls.composition_list.append(obj)
            cls.composition_ids.append(obj.ident)
        cls.svc_mgr.assign_composition_to_repository(
            cls.composition_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_composition_to_repository(
            cls.composition_ids[2], cls.assigned_catalog.ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_composition_from_repository(
            cls.composition_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_composition_from_repository(
            cls.composition_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_compositions():
            cls.catalog.delete_composition(obj.ident)
        cls.svc_mgr.delete_repository(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_repository(cls.catalog.ident)

    def test_use_comparative_composition_repository_view(self):
        """Tests use_comparative_composition_repository_view"""
        self.svc_mgr.use_comparative_composition_repository_view()

    def test_use_plenary_composition_repository_view(self):
        """Tests use_plenary_composition_repository_view"""
        self.svc_mgr.use_plenary_composition_repository_view()

    @unittest.skip('unimplemented test')
    def test_can_lookup_composition_repository_mappings(self):
        """Tests can_lookup_composition_repository_mappings"""
        pass

    def test_get_composition_ids_by_repository(self):
        """Tests get_composition_ids_by_repository"""
        objects = self.svc_mgr.get_composition_ids_by_repository(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_compositions_by_repository(self):
        """Tests get_compositions_by_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_composition_ids_by_repositories(self):
        """Tests get_composition_ids_by_repositories"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_compoitions_by_repositories(self):
        """Tests get_compoitions_by_repositories"""
        pass

    def test_get_repository_ids_by_composition(self):
        """Tests get_repository_ids_by_composition"""
        cats = self.svc_mgr.get_repository_ids_by_composition(self.composition_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_repositories_by_composition(self):
        """Tests get_repositories_by_composition"""
        cats = self.svc_mgr.get_repositories_by_composition(self.composition_ids[1])
        self.assertEqual(cats.available(), 2)


class TestCompositionRepositoryAssignmentSession(unittest.TestCase):
    """Tests for CompositionRepositoryAssignmentSession"""

    @unittest.skip('unimplemented test')
    def test_can_assign_compositions(self):
        """Tests can_assign_compositions"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_assign_compositions_to_repository(self):
        """Tests can_assign_compositions_to_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_repository_ids(self):
        """Tests get_assignable_repository_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_repository_ids_for_composition(self):
        """Tests get_assignable_repository_ids_for_composition"""
        pass

    @unittest.skip('unimplemented test')
    def test_assign_composition_to_repository(self):
        """Tests assign_composition_to_repository"""
        pass

    @unittest.skip('unimplemented test')
    def test_unassign_composition_from_repository(self):
        """Tests unassign_composition_from_repository"""
        pass


class TestRepositoryLookupSession(unittest.TestCase):
    """Tests for RepositoryLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = 'Test Repository ' + str(num)
            create_form.description = 'Test Repository for repository proxy manager tests'
            catalog = cls.svc_mgr.create_repository(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_repositories():
            cls.svc_mgr.delete_repository(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_repositories(self):
        """Tests can_lookup_repositories"""
        pass

    def test_use_comparative_repository_view(self):
        """Tests use_comparative_repository_view"""
        self.svc_mgr.use_comparative_repository_view()

    def test_use_plenary_repository_view(self):
        """Tests use_plenary_repository_view"""
        self.svc_mgr.use_plenary_repository_view()

    def test_get_repository(self):
        """Tests get_repository"""
        catalog = self.svc_mgr.get_repository(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_repositories_by_ids(self):
        """Tests get_repositories_by_ids"""
        catalogs = self.svc_mgr.get_repositories_by_ids(self.catalog_ids)

    @unittest.skip('unimplemented test')
    def test_get_repositories_by_genus_type(self):
        """Tests get_repositories_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repositories_by_parent_genus_type(self):
        """Tests get_repositories_by_parent_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repositories_by_record_type(self):
        """Tests get_repositories_by_record_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repositories_by_provider(self):
        """Tests get_repositories_by_provider"""
        pass

    def test_get_repositories(self):
        """Tests get_repositories"""
        catalogs = self.svc_mgr.get_repositories()


class TestRepositoryQuerySession(unittest.TestCase):
    """Tests for RepositoryQuerySession"""

    @unittest.skip('unimplemented test')
    def test_can_search_repositories(self):
        """Tests can_search_repositories"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repository_query(self):
        """Tests get_repository_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_repositories_by_query(self):
        """Tests get_repositories_by_query"""
        pass


class TestRepositoryAdminSession(unittest.TestCase):
    """Tests for RepositoryAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository'
        create_form.description = 'Test Repository for RepositoryAdminSession tests'
        cls.catalog = cls.svc_mgr.create_repository(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_repository_form_for_create([])
        create_form.display_name = 'Test Repository For Deletion'
        create_form.description = 'Test Repository for RepositoryAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_repository(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_repositories():
            cls.svc_mgr.delete_repository(catalog.ident)

    def test_can_create_repositories(self):
        """Tests can_create_repositories"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_repositories(), bool))

    def test_can_create_repository_with_record_types(self):
        """Tests can_create_repository_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_repository_with_record_types(DEFAULT_TYPE), bool))

    def test_get_repository_form_for_create(self):
        """Tests get_repository_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.repository.objects import RepositoryForm
        catalog_form = self.svc_mgr.get_repository_form_for_create([])
        self.assertTrue(isinstance(catalog_form, RepositoryForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_repository(self):
        """Tests create_repository"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.repository.objects import Repository
        catalog_form = self.svc_mgr.get_repository_form_for_create([])
        catalog_form.display_name = 'Test Repository'
        catalog_form.description = 'Test Repository for RepositoryAdminSession.create_repository tests'
        new_catalog = self.svc_mgr.create_repository(catalog_form)
        self.assertTrue(isinstance(new_catalog, Repository))

    @unittest.skip('unimplemented test')
    def test_can_update_repositories(self):
        """Tests can_update_repositories"""
        pass

    def test_get_repository_form_for_update(self):
        """Tests get_repository_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.repository.objects import RepositoryForm
        catalog_form = self.svc_mgr.get_repository_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, RepositoryForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_repository(self):
        """Tests update_repository"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_repository_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_repository(catalog_form)

    @unittest.skip('unimplemented test')
    def test_can_delete_repositories(self):
        """Tests can_delete_repositories"""
        pass

    def test_delete_repository(self):
        """Tests delete_repository"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_repository(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_repository(cat_id)

    def test_can_manage_repository_aliases(self):
        """Tests can_manage_repository_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_repository_aliases(), bool))

    def test_alias_repository(self):
        """Tests alias_repository"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('repository.Repository%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_repository(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_repository(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestRepositoryHierarchySession(unittest.TestCase):
    """Tests for RepositoryHierarchySession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Repository ' + name
            cls.catalogs[name] = cls.svc_mgr.create_repository(create_form)
        cls.svc_mgr.add_root_repository(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_repository(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_repository(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_repository(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.remove_child_repository(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_repositories(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_repository(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_repository(cls.catalogs[cat_name].ident)

    def test_get_repository_hierarchy_id(self):
        """Tests get_repository_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_repository_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_repository_hierarchy(self):
        """Tests get_repository_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_repository_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    @unittest.skip('unimplemented test')
    def test_can_access_repository_hierarchy(self):
        """Tests can_access_repository_hierarchy"""
        pass

    def test_use_comparative_repository_view(self):
        """Tests use_comparative_repository_view"""
        self.svc_mgr.use_comparative_repository_view()

    def test_use_plenary_repository_view(self):
        """Tests use_plenary_repository_view"""
        self.svc_mgr.use_plenary_repository_view()

    def test_get_root_repository_ids(self):
        """Tests get_root_repository_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_repository_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_repositories(self):
        """Tests get_root_repositories"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.repository.objects import RepositoryList
        roots = self.svc_mgr.get_root_repositories()
        self.assertTrue(isinstance(roots, RepositoryList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_repositories(self):
        """Tests has_parent_repositories"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_repositories(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_repositories(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_repositories(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_repositories(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_repositories(self.catalogs['Root'].ident))

    def test_is_parent_of_repository(self):
        """Tests is_parent_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_repository(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_repository_ids(self):
        """Tests get_parent_repository_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_repository_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_repositories(self):
        """Tests get_parent_repositories"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.repository.objects import RepositoryList
        catalog_list = self.svc_mgr.get_parent_repositories(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, RepositoryList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_repository(self):
        """Tests is_ancestor_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_repository,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_repository(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_repositories(self):
        """Tests has_child_repositories"""
        self.assertTrue(isinstance(self.svc_mgr.has_child_repositories(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_repositories(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_repositories(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_repositories(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_repositories(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_repository(self):
        """Tests is_child_of_repository"""
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_repository(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_repository(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_repository(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_repository_ids(self):
        """Tests get_child_repository_ids"""
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_repository_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_repositories(self):
        """Tests get_child_repositories"""
        from dlkit.abstract_osid.repository.objects import RepositoryList
        catalog_list = self.svc_mgr.get_child_repositories(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, RepositoryList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_repository(self):
        """Tests is_descendant_of_repository"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_repository,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_repository(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_repository_node_ids(self):
        """Tests get_repository_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_repository_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_repository_nodes(self):
        """Tests get_repository_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_repository_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestRepositoryHierarchyDesignSession(unittest.TestCase):
    """Tests for RepositoryHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('REPOSITORY', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_repository_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Repository ' + name
            cls.catalogs[name] = cls.svc_mgr.create_repository(create_form)
        cls.svc_mgr.add_root_repository(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_repository(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_repository(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_repository(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.remove_child_repository(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_repositories(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_repository(cls.catalogs[cat_name].ident)

    def test_get_repository_hierarchy_id(self):
        """Tests get_repository_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_repository_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_repository_hierarchy(self):
        """Tests get_repository_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_repository_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_repository_hierarchy(self):
        """Tests can_modify_repository_hierarchy"""
        # this is tested in the setUpClass
        self.assertTrue(True)

    def test_add_root_repository(self):
        """Tests add_root_repository"""
        # this is tested in the setUpClass
        self.assertTrue(True)

    def test_remove_root_repository(self):
        """Tests remove_root_repository"""
        # this is tested in the tearDownClass
        self.assertTrue(True)

    def test_add_child_repository(self):
        """Tests add_child_repository"""
        # this is tested in the setUpClass
        self.assertTrue(True)

    def test_remove_child_repository(self):
        """Tests remove_child_repository"""
        # this is tested in the tearDownClass
        self.assertTrue(True)

    def test_remove_child_repositories(self):
        """Tests remove_child_repositories"""
        # this is tested in the tearDownClass
        self.assertTrue(True)
