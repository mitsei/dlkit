"""Unit tests of grading sessions."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
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

    @unittest.skip('unimplemented test')
    def test_get_grade_system_by_grade(self):
        """Tests get_grade_system_by_grade"""
        pass

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

    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip('unimplemented test')
    def test_can_search_grade_systems(self):
        """Tests can_search_grade_systems"""
        pass

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        query = self.catalog.get_grade_system_query()

    def test_get_grade_systems_by_query(self):
        """Tests get_grade_systems_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_grade_system_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_grade_systems_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_grade_systems_by_query(query).available(), 3)


class TestGradeSystemAdminSession(unittest.TestCase):
    """Tests for GradeSystemAdminSession"""

    # From test_templates/resource.py::ResourceAdminSession::init_template
    @classmethod
    def setUpClass(cls):
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

    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip('unimplemented test')
    def test_can_create_grades(self):
        """Tests can_create_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_create_grade_with_record_types(self):
        """Tests can_create_grade_with_record_types"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_form_for_create(self):
        """Tests get_grade_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_grade(self):
        """Tests create_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_grades(self):
        """Tests can_update_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_form_for_update(self):
        """Tests get_grade_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_grade(self):
        """Tests update_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_grades(self):
        """Tests can_delete_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_grade(self):
        """Tests delete_grade"""
        pass

    def test_can_manage_grade_aliases(self):
        """Tests can_manage_grade_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_grade_aliases(), bool))

    @unittest.skip('unimplemented test')
    def test_alias_grade(self):
        """Tests alias_grade"""
        pass


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

    @unittest.skip('unimplemented test')
    def test_use_effective_grade_entry_view(self):
        """Tests use_effective_grade_entry_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_any_effective_grade_entry_view(self):
        """Tests use_any_effective_grade_entry_view"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_on_date(self):
        """Tests get_grade_entries_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column(self):
        """Tests get_grade_entries_for_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column_on_date(self):
        """Tests get_grade_entries_for_gradebook_column_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_resource(self):
        """Tests get_grade_entries_for_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_resource_on_date(self):
        """Tests get_grade_entries_for_resource_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column_and_resource(self):
        """Tests get_grade_entries_for_gradebook_column_and_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_for_gradebook_column_and_resource_on_date(self):
        """Tests get_grade_entries_for_gradebook_column_and_resource_on_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries_by_grader(self):
        """Tests get_grade_entries_by_grader"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_can_search_grade_entries(self):
        """Tests can_search_grade_entries"""
        pass

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        query = self.catalog.get_grade_entry_query()

    def test_get_grade_entries_by_query(self):
        """Tests get_grade_entries_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_grade_entry_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_grade_entries_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_grade_entries_by_query(query).available(), 3)


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

    @unittest.skip('unimplemented test')
    def test_can_overridecalculated_grade_entries(self):
        """Tests can_overridecalculated_grade_entries"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_form_for_override(self):
        """Tests get_grade_entry_form_for_override"""
        pass

    @unittest.skip('unimplemented test')
    def test_override_calculated_grade_entry(self):
        """Tests override_calculated_grade_entry"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_can_lookup_gradebook_columns(self):
        """Tests can_lookup_gradebook_columns"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_supports_summary(self):
        """Tests supports_summary"""
        pass

    def test_get_gradebook_column_summary(self):
        """Tests get_gradebook_column_summary"""
        self.assertTrue(isinstance(self.catalog.get_gradebook_column_summary(self.gradebook_column_ids[0]),
                                   GradebookColumnSummary))


class TestGradebookColumnQuerySession(unittest.TestCase):
    """Tests for GradebookColumnQuerySession"""

    @classmethod
    def setUpClass(cls):
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

    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip('unimplemented test')
    def test_can_search_gradebook_columns(self):
        """Tests can_search_gradebook_columns"""
        pass

    def test_use_federated_gradebook_view(self):
        """Tests use_federated_gradebook_view"""
        self.catalog.use_federated_gradebook_view()

    def test_use_isolated_gradebook_view(self):
        """Tests use_isolated_gradebook_view"""
        self.catalog.use_isolated_gradebook_view()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        query = self.catalog.get_gradebook_column_query()

    def test_get_gradebook_columns_by_query(self):
        """Tests get_gradebook_columns_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_gradebook_column_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_gradebook_columns_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_gradebook_columns_by_query(query).available(), 3)


class TestGradebookColumnAdminSession(unittest.TestCase):
    """Tests for GradebookColumnAdminSession"""

    # From test_templates/resource.py::ResourceAdminSession::init_template
    @classmethod
    def setUpClass(cls):
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

    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip('unimplemented test')
    def test_can_update_gradebook_columns(self):
        """Tests can_update_gradebook_columns"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_sequence_gradebook_columns(self):
        """Tests sequence_gradebook_columns"""
        pass

    @unittest.skip('unimplemented test')
    def test_move_gradebook_column(self):
        """Tests move_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_copy_gradebook_column_entries(self):
        """Tests copy_gradebook_column_entries"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_gradebook_columns(self):
        """Tests can_delete_gradebook_columns"""
        pass

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

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_gradebooks():
            cls.svc_mgr.delete_gradebook(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_gradebooks(self):
        """Tests can_lookup_gradebooks"""
        pass

    def test_use_comparative_gradebook_view(self):
        """Tests use_comparative_gradebook_view"""
        self.svc_mgr.use_comparative_gradebook_view()

    def test_use_plenary_gradebook_view(self):
        """Tests use_plenary_gradebook_view"""
        self.svc_mgr.use_plenary_gradebook_view()

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        catalog = self.svc_mgr.get_gradebook(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_gradebooks_by_ids(self):
        """Tests get_gradebooks_by_ids"""
        catalogs = self.svc_mgr.get_gradebooks_by_ids(self.catalog_ids)

    @unittest.skip('unimplemented test')
    def test_get_gradebooks_by_genus_type(self):
        """Tests get_gradebooks_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebooks_by_parent_genus_type(self):
        """Tests get_gradebooks_by_parent_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebooks_by_record_type(self):
        """Tests get_gradebooks_by_record_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebooks_by_provider(self):
        """Tests get_gradebooks_by_provider"""
        pass

    def test_get_gradebooks(self):
        """Tests get_gradebooks"""
        catalogs = self.svc_mgr.get_gradebooks()


class TestGradebookAdminSession(unittest.TestCase):
    """Tests for GradebookAdminSession"""

    @classmethod
    def setUpClass(cls):
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

    @classmethod
    def tearDownClass(cls):
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

    @unittest.skip('unimplemented test')
    def test_can_update_gradebooks(self):
        """Tests can_update_gradebooks"""
        pass

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

    @unittest.skip('unimplemented test')
    def test_can_delete_gradebooks(self):
        """Tests can_delete_gradebooks"""
        pass

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
