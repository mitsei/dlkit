"""Unit tests of grading objects."""


import unittest


from decimal import Decimal


from dlkit.abstract_osid.authentication.objects import Agent
from dlkit.abstract_osid.grading import objects as ABCObjects
from dlkit.abstract_osid.grading.objects import GradeList
from dlkit.abstract_osid.grading.objects import GradeSystem
from dlkit.abstract_osid.grading.objects import GradebookColumn
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.json_.assessment.objects import AssessmentOffered
from dlkit.json_.grading.objects import GradeList
from dlkit.json_.grading.objects import GradebookColumn
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.records import registry
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
SEQUENCE_ASSESSMENT = Type(**registry.ASSESSMENT_RECORD_TYPES["simple-child-sequencing"])


class TestGrade(unittest.TestCase):
    """Tests for Grade"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        cls.grade_system = cls.catalog.create_grade_system(form)

    def setUp(self):
        form = self.catalog.get_grade_form_for_create(
            self.grade_system.ident,
            [])
        form.display_name = 'Test object'
        self.object = self.catalog.create_grade(form)

    def tearDown(self):
        for grade in self.grade_system.get_grades():
            self.catalog.delete_grade(grade.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        grade_system_id = self.object.get_grade_system_id()
        self.assertTrue(isinstance(grade_system_id, Id))
        self.assertEqual(str(grade_system_id),
                         str(self.grade_system.ident))

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        grade_system = self.object.get_grade_system()
        self.assertTrue(isinstance(grade_system, ABCObjects.GradeSystem))
        self.assertEqual(str(grade_system.ident),
                         str(self.grade_system.ident))

    def test_get_input_score_start_range(self):
        """Tests get_input_score_start_range"""
        start_range = self.object.get_input_score_end_range()
        self.assertIsNone(start_range)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_form_for_create(
            self.grade_system.ident,
            [])
        form.set_input_score_start_range(50.0)
        new_grade = self.catalog.create_grade(form)

        self.assertEqual(new_grade.get_input_score_start_range(), 50.0)

    def test_get_input_score_end_range(self):
        """Tests get_input_score_end_range"""
        end_range = self.object.get_input_score_end_range()
        self.assertIsNone(end_range)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_form_for_create(
            self.grade_system.ident,
            [])
        form.set_input_score_end_range(50.0)
        new_grade = self.catalog.create_grade(form)

        self.assertEqual(new_grade.get_input_score_end_range(), 50.0)

    def test_get_output_score(self):
        """Tests get_output_score"""
        score = self.object.get_output_score()
        self.assertIsNone(score)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_form_for_create(
            self.grade_system.ident,
            [])
        form.set_output_score(50.0)
        new_grade = self.catalog.create_grade(form)

        self.assertEqual(new_grade.get_output_score(), 50.0)

    def test_get_grade_record(self):
        """Tests get_grade_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_grade_record(True)


class TestGradeForm(unittest.TestCase):
    """Tests for GradeForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        cls.grade_system = cls.catalog.create_grade_system(form)

    def setUp(self):
        self.form = self.catalog.get_grade_form_for_create(
            self.grade_system.ident,
            [])

    def tearDown(self):
        for grade in self.grade_system.get_grades():
            self.catalog.delete_grade(grade.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_input_score_start_range_metadata(self):
        """Tests get_input_score_start_range_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_input_score_start_range_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_input_score_start_range(self):
        """Tests set_input_score_start_range"""
        self.assertIsNone(self.form._my_map['inputScoreStartRange'])
        self.form.set_input_score_start_range(50.0)
        self.assertEqual(self.form._my_map['inputScoreStartRange'], 50.0)

    def test_clear_input_score_start_range(self):
        """Tests clear_input_score_start_range"""
        self.form.set_input_score_start_range(50.0)
        self.assertIsNotNone(self.form._my_map['inputScoreStartRange'])
        self.form.clear_input_score_start_range()
        self.assertIsNone(self.form._my_map['inputScoreStartRange'])

    def test_get_input_score_end_range_metadata(self):
        """Tests get_input_score_end_range_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_input_score_end_range_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_input_score_end_range(self):
        """Tests set_input_score_end_range"""
        self.assertIsNone(self.form._my_map['inputScoreEndRange'])
        self.form.set_input_score_end_range(50.0)
        self.assertEqual(self.form._my_map['inputScoreEndRange'], 50.0)

    def test_clear_input_score_end_range(self):
        """Tests clear_input_score_end_range"""
        self.form.set_input_score_end_range(50.0)
        self.assertIsNotNone(self.form._my_map['inputScoreEndRange'])
        self.form.clear_input_score_end_range()
        self.assertIsNone(self.form._my_map['inputScoreEndRange'])

    def test_get_output_score_metadata(self):
        """Tests get_output_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_output_score_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_output_score(self):
        """Tests set_output_score"""
        self.assertIsNone(self.form._my_map['outputScore'])
        self.form.set_output_score(50.0)
        self.assertEqual(self.form._my_map['outputScore'], 50.0)

    def test_clear_output_score(self):
        """Tests clear_output_score"""
        self.form.set_output_score(50.0)
        self.assertIsNotNone(self.form._my_map['outputScore'])
        self.form.clear_output_score()
        self.assertIsNone(self.form._my_map['outputScore'])

    def test_get_grade_form_record(self):
        """Tests get_grade_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_grade_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestGradeList(unittest.TestCase):
    """Tests for GradeList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        cls.grade_system = cls.catalog.create_grade_system(form)

    def setUp(self):
        self.grade_list = []
        for num in [0, 1]:
            form = self.catalog.get_grade_form_for_create(
                self.grade_system.ident,
                [])
            new_grade = self.catalog.create_grade(form)
            self.grade_list.append(new_grade)
        self.grade_list = GradeList(self.grade_list,
                                    runtime=self.catalog._runtime,
                                    proxy=self.catalog._proxy)

    def tearDown(self):
        for grade in self.grade_system.get_grades():
            self.catalog.delete_grade(grade.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_next_grade(self):
        """Tests get_next_grade"""
        from dlkit.abstract_osid.grading.objects import Grade
        self.assertTrue(isinstance(self.grade_list.get_next_grade(), Grade))

    def test_get_next_grades(self):
        """Tests get_next_grades"""
        from dlkit.abstract_osid.grading.objects import Grade, GradeList
        new_list = self.grade_list.get_next_grades(2)
        self.assertTrue(isinstance(new_list, GradeList))
        for item in new_list:
            self.assertTrue(isinstance(item, Grade))


class TestGradeSystem(unittest.TestCase):
    """Tests for GradeSystem"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::Resource::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_grade_system(form)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::Resource::init_template
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_is_based_on_grades(self):
        """Tests is_based_on_grades"""
        # when not set on create, returns None
        self.assertIsNone(self.object.is_based_on_grades())

        form = self.catalog.get_grade_system_form_for_create([])
        form.set_based_on_grades(True)
        new_grade_system = self.catalog.create_grade_system(form)

        self.assertTrue(new_grade_system.is_based_on_grades())

    def test_get_grade_ids(self):
        """Tests get_grade_ids"""
        grade_ids = self.object.get_grade_ids()
        self.assertTrue(isinstance(grade_ids, IdList))
        self.assertEqual(grade_ids.available(), 0)

    def test_get_grades(self):
        """Tests get_grades"""
        grades = self.object.get_grades()
        self.assertTrue(isinstance(grades, GradeList))
        self.assertEqual(grades.available(), 0)

    def test_get_lowest_numeric_score(self):
        """Tests get_lowest_numeric_score"""
        score = self.object.get_lowest_numeric_score()
        self.assertIsNone(score)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_system_form_for_create([])
        form.set_lowest_numeric_score(0.0)
        new_grade_system = self.catalog.create_grade_system(form)

        self.assertEqual(new_grade_system.get_lowest_numeric_score(), 0.0)

    def test_get_numeric_score_increment(self):
        """Tests get_numeric_score_increment"""
        score = self.object.get_numeric_score_increment()
        self.assertIsNone(score)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_system_form_for_create([])
        form.set_numeric_score_increment(1.0)
        new_grade_system = self.catalog.create_grade_system(form)

        self.assertEqual(new_grade_system.get_numeric_score_increment(), 1.0)

    def test_get_highest_numeric_score(self):
        """Tests get_highest_numeric_score"""
        score = self.object.get_highest_numeric_score()
        self.assertIsNone(score)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_system_form_for_create([])
        form.set_highest_numeric_score(100.0)
        new_grade_system = self.catalog.create_grade_system(form)

        self.assertEqual(new_grade_system.get_highest_numeric_score(), 100.0)

    def test_get_grade_system_record(self):
        """Tests get_grade_system_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_grade_system_record(True)


class TestGradeSystemForm(unittest.TestCase):
    """Tests for GradeSystemForm"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_grade_system_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_based_on_grades_metadata(self):
        """Tests get_based_on_grades_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_based_on_grades_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'BOOLEAN')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_based_on_grades(self):
        """Tests set_based_on_grades"""
        self.assertIsNone(self.form._my_map['basedOnGrades'])
        self.form.set_based_on_grades(True)
        self.assertIsNotNone(self.form._my_map['basedOnGrades'])

    def test_clear_based_on_grades(self):
        """Tests clear_based_on_grades"""
        self.form.set_based_on_grades(True)
        self.assertIsNotNone(self.form._my_map['basedOnGrades'])
        self.form.clear_based_on_grades()
        self.assertIsNone(self.form._my_map['basedOnGrades'])

    def test_get_lowest_numeric_score_metadata(self):
        """Tests get_lowest_numeric_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_lowest_numeric_score_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_lowest_numeric_score(self):
        """Tests set_lowest_numeric_score"""
        self.assertIsNone(self.form._my_map['lowestNumericScore'])
        self.form.set_lowest_numeric_score(100.0)
        self.assertIsNotNone(self.form._my_map['lowestNumericScore'])

    def test_clear_lowest_numeric_score(self):
        """Tests clear_lowest_numeric_score"""
        self.form.set_lowest_numeric_score(100.0)
        self.assertIsNotNone(self.form._my_map['lowestNumericScore'])
        self.form.clear_lowest_numeric_score()
        self.assertIsNone(self.form._my_map['lowestNumericScore'])

    def test_get_numeric_score_increment_metadata(self):
        """Tests get_numeric_score_increment_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_numeric_score_increment_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_numeric_score_increment(self):
        """Tests set_numeric_score_increment"""
        self.assertIsNone(self.form._my_map['numericScoreIncrement'])
        self.form.set_numeric_score_increment(100.0)
        self.assertIsNotNone(self.form._my_map['numericScoreIncrement'])

    def test_clear_numeric_score_increment(self):
        """Tests clear_numeric_score_increment"""
        self.form.set_numeric_score_increment(100.0)
        self.assertIsNotNone(self.form._my_map['numericScoreIncrement'])
        self.form.clear_numeric_score_increment()
        self.assertIsNone(self.form._my_map['numericScoreIncrement'])

    def test_get_highest_numeric_score_metadata(self):
        """Tests get_highest_numeric_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_highest_numeric_score_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_highest_numeric_score(self):
        """Tests set_highest_numeric_score"""
        self.assertIsNone(self.form._my_map['highestNumericScore'])
        self.form.set_highest_numeric_score(100.0)
        self.assertIsNotNone(self.form._my_map['highestNumericScore'])

    def test_clear_highest_numeric_score(self):
        """Tests clear_highest_numeric_score"""
        self.form.set_highest_numeric_score(100.0)
        self.assertIsNotNone(self.form._my_map['highestNumericScore'])
        self.form.clear_highest_numeric_score()
        self.assertIsNone(self.form._my_map['highestNumericScore'])

    def test_get_grade_system_form_record(self):
        """Tests get_grade_system_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_grade_system_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestGradeSystemList(unittest.TestCase):
    """Tests for GradeSystemList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeSystemList tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.grading.objects import GradeSystemList
        self.grade_system_list = list()
        self.grade_system_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_grade_system_form_for_create([])
            create_form.display_name = 'Test GradeSystem ' + str(num)
            create_form.description = 'Test GradeSystem for GradeSystemList tests'
            obj = self.catalog.create_grade_system(create_form)
            self.grade_system_list.append(obj)
            self.grade_system_ids.append(obj.ident)
        self.grade_system_list = GradeSystemList(self.grade_system_list)
        self.object = self.grade_system_list

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_next_grade_system(self):
        """Tests get_next_grade_system"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradeSystem
        self.assertTrue(isinstance(self.grade_system_list.get_next_grade_system(), GradeSystem))

    def test_get_next_grade_systems(self):
        """Tests get_next_grade_systems"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradeSystemList, GradeSystem
        new_list = self.grade_system_list.get_next_grade_systems(2)
        self.assertTrue(isinstance(new_list, GradeSystemList))
        for item in new_list:
            self.assertTrue(isinstance(item, GradeSystem))


class TestGradeEntry(unittest.TestCase):
    """Tests for GradeEntry"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        cls.grade_system = cls.catalog.create_grade_system(form)

        form = cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(cls.grade_system.ident)
        cls.column = cls.catalog.create_gradebook_column(form)

    def setUp(self):
        form = self.catalog.get_grade_entry_form_for_create(
            self.column.ident,
            AGENT_ID,
            [])
        form.display_name = 'Test object'
        self.object = self.catalog.create_grade_entry(form)

    def tearDown(self):
        for grade_entry in self.catalog.get_grade_entries():
            self.catalog.delete_grade_entry(grade_entry.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook_column_id(self):
        """Tests get_gradebook_column_id"""
        self.assertTrue(isinstance(self.object.get_gradebook_column_id(), Id))
        self.assertEqual(str(self.object.get_gradebook_column_id()),
                         str(self.column.ident))

    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        self.assertTrue(isinstance(self.object.get_gradebook_column(), GradebookColumn))
        self.assertEqual(str(self.object.get_gradebook_column().ident),
                         str(self.column.ident))

    def test_get_key_resource_id(self):
        """Tests get_key_resource_id"""
        agent_id = self.object.get_key_resource_id()
        self.assertTrue(isinstance(agent_id, Id))

    def test_get_key_resource(self):
        """Tests get_key_resource"""
        agent = self.object.get_key_resource()
        self.assertTrue(isinstance(agent, Agent))

    def test_is_derived(self):
        """Tests is_derived"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_derived(), bool))
        self.assertFalse(self.object.is_derived())

    def test_overrides_calculated_entry(self):
        """Tests overrides_calculated_entry"""
        self.assertTrue(isinstance(self.object.overrides_calculated_entry(), bool))

    def test_get_overridden_calculated_entry_id(self):
        """Tests get_overridden_calculated_entry_id"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_overridden_calculated_entry_id)

    def test_get_overridden_calculated_entry(self):
        """Tests get_overridden_calculated_entry"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_overridden_calculated_entry)

    def test_is_ignored_for_calculations(self):
        """Tests is_ignored_for_calculations"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_ignored_for_calculations(), bool))
        self.assertFalse(self.object.is_ignored_for_calculations())

    def test_is_graded(self):
        """Tests is_graded"""
        self.assertTrue(isinstance(self.object.is_graded(), bool))

    def test_get_grade_id(self):
        """Tests get_grade_id"""
        self.assertTrue(isinstance(self.object.get_grade_id(), Id))

    def test_get_grade(self):
        """Tests get_grade"""
        with self.assertRaises(errors.IllegalState):
            self.object.get_grade()

    def test_get_score(self):
        """Tests get_score"""
        score = self.object.get_score()
        self.assertIsNone(score)

        # if this is set, should be a Decimal
        form = self.catalog.get_grade_entry_form_for_create(
            self.column.ident,
            AGENT_ID,
            [])
        form.set_score(50.0)
        new_grade_entry = self.catalog.create_grade_entry(form)

        self.assertEqual(new_grade_entry.get_score(), 50.0)

    def test_get_time_graded(self):
        """Tests get_time_graded"""
        with self.assertRaises(errors.IllegalState):
            self.object.get_time_graded()

    def test_get_grader_id(self):
        """Tests get_grader_id"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_grader_id()

    def test_get_grader(self):
        """Tests get_grader"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_grader()

    def test_get_grading_agent_id(self):
        """Tests get_grading_agent_id"""
        agent_id = self.object.get_grading_agent_id()
        self.assertTrue(isinstance(agent_id, Id))

    def test_get_grading_agent(self):
        """Tests get_grading_agent"""
        agent = self.object.get_grading_agent()
        self.assertTrue(isinstance(agent, Agent))

    def test_get_grade_entry_record(self):
        """Tests get_grade_entry_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_grade_entry_record(True)


class TestGradeEntryForm(unittest.TestCase):
    """Tests for GradeEntryForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        form.set_based_on_grades(True)
        cls.grade_system = cls.catalog.create_grade_system(form)

        form = cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(cls.grade_system.ident)
        cls.column = cls.catalog.create_gradebook_column(form)

    def setUp(self):
        self.form = self.catalog.get_grade_entry_form_for_create(
            self.column.ident,
            AGENT_ID,
            [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_ignored_for_calculations_metadata(self):
        """Tests get_ignored_for_calculations_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_ignored_for_calculations_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'BOOLEAN')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_ignored_for_calculations(self):
        """Tests set_ignored_for_calculations"""
        self.form.set_ignored_for_calculations(True)
        self.assertTrue(self.form._my_map['ignoredForCalculations'])
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_ignored_for_calculations('false')

    def test_clear_ignored_for_calculations(self):
        """Tests clear_ignored_for_calculations"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_ignored_for_calculations(True)
        self.assertTrue(self.form._my_map['ignoredForCalculations'])
        self.form.clear_ignored_for_calculations()
        self.assertIsNone(self.form._my_map['ignoredForCalculations'])

    def test_get_grade_metadata(self):
        """Tests get_grade_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_grade_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'ID')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_grade(self):
        """Tests set_grade"""
        # This should come from ResourceForm.set_avatar_template,
        #   but we override because in this case, there is no acceptable
        #   gradeId set, so we get an exception.
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_grade(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))

    def test_clear_grade(self):
        """Tests clear_grade"""
        # Normally this would follow ResourceForm.clear_avatar_template
        # Except we need a valid ``grade`` for the initial ``set_grade`` to
        #   work, so we provide a hand-written impl here.
        self.form._my_map['gradeId'] = 'repository.Asset%3Afake-id%40ODL.MIT.EDU'
        self.assertEqual(self.form._my_map['gradeId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_grade()
        self.assertEqual(self.form._my_map['gradeId'], '')

    def test_get_score_metadata(self):
        """Tests get_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_score_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DECIMAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_score(self):
        """Tests set_score"""
        # because this GradeSystem is basedOnGrades, set_score() throws
        #   an exception
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_score(50.0)

    def test_clear_score(self):
        """Tests clear_score"""
        # because this GradeSystem is basedOnGrades, cannot use form.set_score()
        #   to set the initial data
        self.form._my_map['score'] = 50.0
        self.assertIsNotNone(self.form._my_map['score'])
        self.form.clear_score()

        # Also, because this is basedOnGrades, no exception thrown
        #  AND this method also does nothing...how confusing
        self.assertIsNotNone(self.form._my_map['score'])

    def test_get_grade_entry_form_record(self):
        """Tests get_grade_entry_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_grade_entry_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestGradeEntryList(unittest.TestCase):
    """Tests for GradeEntryList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        form.set_based_on_grades(True)
        cls.grade_system = cls.catalog.create_grade_system(form)

        form = cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(cls.grade_system.ident)
        cls.column = cls.catalog.create_gradebook_column(form)

    def setUp(self):
        from dlkit.json_.grading.objects import GradeEntryList
        self.grade_entry_list = list()
        self.grade_entry_ids = list()

        for num in [0, 1]:
            form = self.catalog.get_grade_entry_form_for_create(
                self.column.ident,
                AGENT_ID,
                [])

            obj = self.catalog.create_grade_entry(form)

            self.grade_entry_list.append(obj)
            self.grade_entry_ids.append(obj.ident)
        self.grade_entry_list = GradeEntryList(self.grade_entry_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_next_grade_entry(self):
        """Tests get_next_grade_entry"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradeEntry
        self.assertTrue(isinstance(self.grade_entry_list.get_next_grade_entry(), GradeEntry))

    def test_get_next_grade_entries(self):
        """Tests get_next_grade_entries"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradeEntryList, GradeEntry
        new_list = self.grade_entry_list.get_next_grade_entries(2)
        self.assertTrue(isinstance(new_list, GradeEntryList))
        for item in new_list:
            self.assertTrue(isinstance(item, GradeEntry))


class TestGradebookColumn(unittest.TestCase):
    """Tests for GradebookColumn"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_grade_system_form_for_create([])
        form.display_name = 'Grade system'
        cls.grade_system = cls.catalog.create_grade_system(form)

    def setUp(self):
        form = self.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Gradebook Column'
        form.set_grade_system(self.grade_system.ident)
        self.object = self.catalog.create_gradebook_column(form)

    def tearDown(self):
        for gradebook_column in self.catalog.get_gradebook_columns():
            self.catalog.delete_gradebook_column(gradebook_column.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        grade_system_id = self.object.get_grade_system_id()
        self.assertTrue(isinstance(grade_system_id, Id))
        self.assertTrue(str(grade_system_id),
                        str(self.grade_system.ident))

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        grade_system = self.object.get_grade_system()
        self.assertTrue(isinstance(grade_system, GradeSystem))
        self.assertTrue(str(grade_system.ident),
                        str(self.grade_system.ident))

    def test_get_gradebook_column_record(self):
        """Tests get_gradebook_column_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_gradebook_column_record(True)


class TestGradebookColumnForm(unittest.TestCase):
    """Tests for GradebookColumnForm"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_gradebook_column_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_grade_system_metadata(self):
        """Tests get_grade_system_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        mdata = self.form.get_grade_system_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'ID')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_grade_system(self):
        """Tests set_grade_system"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['gradeSystemId'], '')
        self.form.set_grade_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['gradeSystemId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_grade_system(True)

    def test_clear_grade_system(self):
        """Tests clear_grade_system"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_grade_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['gradeSystemId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_grade_system()
        self.assertEqual(self.form._my_map['gradeSystemId'], self.form.get_grade_system_metadata().get_default_id_values()[0])

    def test_get_gradebook_column_form_record(self):
        """Tests get_gradebook_column_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_gradebook_column_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestGradebookColumnList(unittest.TestCase):
    """Tests for GradebookColumnList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookColumnList tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.grading.objects import GradebookColumnList
        self.gradebook_column_list = list()
        self.gradebook_column_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradebookColumnList tests'
            obj = self.catalog.create_gradebook_column(create_form)
            self.gradebook_column_list.append(obj)
            self.gradebook_column_ids.append(obj.ident)
        self.gradebook_column_list = GradebookColumnList(self.gradebook_column_list)
        self.object = self.gradebook_column_list

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_next_gradebook_column(self):
        """Tests get_next_gradebook_column"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookColumn
        self.assertTrue(isinstance(self.gradebook_column_list.get_next_gradebook_column(), GradebookColumn))

    def test_get_next_gradebook_columns(self):
        """Tests get_next_gradebook_columns"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookColumnList, GradebookColumn
        new_list = self.gradebook_column_list.get_next_gradebook_columns(2)
        self.assertTrue(isinstance(new_list, GradebookColumnList))
        for item in new_list:
            self.assertTrue(isinstance(item, GradebookColumn))


class TestGradebookColumnSummary(unittest.TestCase):
    """Tests for GradebookColumnSummary"""

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
        cls.object = cls.catalog.get_gradebook_column_summary(cls.gradebook_column_ids[0])

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

    def test_get_gradebook_column_id(self):
        """Tests get_gradebook_column_id"""
        self.assertTrue(isinstance(self.object.get_gradebook_column_id(), Id))
        self.assertEqual(str(self.object.get_gradebook_column_id()),
                         str(self.gradebook_column_ids[0]))

    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        self.assertTrue(isinstance(self.object.get_gradebook_column(), GradebookColumn))
        self.assertEqual(str(self.object.get_gradebook_column().ident),
                         str(self.gradebook_column_ids[0]))

    def test_get_mean(self):
        """Tests get_mean"""
        self.assertTrue(isinstance(self.object.get_mean(), Decimal))
        self.assertEqual(self.object.get_mean(), Decimal(49.5))

    def test_get_median(self):
        """Tests get_median"""
        self.assertTrue(isinstance(self.object.get_median(), Decimal))
        self.assertEqual(self.object.get_median(), Decimal(49.5))

    def test_get_mode(self):
        """Tests get_mode"""
        # From test_templates/assessment.py::AssessmentTaken::get_score_template
        self.assertTrue(isinstance(self.object.get_mode(), Decimal))
        self.assertEqual(self.object.get_mode(), Decimal(0.0))

    def test_get_rms(self):
        """Tests get_rms"""
        self.assertTrue(isinstance(self.object.get_rms(), Decimal))
        self.assertEqual(self.object.get_rms(), Decimal('57.30183243143276652887614453'))

    def test_get_standard_deviation(self):
        """Tests get_standard_deviation"""
        self.assertTrue(isinstance(self.object.get_standard_deviation(), Decimal))
        self.assertEqual(self.object.get_standard_deviation(), Decimal('28.86607004772211800433171979'))

    def test_get_sum(self):
        """Tests get_sum"""
        self.assertTrue(isinstance(self.object.get_sum(), Decimal))
        self.assertEqual(self.object.get_sum(), Decimal('4950'))

    def test_get_gradebook_column_summary_record(self):
        """Tests get_gradebook_column_summary_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_gradebook_column_summary_record(True)


class TestGradebook(unittest.TestCase):
    """Tests for Gradebook"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::Bin::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')

    def setUp(self):
        # From test_templates/resource.py::Bin::init_template
        form = self.svc_mgr.get_gradebook_form_for_create([])
        form.display_name = 'for testing'
        self.object = self.svc_mgr.create_gradebook(form)

    def tearDown(self):
        # From test_templates/resource.py::Bin::init_template
        self.svc_mgr.delete_gradebook(self.object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::Bin::init_template
        pass

    def test_get_gradebook_record(self):
        """Tests get_gradebook_record"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_gradebook_record(True)


class TestGradebookForm(unittest.TestCase):
    """Tests for GradebookForm"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')

    def setUp(self):
        # From test_templates/resource.py::BinForm::init_template
        self.object = self.svc_mgr.get_gradebook_form_for_create([])

    def tearDown(self):
        # From test_templates/resource.py::BinForm::init_template
        pass

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinForm::init_template
        pass

    def test_get_gradebook_form_record(self):
        """Tests get_gradebook_form_record"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_gradebook_form_record(True)


class TestGradebookList(unittest.TestCase):
    """Tests for GradebookList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookList tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        cls.gradebook_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.grading.objects import GradebookList
        self.gradebook_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test Gradebook ' + str(num)
            create_form.description = 'Test Gradebook for GradebookList tests'
            obj = self.svc_mgr.create_gradebook(create_form)
            self.gradebook_list.append(obj)
            self.gradebook_ids.append(obj.ident)
        self.gradebook_list = GradebookList(self.gradebook_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.gradebook_ids:
            cls.svc_mgr.delete_gradebook(obj)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_next_gradebook(self):
        """Tests get_next_gradebook"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import Gradebook
        self.assertTrue(isinstance(self.gradebook_list.get_next_gradebook(), Gradebook))

    def test_get_next_gradebooks(self):
        """Tests get_next_gradebooks"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookList, Gradebook
        new_list = self.gradebook_list.get_next_gradebooks(2)
        self.assertTrue(isinstance(new_list, GradebookList))
        for item in new_list:
            self.assertTrue(isinstance(item, Gradebook))


class TestGradebookNode(unittest.TestCase):
    """Tests for GradebookNode"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNode
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookNode tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        cls.gradebook_ids = list()

    def setUp(self):
        # Implemented from init template for BinNode
        from dlkit.json_.grading.objects import GradebookNode
        self.gradebook_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test Gradebook ' + str(num)
            create_form.description = 'Test Gradebook for GradebookNode tests'
            obj = self.svc_mgr.create_gradebook(create_form)
            self.gradebook_list.append(GradebookNode(
                obj.object_map,
                runtime=self.svc_mgr._runtime,
                proxy=self.svc_mgr._proxy))
            self.gradebook_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_gradebook(self.gradebook_list[0].ident)
        self.svc_mgr.add_child_gradebook(
            self.gradebook_list[0].ident,
            self.gradebook_list[1].ident)

        self.object = self.svc_mgr.get_gradebook_nodes(
            self.gradebook_list[0].ident, 0, 5, False)

    def tearDown(self):
        # Implemented from init template for BinNode
        self.svc_mgr.remove_child_gradebook(
            self.gradebook_list[0].ident,
            self.gradebook_list[1].ident)
        self.svc_mgr.remove_root_gradebook(self.gradebook_list[0].ident)
        for node in self.gradebook_list:
            self.svc_mgr.delete_gradebook(node.ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNode
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_gradebook(self):
        """Tests get_gradebook"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.grading.objects import Gradebook
        self.assertTrue(isinstance(self.gradebook_list[0].get_gradebook(), Gradebook))
        self.assertEqual(str(self.gradebook_list[0].get_gradebook().ident),
                         str(self.gradebook_list[0].ident))

    def test_get_parent_gradebook_nodes(self):
        """Tests get_parent_gradebook_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.grading.objects import GradebookNodeList
        node = self.svc_mgr.get_gradebook_nodes(
            self.gradebook_list[1].ident,
            1,
            0,
            False)
        self.assertTrue(isinstance(node.get_parent_gradebook_nodes(), GradebookNodeList))
        self.assertEqual(node.get_parent_gradebook_nodes().available(),
                         1)
        self.assertEqual(str(node.get_parent_gradebook_nodes().next().ident),
                         str(self.gradebook_list[0].ident))

    def test_get_child_gradebook_nodes(self):
        """Tests get_child_gradebook_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.grading.objects import GradebookNodeList
        node = self.svc_mgr.get_gradebook_nodes(
            self.gradebook_list[0].ident,
            0,
            1,
            False)
        self.assertTrue(isinstance(node.get_child_gradebook_nodes(), GradebookNodeList))
        self.assertEqual(node.get_child_gradebook_nodes().available(),
                         1)
        self.assertEqual(str(node.get_child_gradebook_nodes().next().ident),
                         str(self.gradebook_list[1].ident))


class TestGradebookNodeList(unittest.TestCase):
    """Tests for GradebookNodeList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNodeList
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradebookNodeList tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        cls.gradebook_node_ids = list()

    def setUp(self):
        # Implemented from init template for BinNodeList
        from dlkit.json_.grading.objects import GradebookNodeList, GradebookNode
        self.gradebook_node_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_gradebook_form_for_create([])
            create_form.display_name = 'Test GradebookNode ' + str(num)
            create_form.description = 'Test GradebookNode for GradebookNodeList tests'
            obj = self.svc_mgr.create_gradebook(create_form)
            self.gradebook_node_list.append(GradebookNode(obj.object_map))
            self.gradebook_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_gradebook(self.gradebook_node_list[0].ident)
        self.svc_mgr.add_child_gradebook(
            self.gradebook_node_list[0].ident,
            self.gradebook_node_list[1].ident)
        self.gradebook_node_list = GradebookNodeList(self.gradebook_node_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNodeList
        for obj in cls.gradebook_node_ids:
            cls.svc_mgr.delete_gradebook(obj)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_get_next_gradebook_node(self):
        """Tests get_next_gradebook_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.grading.objects import GradebookNode
        self.assertTrue(isinstance(self.gradebook_node_list.get_next_gradebook_node(), GradebookNode))

    def test_get_next_gradebook_nodes(self):
        """Tests get_next_gradebook_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.grading.objects import GradebookNodeList, GradebookNode
        new_list = self.gradebook_node_list.get_next_gradebook_nodes(2)
        self.assertTrue(isinstance(new_list, GradebookNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, GradebookNode))
