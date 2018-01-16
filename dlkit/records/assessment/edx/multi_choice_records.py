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

    def __init__(self, osid_object, **kwargs):
        super(edXMultiChoiceQuestionRecord, self).__init__(osid_object)

        # change my_map
        if ('rerandomize' in self.my_osid_object._my_map and
                self.my_osid_object._my_map['rerandomize'] == 'always'):
            shuffle(self.my_osid_object._my_map['choices'])
        # handle deprecated data...this should go away once Luwen re-loads
        # her data with newer assessmentsv2/views.py code
        try:
            am = self.my_osid_object._get_provider_manager('ASSESSMENT', local=True)
            try:
                ils = am.get_item_lookup_session_for_bank(Id(self.my_osid_object._my_map['assignedBankIds'][0]),
                                                          proxy=self.my_osid_object._proxy)
            except TypeError:  # not a proxy manager
                ils = am.get_item_lookup_session_for_bank(Id(self.my_osid_object._my_map['assignedBankIds'][0]))
            item = ils.get_item(Id(self.my_osid_object._my_map['itemId']))
            if 'rerandomize' in item._my_map and item._my_map['rerandomize'] == 'always':
                shuffle(self.my_osid_object._my_map['choices'])
        except (KeyError, NotFound, IllegalState, AttributeError) as ex:
            import logging
            logging.info(ex.args[0])

    def _update_object_map(self, map):
        super(edXMultiChoiceQuestionRecord, self)._update_object_map(map)

    def has_rerandomize(self):
        """stub"""
        return bool(self.my_osid_object._my_map['rerandomize'] is not None)

    def get_rerandomize(self):
        """stub"""
        if self.has_rerandomize():
            return self.my_osid_object._my_map['rerandomize']
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

    def __init__(self, osid_object_form):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not osid_object_form.is_for_update():
            self._init_map()
        super(edXMultiChoiceQuestionFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['rerandomize'] = \
            self._rerandomize_metadata['default_object_values'][0]
        super(edXMultiChoiceQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        self._rerandomize_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
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
        super(edXMultiChoiceQuestionFormRecord, self)._init_metadata()

    def get_rerandomize_metadata(self):
        """stub"""
        return Metadata(**self._rerandomize_metadata)

    def add_rerandomize(self, rerandomize):
        """stub"""
        if not self.my_osid_object_form._is_valid_string(
                rerandomize, self.get_rerandomize_metadata()):
            raise InvalidArgument('rerandomize')
        self.my_osid_object_form._my_map['rerandomize'] = rerandomize

    def clear_rerandomize(self):
        """stub"""
        self.my_osid_object_form._my_map['rerandomize'] = \
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
