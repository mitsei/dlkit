from ..basic.multi_choice_records import MultiChoiceTextQuestionRecord,\
    MultiChoiceTextQuestionFormRecord, MultiChoiceFeedbackAndFilesAnswerFormRecord,\
    MultiChoiceFeedbackAndFilesAnswerRecord, MultiLanguageMultipleChoiceQuestionFormRecord,\
    MultiLanguageMultipleChoiceQuestionRecord
from ..basic.feedback_answer_records import MultiLanguageFeedbacksAnswerFormRecord,\
    MultiLanguageFeedbacksAnswerRecord


class OrderedChoiceTextQuestionFormRecord(MultiChoiceTextQuestionFormRecord):
    _implemented_record_type_identifiers = [
        'ordered-choice-text'
    ]


class OrderedChoiceTextQuestionRecord(MultiChoiceTextQuestionRecord):
    _implemented_record_type_identifiers = [
        'ordered-choice-text'
    ]


class OrderedChoiceFeedbackAndFilesAnswerFormRecord(MultiChoiceFeedbackAndFilesAnswerFormRecord):
    _implemented_record_type_identifiers = [
        'ordered-choice-files-and-feedback'
    ]


class OrderedChoiceFeedbackAndFilesAnswerRecord(MultiChoiceFeedbackAndFilesAnswerRecord):
    _implemented_record_type_identifiers = [
        'ordered-choice-files-and-feedback'
    ]


class MultiLanguageOrderedChoiceQuestionFormRecord(MultiLanguageMultipleChoiceQuestionFormRecord):
    _implemented_record_type_identifiers = [
        'multi-language-ordered-choice-text'
    ]


class MultiLanguageOrderedChoiceQuestionRecord(MultiLanguageMultipleChoiceQuestionRecord):
    _implemented_record_type_identifiers = [
        'multi-language-ordered-choice-text'
    ]
