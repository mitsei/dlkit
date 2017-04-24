"""
records.assessment.edx.numeric_response_records.py
"""

from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.osid import objects as osid_objects
from dlkit.json_.id.objects import IdList

from dlkit.abstract_osid.osid.errors import IllegalState,\
    InvalidArgument, NotFound

from .item_records import edXItemFormRecord, edXItemRecord
from ..basic.base_records import ItemWithWrongAnswerLOsRecord
from ..basic.simple_records import DecimalAnswerRecord,\
    DecimalAnswerFormRecord,\
    QuestionFilesRecord,\
    TextAnswerFormRecord,\
    TextAnswerRecord,\
    QuestionTextFormRecord,\
    QuestionFilesFormRecord
from ..basic.text_answer_records import QuestionTextRecord
from ...osid.base_records import DecimalValuesFormRecord,\
    DecimalValuesRecord,\
    TextsFormRecord,\
    TextsRecord


class EdXNumericResponseItemRecord(ItemWithWrongAnswerLOsRecord,
                                   edXItemRecord):
    def _is_match(self, response, answer):
        lower_bound = answer.get_decimal() - answer.get_tolerance()
        upper_bound = answer.get_decimal() + answer.get_tolerance()
        return lower_bound <= response.get_decimal() <= upper_bound

    def is_correctness_available_for_response(self, response):
        """is a measure of correctness available for a particular mc response"""
        return True

    def is_response_correct(self, response):
        """returns True if response evaluates to an Item Answer that is 100 percent correct"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return True
        return False

    def get_correctness_for_response(self, response):
        """get measure of correctness available for a particular response"""
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 100
        for answer in self.my_osid_object.get_wrong_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 0

    def get_answer_for_response(self, response):
        for answer in self.my_osid_object.get_answers():
            if self._is_match(response, answer):
                return answer

        wrong_answers = None
        try:
            wrong_answers = list(self.my_osid_object.get_wrong_answers())
        except AttributeError:
            pass
        else:
            for answer in wrong_answers:
                if self._is_match(response, answer):
                    return answer

        # also look for generic incorrect answer
        if wrong_answers is not None:
            for answer in wrong_answers:
                if not answer.has_decimal_value():
                    return answer

        raise NotFound('no matching answer found for response')

    def is_feedback_available_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            return False
        try:
            return answer.has_feedback()
        except AttributeError:
            return False

    def get_feedback_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        return answer.get_feedback()  # raises IllegalState

    def get_confused_learning_objective_ids_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        try:
            return answer.get_confused_learning_objective_ids()
        except AttributeError:
            return IdList([])


class EdXNumericResponseItemFormRecord(edXItemFormRecord):
    pass


class edXNumericResponseQuestionRecord(edXItemRecord,
                                       QuestionTextRecord,
                                       QuestionFilesRecord):
    """edX numeric response question"""
    _implemented_record_type_identifiers = [
        'question-text',
        'question-files',
        'edx-item',
        'numeric-response-edx'
    ]

    def config(self, config):
        """stub"""
        self.my_osid_object._my_map['text']['text'] = \
            self._get_parameterized_text(config['paramaters'])

    def has_tolerance_value(self):
        """stub"""
        return 'tolerance' in self.my_osid_object._my_map['decimalValues']

    def get_tolerance_value(self):
        """stub"""
        if self.has_tolerance_value():
            return self.my_osid_object._my_map['decimalValues']['tolerance']
        raise IllegalState()

    tolerance = property(fget=get_tolerance_value)


class edXNumericResponseQuestionFormRecord(edXItemFormRecord,
                                           QuestionTextFormRecord,
                                           QuestionFilesFormRecord):
    """form for edX numeric response question"""
    _implemented_record_type_identifiers = [
        'question-text',
        'question-files',
        'edx-item',
        'numeric-response-edx'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(edXNumericResponseQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(edXNumericResponseQuestionFormRecord, self)._init_map()
        QuestionTextFormRecord._init_map(self)
        QuestionFilesFormRecord._init_map(self)
        self.my_osid_object_form._my_map['text']['text'] = ''

    def _init_metadata(self):
        """stub"""
        super(edXNumericResponseQuestionFormRecord, self)._init_metadata()
        QuestionTextFormRecord._init_metadata(self)
        QuestionFilesFormRecord._init_metadata(self)


class edXNumericResponseAnswerRecord(DecimalAnswerRecord,
                                     DecimalValuesRecord,
                                     TextAnswerRecord,
                                     TextsRecord):
    """answer record for numeric response"""
    _implemented_record_type_identifiers = [
        'decimal-answer',
        'item-decimal-values',
        'text-answer',
        'item-text-values',
        'numeric-response-edx'
    ]

    def get_tolerance(self):
        return self.get_decimal_value('tolerance')

    def get_object_map(self):
        obj_map = dict(self.my_osid_object._my_map)
        obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        obj_map['decimalValue'] = self.my_osid_object.get_decimal()
        return obj_map


class edXNumericResponseAnswerFormRecord(DecimalAnswerFormRecord,
                                         DecimalValuesFormRecord,
                                         TextAnswerFormRecord,
                                         TextsFormRecord):
    """answer form for numeric response"""
    _implemented_record_type_identifiers = [
        'decimal-answer',
        'item-decimal-values',
        'text-answer',
        'item-text-values',
        'numeric-response-edx'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(edXNumericResponseAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """call these all manually because non-cooperative"""
        DecimalAnswerFormRecord._init_map(self)
        DecimalValuesFormRecord._init_map(self)
        TextAnswerFormRecord._init_map(self)
        TextsFormRecord._init_map(self)
        super(edXNumericResponseAnswerFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        DecimalAnswerFormRecord._init_metadata(self)
        DecimalValuesFormRecord._init_metadata(self)
        TextAnswerFormRecord._init_metadata(self)
        TextsFormRecord._init_metadata(self)
        super(edXNumericResponseAnswerFormRecord, self)._init_metadata()

    def get_tolerance_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def set_tolerance_value(self, tolerance):
        """stub"""
        # include index because could be multiple response / tolerance pairs
        if not isinstance(tolerance, float):
            raise InvalidArgument('tolerance value must be a decimal')
        self.add_decimal_value(tolerance, 'tolerance')

    def clear_tolerance_value(self):
        self.clear_decimal_value('tolerance')
