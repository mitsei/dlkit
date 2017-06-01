"""Unit tests of grading queries."""


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


class TestGradeQuery(unittest.TestCase):
    """Tests for GradeQuery"""

    # This really shouldn't be generated...should be GradeEntryQuery??
    @classmethod
    def setUpClass(cls):
        cls.object = None

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skip('unimplemented test')
    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_system_id_terms(self):
        """Tests clear_grade_system_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_input_score_start_range(self):
        """Tests match_input_score_start_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_input_score_start_range_terms(self):
        """Tests clear_input_score_start_range_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_input_score_end_range(self):
        """Tests match_input_score_end_range"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_input_score_end_range_terms(self):
        """Tests clear_input_score_end_range_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_input_score(self):
        """Tests match_input_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_input_score_terms(self):
        """Tests clear_input_score_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_output_score(self):
        """Tests match_output_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_output_score_terms(self):
        """Tests clear_output_score_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_query_record(self):
        """Tests get_grade_query_record"""
        pass


class TestGradeSystemQuery(unittest.TestCase):
    """Tests for GradeSystemQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_grade_system_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_based_on_grades(self):
        """Tests match_based_on_grades"""
        pass

    def test_clear_based_on_grades_terms(self):
        """Tests clear_based_on_grades_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['basedOnGrades'] = 'foo'
        self.query.clear_based_on_grades_terms()
        self.assertNotIn('basedOnGrades',
                         self.query._query_terms)

    def test_match_grade_id(self):
        """Tests match_grade_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradeId'], {
            '$in': [str(test_id)]
        })

    def test_clear_grade_id_terms(self):
        """Tests clear_grade_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_id(test_id, match=True)
        self.assertIn('gradeId',
                      self.query._query_terms)
        self.query.clear_grade_id_terms()
        self.assertNotIn('gradeId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_grade_query(self):
        """Tests supports_grade_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_query(self):
        """Tests get_grade_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade(self):
        """Tests match_any_grade"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_terms(self):
        """Tests clear_grade_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_lowest_numeric_score(self):
        """Tests match_lowest_numeric_score"""
        pass

    def test_clear_lowest_numeric_score_terms(self):
        """Tests clear_lowest_numeric_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['lowestNumericScore'] = 'foo'
        self.query.clear_lowest_numeric_score_terms()
        self.assertNotIn('lowestNumericScore',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_numeric_score_increment(self):
        """Tests match_numeric_score_increment"""
        pass

    def test_clear_numeric_score_increment_terms(self):
        """Tests clear_numeric_score_increment_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['numericScoreIncrement'] = 'foo'
        self.query.clear_numeric_score_increment_terms()
        self.assertNotIn('numericScoreIncrement',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_highest_numeric_score(self):
        """Tests match_highest_numeric_score"""
        pass

    def test_clear_highest_numeric_score_terms(self):
        """Tests clear_highest_numeric_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['highestNumericScore'] = 'foo'
        self.query.clear_highest_numeric_score_terms()
        self.assertNotIn('highestNumericScore',
                         self.query._query_terms)

    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_column_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradebookColumnId'], {
            '$in': [str(test_id)]
        })

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_column_id(test_id, match=True)
        self.assertIn('gradebookColumnId',
                      self.query._query_terms)
        self.query.clear_gradebook_column_id_terms()
        self.assertNotIn('gradebookColumnId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        pass

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedGradebookIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        self.assertIn('assignedGradebookIds',
                      self.query._query_terms)
        self.query.clear_gradebook_id_terms()
        self.assertNotIn('assignedGradebookIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        pass

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_grade_system_query_record(self):
        """Tests get_grade_system_query_record"""
        pass


class TestGradeEntryQuery(unittest.TestCase):
    """Tests for GradeEntryQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_grade_entry_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_column_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradebookColumnId'], {
            '$in': [str(test_id)]
        })

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_column_id(test_id, match=True)
        self.assertIn('gradebookColumnId',
                      self.query._query_terms)
        self.query.clear_gradebook_column_id_terms()
        self.assertNotIn('gradebookColumnId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        pass

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebookColumn'] = 'foo'
        self.query.clear_gradebook_column_terms()
        self.assertNotIn('gradebookColumn',
                         self.query._query_terms)

    def test_match_key_resource_id(self):
        """Tests match_key_resource_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_key_resource_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['keyResourceId'], {
            '$in': [str(test_id)]
        })

    def test_clear_key_resource_id_terms(self):
        """Tests clear_key_resource_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_key_resource_id(test_id, match=True)
        self.assertIn('keyResourceId',
                      self.query._query_terms)
        self.query.clear_key_resource_id_terms()
        self.assertNotIn('keyResourceId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_key_resource_query(self):
        """Tests supports_key_resource_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_key_resource_query(self):
        """Tests get_key_resource_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_key_resource(self):
        """Tests match_any_key_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_key_resource_terms(self):
        """Tests clear_key_resource_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_derived(self):
        """Tests match_derived"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_derived_terms(self):
        """Tests clear_derived_terms"""
        pass

    def test_match_overridden_grade_entry_id(self):
        """Tests match_overridden_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_overridden_grade_entry_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['overriddenGradeEntryId'], {
            '$in': [str(test_id)]
        })

    def test_clear_overridden_grade_entry_id_terms(self):
        """Tests clear_overridden_grade_entry_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_overridden_grade_entry_id(test_id, match=True)
        self.assertIn('overriddenGradeEntryId',
                      self.query._query_terms)
        self.query.clear_overridden_grade_entry_id_terms()
        self.assertNotIn('overriddenGradeEntryId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_overridden_grade_entry_query(self):
        """Tests supports_overridden_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_overridden_grade_entry_query(self):
        """Tests get_overridden_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_overridden_grade_entry(self):
        """Tests match_any_overridden_grade_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_overridden_grade_entry_terms(self):
        """Tests clear_overridden_grade_entry_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ignored_for_calculations(self):
        """Tests match_ignored_for_calculations"""
        pass

    def test_clear_ignored_for_calculations_terms(self):
        """Tests clear_ignored_for_calculations_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['ignoredForCalculations'] = 'foo'
        self.query.clear_ignored_for_calculations_terms()
        self.assertNotIn('ignoredForCalculations',
                         self.query._query_terms)

    def test_match_grade_id(self):
        """Tests match_grade_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradeId'], {
            '$in': [str(test_id)]
        })

    def test_clear_grade_id_terms(self):
        """Tests clear_grade_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_id(test_id, match=True)
        self.assertIn('gradeId',
                      self.query._query_terms)
        self.query.clear_grade_id_terms()
        self.assertNotIn('gradeId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_grade_query(self):
        """Tests supports_grade_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_query(self):
        """Tests get_grade_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade(self):
        """Tests match_any_grade"""
        pass

    def test_clear_grade_terms(self):
        """Tests clear_grade_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['grade'] = 'foo'
        self.query.clear_grade_terms()
        self.assertNotIn('grade',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_score(self):
        """Tests match_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_score(self):
        """Tests match_any_score"""
        pass

    def test_clear_score_terms(self):
        """Tests clear_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['score'] = 'foo'
        self.query.clear_score_terms()
        self.assertNotIn('score',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_time_graded(self):
        """Tests match_time_graded"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_time_graded_terms(self):
        """Tests clear_time_graded_terms"""
        pass

    def test_match_grader_id(self):
        """Tests match_grader_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grader_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['graderId'], {
            '$in': [str(test_id)]
        })

    def test_clear_grader_id_terms(self):
        """Tests clear_grader_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grader_id(test_id, match=True)
        self.assertIn('graderId',
                      self.query._query_terms)
        self.query.clear_grader_id_terms()
        self.assertNotIn('graderId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_grader_query(self):
        """Tests supports_grader_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grader_query(self):
        """Tests get_grader_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grader(self):
        """Tests match_any_grader"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grader_terms(self):
        """Tests clear_grader_terms"""
        pass

    def test_match_grading_agent_id(self):
        """Tests match_grading_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grading_agent_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradingAgentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_grading_agent_id_terms(self):
        """Tests clear_grading_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grading_agent_id(test_id, match=True)
        self.assertIn('gradingAgentId',
                      self.query._query_terms)
        self.query.clear_grading_agent_id_terms()
        self.assertNotIn('gradingAgentId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_grading_agent_query(self):
        """Tests supports_grading_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grading_agent_query(self):
        """Tests get_grading_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grading_agent(self):
        """Tests match_any_grading_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grading_agent_terms(self):
        """Tests clear_grading_agent_terms"""
        pass

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedGradebookIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        self.assertIn('assignedGradebookIds',
                      self.query._query_terms)
        self.query.clear_gradebook_id_terms()
        self.assertNotIn('assignedGradebookIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        pass

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_query_record(self):
        """Tests get_grade_entry_query_record"""
        pass


class TestGradebookColumnQuery(unittest.TestCase):
    """Tests for GradebookColumnQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_gradebook_column_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_system_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradeSystemId'], {
            '$in': [str(test_id)]
        })

    def test_clear_grade_system_id_terms(self):
        """Tests clear_grade_system_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_system_id(test_id, match=True)
        self.assertIn('gradeSystemId',
                      self.query._query_terms)
        self.query.clear_grade_system_id_terms()
        self.assertNotIn('gradeSystemId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade_system(self):
        """Tests match_any_grade_system"""
        pass

    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradeSystem'] = 'foo'
        self.query.clear_grade_system_terms()
        self.assertNotIn('gradeSystem',
                         self.query._query_terms)

    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_entry_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['gradeEntryId'], {
            '$in': [str(test_id)]
        })

    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_grade_entry_id(test_id, match=True)
        self.assertIn('gradeEntryId',
                      self.query._query_terms)
        self.query.clear_grade_entry_id_terms()
        self.assertNotIn('gradeEntryId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_column_summary_query(self):
        """Tests supports_gradebook_column_summary_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_summary_query(self):
        """Tests get_gradebook_column_summary_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_column_summary_terms(self):
        """Tests clear_gradebook_column_summary_terms"""
        pass

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedGradebookIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_gradebook_id(test_id, match=True)
        self.assertIn('assignedGradebookIds',
                      self.query._query_terms)
        self.query.clear_gradebook_id_terms()
        self.assertNotIn('assignedGradebookIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        pass

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_query_record(self):
        """Tests get_gradebook_column_query_record"""
        pass


class TestGradebookColumnSummaryQuery(unittest.TestCase):
    """Tests for GradebookColumnSummaryQuery"""

    @unittest.skip('unimplemented test')
    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_mean(self):
        """Tests match_mean"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_mean_terms(self):
        """Tests clear_mean_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_mean(self):
        """Tests match_minimum_mean"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_mean_terms(self):
        """Tests clear_minimum_mean_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_median(self):
        """Tests match_median"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_median_terms(self):
        """Tests clear_median_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_median(self):
        """Tests match_minimum_median"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_median_terms(self):
        """Tests clear_minimum_median_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_mode(self):
        """Tests match_mode"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_mode_terms(self):
        """Tests clear_mode_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_mode(self):
        """Tests match_minimum_mode"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_mode_terms(self):
        """Tests clear_minimum_mode_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_rms(self):
        """Tests match_rms"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rms_terms(self):
        """Tests clear_rms_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_rms(self):
        """Tests match_minimum_rms"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_rms_terms(self):
        """Tests clear_minimum_rms_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_standard_deviation(self):
        """Tests match_standard_deviation"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_standard_deviation_terms(self):
        """Tests clear_standard_deviation_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_standard_deviation(self):
        """Tests match_minimum_standard_deviation"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_standard_deviation_terms(self):
        """Tests clear_minimum_standard_deviation_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_sum(self):
        """Tests match_sum"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_sum_terms(self):
        """Tests clear_sum_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_sum(self):
        """Tests match_minimum_sum"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_sum_terms(self):
        """Tests clear_minimum_sum_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_summary_query_record(self):
        """Tests get_gradebook_column_summary_query_record"""
        pass


class TestGradebookQuery(unittest.TestCase):
    """Tests for GradebookQuery"""

    @unittest.skip('unimplemented test')
    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_system_id_terms(self):
        """Tests clear_grade_system_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade_system(self):
        """Tests match_any_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_gradebook_id(self):
        """Tests match_ancestor_gradebook_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_gradebook_id_terms(self):
        """Tests clear_ancestor_gradebook_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_gradebook_query(self):
        """Tests supports_ancestor_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_gradebook_query(self):
        """Tests get_ancestor_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_gradebook(self):
        """Tests match_any_ancestor_gradebook"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_gradebook_terms(self):
        """Tests clear_ancestor_gradebook_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_gradebook_id(self):
        """Tests match_descendant_gradebook_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_gradebook_id_terms(self):
        """Tests clear_descendant_gradebook_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_gradebook_query(self):
        """Tests supports_descendant_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_gradebook_query(self):
        """Tests get_descendant_gradebook_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_gradebook(self):
        """Tests match_any_descendant_gradebook"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_gradebook_terms(self):
        """Tests clear_descendant_gradebook_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_gradebook_query_record(self):
        """Tests get_gradebook_query_record"""
        pass
