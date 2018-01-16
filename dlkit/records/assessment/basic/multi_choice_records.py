"""
records.basic.multi_choice_records
"""
from bson.objectid import ObjectId

from copy import deepcopy

from dlkit.json_.id.objects import IdList
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_ import types, utilities

from dlkit.abstract_osid.osid.errors import IllegalState, NoAccess, NotFound, InvalidArgument
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type
from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records

try:
    # python 2
    from urllib import quote
except ImportError:
    # python 3
    from urllib.parse import quote

from ...osid.base_records import ObjectInitRecord
from .feedback_answer_records import FeedbackAnswerFormRecord, FeedbackAnswerRecord,\
    MultiLanguageFeedbacksAnswerFormRecord, MultiLanguageFeedbacksAnswerRecord
from .feedback_item_records import FeedbackAnswerItemRecord, FeedbackAnswerItemFormRecord
from .simple_records import QuestionTextRecord, QuestionTextFormRecord,\
    QuestionTextAndFilesMixin, QuestionFilesRecord,\
    FilesAnswerRecord, FilesAnswerFormRecord
from .base_records import MultiLanguageQuestionFormRecord, MultiLanguageQuestionRecord

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


class BaseMultiChoiceQuestionRecord(ObjectInitRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'base_multi-choice'
    ]

    def get_choices(self):
        """stub"""
        if not self.my_osid_object._my_map['choices']:
            raise IllegalState()
        # return self.my_osid_object.object_map['choices']
        return self.my_osid_object._my_map['choices']

    def is_multi_answer(self):
        """stub"""
        return self.my_osid_object._my_map['multi_answer']

    choices = property(fget=get_choices)


class BaseMultiChoiceQuestionFormRecord(osid_records.OsidRecord):
    """A record for a ``QuestionForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'base-multi-choice'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(BaseMultiChoiceQuestionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['choices'] = []
        self.my_osid_object_form._my_map['multiAnswer'] = False

    def _init_metadata(self):
        """stub"""
        self._choices_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choices'),
            'element_label': 'Choices',
            'instructions': 'Enter as many choices as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [''],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._choice_name_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'question_string'),
            'element_label': 'choice name',
            'instructions': 'enter a short label for this choice',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [''],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        }
        self._multi_answer_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'multi_answer'),
            'element_label': 'Is Multi-Answer',
            'instructions': 'accepts a boolean (True/False) value',
            'required': True,
            'read_only': False,
            'linked': True,
            'array': False,
            'default_boolean_values': ['False'],
            'syntax': 'BOOLEAN',
            'id_set': []
        }

    def get_choices_metadata(self):
        """stub"""
        return Metadata(**self._choices_metadata)

    def clear_choice(self, choice):
        """stub"""
        if len(self.my_osid_object_form._my_map['choices']) == 0:
            raise IllegalState('there are currently no choices defined for this question')
        if (len(self.my_osid_object_form._my_map['choices']) == 1 and
                choice in self.my_osid_object_form._my_map['choices']):
            raise IllegalState()
        self.my_osid_object_form._my_map['choices'] = \
            [c for c in self.my_osid_object_form._my_map['choices'] if c != choice]

    def get_multi_answer_metadata(self):
        """stub"""
        return Metadata(**self._multi_answer_metadata)

    def set_multi_answer(self, multi_answer):
        """stub"""
        self.my_osid_object_form._my_map['multiAnswer'] = multi_answer


class BaseMultiChoiceTextQuestionRecord(BaseMultiChoiceQuestionRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'base-multi-choice-text'
    ]


class BaseMultiChoiceTextQuestionFormRecord(BaseMultiChoiceQuestionFormRecord):
    """A record for a ``QuestionForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'base-multi-choice-text'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(BaseMultiChoiceTextQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        super(BaseMultiChoiceTextQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(BaseMultiChoiceTextQuestionFormRecord, self)._init_metadata()
        self._choice_text_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choice_text'),
            'element_label': 'choice text',
            'instructions': 'enter the text for this choice',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [{
                'text': '',
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE),
            }],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 1024,
            'string_set': []
        }

    def add_choice(self, text, name='', identifier=None):
        """stub"""
        if not utilities.is_string(text):
            raise InvalidArgument('text is not a string')
        choice_display_text = self._choice_text_metadata['default_string_values'][0]
        choice_display_text['text'] = text
        if identifier is None:
            identifier = str(ObjectId())
        choice = {
            'id': identifier,
            'text': text,
            'name': name
        }
        self.my_osid_object_form._my_map['choices'].append(choice)
        return choice

    def edit_choice(self, choice_id, text, name=''):
        """edit an existing choice, to keep the ID the same"""
        for choice in self.my_osid_object_form._my_map['choices']:
            if choice['id'] == choice_id:
                if choice['text'] != text:
                    choice['text'] = text
                if choice['name'] != name and name != '':
                    choice['name'] = name
                break

    def remove_choice(self, choice_id):
        """remove a choice, given the id"""
        updated_choices = []
        for choice in self.my_osid_object_form._my_map['choices']:
            if choice['id'] != choice_id:
                updated_choices.append(choice)
        self.my_osid_object_form._my_map['choices'] = updated_choices

    @utilities.arguments_not_none
    def set_choice_order(self, choice_ids):
        """ reorder choices per the passed in list
        :param choice_ids:
        :return:
        """
        reordered_choices = []
        current_choice_ids = [c['id'] for c in self.my_osid_object_form._my_map['choices']]
        if set(choice_ids) != set(current_choice_ids):
            raise IllegalState('missing choices for choice order')

        for choice_id in choice_ids:
            for current_choice in self.my_osid_object_form._my_map['choices']:
                if choice_id == current_choice['id']:
                    reordered_choices.append(current_choice)
                    break

        self.my_osid_object_form._my_map['choices'] = reordered_choices


class BaseMultiChoiceFileQuestionRecord(BaseMultiChoiceQuestionRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'question-string',
        'multi-choice-file'
    ]


class BaseMultiChoiceFileQuestionFormRecord(BaseMultiChoiceQuestionFormRecord):
    """A record for a ``QuestionForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'base-multi-choice-file'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(BaseMultiChoiceFileQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        super(BaseMultiChoiceFileQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(BaseMultiChoiceFileQuestionFormRecord, self)._init_metadata()
        self._choice_file_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choice-file'),
            'element_label': 'Choice File',
            'instructions': 'accepts an Asset Id',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def add_choice(self, asset_id, name='', identifier=None):
        """stub"""
        if identifier is None:
            identifier = str(ObjectId())
        self.my_osid_object_form._my_map['choices'].append({
            'id': identifier,
            'assetId': str(asset_id),
            'name': name
        })
        return identifier


class MultiChoiceTextQuestionRecord(BaseMultiChoiceQuestionRecord, QuestionTextRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'question-text',
        'multi-choice-text'
    ]


class MultiChoiceTextAndFilesQuestionFormRecord(QuestionTextAndFilesMixin,
                                                BaseMultiChoiceTextQuestionFormRecord):
    _implemented_record_type_identifiers = [
        'question-text',
        'multi-choice-text',
        'multi-choice-files'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(MultiChoiceTextAndFilesQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        QuestionTextAndFilesMixin._init_map(self)
        BaseMultiChoiceTextQuestionFormRecord._init_map(self)
        super(MultiChoiceTextAndFilesQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        QuestionTextAndFilesMixin._init_metadata(self)
        BaseMultiChoiceTextQuestionFormRecord._init_metadata(self)
        super(MultiChoiceTextAndFilesQuestionFormRecord, self)._init_metadata()


class MultiChoiceTextAndFilesQuestionRecord(QuestionTextRecord,
                                            QuestionFilesRecord,
                                            BaseMultiChoiceQuestionRecord):
    _implemented_record_type_identifiers = [
        'question-text',
        'multi-choice-text',
        'multi-choice-files'
    ]

    def __init__(self, osid_object_form):
        super(MultiChoiceTextAndFilesQuestionRecord, self).__init__(osid_object_form)


class MultiChoiceTextQuestionFormRecord(BaseMultiChoiceTextQuestionFormRecord,
                                        QuestionTextFormRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'question-text',
        'multi-choice-text'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(MultiChoiceTextQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        QuestionTextFormRecord._init_map(self)
        super(MultiChoiceTextQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        QuestionTextFormRecord._init_metadata(self)
        super(MultiChoiceTextQuestionFormRecord, self)._init_metadata()


class MultiChoiceFileQuestionRecord(BaseMultiChoiceQuestionRecord, QuestionTextRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'question-text',
        'multi-choice-file'
    ]


class MultiChoiceFileQuestionFormRecord(BaseMultiChoiceFileQuestionFormRecord,
                                        QuestionTextFormRecord):
    """A record for a ``Question``.

    The methods specified by the record type are available through the
    underlying object.

    """

    _implemented_record_type_identifiers = [
        'question-text',
        'multi-choice-file'
    ]

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(MultiChoiceFileQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        super(MultiChoiceFileQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(MultiChoiceFileQuestionFormRecord, self)._init_metadata()


class MultiChoiceItemRecord(FeedbackAnswerItemRecord):
    """A record for a basic multi-choice ``Item``.

    Can evaluate provided Responses with related Answers

    """
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]

    def _is_match(self, response, answer):
        response_set = set([str(c) for c in response.get_choice_ids()])
        return response_set == set([str(c) for c in answer.get_choice_ids()])

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


class MultiChoiceItemFormRecord(FeedbackAnswerItemFormRecord):
    """A record for a basic multi-choice ``Item`` Form.

    Marker

    """
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]


class MultiChoiceAnswerRecord(osid_records.OsidRecord,
                              abc_assessment_records.AnswerRecord):
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(MultiChoiceAnswerRecord, self).__init__()

    def get_choice_ids(self):
        """stub"""
        return IdList(self.my_osid_object._my_map['choiceIds'])

    def has_choice_ids(self):
        """see if has a set of choiceIds"""
        return self.my_osid_object._my_map['choiceIds'] != []


class MultiChoiceAnswerFormRecord(osid_records.OsidRecord,
                                  abc_assessment_records.AnswerFormRecord):
    """A record for an ``AnswerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(MultiChoiceAnswerFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['choiceIds'] = \
            self._choice_ids_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        self._choice_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choice_ids'),
            'element_label': 'response set',
            'instructions': 'submit correct choice for answer',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
        }
        self._choice_id_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choice_id'),
            'element_label': 'response set',
            'instructions': 'submit correct choice for answer',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def get_choice_ids_metadata(self):
        """stub"""
        return Metadata(**self._choice_ids_metadata)

    def add_choice_id(self, choice_id):
        """stub"""
        if choice_id is not None:
            self.my_osid_object_form._my_map['choiceIds'].append(choice_id)

    def set_choice_ids(self, choice_ids):
        if not isinstance(choice_ids, list):
            raise IllegalState()
        self.my_osid_object_form._my_map['choiceIds'] = choice_ids

    def clear_choice_ids(self):
        """stub"""
        if (self.get_choice_ids_metadata().is_read_only() or
                self.get_choice_ids_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['choiceIds'] = \
            self._choice_ids_metadata['default_object_values'][0]


class MultiChoiceTextAnswerRecord(MultiChoiceAnswerRecord):
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-choice-text'
    ]


class MultiChoiceFeedbackAndFilesAnswerFormRecord(MultiChoiceAnswerFormRecord,
                                                  FilesAnswerFormRecord,
                                                  FeedbackAnswerFormRecord):
    _implemented_record_type_identifiers = [
        'answer-with-feedback',
        'multi-choice',
        'multi-choice-files'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(MultiChoiceFeedbackAndFilesAnswerFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        MultiChoiceAnswerFormRecord._init_map(self)
        FilesAnswerFormRecord._init_map(self)
        FeedbackAnswerFormRecord._init_map(self)
        super(MultiChoiceFeedbackAndFilesAnswerFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        MultiChoiceAnswerFormRecord._init_metadata(self)
        FilesAnswerFormRecord._init_metadata(self)
        FeedbackAnswerFormRecord._init_metadata(self)
        super(MultiChoiceFeedbackAndFilesAnswerFormRecord, self)._init_metadata()


class MultiChoiceFeedbackAndFilesAnswerRecord(FilesAnswerRecord,
                                              FeedbackAnswerRecord,
                                              MultiChoiceAnswerRecord):
    _implemented_record_type_identifiers = [
        'answer-with-feedback',
        'multi-choice',
        'multi-choice-files'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(MultiChoiceAnswerRecord, self).__init__()


class MultiChoiceTextAnswerFormRecord(MultiChoiceAnswerFormRecord):
    """A record for an ``AnswerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-choice-text'
    ]


class MultiChoiceFileAnswerRecord(MultiChoiceAnswerRecord):
    """A record for an ``Answer``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-choice-file'
    ]


class MultiChoiceFileAnswerFormRecord(MultiChoiceAnswerFormRecord):
    """A record for an ``AnswerForm``.

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-choice-file'
    ]


class MultiLanguageMultipleChoiceQuestionRecord(MultiLanguageQuestionRecord):
    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        try:
            self.my_osid_object._my_map['multiLanguageChoices'] = deepcopy(self.my_osid_object._original_choice_order)
        except AttributeError:
            self.my_osid_object._my_map['multiLanguageChoices'] = deepcopy(self.my_osid_object._my_map['choices'])
        super(MultiLanguageMultipleChoiceQuestionRecord, self).__init__(osid_object)

    def get_unrandomized_choices(self):
        unrandomized_choices = deepcopy(self.my_osid_object._my_map['multiLanguageChoices'])
        if len(unrandomized_choices) > 0:
            updated_choices = []
            for choice in unrandomized_choices:
                if 'texts' in choice:
                    filtered_choice = {
                        'id': choice['id'],
                        'text': self.get_matching_language_value('texts',
                                                                 dictionary=choice).text,
                        'name': choice['name']
                    }
                    updated_choices.append(filtered_choice)
                else:
                    break
            unrandomized_choices = updated_choices
        return unrandomized_choices

    def get_choices(self):
        """stub"""
        # ideally would return a displayText object in text ... except for legacy
        # use cases like OEA, it expects a text string.
        choices = []
        # for current_choice in self.my_osid_object.object_map['choices']:
        for current_choice in self.my_osid_object._my_map['choices']:
            filtered_choice = {
                'id': current_choice['id'],
                'text': self.get_matching_language_value('texts',
                                                         dictionary=current_choice).text,
                'name': current_choice['name']
            }
            choices.append(filtered_choice)
        return choices

    choices = property(fget=get_choices)

    def get_object_map(self):
        obj_map = super(MultiLanguageMultipleChoiceQuestionRecord, self).get_object_map()
        obj_map['choices'] = self.my_osid_object.get_choices()
        return obj_map

    object_map = property(fget=get_object_map)


class MultiLanguageMultipleChoiceQuestionFormRecord(MultiLanguageQuestionFormRecord):
    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageMultipleChoiceQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        super(MultiLanguageMultipleChoiceQuestionFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['choices'] = \
            self._choices_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        super(MultiLanguageMultipleChoiceQuestionFormRecord, self)._init_metadata()
        self._choices_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choices'),
            'element_label': 'choices',
            'instructions': 'Enter as many text choices as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_choices_metadata(self):
        """stub"""
        return Metadata(**self._choices_metadata)

    @utilities.arguments_not_none
    def add_choice(self, choice, name='', identifier=None):
        """stub"""
        if not isinstance(choice, DisplayText):
            raise InvalidArgument('choice is not a displayText object')
        if identifier is None:
            identifier = str(ObjectId())
        current_identifiers = [c['id'] for c in self.my_osid_object_form._my_map['choices']]
        if identifier not in current_identifiers:
            choice = {
                'id': identifier,
                'texts': [self._dict_display_text(choice)],
                'name': name
            }
            self.my_osid_object_form._my_map['choices'].append(choice)
        else:
            for current_choice in self.my_osid_object_form._my_map['choices']:
                if current_choice['id'] == identifier:
                    self.add_or_replace_value('texts', choice, dictionary=current_choice)
                    choice = current_choice
        return choice

    def clear_choices(self):
        """stub"""
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['choices'] = \
            self._choices_metadata['default_object_values'][0]

    @utilities.arguments_not_none
    def clear_choice_texts(self, choice_id):
        """stub"""
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()
        updated_choices = []
        for current_choice in self.my_osid_object_form._my_map['choices']:
            if current_choice['id'] != choice_id:
                updated_choices.append(current_choice)
            else:
                updated_choices.append({
                    'id': current_choice['id'],
                    'texts': [],
                    'name': current_choice['name']
                })
        self.my_osid_object_form._my_map['choices'] = updated_choices

    @utilities.arguments_not_none
    def remove_choice_language(self, language_type, choice_id):
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()

        choices = [c for c in self.my_osid_object_form._my_map['choices'] if c['id'] == choice_id]
        if len(choices) == 0:
            raise InvalidArgument('invalid choice_id')

        for current_choice in self.my_osid_object_form._my_map['choices']:
            if choice_id == current_choice['id']:
                self.remove_field_by_language('texts',
                                              language_type,
                                              dictionary=current_choice)

    @utilities.arguments_not_none
    def edit_choice(self, new_choice, choice_id):
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_choice, DisplayText):
            raise InvalidArgument('new choice is not a DisplayText object')
        choices = [c for c in self.my_osid_object_form._my_map['choices'] if c['id'] == choice_id]
        if len(choices) == 0:
            raise InvalidArgument('invalid choice_id')

        for current_choice in self.my_osid_object_form._my_map['choices']:
            if choice_id == current_choice['id']:
                index = self.get_index_of_language_type('texts',
                                                        new_choice.language_type,
                                                        dictionary=current_choice)

                current_choice['texts'][index] = self._dict_display_text(new_choice)

    @utilities.arguments_not_none
    def remove_choice(self, choice_id):
        """remove a choice, given the id"""
        updated_choices = []
        for choice in self.my_osid_object_form._my_map['choices']:
            if choice['id'] != choice_id:
                updated_choices.append(choice)
        self.my_osid_object_form._my_map['choices'] = updated_choices

    @utilities.arguments_not_none
    def set_choice_order(self, choice_ids):
        """ reorder choices per the passed in list
        :param choice_ids:
        :return:
        """
        reordered_choices = []
        current_choice_ids = [c['id'] for c in self.my_osid_object_form._my_map['choices']]
        if set(choice_ids) != set(current_choice_ids):
            raise IllegalState('missing choices for choice order')

        for choice_id in choice_ids:
            for current_choice in self.my_osid_object_form._my_map['choices']:
                if choice_id == current_choice['id']:
                    reordered_choices.append(current_choice)
                    break

        self.my_osid_object_form._my_map['choices'] = reordered_choices
