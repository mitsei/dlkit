import json

from bson import ObjectId

from copy import deepcopy

from dlkit.json_.id.objects import IdList  # inherits from osid_objects.OsidList, which is impl dependent

from dlkit.json_ import types, utilities
from dlkit.json_.assessment.objects import Question
from dlkit.json_.assessment.sessions import ItemLookupSession

from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records
from dlkit.abstract_osid.osid.errors import IllegalState, NoAccess,\
    InvalidArgument, NotFound
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type

from random import shuffle

try:
    # python 2
    from urllib import unquote, quote
except ImportError:
    # python 3
    from urllib.parse import unquote, quote

from ..basic.feedback_answer_records import FeedbackAnswerFormRecord, FeedbackAnswerRecord
from ..basic.simple_records import FilesAnswerRecord, FilesAnswerFormRecord,\
    QuestionTextRecord, QuestionTextFormRecord
from ..basic.base_records import MultiLanguageQuestionFormRecord, MultiLanguageQuestionRecord
from ...osid.base_records import ObjectInitRecord

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


MAGIC_AUTHORITY = 'magic-randomize-inline-choices-question-record'


class RandomizedInlineChoiceItemLookupSession(ItemLookupSession):
    """this session does "magic" unscrambling of Inline "fill in the blank"
        question items with
        unique IDs, where the choice order has been specified in the ID.

        For example, we want MC questions to be randomized when they
        are given to the students, so each student sees the choices in
        a different order.

        Student 1:

        Q) What is X?

        a) choice 1
        b) choice 0
        c) choice 3
        d) choice 2

        Student 2:

        Q) What is X?

        a) choice 2
        b) choice 1
        c) choice 0
        d) choice 3

        But in many situations, when the student views the question again
        (i.e. they don't answer and come back, they answer but want to see
        their history, etc.), we want to record the original ordering
        of choices, to reduce confusion. This is being preserved
        in a "magic" ID for the question, which captures the
        state / parameters of the question. This ID is then stored in the
        AssessmentTaken record for that student.

        This "magic" adapter session plugs into the AssessmentSession
        and the AssessmentResultsSession and looks for any question ID
        that is flagged as a Randomized MC Question. It then knows
        to set the choice order to match the previous state. All other
        items are passed along to the unaltered MongoDB ItemLookupSession.

        This adapter session has out-of-band knowledge of the authority
        of the items it needs to deconstruct -- i.e. from the DLKit
        records implementation.
    """
    def __init__(self, *args, **kwargs):
        super(RandomizedInlineChoiceItemLookupSession, self).__init__(*args, **kwargs)

    def get_item(self, item_id):
        authority = item_id.authority
        if authority == MAGIC_AUTHORITY:
            # for now, this will not work with aliased IDs...
            magic_identifier = unquote(item_id.identifier)
            original_identifier = magic_identifier.split('?')[0]
            choice_ids = json.loads(magic_identifier.split('?')[-1])
            original_item_id = Id(identifier=original_identifier,
                                  namespace=item_id.namespace,
                                  authority=self._catalog.ident.authority)
            orig_item = super(RandomizedInlineChoiceItemLookupSession, self).get_item(original_item_id)
            orig_item.set_params(choice_ids)
            return orig_item
        else:
            return super(RandomizedInlineChoiceItemLookupSession, self).get_item(item_id)


class MagicRandomizedInlineChoiceItemRecord(ObjectInitRecord):
    _implemented_record_type_identifiers = [
        'magic-randomized-inline-choice'
    ]

    def __init__(self, *args, **kwargs):
        super(MagicRandomizedInlineChoiceItemRecord, self).__init__(*args, **kwargs)
        self._magic_params = None

    def get_question(self):
        question = Question(osid_object_map=self.my_osid_object._my_map['question'],
                            runtime=self.my_osid_object._runtime,
                            proxy=self.my_osid_object._proxy)
        if self._magic_params is not None:
            question.set_values(self._magic_params)
        return question

    question = property(fget=get_question)

    def set_params(self, params):
        self._magic_params = params

    def _is_match(self, response, answer):
        match = False
        answer_choices = answer.get_inline_choice_ids()
        response_choices = response.get_inline_choice_ids()
        num_total_regions = len(list(answer_choices.keys()))
        num_matching_regions = 0
        if len(list(response_choices.keys())) == len(list(answer_choices.keys())):
            for inline_region, answer_region_choices in answer_choices.items():
                if set(list(answer_region_choices['choiceIds'])) == set(list(response_choices[inline_region]['choiceIds'])):
                    num_matching_regions += 1
            return num_matching_regions == num_total_regions
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
        for answer in self.get_answers():
            if self._is_match(response, answer):
                try:
                    return answer.get_score()
                except AttributeError:
                    return 100
        for answer in self.get_wrong_answers():
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
                if len(list(answer.get_inline_choice_ids().keys())) == 0:
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


class MagicRandomizedInlineChoiceItemFormRecord(osid_records.OsidRecord):
    """form for QTI numeric response question"""
    _implemented_record_type_identifiers = [
        'magic-randomized-inline-choice'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        super(MagicRandomizedInlineChoiceItemFormRecord, self).__init__()


class InlineChoiceTextQuestionFormRecord(QuestionTextFormRecord,
                                         osid_records.OsidRecord):
    """QTI inline choice i.e. fill-in-the-blank"""
    _implemented_record_type_identifiers = [
        'inline-choice-text'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(InlineChoiceTextQuestionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        QuestionTextFormRecord._init_map(self)
        self.my_osid_object_form._my_map['choices'] = \
            self._choices_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        QuestionTextFormRecord._init_metadata(self)
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
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
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

    def get_choices_metadata(self):
        """stub"""
        return Metadata(**self._choices_metadata)

    def add_choice(self, text, inline_region, name='', identifier=None):
        """stub"""
        choice_display_text = self._choice_text_metadata['default_string_values'][0]
        choice_display_text['text'] = text
        if identifier is None:
            identifier = str(ObjectId())
        choice = {
            'id': identifier,
            'text': text,
            'name': name
        }
        if inline_region in self.my_osid_object_form._my_map['choices']:
            self.my_osid_object_form._my_map['choices'][inline_region].append(choice)
        else:
            raise IllegalState('that inline region does not exist')
        return choice

    def edit_choice(self, choice_id, text, inline_region, name=''):
        """edit an existing choice, to keep the ID the same"""
        if inline_region not in self.my_osid_object_form._my_map['choices']:
            raise IllegalState('that inline region does not exist')
        for choice in self.my_osid_object_form._my_map['choices'][inline_region]:
            if choice['id'] == choice_id:
                if choice['text'] != text:
                    choice['text'] = text
                if choice['name'] != name and name != '':
                    choice['name'] = name
                break

    def add_inline_region(self, inline_region):
        if inline_region not in self.my_osid_object_form._my_map['choices']:
            self.my_osid_object_form._my_map['choices'][inline_region] = []
        else:
            raise IllegalState('that inline region already exists')

    def remove_inline_region(self, inline_region):
        if inline_region in self.my_osid_object_form._my_map['choices']:
            del self.my_osid_object_form._my_map['choices'][inline_region]
        else:
            raise IllegalState('that inline region does not exist')

    @utilities.arguments_not_none
    def remove_choice(self, choice_id, inline_region):
        """remove a choice, given the id"""
        if inline_region in self.my_osid_object_form._my_map['choices']:
            updated_choices = []
            for choice in self.my_osid_object_form._my_map['choices'][inline_region]:
                if choice['id'] != choice_id:
                    updated_choices.append(choice)
            self.my_osid_object_form._my_map['choices'][inline_region] = updated_choices

    @utilities.arguments_not_none
    def set_choice_order(self, choice_ids, inline_region):
        """ reorder choices per the passed in list
        :param choice_ids:
        :return:
        """
        reordered_choices = []
        current_choice_ids = [c['id'] for c in self.my_osid_object_form._my_map['choices'][inline_region]]
        if set(choice_ids) != set(current_choice_ids):
            raise IllegalState('missing choices for choice order')

        for choice_id in choice_ids:
            for current_choice in self.my_osid_object_form._my_map['choices'][inline_region]:
                if choice_id == current_choice['id']:
                    reordered_choices.append(current_choice)
                    break

        self.my_osid_object_form._my_map['choices'][inline_region] = reordered_choices


class InlineChoiceTextQuestionRecord(QuestionTextRecord,
                                     ObjectInitRecord):
    """A record for a ``Question``.
    You have to use this with the QTIQuestionRecord in order to get the shuffle key

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'inline-choice-text'
    ]

    def __init__(self, osid_object):
        self._original_choice_order = deepcopy(osid_object._my_map['choices'])
        super(InlineChoiceTextQuestionRecord, self).__init__(osid_object)
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        choices = self.my_osid_object._my_map['choices']
        if self.my_osid_object._my_map['shuffle']:
            for region, region_choices in choices.items():
                shuffle(region_choices)
                choices[region] = region_choices
        self.my_osid_object._my_map['choices'] = choices
        # Claim authority on this object, until someone else does:
        self.my_osid_object._authority = MAGIC_AUTHORITY

    def get_choices(self):
        """stub"""
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        # return self.my_osid_object.object_map['choices']
        return self.my_osid_object._my_map['choices']

    choices = property(fget=get_choices)

    def get_id(self):
        """override get_id to generate our "magic" ids that encode choice order"""

        # Check first to make sure no one else has claimed authority on my object.
        # This will likely occur when an AssessmentSection returns a Question
        # During an AssessmentSession
        if self.my_osid_object._authority != MAGIC_AUTHORITY:
            return self.my_osid_object._item_id
            # raise AttributeError

        # If not, go ahead and build magic Id:
        choices = self.my_osid_object._my_map['choices']
        magic_identifier = quote('{0}?{1}'.format(self.my_osid_object._my_map['_id'],
                                                  json.dumps(choices)))
        return Id(namespace='assessment.Item',
                  identifier=magic_identifier,
                  authority=MAGIC_AUTHORITY)

    ident = property(fget=get_id)
    id_ = property(fget=get_id)

    def get_unrandomized_choices(self):
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        return self._original_choice_order

    def set_values(self, choice_ids):
        """assume choice_ids is a dict of {
            region: choiceIds
         }, like: {
            "REGION_1": ["57978959cdfc5c42eefb36d1", "57978959cdfc5c42eefb36d0",
                         "57978959cdfc5c42eefb36cf", "57978959cdfc5c42eefb36ce"]
         }
        """
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        organized_regions = {}
        for region, choice_ids in choice_ids.items():
            organized_choice_ids = []
            for choice in choice_ids:
                original_region_choices = self._original_choice_order[region]
                choice_obj = [c for c in original_region_choices if c['id'] == choice['id']][0]
                organized_choice_ids.append(choice_obj)
            organized_regions[region] = organized_choice_ids
        self.my_osid_object._my_map['choices'] = organized_regions


class InlineChoiceFeedbackAndFilesAnswerFormRecord(FilesAnswerFormRecord,
                                                   FeedbackAnswerFormRecord,
                                                   osid_records.OsidRecord,
                                                   abc_assessment_records.AnswerFormRecord):
    _implemented_record_type_identifiers = [
        'inline-choice-text'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(InlineChoiceFeedbackAndFilesAnswerFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        FilesAnswerFormRecord._init_map(self)
        FeedbackAnswerFormRecord._init_map(self)
        self.my_osid_object_form._my_map['inlineRegions'] = \
            self._inline_regions_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        FilesAnswerFormRecord._init_metadata(self)
        FeedbackAnswerFormRecord._init_metadata(self)
        self._inline_regions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'inline_regions'),
            'element_label': 'set of inline regions',
            'instructions': 'submit correct choice for answer for each region',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
        }
        self._choice_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choice_ids'),
            'element_label': 'response set with inline regions',
            'instructions': 'submit correct choice for answer for each region',
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

    def get_inline_regions_metadata(self):
        """stub"""
        return Metadata(**self._inline_regions_metadata)

    def get_choice_ids_metadata(self):
        """stub"""
        return Metadata(**self._choice_ids_metadata)

    def add_choice_id(self, choice_id, inline_region):
        """stub"""
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region]['choiceIds'].append(choice_id)
        else:
            raise IllegalState('that inline region is invalid')

    def set_choice_ids(self, choice_ids, inline_region):
        if not isinstance(choice_ids, list):
            raise IllegalState()
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region]['choiceIds'] = choice_ids
        else:
            raise IllegalState('that inline region is invalid')

    def clear_choice_ids(self, inline_region):
        """stub"""
        if (self.get_choice_ids_metadata().is_read_only() or
                self.get_choice_ids_metadata().is_required()):
            raise NoAccess()
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region]['choiceIds'] = \
                deepcopy(self._choice_ids_metadata['default_object_values'][0])
        else:
            raise IllegalState('that inline region is invalid')

    def add_inline_region(self, inline_region):
        if inline_region not in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region] = \
                {
                    "choiceIds": deepcopy(self._choice_ids_metadata['default_object_values'][0])
            }
        else:
            raise IllegalState('that inline region already exists')

    def remove_inline_region(self, inline_region):
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            del self.my_osid_object_form._my_map['inlineRegions'][inline_region]
        else:
            raise IllegalState('that inline region does not exist')


class InlineChoiceFeedbackAndFilesAnswerRecord(FilesAnswerRecord,
                                               FeedbackAnswerRecord,
                                               osid_records.OsidRecord,
                                               abc_assessment_records.AnswerRecord):
    _implemented_record_type_identifiers = [
        'inline-choice-text'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(InlineChoiceFeedbackAndFilesAnswerRecord, self).__init__(osid_object)

    def get_inline_choice_ids(self):
        """stub"""
        return_data = {}
        for inline_region, data in self.my_osid_object._my_map['inlineRegions'].items():
            return_data[inline_region] = {
                'choiceIds': IdList(data['choiceIds'])
            }
        return return_data


class MultiLanguageInlineChoiceQuestionFormRecord(MultiLanguageQuestionFormRecord):
    """QTI inline choice i.e. fill-in-the-blank"""
    _implemented_record_type_identifiers = [
        'multi-language-inline-choice-text'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageInlineChoiceQuestionFormRecord, self).__init__(osid_object_form)

    def _init_map(self):
        """stub"""
        super(MultiLanguageInlineChoiceQuestionFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['choices'] = \
            self._choices_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        super(MultiLanguageInlineChoiceQuestionFormRecord, self)._init_metadata()
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
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
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

    def get_choices_metadata(self):
        """stub"""
        return Metadata(**self._choices_metadata)

    @utilities.arguments_not_none
    def clear_choice_texts(self, choice_id, inline_region):
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()
        updated_choices = []
        for current_choice in self.my_osid_object_form._my_map['choices'][inline_region]:
            if current_choice['id'] != choice_id:
                updated_choices.append(current_choice)
            else:
                updated_choices.append({
                    'id': current_choice['id'],
                    'texts': [],
                    'name': current_choice['name']
                })
        self.my_osid_object_form._my_map['choices'][inline_region] = updated_choices

    @utilities.arguments_not_none
    def remove_choice_language(self, language_type, choice_id, inline_region):
        """stub"""
        if len(self.my_osid_object_form._my_map['choices'][inline_region]) == 0:
            raise IllegalState('there are currently no choices defined for this region')
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()

        choices = [c for c in self.my_osid_object_form._my_map['choices'][inline_region] if c['id'] == choice_id]
        if len(choices) == 0:
            raise InvalidArgument('invalid choice_id')

        for current_choice in self.my_osid_object_form._my_map['choices'][inline_region]:
            if choice_id == current_choice['id']:
                self.remove_field_by_language('texts',
                                              language_type,
                                              current_choice)

    @utilities.arguments_not_none
    def clear_choices(self, inline_region):
        if self.get_choices_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['choices'][inline_region] = \
            self._choices_metadata['default_object_values'][0]

    @utilities.arguments_not_none
    def add_choice(self, choice, inline_region, identifier=None, name=''):
        """stub"""
        if inline_region not in self.my_osid_object_form._my_map['choices']:
            raise IllegalState('that inline region does not exist. Please call add_inline_region first')

        if identifier is None:
            identifier = str(ObjectId())
        current_identifiers = [c['id'] for c in self.my_osid_object_form._my_map['choices'][inline_region]]
        if identifier not in current_identifiers:
            choice = {
                'id': identifier,
                'texts': [self._dict_display_text(choice)],
                'name': name
            }
            self.my_osid_object_form._my_map['choices'][inline_region].append(choice)
        else:
            for current_choice in self.my_osid_object_form._my_map['choices'][inline_region]:
                if current_choice['id'] == identifier:
                    self.add_or_replace_value('texts', choice, dictionary=current_choice)
                    choice = current_choice
        return choice

    @utilities.arguments_not_none
    def edit_choice(self, new_choice, choice_id, inline_region):
        """edit an existing choice, to keep the ID the same"""
        if inline_region not in self.my_osid_object_form._my_map['choices']:
            raise IllegalState('that inline region does not exist')
        if not isinstance(new_choice, DisplayText):
            raise InvalidArgument('new choice is not a DisplayText object')
        choices = [c for c in self.my_osid_object_form._my_map['choices'][inline_region] if c['id'] == choice_id]
        if len(choices) == 0:
            raise InvalidArgument('invalid choice_id for that region')

        for current_choice in self.my_osid_object_form._my_map['choices'][inline_region]:
            if choice_id == current_choice['id']:
                index = self.get_index_of_language_type('texts',
                                                        new_choice.language_type,
                                                        dictionary=current_choice)

                current_choice['texts'][index] = self._dict_display_text(new_choice)

    @utilities.arguments_not_none
    def add_inline_region(self, inline_region):
        if inline_region not in self.my_osid_object_form._my_map['choices']:
            self.my_osid_object_form._my_map['choices'][inline_region] = []
        else:
            raise IllegalState('that inline region already exists')

    @utilities.arguments_not_none
    def remove_inline_region(self, inline_region):
        if inline_region in self.my_osid_object_form._my_map['choices']:
            del self.my_osid_object_form._my_map['choices'][inline_region]
        else:
            raise IllegalState('that inline region does not exist')

    @utilities.arguments_not_none
    def remove_choice(self, choice_id, inline_region):
        """remove a choice, given the id"""
        if inline_region in self.my_osid_object_form._my_map['choices']:
            updated_choices = []
            for choice in self.my_osid_object_form._my_map['choices'][inline_region]:
                if choice['id'] != choice_id:
                    updated_choices.append(choice)
            self.my_osid_object_form._my_map['choices'][inline_region] = updated_choices

    @utilities.arguments_not_none
    def set_choice_order(self, choice_ids, inline_region):
        """ reorder choices per the passed in list
        :param choice_ids:
        :return:
        """
        reordered_choices = []
        current_choice_ids = [c['id'] for c in self.my_osid_object_form._my_map['choices'][inline_region]]
        if set(choice_ids) != set(current_choice_ids):
            raise IllegalState('missing choices for choice order')

        for choice_id in choice_ids:
            for current_choice in self.my_osid_object_form._my_map['choices'][inline_region]:
                if choice_id == current_choice['id']:
                    reordered_choices.append(current_choice)
                    break

        self.my_osid_object_form._my_map['choices'][inline_region] = reordered_choices


class MultiLanguageInlineChoiceQuestionRecord(MultiLanguageQuestionRecord):
    """A record for a ``Question``.
    You have to use this with the QTIQuestionRecord in order to get the shuffle key

    The methods specified by the record type are available through the
    underlying object.

    """
    _implemented_record_type_identifiers = [
        'multi-language-inline-choice-text'
    ]

    def __init__(self, osid_object):
        self._original_choice_order = deepcopy(osid_object._my_map['choices'])
        osid_object._my_map['multiLanguageChoices'] = deepcopy(osid_object._my_map['choices'])
        super(MultiLanguageInlineChoiceQuestionRecord, self).__init__(osid_object)
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        choices = self.my_osid_object._my_map['choices']
        if self.my_osid_object._my_map['shuffle']:
            for region, region_choices in choices.items():
                shuffle(region_choices)
                choices[region] = region_choices
        self.my_osid_object._my_map['choices'] = choices
        # Claim authority on this object, until someone else does:
        self.my_osid_object._authority = MAGIC_AUTHORITY

    def get_id(self):
        """override get_id to generate our "magic" ids that encode choice order"""

        # Check first to make sure no one else has claimed authority on my object.
        # This will likely occur when an AssessmentSection returns a Question
        # During an AssessmentSession
        if self.my_osid_object._authority != MAGIC_AUTHORITY:
            return self.my_osid_object._item_id
            # raise AttributeError

        # If not, go ahead and build magic Id:
        choices = self.my_osid_object._my_map['choices']
        magic_identifier = quote('{0}?{1}'.format(self.my_osid_object._my_map['_id'],
                                                  json.dumps(choices)))
        return Id(namespace='assessment.Item',
                  identifier=magic_identifier,
                  authority=MAGIC_AUTHORITY)

    ident = property(fget=get_id)
    id_ = property(fget=get_id)

    def get_unrandomized_choices(self):
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        if len(list(self._original_choice_order.keys())) > 0:
            for region, choices in self._original_choice_order.items():
                if len(choices) > 0:
                    updated_region_choices = []
                    for choice in choices:
                        filtered_choice = {
                            'id': choice['id'],
                            'text': self.get_matching_language_value('texts',
                                                                     dictionary=choice).text,
                            'name': choice['name']
                        }
                        updated_region_choices.append(filtered_choice)
                    self._original_choice_order[region] = updated_region_choices
        return self._original_choice_order

    def set_values(self, choice_ids):
        """assume choice_ids is a dict of {
            region: choiceIds
         }, like: {
            "REGION_1": ["57978959cdfc5c42eefb36d1", "57978959cdfc5c42eefb36d0",
                         "57978959cdfc5c42eefb36cf", "57978959cdfc5c42eefb36ce"]
         }
        """
        # if not self.my_osid_object._my_map['choices']:
        #     raise IllegalState()
        organized_regions = {}
        for region, choice_ids in choice_ids.items():
            organized_choice_ids = []
            for choice in choice_ids:
                original_region_choices = self._original_choice_order[region]
                choice_obj = [c for c in original_region_choices if c['id'] == choice['id']][0]
                organized_choice_ids.append(choice_obj)
            organized_regions[region] = organized_choice_ids
        self.my_osid_object._my_map['choices'] = organized_regions

    def get_choices(self):
        """stub"""
        # ideally would return a displayText object in text ... except for legacy
        # use cases like OEA, it expects a text string.
        choices = {}
        # for region_name, region_choices in self.my_osid_object.object_map['choices'].items():
        for region_name, region_choices in self.my_osid_object._my_map['choices'].items():
            updated_region_choices = []
            for current_choice in region_choices:
                filtered_choice = {
                    'id': current_choice['id'],
                    'text': self.get_matching_language_value('texts',
                                                             dictionary=current_choice).text,
                    'name': current_choice['name']
                }
                updated_region_choices.append(filtered_choice)
            choices[region_name] = updated_region_choices
        return choices

    choices = property(fget=get_choices)

    def get_object_map(self):
        # to get ['text'] from ['texts']
        obj_map = MultiLanguageQuestionRecord.get_object_map(self)
        # obj_map = dict(self.my_osid_object._my_map)
        # del obj_map['itemId']
        # try:
        #     lo_ids = self.my_osid_object.get_learning_objective_ids()
        #     obj_map['learningObjectiveIds'] = [str(lo_id) for lo_id in lo_ids]
        # except UnicodeEncodeError:
        #     lo_ids = self.my_osid_object.get_learning_objective_ids()
        #     obj_map['learningObjectiveIds'] = [unicode(lo_id) for lo_id in lo_ids]
        #
        # obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        # obj_map['id'] = str(self.my_osid_object.get_id())
        obj_map['choices'] = self.my_osid_object.get_choices()
        return obj_map

    object_map = property(fget=get_object_map)


class InlineChoiceAnswerFormRecord(osid_records.OsidRecord,
                                   abc_assessment_records.AnswerFormRecord):
    _implemented_record_type_identifiers = [
        'inline-choice-text'
    ]

    def __init__(self, osid_object_form):
        self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(InlineChoiceAnswerFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['inlineRegions'] = \
            self._inline_regions_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        self._inline_regions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'inline_regions'),
            'element_label': 'set of inline regions',
            'instructions': 'submit correct choice for answer for each region',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
        }
        self._choice_ids_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'choice_ids'),
            'element_label': 'response set with inline regions',
            'instructions': 'submit correct choice for answer for each region',
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

    def get_inline_regions_metadata(self):
        """stub"""
        return Metadata(**self._inline_regions_metadata)

    def get_choice_ids_metadata(self):
        """stub"""
        return Metadata(**self._choice_ids_metadata)

    def add_choice_id(self, choice_id, inline_region):
        """stub"""
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region]['choiceIds'].append(choice_id)
        else:
            raise IllegalState('that inline region is invalid')

    def set_choice_ids(self, choice_ids, inline_region):
        if not isinstance(choice_ids, list):
            raise IllegalState()
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region]['choiceIds'] = choice_ids
        else:
            raise IllegalState('that inline region is invalid')

    def clear_choice_ids(self, inline_region):
        """stub"""
        if (self.get_choice_ids_metadata().is_read_only() or
                self.get_choice_ids_metadata().is_required()):
            raise NoAccess()
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region]['choiceIds'] = \
                deepcopy(self._choice_ids_metadata['default_object_values'][0])
        else:
            raise IllegalState('that inline region is invalid')

    def add_inline_region(self, inline_region):
        if inline_region not in self.my_osid_object_form._my_map['inlineRegions']:
            self.my_osid_object_form._my_map['inlineRegions'][inline_region] = \
                {
                    "choiceIds": deepcopy(self._choice_ids_metadata['default_object_values'][0])
            }
        else:
            raise IllegalState('that inline region already exists')

    def remove_inline_region(self, inline_region):
        if inline_region in self.my_osid_object_form._my_map['inlineRegions']:
            del self.my_osid_object_form._my_map['inlineRegions'][inline_region]
        else:
            raise IllegalState('that inline region does not exist')


class InlineChoiceAnswerRecord(osid_records.OsidRecord,
                               abc_assessment_records.AnswerRecord):
    _implemented_record_type_identifiers = [
        'inline-choice-text'
    ]

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(InlineChoiceAnswerRecord, self).__init__()

    def get_inline_choice_ids(self):
        """stub"""
        return_data = {}
        for inline_region, data in self.my_osid_object._my_map['inlineRegions'].items():
            return_data[inline_region] = {
                'choiceIds': IdList(data['choiceIds'])
            }
        return return_data
