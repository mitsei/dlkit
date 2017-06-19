"""Unit tests of grading queries."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.grading.queries import GradeQuery
from dlkit.json_.grading.queries import GradebookColumnSummaryQuery
from dlkit.json_.grading.queries import GradebookQuery
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

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)

    def setUp(self):
        # Since the session isn't implemented, we just construct an ActivityQuery directly
        self.query = GradeQuery(runtime=self.catalog._runtime)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('gradeSystemId', self.query._query_terms)
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

    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_system_query()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_system_query()

    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradeSystem'] = 'foo'
        self.query.clear_grade_system_terms()
        self.assertNotIn('gradeSystem',
                         self.query._query_terms)

    def test_match_input_score_start_range(self):
        """Tests match_input_score_start_range"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_input_score_start_range(True, True, True)

    def test_clear_input_score_start_range_terms(self):
        """Tests clear_input_score_start_range_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['inputScoreStartRange'] = 'foo'
        self.query.clear_input_score_start_range_terms()
        self.assertNotIn('inputScoreStartRange',
                         self.query._query_terms)

    def test_match_input_score_end_range(self):
        """Tests match_input_score_end_range"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_input_score_end_range(True, True, True)

    def test_clear_input_score_end_range_terms(self):
        """Tests clear_input_score_end_range_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['inputScoreEndRange'] = 'foo'
        self.query.clear_input_score_end_range_terms()
        self.assertNotIn('inputScoreEndRange',
                         self.query._query_terms)

    def test_match_input_score(self):
        """Tests match_input_score"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_input_score(True, True, True)

    def test_clear_input_score_terms(self):
        """Tests clear_input_score_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_input_score_terms()

    def test_match_output_score(self):
        """Tests match_output_score"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_output_score(True, True, True)

    def test_clear_output_score_terms(self):
        """Tests clear_output_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['outputScore'] = 'foo'
        self.query.clear_output_score_terms()
        self.assertNotIn('outputScore',
                         self.query._query_terms)

    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('gradeEntryId', self.query._query_terms)
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

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_entry_query()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_entry_query()

    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade_entry(True)

    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_grade_entry_terms()

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

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    def test_get_grade_query_record(self):
        """Tests get_grade_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_query_record(True)


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

    def test_match_based_on_grades(self):
        """Tests match_based_on_grades"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_based_on_grades(True)

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
        self.assertNotIn('gradeId', self.query._query_terms)
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

    def test_supports_grade_query(self):
        """Tests supports_grade_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_query()

    def test_get_grade_query(self):
        """Tests get_grade_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_query()

    def test_match_any_grade(self):
        """Tests match_any_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade(True)

    def test_clear_grade_terms(self):
        """Tests clear_grade_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_grade_terms()

    def test_match_lowest_numeric_score(self):
        """Tests match_lowest_numeric_score"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_lowest_numeric_score(True, True, True)

    def test_clear_lowest_numeric_score_terms(self):
        """Tests clear_lowest_numeric_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['lowestNumericScore'] = 'foo'
        self.query.clear_lowest_numeric_score_terms()
        self.assertNotIn('lowestNumericScore',
                         self.query._query_terms)

    def test_match_numeric_score_increment(self):
        """Tests match_numeric_score_increment"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_numeric_score_increment(True, True, True)

    def test_clear_numeric_score_increment_terms(self):
        """Tests clear_numeric_score_increment_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['numericScoreIncrement'] = 'foo'
        self.query.clear_numeric_score_increment_terms()
        self.assertNotIn('numericScoreIncrement',
                         self.query._query_terms)

    def test_match_highest_numeric_score(self):
        """Tests match_highest_numeric_score"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_highest_numeric_score(True, True, True)

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
        self.assertNotIn('gradebookColumnId', self.query._query_terms)
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

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_query()

    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_gradebook_column(True)

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_gradebook_column_terms()

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

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    def test_get_grade_system_query_record(self):
        """Tests get_grade_system_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_system_query_record(True)


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
        self.assertNotIn('gradebookColumnId', self.query._query_terms)
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

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_query()

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
        self.assertNotIn('keyResourceId', self.query._query_terms)
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

    def test_supports_key_resource_query(self):
        """Tests supports_key_resource_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_key_resource_query()

    def test_get_key_resource_query(self):
        """Tests get_key_resource_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_key_resource_query()

    def test_match_any_key_resource(self):
        """Tests match_any_key_resource"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_key_resource(True)

    def test_clear_key_resource_terms(self):
        """Tests clear_key_resource_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_key_resource_terms()

    def test_match_derived(self):
        """Tests match_derived"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_derived(True)

    def test_clear_derived_terms(self):
        """Tests clear_derived_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_derived_terms()

    def test_match_overridden_grade_entry_id(self):
        """Tests match_overridden_grade_entry_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('overriddenGradeEntryId', self.query._query_terms)
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

    def test_supports_overridden_grade_entry_query(self):
        """Tests supports_overridden_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_overridden_grade_entry_query()

    def test_get_overridden_grade_entry_query(self):
        """Tests get_overridden_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_overridden_grade_entry_query()

    def test_match_any_overridden_grade_entry(self):
        """Tests match_any_overridden_grade_entry"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_overridden_grade_entry(True)

    def test_clear_overridden_grade_entry_terms(self):
        """Tests clear_overridden_grade_entry_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_overridden_grade_entry_terms()

    def test_match_ignored_for_calculations(self):
        """Tests match_ignored_for_calculations"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_ignored_for_calculations(True)

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
        self.assertNotIn('gradeId', self.query._query_terms)
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

    def test_supports_grade_query(self):
        """Tests supports_grade_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_query()

    def test_get_grade_query(self):
        """Tests get_grade_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_query()

    def test_match_any_grade(self):
        """Tests match_any_grade"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade(True)

    def test_clear_grade_terms(self):
        """Tests clear_grade_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['grade'] = 'foo'
        self.query.clear_grade_terms()
        self.assertNotIn('grade',
                         self.query._query_terms)

    def test_match_score(self):
        """Tests match_score"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_score(True, True, True)

    def test_match_any_score(self):
        """Tests match_any_score"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_score(True)

    def test_clear_score_terms(self):
        """Tests clear_score_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['score'] = 'foo'
        self.query.clear_score_terms()
        self.assertNotIn('score',
                         self.query._query_terms)

    def test_match_time_graded(self):
        """Tests match_time_graded"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_time_graded(True, True, True)

    def test_clear_time_graded_terms(self):
        """Tests clear_time_graded_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_time_graded_terms()

    def test_match_grader_id(self):
        """Tests match_grader_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('graderId', self.query._query_terms)
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

    def test_supports_grader_query(self):
        """Tests supports_grader_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grader_query()

    def test_get_grader_query(self):
        """Tests get_grader_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grader_query()

    def test_match_any_grader(self):
        """Tests match_any_grader"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grader(True)

    def test_clear_grader_terms(self):
        """Tests clear_grader_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_grader_terms()

    def test_match_grading_agent_id(self):
        """Tests match_grading_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('gradingAgentId', self.query._query_terms)
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

    def test_supports_grading_agent_query(self):
        """Tests supports_grading_agent_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grading_agent_query()

    def test_get_grading_agent_query(self):
        """Tests get_grading_agent_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grading_agent_query()

    def test_match_any_grading_agent(self):
        """Tests match_any_grading_agent"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grading_agent(True)

    def test_clear_grading_agent_terms(self):
        """Tests clear_grading_agent_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_grading_agent_terms()

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

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    def test_get_grade_entry_query_record(self):
        """Tests get_grade_entry_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_entry_query_record(True)


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
        self.assertNotIn('gradeSystemId', self.query._query_terms)
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

    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_system_query()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_system_query()

    def test_match_any_grade_system(self):
        """Tests match_any_grade_system"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade_system(True)

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
        self.assertNotIn('gradeEntryId', self.query._query_terms)
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

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_entry_query()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_entry_query()

    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade_entry(True)

    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_grade_entry_terms()

    def test_supports_gradebook_column_summary_query(self):
        """Tests supports_gradebook_column_summary_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_column_summary_query()

    def test_get_gradebook_column_summary_query(self):
        """Tests get_gradebook_column_summary_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_summary_query()

    def test_clear_gradebook_column_summary_terms(self):
        """Tests clear_gradebook_column_summary_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_gradebook_column_summary_terms()

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

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['gradebook'] = 'foo'
        self.query.clear_gradebook_terms()
        self.assertNotIn('gradebook',
                         self.query._query_terms)

    def test_get_gradebook_column_query_record(self):
        """Tests get_gradebook_column_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_query_record(True)


class TestGradebookColumnSummaryQuery(unittest.TestCase):
    """Tests for GradebookColumnSummaryQuery"""

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

    def setUp(self):
        # Since the session isn't implemented, we just construct a GradebookColumnSummaryQuery directly
        self.query = GradebookColumnSummaryQuery(runtime=self.catalog._runtime)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_grade_entries():
            cls.catalog.delete_grade_entry(obj.ident)
        for obj in cls.catalog.get_gradebook_columns():
            cls.catalog.delete_gradebook_column(obj.ident)
        for obj in cls.catalog.get_grade_systems():
            cls.catalog.delete_grade_system(obj.ident)
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_gradebook_column_id(True, True)

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_gradebook_column_id_terms()

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_query()

    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_gradebook_column(True)

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_gradebook_column_terms()

    def test_match_mean(self):
        """Tests match_mean"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_mean(True, True, True)

    def test_clear_mean_terms(self):
        """Tests clear_mean_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_mean_terms()

    def test_match_minimum_mean(self):
        """Tests match_minimum_mean"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_minimum_mean(True, True)

    def test_clear_minimum_mean_terms(self):
        """Tests clear_minimum_mean_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_minimum_mean_terms()

    def test_match_median(self):
        """Tests match_median"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_median(True, True, True)

    def test_clear_median_terms(self):
        """Tests clear_median_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_median_terms()

    def test_match_minimum_median(self):
        """Tests match_minimum_median"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_minimum_median(True, True)

    def test_clear_minimum_median_terms(self):
        """Tests clear_minimum_median_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_minimum_median_terms()

    def test_match_mode(self):
        """Tests match_mode"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_mode(True, True, True)

    def test_clear_mode_terms(self):
        """Tests clear_mode_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_mode_terms()

    def test_match_minimum_mode(self):
        """Tests match_minimum_mode"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_minimum_mode(True, True)

    def test_clear_minimum_mode_terms(self):
        """Tests clear_minimum_mode_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_minimum_mode_terms()

    def test_match_rms(self):
        """Tests match_rms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_rms(True, True, True)

    def test_clear_rms_terms(self):
        """Tests clear_rms_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_rms_terms()

    def test_match_minimum_rms(self):
        """Tests match_minimum_rms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_minimum_rms(True, True)

    def test_clear_minimum_rms_terms(self):
        """Tests clear_minimum_rms_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_minimum_rms_terms()

    def test_match_standard_deviation(self):
        """Tests match_standard_deviation"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_standard_deviation(True, True, True)

    def test_clear_standard_deviation_terms(self):
        """Tests clear_standard_deviation_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_standard_deviation_terms()

    def test_match_minimum_standard_deviation(self):
        """Tests match_minimum_standard_deviation"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_minimum_standard_deviation(True, True)

    def test_clear_minimum_standard_deviation_terms(self):
        """Tests clear_minimum_standard_deviation_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_minimum_standard_deviation_terms()

    def test_match_sum(self):
        """Tests match_sum"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_sum(True, True, True)

    def test_clear_sum_terms(self):
        """Tests clear_sum_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_sum_terms()

    def test_match_minimum_sum(self):
        """Tests match_minimum_sum"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_minimum_sum(True, True)

    def test_clear_minimum_sum_terms(self):
        """Tests clear_minimum_sum_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_minimum_sum_terms()

    def test_match_gradebook_id(self):
        """Tests match_gradebook_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_gradebook_id(True, True)

    def test_clear_gradebook_id_terms(self):
        """Tests clear_gradebook_id_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_gradebook_id_terms()

    def test_supports_gradebook_query(self):
        """Tests supports_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_query()

    def test_get_gradebook_query(self):
        """Tests get_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_query()

    def test_clear_gradebook_terms(self):
        """Tests clear_gradebook_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_gradebook_terms()

    def test_get_gradebook_column_summary_query_record(self):
        """Tests get_gradebook_column_summary_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_summary_query_record(True)


class TestGradebookQuery(unittest.TestCase):
    """Tests for GradebookQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def setUp(self):
        # Since the session isn't implemented, we just construct a GradebookQuery directly
        self.query = GradebookQuery(runtime=self.catalog._runtime)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_gradebook(cls.catalog.ident)

    def test_match_grade_system_id(self):
        """Tests match_grade_system_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_grade_system_id(True, True)

    def test_clear_grade_system_id_terms(self):
        """Tests clear_grade_system_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['gradeSystemId'] = 'foo'
        self.query.clear_grade_system_id_terms()
        self.assertNotIn('gradeSystemId',
                         self.query._query_terms)

    def test_supports_grade_system_query(self):
        """Tests supports_grade_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_system_query()

    def test_get_grade_system_query(self):
        """Tests get_grade_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_system_query()

    def test_match_any_grade_system(self):
        """Tests match_any_grade_system"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade_system(True)

    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['gradeSystem'] = 'foo'
        self.query.clear_grade_system_terms()
        self.assertNotIn('gradeSystem',
                         self.query._query_terms)

    def test_match_grade_entry_id(self):
        """Tests match_grade_entry_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_grade_entry_id(True, True)

    def test_clear_grade_entry_id_terms(self):
        """Tests clear_grade_entry_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['gradeEntryId'] = 'foo'
        self.query.clear_grade_entry_id_terms()
        self.assertNotIn('gradeEntryId',
                         self.query._query_terms)

    def test_supports_grade_entry_query(self):
        """Tests supports_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_grade_entry_query()

    def test_get_grade_entry_query(self):
        """Tests get_grade_entry_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_grade_entry_query()

    def test_match_any_grade_entry(self):
        """Tests match_any_grade_entry"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_grade_entry(True)

    def test_clear_grade_entry_terms(self):
        """Tests clear_grade_entry_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['gradeEntry'] = 'foo'
        self.query.clear_grade_entry_terms()
        self.assertNotIn('gradeEntry',
                         self.query._query_terms)

    def test_match_gradebook_column_id(self):
        """Tests match_gradebook_column_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_gradebook_column_id(True, True)

    def test_clear_gradebook_column_id_terms(self):
        """Tests clear_gradebook_column_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['gradebookColumnId'] = 'foo'
        self.query.clear_gradebook_column_id_terms()
        self.assertNotIn('gradebookColumnId',
                         self.query._query_terms)

    def test_supports_gradebook_column_query(self):
        """Tests supports_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_gradebook_column_query()

    def test_get_gradebook_column_query(self):
        """Tests get_gradebook_column_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_column_query()

    def test_match_any_gradebook_column(self):
        """Tests match_any_gradebook_column"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_gradebook_column(True)

    def test_clear_gradebook_column_terms(self):
        """Tests clear_gradebook_column_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['gradebookColumn'] = 'foo'
        self.query.clear_gradebook_column_terms()
        self.assertNotIn('gradebookColumn',
                         self.query._query_terms)

    def test_match_ancestor_gradebook_id(self):
        """Tests match_ancestor_gradebook_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_ancestor_gradebook_id(True, True)

    def test_clear_ancestor_gradebook_id_terms(self):
        """Tests clear_ancestor_gradebook_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['ancestorGradebookId'] = 'foo'
        self.query.clear_ancestor_gradebook_id_terms()
        self.assertNotIn('ancestorGradebookId',
                         self.query._query_terms)

    def test_supports_ancestor_gradebook_query(self):
        """Tests supports_ancestor_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_ancestor_gradebook_query()

    def test_get_ancestor_gradebook_query(self):
        """Tests get_ancestor_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_ancestor_gradebook_query()

    def test_match_any_ancestor_gradebook(self):
        """Tests match_any_ancestor_gradebook"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_ancestor_gradebook(True)

    def test_clear_ancestor_gradebook_terms(self):
        """Tests clear_ancestor_gradebook_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['ancestorGradebook'] = 'foo'
        self.query.clear_ancestor_gradebook_terms()
        self.assertNotIn('ancestorGradebook',
                         self.query._query_terms)

    def test_match_descendant_gradebook_id(self):
        """Tests match_descendant_gradebook_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_descendant_gradebook_id(True, True)

    def test_clear_descendant_gradebook_id_terms(self):
        """Tests clear_descendant_gradebook_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['descendantGradebookId'] = 'foo'
        self.query.clear_descendant_gradebook_id_terms()
        self.assertNotIn('descendantGradebookId',
                         self.query._query_terms)

    def test_supports_descendant_gradebook_query(self):
        """Tests supports_descendant_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_descendant_gradebook_query()

    def test_get_descendant_gradebook_query(self):
        """Tests get_descendant_gradebook_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_descendant_gradebook_query()

    def test_match_any_descendant_gradebook(self):
        """Tests match_any_descendant_gradebook"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_descendant_gradebook(True)

    def test_clear_descendant_gradebook_terms(self):
        """Tests clear_descendant_gradebook_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['descendantGradebook'] = 'foo'
        self.query.clear_descendant_gradebook_terms()
        self.assertNotIn('descendantGradebook',
                         self.query._query_terms)

    def test_get_gradebook_query_record(self):
        """Tests get_gradebook_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_gradebook_query_record(True)
