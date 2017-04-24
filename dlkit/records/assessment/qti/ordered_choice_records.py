from dlkit.abstract_osid.osid.errors import IllegalState, NoAccess,\
    NotFound, InvalidArgument
from dlkit.json_.id.objects import IdList

from ..basic.multi_choice_records import MultiChoiceTextQuestionRecord,\
    MultiChoiceTextQuestionFormRecord, MultiChoiceFeedbackAndFilesAnswerFormRecord,\
    MultiChoiceFeedbackAndFilesAnswerRecord, MultiLanguageMultipleChoiceQuestionFormRecord,\
    MultiLanguageMultipleChoiceQuestionRecord
from ..basic.feedback_answer_records import MultiLanguageFeedbacksAnswerFormRecord,\
    MultiLanguageFeedbacksAnswerRecord
from ...osid.base_records import ObjectInitRecord


class OrderedChoiceItemRecord(ObjectInitRecord):
    _implemented_record_type_identifiers = [
        'ordered-choice'
    ]

    def _is_match(self, response, answer):
        # order matters, so can't do list(set())
        match = False
        num_match = 0
        answer_choice_set = [str(c) for c in answer.get_choice_ids()]
        response_choice_set = [str(c) for c in response.get_choice_ids()]
        if len(answer_choice_set) != len(response_choice_set):
            return match

        num_total = len(answer_choice_set)
        for index, choice in enumerate(response_choice_set):
            if answer_choice_set[index] == choice:
                num_match += 1
        if num_match == num_total:
            match = True
        return match

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
                if not answer.has_choice_ids():
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
