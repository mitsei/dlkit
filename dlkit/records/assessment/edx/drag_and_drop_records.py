"""
records.assessment.edx.drag_and_drop_records.py
"""

from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.osid import objects as osid_objects

from dlkit.abstract_osid.osid.errors import IllegalState, InvalidArgument

from .item_records import edXItemFormRecord, edXItemRecord
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


class EdXDragAndDropQuestionRecord(edXItemRecord,
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
        self._my_map['text']['text'] = \
            self._get_parameterized_text(config['paramaters'])

    def has_tolerance_value(self):
        """stub"""
        return 'tolerance' in self._my_map['decimalValues']

    def get_tolerance_value(self):
        """stub"""
        if self.has_tolerance_value():
            return self._my_map['decimalValues']['tolerance']
        raise IllegalState()

    tolerance = property(fget=get_tolerance_value)


class EdXDragAndDropQuestionFormRecord(edXItemFormRecord,
                                       QuestionTextFormRecord,
                                       QuestionFilesFormRecord):
    """form for edX numeric response question"""
    _implemented_record_type_identifiers = [
        'question-text',
        'question-files',
        'edx-item',
        'numeric-response-edx'
    ]

    def _init_map(self, **kwargs):
        """stub"""
        super(EdXDragAndDropQuestionFormRecord, self)._init_map(**kwargs)
        self._my_map['text']['text'] = ''


class EdXDragAndDropAnswerRecord(DecimalAnswerRecord,
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
        obj_map = dict(self._my_map)
        obj_map = osid_objects.OsidObject.get_object_map(self, obj_map)
        obj_map['decimalValue'] = self.get_decimal()
        return obj_map


class EdXDragAndDropAnswerFormRecord(DecimalAnswerFormRecord,
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
