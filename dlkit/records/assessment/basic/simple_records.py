"""
records.assessment.basic.simple_records
"""

from dlkit.json_ import types
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records
from dlkit.abstract_osid.osid.errors import IllegalState, NoAccess, InvalidArgument
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type

from ...osid.base_records import TextsFormRecord,\
    TextFormRecord,\
    TextsRecord,\
    TextRecord,\
    FilesFormRecord,\
    FilesRecord,\
    FileRecord,\
    FileFormRecord,\
    IntegerValueRecord,\
    IntegerValueFormRecord,\
    IntegerValuesFormRecord,\
    IntegerValuesRecord,\
    DecimalValueFormRecord,\
    DecimalValuesFormRecord,\
    DecimalValuesRecord,\
    DecimalValueRecord,\
    ColorCoordinateFormRecord,\
    ColorCoordinateRecord,\
    ProvenanceFormRecord


default_language_type = Type(**types.Language().get_type_data('DEFAULT'))
default_script_type = Type(**types.Script().get_type_data('DEFAULT'))
default_format_type = Type(**types.Format().get_type_data('DEFAULT'))
default_genus_type = Type(**types.Genus().get_type_data('DEFAULT'))


class ItemTextRecord(TextRecord, abc_assessment_records.ItemRecord):
    """Item with a single text value"""
    _implemented_record_type_identifiers = [
        'item-text'
    ]


class ItemTextFormRecord(TextFormRecord, abc_assessment_records.ItemFormRecord):
    """Form for item with a single text value"""
    _implemented_record_type_identifiers = [
        'item-text'
    ]


class ItemTextsRecord(TextsRecord, abc_assessment_records.ItemRecord):
    """Item with multiple text values"""
    _implemented_record_type_identifiers = [
        'item-texts'
    ]


class ItemTextsFormRecord(TextsFormRecord, abc_assessment_records.ItemFormRecord):
    """Form for item with multiple text values"""
    _implemented_record_type_identifiers = [
        'item-texts'
    ]


class ItemFilesRecord(FilesRecord, abc_assessment_records.ItemRecord):
    """Item with multiple files"""
    _implemented_record_type_identifiers = [
        'item-files'
    ]


class ItemFilesFormRecord(FilesFormRecord, abc_assessment_records.ItemFormRecord):
    """Form for item with multiple files"""
    _implemented_record_type_identifiers = [
        'item-files'
    ]


class ItemTextsAndFilesMixin(ItemTextsFormRecord,
                             ItemFilesFormRecord):
    """Mixin class to make the two classes compatible with super()
    for _init_map and _init_metadata

    """
    def _init_map(self):
        """stub"""
        ItemTextsFormRecord._init_map(self)
        ItemFilesFormRecord._init_map(self)
        super(ItemTextsAndFilesMixin, self)._init_map()

    def _init_metadata(self):
        """stub"""
        ItemTextsFormRecord._init_metadata(self)
        ItemFilesFormRecord._init_metadata(self)
        super(ItemTextsAndFilesMixin, self)._init_metadata()


class ProvenanceMixin(ProvenanceFormRecord):
    """Mixin class to make the ProvenanceFormRecord classes compatible with super()
    for _init_map and _init_metadata

    """
    def _init_map(self):
        """stub"""
        super(ProvenanceMixin, self)._init_map()
        ProvenanceFormRecord._init_map(self)

    def _init_metadata(self):
        """stub"""
        super(ProvenanceMixin, self)._init_metadata()
        ProvenanceFormRecord._init_metadata(self)


class QuestionTextRecord(TextRecord, abc_assessment_records.QuestionRecord):
    """Text question"""
    _implemented_record_type_identifiers = [
        'question-text'
    ]


class QuestionTextFormRecord(TextFormRecord, abc_assessment_records.QuestionFormRecord):
    """form for text question"""
    _implemented_record_type_identifiers = [
        'question-text'
    ]


class QuestionTextsRecord(TextsRecord, abc_assessment_records.QuestionRecord):
    """Question with multiple text values"""
    _implemented_record_type_identifiers = [
        'question-texts'
    ]


class QuestionTextsFormRecord(TextsFormRecord, abc_assessment_records.QuestionFormRecord):
    """Form for question with multiple text values"""
    _implemented_record_type_identifiers = [
        'question-texts'
    ]


class QuestionFileRecord(FileRecord, abc_assessment_records.QuestionRecord):
    """Questions with a file as part of the question"""
    _implemented_record_type_identifiers = [
        'question-file'
    ]


class QuestionFileFormRecord(FileFormRecord, abc_assessment_records.QuestionFormRecord):
    """Form to edit / create file-based questions"""
    _implemented_record_type_identifiers = [
        'question-file'
    ]


class QuestionFilesRecord(FilesRecord, abc_assessment_records.QuestionRecord):
    """questions with multiple files"""
    _implemented_record_type_identifiers = [
        'question-files'
    ]


class QuestionFilesFormRecord(FilesFormRecord, abc_assessment_records.QuestionFormRecord):
    """form to edit / create questions with multiple files"""
    _implemented_record_type_identifiers = [
        'question-files'
    ]


class QuestionTextAndFilesMixin(QuestionTextFormRecord,
                                QuestionFilesFormRecord):
    """Mixin class to make the two classes compatible with super()
    for _init_map and _init_metadata

    """
    def _init_map(self):
        """stub"""
        QuestionTextFormRecord._init_map(self)
        QuestionFilesFormRecord._init_map(self)
        super(QuestionTextAndFilesMixin, self)._init_map()

    def _init_metadata(self):
        """stub"""
        QuestionTextFormRecord._init_metadata(self)
        QuestionFilesFormRecord._init_metadata(self)
        super(QuestionTextAndFilesMixin, self)._init_metadata()


class QuestionTextsAndFilesMixin(QuestionTextsFormRecord,
                                 QuestionFilesFormRecord):
    """Mixin class to make the two classes compatible with super()
    for _init_map and _init_metadata

    """
    def _init_map(self):
        """stub"""
        QuestionTextsFormRecord._init_map(self)
        QuestionFilesFormRecord._init_map(self)
        super(QuestionTextsAndFilesMixin, self)._init_map()

    def _init_metadata(self):
        """stub"""
        QuestionTextsFormRecord._init_metadata(self)
        QuestionFilesFormRecord._init_metadata(self)
        super(QuestionTextsAndFilesMixin, self)._init_metadata()


class TextAnswerRecord(TextRecord, abc_assessment_records.AnswerFormRecord):
    """text-based answer"""
    _implemented_record_type_identifiers = [
        'text-answer'
    ]

    def has_min_string_length(self):
        """stub"""
        return bool(self.my_osid_object._my_map['minStringLength'])

    def get_min_string_length(self):
        """stub"""
        if self.has_max_string_length():
            return bool(self.my_osid_object._my_map['minStringLength'])
        raise IllegalState()

    def has_max_string_length(self):
        """stub"""
        return bool(self.my_osid_object._my_map['maxStringLength'])

    def get_max_string_length(self):
        """stub"""
        if self.has_max_string_length() is None:
            return bool(self.my_osid_object._my_map['maxStringLength'])
        raise IllegalState()


class TextAnswerFormRecord(TextFormRecord, abc_assessment_records.AnswerFormRecord):
    """form for text-based answers"""
    _implemented_record_type_identifiers = [
        'text-answer'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        if self.my_osid_object_form.is_for_update():
            self._min_string_length = self.my_osid_object_form._my_map['minStringLength']
            self._max_string_length = self.my_osid_object_form._my_map['maxStringLength']
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()

        super(TextAnswerFormRecord, self).__init__(osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(TextAnswerFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['minStringLength'] = \
            self._min_string_length_metadata['default_cardinal_values'][0]
        self.my_osid_object_form._my_map['maxStringLength'] = \
            self._max_string_length_metadata['default_cardinal_values'][0]

    def _init_metadata(self):
        """stub"""
        super(TextAnswerFormRecord, self)._init_metadata()
        self._min_string_length_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'min-string-length'),
            'element_label': 'min string length',
            'instructions': 'enter minimum string length',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [self._min_string_length],
            'syntax': 'CARDINAL',
            'minimum_cardinal': None,
            'maximum_cardinal': None,
            'cardinal_set': []
        }
        self._max_string_length_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'max-string-length'),
            'element_label': 'max string length',
            'instructions': 'enter maximum string length',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [self._max_string_length],
            'syntax': 'CARDINAL',
            'minimum_cardinal': None,
            'maximum_cardinal': None,
            'cardinal_set': []
        }

    def get_min_string_length_metadata(self):
        """stub"""
        return Metadata(**self._min_string_length_metadata)

    def set_min_string_length(self, length=None):
        """stub"""
        if self.get_min_string_length_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_cardinal(
                length,
                self.get_min_string_length_metadata()):
            raise InvalidArgument()
        if self._max_string_length is not None and length > self._max_string_length - 1:
            raise InvalidArgument()
        self.my_osid_object_form._my_map['minStringLength'] = length
        self._min_string_length = length

    def clear_min_string_length(self):
        """stub"""
        if (self.get_min_string_length_metadata().is_read_only() or
                self.get_min_string_length_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['minStringLength'] = \
            self.get_min_string_length_metadata().get_default_cardinal_values()[0]

    min_string_length = property(fset=set_min_string_length, fdel=clear_min_string_length)

    def get_max_string_length_metadata(self):
        """stub"""
        return Metadata(**self._max_string_length_metadata)

    def set_max_string_length(self, length=None):
        """stub"""
        if self.get_max_string_length_metadata().is_read_only():
            raise NoAccess()
        if length is not None and not self.my_osid_object_form._is_valid_cardinal(
                length,
                self.get_max_string_length_metadata()):
            raise InvalidArgument()
        if self._min_string_length is not None and length < self._min_string_length + 1:
            raise InvalidArgument()
        self.my_osid_object_form._my_map['maxStringLength'] = length
        self._max_string_length = length

    def clear_max_string_length(self):
        """stub"""
        if (self.get_max_string_length_metadata().is_read_only() or
                self.get_max_string_length_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['maxStringLength'] = \
            self.get_max_string_length_metadata().get_default_cardinal_values()[0]

    max_string_length = property(fset=set_max_string_length, fdel=clear_max_string_length)


class TextsAnswerRecord(TextsRecord, abc_assessment_records.AnswerRecord):
    """answer with multiple text components"""
    _implemented_record_type_identifiers = [
        'texts-answer'
    ]

    def has_min_string_length(self):
        """stub"""
        return bool(self.my_osid_object._my_map['minStringLength'])

    def get_min_string_length(self):
        """stub"""
        if self.has_max_string_length():
            return bool(self.my_osid_object._my_map['minStringLength'])
        raise IllegalState()

    def has_max_string_length(self):
        """stub"""
        return bool(self.my_osid_object._my_map['maxStringLength'])

    def get_max_string_length(self):
        """stub"""
        if self.has_max_string_length() is None:
            return bool(self.my_osid_object._my_map['maxStringLength'])
        raise IllegalState()


class TextsAnswerFormRecord(TextsFormRecord, abc_assessment_records.AnswerFormRecord):
    """form for answer with multiple text components"""
    _implemented_record_type_identifiers = [
        'texts-answer'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()

        if self.my_osid_object_form.is_for_update():
            self._min_string_length = \
                self.my_osid_object_form._my_map.get('minStringLength',
                                                     self._min_string_length_metadata['default_cardinal_values'][0])
            self._max_string_length = \
                self.my_osid_object_form._my_map.get('maxStringLength',
                                                     self._max_string_length_metadata['default_cardinal_values'][0])
        if (not self.my_osid_object_form.is_for_update() or
                'texts' not in self.my_osid_object_form._my_map):
            self._init_map()
        super(TextsAnswerFormRecord, self).__init__(osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(TextsAnswerFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['minStringLength'] = \
            self._min_string_length_metadata['default_cardinal_values'][0]
        self.my_osid_object_form._my_map['maxStringLength'] = \
            self._max_string_length_metadata['default_cardinal_values'][0]

    def _init_metadata(self):
        """stub"""
        super(TextsAnswerFormRecord, self)._init_metadata()
        self._min_string_length_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'min-string-length'),
            'element_label': 'min string length',
            'instructions': 'enter minimum string length',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [self._min_string_length],
            'syntax': 'CARDINAL',
            'minimum_cardinal': None,
            'maximum_cardinal': None,
            'cardinal_set': []
        }
        self._max_string_length_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'max-string-length'),
            'element_label': 'max string length',
            'instructions': 'enter maximum string length',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_cardinal_values': [self._max_string_length],
            'syntax': 'CARDINAL',
            'minimum_cardinal': None,
            'maximum_cardinal': None,
            'cardinal_set': []
        }

    def get_min_string_length_metadata(self):
        """stub"""
        return Metadata(**self._min_string_length_metadata)

    def set_min_string_length(self, length=None):
        """stub"""
        if self.get_min_string_length_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_cardinal(
                length,
                self.get_min_string_length_metadata()):
            raise InvalidArgument()
        if self.my_osid_object_form.max_string_length is not None and \
                length > self.my_osid_object_form.max_string_length - 1:
            raise InvalidArgument()
        self.my_osid_object_form._my_map['minStringLength'] = length
        self._min_string_length = length

    def clear_min_string_length(self):
        """stub"""
        if (self.get_min_string_length_metadata().is_read_only() or
                self.get_min_string_length_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['minStringLength'] = \
            self.get_min_string_length_metadata().get_default_cardinal_values()[0]

    min_string_length = property(fset=set_min_string_length,
                                 fdel=clear_min_string_length)

    def get_max_string_length_metadata(self):
        """stub"""
        return Metadata(**self._max_string_length_metadata)

    def set_max_string_length(self, length=None):
        """stub"""
        if self.get_max_string_length_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_cardinal(
                length,
                self.get_max_string_length_metadata()):
            raise InvalidArgument()
        if self.my_osid_object_form.min_string_length is not None and \
                length < self.my_osid_object_form.min_string_length + 1:
            raise InvalidArgument()
        self.my_osid_object_form._my_map['maxStringLength'] = length
        self._max_string_length = length

    def clear_max_string_length(self):
        """stub"""
        if (self.get_max_string_length_metadata().is_read_only() or
                self.get_max_string_length_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['maxStringLength'] = \
            self.get_max_string_length_metadata().get_default_cardinal_values()[0]

    max_string_length = property(fset=set_max_string_length,
                                 fdel=clear_max_string_length)


class IntegerAnswerRecord(IntegerValueRecord, abc_assessment_records.AnswerRecord):
    """answer that is an integer"""
    _implemented_record_type_identifiers = [
        'integer-answer'
    ]


class IntegerAnswerFormRecord(IntegerValueFormRecord,
                              abc_assessment_records.AnswerFormRecord):
    """form to create / edit answers that are integers"""
    _implemented_record_type_identifiers = [
        'integer-answer'
    ]


class IntegerAnswersRecord(IntegerValuesRecord, abc_assessment_records.AnswerRecord):
    """multiple integer answers"""
    _implemented_record_type_identifiers = [
        'integer-answers'
    ]


class IntegerAnswersFormRecord(IntegerValuesFormRecord,
                               abc_assessment_records.AnswerFormRecord):
    """form for multiple integer answers"""
    _implemented_record_type_identifiers = [
        'integer-answers'
    ]


class DecimalAnswerRecord(DecimalValueRecord, abc_assessment_records.AnswerRecord):
    """single decimal answer"""
    _implemented_record_type_identifiers = [
        'decimal-answer'
    ]


class DecimalAnswerFormRecord(DecimalValueFormRecord,
                              abc_assessment_records.AnswerFormRecord):
    """form for single decimal answer"""
    _implemented_record_type_identifiers = [
        'decimal-answer'
    ]


class DecimalAnswersRecord(DecimalValuesRecord, abc_assessment_records.AnswerRecord):
    """multiple decimal answers"""
    _implemented_record_type_identifiers = [
        'decimal-answers'
    ]


class DecimalAnswersFormRecord(DecimalValuesFormRecord,
                               abc_assessment_records.AnswerFormRecord):
    """form for multiple decimal answers"""
    _implemented_record_type_identifiers = [
        'decimal-answers'
    ]


class FileAnswerRecord(FileRecord, abc_assessment_records.AnswerRecord):
    """answer that is a file"""
    _implemented_record_type_identifiers = [
        'file-answer'
    ]


class FileAnswerFormRecord(FileFormRecord, abc_assessment_records.AnswerFormRecord):
    """form for file-based answer"""
    _implemented_record_type_identifiers = [
        'file-answer'
    ]


class FilesAnswerRecord(FilesRecord, abc_assessment_records.AnswerRecord):
    """answer that is multiple files"""
    _implemented_record_type_identifiers = [
        'files-answer'
    ]


class FilesAnswerFormRecord(FilesFormRecord, abc_assessment_records.AnswerFormRecord):
    """form for multiple-file answers"""
    _implemented_record_type_identifiers = [
        'files-answer'
    ]


class FilesQuestionRecord(FilesRecord, abc_assessment_records.QuestionRecord):
    """questions with multiple files"""
    _implemented_record_type_identifiers = [
        'files-question'
    ]


class FilesQuestionFormRecord(FilesFormRecord, abc_assessment_records.QuestionFormRecord):
    """form for questions with multiple files"""
    _implemented_record_type_identifiers = [
        'files-question'
    ]


class BankColorRecord(ColorCoordinateRecord, abc_assessment_records.BankRecord):
    """assessment banks with color attribute"""
    _implemented_record_type_identifiers = [
        'bank-color'
    ]


class BankColorFormRecord(ColorCoordinateFormRecord, abc_assessment_records.BankFormRecord):
    """form for assessment banks with color attribute"""
    _implemented_record_type_identifiers = [
        'bank-color'
    ]


class AnswerTextAndFilesMixin(TextAnswerFormRecord,
                              FilesAnswerFormRecord):
    """Mixin class to make the two classes compatible with super()
    for _init_map and _init_metadata

    """
    def _init_map(self):
        """stub"""
        TextAnswerFormRecord._init_map(self)
        FilesAnswerFormRecord._init_map(self)
        super(AnswerTextAndFilesMixin, self)._init_map()

    def _init_metadata(self):
        """stub"""
        TextAnswerFormRecord._init_metadata(self)
        FilesAnswerFormRecord._init_metadata(self)
        super(AnswerTextAndFilesMixin, self)._init_metadata()
