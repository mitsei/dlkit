from __future__ import unicode_literals

import datetime
import unittest

from copy import deepcopy

from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.records.assessment.basic.assessment_records import *

from dlkit.json_.assessment.objects import AssessmentSection
from dlkit.json_.osid.objects import OsidObject, OsidObjectForm
from dlkit.json_.osid.queries import OsidObjectQuery
from dlkit.json_.osid.metadata import Metadata
from dlkit.records import registry
from dlkit.runtime import RUNTIME, PROXY_SESSION
from dlkit.runtime.proxy_example import SimpleRequest

from ... import utilities


ITEM_FORM_WITH_SOLUTION = Type(**registry.ITEM_RECORD_TYPES['with-solution'])
ASSESSMENT_FORM_SIMPLE_SEQUENCING = Type(**registry.ASSESSMENT_RECORD_TYPES['simple-child-sequencing'])
ASSESSMENT_OFFERED_REVIEWABLE = Type(**registry.ASSESSMENT_OFFERED_RECORD_TYPES['review-options'])
ASSESSMENT_TAKEN_REVIEWABLE = Type(**registry.ASSESSMENT_TAKEN_RECORD_TYPES['review-options'])


def get_assessment_manager():
    request = SimpleRequest(username='tester')
    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)
    return RUNTIME.get_service_manager('ASSESSMENT',
                                       implementation='TEST_SERVICE',
                                       proxy=proxy)


class TestReviewOptionsAssessmentOfferedRecord(unittest.TestCase):
    """Tests for ReviewOptionsAssessmentOfferedRecord"""

    @classmethod
    def setUpClass(cls):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['reviewOptions'] = {
            'whetherCorrect': {
                'duringAttempt': False,
                'afterAttempt': False,
                'beforeDeadline': False,
                'afterDeadline': False
            },
            'solution': {
                'duringAttempt': False,
                'afterAttempt': False,
                'beforeDeadline': False,
                'afterDeadline': False
            }
        }
        cls.osid_object = OsidObject(object_name='TEST_OBJECT',
                                     osid_object_map=obj_map)

    def setUp(self):
        self.review_offered_object = ReviewOptionsAssessmentOfferedRecord(self.osid_object)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_review_correct_during_attempt(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_whether_correct_during_attempt(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_whether_correct_during_attempt())

    def test_can_get_review_correct_after_attempt(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_whether_correct_after_attempt(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_whether_correct_after_attempt())

    def test_can_get_review_correct_before_deadline(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_whether_correct_before_deadline(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_whether_correct_before_deadline())

    def test_can_get_review_correct_after_deadline(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_whether_correct_after_deadline(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_whether_correct_after_deadline())

    def test_can_get_review_solution_during_attempt(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_solution_during_attempt(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_solution_during_attempt())

    def test_can_get_review_solution_after_attempt(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_solution_after_attempt(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_solution_after_attempt())

    def test_can_get_review_solution_before_deadline(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_solution_before_deadline(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_solution_before_deadline())

    def test_can_get_review_solution_after_deadline(self):
        self.assertTrue(isinstance(self.review_offered_object.can_review_solution_after_deadline(),
                                   bool))
        self.assertFalse(self.review_offered_object.can_review_solution_after_deadline())

    def test_can_test_has_attempts(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['maxAttempts'] = 5
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        review_offered_object = ReviewOptionsAssessmentOfferedRecord(osid_object)
        self.assertTrue(review_offered_object.has_max_attempts())
        self.assertFalse(self.review_offered_object.has_max_attempts())

    def test_get_attempts_throws_exception_if_no_attempts(self):
        with self.assertRaises(errors.IllegalState):
            self.review_offered_object.max_attempts

    def test_has_attempts_false_if_none(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['maxAttempts'] = None
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        review_offered_object = ReviewOptionsAssessmentOfferedRecord(osid_object)
        self.assertFalse(review_offered_object.has_max_attempts())

    def test_can_get_max_attempts(self):
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['maxAttempts'] = 2
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        review_offered_object = ReviewOptionsAssessmentOfferedRecord(osid_object)
        self.assertEqual(review_offered_object.max_attempts, 2)

    def test_can_get_object_map(self):
        utcnow = datetime.datetime.utcnow()
        utcfuture = utcnow + datetime.timedelta(hours=5)
        obj_map = deepcopy(utilities.TEST_OBJECT_MAP)
        obj_map['_id'] = 0
        obj_map['startTime'] = utcnow
        obj_map['deadline'] = utcfuture
        osid_object = OsidObject(object_name='TEST_OBJECT',
                                 osid_object_map=obj_map)
        review_offered_object = ReviewOptionsAssessmentOfferedRecord(osid_object)
        object_map = review_offered_object.object_map
        self.assertIn('startTime', object_map)
        self.assertIn('deadline', object_map)
        self.assertEqual(object_map['startTime'], {
            'year': utcnow.year,
            'month': utcnow.month,
            'day': utcnow.day,
            'hour': utcnow.hour,
            'minute': utcnow.minute,
            'second': utcnow.second,
            'microsecond': utcnow.microsecond
        })
        self.assertEqual(object_map['deadline'], {
            'year': utcfuture.year,
            'month': utcfuture.month,
            'day': utcfuture.day,
            'hour': utcfuture.hour,
            'minute': utcfuture.minute,
            'second': utcfuture.second,
            'microsecond': utcfuture.microsecond
        })


class TestReviewOptionsAssessmentOfferedFormRecord(unittest.TestCase):
    """Tests for ReviewOptionsAssessmentOfferedFormRecord"""

    @classmethod
    def setUpClass(cls):
        cls.osid_object_form = OsidObjectForm(object_name='TEST_OBJECT')
        cls.osid_object_form._authority = 'TESTING.MIT.EDU'
        cls.osid_object_form._namespace = 'records.Testing'

    def setUp(self):
        self.form = ReviewOptionsAssessmentOfferedFormRecord(self.osid_object_form)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_can_get_review_options_metadata(self):
        self.assertTrue(isinstance(self.form.get_review_options_metadata(), Metadata))

    def test_can_get_whether_correct_metadata(self):
        self.assertTrue(isinstance(self.form.get_whether_correct_metadata(), Metadata))

    def test_can_get_during_attempt_metadata(self):
        self.assertTrue(isinstance(self.form.get_during_attempt_metadata(), Metadata))

    def test_can_get_after_attempt_metadata(self):
        self.assertTrue(isinstance(self.form.get_after_attempt_metadata(), Metadata))

    def test_can_get_before_deadline_metadata(self):
        self.assertTrue(isinstance(self.form.get_before_deadline_metadata(), Metadata))

    def test_can_get_after_deadline_metadata(self):
        self.assertTrue(isinstance(self.form.get_after_deadline_metadata(), Metadata))

    def test_can_set_whether_correct(self):
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['duringAttempt'])
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['afterAttempt'])
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['beforeDeadline'])
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['afterDeadline'])
        self.form.set_review_whether_correct(during_attempt=False,
                                             after_attempt=False,
                                             before_deadline=False,
                                             after_deadline=False)
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['duringAttempt'])
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['afterAttempt'])
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['beforeDeadline'])
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['afterDeadline'])

    def test_can_set_review_solution(self):
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['duringAttempt'])
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['afterAttempt'])
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['beforeDeadline'])
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['afterDeadline'])
        self.form.set_review_solution(during_attempt=True,
                                      after_attempt=False,
                                      before_deadline=False,
                                      after_deadline=False)
        self.assertTrue(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['duringAttempt'])
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['afterAttempt'])
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['beforeDeadline'])
        self.assertFalse(self.form.my_osid_object_form._my_map['reviewOptions']['solution']['afterDeadline'])

    def test_can_get_max_attempts_metadata(self):
        self.assertTrue(isinstance(self.form.get_max_attempts_metadata(), Metadata))

    def test_can_set_max_attempts(self):
        self.assertIsNone(self.form.my_osid_object_form._my_map['maxAttempts'])
        self.form.set_max_attempts(4)
        self.assertEqual(self.form.my_osid_object_form._my_map['maxAttempts'], 4)

    def test_setting_max_attempts_with_none_throws_exception(self):
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_max_attempts(None)

    def test_setting_max_attempts_with_non_int_throws_exception(self):
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_max_attempts(float(1.2))
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_max_attempts('0')

    def test_can_clear_max_attempts(self):
        self.form.set_max_attempts(4)
        self.assertEqual(self.form.my_osid_object_form._my_map['maxAttempts'], 4)
        self.form.clear_max_attempts()
        self.assertIsNone(self.form.my_osid_object_form._my_map['maxAttempts'])


class TestReviewOptionsAssessmentTakenRecord(unittest.TestCase):
    """Tests for ReviewOptionsAssessmentTakenRecord"""

    @classmethod
    def setUpClass(cls):
        cls.mgr = get_assessment_manager()
        form = cls.mgr.get_bank_form_for_create([])
        form.display_name = 'Bank for testing'
        cls.bank = cls.mgr.create_bank(form)

        form = cls.bank.get_item_form_for_create([ITEM_FORM_WITH_SOLUTION])
        form.set_solution('a solution')
        cls.item_1 = cls.bank.create_item(form)

        form = cls.bank.get_question_form_for_create(cls.item_1.ident, [])
        cls.bank.create_question(form)

        form = cls.bank.get_item_form_for_create([ITEM_FORM_WITH_SOLUTION])
        form.set_solution('a solution 2')
        cls.item_2 = cls.bank.create_item(form)

        form = cls.bank.get_question_form_for_create(cls.item_2.ident, [])
        cls.bank.create_question(form)

        form = cls.bank.get_assessment_form_for_create([ASSESSMENT_FORM_SIMPLE_SEQUENCING])
        form.display_name = 'assessment 1'
        cls.assessment = cls.bank.create_assessment(form)

        cls.bank.add_item(cls.assessment.ident, cls.item_1.ident)

        form = cls.bank.get_assessment_offered_form_for_create(cls.assessment.ident,
                                                               [ASSESSMENT_OFFERED_REVIEWABLE])
        cls.offered = cls.bank.create_assessment_offered(form)

    def setUp(self):
        form = self.bank.get_assessment_taken_form_for_create(self.offered.ident,
                                                              [ASSESSMENT_TAKEN_REVIEWABLE])
        self.taken = self.bank.create_assessment_taken(form)
        section = self.bank.get_first_assessment_section(self.taken.ident)
        question = self.bank.get_first_question(section.ident)
        self.taken = self.bank.get_assessment_taken(self.taken.ident)  # to update the taken map

    @classmethod
    def tearDownClass(cls):
        for assessment in cls.bank.get_assessments():
            for assessment_offered in cls.bank.get_assessments_offered_for_assessment(assessment.ident):
                for assessment_taken in cls.bank.get_assessments_taken_for_assessment_offered(assessment_offered.ident):
                    cls.bank.delete_assessment_taken(assessment_taken.ident)
                cls.bank.delete_assessment_offered(assessment_offered.ident)
            cls.bank.delete_assessment(assessment.ident)
        for item in cls.bank.get_items():
            cls.bank.delete_item(item.ident)
        cls.mgr.delete_bank(cls.bank.ident)

    def test_can_get_section_for_question(self):
        section = self.bank.get_first_assessment_section(self.taken.ident)
        question = self.bank.get_first_question(section.ident)
        self.assertTrue(isinstance(self.taken._get_section_for_question(question.ident),
                                   AssessmentSection))
        self.assertEqual(str(section.ident),
                         str(self.taken._get_section_for_question(question.ident).ident))

    def test_getting_section_throws_exception_for_external_question(self):
        with self.assertRaises(errors.NotFound):
            self.taken._get_section_for_question(self.item_2.ident)

    def test_can_review_solution_reads_correctly_from_offered(self):
        # This can be made better by testing all the combinations
        section = self.bank.get_first_assessment_section(self.taken.ident)
        question = self.bank.get_first_question(section.ident)
        self.assertTrue(self.taken.can_review_solution(question.ident))

    def test_can_review_correct_reads_correctly_from_offered(self):
        # This can be made better by testing all the combinations
        self.assertTrue(self.taken.can_review_whether_correct())

    def test_can_get_solution_for_question(self):
        section = self.bank.get_first_assessment_section(self.taken.ident)
        question = self.bank.get_first_question(section.ident)
        solution = self.taken.get_solution_for_question(question.ident)
        self.assertEqual(solution, {
            'answers': [],
            'explanation': {
                'text': 'a solution',
                'languageTypeId': '639-2%3AENG%40ISO',
                'formatTypeId': 'TextFormats%3APLAIN%40okapia.net',
                'scriptTypeId': '15924%3ALATN%40ISO'
            }
        })

    def test_can_get_updated_object_map(self):
        obj_map_to_test = {}
        self.taken._update_object_map(obj_map_to_test)
        self.assertEqual(obj_map_to_test, {
            'reviewWhetherCorrect': True
        })
