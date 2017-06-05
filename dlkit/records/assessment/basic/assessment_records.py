"""
Establishes a "when reviewable" flag for items, like Moodle
Also adds records for supporting AssessmentPart child management
"""

from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records

from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid import objects as osid_objects
from dlkit.json_.osid.metadata import Metadata

from dlkit.primordium.id.primitives import Id
from dlkit.abstract_osid.osid.errors import IllegalState, InvalidArgument,\
    NoAccess, NotFound

from ...osid.base_records import ObjectInitRecord


class ReviewOptionsAssessmentOfferedRecord(ObjectInitRecord):
    """when reviewable option on assessment offereds"""
    _implemented_record_type_identifiers = [
        'review-options'
    ]

    def can_review_whether_correct_during_attempt(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['whetherCorrect']['duringAttempt'])

    def can_review_whether_correct_after_attempt(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['whetherCorrect']['afterAttempt'])

    def can_review_whether_correct_before_deadline(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['whetherCorrect']['beforeDeadline'])

    def can_review_whether_correct_after_deadline(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['whetherCorrect']['afterDeadline'])

    def can_review_solution_during_attempt(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['solution']['duringAttempt'])

    def can_review_solution_after_attempt(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['solution']['afterAttempt'])

    def can_review_solution_before_deadline(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['solution']['beforeDeadline'])

    def can_review_solution_after_deadline(self):
        """stub"""
        return bool(self.my_osid_object._my_map['reviewOptions']['solution']['afterDeadline'])

    def has_max_attempts(self):
        """stub"""
        if 'maxAttempts' not in self.my_osid_object._my_map or \
                self.my_osid_object._my_map['maxAttempts'] is None:
            return False
        return True

    def get_max_attempts(self):
        """stub"""
        if self.has_max_attempts():
            return self.my_osid_object._my_map['maxAttempts']
        raise IllegalState()

    max_attempts = property(fget=get_max_attempts)

    def get_object_map(self):
        obj_map = dict(self.my_osid_object._my_map)
        if obj_map['startTime'] is not None:
            start_time = obj_map['startTime']
            obj_map['startTime'] = dict()
            obj_map['startTime']['year'] = start_time.year
            obj_map['startTime']['month'] = start_time.month
            obj_map['startTime']['day'] = start_time.day
            obj_map['startTime']['hour'] = start_time.hour
            obj_map['startTime']['minute'] = start_time.minute
            obj_map['startTime']['second'] = start_time.second
            obj_map['startTime']['microsecond'] = start_time.microsecond
        if obj_map['deadline'] is not None:
            deadline = obj_map['deadline']
            obj_map['deadline'] = dict()
            obj_map['deadline']['year'] = deadline.year
            obj_map['deadline']['month'] = deadline.month
            obj_map['deadline']['day'] = deadline.day
            obj_map['deadline']['hour'] = deadline.hour
            obj_map['deadline']['minute'] = deadline.minute
            obj_map['deadline']['second'] = deadline.second
            obj_map['deadline']['microsecond'] = deadline.microsecond
        obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        return obj_map

    object_map = property(fget=get_object_map)


class ReviewOptionsAssessmentOfferedFormRecord(abc_assessment_records.AssessmentOfferedFormRecord,
                                               osid_records.OsidRecord):
    """form to set / update the reviewable option"""

    _implemented_record_type_identifiers = [
        'review-options'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(ReviewOptionsAssessmentOfferedFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['reviewOptions'] = \
            dict(self._review_options_metadata['default_object_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['whetherCorrect'] = \
            dict(self._whether_correct_metadata['default_object_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['duringAttempt'] = \
            bool(self._during_attempt_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['afterAttempt'] = \
            bool(self._after_attempt_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['beforeDeadline'] = \
            bool(self._before_deadline_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']['afterDeadline'] = \
            bool(self._after_deadline_metadata['default_boolean_values'][0])

        self.my_osid_object_form._my_map['reviewOptions']['solution'] = \
            dict(self._solutions_metadata['default_object_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['solution']['duringAttempt'] = False
        self.my_osid_object_form._my_map['reviewOptions']['solution']['afterAttempt'] = \
            bool(self._after_attempt_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['solution']['beforeDeadline'] = \
            bool(self._before_deadline_metadata['default_boolean_values'][0])
        self.my_osid_object_form._my_map['reviewOptions']['solution']['afterDeadline'] = \
            bool(self._after_deadline_metadata['default_boolean_values'][0])

        self.my_osid_object_form._my_map['maxAttempts'] = \
            list(self._max_attempts_metadata['default_integer_values'])[0]

    def _init_metadata(self):
        """stub"""
        self._review_options_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'review_options'),
            'element_label': 'Review Options',
            'instructions': 'Choose various Review Options',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._whether_correct_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'report_correct'),
            'element_label': 'Report Correct',
            'instructions': 'Choose when to report correct answer to Taker',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._solutions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'review_solutions'),
            'element_label': 'Review Solutions / Explanations',
            'instructions': 'Choose when to report a solution or explanation text blob, when available',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._during_attempt_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'during-attempt'),
            'element_label': 'During Attempt',
            'instructions': 'accepts a boolean (True/False) value',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }
        self._after_attempt_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'during-attempt'),
            'element_label': 'During Attempt',
            'instructions': 'accepts a boolean (True/False) value',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }
        self._before_deadline_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'during-attempt'),
            'element_label': 'During Attempt',
            'instructions': 'accepts a boolean (True/False) value',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }
        self._after_deadline_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'during-attempt'),
            'element_label': 'During Attempt',
            'instructions': 'accepts a boolean (True/False) value',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': [True],
            'syntax': 'BOOLEAN',
        }
        self._min_max_attempts_value = None
        self._max_max_attempts_value = None
        self._max_attempts_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'max_attempts'),
            'element_label': 'Maximum Attempts',
            'instructions': 'enter an integer value for maximum attempts',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [None],
            'syntax': 'INTEGER',
            'minimum_integer': self._min_max_attempts_value,
            'maximum_integer': self._max_max_attempts_value,
            'integer_set': []
        }

    def get_review_options_metadata(self):
        """stub"""
        return Metadata(**self._review_options_metadata)

    def get_whether_correct_metadata(self):
        """stub"""
        return Metadata(**self._whether_correct_metadata)

    def get_during_attempt_metadata(self):
        """stub"""
        return Metadata(**self._during_attempt_metadata)

    def get_after_attempt_metadata(self):
        """stub"""
        return Metadata(**self._after_attempt_metadata)

    def get_before_deadline_metadata(self):
        """stub"""
        return Metadata(**self._before_deadline_metadata)

    def get_after_deadline_metadata(self):
        """stub"""
        return Metadata(**self._after_deadline_metadata)

    def set_review_whether_correct(self,
                                   during_attempt=None,
                                   after_attempt=None,
                                   before_deadline=None,
                                   after_deadline=None):
        """stub"""
        whether_correct = self.my_osid_object_form._my_map['reviewOptions']['whetherCorrect']
        if during_attempt is not None:
            whether_correct['duringAttempt'] = bool(during_attempt)
        if after_attempt is not None:
            whether_correct['afterAttempt'] = bool(after_attempt)
        if before_deadline is not None:
            whether_correct['beforeDeadline'] = bool(before_deadline)
        if after_deadline is not None:
            whether_correct['afterDeadline'] = bool(after_deadline)

    def set_review_solution(self,
                            during_attempt=None,
                            after_attempt=None,
                            before_deadline=None,
                            after_deadline=None):
        """stub"""
        solution = self.my_osid_object_form._my_map['reviewOptions']['solution']
        if during_attempt is not None:
            solution['duringAttempt'] = bool(during_attempt)
        if after_attempt is not None:
            solution['afterAttempt'] = bool(after_attempt)
        if before_deadline is not None:
            solution['beforeDeadline'] = bool(before_deadline)
        if after_deadline is not None:
            solution['afterDeadline'] = bool(after_deadline)

    def get_max_attempts_metadata(self):
        """stub"""
        return Metadata(**self._max_attempts_metadata)

    def set_max_attempts(self, value):
        """stub"""
        if value is None:
            raise InvalidArgument('value must be an integer')
        if value is not None and not isinstance(value, int):
            raise InvalidArgument('value is not an integer')
        if not self.my_osid_object_form._is_valid_integer(value,
                                                          self.get_max_attempts_metadata()):
            raise InvalidArgument('value must be an integer')
        self.my_osid_object_form._my_map['maxAttempts'] = value

    def clear_max_attempts(self):
        """stub"""
        if (self.get_max_attempts_metadata().is_read_only() or
                self.get_max_attempts_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['maxAttempts'] = \
            list(self._max_attempts_metadata['default_integer_values'])[0]


class ReviewOptionsAssessmentTakenRecord(ObjectInitRecord):
    """show review options on takens too"""
    _implemented_record_type_identifiers = [
        'review-options'
    ]

    def _get_section_for_question(self, question_id):
        sections = self.my_osid_object._get_assessment_sections()
        for section in sections:
            try:
                section.get_question(question_id)
                return section
            except NotFound:
                pass
        raise NotFound

    def can_review_solution(self, question_id):
        ao = self.my_osid_object.get_assessment_offered()
        try:
            section = self._get_section_for_question(question_id)
            section.get_response(question_id)
            attempt_complete = True
        except (IllegalState, NotFound):
            attempt_complete = False
        if ao.can_review_solution_during_attempt() and not attempt_complete:
            return True
        if ao.can_review_solution_after_attempt() and attempt_complete:
            return True
        return False

    def can_review_whether_correct(self):
        """stub"""
        ao = self.my_osid_object.get_assessment_offered()
        attempt_complete = self.my_osid_object.has_ended()
        if ao.can_review_whether_correct_during_attempt() and not attempt_complete:
            return True
        if ao.can_review_whether_correct_after_attempt and attempt_complete:
            return True
        return False

    def get_solution_for_question(self, question_id, section=None):
        try:
            if section is None:
                section = self._get_section_for_question(question_id)

            if self.can_review_solution(question_id):
                item = section._get_item(question_id)
                item_map = item.object_map
                answers = [a.object_map for a in item.get_answers()]
                try:
                    answers = answers + [a.object_map for a in item.get_wrong_answers()]
                except AttributeError:
                    # no wrong answers
                    pass
                try:
                    if 'solution' in item_map:
                        return {
                            'answers': answers,
                            'explanation': item_map['solution']  # fbw items
                        }
                    else:
                        return {
                            'answers': answers,
                            'explanation': item_map['texts']['solution']  # edX items
                        }
                except KeyError:
                    pass
        except KeyError:
            pass
        raise IllegalState()

    def _update_object_map(self, obj_map):
        """stub"""
        obj_map['reviewWhetherCorrect'] = self.can_review_whether_correct()


class ReviewOptionsAssessmentTakenFormRecord(abc_assessment_records.AssessmentTakenFormRecord,
                                             osid_records.OsidRecord):
    """form to create / update the taken options"""

    _implemented_record_type_identifiers = [
        'review-options'
    ]

    def __init__(self, osid_object_form):
        super(ReviewOptionsAssessmentTakenFormRecord, self).__init__()
