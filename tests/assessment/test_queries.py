"""Unit tests of assessment queries."""


import unittest


from dlkit.abstract_osid.osid import errors
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

        item_query = cls.catalog.get_item_query()
        # cls.query = item_query.get_question_query()
        # Currently raises Unsupported()

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_question_query_record(self):
        """Tests get_question_query_record"""
        pass


class TestAnswerQuery(unittest.TestCase):
    """Tests for AnswerQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_query = cls.catalog.get_item_query()
        # cls.query = item_query.get_answer_query()
        # Currently raises Unsupported()

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_answer_query_record(self):
        """Tests get_answer_query_record"""
        pass


class TestItemQuery(unittest.TestCase):
    """Tests for ItemQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        cls.query = cls.catalog.get_item_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_learning_objective_id(self):
        """Tests match_learning_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_learning_objective_id_terms(self):
        """Tests clear_learning_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_learning_objective_query(self):
        """Tests supports_learning_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_learning_objective_query(self):
        """Tests get_learning_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_learning_objective(self):
        """Tests match_any_learning_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_learning_objective_terms(self):
        """Tests clear_learning_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_question_id(self):
        """Tests match_question_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_question_id_terms(self):
        """Tests clear_question_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_question_query(self):
        """Tests supports_question_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question_query(self):
        """Tests get_question_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_question(self):
        """Tests match_any_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_question_terms(self):
        """Tests clear_question_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_answer_id(self):
        """Tests match_answer_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_answer_id_terms(self):
        """Tests clear_answer_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_answer_query(self):
        """Tests supports_answer_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answer_query(self):
        """Tests get_answer_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_answer(self):
        """Tests match_any_answer"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_answer_terms(self):
        """Tests clear_answer_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_bank_id(self):
        """Tests match_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_query_record(self):
        """Tests get_item_query_record"""
        pass


class TestAssessmentQuery(unittest.TestCase):
    """Tests for AssessmentQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        cls.query = cls.catalog.get_assessment_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_level_id(self):
        """Tests match_level_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_level_query(self):
        """Tests supports_level_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_level_query(self):
        """Tests get_level_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_level(self):
        """Tests match_any_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_item_id(self):
        """Tests match_item_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_item_id_terms(self):
        """Tests clear_item_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_item_query(self):
        """Tests supports_item_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_query(self):
        """Tests get_item_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_item(self):
        """Tests match_any_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_item_terms(self):
        """Tests clear_item_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment_offered(self):
        """Tests match_any_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_taken_id(self):
        """Tests match_assessment_taken_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_taken_id_terms(self):
        """Tests clear_assessment_taken_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment_taken(self):
        """Tests match_any_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_taken_terms(self):
        """Tests clear_assessment_taken_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_bank_id(self):
        """Tests match_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query_record(self):
        """Tests get_assessment_query_record"""
        pass


class TestAssessmentOfferedQuery(unittest.TestCase):
    """Tests for AssessmentOfferedQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        cls.query = cls.catalog.get_assessment_offered_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_level_id(self):
        """Tests match_level_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_level_query(self):
        """Tests supports_level_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_level_query(self):
        """Tests get_level_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_level(self):
        """Tests match_any_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_items_sequential(self):
        """Tests match_items_sequential"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_items_sequential_terms(self):
        """Tests clear_items_sequential_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_items_shuffled(self):
        """Tests match_items_shuffled"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_items_shuffled_terms(self):
        """Tests clear_items_shuffled_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_start_time(self):
        """Tests match_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_start_time(self):
        """Tests match_any_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_start_time_terms(self):
        """Tests clear_start_time_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_deadline(self):
        """Tests match_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_deadline(self):
        """Tests match_any_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_deadline_terms(self):
        """Tests clear_deadline_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_duration(self):
        """Tests match_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_duration(self):
        """Tests match_any_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_duration_terms(self):
        """Tests clear_duration_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_score_system_id(self):
        """Tests match_score_system_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score_system_id_terms(self):
        """Tests clear_score_system_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_score_system_query(self):
        """Tests supports_score_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_score_system_query(self):
        """Tests get_score_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_score_system(self):
        """Tests match_any_score_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score_system_terms(self):
        """Tests clear_score_system_terms"""
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
    def test_match_any_grade_system(self):
        """Tests match_any_grade_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_system_terms(self):
        """Tests clear_grade_system_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_taken_id(self):
        """Tests match_assessment_taken_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_taken_id_terms(self):
        """Tests clear_assessment_taken_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_taken_query(self):
        """Tests supports_assessment_taken_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment_taken(self):
        """Tests match_any_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_taken_terms(self):
        """Tests clear_assessment_taken_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_bank_id(self):
        """Tests match_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_query_record(self):
        """Tests get_assessment_offered_query_record"""
        pass


class TestAssessmentTakenQuery(unittest.TestCase):
    """Tests for AssessmentTakenQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        cls.query = cls.catalog.get_assessment_taken_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_taker_id(self):
        """Tests match_taker_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_taker_id_terms(self):
        """Tests clear_taker_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_taker_query(self):
        """Tests supports_taker_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taker_query(self):
        """Tests get_taker_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_taker_terms(self):
        """Tests clear_taker_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_taking_agent_id(self):
        """Tests match_taking_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_taking_agent_id_terms(self):
        """Tests clear_taking_agent_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_taking_agent_query(self):
        """Tests supports_taking_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taking_agent_query(self):
        """Tests get_taking_agent_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_taking_agent_terms(self):
        """Tests clear_taking_agent_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_actual_start_time(self):
        """Tests match_actual_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_actual_start_time(self):
        """Tests match_any_actual_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_actual_start_time_terms(self):
        """Tests clear_actual_start_time_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_completion_time(self):
        """Tests match_completion_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_completion_time(self):
        """Tests match_any_completion_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_completion_time_terms(self):
        """Tests clear_completion_time_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_time_spent(self):
        """Tests match_time_spent"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_time_spent_terms(self):
        """Tests clear_time_spent_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_score_system_id(self):
        """Tests match_score_system_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score_system_id_terms(self):
        """Tests clear_score_system_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_score_system_query(self):
        """Tests supports_score_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_score_system_query(self):
        """Tests get_score_system_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_score_system(self):
        """Tests match_any_score_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score_system_terms(self):
        """Tests clear_score_system_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_score(self):
        """Tests match_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_score(self):
        """Tests match_any_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score_terms(self):
        """Tests clear_score_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_grade_id(self):
        """Tests match_grade_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_grade_id_terms(self):
        """Tests clear_grade_id_terms"""
        pass

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
    def test_match_feedback(self):
        """Tests match_feedback"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_feedback(self):
        """Tests match_any_feedback"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_feedback_terms(self):
        """Tests clear_feedback_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_rubric_id(self):
        """Tests match_rubric_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric_id_terms(self):
        """Tests clear_rubric_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_rubric_query(self):
        """Tests supports_rubric_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rubric_query(self):
        """Tests get_rubric_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_rubric(self):
        """Tests match_any_rubric"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric_terms(self):
        """Tests clear_rubric_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_bank_id(self):
        """Tests match_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_query_record(self):
        """Tests get_assessment_taken_query_record"""
        pass


class TestBankQuery(unittest.TestCase):
    """Tests for BankQuery"""

    @unittest.skip('unimplemented test')
    def test_match_item_id(self):
        """Tests match_item_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_item_id_terms(self):
        """Tests clear_item_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_item_query(self):
        """Tests supports_item_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_query(self):
        """Tests get_item_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_item(self):
        """Tests match_any_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_item_terms(self):
        """Tests clear_item_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_offered_id(self):
        """Tests match_assessment_offered_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_offered_id_terms(self):
        """Tests clear_assessment_offered_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_offered_query(self):
        """Tests supports_assessment_offered_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment_offered(self):
        """Tests match_any_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_offered_terms(self):
        """Tests clear_assessment_offered_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_bank_id(self):
        """Tests match_ancestor_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_bank_id_terms(self):
        """Tests clear_ancestor_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_bank_query(self):
        """Tests supports_ancestor_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_bank_query(self):
        """Tests get_ancestor_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_bank(self):
        """Tests match_any_ancestor_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_bank_terms(self):
        """Tests clear_ancestor_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_bank_id(self):
        """Tests match_descendant_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_bank_id_terms(self):
        """Tests clear_descendant_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_bank_query(self):
        """Tests supports_descendant_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_bank_query(self):
        """Tests get_descendant_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_bank(self):
        """Tests match_any_descendant_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_bank_terms(self):
        """Tests clear_descendant_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query_record(self):
        """Tests get_bank_query_record"""
        pass
