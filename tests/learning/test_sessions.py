"""Unit tests of learning sessions."""


import datetime
import unittest


from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.learning import objects as ABCObjects
from dlkit.abstract_osid.learning.objects import ObjectiveList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.json_.id.objects import IdList
from dlkit.primordium.calendaring.primitives import DateTime
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
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


class TestObjectiveLookupSession(unittest.TestCase):
    """Tests for ObjectiveLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.objective_list = list()
        cls.objective_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveLookupSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveLookupSession tests'
            obj = cls.catalog.create_objective(create_form)
            cls.objective_list.append(obj)
            cls.objective_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_objectives(self):
        """Tests can_lookup_objectives"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_objectives(), bool))

    def test_use_comparative_objective_view(self):
        """Tests use_comparative_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_objective_view()

    def test_use_plenary_objective_view(self):
        """Tests use_plenary_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_objective_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_objective(self):
        """Tests get_objective"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_objective_bank_view()
        obj = self.catalog.get_objective(self.objective_list[0].ident)
        self.assertEqual(obj.ident, self.objective_list[0].ident)
        self.catalog.use_federated_objective_bank_view()
        obj = self.catalog.get_objective(self.objective_list[0].ident)
        self.assertEqual(obj.ident, self.objective_list[0].ident)

    def test_get_objectives_by_ids(self):
        """Tests get_objectives_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_ids(self.objective_ids)
        self.assertTrue(isinstance(objects, ObjectiveList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_ids(self.objective_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ObjectiveList))

    def test_get_objectives_by_genus_type(self):
        """Tests get_objectives_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ObjectiveList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ObjectiveList))

    def test_get_objectives_by_parent_genus_type(self):
        """Tests get_objectives_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ObjectiveList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ObjectiveList))

    def test_get_objectives_by_record_type(self):
        """Tests get_objectives_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ObjectiveList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ObjectiveList))

    def test_get_objectives(self):
        """Tests get_objectives"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList
        objects = self.catalog.get_objectives()
        self.assertTrue(isinstance(objects, ObjectiveList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_objectives()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ObjectiveList))

    def test_get_objective_with_alias(self):
        self.catalog.alias_objective(self.objective_ids[0], ALIAS_ID)
        obj = self.catalog.get_objective(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.objective_ids[0])


class TestObjectiveQuerySession(unittest.TestCase):
    """Tests for ObjectiveQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        cls.objective_list = list()
        cls.objective_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveQuerySession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + color
            create_form.description = (
                'Test Objective for ObjectiveQuerySession tests, did I mention green')
            obj = cls.catalog.create_objective(create_form)
            cls.objective_list.append(obj)
            cls.objective_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_objectives(self):
        """Tests can_search_objectives"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_objectives(), bool))

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_objective_query(self):
        """Tests get_objective_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_objective_query()

    def test_get_objectives_by_query(self):
        """Tests get_objectives_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_objective_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_objectives_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_objectives_by_query(query).available(), 3)


class TestObjectiveAdminSession(unittest.TestCase):
    """Tests for ObjectiveAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveAdminSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        form = self.catalog.get_objective_form_for_create([])
        form.display_name = 'new Objective'
        form.description = 'description of Objective'
        form.set_genus_type(NEW_TYPE)
        self.osid_object = self.catalog.create_objective(form)
        self.session = self.catalog

    def tearDown(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        self.catalog.delete_objective(self.osid_object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_objectives(self):
        """Tests can_create_objectives"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_objectives(), bool))

    def test_can_create_objective_with_record_types(self):
        """Tests can_create_objective_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_objective_with_record_types(DEFAULT_TYPE), bool))

    def test_get_objective_form_for_create(self):
        """Tests get_objective_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_objective_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_objective(self):
        """Tests create_objective"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.learning.objects import Objective
        self.assertTrue(isinstance(self.osid_object, Objective))
        self.assertEqual(self.osid_object.display_name.text, 'new Objective')
        self.assertEqual(self.osid_object.description.text, 'description of Objective')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_objectives(self):
        """Tests can_update_objectives"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_objectives(), bool))

    def test_get_objective_form_for_update(self):
        """Tests get_objective_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_objective_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_objective(self):
        """Tests update_objective"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.learning.objects import Objective
        form = self.catalog.get_objective_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_objective(form)
        self.assertTrue(isinstance(updated_object, Objective))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_objectives(self):
        """Tests can_delete_objectives"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_objectives(), bool))

    def test_delete_objective(self):
        """Tests delete_objective"""
        # From test_templates/learning.py::ObjectiveAdminSession::delete_objective_template
        results = self.catalog.get_objectives()
        self.assertEqual(results.available(), 1)

        form = self.catalog.get_objective_form_for_create([])
        form.display_name = 'new Objective'
        form.description = 'description of Objective'
        new_objective = self.catalog.create_objective(form)

        results = self.catalog.get_objectives()
        self.assertEqual(results.available(), 2)

        self.session.delete_objective(new_objective.ident)

        results = self.catalog.get_objectives()
        self.assertEqual(results.available(), 1)
        self.assertNotEqual(str(results.next().ident),
                            str(new_objective.ident))

    def test_can_manage_objective_aliases(self):
        """Tests can_manage_objective_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_objective_aliases(), bool))

    def test_alias_objective(self):
        """Tests alias_objective"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_objective(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_objective(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestObjectiveHierarchySession(unittest.TestCase):
    """Tests for ObjectiveHierarchySession"""

    @classmethod
    def setUpClass(cls):
        cls.child_list = list()
        cls.child_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveHierarchySession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        self.child_list = list()
        self.child_ids = list()
        create_form = self.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveHierarchySession Lookup'
        create_form.description = 'Test Objective for ObjectiveHierarchySession tests'
        self.objective = self.catalog.create_objective(create_form)
        self.catalog.add_root_objective(self.objective.ident)
        for num in [0, 1]:
            create_form = self.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveHierarchySession tests'
            obj = self.catalog.create_objective(create_form)
            self.child_list.append(obj)
            self.child_ids.append(obj.ident)
            self.catalog.add_child_objective(self.objective.ident, obj.ident)
        self.session = self.catalog

    def tearDown(self):
        for obj_id in self.child_ids:
            self.catalog.delete_objective(obj_id)
        for obj in self.catalog.get_objectives():
            self.catalog.delete_objective(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_hierarchy_id(self):
        """Tests get_objective_hierarchy_id"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_hierarchy_id()

    def test_get_objective_hierarchy(self):
        """Tests get_objective_hierarchy"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_hierarchy()

    def test_can_access_objective_hierarchy(self):
        """Tests can_access_objective_hierarchy"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_access_objective_hierarchy()

    def test_use_comparative_objective_view(self):
        """Tests use_comparative_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_objective_view()

    def test_use_plenary_objective_view(self):
        """Tests use_plenary_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_objective_view()

    def test_get_root_objective_ids(self):
        """Tests get_root_objective_ids"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_root_objective_ids()

    def test_get_root_objectives(self):
        """Tests get_root_objectives"""
        roots = self.catalog.get_root_objectives()
        self.assertEqual(roots.available(), 1)
        self.assertTrue(isinstance(roots, ObjectiveList))
        self.assertEqual(str(roots.next().ident),
                         str(self.objective.ident))

    def test_has_parent_objectives(self):
        """Tests has_parent_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.has_parent_objectives(True)

    def test_is_parent_of_objective(self):
        """Tests is_parent_of_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.is_parent_of_objective(True, True)

    def test_get_parent_objective_ids(self):
        """Tests get_parent_objective_ids"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_parent_objective_ids(True)

    def test_get_parent_objectives(self):
        """Tests get_parent_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_parent_objectives(True)

    def test_is_ancestor_of_objective(self):
        """Tests is_ancestor_of_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.is_ancestor_of_objective(True, True)

    def test_has_child_objectives(self):
        """Tests has_child_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.has_child_objectives(True)

    def test_is_child_of_objective(self):
        """Tests is_child_of_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.is_child_of_objective(True, True)

    def test_get_child_objective_ids(self):
        """Tests get_child_objective_ids"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_child_objective_ids(True)

    def test_get_child_objectives(self):
        """Tests get_child_objectives"""
        children = self.catalog.get_child_objectives(self.objective.ident)
        self.assertEqual(children.available(), 2)
        self.assertTrue(isinstance(children, ObjectiveList))
        self.assertEqual(str(children.next().ident),
                         str(self.child_ids[0]))
        self.assertEqual(str(children.next().ident),
                         str(self.child_ids[1]))

    def test_is_descendant_of_objective(self):
        """Tests is_descendant_of_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.is_descendant_of_objective(True, True)

    def test_get_objective_node_ids(self):
        """Tests get_objective_node_ids"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_node_ids(True, True, True, True)

    def test_get_objective_nodes(self):
        """Tests get_objective_nodes"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_nodes(True, True, True, True)


class TestObjectiveHierarchyDesignSession(unittest.TestCase):
    """Tests for ObjectiveHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveHierarchyDesignSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        self.child_list = list()
        self.child_ids = list()
        create_form = self.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveHierarchyDesignSession Lookup'
        create_form.description = 'Test Objective for ObjectiveHierarchyDesignSession tests'
        self.objective = self.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = self.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveHierarchyDesignSession tests'
            obj = self.catalog.create_objective(create_form)
            self.child_list.append(obj)
            self.child_ids.append(obj.ident)
        self.session = self.catalog

    def tearDown(self):
        for obj_id in self.child_ids:
            self.catalog.delete_objective(obj_id)
        for obj in self.catalog.get_objectives():
            self.catalog.delete_objective(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_hierarchy_id(self):
        """Tests get_objective_hierarchy_id"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_hierarchy_id()

    def test_get_objective_hierarchy(self):
        """Tests get_objective_hierarchy"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_hierarchy()

    def test_can_modify_objective_hierarchy(self):
        """Tests can_modify_objective_hierarchy"""
        self.assertTrue(isinstance(self.catalog.can_modify_objective_hierarchy(), bool))

    def test_add_root_objective(self):
        """Tests add_root_objective"""
        roots = self.catalog.get_root_objectives()
        self.assertEqual(roots.available(), 0)
        self.assertTrue(isinstance(roots, ObjectiveList))

        self.catalog.add_root_objective(self.objective.ident)
        roots = self.catalog.get_root_objectives()
        self.assertEqual(roots.available(), 1)

    def test_remove_root_objective(self):
        """Tests remove_root_objective"""
        self.catalog.add_root_objective(self.objective.ident)

        roots = self.catalog.get_root_objectives()
        self.assertEqual(roots.available(), 1)

        self.catalog.remove_root_objective(self.objective.ident)

        roots = self.catalog.get_root_objectives()
        self.assertEqual(roots.available(), 0)

    def test_add_child_objective(self):
        """Tests add_child_objective"""
        self.catalog.add_root_objective(self.objective.ident)

        with self.assertRaises(errors.IllegalState):
            self.catalog.get_child_objectives(self.objective.ident)

        self.catalog.add_child_objective(self.objective.ident, self.child_ids[0])

        children = self.catalog.get_child_objectives(self.objective.ident)
        self.assertEqual(children.available(), 1)
        self.assertTrue(isinstance(children, ObjectiveList))

    def test_remove_child_objective(self):
        """Tests remove_child_objective"""
        self.catalog.add_root_objective(self.objective.ident)
        self.catalog.add_child_objective(self.objective.ident, self.child_ids[0])

        children = self.catalog.get_child_objectives(self.objective.ident)
        self.assertEqual(children.available(), 1)

        self.catalog.remove_child_objective(self.objective.ident, self.child_ids[0])

        with self.assertRaises(errors.IllegalState):
            self.catalog.get_child_objectives(self.objective.ident)

    def test_remove_child_objectives(self):
        """Tests remove_child_objectives"""
        self.catalog.add_root_objective(self.objective.ident)
        self.catalog.add_child_objective(self.objective.ident, self.child_ids[0])
        self.catalog.add_child_objective(self.objective.ident, self.child_ids[1])

        children = self.catalog.get_child_objectives(self.objective.ident)
        self.assertEqual(children.available(), 2)

        self.catalog.remove_child_objectives(self.objective.ident)

        with self.assertRaises(errors.IllegalState):
            self.catalog.get_child_objectives(self.objective.ident)


class TestObjectiveSequencingSession(unittest.TestCase):
    """Tests for ObjectiveSequencingSession"""

    @classmethod
    def setUpClass(cls):
        cls.child_list = list()
        cls.child_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveSequencingSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        self.objective_list = list()
        for num in [0, 1]:
            create_form = self.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveSequencingSession tests'
            obj = self.catalog.create_objective(create_form)
            self.objective_list.append(obj)

        self.session = self.catalog

    def tearDown(self):
        for obj_id in self.child_ids:
            self.catalog.delete_objective(obj_id)
        for obj in self.catalog.get_objectives():
            self.catalog.delete_objective(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_hierarchy_id(self):
        """Tests get_objective_hierarchy_id"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_hierarchy_id()

    def test_get_objective_hierarchy(self):
        """Tests get_objective_hierarchy"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_hierarchy()

    def test_can_sequence_objectives(self):
        """Tests can_sequence_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_sequence_objectives()

    def test_move_objective_ahead(self):
        """Tests move_objective_ahead"""
        with self.assertRaises(errors.Unimplemented):
            self.session.move_objective_ahead(True, True, True)

    def test_move_objective_behind(self):
        """Tests move_objective_behind"""
        with self.assertRaises(errors.Unimplemented):
            self.session.move_objective_behind(True, True, True)

    def test_sequence_objectives(self):
        """Tests sequence_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.sequence_objectives(True, True)


class TestObjectiveObjectiveBankSession(unittest.TestCase):
    """Tests for ObjectiveObjectiveBankSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinSession::init_template
        cls.objective_list = list()
        cls.objective_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveObjectiveBankSession tests'
            obj = cls.catalog.create_objective(create_form)
            cls.objective_list.append(obj)
            cls.objective_ids.append(obj.ident)
        cls.svc_mgr.assign_objective_to_objective_bank(
            cls.objective_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_objective_to_objective_bank(
            cls.objective_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinSession::init_template
        cls.svc_mgr.unassign_objective_from_objective_bank(
            cls.objective_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_objective_from_objective_bank(
            cls.objective_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_can_lookup_objective_objective_bank_mappings(self):
        """Tests can_lookup_objective_objective_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_objective_objective_bank_mappings()
        self.assertTrue(isinstance(result, bool))

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_objective_ids_by_objective_bank(self):
        """Tests get_objective_ids_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_objective_ids_by_objective_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_objectives_by_objective_bank(self):
        """Tests get_objectives_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_objectives_by_objective_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.ObjectiveList))
        self.assertEqual(results.available(), 2)

    def test_get_objective_ids_by_objective_banks(self):
        """Tests get_objective_ids_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_objective_ids_by_objective_banks(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_objectives_by_objective_banks(self):
        """Tests get_objectives_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_objectives_by_objective_banks(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.ObjectiveList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_objective_bank_ids_by_objective(self):
        """Tests get_objective_bank_ids_by_objective"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_objective_bank_ids_by_objective(self.objective_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_objective_banks_by_objective(self):
        """Tests get_objective_banks_by_objective"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_objective_banks_by_objective(self.objective_ids[1])
        self.assertEqual(cats.available(), 2)


class TestObjectiveObjectiveBankAssignmentSession(unittest.TestCase):
    """Tests for ObjectiveObjectiveBankAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        cls.objective_list = list()
        cls.objective_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ObjectiveObjectiveBankAssignmentSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveObjectiveBankAssignmentSession tests'
            obj = cls.catalog.create_objective(create_form)
            cls.objective_list.append(obj)
            cls.objective_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_can_assign_objectives(self):
        """Tests can_assign_objectives"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_objectives()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_objectives_to_objective_bank(self):
        """Tests can_assign_objectives_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_objectives_to_objective_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_objective_bank_ids(self):
        """Tests get_assignable_objective_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_objective_bank_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_objective_bank_ids_for_objective(self):
        """Tests get_assignable_objective_bank_ids_for_objective"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_objective_bank_ids_for_objective(self.catalog.ident, self.objective_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_objective_to_objective_bank(self):
        """Tests assign_objective_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_objectives()
        self.assertEqual(results.available(), 0)
        self.session.assign_objective_to_objective_bank(self.objective_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_objectives()
        self.assertEqual(results.available(), 1)
        self.session.unassign_objective_from_objective_bank(
            self.objective_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_objective_from_objective_bank(self):
        """Tests unassign_objective_from_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_objectives()
        self.assertEqual(results.available(), 0)
        self.session.assign_objective_to_objective_bank(
            self.objective_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_objectives()
        self.assertEqual(results.available(), 1)
        self.session.unassign_objective_from_objective_bank(
            self.objective_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_objectives()
        self.assertEqual(results.available(), 0)

    def test_reassign_proficiency_to_objective_bank(self):
        """Tests reassign_proficiency_to_objective_bank"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reassign_proficiency_to_objective_bank(True, True, True)


class TestObjectiveRequisiteSession(unittest.TestCase):
    """Tests for ObjectiveRequisiteSession"""

    @classmethod
    def setUpClass(cls):
        cls.requisite_list = list()
        cls.requisite_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveRequisiteSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveRequisiteSession Lookup'
        create_form.description = 'Test Objective for ObjectiveRequisiteSession tests'
        cls.objective = cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveRequisiteSession tests'
            obj = cls.catalog.create_objective(create_form)
            cls.requisite_list.append(obj)
            cls.requisite_ids.append(obj.ident)
            cls.catalog.assign_objective_requisite(cls.objective.ident, obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj_id in cls.requisite_ids:
                catalog.delete_objective(obj_id)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_objective_prerequisites(self):
        """Tests can_lookup_objective_prerequisites"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_lookup_objective_prerequisites()

    def test_use_comparative_objective_view(self):
        """Tests use_comparative_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_objective_view()

    def test_use_plenary_objective_view(self):
        """Tests use_plenary_objective_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_objective_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_requisite_objectives(self):
        """Tests get_requisite_objectives"""
        requisites = self.catalog.get_requisite_objectives(self.objective.ident)
        self.assertEqual(
            requisites.available(),
            len(self.requisite_ids)
        )
        for req in requisites:
            self.assertIn(
                req.ident,
                self.requisite_ids
            )

    def test_get_all_requisite_objectives(self):
        """Tests get_all_requisite_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_all_requisite_objectives(True)

    def test_get_dependent_objectives(self):
        """Tests get_dependent_objectives"""
        dependents = self.catalog.get_dependent_objectives(self.objective.ident)
        self.assertEqual(
            dependents.available(),
            0
        )
        dependents = self.catalog.get_dependent_objectives(self.requisite_ids[0])
        self.assertEqual(
            dependents.available(),
            1
        )
        self.assertEqual(
            dependents.next().ident,
            self.objective.ident
        )

    def test_is_objective_required(self):
        """Tests is_objective_required"""
        with self.assertRaises(errors.Unimplemented):
            self.session.is_objective_required(True, True)

    def test_get_equivalent_objectives(self):
        """Tests get_equivalent_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_equivalent_objectives(True)


class TestObjectiveRequisiteAssignmentSession(unittest.TestCase):
    """Tests for ObjectiveRequisiteAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.requisite_list = list()
        cls.requisite_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveRequisiteAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ObjectiveRequisiteAssignmentSession Lookup'
        create_form.description = 'Test Objective for ObjectiveRequisiteAssignmentSession tests'
        cls.objective = cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveRequisiteAssignmentSession tests'
            obj = cls.catalog.create_objective(create_form)
            cls.requisite_list.append(obj)
            cls.requisite_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj_id in cls.requisite_ids:
                catalog.delete_objective(obj_id)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_assign_requisites(self):
        """Tests can_assign_requisites"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_assign_requisites()

    def test_assign_objective_requisite(self):
        """Tests assign_objective_requisite"""
        results = self.catalog.get_requisite_objectives(self.objective.ident)
        self.assertTrue(isinstance(results, ObjectiveList))
        self.assertEqual(results.available(), 0)

        self.catalog.assign_objective_requisite(self.objective.ident, self.requisite_ids[0])

        results = self.catalog.get_requisite_objectives(self.objective.ident)
        self.assertEqual(results.available(), 1)

    def test_unassign_objective_requisite(self):
        """Tests unassign_objective_requisite"""
        self.catalog.assign_objective_requisite(self.objective.ident, self.requisite_ids[0])

        results = self.catalog.get_requisite_objectives(self.objective.ident)
        self.assertEqual(results.available(), 1)

        self.catalog.unassign_objective_requisite(self.objective.ident, self.requisite_ids[0])

        results = self.catalog.get_requisite_objectives(self.objective.ident)
        self.assertEqual(results.available(), 0)

    def test_assign_equivalent_objective(self):
        """Tests assign_equivalent_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.assign_equivalent_objective(True, True)

    def test_unassign_equivalent_objective(self):
        """Tests unassign_equivalent_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.unassign_equivalent_objective(True, True)


class TestActivityLookupSession(unittest.TestCase):
    """Tests for ActivityLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.activity_list = list()
        cls.activity_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityLookupSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityLookupSession tests'
        cls.objective = cls.catalog.create_objective(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityLookupSession tests'
            obj = cls.catalog.create_activity(create_form)
            cls.activity_list.append(obj)
            cls.activity_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_activities():
                catalog.delete_activity(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_activities(self):
        """Tests can_lookup_activities"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_activities(), bool))

    def test_use_comparative_activity_view(self):
        """Tests use_comparative_activity_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_activity_view()

    def test_use_plenary_activity_view(self):
        """Tests use_plenary_activity_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_activity_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_activity(self):
        """Tests get_activity"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_objective_bank_view()
        obj = self.catalog.get_activity(self.activity_list[0].ident)
        self.assertEqual(obj.ident, self.activity_list[0].ident)
        self.catalog.use_federated_objective_bank_view()
        obj = self.catalog.get_activity(self.activity_list[0].ident)
        self.assertEqual(obj.ident, self.activity_list[0].ident)

    def test_get_activities_by_ids(self):
        """Tests get_activities_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        objects = self.catalog.get_activities_by_ids(self.activity_ids)
        self.assertTrue(isinstance(objects, ActivityList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_activities_by_ids(self.activity_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ActivityList))

    def test_get_activities_by_genus_type(self):
        """Tests get_activities_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        objects = self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ActivityList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_activities_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ActivityList))

    def test_get_activities_by_parent_genus_type(self):
        """Tests get_activities_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        objects = self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ActivityList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_activities_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ActivityList))

    def test_get_activities_by_record_type(self):
        """Tests get_activities_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        objects = self.catalog.get_activities_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ActivityList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_activities_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ActivityList))

    def test_get_activities_for_objective(self):
        """Tests get_activities_for_objective"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        results = self.session.get_activities_for_objective(self.objective.ident)
        self.assertEqual(results.available(), 2)
        self.assertTrue(isinstance(results, ABCObjects.ActivityList))

    def test_get_activities_for_objectives(self):
        """Tests get_activities_for_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_activities_for_objectives(True)

    def test_get_activities_by_asset(self):
        """Tests get_activities_by_asset"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_activities_by_asset(True)

    def test_get_activities_by_assets(self):
        """Tests get_activities_by_assets"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_activities_by_assets(True)

    def test_get_activities(self):
        """Tests get_activities"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.learning.objects import ActivityList
        objects = self.catalog.get_activities()
        self.assertTrue(isinstance(objects, ActivityList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_activities()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ActivityList))

    def test_get_activity_with_alias(self):
        self.catalog.alias_activity(self.activity_ids[0], ALIAS_ID)
        obj = self.catalog.get_activity(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.activity_ids[0])


class TestActivityAdminSession(unittest.TestCase):
    """Tests for ActivityAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.activity_list = list()
        cls.activity_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityLookupSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityLookupSession tests'
        cls.objective = cls.catalog.create_objective(create_form)
        cls.parent_object = cls.objective
        for num in [0, 1]:
            create_form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityLookupSession tests'
            obj = cls.catalog.create_activity(create_form)
            cls.activity_list.append(obj)
            cls.activity_ids.append(obj.ident)

        create_form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])
        create_form.display_name = 'new Activity'
        create_form.description = 'description of Activity'
        create_form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_activity(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_activities():
                catalog.delete_activity(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_activities(self):
        """Tests can_create_activities"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_activities(), bool))

    def test_can_create_activity_with_record_types(self):
        """Tests can_create_activity_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_activity_with_record_types(DEFAULT_TYPE), bool))

    def test_get_activity_form_for_create(self):
        """Tests get_activity_form_for_create"""
        form = self.catalog.get_activity_form_for_create(self.parent_object.ident, [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_activity(self):
        """Tests create_activity"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.learning.objects import Activity
        self.assertTrue(isinstance(self.osid_object, Activity))
        self.assertEqual(self.osid_object.display_name.text, 'new Activity')
        self.assertEqual(self.osid_object.description.text, 'description of Activity')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_activities(self):
        """Tests can_update_activities"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_activities(), bool))

    def test_get_activity_form_for_update(self):
        """Tests get_activity_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_activity_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_activity(self):
        """Tests update_activity"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.learning.objects import Activity
        form = self.catalog.get_activity_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_activity(form)
        self.assertTrue(isinstance(updated_object, Activity))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_activities(self):
        """Tests can_delete_activities"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_activities(), bool))

    def test_delete_activity(self):
        """Tests delete_activity"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_activity_form_for_create([])
        form.display_name = 'new Activity'
        form.description = 'description of Activity'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_activity(form)
        self.catalog.delete_activity(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_activity(osid_object.ident)

    def test_can_manage_activity_aliases(self):
        """Tests can_manage_activity_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_activity_aliases(), bool))

    def test_alias_activity(self):
        """Tests alias_activity"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_activity(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_activity(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestActivityObjectiveBankSession(unittest.TestCase):
    """Tests for ActivityObjectiveBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.activity_list = list()
        cls.activity_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for ActivIty Lookup'
        create_form.description = 'Test Objective for ActivityLookupSession tests'
        cls.objective = cls.catalog.create_objective(create_form)

        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_objective_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityObjectiveBankSession tests'
            obj = cls.catalog.create_activity(create_form)
            cls.activity_list.append(obj)
            cls.activity_ids.append(obj.ident)
        cls.svc_mgr.assign_activity_to_objective_bank(
            cls.activity_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_activity_to_objective_bank(
            cls.activity_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_activity_from_objective_bank(
            cls.activity_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_activity_from_objective_bank(
            cls.activity_ids[2], cls.assigned_catalog.ident)
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_activities():
                catalog.delete_activity(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_can_lookup_activity_objective_bank_mappings(self):
        """Tests can_lookup_activity_objective_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_activity_objective_bank_mappings()
        self.assertTrue(isinstance(result, bool))

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_activity_ids_by_objective_bank(self):
        """Tests get_activity_ids_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_activity_ids_by_objective_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_activities_by_objective_bank(self):
        """Tests get_activities_by_objective_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_activities_by_objective_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.ActivityList))
        self.assertEqual(results.available(), 2)

    def test_get_activity_ids_by_objective_banks(self):
        """Tests get_activity_ids_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_activity_ids_by_objective_banks(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_activities_by_objective_banks(self):
        """Tests get_activities_by_objective_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_activities_by_objective_banks(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.ActivityList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_objective_bank_ids_by_activity(self):
        """Tests get_objective_bank_ids_by_activity"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_objective_bank_ids_by_activity(self.activity_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_objective_banks_by_activity(self):
        """Tests get_objective_banks_by_activity"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_objective_banks_by_activity(self.activity_ids[1])
        self.assertEqual(cats.available(), 2)


class TestActivityObjectiveBankAssignmentSession(unittest.TestCase):
    """Tests for ActivityObjectiveBankAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.activity_list = list()
        cls.activity_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank for Assignment'
        create_form.description = 'Test ObjectiveBank for ActivityObjectiveBankAssignmentSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_objective_bank(create_form)

        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Assignment'
        create_form.description = 'Test Objective for ActivityObjectiveBankAssignmentSession tests assignment'
        cls.objective = cls.catalog.create_objective(create_form)

        for num in [0, 1, 2]:
            create_form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])
            create_form.display_name = 'Test Activity ' + str(num)
            create_form.description = 'Test Activity for ActivityObjectiveBankAssignmentSession tests'
            obj = cls.catalog.create_activity(create_form)
            cls.activity_list.append(obj)
            cls.activity_ids.append(obj.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_activities():
            cls.catalog.delete_activity(obj.ident)
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_can_assign_activities(self):
        """Tests can_assign_activities"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_activities()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_activities_to_objective_bank(self):
        """Tests can_assign_activities_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_activities_to_objective_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_objective_bank_ids(self):
        """Tests get_assignable_objective_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_objective_bank_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_objective_bank_ids_for_activity(self):
        """Tests get_assignable_objective_bank_ids_for_activity"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_objective_bank_ids_for_activity(self.catalog.ident, self.activity_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_activity_to_objective_bank(self):
        """Tests assign_activity_to_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_activities()
        self.assertEqual(results.available(), 0)
        self.session.assign_activity_to_objective_bank(self.activity_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_activities()
        self.assertEqual(results.available(), 1)
        self.session.unassign_activity_from_objective_bank(
            self.activity_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_activity_from_objective_bank(self):
        """Tests unassign_activity_from_objective_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_activities()
        self.assertEqual(results.available(), 0)
        self.session.assign_activity_to_objective_bank(
            self.activity_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_activities()
        self.assertEqual(results.available(), 1)
        self.session.unassign_activity_from_objective_bank(
            self.activity_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_activities()
        self.assertEqual(results.available(), 0)

    def test_reassign_activity_to_objective_bank(self):
        """Tests reassign_activity_to_objective_bank"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reassign_activity_to_objective_bank(True, True, True)


class TestProficiencyLookupSession(unittest.TestCase):
    """Tests for ProficiencyLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.proficiency_list = list()
        cls.proficiency_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyLookupSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        objective = cls.catalog.create_objective(form)

        for color in ['Orange', 'Blue']:
            create_form = cls.catalog.get_proficiency_form_for_create(objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + color
            create_form.description = (
                'Test Proficiency for ProficiencyLookupSession tests, did I mention green')
            obj = cls.catalog.create_proficiency(create_form)
            cls.proficiency_list.append(obj)
            cls.proficiency_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_proficiencies():
                catalog.delete_proficiency(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_proficiencies(self):
        """Tests can_lookup_proficiencies"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_proficiencies(), bool))

    def test_use_comparative_proficiency_view(self):
        """Tests use_comparative_proficiency_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_proficiency_view()

    def test_use_plenary_proficiency_view(self):
        """Tests use_plenary_proficiency_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_proficiency_view()

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_use_effective_proficiency_view(self):
        """Tests use_effective_proficiency_view"""
        with self.assertRaises(errors.Unimplemented):
            self.session.use_effective_proficiency_view()

    def test_use_any_effective_proficiency_view(self):
        """Tests use_any_effective_proficiency_view"""
        with self.assertRaises(errors.Unimplemented):
            self.session.use_any_effective_proficiency_view()

    def test_get_proficiency(self):
        """Tests get_proficiency"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_objective_bank_view()
        obj = self.catalog.get_proficiency(self.proficiency_list[0].ident)
        self.assertEqual(obj.ident, self.proficiency_list[0].ident)
        self.catalog.use_federated_objective_bank_view()
        obj = self.catalog.get_proficiency(self.proficiency_list[0].ident)
        self.assertEqual(obj.ident, self.proficiency_list[0].ident)

    def test_get_proficiencies_by_ids(self):
        """Tests get_proficiencies_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        objects = self.catalog.get_proficiencies_by_ids(self.proficiency_ids)
        self.assertTrue(isinstance(objects, ProficiencyList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_proficiencies_by_ids(self.proficiency_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ProficiencyList))

    def test_get_proficiencies_by_genus_type(self):
        """Tests get_proficiencies_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        objects = self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ProficiencyList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_proficiencies_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ProficiencyList))

    def test_get_proficiencies_by_parent_genus_type(self):
        """Tests get_proficiencies_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        objects = self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ProficiencyList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_proficiencies_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ProficiencyList))

    def test_get_proficiencies_by_record_type(self):
        """Tests get_proficiencies_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        objects = self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ProficiencyList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_proficiencies_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ProficiencyList))

    def test_get_proficiencies_on_date(self):
        """Tests get_proficiencies_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_on_date(True, True)

    def test_get_proficiencies_by_genus_type_on_date(self):
        """Tests get_proficiencies_by_genus_type_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_by_genus_type_on_date(True, True, True)

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_for_objective(self):
        """Tests get_proficiencies_for_objective"""
        pass

    def test_get_proficiencies_for_objective_on_date(self):
        """Tests get_proficiencies_for_objective_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_for_objective_on_date(True, True, True)

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_by_genus_type_for_objective(self):
        """Tests get_proficiencies_by_genus_type_for_objective"""
        pass

    def test_get_proficiencies_by_genus_type_for_objective_on_date(self):
        """Tests get_proficiencies_by_genus_type_for_objective_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_by_genus_type_for_objective_on_date(True, True, True, True)

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_for_objectives(self):
        """Tests get_proficiencies_for_objectives"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_for_resource(self):
        """Tests get_proficiencies_for_resource"""
        pass

    def test_get_proficiencies_for_resource_on_date(self):
        """Tests get_proficiencies_for_resource_on_date"""
        # From test_templates/relationship.py::RelationshipLookupSession::get_relationships_for_source_on_date_template
        end_date = DateTime.utcnow() + datetime.timedelta(days=5)
        end_date = DateTime(**{
            'year': end_date.year,
            'month': end_date.month,
            'day': end_date.day,
            'hour': end_date.hour,
            'minute': end_date.minute,
            'second': end_date.second,
            'microsecond': end_date.microsecond
        })

        # NOTE: this first argument will probably break in many of the other methods,
        #   since it's not clear they always use something like AGENT_ID
        # i.e. in get_grade_entries_for_gradebook_column_on_date it needs to be
        #   a gradebookColumnId.
        results = self.session.get_proficiencies_for_resource_on_date(AGENT_ID, DateTime.utcnow(), end_date)
        self.assertTrue(isinstance(results, ABCObjects.ProficiencyList))
        self.assertEqual(results.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_by_genus_type_for_resource(self):
        """Tests get_proficiencies_by_genus_type_for_resource"""
        pass

    def test_get_proficiencies_by_genus_type_for_resource_on_date(self):
        """Tests get_proficiencies_by_genus_type_for_resource_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_by_genus_type_for_resource_on_date(True, True, True, True)

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_for_resources(self):
        """Tests get_proficiencies_for_resources"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_for_objective_and_resource(self):
        """Tests get_proficiencies_for_objective_and_resource"""
        pass

    def test_get_proficiencies_for_objective_and_resource_on_date(self):
        """Tests get_proficiencies_for_objective_and_resource_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_for_objective_and_resource_on_date(True, True, True, True)

    @unittest.skip('unimplemented test')
    def test_get_proficiencies_by_genus_type_for_objective_and_resource(self):
        """Tests get_proficiencies_by_genus_type_for_objective_and_resource"""
        pass

    def test_get_proficiencies_by_genus_type_for_objective_and_resource_on_date(self):
        """Tests get_proficiencies_by_genus_type_for_objective_and_resource_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_proficiencies_by_genus_type_for_objective_and_resource_on_date(True, True, True, True, True)

    def test_get_proficiencies(self):
        """Tests get_proficiencies"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList
        objects = self.catalog.get_proficiencies()
        self.assertTrue(isinstance(objects, ProficiencyList))
        self.catalog.use_federated_objective_bank_view()
        objects = self.catalog.get_proficiencies()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ProficiencyList))

    def test_get_proficiency_with_alias(self):
        self.catalog.alias_proficiency(self.proficiency_ids[0], ALIAS_ID)
        obj = self.catalog.get_proficiency(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.proficiency_ids[0])


class TestProficiencyQuerySession(unittest.TestCase):
    """Tests for ProficiencyQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.proficiency_list = list()
        cls.proficiency_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyQuerySession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        objective = cls.catalog.create_objective(form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_proficiency_form_for_create(objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + color
            create_form.description = (
                'Test Proficiency for ProficiencyQuerySession tests, did I mention green')
            obj = cls.catalog.create_proficiency(create_form)
            cls.proficiency_list.append(obj)
            cls.proficiency_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_proficiencies():
                catalog.delete_proficiency(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_proficiencies(self):
        """Tests can_search_proficiencies"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_proficiencies(), bool))

    def test_use_federated_objective_bank_view(self):
        """Tests use_federated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_objective_bank_view()

    def test_use_isolated_objective_bank_view(self):
        """Tests use_isolated_objective_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_objective_bank_view()

    def test_get_proficiency_query(self):
        """Tests get_proficiency_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_proficiency_query()

    def test_get_proficiencies_by_query(self):
        """Tests get_proficiencies_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_proficiency_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_proficiencies_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_proficiencies_by_query(query).available(), 3)


class TestProficiencyAdminSession(unittest.TestCase):
    """Tests for ProficiencyAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.proficiency_list = list()
        cls.proficiency_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyLookupSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        cls.objective = cls.catalog.create_objective(form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_proficiency_form_for_create(cls.objective.ident, AGENT_ID, [])
            create_form.display_name = 'Test Proficiency ' + color
            create_form.description = (
                'Test Proficiency for ProficiencyLookupSession tests, did I mention green')
            obj = cls.catalog.create_proficiency(create_form)
            cls.proficiency_list.append(obj)
            cls.proficiency_ids.append(obj.ident)

        create_form = cls.catalog.get_proficiency_form_for_create(cls.objective.ident, AGENT_ID, [])
        create_form.display_name = 'new Proficiency'
        create_form.description = 'description of Proficiency'
        create_form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_proficiency(create_form)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_proficiencies():
                catalog.delete_proficiency(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_objective_bank_id(self):
        """Tests get_objective_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_objective_bank_id(), self.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_proficiencies(self):
        """Tests can_create_proficiencies"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_proficiencies(), bool))

    def test_can_create_proficiency_with_record_types(self):
        """Tests can_create_proficiency_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_proficiency_with_record_types(DEFAULT_TYPE), bool))

    def test_get_proficiency_form_for_create(self):
        """Tests get_proficiency_form_for_create"""
        form = self.catalog.get_proficiency_form_for_create(self.objective.ident, AGENT_ID, [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_proficiency(self):
        """Tests create_proficiency"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.learning.objects import Proficiency
        self.assertTrue(isinstance(self.osid_object, Proficiency))
        self.assertEqual(self.osid_object.display_name.text, 'new Proficiency')
        self.assertEqual(self.osid_object.description.text, 'description of Proficiency')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_proficiencies(self):
        """Tests can_update_proficiencies"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_proficiencies(), bool))

    def test_get_proficiency_form_for_update(self):
        """Tests get_proficiency_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_proficiency_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_proficiency(self):
        """Tests update_proficiency"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.learning.objects import Proficiency
        form = self.catalog.get_proficiency_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_proficiency(form)
        self.assertTrue(isinstance(updated_object, Proficiency))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_proficiencies(self):
        """Tests can_delete_proficiencies"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_proficiencies(), bool))

    def test_delete_proficiency(self):
        """Tests delete_proficiency"""
        create_form = self.catalog.get_proficiency_form_for_create(self.objective.ident, AGENT_ID, [])
        create_form.display_name = 'new Proficiency'
        create_form.description = 'description of Proficiency'
        create_form.genus_type = NEW_TYPE
        osid_object = self.catalog.create_proficiency(create_form)
        self.catalog.delete_proficiency(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_proficiency(osid_object.ident)

    def test_delete_proficiencies(self):
        """Tests delete_proficiencies"""
        with self.assertRaises(errors.Unimplemented):
            self.session.delete_proficiencies()

    def test_can_manage_proficiency_aliases(self):
        """Tests can_manage_proficiency_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_proficiency_aliases(), bool))

    def test_alias_proficiency(self):
        """Tests alias_proficiency"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_proficiency(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_proficiency(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestObjectiveBankLookupSession(unittest.TestCase):
    """Tests for ObjectiveBankLookupSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for learning proxy manager tests'
            catalog = cls.svc_mgr.create_objective_bank(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::BinLookupSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        for catalog in cls.svc_mgr.get_objective_banks():
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_can_lookup_objective_banks(self):
        """Tests can_lookup_objective_banks"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_lookup_objective_banks(), bool))

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        catalog = self.svc_mgr.get_objective_bank(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_objective_banks_by_ids(self):
        """Tests get_objective_banks_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        catalogs = self.svc_mgr.get_objective_banks_by_ids(self.catalog_ids)
        self.assertTrue(catalogs.available() == 2)
        self.assertTrue(isinstance(catalogs, ABCObjects.ObjectiveBankList))
        reversed_catalog_ids = [str(cat_id) for cat_id in self.catalog_ids][::-1]
        for index, catalog in enumerate(catalogs):
            self.assertEqual(str(catalog.ident),
                             reversed_catalog_ids[index])

    def test_get_objective_banks_by_genus_type(self):
        """Tests get_objective_banks_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        catalogs = self.svc_mgr.get_objective_banks_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.ObjectiveBankList))

    def test_get_objective_banks_by_parent_genus_type(self):
        """Tests get_objective_banks_by_parent_genus_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_banks_by_parent_genus_type(True)

    def test_get_objective_banks_by_record_type(self):
        """Tests get_objective_banks_by_record_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_banks_by_record_type(True)

    def test_get_objective_banks_by_provider(self):
        """Tests get_objective_banks_by_provider"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_objective_banks_by_provider(True)

    def test_get_objective_banks(self):
        """Tests get_objective_banks"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        catalogs = self.svc_mgr.get_objective_banks()
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.ObjectiveBankList))


class TestObjectiveBankAdminSession(unittest.TestCase):
    """Tests for ObjectiveBankAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankAdminSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank For Deletion'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::BinAdminSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        for catalog in cls.svc_mgr.get_objective_banks():
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_can_create_objective_banks(self):
        """Tests can_create_objective_banks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_objective_banks(), bool))

    def test_can_create_objective_bank_with_record_types(self):
        """Tests can_create_objective_bank_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_objective_bank_with_record_types(DEFAULT_TYPE), bool))

    def test_get_objective_bank_form_for_create(self):
        """Tests get_objective_bank_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankForm
        catalog_form = self.svc_mgr.get_objective_bank_form_for_create([])
        self.assertTrue(isinstance(catalog_form, ObjectiveBankForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_objective_bank(self):
        """Tests create_objective_bank"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBank
        catalog_form = self.svc_mgr.get_objective_bank_form_for_create([])
        catalog_form.display_name = 'Test ObjectiveBank'
        catalog_form.description = 'Test ObjectiveBank for ObjectiveBankAdminSession.create_objective_bank tests'
        new_catalog = self.svc_mgr.create_objective_bank(catalog_form)
        self.assertTrue(isinstance(new_catalog, ObjectiveBank))

    def test_can_update_objective_banks(self):
        """Tests can_update_objective_banks"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_update_objective_banks(), bool))

    def test_get_objective_bank_form_for_update(self):
        """Tests get_objective_bank_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankForm
        catalog_form = self.svc_mgr.get_objective_bank_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, ObjectiveBankForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_objective_bank(self):
        """Tests update_objective_bank"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_objective_bank_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_objective_bank(catalog_form)

    def test_can_delete_objective_banks(self):
        """Tests can_delete_objective_banks"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_delete_objective_banks(), bool))

    def test_delete_objective_bank(self):
        """Tests delete_objective_bank"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_objective_bank(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_objective_bank(cat_id)

    def test_can_manage_objective_bank_aliases(self):
        """Tests can_manage_objective_bank_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_objective_bank_aliases(), bool))

    def test_alias_objective_bank(self):
        """Tests alias_objective_bank"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('learning.ObjectiveBank%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_objective_bank(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_objective_bank(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestObjectiveBankHierarchySession(unittest.TestCase):
    """Tests for ObjectiveBankHierarchySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test ObjectiveBank ' + name
            cls.catalogs[name] = cls.svc_mgr.create_objective_bank(create_form)
        cls.svc_mgr.add_root_objective_bank(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_objective_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_objective_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_objective_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr.remove_child_objective_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_objective_banks(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_objective_bank(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_objective_bank(cls.catalogs[cat_name].ident)

    def test_get_objective_bank_hierarchy_id(self):
        """Tests get_objective_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_objective_bank_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_objective_bank_hierarchy(self):
        """Tests get_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_objective_bank_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_access_objective_bank_hierarchy(self):
        """Tests can_access_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        self.assertTrue(isinstance(self.svc_mgr.can_access_objective_bank_hierarchy(), bool))

    def test_use_comparative_objective_bank_view(self):
        """Tests use_comparative_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_objective_bank_view()

    def test_use_plenary_objective_bank_view(self):
        """Tests use_plenary_objective_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_objective_bank_view()

    def test_get_root_objective_bank_ids(self):
        """Tests get_root_objective_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_objective_bank_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_objective_banks(self):
        """Tests get_root_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankList
        roots = self.svc_mgr.get_root_objective_banks()
        self.assertTrue(isinstance(roots, ObjectiveBankList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_objective_banks(self):
        """Tests has_parent_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_objective_banks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_objective_banks(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_objective_banks(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_objective_banks(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_objective_banks(self.catalogs['Root'].ident))

    def test_is_parent_of_objective_bank(self):
        """Tests is_parent_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_objective_bank_ids(self):
        """Tests get_parent_objective_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_objective_bank_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_objective_banks(self):
        """Tests get_parent_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankList
        catalog_list = self.svc_mgr.get_parent_objective_banks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, ObjectiveBankList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_objective_bank(self):
        """Tests is_ancestor_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_objective_bank,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_objective_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_objective_banks(self):
        """Tests has_child_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_child_objective_banks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_objective_banks(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_objective_banks(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_objective_banks(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_objective_banks(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_objective_bank(self):
        """Tests is_child_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_objective_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_objective_bank(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_objective_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_objective_bank_ids(self):
        """Tests get_child_objective_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_objective_bank_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_objective_banks(self):
        """Tests get_child_objective_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankList
        catalog_list = self.svc_mgr.get_child_objective_banks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, ObjectiveBankList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_objective_bank(self):
        """Tests is_descendant_of_objective_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_objective_bank,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_objective_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_objective_bank_node_ids(self):
        """Tests get_objective_bank_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_objective_bank_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_objective_bank_nodes(self):
        """Tests get_objective_bank_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_objective_bank_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestObjectiveBankHierarchyDesignSession(unittest.TestCase):
    """Tests for ObjectiveBankHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test ObjectiveBank ' + name
            cls.catalogs[name] = cls.svc_mgr.create_objective_bank(create_form)
        cls.svc_mgr.add_root_objective_bank(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_objective_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_objective_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_objective_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr.remove_child_objective_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_objective_banks(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_objective_bank(cls.catalogs[cat_name].ident)

    def test_get_objective_bank_hierarchy_id(self):
        """Tests get_objective_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_objective_bank_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_objective_bank_hierarchy(self):
        """Tests get_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_objective_bank_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_objective_bank_hierarchy(self):
        """Tests can_modify_objective_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        self.assertTrue(isinstance(self.session.can_modify_objective_bank_hierarchy(), bool))

    def test_add_root_objective_bank(self):
        """Tests add_root_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        roots = self.session.get_root_objective_banks()
        self.assertTrue(isinstance(roots, ABCObjects.ObjectiveBankList))
        self.assertEqual(roots.available(), 1)

    def test_remove_root_objective_bank(self):
        """Tests remove_root_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        roots = self.session.get_root_objective_banks()
        self.assertEqual(roots.available(), 1)

        create_form = self.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'new root'
        create_form.description = 'Test ObjectiveBank root'
        new_objective_bank = self.svc_mgr.create_objective_bank(create_form)
        self.svc_mgr.add_root_objective_bank(new_objective_bank.ident)

        roots = self.session.get_root_objective_banks()
        self.assertEqual(roots.available(), 2)

        self.session.remove_root_objective_bank(new_objective_bank.ident)

        roots = self.session.get_root_objective_banks()
        self.assertEqual(roots.available(), 1)

    def test_add_child_objective_bank(self):
        """Tests add_child_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        # this is tested in the setUpClass
        children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
        self.assertTrue(isinstance(children, ABCObjects.ObjectiveBankList))
        self.assertEqual(children.available(), 2)

    def test_remove_child_objective_bank(self):
        """Tests remove_child_objective_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

        create_form = self.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'test child'
        create_form.description = 'Test ObjectiveBank child'
        new_objective_bank = self.svc_mgr.create_objective_bank(create_form)
        self.svc_mgr.add_child_objective_bank(
            self.catalogs['Root'].ident,
            new_objective_bank.ident)

        children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 3)

        self.session.remove_child_objective_bank(
            self.catalogs['Root'].ident,
            new_objective_bank.ident)

        children = self.session.get_child_objective_banks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

    def test_remove_child_objective_banks(self):
        """Tests remove_child_objective_banks"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        children = self.session.get_child_objective_banks(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)

        create_form = self.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'test great grandchild'
        create_form.description = 'Test ObjectiveBank child'
        new_objective_bank = self.svc_mgr.create_objective_bank(create_form)
        self.svc_mgr.add_child_objective_bank(
            self.catalogs['Grandchild 1'].ident,
            new_objective_bank.ident)

        children = self.session.get_child_objective_banks(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 1)

        self.session.remove_child_objective_banks(self.catalogs['Grandchild 1'].ident)

        children = self.session.get_child_objective_banks(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)
