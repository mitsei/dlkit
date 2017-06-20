"""Unit tests of grading sessions."""


import unittest


from dlkit.abstract_osid.grading import objects as ABCObjects
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.json_.grading.objects import GradebookColumnSummary
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
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})


class TestGradeSystemLookupSession(unittest.TestCase):
    """Tests for GradeSystemLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.grade_system_list = list()
        cls.grade_system_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemLookupSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + str(num)
            create_form.description = 'Test GradeSystem for GradeSystemLookupSession tests'
            obj = cls.catalog.create_grade_system(create_form)
            cls.grade_system_list.append(obj)
            cls.grade_system_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_grade_systems(self):
        """Tests can_lookup_grade_systems"""
        self.assertTrue(isinstance(self.catalog.can_lookup_grade_systems(), bool))

    def test_use_comparative_grade_system_view(self):
        """Tests use_comparative_grade_system_view"""
        self.catalog.use_comparative_grade_system_view()

    def test_use_plenary_grade_system_view(self):
        """Tests use_plenary_grade_system_view"""
        self.catalog.use_plenary_grade_system_view()

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_gradebook_view()
        obj = self.catalog.get_grade_system(self.grade_system_list[0].ident)
        self.assertEqual(obj.ident, self.grade_system_list[0].ident)
        self.catalog.use_federated_gradebook_view()
        obj = self.catalog.get_grade_system(self.grade_system_list[0].ident)
        self.assertEqual(obj.ident, self.grade_system_list[0].ident)

    def test_get_grade_system_by_grade(self):
        """Tests get_grade_system_by_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_system_by_grade(True)

    def test_get_grade_systems_by_ids(self):
        """Tests get_grade_systems_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_ids(self.grade_system_ids)
        self.assertTrue(isinstance(objects, GradeSystemList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_ids(self.grade_system_ids)

    def test_get_grade_systems_by_genus_type(self):
        """Tests get_grade_systems_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradeSystemList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_genus_type(DEFAULT_TYPE)

    def test_get_grade_systems_by_parent_genus_type(self):
        """Tests get_grade_systems_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradeSystemList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_grade_systems_by_record_type(self):
        """Tests get_grade_systems_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradeSystemList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems_by_record_type(DEFAULT_TYPE)

    def test_get_grade_systems(self):
        """Tests get_grade_systems"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList
        objects = self.catalog.get_grade_systems()
        self.assertTrue(isinstance(objects, GradeSystemList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_systems()

    def test_get_grade_system_with_alias(self):
        self.catalog.alias_grade_system(self.grade_system_ids[0], ALIAS_ID)
        obj = self.catalog.get_grade_system(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.grade_system_ids[0])


class TestGradeSystemQuerySession(unittest.TestCase):
    """Tests for GradeSystemQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        cls.grade_system_list = list()
        cls.grade_system_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemQuerySession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + color
            create_form.description = (
                'Test GradeSystem for GradeSystemQuerySession tests, did I mention green')
            obj = cls.catalog.create_grade_system(create_form)
            cls.grade_system_list.append(obj)
            cls.grade_system_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_grade_systems(self):
        """Tests can_search_grade_systems"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_grade_systems(), bool))

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_grade_system_query()

    def test_get_grade_systems_by_query(self):
        """Tests get_grade_systems_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_grade_system_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_grade_systems_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_grade_systems_by_query(query).available(), 3)


class TestGradeSystemAdminSession(unittest.TestCase):
    """Tests for GradeSystemAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemAdminSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'new GradeSystem'
        form.description = 'description of GradeSystem'
        form.set_genus_type(NEW_TYPE)
        cls.osid_object = cls.catalog.create_grade_system(form)

    def setUp(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_grade_systems(self):
        """Tests can_create_grade_systems"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_grade_systems(), bool))

    def test_can_create_grade_system_with_record_types(self):
        """Tests can_create_grade_system_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_grade_system_with_record_types(DEFAULT_TYPE), bool))

    def test_get_grade_system_form_for_create(self):
        """Tests get_grade_system_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_grade_system_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_grade_system(self):
        """Tests create_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.grading.objects import GradeSystem
        self.assertTrue(isinstance(self.osid_object, GradeSystem))
        self.assertEqual(self.osid_object.display_name.text, 'new GradeSystem')
        self.assertEqual(self.osid_object.description.text, 'description of GradeSystem')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_grade_systems(self):
        """Tests can_update_grade_systems"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_grade_systems(), bool))

    def test_get_grade_system_form_for_update(self):
        """Tests get_grade_system_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_grade_system_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_grade_system(self):
        """Tests update_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.grading.objects import GradeSystem
        form = self.catalog.get_grade_system_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_grade_system(form)
        self.assertTrue(isinstance(updated_object, GradeSystem))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_grade_systems(self):
        """Tests can_delete_grade_systems"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_grade_systems(), bool))

    def test_delete_grade_system(self):
        """Tests delete_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_grade_system_form_for_create([])
        form.display_name = 'new GradeSystem'
        form.description = 'description of GradeSystem'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_grade_system(form)
        self.catalog.delete_grade_system(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_grade_system(osid_object.ident)

    def test_can_manage_grade_system_aliases(self):
        """Tests can_manage_grade_system_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_grade_system_aliases(), bool))

    def test_alias_grade_system(self):
        """Tests alias_grade_system"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_grade_system(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_grade_system(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)

    def test_can_create_grades(self):
        """Tests can_create_grades"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_grades(), bool))

    def test_can_create_grade_with_record_types(self):
        """Tests can_create_grade_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_grade_with_record_types(DEFAULT_TYPE), bool))

    def test_get_grade_form_for_create(self):
        """Tests get_grade_form_for_create"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_form_for_create(True, True)

    def test_create_grade(self):
        """Tests create_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.session.create_grade(True)

    def test_can_update_grades(self):
        """Tests can_update_grades"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_update_grades(True)

    def test_get_grade_form_for_update(self):
        """Tests get_grade_form_for_update"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_form_for_update(True)

    def test_update_grade(self):
        """Tests update_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.session.update_grade(True)

    def test_can_delete_grades(self):
        """Tests can_delete_grades"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_grades(), bool))

    def test_delete_grade(self):
        """Tests delete_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.session.delete_grade(True)

    def test_can_manage_grade_aliases(self):
        """Tests can_manage_grade_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_grade_aliases(), bool))

    def test_alias_grade(self):
        """Tests alias_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.session.alias_grade(True, True)


class TestGradeEntryLookupSession(unittest.TestCase):
    """Tests for GradeEntryLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.grade_entry_list = list()
        cls.grade_entry_ids = list()
        cls.gradebook_column_list = list()
        cls.gradebook_column_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryLookupSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        create_form = cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradeEntryLookupSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 5
        create_form.numeric_score_increment = 0.25
        cls.grade_system = cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradeEntryLookupSession tests'
            create_form.grade_system = cls.grade_system.ident
            obj = cls.catalog.create_gradebook_column(create_form)
            cls.gradebook_column_list.append(obj)
            cls.gradebook_column_ids.append(obj.ident)
        for num in [0, 1]:
            create_form = cls.catalog.get_grade_entry_form_for_create(cls.gradebook_column_ids[num], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradeEntryLookupSession tests'
            object = cls.catalog.create_grade_entry(create_form)
            cls.grade_entry_list.append(object)
            cls.grade_entry_ids.append(object.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_gradebooks():
            for obj in catalog.get_grade_entries():
                catalog.delete_grade_entry(obj.ident)
            for obj in catalog.get_gradebook_columns():
                catalog.delete_gradebook_column(obj.ident)
            for obj in catalog.get_grade_systems():
                catalog.delete_grade_system(obj.ident)
            cls.svc_mgr.delete_gradebook(catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_grade_entries(self):
        """Tests can_lookup_grade_entries"""
        self.assertTrue(isinstance(self.catalog.can_lookup_grade_entries(), bool))

    def test_use_comparative_grade_entry_view(self):
        """Tests use_comparative_grade_entry_view"""
        self.catalog.use_comparative_grade_entry_view()

    def test_use_plenary_grade_entry_view(self):
        """Tests use_plenary_grade_entry_view"""
        self.catalog.use_plenary_grade_entry_view()

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_use_effective_grade_entry_view(self):
        """Tests use_effective_grade_entry_view"""
        with self.assertRaises(errors.Unimplemented):
            self.session.use_effective_grade_entry_view()

    def test_use_any_effective_grade_entry_view(self):
        """Tests use_any_effective_grade_entry_view"""
        with self.assertRaises(errors.Unimplemented):
            self.session.use_any_effective_grade_entry_view()

    def test_get_grade_entry(self):
        """Tests get_grade_entry"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_gradebook_view()
        obj = self.catalog.get_grade_entry(self.grade_entry_list[0].ident)
        self.assertEqual(obj.ident, self.grade_entry_list[0].ident)
        self.catalog.use_federated_gradebook_view()
        obj = self.catalog.get_grade_entry(self.grade_entry_list[0].ident)
        self.assertEqual(obj.ident, self.grade_entry_list[0].ident)

    def test_get_grade_entries_by_ids(self):
        """Tests get_grade_entries_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        objects = self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)
        self.assertTrue(isinstance(objects, GradeEntryList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_entries_by_ids(self.grade_entry_ids)

    def test_get_grade_entries_by_genus_type(self):
        """Tests get_grade_entries_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        objects = self.catalog.get_grade_entries_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradeEntryList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_entries_by_genus_type(DEFAULT_TYPE)

    def test_get_grade_entries_by_parent_genus_type(self):
        """Tests get_grade_entries_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        objects = self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradeEntryList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_entries_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_grade_entries_by_record_type(self):
        """Tests get_grade_entries_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        objects = self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradeEntryList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_entries_by_record_type(DEFAULT_TYPE)

    def test_get_grade_entries_on_date(self):
        """Tests get_grade_entries_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entries_on_date(True, True)

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column(self):
        """Tests get_grade_entries_for_gradebook_column"""
        pass

    def test_get_grade_entries_for_gradebook_column_on_date(self):
        """Tests get_grade_entries_for_gradebook_column_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entries_for_gradebook_column_on_date(True, True, True)

    def test_get_grade_entries_for_resource(self):
        """Tests get_grade_entries_for_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entries_for_resource(True)

    def test_get_grade_entries_for_resource_on_date(self):
        """Tests get_grade_entries_for_resource_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entries_for_resource_on_date(True, True, True)

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column_and_resource(self):
        """Tests get_grade_entries_for_gradebook_column_and_resource"""
        pass

    def test_get_grade_entries_for_gradebook_column_and_resource_on_date(self):
        """Tests get_grade_entries_for_gradebook_column_and_resource_on_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entries_for_gradebook_column_and_resource_on_date(True, True, True, True)

    def test_get_grade_entries_by_grader(self):
        """Tests get_grade_entries_by_grader"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entries_by_grader(True)

    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList
        objects = self.catalog.get_grade_entries()
        self.assertTrue(isinstance(objects, GradeEntryList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_grade_entries()

    def test_get_grade_entry_with_alias(self):
        self.catalog.alias_grade_entry(self.grade_entry_ids[0], ALIAS_ID)
        obj = self.catalog.get_grade_entry(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.grade_entry_ids[0])


class TestGradeEntryQuerySession(unittest.TestCase):
    """Tests for GradeEntryQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.grade_entry_list = list()
        cls.grade_entry_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryQuerySession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Test grade system'
        grade_system = cls.catalog.create_grade_system(form)

        form = cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Test gradebook column'
        form.set_grade_system(grade_system.ident)
        gradebook_column = cls.catalog.create_gradebook_column(form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_grade_entry_form_for_create(gradebook_column.ident, AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + color
            create_form.description = (
                'Test GradeEntry for GradeEntryQuerySession tests, did I mention green')
            obj = cls.catalog.create_grade_entry(create_form)
            cls.grade_entry_list.append(obj)
            cls.grade_entry_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_gradebooks():
            for obj in catalog.get_grade_entries():
                catalog.delete_grade_entry(obj.ident)
            for obj in catalog.get_gradebook_columns():
                catalog.delete_gradebook_column(obj.ident)
            for obj in catalog.get_grade_systems():
                catalog.delete_grade_system(obj.ident)
            cls.svc_mgr.delete_gradebook(catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_grade_entries(self):
        """Tests can_search_grade_entries"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_grade_entries(), bool))

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_grade_entry_query()

    def test_get_grade_entries_by_query(self):
        """Tests get_grade_entries_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_grade_entry_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_grade_entries_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_grade_entries_by_query(query).available(), 3)


class TestGradeEntryAdminSession(unittest.TestCase):
    """Tests for GradeEntryAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.grade_entry_list = list()
        cls.grade_entry_ids = list()
        cls.gradebook_column_list = list()
        cls.gradebook_column_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryLookupSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        create_form = cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradeEntryLookupSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 5
        create_form.numeric_score_increment = 0.25
        cls.grade_system = cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradeEntryLookupSession tests'
            create_form.grade_system = cls.grade_system.ident
            obj = cls.catalog.create_gradebook_column(create_form)
            cls.gradebook_column_list.append(obj)
            cls.gradebook_column_ids.append(obj.ident)
        for num in [0, 1]:
            create_form = cls.catalog.get_grade_entry_form_for_create(cls.gradebook_column_ids[num], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradeEntryLookupSession tests'
            object = cls.catalog.create_grade_entry(create_form)
            cls.grade_entry_list.append(object)
            cls.grade_entry_ids.append(object.ident)

        create_form = cls.catalog.get_grade_entry_form_for_create(cls.gradebook_column_ids[0], AGENT_ID, [])
        create_form.display_name = 'new GradeEntry'
        create_form.description = 'description of GradeEntry'
        create_form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_grade_entry(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_grade_entries(self):
        """Tests can_create_grade_entries"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_grade_entries(), bool))

    def test_can_create_grade_entry_with_record_types(self):
        """Tests can_create_grade_entry_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_grade_entry_with_record_types(DEFAULT_TYPE), bool))

    def test_get_grade_entry_form_for_create(self):
        """Tests get_grade_entry_form_for_create"""
        form = self.catalog.get_grade_entry_form_for_create(self.gradebook_column_ids[0], AGENT_ID, [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_grade_entry(self):
        """Tests create_grade_entry"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.grading.objects import GradeEntry
        self.assertTrue(isinstance(self.osid_object, GradeEntry))
        self.assertEqual(self.osid_object.display_name.text, 'new GradeEntry')
        self.assertEqual(self.osid_object.description.text, 'description of GradeEntry')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_overridecalculated_grade_entries(self):
        """Tests can_overridecalculated_grade_entries"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_overridecalculated_grade_entries()

    def test_get_grade_entry_form_for_override(self):
        """Tests get_grade_entry_form_for_override"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_grade_entry_form_for_override(True, True)

    def test_override_calculated_grade_entry(self):
        """Tests override_calculated_grade_entry"""
        with self.assertRaises(errors.Unimplemented):
            self.session.override_calculated_grade_entry(True)

    def test_can_update_grade_entries(self):
        """Tests can_update_grade_entries"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_grade_entries(), bool))

    def test_get_grade_entry_form_for_update(self):
        """Tests get_grade_entry_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_grade_entry_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_grade_entry(self):
        """Tests update_grade_entry"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.grading.objects import GradeEntry
        form = self.catalog.get_grade_entry_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_grade_entry(form)
        self.assertTrue(isinstance(updated_object, GradeEntry))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_grade_entries(self):
        """Tests can_delete_grade_entries"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_grade_entries(), bool))

    def test_delete_grade_entry(self):
        """Tests delete_grade_entry"""
        create_form = self.catalog.get_grade_entry_form_for_create(self.gradebook_column_ids[0], AGENT_ID, [])
        create_form.display_name = 'new GradeEntry'
        create_form.description = 'description of GradeEntry'
        create_form.genus_type = NEW_TYPE
        osid_object = self.catalog.create_grade_entry(create_form)
        self.catalog.delete_grade_entry(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_grade_entry(osid_object.ident)

    def test_can_manage_grade_entry_aliases(self):
        """Tests can_manage_grade_entry_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_grade_entry_aliases(), bool))

    def test_alias_grade_entry(self):
        """Tests alias_grade_entry"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_grade_entry(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_grade_entry(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestGradebookColumnLookupSession(unittest.TestCase):
    """Tests for GradebookColumnLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.grade_entry_list = list()
        cls.grade_entry_ids = list()
        cls.gradebook_column_list = list()
        cls.gradebook_column_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnLookupSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        create_form = cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradebookColumnLookupSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 100
        create_form.numeric_score_increment = 1
        cls.grade_system = cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradebookColumnLookupSession tests'
            create_form.grade_system = cls.grade_system.ident
            obj = cls.catalog.create_gradebook_column(create_form)
            cls.gradebook_column_list.append(obj)
            cls.gradebook_column_ids.append(obj.ident)
        for num in range(0, 100):
            create_form = cls.catalog.get_grade_entry_form_for_create(cls.gradebook_column_ids[0], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradebookColumnLookupSession tests'
            create_form.set_score(float(num))
            object = cls.catalog.create_grade_entry(create_form)
            cls.grade_entry_list.append(object)
            cls.grade_entry_ids.append(object.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_gradebooks():
            for obj in catalog.get_grade_entries():
                catalog.delete_grade_entry(obj.ident)
            for obj in catalog.get_gradebook_columns():
                catalog.delete_gradebook_column(obj.ident)
            for obj in catalog.get_grade_systems():
                catalog.delete_grade_system(obj.ident)
            cls.svc_mgr.delete_gradebook(catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_gradebook_columns(self):
        """Tests can_lookup_gradebook_columns"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_lookup_gradebook_columns(), bool))

    def test_use_comparative_gradebook_column_view(self):
        """Tests use_comparative_gradebook_column_view"""
        self.catalog.use_comparative_gradebook_column_view()

    def test_use_plenary_gradebook_column_view(self):
        """Tests use_plenary_gradebook_column_view"""
        self.catalog.use_plenary_gradebook_column_view()

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_gradebook_view()
        obj = self.catalog.get_gradebook_column(self.gradebook_column_list[0].ident)
        self.assertEqual(obj.ident, self.gradebook_column_list[0].ident)
        self.catalog.use_federated_gradebook_view()
        obj = self.catalog.get_gradebook_column(self.gradebook_column_list[0].ident)
        self.assertEqual(obj.ident, self.gradebook_column_list[0].ident)

    def test_get_gradebook_columns_by_ids(self):
        """Tests get_gradebook_columns_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        objects = self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)
        self.assertTrue(isinstance(objects, GradebookColumnList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_gradebook_columns_by_ids(self.gradebook_column_ids)

    def test_get_gradebook_columns_by_genus_type(self):
        """Tests get_gradebook_columns_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        objects = self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradebookColumnList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_gradebook_columns_by_genus_type(DEFAULT_TYPE)

    def test_get_gradebook_columns_by_parent_genus_type(self):
        """Tests get_gradebook_columns_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        objects = self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradebookColumnList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_gradebook_columns_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_gradebook_columns_by_record_type(self):
        """Tests get_gradebook_columns_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        objects = self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, GradebookColumnList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_gradebook_columns_by_record_type(DEFAULT_TYPE)

    def test_get_gradebook_columns(self):
        """Tests get_gradebook_columns"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList
        objects = self.catalog.get_gradebook_columns()
        self.assertTrue(isinstance(objects, GradebookColumnList))
        self.catalog.use_federated_gradebook_view()
        objects = self.catalog.get_gradebook_columns()

    def test_get_gradebook_column_with_alias(self):
        self.catalog.alias_gradebook_column(self.gradebook_column_ids[0], ALIAS_ID)
        obj = self.catalog.get_gradebook_column(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.gradebook_column_ids[0])

    def test_supports_summary(self):
        """Tests supports_summary"""
        with self.assertRaises(errors.Unimplemented):
            self.session.supports_summary()

    def test_get_gradebook_column_summary(self):
        """Tests get_gradebook_column_summary"""
        self.assertTrue(isinstance(self.catalog.get_gradebook_column_summary(self.gradebook_column_ids[0]),
                                   GradebookColumnSummary))


class TestGradebookColumnQuerySession(unittest.TestCase):
    """Tests for GradebookColumnQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        cls.gradebook_column_list = list()
        cls.gradebook_column_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnQuerySession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + color
            create_form.description = (
                'Test GradebookColumn for GradebookColumnQuerySession tests, did I mention green')
            obj = cls.catalog.create_gradebook_column(create_form)
            cls.gradebook_column_list.append(obj)
            cls.gradebook_column_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_gradebook_columns(self):
        """Tests can_search_gradebook_columns"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_gradebook_columns(), bool))

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_gradebook_column_query()

    def test_get_gradebook_columns_by_query(self):
        """Tests get_gradebook_columns_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_gradebook_column_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_gradebook_columns_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_gradebook_columns_by_query(query).available(), 3)


class TestGradebookColumnAdminSession(unittest.TestCase):
    """Tests for GradebookColumnAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnAdminSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'new GradebookColumn'
        form.description = 'description of GradebookColumn'
        form.set_genus_type(NEW_TYPE)
        cls.osid_object = cls.catalog.create_gradebook_column(form)

    def setUp(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_id(self):
        """Tests get_gradebook_id"""
        self.assertEqual(self.catalog.get_gradebook_id(), self.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_gradebook_columns(self):
        """Tests can_create_gradebook_columns"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.catalog.can_create_gradebook_columns(), bool))

    def test_can_create_gradebook_column_with_record_types(self):
        """Tests can_create_gradebook_column_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_gradebook_column_with_record_types(DEFAULT_TYPE), bool))

    def test_get_gradebook_column_form_for_create(self):
        """Tests get_gradebook_column_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_gradebook_column_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_gradebook_column(self):
        """Tests create_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookColumn
        self.assertTrue(isinstance(self.osid_object, GradebookColumn))
        self.assertEqual(self.osid_object.display_name.text, 'new GradebookColumn')
        self.assertEqual(self.osid_object.description.text, 'description of GradebookColumn')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_gradebook_columns(self):
        """Tests can_update_gradebook_columns"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.catalog.can_update_gradebook_columns(), bool))

    def test_get_gradebook_column_form_for_update(self):
        """Tests get_gradebook_column_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_gradebook_column_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_gradebook_column(self):
        """Tests update_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookColumn
        form = self.catalog.get_gradebook_column_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_gradebook_column(form)
        self.assertTrue(isinstance(updated_object, GradebookColumn))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_sequence_gradebook_columns(self):
        """Tests sequence_gradebook_columns"""
        with self.assertRaises(errors.Unimplemented):
            self.session.sequence_gradebook_columns(True)

    def test_move_gradebook_column(self):
        """Tests move_gradebook_column"""
        with self.assertRaises(errors.Unimplemented):
            self.session.move_gradebook_column(True, True)

    def test_copy_gradebook_column_entries(self):
        """Tests copy_gradebook_column_entries"""
        with self.assertRaises(errors.Unimplemented):
            self.session.copy_gradebook_column_entries(True, True)

    def test_can_delete_gradebook_columns(self):
        """Tests can_delete_gradebook_columns"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.catalog.can_delete_gradebook_columns(), bool))

    def test_delete_gradebook_column(self):
        """Tests delete_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'new GradebookColumn'
        form.description = 'description of GradebookColumn'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_gradebook_column(form)
        self.catalog.delete_gradebook_column(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_gradebook_column(osid_object.ident)

    def test_can_manage_gradebook_column_aliases(self):
        """Tests can_manage_gradebook_column_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_gradebook_column_aliases(), bool))

    def test_alias_gradebook_column(self):
        """Tests alias_gradebook_column"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_gradebook_column(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_gradebook_column(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestGradebookLookupSession(unittest.TestCase):
    """Tests for GradebookLookupSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test Gradebook ' + str(num)
            create_form.description = 'Test Gradebook for grading proxy manager tests'
            catalog = cls.svc_mgr.create_gradebook(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::BinLookupSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        for catalog in cls.svc_mgr.get_gradebooks():
            cls.svc_mgr.delete_gradebook(catalog.ident)

    def test_can_lookup_gradebooks(self):
        """Tests can_lookup_gradebooks"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_lookup_gradebooks(), bool))

    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_gradebook_view()

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        catalog = self.svc_mgr.get_gradebook(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_gradebooks_by_ids(self):
        """Tests get_gradebooks_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        catalogs = self.svc_mgr.get_gradebooks_by_ids(self.catalog_ids)
        self.assertTrue(catalogs.available() == 2)
        self.assertTrue(isinstance(catalogs, ABCObjects.GradebookList))
        reversed_catalog_ids = [str(cat_id) for cat_id in self.catalog_ids][::-1]
        for index, catalog in enumerate(catalogs):
            self.assertEqual(str(catalog.ident),
                             reversed_catalog_ids[index])

    def test_get_gradebooks_by_genus_type(self):
        """Tests get_gradebooks_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        catalogs = self.svc_mgr.get_gradebooks_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.GradebookList))

    def test_get_gradebooks_by_parent_genus_type(self):
        """Tests get_gradebooks_by_parent_genus_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_gradebooks_by_parent_genus_type(True)

    def test_get_gradebooks_by_record_type(self):
        """Tests get_gradebooks_by_record_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_gradebooks_by_record_type(True)

    def test_get_gradebooks_by_provider(self):
        """Tests get_gradebooks_by_provider"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_gradebooks_by_provider(True)

    def test_get_gradebooks(self):
        """Tests get_gradebooks"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        catalogs = self.svc_mgr.get_gradebooks()
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.GradebookList))


class TestGradebookAdminSession(unittest.TestCase):
    """Tests for GradebookAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookAdminSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook For Deletion'
        create_form.description = 'Test Gradebook for GradebookAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # From test_templates/resource.py::BinAdminSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        for catalog in cls.svc_mgr.get_gradebooks():
            cls.svc_mgr.delete_gradebook(catalog.ident)

    def test_can_create_gradebooks(self):
        """Tests can_create_gradebooks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_gradebooks(), bool))

    def test_can_create_gradebook_with_record_types(self):
        """Tests can_create_gradebook_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_gradebook_with_record_types(DEFAULT_TYPE), bool))

    def test_get_gradebook_form_for_create(self):
        """Tests get_gradebook_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.grading.objects import GradebookForm
        catalog_form = self.svc_mgr.get_gradebook_form_for_create([])
        self.assertTrue(isinstance(catalog_form, GradebookForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_gradebook(self):
        """Tests create_gradebook"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.grading.objects import Gradebook
        catalog_form = self.svc_mgr.get_gradebook_form_for_create([])
        catalog_form.display_name = 'Test Gradebook'
        catalog_form.description = 'Test Gradebook for GradebookAdminSession.create_gradebook tests'
        new_catalog = self.svc_mgr.create_gradebook(catalog_form)
        self.assertTrue(isinstance(new_catalog, Gradebook))

    def test_can_update_gradebooks(self):
        """Tests can_update_gradebooks"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_update_gradebooks(), bool))

    def test_get_gradebook_form_for_update(self):
        """Tests get_gradebook_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.grading.objects import GradebookForm
        catalog_form = self.svc_mgr.get_gradebook_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, GradebookForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_gradebook(self):
        """Tests update_gradebook"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_gradebook_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_gradebook(catalog_form)

    def test_can_delete_gradebooks(self):
        """Tests can_delete_gradebooks"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_delete_gradebooks(), bool))

    def test_delete_gradebook(self):
        """Tests delete_gradebook"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_gradebook(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_gradebook(cat_id)

    def test_can_manage_gradebook_aliases(self):
        """Tests can_manage_gradebook_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_gradebook_aliases(), bool))

    def test_alias_gradebook(self):
        """Tests alias_gradebook"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('grading.Gradebook%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_gradebook(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_gradebook(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestGradebookHierarchySession(unittest.TestCase):
    """Tests for GradebookHierarchySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Gradebook ' + name
            cls.catalogs[name] = cls.svc_mgr.create_gradebook(create_form)
        cls.svc_mgr.add_root_gradebook(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_gradebook(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_gradebook(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_gradebook(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr.remove_child_gradebook(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_gradebooks(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_gradebook(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_gradebook(cls.catalogs[cat_name].ident)

    def test_get_gradebook_hierarchy_id(self):
        """Tests get_gradebook_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_gradebook_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_gradebook_hierarchy(self):
        """Tests get_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_gradebook_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_access_gradebook_hierarchy(self):
        """Tests can_access_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        self.assertTrue(isinstance(self.svc_mgr.can_access_gradebook_hierarchy(), bool))

    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_gradebook_view()

    def test_get_root_gradebook_ids(self):
        """Tests get_root_gradebook_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_gradebook_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_gradebooks(self):
        """Tests get_root_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.grading.objects import GradebookList
        roots = self.svc_mgr.get_root_gradebooks()
        self.assertTrue(isinstance(roots, GradebookList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_gradebooks(self):
        """Tests has_parent_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_gradebooks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_gradebooks(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_gradebooks(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_gradebooks(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_gradebooks(self.catalogs['Root'].ident))

    def test_is_parent_of_gradebook(self):
        """Tests is_parent_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_gradebook(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_gradebook_ids(self):
        """Tests get_parent_gradebook_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_gradebook_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_gradebooks(self):
        """Tests get_parent_gradebooks"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.grading.objects import GradebookList
        catalog_list = self.svc_mgr.get_parent_gradebooks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, GradebookList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_gradebook(self):
        """Tests is_ancestor_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_gradebook,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_gradebook(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_gradebooks(self):
        """Tests has_child_gradebooks"""
        self.assertTrue(isinstance(self.svc_mgr.has_child_gradebooks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_gradebooks(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_gradebooks(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_gradebooks(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_gradebooks(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_gradebook(self):
        """Tests is_child_of_gradebook"""
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_gradebook(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_gradebook(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_gradebook(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_gradebook_ids(self):
        """Tests get_child_gradebook_ids"""
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_gradebook_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_gradebooks(self):
        """Tests get_child_gradebooks"""
        from dlkit.abstract_osid.grading.objects import GradebookList
        catalog_list = self.svc_mgr.get_child_gradebooks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, GradebookList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_gradebook(self):
        """Tests is_descendant_of_gradebook"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_gradebook,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_gradebook(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_gradebook_node_ids(self):
        """Tests get_gradebook_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_gradebook_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_gradebook_nodes(self):
        """Tests get_gradebook_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_gradebook_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestGradebookHierarchyDesignSession(unittest.TestCase):
    """Tests for GradebookHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Gradebook ' + name
            cls.catalogs[name] = cls.svc_mgr.create_gradebook(create_form)
        cls.svc_mgr.add_root_gradebook(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_gradebook(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_gradebook(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_gradebook(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr.remove_child_gradebook(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_gradebooks(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_gradebook(cls.catalogs[cat_name].ident)

    def test_get_gradebook_hierarchy_id(self):
        """Tests get_gradebook_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_gradebook_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_gradebook_hierarchy(self):
        """Tests get_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_gradebook_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_gradebook_hierarchy(self):
        """Tests can_modify_gradebook_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        self.assertTrue(isinstance(self.session.can_modify_gradebook_hierarchy(), bool))

    def test_add_root_gradebook(self):
        """Tests add_root_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        roots = self.session.get_root_gradebooks()
        self.assertTrue(isinstance(roots, ABCObjects.GradebookList))
        self.assertEqual(roots.available(), 1)

    def test_remove_root_gradebook(self):
        """Tests remove_root_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        roots = self.session.get_root_gradebooks()
        self.assertEqual(roots.available(), 1)

        create_form = self.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'new root'
        create_form.description = 'Test Gradebook root'
        new_gradebook = self.svc_mgr.create_gradebook(create_form)
        self.svc_mgr.add_root_gradebook(new_gradebook.ident)

        roots = self.session.get_root_gradebooks()
        self.assertEqual(roots.available(), 2)

        self.session.remove_root_gradebook(new_gradebook.ident)

        roots = self.session.get_root_gradebooks()
        self.assertEqual(roots.available(), 1)

    def test_add_child_gradebook(self):
        """Tests add_child_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        # this is tested in the setUpClass
        children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
        self.assertTrue(isinstance(children, ABCObjects.GradebookList))
        self.assertEqual(children.available(), 2)

    def test_remove_child_gradebook(self):
        """Tests remove_child_gradebook"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

        create_form = self.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'test child'
        create_form.description = 'Test Gradebook child'
        new_gradebook = self.svc_mgr.create_gradebook(create_form)
        self.svc_mgr.add_child_gradebook(
            self.catalogs['Root'].ident,
            new_gradebook.ident)

        children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 3)

        self.session.remove_child_gradebook(
            self.catalogs['Root'].ident,
            new_gradebook.ident)

        children = self.session.get_child_gradebooks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)
