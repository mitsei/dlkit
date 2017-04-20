"""
records.assessment.basic.feedback_item_records.py
"""

from .wrong_answers import WrongAnswerItemRecord
# from dlkit.json_.osid.osid_errors import InvalidArgument
# from dlkit.primordium.id.primitives import Id


class FeedbackAnswerItemRecord(WrongAnswerItemRecord):
    """
    This is really only a marker implementation to indicate that
    this item can have answers which include a hint / feedback text.
    """
    _implemented_record_type_identifiers = [
        'answer-with-feedback',
        'wrong-answer'
    ]


class FeedbackAnswerItemFormRecord(WrongAnswerItemRecord):
    """
    This is really only a marker implementation to indicate that
    this item can have answers which include a hint / feedback text.
    """
    _implemented_record_type_identifiers = [
        'answer-with-feedback',
        'wrong-answer'
    ]
