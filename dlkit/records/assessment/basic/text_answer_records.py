"""
records.assessment.basic.text_answer_records.py
"""

from .simple_records import QuestionTextRecord,\
    QuestionTextFormRecord,\
    TextAnswerFormRecord,\
    TextAnswerRecord,\
    QuestionTextsFormRecord,\
    QuestionTextsRecord,\
    TextsAnswerFormRecord,\
    TextsAnswerRecord


class ShortTextAnswerQuestionRecord(QuestionTextRecord):
    """
    # This is really only a marker implementation to indicate that a
    # short answer response will be required
    """
    _implemented_record_type_identifiers = [
        'question-text'
        'short-text-answer'
    ]


class ShortTextAnswerQuestionFormRecord(QuestionTextFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # short answer response will be required
    """
    _implemented_record_type_identifiers = [
        'question-text'
        'short-text-answer'
    ]


class ShortTextAnswerRecord(TextAnswerRecord):
    """short text as an answer"""
    _implemented_record_type_identifiers = [
        'short-text-answer'
    ]


class ShortTextAnswerFormRecord(TextAnswerFormRecord):
    """form for creating short-text answer"""
    _implemented_record_type_identifiers = [
        'short-text-answer'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(ShortTextAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)
        if not self.my_osid_object_form.is_for_update():
            TextAnswerFormRecord._init_map(self)
        self.set_max_string_length(128)


class ShortTextAnswersQuestionRecord(QuestionTextsRecord):
    """
    # This is really only a place-holder implementation to indicate that
    # multiple short answer responses will be required
    """
    _implemented_record_type_identifiers = [
        'question-texts'
        'short-answers'
    ]


class ShortTextAnswersQuestionFormRecord(QuestionTextsFormRecord):
    """
    # This is really only a place-holder implementation to indicate that
    # multiple short answer responses will be required
    """
    _implemented_record_type_identifiers = [
        'question-texts'
        'short-answers'
    ]


class ShortTextAnswersRecord(TextsAnswerRecord):
    """
    answer with multiple short texts
    """
    _implemented_record_type_identifiers = [
        'short-text-answers'
    ]


class ShortTextAnswersFormRecord(TextsAnswerFormRecord):
    """form for answer with multiple short texts"""

    _implemented_record_type_identifiers = [
        'short-text-answers'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(ShortTextAnswersFormRecord, self).__init__(
            osid_object_form=osid_object_form)
        if not self.my_osid_object_form.is_for_update():
            TextsAnswerFormRecord._init_map(self)
        self.set_max_string_length(128)


class ExtendedTextAnswerQuestionRecord(QuestionTextRecord):
    """
    # This is really only a place-holder implementation to indicate that
    # a short answer response will be required
    """
    _implemented_record_type_identifiers = [
        'question-text'
        'extended-text-answer'
    ]


class ExtendedTextAnswerQuestionFormRecord(QuestionTextFormRecord):
    """
    # This is really only a place-holder implementation to indicate that
    # a short answer response will be required
    """
    _implemented_record_type_identifiers = [
        'question-text'
        'extended-text-answer'
    ]


class ExtendedTextAnswerRecord(TextAnswerRecord):
    """answer with extended text"""
    _implemented_record_type_identifiers = [
        'extended-text-answer'
    ]


class ExtendedTextAnswerFormRecord(TextAnswerFormRecord):
    """ form for answer with extended text
    """
    _implemented_record_type_identifiers = [
        'extended-text-answer'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(ExtendedTextAnswerFormRecord, self).__init__(
            osid_object_form=osid_object_form)
        if not self.my_osid_object_form.is_for_update():
            TextAnswerFormRecord._init_map(self)
        self.set_max_string_length(None)
