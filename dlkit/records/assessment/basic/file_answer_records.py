"""
records.assessment.basic.file_answer_records.py
"""

from .simple_records import QuestionTextRecord,\
    QuestionTextFormRecord,\
    FileAnswerRecord,\
    FileAnswerFormRecord,\
    FilesAnswerRecord,\
    FilesAnswerFormRecord
from .base_records import MultiLanguageQuestionRecord, MultiLanguageQuestionFormRecord


class FileSubmissionQuestionRecord(QuestionTextRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'question-text',
        'file_submission'
    ]


class FileSubmissionQuestionFormRecord(QuestionTextFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'question-text',
        'file_submission'
    ]


class MultiLanguageFileSubmissionQuestionRecord(MultiLanguageQuestionRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'multi-language-question-text',
        'file_submission'
    ]


class MultiLanguageFileSubmissionQuestionFormRecord(MultiLanguageQuestionFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'multi-language-question-text',
        'file_submission'
    ]


class FileSubmissionAnswerRecord(FileAnswerRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'file-answer',
        'file-submission'
    ]


class FileSubmissionAnswerFormRecord(FileAnswerFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'file-answer',
        'file-submission'
    ]


class FilesSubmissionAnswerRecord(FilesAnswerRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'files-answer',
        'files-submission'
    ]


class FilesSubmissionAnswerFormRecord(FilesAnswerFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'files-answer',
        'files-submission'
    ]


class FilesSubmissionQuestionRecord(QuestionTextRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'files-submission',
        'question-text'
    ]


class FilesSubmissionQuestionFormRecord(QuestionTextFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'files-submission',
        'question-text'
    ]
