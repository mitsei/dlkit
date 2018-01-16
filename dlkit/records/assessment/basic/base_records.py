from __future__ import unicode_literals

from dlkit.json_ import types
from dlkit.json_.id.objects import IdList
from dlkit.json_.assessment.objects import ItemList, Item
from dlkit.json_.utilities import JSONClientValidated, arguments_not_none, is_string
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid import objects as osid_objects
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.osid.errors import IllegalState, InvalidArgument, NotFound, NoAccess
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.type.primitives import Type

from bson.objectid import ObjectId

from ...osid.base_records import ProvenanceRecord, ProvenanceFormRecord, ObjectInitRecord,\
    MultiLanguageUtils

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))


class ProvenanceItemFormRecord(ProvenanceFormRecord):
    """Provenance == "parent record" of this record...simple way to track
    item inheritance."""


class ProvenanceItemRecord(ProvenanceRecord):
    """Provenance == "parent record" of this record...simple way to track
    item inheritance."""

    def has_provenance(self):
        """to handle deprecated mecqbank data"""
        if 'provenanceId' in self.my_osid_object._my_map:
            return bool(self.my_osid_object._my_map['provenanceId'] != '')
        else:
            return bool(self.my_osid_object._my_map['provenanceItemId'] != '')

    def get_provenance_id(self):
        """to handle deprecated mecqbank data"""
        if self.has_provenance():
            if 'provenanceId' in self.my_osid_object._my_map:
                return self.my_osid_object._my_map['provenanceId']
            else:
                return self.my_osid_object._my_map['provenanceItemId']
        raise IllegalState()

    def get_provenance_parent(self):
        """stub"""
        if self.has_provenance():
            collection = JSONClientValidated('assessment',
                                             collection='Item',
                                             runtime=self.my_osid_object._runtime)
            result = collection.find_one(
                {'_id': ObjectId(Id(self.get_provenance_id()).get_identifier())})
            return Item(osid_object_map=result,
                        runtime=self.my_osid_object._runtime,
                        proxy=self.my_osid_object._proxy)
        raise IllegalState("Item has no provenance parent.")

    def has_provenance_children(self):
        """stub"""
        collection = JSONClientValidated('assessment',
                                         collection='Item',
                                         runtime=self.my_osid_object._runtime)
        if (collection.find(
                {'provenanceId': self.my_osid_object.object_map['id']}).count() > 0 or
            collection.find(  # for backwards compatibility
                    {'provenanceItemId': self.my_osid_object.object_map['id']}).count() > 0):
            return True
        else:
            return False

    def get_provenance_children(self):
        """stub"""
        if self.has_provenance_children():
            collection = JSONClientValidated('assessment',
                                             collection='Item',
                                             runtime=self.my_osid_object._runtime)
            try:
                result = collection.find(
                    {'provenanceId': self.my_osid_object.object_map['id']})
                if result.count() == 0:
                    raise KeyError
            except KeyError:
                # For deprecated mecqbank data
                result = collection.find(
                    {'provenanceItemId': self.my_osid_object.object_map['id']})
            return ItemList(result,
                            runtime=self.my_osid_object._runtime,
                            proxy=self.my_osid_object._proxy)
        raise IllegalState('No provenance children.')

    provenance_children = property(fget=get_provenance_children)
    provenance_parent = property(fget=get_provenance_parent)


class ItemWithWrongAnswerLOsRecord(ObjectInitRecord):
    def get_answer_for_response(self, response):
        response_set = set([str(c) for c in response.get_choice_ids()])
        for answer in self.my_osid_object.get_answers():
            if response_set == set([str(c) for c in answer.get_choice_ids()]):
                return answer
        for answer in self.my_osid_object.get_wrong_answers():
            if response_set == set([str(c) for c in answer.get_choice_ids()]):
                return answer
        raise NotFound('no matching answer found for response')

    def get_confused_learning_objective_ids_for_response(self, response):
        try:
            answer = self.get_answer_for_response(response)
        except NotFound:
            raise IllegalState('no answer matching response was found')
        try:
            return answer.get_confused_learning_objective_ids()
        except AttributeError:
            return IdList([])


class ItemWithSolutionRecord(ObjectInitRecord):
    def has_solution(self):
        """stub"""
        if self.my_osid_object._my_map['solution'] is not None:
            return True
        return False

    def get_solution(self, parameters=None):
        """stub"""
        if not self.has_solution():
            raise IllegalState()
        return DisplayText(self.my_osid_object._my_map['solution'])

    solution = property(fget=get_solution)


class ItemWithSolutionFormRecord(osid_records.OsidRecord):
    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(ItemWithSolutionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['solution'] = \
            dict(self._solution_metadata['default_string_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_string_length = None
        self._max_string_length = None
        self._solution_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'solution'),
            'element_label': 'Solution',
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

    def get_solution_metadata(self):
        """stub"""
        return Metadata(**self._solution_metadata)

    def set_solution(self, text):
        """stub"""
        if not self.my_osid_object_form._is_valid_string(
                text, self.get_solution_metadata()):
            raise InvalidArgument('text')
        if is_string(text):
            self.my_osid_object_form._my_map['solution'] = {
                'text': text,
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE)
            }
        else:
            self.my_osid_object_form._my_map['solution'] = text

    def clear_solution(self):
        """stub"""
        if 'solution' not in self.my_osid_object_form._my_map:
            raise NotFound()
        self.my_osid_object_form._my_map['solution'] = \
            dict(self._solution_metadata['default_string_values'][0])


class MultiLanguageQuestionRecord(MultiLanguageUtils,
                                  ObjectInitRecord):
    def get_text(self):
        """stub"""
        return self.get_matching_language_value('texts')

    text = property(fget=get_text)

    def get_object_map(self):
        obj_map = dict(self.my_osid_object._my_map)
        del obj_map['itemId']
        lo_ids = self.my_osid_object.get_learning_objective_ids()
        try:
            # python 2
            obj_map['learningObjectiveIds'] = [unicode(lo_id) for lo_id in lo_ids]
        except NameError:
            # python 3
            obj_map['learningObjectiveIds'] = [str(lo_id) for lo_id in lo_ids]

        obj_map = osid_objects.OsidObject.get_object_map(self.my_osid_object, obj_map)
        obj_map['id'] = str(self.my_osid_object.get_id())
        obj_map['text'] = self._dict_display_text(self.my_osid_object.get_text())
        return obj_map

    object_map = property(fget=get_object_map)


class MultiLanguageQuestionFormRecord(MultiLanguageUtils,
                                      osid_records.OsidRecord):
    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageQuestionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['texts'] = \
            self._texts_metadata['default_object_values'][0]

    def _init_metadata(self):
        """stub"""
        self._texts_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'texts'),
            'element_label': 'Texts',
            'instructions': 'Enter as many text question strings as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_texts_metadata(self):
        """stub"""
        return Metadata(**self._texts_metadata)

    @arguments_not_none
    def add_text(self, text):
        """stub"""
        self.add_or_replace_value('texts', text)

    def clear_texts(self):
        """stub"""
        if self.get_texts_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['texts'] = \
            self._texts_metadata['default_object_values'][0]

    @arguments_not_none
    def remove_text_language(self, language_type):
        if self.get_texts_metadata().is_read_only():
            raise NoAccess()
        self.remove_field_by_language('texts', language_type)

    @arguments_not_none
    def edit_text(self, new_text):
        if self.get_texts_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_text, DisplayText):
            raise InvalidArgument('new text is not a DisplayText object')

        index = self.get_index_of_language_type('texts', new_text.language_type)

        self.my_osid_object_form._my_map['texts'][index] = \
            self._dict_display_text(new_text)
