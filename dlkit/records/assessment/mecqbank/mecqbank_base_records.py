"""
records.assessment.mecqbank.mecqbank_base_records.py
"""

from dlkit.json_ import types
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.utilities import is_string

from dlkit.abstract_osid.osid.errors import NotFound,\
    IllegalState,\
    InvalidArgument,\
    NullArgument,\
    NoAccess
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type


from ...osid.base_records import FilesRecord,\
    FilesFormRecord,\
    TextsFormRecord,\
    TextsRecord,\
    QueryInitRecord,\
    ObjectInitRecord,\
    ProvenanceFormRecord

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))

PDF_PREVIEW_ASSET_TYPE = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'repository.Asset',
    'identifier': 'mecqbank-pdf-preview',
    'display_name': 'PDF Preview',
    'display_label': 'PDF Preview',
    'description': 'Asset type for a PDF preview of a MecQBank item',
    'domain': 'repository.Asset'
})


PDF_ASSET_CONTENT_GENUS_TYPE = Type(**{
    'authority': 'iana.org',
    'namespace': 'asset-content-genus-type',
    'identifier': 'pdf',
    'display_name': 'application/PDF',
    'display_label': 'application/PDF',
    'description': 'A PDF file',
    'domain': 'repository.AssetContent'
})


class PDFPreviewRecord(FilesRecord):
    """for records with a PDF preview file"""
    _implemented_record_type_identifiers = [
        'mecqbank-pdf-preview'
    ]

    def has_preview(self):
        """stub"""
        # I had to add the following check because file record types don't seem to be implemented
        # correctly for raw edx Question objects
        if ('fileIds' not in self.my_osid_object._my_map or
                'preview' not in self.my_osid_object._my_map['fileIds'] or
                self.my_osid_object._my_map['fileIds']['preview'] is None):
            return False
        return bool(self.my_osid_object._my_map['fileIds']['preview'])

    def get_preview(self):
        """stub"""
        if self.has_preview():
            pass
        raise LookupError("No PDF file preview available.")

    def get_preview_raw(self):
        """stub"""
        if self.has_preview():
            pass
        raise LookupError("No PDF file preview available.")

    preview = property(fget=get_preview)
    preview_raw = property(fget=get_preview_raw)


class PDFPreviewFormRecord(FilesFormRecord):
    """form to add pdf preview file"""
    _implemented_record_type_identifiers = [
        'mecqbank-pdf-preview'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(PDFPreviewFormRecord, self).__init__(osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(PDFPreviewFormRecord, self)._init_map()

    def _init_metadata(self):
        """stub"""
        super(PDFPreviewFormRecord, self)._init_metadata()
        self._preview_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'file'),
            'element_label': 'File',
            'instructions': 'accepts an Asset Id',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def get_file_metadata(self):
        """stub"""
        return Metadata(**self._file_metadata)

    def add_preview(self, preview_data, file_name):
        """stub"""
        label = 'preview'
        asset_type = PDF_PREVIEW_ASSET_TYPE
        asset_content_type = PDF_ASSET_CONTENT_GENUS_TYPE
        self.add_file(preview_data,
                      label=label,
                      asset_type=asset_type,
                      asset_content_type=asset_content_type,
                      asset_name=file_name,
                      asset_description='A PDF file with rendered LaTeX.')

    def clear_preview(self):
        """stub"""
        try:
            rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        except AttributeError:
            rm = self.my_osid_object_form._get_provider_manager('REPOSITORY')
        try:
            aas = rm.get_asset_admin_session_for_repository(
                Id(self.my_osid_object._my_map['assignedBankIds'][0]))
        except AttributeError:
            # for update forms
            aas = rm.get_asset_admin_session_for_repository(
                Id(self.my_osid_object_form._my_map['assignedBankIds'][0]))
        if 'preview' not in self.my_osid_object_form._my_map['fileIds']:
            raise NotFound()
        aas.delete_asset(
            Id(self.my_osid_object_form._my_map['fileIds']['preview']['assetId']))
        del self.my_osid_object_form._my_map['fileIds']['preview']


class SimpleDifficultyItemRecord(TextsRecord):
    """record with one of 3 difficulty levels: low, medium, hard"""
    _implemented_record_type_identifiers = [
        'simple-difficulty',
        'texts-record'
    ]

    def has_difficulty_value(self):
        """stub"""
        return 'difficulty' in self.my_osid_object._my_map['texts']

    def get_difficulty_value(self):
        """stub"""
        if self.has_difficulty_value():
            return self.my_osid_object._my_map['texts']['difficulty']['text']
        raise IllegalState()

    difficulty = property(fget=get_difficulty_value)


class SimpleDifficultyItemFormRecord(TextsFormRecord):
    """form for simple difficulty records"""
    _implemented_record_type_identifiers = [
        'simple-difficulty',
        'texts-record'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(SimpleDifficultyItemFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(SimpleDifficultyItemFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['texts']['difficulty'] = \
            self._difficulty_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        super(SimpleDifficultyItemFormRecord, self)._init_metadata()
        self._min_string_length = None
        self._max_string_length = None
        self._difficulty_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'text'),
            'element_label': 'Text',
            'instructions': 'enter a text string',
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

    def get_difficulty_metadata(self):
        """stub"""
        return Metadata(**self._difficulty_metadata)

    def set_difficulty(self, difficulty):
        """stub"""
        if not is_string(difficulty):
            raise InvalidArgument('difficulty value must be a string')
        if difficulty.lower() not in ['low', 'medium', 'hard']:
            raise InvalidArgument('difficulty value must be low, medium, or hard')
        self.my_osid_object_form._my_map['texts']['difficulty']['text'] = difficulty

    def clear_difficulty(self):
        """stub"""
        if (self.get_difficulty_metadata().is_read_only() or
                self.get_difficulty_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['texts']['difficulty'] = \
            self._difficulty_metadata['default_string_values'][0]


class SimpleDifficultyItemQueryRecord(QueryInitRecord):
    """make difficulty a queryable field"""
    def match_difficulty(self, value):
        """stub"""
        self._my_osid_query._add_match('texts.difficulty', str(value).lower(), True)

    def clear_match_difficulty(self):
        """stub"""
        self._my_osid_query._add_match('texts.difficulty')


class SourceItemRecord(TextsRecord):
    """give a text source field"""
    _implemented_record_type_identifiers = [
        'mecqbank-source',
        'texts-record'
    ]

    def has_source_value(self):
        """stub"""
        return 'source' in self.my_osid_object._my_map['texts']

    def get_source_value(self):
        """stub"""
        if self.has_source_value():
            return self.my_osid_object._my_map['texts']['source']['text']
        raise IllegalState()

    source = property(fget=get_source_value)


class SourceItemFormRecord(TextsFormRecord):
    """form to add / edit a source"""
    _implemented_record_type_identifiers = [
        'mecqbank-source',
        'texts-record'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(SourceItemFormRecord, self).__init__(
            osid_object_form=osid_object_form)

    def _init_map(self):
        """stub"""
        super(SourceItemFormRecord, self)._init_map()
        self.my_osid_object_form._my_map['texts']['source'] = \
            self._source_metadata['default_string_values'][0]

    def _init_metadata(self):
        """stub"""
        super(SourceItemFormRecord, self)._init_metadata()
        self._min_string_length = None
        self._max_string_length = None
        self._source_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'text'),
            'element_label': 'Text',
            'instructions': 'enter a text string',
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

    def get_source_metadata(self):
        """stub"""
        return Metadata(**self._source_metadata)

    def set_source(self, source):
        """stub"""
        if not is_string(source):
            raise InvalidArgument('source value must be a string')
        self.my_osid_object_form._my_map['texts']['source']['text'] = source

    def clear_source(self):
        """stub"""
        if (self.get_source_metadata().is_read_only() or
                self.get_source_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['texts']['source'] = \
            self._source_metadata['default_string_values'][0]


class SourceItemQueryRecord(QueryInitRecord):
    """make source a queryable field"""

    def match_source(self, value):
        """stub"""
        self._my_osid_query._add_match('texts.source', str(value), True)

    def clear_match_source(self):
        """stub"""
        self._my_osid_query._add_match('texts.source')


class PublishedRecord(ObjectInitRecord):
    """flag for published or not"""
    _implemented_record_type_identifiers = [
        'mecqbank-published'
    ]

    def is_published(self):
        """stub"""
        if 'published' not in self.my_osid_object._my_map:
            return False
        return bool(self.my_osid_object._my_map['published'])

    published = property(fget=is_published)


class PublishedFormRecord(osid_records.OsidRecord):
    """form to set published flag"""
    _implemented_record_type_identifiers = [
        'mecqbank-published'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(PublishedFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['published'] = \
            self._published_metadata['default_published_values'][0]

    def _init_metadata(self):
        """stub"""
        self._published_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'published'),
            'element_label': 'Published',
            'instructions': 'flags if item is published or not',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_published_values': [False],
            'syntax': 'BOOLEAN',
        }

    def get_published_metadata(self):
        """stub"""
        return Metadata(**self._published_metadata)

    def set_published(self, value=None):
        """stub"""
        if value is None:
            raise NullArgument()
        if self.get_published_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_boolean(value):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['published'] = value

    def clear_published(self):
        """stub"""
        if (self.get_published_metadata().is_read_only() or
                self.get_published_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['published'] = \
            self._published_metadata['default_published_values'][0]

    published = property(fset=set_published, fdel=clear_published)


class MecQBankBaseMixin(SimpleDifficultyItemFormRecord,
                        SourceItemFormRecord,
                        PDFPreviewFormRecord,
                        PublishedFormRecord,
                        ProvenanceFormRecord):
    """to make this cooperative with super()"""

    def _init_map(self):
        """stub"""
        SimpleDifficultyItemFormRecord._init_map(self)
        SourceItemFormRecord._init_map(self)
        PDFPreviewFormRecord._init_map(self)
        PublishedFormRecord._init_map(self)
        ProvenanceFormRecord._init_map(self)
        super(MecQBankBaseMixin, self)._init_map()

    def _init_metadata(self):
        """stub"""
        SimpleDifficultyItemFormRecord._init_metadata(self)
        SourceItemFormRecord._init_metadata(self)
        PDFPreviewFormRecord._init_metadata(self)
        PublishedFormRecord._init_metadata(self)
        ProvenanceFormRecord._init_metadata(self)
        super(MecQBankBaseMixin, self)._init_metadata()
