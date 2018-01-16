from dlkit.json_.osid.metadata import Metadata

from dlkit.primordium.id.primitives import Id
from dlkit.abstract_osid.osid.errors import InvalidArgument, IllegalState

from ..basic.text_answer_records import ExtendedTextAnswerQuestionFormRecord,\
    ExtendedTextAnswerQuestionRecord
from ..basic.base_records import MultiLanguageQuestionRecord, MultiLanguageQuestionFormRecord


class QTIExtendedTextAnswerQuestionFormRecord(ExtendedTextAnswerQuestionFormRecord):
    """A record for an ``ExtendedTextAnswer``.

    Adds metadata used to construct the QTI, like maxStrings, expectedLength, expectedLines

    """
    _implemented_record_type_identifiers = [
        'qti-extended-text-interaction'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(QTIExtendedTextAnswerQuestionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['maxStrings'] = \
            self._max_strings_metadata['default_integer_values'][0]
        self.my_osid_object_form._my_map['expectedLength'] = \
            self._expected_length_metadata['default_integer_values'][0]
        self.my_osid_object_form._my_map['expectedLines'] = \
            self._expected_lines_metadata['default_integer_values'][0]
        super(QTIExtendedTextAnswerQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        self._max_strings_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'maxStrings'),
            'element_label': 'maxStrings',
            'instructions': 'QTI maxStrings settings',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [100],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        self._expected_length_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'expectedLength'),
            'element_label': 'expectedLength',
            'instructions': 'QTI expectedLength setting',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [200],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        self._expected_lines_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'expectedLines'),
            'element_label': 'expectedLines',
            'instructions': 'QTI expectedLines setting',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [10],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        super(QTIExtendedTextAnswerQuestionFormRecord, self)._init_metadata()

    def get_max_strings_metadata(self):
        """stub"""
        return Metadata(**self._max_strings_metadata)

    def get_expected_length_metadata(self):
        """stub"""
        return Metadata(**self._expected_length_metadata)

    def get_expected_lines_metadata(self):
        """stub"""
        return Metadata(**self._expected_lines_metadata)

    def set_max_strings(self, max_strings):
        """stub"""
        if not self.my_osid_object_form._is_valid_integer(
                max_strings, self.get_max_strings_metadata()):
            raise InvalidArgument('maxStrings')
        self.my_osid_object_form._my_map['maxStrings'] = max_strings

    def clear_max_strings(self):
        """stub"""
        self.my_osid_object_form._my_map['maxStrings'] = \
            self._max_strings_metadata['default_integer_values'][0]

    def set_expected_length(self, expected_length):
        """stub"""
        if not self.my_osid_object_form._is_valid_integer(
                expected_length, self.get_expected_length_metadata()):
            raise InvalidArgument('expectedLength')
        self.my_osid_object_form._my_map['expectedLength'] = expected_length

    def clear_expected_length(self):
        """stub"""
        self.my_osid_object_form._my_map['expectedLength'] = \
            self._expected_length_metadata['default_integer_values'][0]

    def set_expected_lines(self, expected_lines):
        """stub"""
        if not self.my_osid_object_form._is_valid_integer(
                expected_lines, self.get_expected_lines_metadata()):
            raise InvalidArgument('expectedLines')
        self.my_osid_object_form._my_map['expectedLines'] = expected_lines

    def clear_expected_lines(self):
        """stub"""
        self.my_osid_object_form._my_map['expectedLines'] = \
            self._expected_lines_metadata['default_lines_values'][0]


class QTIExtendedTextAnswerQuestionRecord(ExtendedTextAnswerQuestionRecord):
    """A record for an ``ExtendedTextAnswer``.

    Adds metadata used to construct the QTI, like maxStrings, expectedLength, expectedLines

    """
    _implemented_record_type_identifiers = [
        'qti-extended-text-interaction'
    ]

    def has_max_strings(self):
        """stub"""
        return bool(self.my_osid_object._my_map['maxStrings'] is not None)

    def get_max_strings(self):
        """stub"""
        if self.has_max_strings():
            return int(self.my_osid_object._my_map['maxStrings'])
        raise IllegalState()

    def has_expected_length(self):
        """stub"""
        return bool(self.my_osid_object._my_map['expectedLength'] is not None)

    def get_expected_length(self):
        """stub"""
        if self.has_expected_length():
            return int(self.my_osid_object._my_map['expectedLength'])
        raise IllegalState()

    def has_expected_lines(self):
        """stub"""
        return bool(self.my_osid_object._my_map['expectedLines'] is not None)

    def get_expected_lines(self):
        """stub"""
        if self.has_expected_lines():
            return int(self.my_osid_object._my_map['expectedLines'])
        raise IllegalState()

    max_strings = property(fget=get_max_strings)
    expected_length = property(fget=get_expected_length)
    expected_lines = property(fget=get_expected_lines)


class MultiLanguageQTIExtendedTextAnswerQuestionFormRecord(MultiLanguageQuestionFormRecord):
    """A record for an ``ExtendedTextAnswer`` with multiple languages

    Adds metadata used to construct the QTI, like maxStrings, expectedLength, expectedLines

    """
    _implemented_record_type_identifiers = [
        'multi-language-qti-extended-text-interaction'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageQTIExtendedTextAnswerQuestionFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['maxStrings'] = \
            self._max_strings_metadata['default_integer_values'][0]
        self.my_osid_object_form._my_map['expectedLength'] = \
            self._expected_length_metadata['default_integer_values'][0]
        self.my_osid_object_form._my_map['expectedLines'] = \
            self._expected_lines_metadata['default_integer_values'][0]
        super(MultiLanguageQTIExtendedTextAnswerQuestionFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        self._max_strings_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'maxStrings'),
            'element_label': 'maxStrings',
            'instructions': 'QTI maxStrings settings',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [100],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        self._expected_length_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'expectedLength'),
            'element_label': 'expectedLength',
            'instructions': 'QTI expectedLength setting',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [200],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        self._expected_lines_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'expectedLines'),
            'element_label': 'expectedLines',
            'instructions': 'QTI expectedLines setting',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [10],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        super(MultiLanguageQTIExtendedTextAnswerQuestionFormRecord, self)._init_metadata()

    def get_max_strings_metadata(self):
        """stub"""
        return Metadata(**self._max_strings_metadata)

    def get_expected_length_metadata(self):
        """stub"""
        return Metadata(**self._expected_length_metadata)

    def get_expected_lines_metadata(self):
        """stub"""
        return Metadata(**self._expected_lines_metadata)

    def set_max_strings(self, max_strings):
        """stub"""
        if not self.my_osid_object_form._is_valid_integer(
                max_strings, self.get_max_strings_metadata()):
            raise InvalidArgument('maxStrings')
        self.my_osid_object_form._my_map['maxStrings'] = max_strings

    def clear_max_strings(self):
        """stub"""
        self.my_osid_object_form._my_map['maxStrings'] = \
            self._max_strings_metadata['default_integer_values'][0]

    def set_expected_length(self, expected_length):
        """stub"""
        if not self.my_osid_object_form._is_valid_integer(
                expected_length, self.get_expected_length_metadata()):
            raise InvalidArgument('expectedLength')
        self.my_osid_object_form._my_map['expectedLength'] = expected_length

    def clear_expected_length(self):
        """stub"""
        self.my_osid_object_form._my_map['expectedLength'] = \
            self._expected_length_metadata['default_integer_values'][0]

    def set_expected_lines(self, expected_lines):
        """stub"""
        if not self.my_osid_object_form._is_valid_integer(
                expected_lines, self.get_expected_lines_metadata()):
            raise InvalidArgument('expectedLines')
        self.my_osid_object_form._my_map['expectedLines'] = expected_lines

    def clear_expected_lines(self):
        """stub"""
        self.my_osid_object_form._my_map['expectedLines'] = \
            self._expected_lines_metadata['default_lines_values'][0]


class MultiLanguageQTIExtendedTextAnswerQuestionRecord(MultiLanguageQuestionRecord):
    """A record for an ``ExtendedTextAnswer`` with multiple languages

    Adds metadata used to construct the QTI, like maxStrings, expectedLength, expectedLines

    """
    _implemented_record_type_identifiers = [
        'multi-language-qti-extended-text-interaction'
    ]

    def has_max_strings(self):
        """stub"""
        return bool(self.my_osid_object._my_map['maxStrings'] is not None)

    def get_max_strings(self):
        """stub"""
        if self.has_max_strings():
            return int(self.my_osid_object._my_map['maxStrings'])
        raise IllegalState()

    def has_expected_length(self):
        """stub"""
        return bool(self.my_osid_object._my_map['expectedLength'] is not None)

    def get_expected_length(self):
        """stub"""
        if self.has_expected_length():
            return int(self.my_osid_object._my_map['expectedLength'])
        raise IllegalState()

    def has_expected_lines(self):
        """stub"""
        return bool(self.my_osid_object._my_map['expectedLines'] is not None)

    def get_expected_lines(self):
        """stub"""
        if self.has_expected_lines():
            return int(self.my_osid_object._my_map['expectedLines'])
        raise IllegalState()

    max_strings = property(fget=get_max_strings)
    expected_length = property(fget=get_expected_length)
    expected_lines = property(fget=get_expected_lines)
