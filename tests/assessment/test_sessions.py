"""Unit tests of assessment sessions."""


import datetime
import unittest


from dlkit.abstract_osid.assessment import objects
from dlkit.abstract_osid.assessment import objects as ABCObjects
from dlkit.abstract_osid.assessment import queries as ABCQueries
from dlkit.abstract_osid.assessment import searches as ABCSearches
from dlkit.abstract_osid.assessment.objects import AssessmentOffered
from dlkit.abstract_osid.assessment.objects import AssessmentSection, AssessmentSectionList
from dlkit.abstract_osid.assessment.objects import AssessmentTaken
from dlkit.abstract_osid.assessment.objects import Bank, Answer, AnswerList, AnswerForm
from dlkit.abstract_osid.assessment.objects import Question, QuestionList
from dlkit.abstract_osid.assessment.objects import ResponseList
from dlkit.abstract_osid.assessment.rules import Response
from dlkit.abstract_osid.hierarchy.objects import Hierarchy
from dlkit.abstract_osid.id.objects import IdList
from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.abstract_osid.osid.objects import OsidNode
from dlkit.json_.assessment import searches
from dlkit.json_.id.objects import IdList
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.types.string import get_type_data as get_string_type_data
from dlkit.primordium.type.primitives import Type
from dlkit.records import registry
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


SEQUENCE_ASSESSMENT = Type(**registry.ASSESSMENT_RECORD_TYPES["simple-child-sequencing"])
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
DEFAULT_STRING_MATCH_TYPE = Type(**get_string_type_data("WORDIGNORECASE"))
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE 2', 'authority': 'YOURS 2'})


class TestAssessmentSession(unittest.TestCase):
    """Tests for AssessmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([SEQUENCE_ASSESSMENT])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = cls.catalog.create_item(ifc)
            form = cls.catalog.get_question_form_for_create(test_item.ident, [])
            cls.catalog.create_question(form)

            if number == 'One':
                form = cls.catalog.get_answer_form_for_create(test_item.ident, [])
                cls.catalog.create_answer(form)

            cls.catalog.add_item(cls.assessment.ident, test_item.ident)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        cls.assessment_offered = cls.catalog.create_assessment_offered(form)

    def setUp(self):
        self.session = self.catalog
        form = self.catalog.get_assessment_taken_form_for_create(self.assessment_offered.ident, [])
        self.taken = self.catalog.create_assessment_taken(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        for item in cls.catalog.get_items():
            cls.catalog.delete_item(item.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # this test should not be needed....
        self.assertTrue(isinstance(self.catalog, Bank))

    def test_can_take_assessments(self):
        """Tests can_take_assessments"""
        self.assertTrue(self.session.can_take_assessments())

    def test_has_assessment_begun(self):
        """Tests has_assessment_begun"""
        future_start = DateTime.utcnow() + datetime.timedelta(days=1)
        form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
        form.set_start_time(DateTime(**{
            'year': future_start.year,
            'month': future_start.month,
            'day': future_start.day,
            'hour': future_start.hour,
            'minute': future_start.minute,
            'second': future_start.second
        }))
        future_offered = self.catalog.create_assessment_offered(form)
        form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
        future_taken = self.catalog.create_assessment_taken(form)
        self.assertFalse(self.session.has_assessment_begun(future_taken.ident))

        self.assertTrue(self.session.has_assessment_begun(self.taken.ident))

    def test_is_assessment_over(self):
        """Tests is_assessment_over"""
        # There are also other conditions that flag "over", but are not
        # tested here. Like if the offered goes past the deadline...so we
        # would have to do a time.sleep(). TODO: add those tests in.

        self.assertFalse(self.session.is_assessment_over(self.taken.ident))
        self.session.finish_assessment(self.taken.ident)
        self.assertTrue(self.session.is_assessment_over(self.taken.ident))

    def test_requires_synchronous_sections(self):
        """Tests requires_synchronous_sections"""
        self.assertFalse(self.session.requires_synchronous_sections(self.taken.ident))

    def test_get_first_assessment_section(self):
        """Tests get_first_assessment_section"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        self.assertTrue(isinstance(section, AssessmentSection))

    def test_has_next_assessment_section(self):
        """Tests has_next_assessment_section"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        self.assertFalse(self.session.has_next_assessment_section(section.ident))

    def test_get_next_assessment_section(self):
        """Tests get_next_assessment_section"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        with self.assertRaises(errors.IllegalState):
            self.session.get_next_assessment_section(section.ident)

    def test_has_previous_assessment_section(self):
        """Tests has_previous_assessment_section"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        self.assertFalse(self.session.has_previous_assessment_section(section.ident))

    def test_get_previous_assessment_section(self):
        """Tests get_previous_assessment_section"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        with self.assertRaises(errors.IllegalState):
            self.session.get_previous_assessment_section(section.ident)

    def test_get_assessment_section(self):
        """Tests get_assessment_section"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        test_section = self.session.get_assessment_section(section.ident)
        self.assertTrue(isinstance(test_section, AssessmentSection))
        self.assertEqual(str(test_section.ident),
                         str(section.ident))

    def test_get_assessment_sections(self):
        """Tests get_assessment_sections"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        test_sections = self.session.get_assessment_sections(self.taken.ident)
        self.assertTrue(isinstance(test_sections, AssessmentSectionList))
        self.assertEqual(test_sections.available(), 1)
        first_section = test_sections.next()
        self.assertTrue(isinstance(first_section, AssessmentSection))
        self.assertEqual(str(first_section.ident),
                         str(section.ident))

    def test_is_assessment_section_complete(self):
        """Tests is_assessment_section_complete"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        total_questions = questions.available()

        self.assertFalse(self.session.is_assessment_section_complete(section.ident))

        for index, question in enumerate(questions):
            form = self.session.get_response_form(section.ident, question.ident)
            self.session.submit_response(section.ident, question.ident, form)
            if index < (total_questions - 1):
                self.assertFalse(self.session.is_assessment_section_complete(section.ident))
            else:
                self.assertTrue(self.session.is_assessment_section_complete(section.ident))

    def test_get_incomplete_assessment_sections(self):
        """Tests get_incomplete_assessment_sections"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()

        test_sections = self.session.get_incomplete_assessment_sections(self.taken.ident)
        self.assertTrue(isinstance(test_sections, AssessmentSectionList))
        self.assertEqual(test_sections.available(), 1)
        first_section = test_sections.next()
        self.assertTrue(isinstance(first_section, AssessmentSection))
        self.assertEqual(str(first_section.ident),
                         str(section.ident))

        for question in questions:
            form = self.session.get_response_form(section.ident, question.ident)
            self.session.submit_response(section.ident, question.ident, form)

        self.session._provider_sessions = {}  # need to get rid of the cached taken
        test_sections = self.session.get_incomplete_assessment_sections(self.taken.ident)
        self.assertTrue(isinstance(test_sections, AssessmentSectionList))
        self.assertEqual(test_sections.available(), 0)

    def test_has_assessment_section_begun(self):
        """Tests has_assessment_section_begun"""
        future_start = DateTime.utcnow() + datetime.timedelta(days=1)
        form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
        form.set_start_time(DateTime(**{
            'year': future_start.year,
            'month': future_start.month,
            'day': future_start.day,
            'hour': future_start.hour,
            'minute': future_start.minute,
            'second': future_start.second
        }))
        future_offered = self.catalog.create_assessment_offered(form)
        form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
        future_taken = self.catalog.create_assessment_taken(form)

        with self.assertRaises(errors.IllegalState):
            # cannot even get the sectionId to call the method
            self.catalog.get_first_assessment_section(future_taken.ident)

        section = self.catalog.get_first_assessment_section(self.taken.ident)
        self.assertTrue(self.session.has_assessment_section_begun(section.ident))

    def test_is_assessment_section_over(self):
        """Tests is_assessment_section_over"""
        # There are also other conditions that flag "over", but are not
        # tested here. Like if the offered goes past the deadline...so we
        # would have to do a time.sleep(). TODO: add those tests in.

        section = self.catalog.get_first_assessment_section(self.taken.ident)

        self.assertFalse(self.session.is_assessment_section_over(section.ident))
        self.session.finish_assessment_section(section.ident)
        self.assertTrue(self.session.is_assessment_section_over(section.ident))

    def test_requires_synchronous_responses(self):
        """Tests requires_synchronous_responses"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        self.assertFalse(self.session.requires_synchronous_responses(section.ident))

    def test_get_first_question(self):
        """Tests get_first_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        test_question = self.session.get_first_question(section.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(first_question.ident),
                         str(test_question.ident))

    def test_has_next_question(self):
        """Tests has_next_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        self.assertTrue(self.session.has_next_question(section.ident,
                                                       first_question.ident))
        self.assertFalse(self.session.has_next_question(section.ident,
                                                        fourth_question.ident))

    def test_get_next_question(self):
        """Tests get_next_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        test_question = self.session.get_next_question(section.ident,
                                                       first_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(second_question.ident),
                         str(test_question.ident))

        with self.assertRaises(errors.IllegalState):
            self.session.get_next_question(section.ident, fourth_question.ident)

    def test_has_previous_question(self):
        """Tests has_previous_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        self.assertTrue(self.session.has_previous_question(section.ident,
                                                           fourth_question.ident))
        self.assertFalse(self.session.has_previous_question(section.ident,
                                                            first_question.ident))

    def test_get_previous_question(self):
        """Tests get_previous_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        test_question = self.session.get_previous_question(section.ident,
                                                           fourth_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(third_question.ident),
                         str(test_question.ident))

        with self.assertRaises(errors.IllegalState):
            self.session.get_previous_question(section.ident, first_question.ident)

    def test_get_question(self):
        """Tests get_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        test_question = self.session.get_question(section.ident, first_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(test_question.ident),
                         str(first_question.ident))

    def test_get_questions(self):
        """Tests get_questions"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        test_questions = self.session.get_questions(section.ident)
        self.assertTrue(isinstance(test_questions, QuestionList))
        self.assertEqual(test_questions.available(), 4)
        first_test_question = test_questions.next()
        self.assertTrue(isinstance(first_test_question, Question)),
        self.assertEqual(str(first_test_question.ident),
                         str(first_question.ident))

    def test_get_response_form(self):
        """Tests get_response_form"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.assertTrue(isinstance(form, AnswerForm))

    def test_submit_response(self):
        """Tests submit_response"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        self.assertIn('missingResponse',
                      section._my_map['questions'][0]['responses'][0])
        self.assertEqual(0, section._my_map['questions'][0]['responses'][0]['missingResponse'])

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)
        section = self.catalog.get_assessment_section(section.ident)

        self.assertNotIn('missingResponse',
                         section._my_map['questions'][0]['responses'][0])

    def test_skip_item(self):
        """Tests skip_item"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        self.assertIn('missingResponse',
                      section._my_map['questions'][0]['responses'][0])
        self.assertEqual(0, section._my_map['questions'][0]['responses'][0]['missingResponse'])

        self.session.skip_item(section.ident, first_question.ident)
        section = self.catalog.get_assessment_section(section.ident)

        self.assertIn('missingResponse',
                      section._my_map['questions'][0]['responses'][0])
        self.assertEqual(1, section._my_map['questions'][0]['responses'][0]['missingResponse'])

    def test_is_question_answered(self):
        """Tests is_question_answered"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        self.assertFalse(self.session.is_question_answered(section.ident,
                                                           first_question.ident))

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)

        self.assertTrue(self.session.is_question_answered(section.ident,
                                                          first_question.ident))

    def test_get_unanswered_questions(self):
        """Tests get_unanswered_questions"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        question_ids = [q.ident for q in questions]

        test_questions = self.session.get_unanswered_questions(section.ident)
        self.assertTrue(isinstance(test_questions, QuestionList))
        self.assertEqual(test_questions.available(), 4)
        test_question_ids = [q.ident for q in test_questions]
        self.assertEqual(question_ids, test_question_ids)

        form = self.session.get_response_form(section.ident, question_ids[1])
        self.session.submit_response(section.ident, question_ids[1], form)

        test_questions = self.session.get_unanswered_questions(section.ident)
        self.assertTrue(isinstance(test_questions, QuestionList))
        self.assertEqual(test_questions.available(), 3)
        test_question_ids = [q.ident for q in test_questions]
        self.assertNotIn(question_ids[1], test_question_ids)

    def test_has_unanswered_questions(self):
        """Tests has_unanswered_questions"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        total_questions = questions.available()

        self.assertTrue(self.session.has_unanswered_questions(section.ident))

        for index, question in enumerate(questions):
            form = self.session.get_response_form(section.ident, question.ident)
            self.session.submit_response(section.ident, question.ident, form)
            if index < (total_questions - 1):
                self.assertTrue(self.session.has_unanswered_questions(section.ident))
            else:
                self.assertFalse(self.session.has_unanswered_questions(section.ident))

    def test_get_first_unanswered_question(self):
        """Tests get_first_unanswered_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()

        unanswered_question = self.session.get_first_unanswered_question(section.ident)
        self.assertTrue(isinstance(unanswered_question, Question))
        self.assertEqual(str(unanswered_question.ident),
                         str(first_question.ident))

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)

        unanswered_question = self.session.get_first_unanswered_question(section.ident)
        self.assertTrue(isinstance(unanswered_question, Question))
        self.assertEqual(str(unanswered_question.ident),
                         str(second_question.ident))

    def test_has_next_unanswered_question(self):
        """Tests has_next_unanswered_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        self.assertTrue(self.session.has_next_unanswered_question(section.ident,
                                                                  first_question.ident))

        form = self.session.get_response_form(section.ident, second_question.ident)
        self.session.submit_response(section.ident, second_question.ident, form)

        self.assertTrue(self.session.has_next_unanswered_question(section.ident,
                                                                  first_question.ident))
        self.assertFalse(self.session.has_next_unanswered_question(section.ident,
                                                                   fourth_question.ident))

    def test_get_next_unanswered_question(self):
        """Tests get_next_unanswered_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        test_question = self.session.get_next_unanswered_question(section.ident,
                                                                  first_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(second_question.ident),
                         str(test_question.ident))

        form = self.session.get_response_form(section.ident, second_question.ident)
        self.session.submit_response(section.ident, second_question.ident, form)

        test_question = self.session.get_next_unanswered_question(section.ident,
                                                                  first_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(third_question.ident),
                         str(test_question.ident))

        with self.assertRaises(errors.IllegalState):
            self.session.get_next_unanswered_question(section.ident,
                                                      fourth_question.ident)

    def test_has_previous_unanswered_question(self):
        """Tests has_previous_unanswered_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        self.assertTrue(self.session.has_previous_unanswered_question(section.ident,
                                                                      fourth_question.ident))

        form = self.session.get_response_form(section.ident, third_question.ident)
        self.session.submit_response(section.ident, third_question.ident, form)

        self.assertTrue(self.session.has_previous_unanswered_question(section.ident,
                                                                      fourth_question.ident))
        self.assertFalse(self.session.has_previous_unanswered_question(section.ident,
                                                                       first_question.ident))

    def test_get_previous_unanswered_question(self):
        """Tests get_previous_unanswered_question"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()
        third_question = questions.next()
        fourth_question = questions.next()

        test_question = self.session.get_previous_unanswered_question(section.ident,
                                                                      fourth_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(third_question.ident),
                         str(test_question.ident))

        form = self.session.get_response_form(section.ident, third_question.ident)
        self.session.submit_response(section.ident, third_question.ident, form)

        test_question = self.session.get_previous_unanswered_question(section.ident,
                                                                      fourth_question.ident)
        self.assertTrue(isinstance(test_question, Question))
        self.assertEqual(str(second_question.ident),
                         str(test_question.ident))

        with self.assertRaises(errors.IllegalState):
            self.session.get_previous_unanswered_question(section.ident,
                                                          first_question.ident)

    def test_get_response(self):
        """Tests get_response"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        test_response = self.session.get_response(section.ident, first_question.ident)
        self.assertTrue(isinstance(test_response, Response))

        with self.assertRaises(errors.IllegalState):
            test_response.object_map

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)

        test_response = self.session.get_response(section.ident, first_question.ident)
        self.assertTrue(isinstance(test_response, Response))

        test_response.object_map

    def test_get_responses(self):
        """Tests get_responses"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()

        test_responses = self.session.get_responses(section.ident)
        self.assertTrue(isinstance(test_responses, ResponseList))
        self.assertEqual(test_responses.available(), 4)
        first_response = test_responses.next()
        self.assertTrue(isinstance(first_response, Response))

        with self.assertRaises(errors.IllegalState):
            first_response.object_map

    def test_clear_response(self):
        """Tests clear_response"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()

        self.assertIn('missingResponse',
                      section._my_map['questions'][0]['responses'][0])
        self.assertEqual(0, section._my_map['questions'][0]['responses'][0]['missingResponse'])

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)
        section = self.catalog.get_assessment_section(section.ident)

        self.assertNotIn('missingResponse',
                         section._my_map['questions'][0]['responses'][0])

        self.session.clear_response(section.ident, first_question.ident)
        section = self.catalog.get_assessment_section(section.ident)

        self.assertIn('missingResponse',
                      section._my_map['questions'][0]['responses'][0])
        self.assertEqual(1, section._my_map['questions'][0]['responses'][0]['missingResponse'])

    def test_finish_assessment_section(self):
        """Tests finish_assessment_section"""
        future_start = DateTime.utcnow() + datetime.timedelta(days=1)
        form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
        form.set_start_time(DateTime(**{
            'year': future_start.year,
            'month': future_start.month,
            'day': future_start.day,
            'hour': future_start.hour,
            'minute': future_start.minute,
            'second': future_start.second
        }))
        future_offered = self.catalog.create_assessment_offered(form)
        form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
        future_taken = self.catalog.create_assessment_taken(form)
        with self.assertRaises(errors.IllegalState):
            self.catalog.get_first_assessment_section(future_taken.ident)

        first_section = self.catalog.get_first_assessment_section(self.taken.ident)
        self.assertNotIn('completionTime', first_section._my_map)
        self.session.finish_assessment_section(first_section.ident)

        with self.assertRaises(errors.IllegalState):
            # it is over, so can't GET the section now
            self.catalog.get_assessment_section(first_section.ident)

    def test_is_answer_available(self):
        """Tests is_answer_available"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()

        self.assertFalse(self.session.is_answer_available(section.ident,
                                                          second_question.ident))

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)

        answers = self.session.get_answers(section.ident, first_question.ident)
        self.assertTrue(isinstance(answers, AnswerList))
        self.assertTrue(self.session.is_answer_available(section.ident,
                                                         first_question.ident))

    def test_get_answers(self):
        """Tests get_answers"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()
        first_question = questions.next()
        second_question = questions.next()

        with self.assertRaises(errors.IllegalState):
            self.session.get_answers(section.ident, second_question.ident)

        form = self.session.get_response_form(section.ident, first_question.ident)
        self.session.submit_response(section.ident, first_question.ident, form)

        answers = self.session.get_answers(section.ident, first_question.ident)
        self.assertTrue(isinstance(answers, AnswerList))
        self.assertEqual(answers.available(), 1)
        self.assertTrue(isinstance(answers.next(), Answer))

    def test_finish_assessment(self):
        """Tests finish_assessment"""
        future_start = DateTime.utcnow() + datetime.timedelta(days=1)
        form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
        form.set_start_time(DateTime(**{
            'year': future_start.year,
            'month': future_start.month,
            'day': future_start.day,
            'hour': future_start.hour,
            'minute': future_start.minute,
            'second': future_start.second
        }))
        future_offered = self.catalog.create_assessment_offered(form)
        form = self.catalog.get_assessment_taken_form_for_create(future_offered.ident, [])
        future_taken = self.catalog.create_assessment_taken(form)
        with self.assertRaises(errors.IllegalState):
            self.session.finish_assessment(future_taken.ident)

        self.assertIsNone(self.taken._my_map['completionTime'])
        self.session.finish_assessment(self.taken.ident)
        taken = self.catalog.get_assessment_taken(self.taken.ident)
        self.assertIsNotNone(taken._my_map['completionTime'])


class TestAssessmentResultsSession(unittest.TestCase):
    """Tests for AssessmentResultsSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentResultsSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([SEQUENCE_ASSESSMENT])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentResultsSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = cls.catalog.create_item(ifc)

            form = cls.catalog.get_question_form_for_create(test_item.ident, [])
            cls.catalog.create_question(form)

            cls.catalog.add_item(cls.assessment.ident, test_item.ident)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        cls.assessment_offered = cls.catalog.create_assessment_offered(form)

    def setUp(self):
        self.session = self.svc_mgr.get_assessment_results_session(proxy=self.catalog._proxy)
        form = self.catalog.get_assessment_taken_form_for_create(self.assessment_offered.ident, [])
        self.taken = self.catalog.create_assessment_taken(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        for item in cls.catalog.get_items():
            cls.catalog.delete_item(item.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_access_assessment_results(self):
        """Tests can_access_assessment_results"""
        self.assertTrue(self.session.can_access_assessment_results())

    def test_get_items(self):
        """Tests get_items"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        section.get_questions()
        self.assertEqual(self.session.get_items(self.taken.ident).available(), 4)

    def test_get_responses(self):
        """Tests get_responses"""
        section = self.catalog.get_first_assessment_section(self.taken.ident)
        questions = section.get_questions()

        test_responses = self.session.get_responses(self.taken.ident)
        self.assertTrue(isinstance(test_responses, ResponseList))
        self.assertEqual(test_responses.available(), 4)
        first_response = test_responses.next()
        self.assertTrue(isinstance(first_response, Response))

        with self.assertRaises(errors.IllegalState):
            first_response.object_map

    def test_are_results_available(self):
        """Tests are_results_available"""
        self.assertFalse(self.session.are_results_available(self.assessment.ident))

    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        with self.assertRaises(errors.IllegalState):
            self.session.get_grade_entries(self.assessment.ident)


class TestItemLookupSession(unittest.TestCase):
    """Tests for ItemLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemLookupSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_items(self):
        """Tests can_lookup_items"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_items(), bool))

    def test_use_comparative_item_view(self):
        """Tests use_comparative_item_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_item_view()

    def test_use_plenary_item_view(self):
        """Tests use_plenary_item_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_item_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_item(self):
        """Tests get_item"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_item(self.item_list[0].ident)
        self.assertEqual(obj.ident, self.item_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_item(self.item_list[0].ident)
        self.assertEqual(obj.ident, self.item_list[0].ident)

    def test_get_items_by_ids(self):
        """Tests get_items_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_ids(self.item_ids)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_ids(self.item_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ItemList))

    def test_get_items_by_genus_type(self):
        """Tests get_items_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ItemList))

    def test_get_items_by_parent_genus_type(self):
        """Tests get_items_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ItemList))

    def test_get_items_by_record_type(self):
        """Tests get_items_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, ItemList))

    def test_get_items_by_question(self):
        """Tests get_items_by_question"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_items_by_question(True)

    def test_get_items_by_answer(self):
        """Tests get_items_by_answer"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_items_by_answer(True)

    def test_get_items_by_learning_objective(self):
        """Tests get_items_by_learning_objective"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_items_by_learning_objective(True)

    def test_get_items_by_learning_objectives(self):
        """Tests get_items_by_learning_objectives"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_items_by_learning_objectives(True)

    def test_get_items(self):
        """Tests get_items"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items()
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, ItemList))

    def test_get_item_with_alias(self):
        self.catalog.alias_item(self.item_ids[0], ALIAS_ID)
        obj = self.catalog.get_item(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.item_ids[0])


class TestItemQuerySession(unittest.TestCase):
    """Tests for ItemQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemQuerySession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + color
            create_form.description = (
                'Test Item for ItemQuerySession tests, did I mention green')
            obj = cls.catalog.create_item(create_form)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        for item in cls.catalog.get_items():
            cls.catalog.delete_item(item.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_items(self):
        """Tests can_search_items"""
        self.assertTrue(self.session.can_search_items())

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_item_query(self):
        """Tests get_item_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_item_query()

    def test_get_items_by_query(self):
        """Tests get_items_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_item_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_items_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_items_by_query(query).available(), 3)


class TestItemSearchSession(unittest.TestCase):
    """Tests for ItemSearchSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemSearchSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + color
            create_form.description = (
                'Test Item for ItemSearchSession tests, did I mention green')
            obj = cls.catalog.create_item(create_form)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        for item in cls.catalog.get_items():
            cls.catalog.delete_item(item.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_item_search(self):
        """Tests get_item_search"""
        search = self.session.get_item_search()
        self.assertTrue(isinstance(search, searches.ItemSearch))

    def test_get_item_search_order(self):
        """Tests get_item_search_order"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_item_search_order()

    def test_get_items_by_search(self):
        """Tests get_items_by_search"""
        query = self.session.get_item_query()
        query.match_display_name('zxy', DEFAULT_STRING_MATCH_TYPE, True)
        search = self.session.get_item_search()
        results = self.session.get_items_by_search(query, search)
        self.assertTrue(isinstance(results, searches.ItemSearchResults))
        self.assertEqual(results.get_result_size(), 0)

    def test_get_item_query_from_inspector(self):
        """Tests get_item_query_from_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_item_query_from_inspector(True)


class TestItemAdminSession(unittest.TestCase):
    """Tests for ItemAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        create_form = self.catalog.get_item_form_for_create([])
        create_form.display_name = 'new Item'
        create_form.description = 'description of Item'
        create_form.set_genus_type(NEW_TYPE)
        self.osid_object = self.catalog.create_item(create_form)
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        for item in cls.catalog.get_items():
            cls.catalog.delete_item(item.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_items(self):
        """Tests can_create_items"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_items(), bool))

    def test_can_create_item_with_record_types(self):
        """Tests can_create_item_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_item_with_record_types(DEFAULT_TYPE), bool))

    def test_get_item_form_for_create(self):
        """Tests get_item_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_item_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_item(self):
        """Tests create_item"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import Item
        self.assertTrue(isinstance(self.osid_object, Item))
        self.assertEqual(self.osid_object.display_name.text, 'new Item')
        self.assertEqual(self.osid_object.description.text, 'description of Item')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_items(self):
        """Tests can_update_items"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_items(), bool))

    def test_get_item_form_for_update(self):
        """Tests get_item_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_item_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_item(self):
        """Tests update_item"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.assessment.objects import Item
        form = self.catalog.get_item_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_item(form)
        self.assertTrue(isinstance(updated_object, Item))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_items(self):
        """Tests can_delete_items"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_items(), bool))

    def test_delete_item(self):
        """Tests delete_item"""
        # From test_templates/resource.py::ResourceAdminSession::delete_resource_template
        form = self.catalog.get_item_form_for_create([])
        form.display_name = 'new Item'
        form.description = 'description of Item'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_item(form)
        self.catalog.delete_item(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_item(osid_object.ident)

    def test_can_manage_item_aliases(self):
        """Tests can_manage_item_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_item_aliases(), bool))

    def test_alias_item(self):
        """Tests alias_item"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_item(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_item(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)

    def test_can_create_questions(self):
        """Tests can_create_questions"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_questions(), bool))

    def test_can_create_question_with_record_types(self):
        """Tests can_create_question_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_question_with_record_types(DEFAULT_TYPE), bool))

    def test_get_question_form_for_create(self):
        """Tests get_question_form_for_create"""
        form = self.session.get_question_form_for_create(self.osid_object.ident, [])
        self.assertTrue(isinstance(form, objects.QuestionForm))
        self.assertFalse(form.is_for_update())

    def test_create_question(self):
        """Tests create_question"""
        with self.assertRaises(TypeError):
            # question_map = dict(self._my_map['question'])
            # TypeError: 'NoneType' object is not iterable
            self.osid_object.get_question()

        form = self.session.get_question_form_for_create(self.osid_object.ident, [])
        self.session.create_question(form)
        updated_item = self.catalog.get_item(self.osid_object.ident)
        self.assertTrue(isinstance(updated_item.get_question(), Question))

    def test_can_update_questions(self):
        """Tests can_update_questions"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_questions(), bool))

    def test_get_question_form_for_update(self):
        """Tests get_question_form_for_update"""
        form = self.session.get_question_form_for_create(self.osid_object.ident, [])
        question = self.session.create_question(form)

        form = self.session.get_question_form_for_update(question.ident)
        self.assertTrue(isinstance(form, objects.QuestionForm))
        self.assertTrue(form.is_for_update())

    def test_update_question(self):
        """Tests update_question"""
        form = self.session.get_question_form_for_create(self.osid_object.ident, [])
        question = self.session.create_question(form)
        self.assertEqual(question.display_name.text, 'new Item')

        form = self.session.get_question_form_for_update(question.ident)
        form.display_name = 'second name'
        question = self.session.update_question(form)
        self.assertTrue(isinstance(question, objects.Question))
        self.assertEqual(question.display_name.text, 'second name')

    def test_can_delete_questions(self):
        """Tests can_delete_questions"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_questions(), bool))

    def test_delete_question(self):
        """Tests delete_question"""
        with self.assertRaises(TypeError):
            # question_map = dict(self._my_map['question'])
            # TypeError: 'NoneType' object is not iterable
            self.osid_object.get_question()

        form = self.session.get_question_form_for_create(self.osid_object.ident, [])
        question = self.session.create_question(form)
        updated_item = self.catalog.get_item(self.osid_object.ident)
        self.assertTrue(isinstance(updated_item.get_question(), Question))

        with self.assertRaises(errors.NotFound):
            self.session.delete_question(Id('fake.Package%3A000000000000000000000000%40ODL.MIT.EDU'))

        self.session.delete_question(question.ident)
        updated_item = self.catalog.get_item(self.osid_object.ident)

        with self.assertRaises(TypeError):
            updated_item.get_question()

    def test_can_create_answers(self):
        """Tests can_create_answers"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_answers(), bool))

    def test_can_create_answers_with_record_types(self):
        """Tests can_create_answers_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_answers_with_record_types(DEFAULT_TYPE), bool))

    def test_get_answer_form_for_create(self):
        """Tests get_answer_form_for_create"""
        form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
        self.assertTrue(isinstance(form, objects.AnswerForm))
        self.assertFalse(form.is_for_update())

    def test_create_answer(self):
        """Tests create_answer"""
        self.assertEqual(self.osid_object.get_answers().available(), 0)
        form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
        self.session.create_answer(form)
        updated_item = self.catalog.get_item(self.osid_object.ident)
        self.assertEqual(updated_item.get_answers().available(), 1)

    def test_can_update_answers(self):
        """Tests can_update_answers"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_answers(), bool))

    def test_get_answer_form_for_update(self):
        """Tests get_answer_form_for_update"""
        form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
        answer = self.session.create_answer(form)

        form = self.session.get_answer_form_for_update(answer.ident)
        self.assertTrue(isinstance(form, objects.AnswerForm))
        self.assertTrue(form.is_for_update())

    def test_update_answer(self):
        """Tests update_answer"""
        form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
        form.display_name = 'first name'
        answer = self.session.create_answer(form)
        self.assertEqual(answer.display_name.text, 'first name')

        form = self.session.get_answer_form_for_update(answer.ident)
        form.display_name = 'second name'
        answer = self.session.update_answer(form)
        self.assertTrue(isinstance(answer, objects.Answer))
        self.assertEqual(answer.display_name.text, 'second name')

    def test_can_delete_answers(self):
        """Tests can_delete_answers"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_answers(), bool))

    def test_delete_answer(self):
        """Tests delete_answer"""
        self.assertEqual(self.osid_object.get_answers().available(), 0)
        form = self.session.get_answer_form_for_create(self.osid_object.ident, [])
        answer = self.session.create_answer(form)
        updated_item = self.catalog.get_item(self.osid_object.ident)
        self.assertEqual(updated_item.get_answers().available(), 1)

        with self.assertRaises(errors.NotFound):
            self.session.delete_answer(Id('fake.Package%3A000000000000000000000000%40ODL.MIT.EDU'))

        self.session.delete_answer(answer.ident)
        updated_item = self.catalog.get_item(self.osid_object.ident)
        self.assertEqual(updated_item.get_answers().available(), 0)


class TestItemNotificationSession(unittest.TestCase):
    """Tests for ItemNotificationSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemNotificationSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemNotificationSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_register_for_item_notifications(self):
        """Tests can_register_for_item_notifications"""
        with self.assertRaises(errors.Unimplemented):
            self.session.can_register_for_item_notifications()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_reliable_item_notifications(self):
        """Tests reliable_item_notifications"""
        self.session.reliable_item_notifications()

    def test_unreliable_item_notifications(self):
        """Tests unreliable_item_notifications"""
        self.session.unreliable_item_notifications()

    def test_acknowledge_item_notification(self):
        """Tests acknowledge_item_notification"""
        with self.assertRaises(errors.Unimplemented):
            self.session.acknowledge_item_notification(True)

    def test_register_for_new_items(self):
        """Tests register_for_new_items"""
        self.session.register_for_new_items()

    def test_register_for_changed_items(self):
        """Tests register_for_changed_items"""
        self.session.register_for_changed_items()

    def test_register_for_changed_item(self):
        """Tests register_for_changed_item"""
        self.session.register_for_changed_item(Id('package.Catalog%3Afake%40DLKIT.MIT.EDU'))

    def test_register_for_deleted_items(self):
        """Tests register_for_deleted_items"""
        self.session.register_for_deleted_items()

    def test_register_for_deleted_item(self):
        """Tests register_for_deleted_item"""
        self.session.register_for_deleted_item(Id('package.Catalog%3Afake%40DLKIT.MIT.EDU'))

    def test_reliable_item_notifications(self):
        """Tests reliable_item_notifications"""
        self.session.reliable_item_notifications()

    def test_unreliable_item_notifications(self):
        """Tests unreliable_item_notifications"""
        self.session.unreliable_item_notifications()

    def test_acknowledge_item_notification(self):
        """Tests acknowledge_item_notification"""
        with self.assertRaises(errors.Unimplemented):
            self.session.acknowledge_item_notification(True)


class TestItemBankSession(unittest.TestCase):
    """Tests for ItemBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for ItemBankSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemBankSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)
        cls.svc_mgr.assign_item_to_bank(
            cls.item_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_item_to_bank(
            cls.item_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_item_from_bank(
            cls.item_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_item_from_bank(
            cls.item_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_lookup_item_bank_mappings(self):
        """Tests can_lookup_item_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_item_bank_mappings()
        self.assertTrue(isinstance(result, bool))

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_item_ids_by_bank(self):
        """Tests get_item_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_item_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_items_by_bank(self):
        """Tests get_items_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_items_by_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.ItemList))
        self.assertEqual(results.available(), 2)

    def test_get_item_ids_by_banks(self):
        """Tests get_item_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_item_ids_by_banks(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_items_by_banks(self):
        """Tests get_items_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_items_by_banks(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.ItemList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_bank_ids_by_item(self):
        """Tests get_bank_ids_by_item"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_bank_ids_by_item(self.item_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_item(self):
        """Tests get_banks_by_item"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_banks_by_item(self.item_ids[1])
        self.assertEqual(cats.available(), 2)


class TestItemBankAssignmentSession(unittest.TestCase):
    """Tests for ItemBankAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemBankAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for ItemBankAssignmentSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemBankAssignmentSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_assign_items(self):
        """Tests can_assign_items"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_items()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_items_to_bank(self):
        """Tests can_assign_items_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_items_to_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_bank_ids_for_item(self):
        """Tests get_assignable_bank_ids_for_item"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids_for_item(self.catalog.ident, self.item_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_item_to_bank(self):
        """Tests assign_item_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_items()
        self.assertEqual(results.available(), 0)
        self.session.assign_item_to_bank(self.item_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_items()
        self.assertEqual(results.available(), 1)
        self.session.unassign_item_from_bank(
            self.item_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_item_from_bank(self):
        """Tests unassign_item_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_items()
        self.assertEqual(results.available(), 0)
        self.session.assign_item_to_bank(
            self.item_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_items()
        self.assertEqual(results.available(), 1)
        self.session.unassign_item_from_bank(
            self.item_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_items()
        self.assertEqual(results.available(), 0)

    def test_reassign_item_to_billing(self):
        """Tests reassign_item_to_billing"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reassign_item_to_billing(True, True, True)


class TestAssessmentLookupSession(unittest.TestCase):
    """Tests for AssessmentLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentLookupSession tests'
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_assessments(self):
        """Tests can_lookup_assessments"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_assessments(), bool))

    def test_use_comparative_assessment_view(self):
        """Tests use_comparative_assessment_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_view()

    def test_use_plenary_assessment_view(self):
        """Tests use_plenary_assessment_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment(self):
        """Tests get_assessment"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment(self.assessment_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment(self.assessment_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_list[0].ident)

    def test_get_assessments_by_ids(self):
        """Tests get_assessments_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_ids(self.assessment_ids)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_ids(self.assessment_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentList))

    def test_get_assessments_by_genus_type(self):
        """Tests get_assessments_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentList))

    def test_get_assessments_by_parent_genus_type(self):
        """Tests get_assessments_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, AssessmentList))

    def test_get_assessments_by_record_type(self):
        """Tests get_assessments_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, AssessmentList))

    def test_get_assessments(self):
        """Tests get_assessments"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments()
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentList))

    def test_get_assessment_with_alias(self):
        self.catalog.alias_assessment(self.assessment_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_ids[0])


class TestAssessmentQuerySession(unittest.TestCase):
    """Tests for AssessmentQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentQuerySession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + color
            create_form.description = (
                'Test Assessment for AssessmentQuerySession tests, did I mention green')
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceQuerySession::init_template
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_assessments(self):
        """Tests can_search_assessments"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_assessments(), bool))

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_query()

    def test_get_assessments_by_query(self):
        """Tests get_assessments_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_assessment_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessments_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_assessments_by_query(query).available(), 3)


class TestAssessmentAdminSession(unittest.TestCase):
    """Tests for AssessmentAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        form = self.catalog.get_assessment_form_for_create([])
        form.display_name = 'new Assessment'
        form.description = 'description of Assessment'
        form.set_genus_type(NEW_TYPE)
        self.osid_object = self.catalog.create_assessment(form)
        self.session = self.catalog

    def tearDown(self):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        self.catalog.delete_assessment(self.osid_object.ident)

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceAdminSession::init_template
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_assessments(self):
        """Tests can_create_assessments"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_assessments(), bool))

    def test_can_create_assessment_with_record_types(self):
        """Tests can_create_assessment_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_assessment_with_record_types(DEFAULT_TYPE), bool))

    def test_get_assessment_form_for_create(self):
        """Tests get_assessment_form_for_create"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_create_template
        form = self.catalog.get_assessment_form_for_create([])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_assessment(self):
        """Tests create_assessment"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import Assessment
        self.assertTrue(isinstance(self.osid_object, Assessment))
        self.assertEqual(self.osid_object.display_name.text, 'new Assessment')
        self.assertEqual(self.osid_object.description.text, 'description of Assessment')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_assessments(self):
        """Tests can_update_assessments"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_assessments(), bool))

    def test_get_assessment_form_for_update(self):
        """Tests get_assessment_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_assessment_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_assessment(self):
        """Tests update_assessment"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.assessment.objects import Assessment
        form = self.catalog.get_assessment_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_assessment(form)
        self.assertTrue(isinstance(updated_object, Assessment))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_assessments(self):
        """Tests can_delete_assessments"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_assessments(), bool))

    def test_delete_assessment(self):
        """Tests delete_assessment"""
        # From test_templates/learning.py::ObjectiveAdminSession::delete_objective_template
        results = self.catalog.get_assessments()
        self.assertEqual(results.available(), 1)

        form = self.catalog.get_assessment_form_for_create([])
        form.display_name = 'new Assessment'
        form.description = 'description of Assessment'
        new_assessment = self.catalog.create_assessment(form)

        results = self.catalog.get_assessments()
        self.assertEqual(results.available(), 2)

        self.session.delete_assessment(new_assessment.ident)

        results = self.catalog.get_assessments()
        self.assertEqual(results.available(), 1)
        self.assertNotEqual(str(results.next().ident),
                            str(new_assessment.ident))

    def test_can_manage_assessment_aliases(self):
        """Tests can_manage_assessment_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_assessment_aliases(), bool))

    def test_alias_assessment(self):
        """Tests alias_assessment"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_assessment(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_assessment(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestAssessmentBankSession(unittest.TestCase):
    """Tests for AssessmentBankSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinSession::init_template
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentBankSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentBankSession tests'
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)
        cls.svc_mgr.assign_assessment_to_bank(
            cls.assessment_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_assessment_to_bank(
            cls.assessment_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinSession::init_template
        cls.svc_mgr.unassign_assessment_from_bank(
            cls.assessment_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_assessment_from_bank(
            cls.assessment_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_lookup_assessment_bank_mappings(self):
        """Tests can_lookup_assessment_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_bank_mappings()
        self.assertTrue(isinstance(result, bool))

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_ids_by_bank(self):
        """Tests get_assessment_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_assessment_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_assessments_by_bank(self):
        """Tests get_assessments_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_assessments_by_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentList))
        self.assertEqual(results.available(), 2)

    def test_get_assessment_ids_by_banks(self):
        """Tests get_assessment_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_assessment_ids_by_banks(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_assessments_by_banks(self):
        """Tests get_assessments_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_assessments_by_banks(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_bank_ids_by_assessment(self):
        """Tests get_bank_ids_by_assessment"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_bank_ids_by_assessment(self.assessment_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_assessment(self):
        """Tests get_banks_by_assessment"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_banks_by_assessment(self.assessment_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssessmentBankAssignmentSession(unittest.TestCase):
    """Tests for AssessmentBankAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBankAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentBankAssignmentSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentBankAssignmentSession tests'
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)

    def setUp(self):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceBinAssignmentSession::init_template
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.assigned_catalog.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_assign_assessments(self):
        """Tests can_assign_assessments"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessments()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_assessments_to_bank(self):
        """Tests can_assign_assessments_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessments_to_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_bank_ids_for_assessment(self):
        """Tests get_assignable_bank_ids_for_assessment"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids_for_assessment(self.catalog.ident, self.assessment_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_assessment_to_bank(self):
        """Tests assign_assessment_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_assessments()
        self.assertEqual(results.available(), 0)
        self.session.assign_assessment_to_bank(self.assessment_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments()
        self.assertEqual(results.available(), 1)
        self.session.unassign_assessment_from_bank(
            self.assessment_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_assessment_from_bank(self):
        """Tests unassign_assessment_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_assessments()
        self.assertEqual(results.available(), 0)
        self.session.assign_assessment_to_bank(
            self.assessment_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments()
        self.assertEqual(results.available(), 1)
        self.session.unassign_assessment_from_bank(
            self.assessment_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments()
        self.assertEqual(results.available(), 0)

    def test_reassign_assessment_to_billing(self):
        """Tests reassign_assessment_to_billing"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reassign_assessment_to_billing(True, True, True)


class TestAssessmentBasicAuthoringSession(unittest.TestCase):
    """Tests for AssessmentBasicAuthoringSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        simple_sequence_record_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'osid-object',
            'identifier': 'simple-child-sequencing'})
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        # cls.auth_svc_mgr = Runtime().get_service_manager('ASSESSMENT_AUTHORING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBasicAuthoringSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([simple_sequence_record_type])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentBasicAuthoringSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        cls.test_items = list()
        cls.test_item_ids = list()
        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = cls.catalog.create_item(ifc)
            cls.test_items.append(test_item)
            cls.test_item_ids.append(test_item.ident)
            cls.catalog.add_item(cls.assessment.ident, test_item.ident)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_author_assessments(self):
        """Tests can_author_assessments"""
        self.assertTrue(isinstance(self.catalog.can_author_assessments(), bool))

    def test_get_items(self):
        """Tests get_items"""
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).available(), 4)

    def test_add_item(self):
        """Tests add_item"""
        self._reorder_items()
        ifc = self.catalog.get_item_form_for_create([])
        ifc.set_display_name('Test Assessment Additional Item')
        ifc.set_description('This is an addtional Test Item')
        additional_item = self.catalog.create_item(ifc)
        self.catalog.add_item(self.assessment.ident, additional_item.ident)
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).available(), 5)
        self.catalog.remove_item(self.assessment.ident, additional_item.ident)

    def test_remove_item(self):
        """Tests remove_item"""
        self._reorder_items()
        self.catalog.remove_item(self.assessment.ident, self.test_item_ids[1])
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).available(), 3)
        self.catalog.add_item(self.assessment.ident, self.test_item_ids[1])
        items = self.catalog.get_assessment_items(self.assessment.ident)
        self.assertEqual(items.next().ident, self.test_item_ids[0])
        self.assertEqual(items.next().ident, self.test_item_ids[2])
        self.assertEqual(items.next().ident, self.test_item_ids[3])
        self.assertEqual(items.next().ident, self.test_item_ids[1])

    def test_move_item(self):
        """Tests move_item"""
        self._reorder_items()
        self.catalog.move_item(self.assessment.ident, self.test_item_ids[0], self.test_item_ids[3])
        items = self.catalog.get_assessment_items(self.assessment.ident)
        self.assertEqual(items.next().ident, self.test_item_ids[1])
        self.assertEqual(items.next().ident, self.test_item_ids[2])
        self.assertEqual(items.next().ident, self.test_item_ids[3])
        self.assertEqual(items.next().ident, self.test_item_ids[0])

    def test_order_items(self):
        """Tests order_items"""
        self.catalog.order_items([
            self.test_item_ids[3],
            self.test_item_ids[2],
            self.test_item_ids[1],
            self.test_item_ids[0]],
            self.assessment.ident)
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).next().ident, self.test_item_ids[3])

    def _reorder_items(self):
        self.catalog.order_items([
            self.test_item_ids[0],
            self.test_item_ids[1],
            self.test_item_ids[2],
            self.test_item_ids[3]],
            self.assessment.ident)


class TestAssessmentOfferedLookupSession(unittest.TestCase):
    """Tests for AssessmentOfferedLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedLookupSession tests'
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_assessments_offered(self):
        """Tests can_lookup_assessments_offered"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_assessments_offered(), bool))

    def test_use_comparative_assessment_offered_view(self):
        """Tests use_comparative_assessment_offered_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_offered_view()

    def test_use_plenary_assessment_offered_view(self):
        """Tests use_plenary_assessment_offered_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_offered_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_offered(self):
        """Tests get_assessment_offered"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_offered_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_offered_list[0].ident)

    def test_get_assessments_offered_by_ids(self):
        """Tests get_assessments_offered_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))

    def test_get_assessments_offered_by_genus_type(self):
        """Tests get_assessments_offered_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))

    def test_get_assessments_offered_by_parent_genus_type(self):
        """Tests get_assessments_offered_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))

    def test_get_assessments_offered_by_record_type(self):
        """Tests get_assessments_offered_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))

    def test_get_assessments_offered_by_date(self):
        """Tests get_assessments_offered_by_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_offered_by_date(True, True)

    def test_get_assessments_offered_for_assessment(self):
        """Tests get_assessments_offered_for_assessment"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        results = self.session.get_assessments_offered_for_assessment(self.assessment.ident)
        self.assertEqual(results.available(), 2)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentOfferedList))

    def test_get_assessments_offered(self):
        """Tests get_assessments_offered"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered()
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))

    def test_get_assessment_offered_with_alias(self):
        self.catalog.alias_assessment_offered(self.assessment_offered_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment_offered(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_offered_ids[0])


class TestAssessmentOfferedQuerySession(unittest.TestCase):
    """Tests for AssessmentOfferedQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedQuerySession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedQuerySession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + color
            create_form.description = (
                'Test AssessmentOffered for AssessmentOfferedQuerySession tests, did I mention green')
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_assessments_offered(self):
        """Tests can_search_assessments_offered"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_assessments_offered(), bool))

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_offered_query()

    def test_get_assessments_offered_by_query(self):
        """Tests get_assessments_offered_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_assessment_offered_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessments_offered_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_assessments_offered_by_query(query).available(), 3)


class TestAssessmentOfferedAdminSession(unittest.TestCase):
    """Tests for AssessmentOfferedAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedAdminSession tests'
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'new AssessmentOffered'
        create_form.description = 'description of AssessmentOffered'
        create_form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_assessment_offered(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_taken():
            cls.catalog.delete_assessment_taken(obj.ident)
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_assessments_offered(self):
        """Tests can_create_assessments_offered"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_assessments_offered(), bool))

    def test_can_create_assessment_offered_with_record_types(self):
        """Tests can_create_assessment_offered_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_assessment_offered_with_record_types(DEFAULT_TYPE), bool))

    def test_get_assessment_offered_form_for_create(self):
        """Tests get_assessment_offered_form_for_create"""
        form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_assessment_offered(self):
        """Tests create_assessment_offered"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOffered
        self.assertTrue(isinstance(self.osid_object, AssessmentOffered))
        self.assertEqual(self.osid_object.display_name.text, 'new AssessmentOffered')
        self.assertEqual(self.osid_object.description.text, 'description of AssessmentOffered')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_assessments_offered(self):
        """Tests can_update_assessments_offered"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_assessments_offered(), bool))

    def test_get_assessment_offered_form_for_update(self):
        """Tests get_assessment_offered_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_assessment_offered_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_assessment_offered(self):
        """Tests update_assessment_offered"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOffered
        form = self.catalog.get_assessment_offered_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_assessment_offered(form)
        self.assertTrue(isinstance(updated_object, AssessmentOffered))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_assessments_offered(self):
        """Tests can_delete_assessments_offered"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_assessments_offered(), bool))

    def test_delete_assessment_offered(self):
        """Tests delete_assessment_offered"""
        form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident, [])
        form.display_name = 'new Assessment Offered'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_assessment_offered(form)
        self.catalog.delete_assessment_offered(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_assessment_offered(osid_object.ident)

    def test_can_manage_assessment_offered_aliases(self):
        """Tests can_manage_assessment_offered_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_assessment_offered_aliases(), bool))

    def test_alias_assessment_offered(self):
        """Tests alias_assessment_offered"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_assessment_offered(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_assessment_offered(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestAssessmentOfferedBankSession(unittest.TestCase):
    """Tests for AssessmentOfferedBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentOfferedBankSession tests'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedBankSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedBankSession tests'
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)
        cls.svc_mgr.assign_assessment_offered_to_bank(
            cls.assessment_offered_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_assessment_offered_to_bank(
            cls.assessment_offered_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_assessment_offered_from_bank(
            cls.assessment_offered_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_assessment_offered_from_bank(
            cls.assessment_offered_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_lookup_assessment_offered_bank_mappings(self):
        """Tests can_lookup_assessment_offered_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_offered_bank_mappings()
        self.assertTrue(isinstance(result, bool))

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_offered_ids_by_bank(self):
        """Tests get_assessment_offered_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_assessment_offered_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_assessments_offered_by_bank(self):
        """Tests get_assessments_offered_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_assessments_offered_by_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentOfferedList))
        self.assertEqual(results.available(), 2)

    def test_get_assessment_offered_ids_by_banks(self):
        """Tests get_assessment_offered_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_assessment_offered_ids_by_banks(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_assessments_offered_by_banks(self):
        """Tests get_assessments_offered_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_assessments_offered_by_banks(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentOfferedList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_bank_ids_by_assessment_offered(self):
        """Tests get_bank_ids_by_assessment_offered"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_bank_ids_by_assessment_offered(self.assessment_offered_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_assessment_offered(self):
        """Tests get_banks_by_assessment_offered"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_banks_by_assessment_offered(self.assessment_offered_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssessmentOfferedBankAssignmentSession(unittest.TestCase):
    """Tests for AssessmentOfferedBankAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedBankAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentOfferedBankAssignmentSession tests'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedBankAssignmentSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedBankAssignmentSession tests'
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_assign_assessments_offered(self):
        """Tests can_assign_assessments_offered"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessments_offered()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_assessments_offered_to_bank(self):
        """Tests can_assign_assessments_offered_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessments_offered_to_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_bank_ids_for_assessment_offered(self):
        """Tests get_assignable_bank_ids_for_assessment_offered"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids_for_assessment_offered(self.catalog.ident, self.assessment_offered_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_assessment_offered_to_bank(self):
        """Tests assign_assessment_offered_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_assessments_offered()
        self.assertEqual(results.available(), 0)
        self.session.assign_assessment_offered_to_bank(self.assessment_offered_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments_offered()
        self.assertEqual(results.available(), 1)
        self.session.unassign_assessment_offered_from_bank(
            self.assessment_offered_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_assessment_offered_from_bank(self):
        """Tests unassign_assessment_offered_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_assessments_offered()
        self.assertEqual(results.available(), 0)
        self.session.assign_assessment_offered_to_bank(
            self.assessment_offered_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments_offered()
        self.assertEqual(results.available(), 1)
        self.session.unassign_assessment_offered_from_bank(
            self.assessment_offered_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments_offered()
        self.assertEqual(results.available(), 0)

    def test_reassign_assessment_offered_to_billing(self):
        """Tests reassign_assessment_offered_to_billing"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reassign_assessment_offered_to_billing(True, True, True)


class TestAssessmentTakenLookupSession(unittest.TestCase):
    """Tests for AssessmentTakenLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentOfferedLookupSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenLookupSession tests'
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                for offered in catalog.get_assessments_offered_for_assessment(obj.ident):
                    for taken in catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                        catalog.delete_assessment_taken(taken.ident)
                    catalog.delete_assessment_offered(offered.ident)
                catalog.delete_assessment(obj.ident)
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_assessments_taken(self):
        """Tests can_lookup_assessments_taken"""
        # From test_templates/resource.py ResourceLookupSession.can_lookup_resources_template
        self.assertTrue(isinstance(self.catalog.can_lookup_assessments_taken(), bool))

    def test_use_comparative_assessment_taken_view(self):
        """Tests use_comparative_assessment_taken_view"""
        # From test_templates/resource.py ResourceLookupSession.use_comparative_resource_view_template
        self.catalog.use_comparative_assessment_taken_view()

    def test_use_plenary_assessment_taken_view(self):
        """Tests use_plenary_assessment_taken_view"""
        # From test_templates/resource.py ResourceLookupSession.use_plenary_resource_view_template
        self.catalog.use_plenary_assessment_taken_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_taken(self):
        """Tests get_assessment_taken"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_taken_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_taken_list[0].ident)

    def test_get_assessments_taken_by_ids(self):
        """Tests get_assessments_taken_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentTakenList))

    def test_get_assessments_taken_by_genus_type(self):
        """Tests get_assessments_taken_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentTakenList))

    def test_get_assessments_taken_by_parent_genus_type(self):
        """Tests get_assessments_taken_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, AssessmentTakenList))

    def test_get_assessments_taken_by_record_type(self):
        """Tests get_assessments_taken_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
        self.assertTrue(objects.available() == 0)
        self.assertTrue(isinstance(objects, AssessmentTakenList))

    def test_get_assessments_taken_by_date(self):
        """Tests get_assessments_taken_by_date"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_by_date(True, True)

    def test_get_assessments_taken_for_taker(self):
        """Tests get_assessments_taken_for_taker"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_for_taker(True)

    def test_get_assessments_taken_by_date_for_taker(self):
        """Tests get_assessments_taken_by_date_for_taker"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_by_date_for_taker(True, True, True)

    def test_get_assessments_taken_for_assessment(self):
        """Tests get_assessments_taken_for_assessment"""
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        takens = self.session.get_assessments_taken_for_assessment(self.assessment.ident)
        self.assertTrue(isinstance(takens, AssessmentTakenList))
        self.assertEqual(takens.available(), 2)

    def test_get_assessments_taken_by_date_for_assessment(self):
        """Tests get_assessments_taken_by_date_for_assessment"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_by_date_for_assessment(True, True, True)

    def test_get_assessments_taken_for_taker_and_assessment(self):
        """Tests get_assessments_taken_for_taker_and_assessment"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_for_taker_and_assessment(True, True)

    def test_get_assessments_taken_by_date_for_taker_and_assessment(self):
        """Tests get_assessments_taken_by_date_for_taker_and_assessment"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_by_date_for_taker_and_assessment(True, True, True, True)

    def test_get_assessments_taken_for_assessment_offered(self):
        """Tests get_assessments_taken_for_assessment_offered"""
        # From test_templates/learning.py::ActivityLookupSession::get_activities_for_objective_template
        results = self.session.get_assessments_taken_for_assessment_offered(self.assessment_offered.ident)
        self.assertEqual(results.available(), 2)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentTakenList))

    def test_get_assessments_taken_by_date_for_assessment_offered(self):
        """Tests get_assessments_taken_by_date_for_assessment_offered"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_by_date_for_assessment_offered(True, True, True)

    def test_get_assessments_taken_for_taker_and_assessment_offered(self):
        """Tests get_assessments_taken_for_taker_and_assessment_offered"""
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        takens = self.session.get_assessments_taken_for_taker_and_assessment_offered(
            self.catalog._proxy.get_effective_agent_id(),
            self.assessment_offered.ident)
        self.assertTrue(isinstance(takens, AssessmentTakenList))
        self.assertEqual(takens.available(), 2)

    def test_get_assessments_taken_by_date_for_taker_and_assessment_offered(self):
        """Tests get_assessments_taken_by_date_for_taker_and_assessment_offered"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_assessments_taken_by_date_for_taker_and_assessment_offered(True, True, True, True)

    def test_get_assessments_taken(self):
        """Tests get_assessments_taken"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken()
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken()
        self.assertTrue(objects.available() > 0)
        self.assertTrue(isinstance(objects, AssessmentTakenList))

    def test_get_assessment_taken_with_alias(self):
        self.catalog.alias_assessment_taken(self.assessment_taken_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment_taken(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_taken_ids[0])


class TestAssessmentTakenQuerySession(unittest.TestCase):
    """Tests for AssessmentTakenQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenLookupSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + color
            create_form.description = (
                'Test AssessmentTaken for AssessmentTakenQuerySession tests, did I mention green')
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)

    def setUp(self):
        self.session = self.catalog

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_taken():
                catalog.delete_assessment_taken(obj.ident)
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_search_assessments_taken(self):
        """Tests can_search_assessments_taken"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_assessments_taken(), bool))

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_federated_bin_view_template
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        # From test_templates/resource.py ResourceLookupSession.use_isolated_bin_view_template
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resource_query_template
        query = self.session.get_assessment_taken_query()

    def test_get_assessments_taken_by_query(self):
        """Tests get_assessments_taken_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.session.get_assessment_taken_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessments_taken_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.session.get_assessments_taken_by_query(query).available(), 3)


class TestAssessmentTakenAdminSession(unittest.TestCase):
    """Tests for AssessmentTakenAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenAdminSession tests'
        obj = cls.catalog.create_assessment_offered(create_form)
        cls.assessment_offered = obj
        form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
        form.display_name = 'new AssessmentTaken'
        form.description = 'description of AssessmentTaken'
        form.set_genus_type(NEW_TYPE)
        cls.osid_object = cls.catalog.create_assessment_taken(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_taken():
            cls.catalog.delete_assessment_taken(obj.ident)
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # From test_templates/resource.py ResourceLookupSession.get_bin_id_template
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_assessments_taken(self):
        """Tests can_create_assessments_taken"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_assessments_taken(), bool))

    def test_can_create_assessment_taken_with_record_types(self):
        """Tests can_create_assessment_taken_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_assessment_taken_with_record_types(DEFAULT_TYPE), bool))

    def test_get_assessment_taken_form_for_create(self):
        """Tests get_assessment_taken_form_for_create"""
        form = self.catalog.get_assessment_taken_form_for_create(self.assessment_offered.ident, [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_assessment_taken(self):
        """Tests create_assessment_taken"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTaken
        self.assertTrue(isinstance(self.osid_object, AssessmentTaken))
        self.assertEqual(self.osid_object.display_name.text, 'new AssessmentTaken')
        self.assertEqual(self.osid_object.description.text, 'description of AssessmentTaken')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_assessments_taken(self):
        """Tests can_update_assessments_taken"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_assessments_taken(), bool))

    def test_get_assessment_taken_form_for_update(self):
        """Tests get_assessment_taken_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_assessment_taken_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_assessment_taken(self):
        """Tests update_assessment_taken"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTaken
        form = self.catalog.get_assessment_taken_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_assessment_taken(form)
        self.assertTrue(isinstance(updated_object, AssessmentTaken))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_assessments_taken(self):
        """Tests can_delete_assessments_taken"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_assessments_taken(), bool))

    def test_delete_assessment_taken(self):
        """Tests delete_assessment_taken"""
        form = self.catalog.get_assessment_taken_form_for_create(self.assessment_offered.ident, [])
        form.display_name = 'new Assessment Taken'
        form.set_genus_type(NEW_TYPE)
        osid_object = self.catalog.create_assessment_taken(form)
        self.catalog.delete_assessment_taken(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_assessment_taken(osid_object.ident)

    def test_can_manage_assessment_taken_aliases(self):
        """Tests can_manage_assessment_taken_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_assessment_taken_aliases(), bool))

    def test_alias_assessment_taken(self):
        """Tests alias_assessment_taken"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_assessment_taken(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_assessment_taken(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestAssessmentTakenBankSession(unittest.TestCase):
    """Tests for AssessmentTakenBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentTakenBankSession tests'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenBankSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenLBankSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenLookupSession tests'
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)
        cls.svc_mgr.assign_assessment_taken_to_bank(
            cls.assessment_taken_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_assessment_taken_to_bank(
            cls.assessment_taken_ids[2], cls.assigned_catalog.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_assessment_taken_from_bank(
            cls.assessment_taken_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_assessment_taken_from_bank(
            cls.assessment_taken_ids[2], cls.assigned_catalog.ident)
        for obj in cls.catalog.get_assessments_taken():
            cls.catalog.delete_assessment_taken(obj.ident)
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_lookup_assessment_taken_bank_mappings(self):
        """Tests can_lookup_assessment_taken_bank_mappings"""
        # From test_templates/resource.py::ResourceBinSession::can_lookup_resource_bin_mappings
        result = self.session.can_lookup_assessment_taken_bank_mappings()
        self.assertTrue(isinstance(result, bool))

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_taken_ids_by_bank(self):
        """Tests get_assessment_taken_ids_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bin_template
        objects = self.svc_mgr.get_assessment_taken_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    def test_get_assessments_taken_by_bank(self):
        """Tests get_assessments_taken_by_bank"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bin_template
        results = self.session.get_assessments_taken_by_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentTakenList))
        self.assertEqual(results.available(), 2)

    def test_get_assessment_taken_ids_by_banks(self):
        """Tests get_assessment_taken_ids_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resource_ids_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        object_ids = self.session.get_assessment_taken_ids_by_banks(catalog_ids)
        self.assertTrue(isinstance(object_ids, IdList))
        # Currently our impl does not remove duplicate objectIds
        self.assertEqual(object_ids.available(), 5)

    def test_get_assessments_taken_by_banks(self):
        """Tests get_assessments_taken_by_banks"""
        # From test_templates/resource.py::ResourceBinSession::get_resources_by_bins_template
        catalog_ids = [self.catalog.ident, self.assigned_catalog.ident]
        results = self.session.get_assessments_taken_by_banks(catalog_ids)
        self.assertTrue(isinstance(results, ABCObjects.AssessmentTakenList))
        # Currently our impl does not remove duplicate objects
        self.assertEqual(results.available(), 5)

    def test_get_bank_ids_by_assessment_taken(self):
        """Tests get_bank_ids_by_assessment_taken"""
        # From test_templates/resource.py::ResourceBinSession::get_bin_ids_by_resource_template
        cats = self.svc_mgr.get_bank_ids_by_assessment_taken(self.assessment_taken_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_assessment_taken(self):
        """Tests get_banks_by_assessment_taken"""
        # From test_templates/resource.py::ResourceBinSession::get_bins_by_resource_template
        cats = self.svc_mgr.get_banks_by_assessment_taken(self.assessment_taken_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssessmentTakenBankAssignmentSession(unittest.TestCase):
    """Tests for AssessmentTakenBankAssignmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenBankAssignmentSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentTakenBankAssignmentSession tests'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenBankAssignmentSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenBankAssignmentSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenBankAssignmentSession tests'
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)

    def setUp(self):
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_taken():
            cls.catalog.delete_assessment_taken(obj.ident)
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_assign_assessments_taken(self):
        """Tests can_assign_assessments_taken"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_template
        result = self.session.can_assign_assessments_taken()
        self.assertTrue(isinstance(result, bool))

    def test_can_assign_assessments_taken_to_bank(self):
        """Tests can_assign_assessments_taken_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::can_assign_resources_to_bin_template
        result = self.session.can_assign_assessments_taken_to_bank(self.assigned_catalog.ident)
        self.assertTrue(isinstance(result, bool))

    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids(self.catalog.ident)
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_get_assignable_bank_ids_for_assessment_taken(self):
        """Tests get_assignable_bank_ids_for_assessment_taken"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::get_assignable_bin_ids_for_item_template
        # Note that our implementation just returns all catalogIds, which does not follow
        #   the OSID spec (should return only the catalogIds below the given one in the hierarchy.
        results = self.session.get_assignable_bank_ids_for_assessment_taken(self.catalog.ident, self.assessment_taken_ids[0])
        self.assertTrue(isinstance(results, IdList))

        # Because we're not deleting all banks from all tests, we might
        #   have some crufty banks here...but there should be at least 2.
        self.assertTrue(results.available() >= 2)

    def test_assign_assessment_taken_to_bank(self):
        """Tests assign_assessment_taken_to_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::assign_resource_to_bin_template
        results = self.assigned_catalog.get_assessments_taken()
        self.assertEqual(results.available(), 0)
        self.session.assign_assessment_taken_to_bank(self.assessment_taken_ids[1], self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments_taken()
        self.assertEqual(results.available(), 1)
        self.session.unassign_assessment_taken_from_bank(
            self.assessment_taken_ids[1],
            self.assigned_catalog.ident)

    def test_unassign_assessment_taken_from_bank(self):
        """Tests unassign_assessment_taken_from_bank"""
        # From test_templates/resource.py::ResourceBinAssignmentSession::unassign_resource_from_bin_template
        results = self.assigned_catalog.get_assessments_taken()
        self.assertEqual(results.available(), 0)
        self.session.assign_assessment_taken_to_bank(
            self.assessment_taken_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments_taken()
        self.assertEqual(results.available(), 1)
        self.session.unassign_assessment_taken_from_bank(
            self.assessment_taken_ids[1],
            self.assigned_catalog.ident)
        results = self.assigned_catalog.get_assessments_taken()
        self.assertEqual(results.available(), 0)

    def test_reassign_assessment_taken_to_billing(self):
        """Tests reassign_assessment_taken_to_billing"""
        with self.assertRaises(errors.Unimplemented):
            self.session.reassign_assessment_taken_to_billing(True, True, True)


class TestBankLookupSession(unittest.TestCase):
    """Tests for BankLookupSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for assessment proxy manager tests'
            catalog = cls.svc_mgr.create_bank(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    def setUp(self):
        # From test_templates/resource.py::BinLookupSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinLookupSession::init_template
        for catalog in cls.svc_mgr.get_banks():
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_can_lookup_banks(self):
        """Tests can_lookup_banks"""
        # From test_templates/resource.py::BinLookupSession::can_lookup_bins_template
        self.assertTrue(isinstance(self.session.can_lookup_banks(), bool))

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_bank(self):
        """Tests get_bank"""
        # From test_templates/resource.py::BinLookupSession::get_bin_template
        catalog = self.svc_mgr.get_bank(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_banks_by_ids(self):
        """Tests get_banks_by_ids"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_ids_template
        catalogs = self.svc_mgr.get_banks_by_ids(self.catalog_ids)
        self.assertTrue(catalogs.available() == 2)
        self.assertTrue(isinstance(catalogs, ABCObjects.BankList))
        reversed_catalog_ids = [str(cat_id) for cat_id in self.catalog_ids][::-1]
        for index, catalog in enumerate(catalogs):
            self.assertEqual(str(catalog.ident),
                             reversed_catalog_ids[index])

    def test_get_banks_by_genus_type(self):
        """Tests get_banks_by_genus_type"""
        # From test_templates/resource.py::BinLookupSession::get_bins_by_genus_type_template
        catalogs = self.svc_mgr.get_banks_by_genus_type(DEFAULT_GENUS_TYPE)
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.BankList))

    def test_get_banks_by_parent_genus_type(self):
        """Tests get_banks_by_parent_genus_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_banks_by_parent_genus_type(True)

    def test_get_banks_by_record_type(self):
        """Tests get_banks_by_record_type"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_banks_by_record_type(True)

    def test_get_banks_by_provider(self):
        """Tests get_banks_by_provider"""
        with self.assertRaises(errors.Unimplemented):
            self.session.get_banks_by_provider(True)

    def test_get_banks(self):
        """Tests get_banks"""
        # From test_templates/resource.py::BinLookupSession::get_bins_template
        catalogs = self.svc_mgr.get_banks()
        self.assertTrue(catalogs.available() > 0)
        self.assertTrue(isinstance(catalogs, ABCObjects.BankList))


class TestBankQuerySession(unittest.TestCase):
    """Tests for BankQuerySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinQuerySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        cls.fake_id = Id('resource.Resource%3A1%40ODL.MIT.EDU')

    def setUp(self):
        # From test_templates/resource.py::BinQuerySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinQuerySession::init_template
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_can_search_banks(self):
        """Tests can_search_banks"""
        # From test_templates/resource.py ResourceQuerySession::can_search_resources_template
        self.assertTrue(isinstance(self.session.can_search_banks(), bool))

    def test_get_bank_query(self):
        """Tests get_bank_query"""
        # From test_templates/resource.py::BinQuerySession::get_bin_query_template
        query = self.session.get_bank_query()
        self.assertTrue(isinstance(query, ABCQueries.BankQuery))

    def test_get_banks_by_query(self):
        """Tests get_banks_by_query"""
        # From test_templates/resource.py::BinQuerySession::get_bins_by_query_template
        query = self.session.get_bank_query()
        query.match_display_name('Test catalog')
        self.assertEqual(self.session.get_banks_by_query(query).available(), 1)
        query.clear_display_name_terms()
        query.match_display_name('Test catalog', match=False)
        self.assertEqual(self.session.get_banks_by_query(query).available(), 0)


class TestBankAdminSession(unittest.TestCase):
    """Tests for BankAdminSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank For Deletion'
        create_form.description = 'Test Bank for BankAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::BinAdminSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinAdminSession::init_template
        for catalog in cls.svc_mgr.get_banks():
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_can_create_banks(self):
        """Tests can_create_banks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_banks(), bool))

    def test_can_create_bank_with_record_types(self):
        """Tests can_create_bank_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_bank_with_record_types(DEFAULT_TYPE), bool))

    def test_get_bank_form_for_create(self):
        """Tests get_bank_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.assessment.objects import BankForm
        catalog_form = self.svc_mgr.get_bank_form_for_create([])
        self.assertTrue(isinstance(catalog_form, BankForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_bank(self):
        """Tests create_bank"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.assessment.objects import Bank
        catalog_form = self.svc_mgr.get_bank_form_for_create([])
        catalog_form.display_name = 'Test Bank'
        catalog_form.description = 'Test Bank for BankAdminSession.create_bank tests'
        new_catalog = self.svc_mgr.create_bank(catalog_form)
        self.assertTrue(isinstance(new_catalog, Bank))

    def test_can_update_banks(self):
        """Tests can_update_banks"""
        # From test_templates/resource.py BinAdminSession.can_update_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_update_banks(), bool))

    def test_get_bank_form_for_update(self):
        """Tests get_bank_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.assessment.objects import BankForm
        catalog_form = self.svc_mgr.get_bank_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, BankForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_bank(self):
        """Tests update_bank"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_bank_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_bank(catalog_form)

    def test_can_delete_banks(self):
        """Tests can_delete_banks"""
        # From test_templates/resource.py BinAdminSession.can_delete_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_delete_banks(), bool))

    def test_delete_bank(self):
        """Tests delete_bank"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_bank(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_bank(cat_id)

    def test_can_manage_bank_aliases(self):
        """Tests can_manage_bank_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.svc_mgr.can_manage_bank_aliases(), bool))

    def test_alias_bank(self):
        """Tests alias_bank"""
        # From test_templates/resource.py BinAdminSession.alias_bin_template
        alias_id = Id('assessment.Bank%3Amy-alias%40ODL.MIT.EDU')
        self.svc_mgr.alias_bank(self.catalog_to_delete.ident, alias_id)
        aliased_catalog = self.svc_mgr.get_bank(alias_id)
        self.assertEqual(self.catalog_to_delete.ident, aliased_catalog.ident)


class TestBankHierarchySession(unittest.TestCase):
    """Tests for BankHierarchySession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bank ' + name
            cls.catalogs[name] = cls.svc_mgr.create_bank(create_form)
        cls.svc_mgr.add_root_bank(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchySession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchySession::init_template
        cls.svc_mgr.remove_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_banks(cls.catalogs['Root'].ident)
        cls.svc_mgr.remove_root_bank(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_bank(cls.catalogs[cat_name].ident)

    def test_get_bank_hierarchy_id(self):
        """Tests get_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bank_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_bank_hierarchy(self):
        """Tests get_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_bank_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_access_bank_hierarchy(self):
        """Tests can_access_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::can_access_objective_bank_hierarchy_template
        self.assertTrue(isinstance(self.svc_mgr.can_access_bank_hierarchy(), bool))

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_comparative_bin_view_template
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        # From test_templates/resource.py::BinLookupSession::use_plenary_bin_view_template
        self.svc_mgr.use_plenary_bank_view()

    def test_get_root_bank_ids(self):
        """Tests get_root_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bin_ids_template
        root_ids = self.svc_mgr.get_root_bank_ids()
        self.assertTrue(isinstance(root_ids, IdList))
        # probably should be == 1, but we seem to be getting test cruft,
        # and I can't pinpoint where it's being introduced.
        self.assertTrue(root_ids.available() >= 1)

    def test_get_root_banks(self):
        """Tests get_root_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_root_bins_template
        from dlkit.abstract_osid.assessment.objects import BankList
        roots = self.svc_mgr.get_root_banks()
        self.assertTrue(isinstance(roots, BankList))
        self.assertTrue(roots.available() == 1)

    def test_has_parent_banks(self):
        """Tests has_parent_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_parent_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_parent_banks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_banks(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_banks(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_banks(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_banks(self.catalogs['Root'].ident))

    def test_is_parent_of_bank(self):
        """Tests is_parent_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_parent_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_bank_ids(self):
        """Tests get_parent_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_bank_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_banks(self):
        """Tests get_parent_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_parent_bins_template
        from dlkit.abstract_osid.assessment.objects import BankList
        catalog_list = self.svc_mgr.get_parent_banks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BankList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    def test_is_ancestor_of_bank(self):
        """Tests is_ancestor_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_ancestor_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_ancestor_of_bank,
                          self.catalogs['Root'].ident,
                          self.catalogs['Child 1'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))
        # self.assertTrue(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Grandchild 1'].ident))
        # self.assertFalse(self.svc_mgr.is_ancestor_of_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))

    def test_has_child_banks(self):
        """Tests has_child_banks"""
        # From test_templates/resource.py::BinHierarchySession::has_child_bins_template
        self.assertTrue(isinstance(self.svc_mgr.has_child_banks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_banks(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_banks(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_banks(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_banks(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_bank(self):
        """Tests is_child_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_child_of_bin_template
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_bank(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_bank_ids(self):
        """Tests get_child_bank_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bin_ids_template
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_bank_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_banks(self):
        """Tests get_child_banks"""
        # From test_templates/resource.py::BinHierarchySession::get_child_bins_template
        from dlkit.abstract_osid.assessment.objects import BankList
        catalog_list = self.svc_mgr.get_child_banks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BankList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    def test_is_descendant_of_bank(self):
        """Tests is_descendant_of_bank"""
        # From test_templates/resource.py::BinHierarchySession::is_descendant_of_bin_template
        self.assertRaises(errors.Unimplemented,
                          self.svc_mgr.is_descendant_of_bank,
                          self.catalogs['Child 1'].ident,
                          self.catalogs['Root'].ident)
        # self.assertTrue(isinstance(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident),
        #     bool))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Child 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertTrue(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Grandchild 1'].ident,
        #     self.catalogs['Root'].ident))
        # self.assertFalse(self.svc_mgr.is_descendant_of_bank(
        #     self.catalogs['Root'].ident,
        #     self.catalogs['Child 1'].ident))

    def test_get_bank_node_ids(self):
        """Tests get_bank_node_ids"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_node_ids_template
        # Per the spec, perhaps counterintuitively this method returns a
        #  node, **not** a IdList...
        node = self.svc_mgr.get_bank_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))

    def test_get_bank_nodes(self):
        """Tests get_bank_nodes"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_nodes_template
        node = self.svc_mgr.get_bank_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        self.assertTrue(isinstance(node, OsidNode))
        self.assertFalse(node.is_root())
        self.assertFalse(node.is_leaf())
        self.assertTrue(node.get_child_ids().available(), 1)
        self.assertTrue(isinstance(node.get_child_ids(), IdList))
        self.assertTrue(node.get_parent_ids().available(), 1)
        self.assertTrue(isinstance(node.get_parent_ids(), IdList))


class TestBankHierarchyDesignSession(unittest.TestCase):
    """Tests for BankHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bank ' + name
            cls.catalogs[name] = cls.svc_mgr.create_bank(create_form)
        cls.svc_mgr.add_root_bank(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    def setUp(self):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        self.session = self.svc_mgr

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::BinHierarchyDesignSession::init_template
        cls.svc_mgr.remove_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_banks(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_bank(cls.catalogs[cat_name].ident)

    def test_get_bank_hierarchy_id(self):
        """Tests get_bank_hierarchy_id"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_id_template
        hierarchy_id = self.svc_mgr.get_bank_hierarchy_id()
        self.assertTrue(isinstance(hierarchy_id, Id))

    def test_get_bank_hierarchy(self):
        """Tests get_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchySession::get_bin_hierarchy_template
        hierarchy = self.svc_mgr.get_bank_hierarchy()
        self.assertTrue(isinstance(hierarchy, Hierarchy))

    def test_can_modify_bank_hierarchy(self):
        """Tests can_modify_bank_hierarchy"""
        # From test_templates/resource.py::BinHierarchyDesignSession::can_modify_bin_hierarchy_template
        self.assertTrue(isinstance(self.session.can_modify_bank_hierarchy(), bool))

    def test_add_root_bank(self):
        """Tests add_root_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_root_bin_template
        # this is tested in the setUpClass
        roots = self.session.get_root_banks()
        self.assertTrue(isinstance(roots, ABCObjects.BankList))
        self.assertEqual(roots.available(), 1)

    def test_remove_root_bank(self):
        """Tests remove_root_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_root_bin_template
        roots = self.session.get_root_banks()
        self.assertEqual(roots.available(), 1)

        create_form = self.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'new root'
        create_form.description = 'Test Bank root'
        new_bank = self.svc_mgr.create_bank(create_form)
        self.svc_mgr.add_root_bank(new_bank.ident)

        roots = self.session.get_root_banks()
        self.assertEqual(roots.available(), 2)

        self.session.remove_root_bank(new_bank.ident)

        roots = self.session.get_root_banks()
        self.assertEqual(roots.available(), 1)

    def test_add_child_bank(self):
        """Tests add_child_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::add_child_bin_template
        # this is tested in the setUpClass
        children = self.session.get_child_banks(self.catalogs['Root'].ident)
        self.assertTrue(isinstance(children, ABCObjects.BankList))
        self.assertEqual(children.available(), 2)

    def test_remove_child_bank(self):
        """Tests remove_child_bank"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bin_template
        children = self.session.get_child_banks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

        create_form = self.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'test child'
        create_form.description = 'Test Bank child'
        new_bank = self.svc_mgr.create_bank(create_form)
        self.svc_mgr.add_child_bank(
            self.catalogs['Root'].ident,
            new_bank.ident)

        children = self.session.get_child_banks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 3)

        self.session.remove_child_bank(
            self.catalogs['Root'].ident,
            new_bank.ident)

        children = self.session.get_child_banks(self.catalogs['Root'].ident)
        self.assertEqual(children.available(), 2)

    def test_remove_child_banks(self):
        """Tests remove_child_banks"""
        # From test_templates/resource.py::BinHierarchyDesignSession::remove_child_bins_template
        children = self.session.get_child_banks(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)

        create_form = self.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'test great grandchild'
        create_form.description = 'Test Bank child'
        new_bank = self.svc_mgr.create_bank(create_form)
        self.svc_mgr.add_child_bank(
            self.catalogs['Grandchild 1'].ident,
            new_bank.ident)

        children = self.session.get_child_banks(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 1)

        self.session.remove_child_banks(self.catalogs['Grandchild 1'].ident)

        children = self.session.get_child_banks(self.catalogs['Grandchild 1'].ident)
        self.assertEqual(children.available(), 0)
