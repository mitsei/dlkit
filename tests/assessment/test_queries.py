"""Unit tests of assessment queries."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.assessment.queries import AnswerQuery
from dlkit.json_.assessment.queries import QuestionQuery
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestQuestionQuery(unittest.TestCase):
    """Tests for QuestionQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # Since the session isn't implemented, we just construct a QuestionQuery directly
        self.query = QuestionQuery(runtime=self.catalog._runtime)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_question_query_record(self):
        """Tests get_question_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_question_query_record(True)


class TestAnswerQuery(unittest.TestCase):
    """Tests for AnswerQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # Since the session isn't implemented, we just construct a AnswerQuery directly
        self.query = AnswerQuery(runtime=self.catalog._runtime)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_answer_query_record(self):
        """Tests get_answer_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_answer_query_record(True)


class TestItemQuery(unittest.TestCase):
    """Tests for ItemQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_item_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_match_learning_objective_id(self):
        """Tests match_learning_objective_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('learningObjectiveIds', self.query._query_terms)
        self.query.match_learning_objective_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['learningObjectiveIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_learning_objective_id_terms(self):
        """Tests clear_learning_objective_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_learning_objective_id(test_id, match=True)
        self.assertIn('learningObjectiveIds',
                      self.query._query_terms)
        self.query.clear_learning_objective_id_terms()
        self.assertNotIn('learningObjectiveIds',
                         self.query._query_terms)

    def test_supports_learning_objective_query(self):
        """Tests supports_learning_objective_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_learning_objective_query()

    def test_get_learning_objective_query(self):
        """Tests get_learning_objective_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_learning_objective_query()

    def test_match_any_learning_objective(self):
        """Tests match_any_learning_objective"""
        self.assertNotIn('learningObjectiveIds', self.query._query_terms)
        self.query.match_any_learning_objective(match=True)
        self.assertEqual(self.query._query_terms['learningObjectiveIds'], {
            '$exists': 'true',
            '$nin': [[], ['']]
        })

    def test_clear_learning_objective_terms(self):
        """Tests clear_learning_objective_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_any_learning_objective(match=True)
        self.assertIn('learningObjectiveIds',
                      self.query._query_terms)
        self.query.clear_learning_objective_terms()
        self.assertNotIn('learningObjectiveIds',
                         self.query._query_terms)

    def test_match_question_id(self):
        """Tests match_question_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('questionId', self.query._query_terms)
        self.query.match_question_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['questionId'], {
            '$in': [str(test_id)]
        })

    def test_clear_question_id_terms(self):
        """Tests clear_question_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_question_id(test_id, match=True)
        self.assertIn('questionId',
                      self.query._query_terms)
        self.query.clear_question_id_terms()
        self.assertNotIn('questionId',
                         self.query._query_terms)

    def test_supports_question_query(self):
        """Tests supports_question_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_question_query()

    def test_get_question_query(self):
        """Tests get_question_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_question_query()

    def test_match_any_question(self):
        """Tests match_any_question"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_question(True)

    def test_clear_question_terms(self):
        """Tests clear_question_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_question_terms()

    def test_match_answer_id(self):
        """Tests match_answer_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('answerId', self.query._query_terms)
        self.query.match_answer_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['answerId'], {
            '$in': [str(test_id)]
        })

    def test_clear_answer_id_terms(self):
        """Tests clear_answer_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_answer_id(test_id, match=True)
        self.assertIn('answerId',
                      self.query._query_terms)
        self.query.clear_answer_id_terms()
        self.assertNotIn('answerId',
                         self.query._query_terms)

    def test_supports_answer_query(self):
        """Tests supports_answer_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_answer_query()

    def test_get_answer_query(self):
        """Tests get_answer_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_answer_query()

    def test_match_any_answer(self):
        """Tests match_any_answer"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_answer(True)

    def test_clear_answer_terms(self):
        """Tests clear_answer_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_answer_terms()

    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('assessmentId', self.query._query_terms)
        self.query.match_assessment_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_id(test_id, match=True)
        self.assertIn('assessmentId',
                      self.query._query_terms)
        self.query.clear_assessment_id_terms()
        self.assertNotIn('assessmentId',
                         self.query._query_terms)

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_query()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_query()

    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_assessment(True)

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_assessment_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedBankIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertIn('assignedBankIds',
                      self.query._query_terms)
        self.query.clear_bank_id_terms()
        self.assertNotIn('assignedBankIds',
                         self.query._query_terms)

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        self.assertNotIn('bank',
                         self.query._query_terms)

    def test_get_item_query_record(self):
        """Tests get_item_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_item_query_record(True)


class TestAssessmentQuery(unittest.TestCase):
    """Tests for AssessmentQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_assessment_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_match_level_id(self):
        """Tests match_level_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('levelId', self.query._query_terms)
        self.query.match_level_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['levelId'], {
            '$in': [str(test_id)]
        })

    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_level_id(test_id, match=True)
        self.assertIn('levelId',
                      self.query._query_terms)
        self.query.clear_level_id_terms()
        self.assertNotIn('levelId',
                         self.query._query_terms)

    def test_supports_level_query(self):
        """Tests supports_level_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_level_query()

    def test_get_level_query(self):
        """Tests get_level_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_level_query()

    def test_match_any_level(self):
        """Tests match_any_level"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_level(True)

    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['level'] = 'foo'
        self.query.clear_level_terms()
        self.assertNotIn('level',
                         self.query._query_terms)

    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('rubricId', self.query._query_terms)
        self.query.match_rubric_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['rubricId'], {
            '$in': [str(test_id)]
        })

    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rubric_id(test_id, match=True)
        self.assertIn('rubricId',
                      self.query._query_terms)
        self.query.clear_rubric_id_terms()
        self.assertNotIn('rubricId',
                         self.query._query_terms)

    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_rubric_query()

    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_rubric_query()

    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_rubric(True)

    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['rubric'] = 'foo'
        self.query.clear_rubric_terms()
        self.assertNotIn('rubric',
                         self.query._query_terms)

    def test_match_item_id(self):
        """Tests match_item_id"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_item_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['itemIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_item_id_terms(self):
        """Tests clear_item_id_terms"""
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_item_id(test_id, match=True)
        self.assertIn('itemIds',
                      self.query._query_terms)
        self.query.clear_item_id_terms()
        self.assertNotIn('itemIds',
                         self.query._query_terms)

    def test_supports_item_query(self):
        """Tests supports_item_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_item_query()

    def test_get_item_query(self):
        """Tests get_item_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_item_query()

    def test_match_any_item(self):
        """Tests match_any_item"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_item(True)

    def test_clear_item_terms(self):
        """Tests clear_item_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_item_terms()

    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('assessmentOfferedId', self.query._query_terms)
        self.query.match_assessment_offered_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentOfferedId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_offered_id(test_id, match=True)
        self.assertIn('assessmentOfferedId',
                      self.query._query_terms)
        self.query.clear_assessment_offered_id_terms()
        self.assertNotIn('assessmentOfferedId',
                         self.query._query_terms)

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_offered_query()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_offered_query()

    def test_match_any_assessment_offered(self):
        """Tests match_any_assessment_offered"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_assessment_offered(True)

    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_assessment_offered_terms()

    def test_match_assessment_taken_id(self):
        """Tests match_assessment_taken_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('assessmentTakenId', self.query._query_terms)
        self.query.match_assessment_taken_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentTakenId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_taken_id_terms(self):
        """Tests clear_assessment_taken_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_taken_id(test_id, match=True)
        self.assertIn('assessmentTakenId',
                      self.query._query_terms)
        self.query.clear_assessment_taken_id_terms()
        self.assertNotIn('assessmentTakenId',
                         self.query._query_terms)

    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_taken_query()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_taken_query()

    def test_match_any_assessment_taken(self):
        """Tests match_any_assessment_taken"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_assessment_taken(True)

    def test_clear_assessment_taken_terms(self):
        """Tests clear_assessment_taken_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_assessment_taken_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedBankIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertIn('assignedBankIds',
                      self.query._query_terms)
        self.query.clear_bank_id_terms()
        self.assertNotIn('assignedBankIds',
                         self.query._query_terms)

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        self.assertNotIn('bank',
                         self.query._query_terms)

    def test_get_assessment_query_record(self):
        """Tests get_assessment_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_query_record(True)


class TestAssessmentOfferedQuery(unittest.TestCase):
    """Tests for AssessmentOfferedQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_assessment_offered_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('assessmentId', self.query._query_terms)
        self.query.match_assessment_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_id(test_id, match=True)
        self.assertIn('assessmentId',
                      self.query._query_terms)
        self.query.clear_assessment_id_terms()
        self.assertNotIn('assessmentId',
                         self.query._query_terms)

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_query()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_query()

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['assessment'] = 'foo'
        self.query.clear_assessment_terms()
        self.assertNotIn('assessment',
                         self.query._query_terms)

    def test_match_level_id(self):
        """Tests match_level_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('levelId', self.query._query_terms)
        self.query.match_level_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['levelId'], {
            '$in': [str(test_id)]
        })

    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_level_id(test_id, match=True)
        self.assertIn('levelId',
                      self.query._query_terms)
        self.query.clear_level_id_terms()
        self.assertNotIn('levelId',
                         self.query._query_terms)

    def test_supports_level_query(self):
        """Tests supports_level_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_level_query()

    def test_get_level_query(self):
        """Tests get_level_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_level_query()

    def test_match_any_level(self):
        """Tests match_any_level"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_level(True)

    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['level'] = 'foo'
        self.query.clear_level_terms()
        self.assertNotIn('level',
                         self.query._query_terms)

    def test_match_items_sequential(self):
        """Tests match_items_sequential"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_items_sequential(True)

    def test_clear_items_sequential_terms(self):
        """Tests clear_items_sequential_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['itemsSequential'] = 'foo'
        self.query.clear_items_sequential_terms()
        self.assertNotIn('itemsSequential',
                         self.query._query_terms)

    def test_match_items_shuffled(self):
        """Tests match_items_shuffled"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_items_shuffled(True)

    def test_clear_items_shuffled_terms(self):
        """Tests clear_items_shuffled_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['itemsShuffled'] = 'foo'
        self.query.clear_items_shuffled_terms()
        self.assertNotIn('itemsShuffled',
                         self.query._query_terms)

    def test_match_start_time(self):
        """Tests match_start_time"""
        pass

    def test_match_any_start_time(self):
        """Tests match_any_start_time"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_start_time(True)

    def test_clear_start_time_terms(self):
        """Tests clear_start_time_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['startTime'] = 'foo'
        self.query.clear_start_time_terms()
        self.assertNotIn('startTime',
                         self.query._query_terms)

    def test_match_deadline(self):
        """Tests match_deadline"""
        pass

    def test_match_any_deadline(self):
        """Tests match_any_deadline"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_deadline(True)

    def test_clear_deadline_terms(self):
        """Tests clear_deadline_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['deadline'] = 'foo'
        self.query.clear_deadline_terms()
        self.assertNotIn('deadline',
                         self.query._query_terms)

    def test_match_duration(self):
        """Tests match_duration"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_duration(True, True, True)

    def test_match_any_duration(self):
        """Tests match_any_duration"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_duration(True)

    def test_clear_duration_terms(self):
        """Tests clear_duration_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['duration'] = 'foo'
        self.query.clear_duration_terms()
        self.assertNotIn('duration',
                         self.query._query_terms)

    def test_match_score_system_id(self):
        """Tests match_score_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('scoreSystemId', self.query._query_terms)
        self.query.match_score_system_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['scoreSystemId'], {
            '$in': [str(test_id)]
        })

    def test_clear_score_system_id_terms(self):
        """Tests clear_score_system_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_score_system_id(test_id, match=True)
        self.assertIn('scoreSystemId',
                      self.query._query_terms)
        self.query.clear_score_system_id_terms()
        self.assertNotIn('scoreSystemId',
                         self.query._query_terms)

    def test_supports_score_system_query(self):
        """Tests supports_score_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_score_system_query()

    def test_get_score_system_query(self):
        """Tests get_score_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_score_system_query()

    def test_match_any_score_system(self):
        """Tests match_any_score_system"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_score_system(True)

    def test_clear_score_system_terms(self):
        """Tests clear_score_system_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['scoreSystem'] = 'foo'
        self.query.clear_score_system_terms()
        self.assertNotIn('scoreSystem',
                         self.query._query_terms)

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

    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('rubricId', self.query._query_terms)
        self.query.match_rubric_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['rubricId'], {
            '$in': [str(test_id)]
        })

    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rubric_id(test_id, match=True)
        self.assertIn('rubricId',
                      self.query._query_terms)
        self.query.clear_rubric_id_terms()
        self.assertNotIn('rubricId',
                         self.query._query_terms)

    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_rubric_query()

    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_rubric_query()

    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_rubric(True)

    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_rubric_terms()

    def test_match_assessment_taken_id(self):
        """Tests match_assessment_taken_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('assessmentTakenId', self.query._query_terms)
        self.query.match_assessment_taken_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentTakenId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_taken_id_terms(self):
        """Tests clear_assessment_taken_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_taken_id(test_id, match=True)
        self.assertIn('assessmentTakenId',
                      self.query._query_terms)
        self.query.clear_assessment_taken_id_terms()
        self.assertNotIn('assessmentTakenId',
                         self.query._query_terms)

    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_taken_query()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_taken_query()

    def test_match_any_assessment_taken(self):
        """Tests match_any_assessment_taken"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_assessment_taken(True)

    def test_clear_assessment_taken_terms(self):
        """Tests clear_assessment_taken_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_assessment_taken_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedBankIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertIn('assignedBankIds',
                      self.query._query_terms)
        self.query.clear_bank_id_terms()
        self.assertNotIn('assignedBankIds',
                         self.query._query_terms)

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        self.assertNotIn('bank',
                         self.query._query_terms)

    def test_get_assessment_offered_query_record(self):
        """Tests get_assessment_offered_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_offered_query_record(True)


class TestAssessmentTakenQuery(unittest.TestCase):
    """Tests for AssessmentTakenQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuery::init_template
        self.query = self.catalog.get_assessment_taken_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuery::init_template
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('assessmentOfferedId', self.query._query_terms)
        self.query.match_assessment_offered_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentOfferedId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_offered_id(test_id, match=True)
        self.assertIn('assessmentOfferedId',
                      self.query._query_terms)
        self.query.clear_assessment_offered_id_terms()
        self.assertNotIn('assessmentOfferedId',
                         self.query._query_terms)

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_offered_query()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_offered_query()

    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['assessmentOffered'] = 'foo'
        self.query.clear_assessment_offered_terms()
        self.assertNotIn('assessmentOffered',
                         self.query._query_terms)

    def test_match_taker_id(self):
        """Tests match_taker_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('takerId', self.query._query_terms)
        self.query.match_taker_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['takerId'], {
            '$in': [str(test_id)]
        })

    def test_clear_taker_id_terms(self):
        """Tests clear_taker_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_taker_id(test_id, match=True)
        self.assertIn('takerId',
                      self.query._query_terms)
        self.query.clear_taker_id_terms()
        self.assertNotIn('takerId',
                         self.query._query_terms)

    def test_supports_taker_query(self):
        """Tests supports_taker_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_taker_query()

    def test_get_taker_query(self):
        """Tests get_taker_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_taker_query()

    def test_clear_taker_terms(self):
        """Tests clear_taker_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['taker'] = 'foo'
        self.query.clear_taker_terms()
        self.assertNotIn('taker',
                         self.query._query_terms)

    def test_match_taking_agent_id(self):
        """Tests match_taking_agent_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('takingAgentId', self.query._query_terms)
        self.query.match_taking_agent_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['takingAgentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_taking_agent_id_terms(self):
        """Tests clear_taking_agent_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_taking_agent_id(test_id, match=True)
        self.assertIn('takingAgentId',
                      self.query._query_terms)
        self.query.clear_taking_agent_id_terms()
        self.assertNotIn('takingAgentId',
                         self.query._query_terms)

    def test_supports_taking_agent_query(self):
        """Tests supports_taking_agent_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_taking_agent_query()

    def test_get_taking_agent_query(self):
        """Tests get_taking_agent_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_taking_agent_query()

    def test_clear_taking_agent_terms(self):
        """Tests clear_taking_agent_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_taking_agent_terms()

    def test_match_actual_start_time(self):
        """Tests match_actual_start_time"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_actual_start_time(True, True, True)

    def test_match_any_actual_start_time(self):
        """Tests match_any_actual_start_time"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_actual_start_time(True)

    def test_clear_actual_start_time_terms(self):
        """Tests clear_actual_start_time_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_actual_start_time_terms()

    def test_match_completion_time(self):
        """Tests match_completion_time"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_completion_time(True, True, True)

    def test_match_any_completion_time(self):
        """Tests match_any_completion_time"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_completion_time(True)

    def test_clear_completion_time_terms(self):
        """Tests clear_completion_time_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_completion_time_terms()

    def test_match_time_spent(self):
        """Tests match_time_spent"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_time_spent(True, True, True)

    def test_clear_time_spent_terms(self):
        """Tests clear_time_spent_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_time_spent_terms()

    def test_match_score_system_id(self):
        """Tests match_score_system_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('scoreSystemId', self.query._query_terms)
        self.query.match_score_system_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['scoreSystemId'], {
            '$in': [str(test_id)]
        })

    def test_clear_score_system_id_terms(self):
        """Tests clear_score_system_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_score_system_id(test_id, match=True)
        self.assertIn('scoreSystemId',
                      self.query._query_terms)
        self.query.clear_score_system_id_terms()
        self.assertNotIn('scoreSystemId',
                         self.query._query_terms)

    def test_supports_score_system_query(self):
        """Tests supports_score_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_score_system_query()

    def test_get_score_system_query(self):
        """Tests get_score_system_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_score_system_query()

    def test_match_any_score_system(self):
        """Tests match_any_score_system"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_score_system(True)

    def test_clear_score_system_terms(self):
        """Tests clear_score_system_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_score_system_terms()

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
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_score_terms()

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

    def test_match_feedback(self):
        """Tests match_feedback"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_feedback(True, True, True)

    def test_match_any_feedback(self):
        """Tests match_any_feedback"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_feedback(True)

    def test_clear_feedback_terms(self):
        """Tests clear_feedback_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_feedback_terms()

    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.assertNotIn('rubricId', self.query._query_terms)
        self.query.match_rubric_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['rubricId'], {
            '$in': [str(test_id)]
        })

    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_rubric_id(test_id, match=True)
        self.assertIn('rubricId',
                      self.query._query_terms)
        self.query.clear_rubric_id_terms()
        self.assertNotIn('rubricId',
                         self.query._query_terms)

    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_rubric_query()

    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_rubric_query()

    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_rubric(True)

    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        with self.assertRaises(errors.Unimplemented):
            self.query.clear_rubric_terms()

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedBankIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertIn('assignedBankIds',
                      self.query._query_terms)
        self.query.clear_bank_id_terms()
        self.assertNotIn('assignedBankIds',
                         self.query._query_terms)

    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_bank_query()

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_bank_query()

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        self.assertNotIn('bank',
                         self.query._query_terms)

    def test_get_assessment_taken_query_record(self):
        """Tests get_assessment_taken_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_taken_query_record(True)


class TestBankQuery(unittest.TestCase):
    """Tests for BankQuery"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinQuery::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def setUp(self):
        # From test_templates/resource.py::BinQuery::init_template
        self.query = self.svc_mgr.get_bank_query()

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinQuery::init_template
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_match_item_id(self):
        """Tests match_item_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_item_id(True, True)

    def test_clear_item_id_terms(self):
        """Tests clear_item_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['itemId'] = 'foo'
        self.query.clear_item_id_terms()
        self.assertNotIn('itemId',
                         self.query._query_terms)

    def test_supports_item_query(self):
        """Tests supports_item_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_item_query()

    def test_get_item_query(self):
        """Tests get_item_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_item_query()

    def test_match_any_item(self):
        """Tests match_any_item"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_item(True)

    def test_clear_item_terms(self):
        """Tests clear_item_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['item'] = 'foo'
        self.query.clear_item_terms()
        self.assertNotIn('item',
                         self.query._query_terms)

    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_assessment_id(True, True)

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['assessmentId'] = 'foo'
        self.query.clear_assessment_id_terms()
        self.assertNotIn('assessmentId',
                         self.query._query_terms)

    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_query()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_query()

    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_assessment(True)

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['assessment'] = 'foo'
        self.query.clear_assessment_terms()
        self.assertNotIn('assessment',
                         self.query._query_terms)

    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_assessment_offered_id(True, True)

    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['assessmentOfferedId'] = 'foo'
        self.query.clear_assessment_offered_id_terms()
        self.assertNotIn('assessmentOfferedId',
                         self.query._query_terms)

    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_assessment_offered_query()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_assessment_offered_query()

    def test_match_any_assessment_offered(self):
        """Tests match_any_assessment_offered"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_assessment_offered(True)

    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['assessmentOffered'] = 'foo'
        self.query.clear_assessment_offered_terms()
        self.assertNotIn('assessmentOffered',
                         self.query._query_terms)

    def test_match_ancestor_bank_id(self):
        """Tests match_ancestor_bank_id"""
        self.assertNotIn('_id', self.query._query_terms)
        self.query.match_ancestor_bank_id(self.fake_id, True)
        self.assertEqual(self.query._query_terms['_id'], {
            '$in': []
        })

    def test_clear_ancestor_bank_id_terms(self):
        """Tests clear_ancestor_bank_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['ancestorBankId'] = 'foo'
        self.query.clear_ancestor_bank_id_terms()
        self.assertNotIn('ancestorBankId',
                         self.query._query_terms)

    def test_supports_ancestor_bank_query(self):
        """Tests supports_ancestor_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_ancestor_bank_query()

    def test_get_ancestor_bank_query(self):
        """Tests get_ancestor_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_ancestor_bank_query()

    def test_match_any_ancestor_bank(self):
        """Tests match_any_ancestor_bank"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_ancestor_bank(True)

    def test_clear_ancestor_bank_terms(self):
        """Tests clear_ancestor_bank_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['ancestorBank'] = 'foo'
        self.query.clear_ancestor_bank_terms()
        self.assertNotIn('ancestorBank',
                         self.query._query_terms)

    def test_match_descendant_bank_id(self):
        """Tests match_descendant_bank_id"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_descendant_bank_id(True, True)

    def test_clear_descendant_bank_id_terms(self):
        """Tests clear_descendant_bank_id_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['descendantBankId'] = 'foo'
        self.query.clear_descendant_bank_id_terms()
        self.assertNotIn('descendantBankId',
                         self.query._query_terms)

    def test_supports_descendant_bank_query(self):
        """Tests supports_descendant_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.supports_descendant_bank_query()

    def test_get_descendant_bank_query(self):
        """Tests get_descendant_bank_query"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_descendant_bank_query()

    def test_match_any_descendant_bank(self):
        """Tests match_any_descendant_bank"""
        with self.assertRaises(errors.Unimplemented):
            self.query.match_any_descendant_bank(True)

    def test_clear_descendant_bank_terms(self):
        """Tests clear_descendant_bank_terms"""
        # From test_templates/resource.py::BinQuery::clear_group_terms_template
        self.query._query_terms['descendantBank'] = 'foo'
        self.query.clear_descendant_bank_terms()
        self.assertNotIn('descendantBank',
                         self.query._query_terms)

    def test_get_bank_query_record(self):
        """Tests get_bank_query_record"""
        with self.assertRaises(errors.Unimplemented):
            self.query.get_bank_query_record(True)
