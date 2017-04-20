"""
records.assessment.basic.wrong_answers.py
"""

from .simple_records import TextsAnswerRecord, TextsAnswerFormRecord
from ...osid.base_records import ObjectInitRecord
from ..registry import ANSWER_GENUS_TYPES

from dlkit.json_.assessment.objects import AnswerList
from dlkit.json_.id.objects import IdList

from dlkit.primordium.type.primitives import Type

WRONG_ANSWER_GENUS_TYPE = Type(**ANSWER_GENUS_TYPES['wrong-answer'])


class WrongAnswerItemRecord(ObjectInitRecord):
    """
    This is really only a marker implementation to indicate that
    this item includes wrong answers.
    """
    _implemented_record_type_identifiers = [
        'wrong-answer'
    ]

    def get_answers(self):
        """ override this so only right answers are returned
        :return:
        """
        all_answers = self.my_osid_object._my_map['answers']
        right_answers = [a for a in all_answers
                         if a['genusTypeId'] != str(WRONG_ANSWER_GENUS_TYPE)]
        return AnswerList(right_answers,
                          runtime=self.my_osid_object._runtime,
                          proxy=self.my_osid_object._proxy)

    answers = property(fget=get_answers)

    def get_answer_ids(self):
        """ override this so only right answer ids are returned
        :return:
        """
        id_list = []
        for answer in self.get_answers():
            id_list.append(answer.get_id())
        return IdList(id_list)

    answer_ids = property(fget=get_answer_ids)

    def get_wrong_answers(self):
        """ provide this method to return only wrong answers
        :return:
        """
        all_answers = self.my_osid_object._my_map['answers']
        wrong_answers = [a for a in all_answers
                         if a['genusTypeId'] == str(WRONG_ANSWER_GENUS_TYPE)]
        return AnswerList(wrong_answers,
                          runtime=self.my_osid_object._runtime,
                          proxy=self.my_osid_object._proxy)

    wrong_answers = property(fget=get_wrong_answers)

    def get_wrong_answer_ids(self):
        """provide this method to return only wrong answer ids"""
        id_list = []
        for answer in self.get_wrong_answers():
            id_list.append(answer.get_id())
        return IdList(id_list)

    wrong_answer_ids = property(fget=get_wrong_answer_ids)


class WrongAnswerItemFormRecord(TextsAnswerFormRecord):
    pass
