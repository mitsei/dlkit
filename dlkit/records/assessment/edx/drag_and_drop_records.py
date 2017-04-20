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

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(EdXDragAndDropQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(EdXDragAndDropQuestionFormRecord, self)._init_map()
        QuestionTextFormRecord._init_map(self)
        QuestionFilesFormRecord._init_map(self)
        self.my_osid_object_form._my_map['text']['text'] = ''

    def _init_metadata(self):
        """stub"""
        super(EdXDragAndDropQuestionFormRecord, self)._init_metadata()
        QuestionTextFormRecord._init_metadata(self)
        QuestionFilesFormRecord._init_metadata(self)


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
        obj_map = dict(self.my_osid_object._my_map)
        obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        obj_map['decimalValue'] = self.my_osid_object.get_decimal()
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
