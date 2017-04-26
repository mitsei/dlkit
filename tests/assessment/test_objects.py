"""Unit tests of assessment objects."""


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


class TestQuestion(unittest.TestCase):
    """Tests for Question"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_form = cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        cls.item = cls.catalog.create_item(item_form)

        form = cls.catalog.get_question_form_for_create(cls.item.ident, [])
        form.display_name = 'Test question'
        cls.question = cls.catalog.create_question(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_question_record(self):
        """Tests get_question_record"""
        pass


class TestQuestionForm(unittest.TestCase):
    """Tests for QuestionForm"""

    @unittest.skip('unimplemented test')
    def test_get_question_form_record(self):
        """Tests get_question_form_record"""
        pass


class TestQuestionList(unittest.TestCase):
    """Tests for QuestionList"""

    @unittest.skip('unimplemented test')
    def test_get_next_question(self):
        """Tests get_next_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_questions(self):
        """Tests get_next_questions"""
        pass


class TestAnswer(unittest.TestCase):
    """Tests for Answer"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_form = cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        cls.item = cls.catalog.create_item(item_form)

        form = cls.catalog.get_answer_form_for_create(cls.item.ident, [])
        form.display_name = 'Test answer'
        cls.answer = cls.catalog.create_answer(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_answer_record(self):
        """Tests get_answer_record"""
        pass


class TestAnswerForm(unittest.TestCase):
    """Tests for AnswerForm"""

    @unittest.skip('unimplemented test')
    def test_get_answer_form_record(self):
        """Tests get_answer_form_record"""
        pass


class TestAnswerList(unittest.TestCase):
    """Tests for AnswerList"""

    @unittest.skip('unimplemented test')
    def test_get_next_answer(self):
        """Tests get_next_answer"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_answers(self):
        """Tests get_next_answers"""
        pass


class TestItem(unittest.TestCase):
    """Tests for Item"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_item_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_item(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_learning_objective_ids(self):
        """Tests get_learning_objective_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_learning_objectives(self):
        """Tests get_learning_objectives"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question_id(self):
        """Tests get_question_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question(self):
        """Tests get_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answer_ids(self):
        """Tests get_answer_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answers(self):
        """Tests get_answers"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_record(self):
        """Tests get_item_record"""
        pass

        pass


class TestItemForm(unittest.TestCase):
    """Tests for ItemForm"""

    @unittest.skip('unimplemented test')
    def test_get_learning_objectives_metadata(self):
        """Tests get_learning_objectives_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_learning_objectives(self):
        """Tests set_learning_objectives"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_learning_objectives(self):
        """Tests clear_learning_objectives"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_form_record(self):
        """Tests get_item_form_record"""
        pass


class TestItemList(unittest.TestCase):
    """Tests for ItemList"""

    @unittest.skip('unimplemented test')
    def test_get_next_item(self):
        """Tests get_next_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_items(self):
        """Tests get_next_items"""
        pass


class TestAssessment(unittest.TestCase):
    """Tests for Assessment"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_assessment(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_level_id(self):
        """Tests get_level_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level_id)

    def test_get_level(self):
        """Tests get_level"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # From test_templates/resources.py::Resource::has_avatar_template
        self.assertTrue(isinstance(self.object.has_rubric(), bool))
        self.assertFalse(self.object.has_rubric())

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_rubric)

    @unittest.skip('unimplemented test')
    def test_get_assessment_record(self):
        """Tests get_assessment_record"""
        pass


class TestAssessmentForm(unittest.TestCase):
    """Tests for AssessmentForm"""

    @unittest.skip('unimplemented test')
    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_level(self):
        """Tests set_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level(self):
        """Tests clear_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_rubric_metadata(self):
        """Tests get_rubric_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_rubric(self):
        """Tests set_rubric"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_rubric(self):
        """Tests clear_rubric"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_form_record(self):
        """Tests get_assessment_form_record"""
        pass


class TestAssessmentList(unittest.TestCase):
    """Tests for AssessmentList"""

    @unittest.skip('unimplemented test')
    def test_get_next_assessment(self):
        """Tests get_next_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessments(self):
        """Tests get_next_assessments"""
        pass


class TestAssessmentOffered(unittest.TestCase):
    """Tests for AssessmentOffered"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Assessment'
        cls.assessment = cls.catalog.create_assessment(form)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        cls.object = cls.catalog.create_assessment_offered(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment(self):
        """Tests get_assessment"""
        pass

    def test_get_level_id(self):
        """Tests get_level_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level_id)

    def test_get_level(self):
        """Tests get_level"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level)

    def test_are_items_sequential(self):
        """Tests are_items_sequential"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.are_items_sequential(), bool))
        self.assertFalse(self.object.are_items_sequential())

    def test_are_items_shuffled(self):
        """Tests are_items_shuffled"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.are_items_shuffled(), bool))
        self.assertFalse(self.object.are_items_shuffled())

    @unittest.skip('unimplemented test')
    def test_has_start_time(self):
        """Tests has_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_start_time(self):
        """Tests get_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_deadline(self):
        """Tests has_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_deadline(self):
        """Tests get_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_duration(self):
        """Tests has_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_duration(self):
        """Tests get_duration"""
        pass

    def test_is_scored(self):
        """Tests is_scored"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scored?
        self.assertRaises(KeyError,
                          self.object.is_scored)

    def test_get_score_system_id(self):
        """Tests get_score_system_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_score_system_id)

    def test_get_score_system(self):
        """Tests get_score_system"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_score_system)

    def test_is_graded(self):
        """Tests is_graded"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set graded?
        self.assertRaises(KeyError,
                          self.object.is_graded)

    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade_system_id)

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade_system)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.has_rubric)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric)

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_record(self):
        """Tests get_assessment_offered_record"""
        pass

        pass


class TestAssessmentOfferedForm(unittest.TestCase):
    """Tests for AssessmentOfferedForm"""

    @unittest.skip('unimplemented test')
    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_level(self):
        """Tests set_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level(self):
        """Tests clear_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_sequential_metadata(self):
        """Tests get_items_sequential_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_items_sequential(self):
        """Tests set_items_sequential"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_items_sequential(self):
        """Tests clear_items_sequential"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_shuffled_metadata(self):
        """Tests get_items_shuffled_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_items_shuffled(self):
        """Tests set_items_shuffled"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_items_shuffled(self):
        """Tests clear_items_shuffled"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_start_time_metadata(self):
        """Tests get_start_time_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_start_time(self):
        """Tests set_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_start_time(self):
        """Tests clear_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_deadline_metadata(self):
        """Tests get_deadline_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_deadline(self):
        """Tests set_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_deadline(self):
        """Tests clear_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_duration_metadata(self):
        """Tests get_duration_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_duration(self):
        """Tests set_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_duration(self):
        """Tests clear_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_score_system_metadata(self):
        """Tests get_score_system_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_score_system(self):
        """Tests set_score_system"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_score_system(self):
        """Tests clear_score_system"""
        pass

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
    def test_get_assessment_offered_form_record(self):
        """Tests get_assessment_offered_form_record"""
        pass


class TestAssessmentOfferedList(unittest.TestCase):
    """Tests for AssessmentOfferedList"""

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_offered(self):
        """Tests get_next_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessments_offered(self):
        """Tests get_next_assessments_offered"""
        pass


class TestAssessmentTaken(unittest.TestCase):
    """Tests for AssessmentTaken"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Assessment'
        cls.assessment = cls.catalog.create_assessment(form)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        cls.offered = cls.catalog.create_assessment_offered(form)

        form = cls.catalog.get_assessment_taken_form_for_create(cls.offered.ident,
                                                                [])
        cls.object = cls.catalog.create_assessment_taken(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_id(self):
        """Tests get_assessment_offered_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered(self):
        """Tests get_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taker_id(self):
        """Tests get_taker_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taker(self):
        """Tests get_taker"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taking_agent_id(self):
        """Tests get_taking_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taking_agent(self):
        """Tests get_taking_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_started(self):
        """Tests has_started"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_actual_start_time(self):
        """Tests get_actual_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_ended(self):
        """Tests has_ended"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_completion_time(self):
        """Tests get_completion_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_time_spent(self):
        """Tests get_time_spent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_completion(self):
        """Tests get_completion"""
        pass

    def test_is_scored(self):
        """Tests is_scored"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scored?
        self.assertRaises(KeyError,
                          self.object.is_scored)

    def test_get_score_system_id(self):
        """Tests get_score_system_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scoreSystemId?
        self.assertRaises(KeyError,
                          self.object.get_score_system_id)

    def test_get_score_system(self):
        """Tests get_score_system"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scoreSystemId?
        self.assertRaises(KeyError,
                          self.object.get_score_system)

    @unittest.skip('unimplemented test')
    def test_get_score(self):
        """Tests get_score"""
        pass

    def test_is_graded(self):
        """Tests is_graded"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set graded?
        self.assertRaises(KeyError,
                          self.object.is_graded)

    def test_get_grade_id(self):
        """Tests get_grade_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade_id)

    def test_get_grade(self):
        """Tests get_grade"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade)

    @unittest.skip('unimplemented test')
    def test_get_feedback(self):
        """Tests get_feedback"""
        pass

    def test_has_rubric(self):
        """Tests has_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.has_rubric)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric)

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_record(self):
        """Tests get_assessment_taken_record"""
        pass


class TestAssessmentTakenForm(unittest.TestCase):
    """Tests for AssessmentTakenForm"""

    @unittest.skip('unimplemented test')
    def test_get_taker_metadata(self):
        """Tests get_taker_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_taker(self):
        """Tests set_taker"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_taker(self):
        """Tests clear_taker"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_form_record(self):
        """Tests get_assessment_taken_form_record"""
        pass


class TestAssessmentTakenList(unittest.TestCase):
    """Tests for AssessmentTakenList"""

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_taken(self):
        """Tests get_next_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessments_taken(self):
        """Tests get_next_assessments_taken"""
        pass


class TestAssessmentSection(unittest.TestCase):
    """Tests for AssessmentSection"""

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_id(self):
        """Tests get_assessment_taken_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken(self):
        """Tests get_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_allocated_time(self):
        """Tests has_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_allocated_time(self):
        """Tests get_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_are_items_sequential(self):
        """Tests are_items_sequential"""
        pass

    @unittest.skip('unimplemented test')
    def test_are_items_shuffled(self):
        """Tests are_items_shuffled"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_section_record(self):
        """Tests get_assessment_section_record"""
        pass


class TestAssessmentSectionList(unittest.TestCase):
    """Tests for AssessmentSectionList"""

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_section(self):
        """Tests get_next_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_sections(self):
        """Tests get_next_assessment_sections"""
        pass


class TestBank(unittest.TestCase):
    """Tests for Bank"""

    @unittest.skip('unimplemented test')
    def test_get_bank_record(self):
        """Tests get_bank_record"""
        pass


class TestBankForm(unittest.TestCase):
    """Tests for BankForm"""

    @unittest.skip('unimplemented test')
    def test_get_bank_form_record(self):
        """Tests get_bank_form_record"""
        pass


class TestBankList(unittest.TestCase):
    """Tests for BankList"""

    @unittest.skip('unimplemented test')
    def test_get_next_bank(self):
        """Tests get_next_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_banks(self):
        """Tests get_next_banks"""
        pass


class TestBankNode(unittest.TestCase):
    """Tests for BankNode"""

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_bank_nodes(self):
        """Tests get_parent_bank_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_bank_nodes(self):
        """Tests get_child_bank_nodes"""
        pass


class TestBankNodeList(unittest.TestCase):
    """Tests for BankNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_bank_node(self):
        """Tests get_next_bank_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_bank_nodes(self):
        """Tests get_next_bank_nodes"""
        pass


class TestResponseList(unittest.TestCase):
    """Tests for ResponseList"""

    @unittest.skip('unimplemented test')
    def test_get_next_response(self):
        """Tests get_next_response"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_responses(self):
        """Tests get_next_responses"""
        pass
