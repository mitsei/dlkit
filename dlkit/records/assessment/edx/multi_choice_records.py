"""
records.assessment.edx.multi_choice_records.py
"""
from random import shuffle

from ..basic.base_records import ItemWithWrongAnswerLOsRecord
from ..basic.simple_records import QuestionFilesRecord,\
    QuestionTextAndFilesMixin
from ..basic.multi_choice_records import MultiChoiceTextQuestionRecord,\
    MultiChoiceTextQuestionFormRecord,\
    MultiChoiceTextAnswerRecord,\
    MultiChoiceTextAnswerFormRecord, MultiChoiceItemRecord
from .base_records import edXProviderIdMixin
from .item_records import edXItemRecord, edXItemFormRecord

from dlkit.json_.osid.metadata import Metadata

from dlkit.primordium.id.primitives import Id
from dlkit.abstract_osid.osid.errors import InvalidArgument, IllegalState, NotFound


class EdXMultipleChoiceItemRecord(ItemWithWrongAnswerLOsRecord,
                                  MultiChoiceItemRecord,
                                  edXItemRecord):
    pass


class EdXMultipleChoiceItemFormRecord(edXItemFormRecord):
    pass


class edXMultiChoiceQuestionRecord(MultiChoiceTextQuestionRecord,
                                   edXProviderIdMixin,
                                   QuestionFilesRecord):
    """edX multiple choice questions"""
    _implemented_record_type_identifiers = [
        'multi-choice-edx',
        'multi-choice-text',
        'question-text',
        'question-files'
    ]

    def __init__(self, **kwargs):
        super(edXMultiChoiceQuestionRecord, self).__init__(**kwargs)

        # change my_map
        if ('rerandomize' in self._my_map and
                self._my_map['rerandomize'] == 'always'):
            shuffle(self._my_map['choices'])
        # handle deprecated data...this should go away once Luwen re-loads
        # her data with newer assessmentsv2/views.py code
        try:
            am = self._get_provider_manager('ASSESSMENT', local=True)
            try:
                ils = am.get_item_lookup_session_for_bank(Id(self._my_map['assignedBankIds'][0]),
                                                          proxy=self._proxy)
            except TypeError:  # not a proxy manager
                ils = am.get_item_lookup_session_for_bank(Id(self._my_map['assignedBankIds'][0]))
            item = ils.get_item(Id(self._my_map['itemId']))
            if 'rerandomize' in item._my_map and item._my_map['rerandomize'] == 'always':
                shuffle(self._my_map['choices'])
        except (KeyError, NotFound, IllegalState, AttributeError) as ex:
            import logging
            logging.info(ex.args[0])

    def _update_object_map(self, map):
        super(edXMultiChoiceQuestionRecord, self)._update_object_map(map)

    def has_rerandomize(self):
        """stub"""
        return bool(self._my_map['rerandomize'] is not None)

    def get_rerandomize(self):
        """stub"""
        if self.has_rerandomize():
            return self._my_map['rerandomize']
        raise IllegalState()

    rerandomize = property(fget=get_rerandomize)


class edXMultiChoiceQuestionFormRecord(QuestionTextAndFilesMixin,
                                       MultiChoiceTextQuestionFormRecord):
    """form for edX multiple choice questions"""
    _implemented_record_type_identifiers = [
        'multi-choice-edx',
        'multi-choice-text',
        'question-text',
        'question-files'
    ]

    def __init__(self, **kwargs):
        super(edXMultiChoiceQuestionFormRecord, self).__init__(**kwargs)
        self._rerandomize_metadata = None

    def _init_map(self, **kwargs):
        """stub"""
        super(edXMultiChoiceQuestionFormRecord, self)._init_map(**kwargs)
        self._my_map['rerandomize'] = \
            self._rerandomize_metadata['default_object_values'][0]

    def _init_metadata(self, **kwargs):
        """stub"""
        super(edXMultiChoiceQuestionFormRecord, self)._init_metadata(**kwargs)
        self._rerandomize_metadata = {
            'element_id': Id(self._authority,
                             self._namespace,
                             'rerandomize'),
            'element_label': 'Randomize',
            'instructions': 'How to rerandomize the parameters',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': ['never'],
            'syntax': 'STRING',
            'minimum_string_length': None,
            'maximum_string_length': None,
            'string_set': []
        }

    def get_rerandomize_metadata(self):
        """stub"""
        return Metadata(**self._rerandomize_metadata)

    def add_rerandomize(self, rerandomize):
        """stub"""
        if not self._is_valid_string(
                rerandomize, self.get_rerandomize_metadata()):
            raise InvalidArgument('rerandomize')
        self._my_map['rerandomize'] = rerandomize

    def clear_rerandomize(self):
        """stub"""
        self._my_map['rerandomize'] = \
            self._rerandomize_metadata['default_object_values'][0]


class edXMultiChoiceAnswerRecord(MultiChoiceTextAnswerRecord):
    """answer to edX multi choice questions"""
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]

    def _update_object_map(self, map):
        pass


class edXMultiChoiceAnswerFormRecord(MultiChoiceTextAnswerFormRecord):
    """form for edX multi choice answers"""
    _implemented_record_type_identifiers = [
        'multi-choice'
    ]
