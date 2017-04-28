"""Unit tests of grading objects."""


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
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


class TestGrade(unittest.TestCase):
    """Tests for Grade"""

    # This really shouldn't be generated...should be GradeBook??
    @classmethod
    def setUpClass(cls):
        cls.object = None

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system(self):
        """Tests get_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_input_score_start_range(self):
        """Tests get_input_score_start_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_input_score_end_range(self):
        """Tests get_input_score_end_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_output_score(self):
        """Tests get_output_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_record(self):
        """Tests get_grade_record"""
        pass


class TestGradeForm(unittest.TestCase):
    """Tests for GradeForm"""

    @unittest.skip('unimplemented test')
    def test_get_input_score_start_range_metadata(self):
        """Tests get_input_score_start_range_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_input_score_start_range(self):
        """Tests set_input_score_start_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_input_score_start_range(self):
        """Tests clear_input_score_start_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_input_score_end_range_metadata(self):
        """Tests get_input_score_end_range_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_input_score_end_range(self):
        """Tests set_input_score_end_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_input_score_end_range(self):
        """Tests clear_input_score_end_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_output_score_metadata(self):
        """Tests get_output_score_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_output_score(self):
        """Tests set_output_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_output_score(self):
        """Tests clear_output_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_form_record(self):
        """Tests get_grade_form_record"""
        pass


class TestGradeList(unittest.TestCase):
    """Tests for GradeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_grade(self):
        """Tests get_next_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_grades(self):
        """Tests get_next_grades"""
        pass


class TestGradeSystem(unittest.TestCase):
    """Tests for GradeSystem"""

    @classmethod
    def setUpClass(cls):
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
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_is_based_on_grades(self):
        """Tests is_based_on_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_ids(self):
        """Tests get_grade_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grades(self):
        """Tests get_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_lowest_numeric_score(self):
        """Tests get_lowest_numeric_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_numeric_score_increment(self):
        """Tests get_numeric_score_increment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_highest_numeric_score(self):
        """Tests get_highest_numeric_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system_record(self):
        """Tests get_grade_system_record"""
        pass


class TestGradeSystemForm(unittest.TestCase):
    """Tests for GradeSystemForm"""

    @unittest.skip('unimplemented test')
    def test_get_based_on_grades_metadata(self):
        """Tests get_based_on_grades_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_based_on_grades(self):
        """Tests set_based_on_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_based_on_grades(self):
        """Tests clear_based_on_grades"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_lowest_numeric_score_metadata(self):
        """Tests get_lowest_numeric_score_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_lowest_numeric_score(self):
        """Tests set_lowest_numeric_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_lowest_numeric_score(self):
        """Tests clear_lowest_numeric_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_numeric_score_increment_metadata(self):
        """Tests get_numeric_score_increment_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_numeric_score_increment(self):
        """Tests set_numeric_score_increment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_numeric_score_increment(self):
        """Tests clear_numeric_score_increment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_highest_numeric_score_metadata(self):
        """Tests get_highest_numeric_score_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_highest_numeric_score(self):
        """Tests set_highest_numeric_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_highest_numeric_score(self):
        """Tests clear_highest_numeric_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system_form_record(self):
        """Tests get_grade_system_form_record"""
        pass


class TestGradeSystemList(unittest.TestCase):
    """Tests for GradeSystemList"""

    @unittest.skip('unimplemented test')
    def test_get_next_grade_system(self):
        """Tests get_next_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_grade_systems(self):
        """Tests get_next_grade_systems"""
        pass


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

        form = cls.catalog.get_grade_entry_form_for_create(
            cls.column.ident,
            AGENT_ID,
            [])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_grade_entry(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.catalog.delete_grade_system(cls.grade_system.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_id(self):
        """Tests get_gradebook_column_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_key_resource_id(self):
        """Tests get_key_resource_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_key_resource(self):
        """Tests get_key_resource"""
        pass

    def test_is_derived(self):
        """Tests is_derived"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_derived(), bool))
        self.assertFalse(self.object.is_derived())

    @unittest.skip('unimplemented test')
    def test_overrides_calculated_entry(self):
        """Tests overrides_calculated_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_overridden_calculated_entry_id(self):
        """Tests get_overridden_calculated_entry_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_overridden_calculated_entry(self):
        """Tests get_overridden_calculated_entry"""
        pass

    def test_is_ignored_for_calculations(self):
        """Tests is_ignored_for_calculations"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_ignored_for_calculations(), bool))
        self.assertFalse(self.object.is_ignored_for_calculations())

    @unittest.skip('unimplemented test')
    def test_is_graded(self):
        """Tests is_graded"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_id(self):
        """Tests get_grade_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade(self):
        """Tests get_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_score(self):
        """Tests get_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_time_graded(self):
        """Tests get_time_graded"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grader_id(self):
        """Tests get_grader_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grader(self):
        """Tests get_grader"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grading_agent_id(self):
        """Tests get_grading_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grading_agent(self):
        """Tests get_grading_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_record(self):
        """Tests get_grade_entry_record"""
        pass


class TestGradeEntryForm(unittest.TestCase):
    """Tests for GradeEntryForm"""

    @unittest.skip('unimplemented test')
    def test_get_ignored_for_calculations_metadata(self):
        """Tests get_ignored_for_calculations_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_ignored_for_calculations(self):
        """Tests set_ignored_for_calculations"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ignored_for_calculations(self):
        """Tests clear_ignored_for_calculations"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_metadata(self):
        """Tests get_grade_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_grade(self):
        """Tests set_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade(self):
        """Tests clear_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_score_metadata(self):
        """Tests get_score_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_score(self):
        """Tests set_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score(self):
        """Tests clear_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_form_record(self):
        """Tests get_grade_entry_form_record"""
        pass


class TestGradeEntryList(unittest.TestCase):
    """Tests for GradeEntryList"""

    @unittest.skip('unimplemented test')
    def test_get_next_grade_entry(self):
        """Tests get_next_grade_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_grade_entries(self):
        """Tests get_next_grade_entries"""
        pass


class TestGradebookColumn(unittest.TestCase):
    """Tests for GradebookColumn"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

        form = cls.catalog.get_gradebook_column_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_gradebook_column(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system(self):
        """Tests get_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_record(self):
        """Tests get_gradebook_column_record"""
        pass


class TestGradebookColumnForm(unittest.TestCase):
    """Tests for GradebookColumnForm"""

    @unittest.skip('unimplemented test')
    def test_get_grade_system_metadata(self):
        """Tests get_grade_system_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_grade_system(self):
        """Tests set_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_system(self):
        """Tests clear_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_form_record(self):
        """Tests get_gradebook_column_form_record"""
        pass


class TestGradebookColumnList(unittest.TestCase):
    """Tests for GradebookColumnList"""

    @unittest.skip('unimplemented test')
    def test_get_next_gradebook_column(self):
        """Tests get_next_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_gradebook_columns(self):
        """Tests get_next_gradebook_columns"""
        pass


class TestGradebookColumnSummary(unittest.TestCase):
    """Tests for GradebookColumnSummary"""

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_id(self):
        """Tests get_gradebook_column_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column(self):
        """Tests get_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_mean(self):
        """Tests get_mean"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_median(self):
        """Tests get_median"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_mode(self):
        """Tests get_mode"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rms(self):
        """Tests get_rms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_standard_deviation(self):
        """Tests get_standard_deviation"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_sum(self):
        """Tests get_sum"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_summary_record(self):
        """Tests get_gradebook_column_summary_record"""
        pass


class TestGradebook(unittest.TestCase):
    """Tests for Gradebook"""

    @unittest.skip('unimplemented test')
    def test_get_gradebook_record(self):
        """Tests get_gradebook_record"""
        pass


class TestGradebookForm(unittest.TestCase):
    """Tests for GradebookForm"""

    @unittest.skip('unimplemented test')
    def test_get_gradebook_form_record(self):
        """Tests get_gradebook_form_record"""
        pass


class TestGradebookList(unittest.TestCase):
    """Tests for GradebookList"""

    @unittest.skip('unimplemented test')
    def test_get_next_gradebook(self):
        """Tests get_next_gradebook"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_gradebooks(self):
        """Tests get_next_gradebooks"""
        pass


class TestGradebookNode(unittest.TestCase):
    """Tests for GradebookNode"""

    @unittest.skip('unimplemented test')
    def test_get_gradebook(self):
        """Tests get_gradebook"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_gradebook_nodes(self):
        """Tests get_parent_gradebook_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_gradebook_nodes(self):
        """Tests get_child_gradebook_nodes"""
        pass


class TestGradebookNodeList(unittest.TestCase):
    """Tests for GradebookNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_gradebook_node(self):
        """Tests get_next_gradebook_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_gradebook_nodes(self):
        """Tests get_next_gradebook_nodes"""
        pass
