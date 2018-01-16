"""
records.assessment.basic.feedback_answer_records.py
"""

from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid import objects as osid_objects
from dlkit.json_ import types, utilities
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.learning.objects import ObjectiveList

from dlkit.abstract_osid.osid.errors import InvalidArgument, IllegalState, NoAccess
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.locale.primitives import DisplayText

from ...osid.base_records import ObjectInitRecord, MultiLanguageUtils

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


class FeedbackAnswerRecord(ObjectInitRecord):
    """
    This is really only a marker implementation to indicate that
    this answer includes a hint / feedback text.
    """
    _implemented_record_type_identifiers = [
        'answer-with-feedback',
        'texts-answer'
    ]

    def has_feedback(self):
        if self.my_osid_object._my_map['feedback']:
            return True
        return False

    def get_feedback(self):
        if self.has_feedback():
            return DisplayText(display_text_map=self.my_osid_object._my_map['feedback'])
        raise IllegalState()

    feedback = property(fget=get_feedback)

    def has_confused_learning_objective_ids(self):
        return 'confusedLearningObjectiveIds' in self.my_osid_object._my_map

    def get_confused_learning_objective_ids(self):
        confused_lo_ids = []
        if self.my_osid_object.has_confused_learning_objective_ids():
            confused_lo_ids = self.my_osid_object._my_map['confusedLearningObjectiveIds']
        return ObjectiveList(confused_lo_ids,
                             runtime=self.my_osid_object._runtime,
                             proxy=self.my_osid_object._proxy)

    confused_learning_objective_ids = property(fget=get_confused_learning_objective_ids)


class FeedbackAnswerFormRecord(osid_records.OsidRecord):
    """
    This is really only a marker implementation to indicate that
    this answer includes a hint / feedback text.
    """
    _implemented_record_type_identifiers = [
        'answer-with-feedback',
        'texts-answer'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(FeedbackAnswerFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['confusedLearningObjectiveIds'] = \
            self._confused_learning_objectives_metadata['default_list_values'][0]
        self.my_osid_object_form._my_map['feedback'] = \
            self._feedback_metadata['default_string_values'][0]
        # super(FeedbackAnswerFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        self._min_string_length = None
        self._max_string_length = None
        self._confused_learning_objectives_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'confusedLearningObjectiveIds'),
            'element_label': 'Confused Learning Objectives',
            'instructions': 'List of IDs',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_list_values': [[]],
            'syntax': 'LIST'
        }
        self._feedback_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'feedback'),
            'element_label': 'Feedback',
            'instructions': 'enter a feedback string',
            'required': False,
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
            'minimum_string_length': self._min_string_length,
            'maximum_string_length': self._max_string_length,
            'string_set': []
        }
        # super(FeedbackAnswerFormRecord, self)._init_metadata()

    def get_feedback_metadata(self):
        """stub"""
        return Metadata(**self._feedback_metadata)

    def set_feedback(self, text):
        self.my_osid_object_form._my_map['feedback'] = self.my_osid_object_form._get_display_text(
            text, self.get_feedback_metadata())

    def clear_feedback(self):
        self.my_osid_object_form._my_map['feedback'] = \
            self.get_feedback_metadata().get_default_string_values()[0]

    def get_confused_learning_objective_ids_metadata(self):
        """stub"""
        return Metadata(**self._confused_learning_objectives_metadata)

    def set_confused_learning_objective_ids(self, objectives_list):
        if not isinstance(objectives_list, list):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['confusedLearningObjectiveIds'] = objectives_list

    def clear_confused_learning_objective_ids(self):
        self.my_osid_object_form._my_map['confusedLearningObjectiveIds'] = \
            self._confused_learning_objectives_metadata['default_list_values'][0]


class MultiLanguageFeedbacksAnswerRecord(MultiLanguageUtils,
                                         ObjectInitRecord):
    def has_feedback(self):
        return True

    def get_feedback(self):
        return self.get_matching_language_value('feedbacks')

    feedback = property(fget=get_feedback)

    def has_confused_learning_objective_ids(self):
        return 'confusedLearningObjectiveIds' in self.my_osid_object._my_map

    def get_confused_learning_objective_ids(self):
        confused_lo_ids = []
        if self.my_osid_object.has_confused_learning_objective_ids():
            confused_lo_ids = self.my_osid_object._my_map['confusedLearningObjectiveIds']

        return ObjectiveList(confused_lo_ids,
                             runtime=self.my_osid_object._runtime,
                             proxy=self.my_osid_object._proxy)

    confused_learning_objective_ids = property(fget=get_confused_learning_objective_ids)

    def get_object_map(self):
        obj_map = dict(self.my_osid_object._my_map)
        del obj_map['itemId']
        obj_map['feedback'] = self._dict_display_text(self.my_osid_object.feedback)
        return osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)

    object_map = property(fget=get_object_map)


class MultiLanguageFeedbacksAnswerFormRecord(MultiLanguageUtils,
                                             osid_records.OsidRecord):
    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageFeedbacksAnswerFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['feedbacks'] = \
            self._feedbacks_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        self._confused_learning_objectives_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'confusedLearningObjectiveIds'),
            'element_label': 'Confused Learning Objectives',
            'instructions': 'List of IDs',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_list_values': [[]],
            'syntax': 'LIST'
        }
        self._feedbacks_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'feedbacks'),
            'element_label': 'Feedbacks',
            'instructions': 'Enter as many text feedback strings as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_feedbacks_metadata(self):
        """stub"""
        return Metadata(**self._feedbacks_metadata)

    @utilities.arguments_not_none
    def add_feedback(self, feedback):
        """stub"""
        self.add_or_replace_value('feedbacks', feedback)

    def clear_feedbacks(self):
        """stub"""
        if self.get_feedbacks_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['feedbacks'] = \
            self._feedbacks_metadata['default_object_values'][0]

    @utilities.arguments_not_none
    def remove_feedback_language(self, language_type):
        if self.get_feedbacks_metadata().is_read_only():
            raise NoAccess()
        self.remove_field_by_language('feedbacks', language_type)

    @utilities.arguments_not_none
    def edit_feedback(self, new_feedback):
        if self.get_feedbacks_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_feedback, DisplayText):
            raise InvalidArgument('new feedback is not a DisplayText object')
        index = self.get_index_of_language_type('feedbacks', new_feedback.language_type)
        self.my_osid_object_form._my_map['feedbacks'][index] = self._dict_display_text(new_feedback)

    def get_confused_learning_objective_ids_metadata(self):
        """stub"""
        return Metadata(**self._confused_learning_objectives_metadata)

    def set_confused_learning_objective_ids(self, objectives_list):
        if not isinstance(objectives_list, list):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['confusedLearningObjectiveIds'] = objectives_list

    def clear_confused_learning_objective_ids(self):
        self.my_osid_object_form._my_map['confusedLearningObjectiveIds'] = \
            self._confused_learning_objectives_metadata['default_list_values'][0]
