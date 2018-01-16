# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
records.repository.basic.media_accessibility.py
"""
from dlkit.json_ import utilities, types
from dlkit.json_.osid.metadata import Metadata
from dlkit.json_.osid import record_templates as osid_records

from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.transport.objects import DataInputStream
from dlkit.abstract_osid.osid.errors import InvalidArgument, NoAccess

from ...osid.base_records import MultiLanguageUtils, ObjectInitRecord,\
    FilesFormRecord, FilesRecord

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))


class AssetContentMultiLanguageAltTextRecord(MultiLanguageUtils, ObjectInitRecord):
    """asset content with alt-text"""
    _implemented_record_type_identifiers = [
        'asset-content-alt-text'
    ]

    def _update_object_map(self, obj_map):
        obj_map['altText'] = self._dict_display_text(self.my_osid_object.get_alt_text())
        return obj_map

    def get_alt_text(self):
        return self.get_matching_language_value('altTexts')

    alt_text = property(fget=get_alt_text)


class AssetContentMultiLanguageAltTextFormRecord(MultiLanguageUtils, osid_records.OsidRecord):
    """form for asset content with alt-text"""
    _implemented_record_type_identifiers = [
        'asset-content-alt-text'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(AssetContentMultiLanguageAltTextFormRecord, self).__init__()

    def _init_metadata(self, **kwargs):
        self._alt_texts_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'alt_text'),
            'element_label': 'Alt Text',
            'instructions': 'Enter as many alt texts as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def _init_map(self, **kwargs):
        self.my_osid_object_form._my_map['altTexts'] = self._alt_texts_metadata['default_object_values'][0]

    def get_alt_texts_metadata(self):
        """Gets the metadata for all alt_texts.

        return: (osid.Metadata) - metadata for the alt_texts
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._alt_texts_metadata)
        metadata.update({'existing_string_values': [t['text'] for t in self.my_osid_object_form._my_map['altTexts']]})
        return Metadata(**metadata)

    alt_texts_metadata = property(fget=get_alt_texts_metadata)

    @utilities.arguments_not_none
    def add_alt_text(self, alt_text):
        """Adds an alt_text.

        arg:    alt_text (displayText): the new alt_text
        raise:  InvalidArgument - ``alt_text`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``alt_text`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_alt_texts_metadata().is_read_only():
            raise NoAccess()
        self.add_or_replace_value('altTexts', alt_text)

    def clear_alt_texts(self):
        """Removes all alt_texts.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_alt_texts_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['altTexts'] = []

    @utilities.arguments_not_none
    def remove_alt_text_language(self, language_type):
        """Removes the specified alt_text.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_alt_texts_metadata().is_read_only():
            raise NoAccess()
        self.remove_field_by_language('altTexts',
                                      language_type)

    @utilities.arguments_not_none
    def edit_alt_text(self, new_alt_text):
        if self.get_alt_texts_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_alt_text, DisplayText):
            raise InvalidArgument()
        index = self.get_index_of_language_type('altTexts',
                                                new_alt_text.language_type)

        self.my_osid_object_form._my_map['altTexts'][index] = self._dict_display_text(new_alt_text)


class AssetContentMultiLanguageMediaDescriptionRecord(MultiLanguageUtils, ObjectInitRecord):
    """asset content with media description"""
    _implemented_record_type_identifiers = [
        'asset-content-media-description'
    ]

    def _update_object_map(self, obj_map):
        obj_map['mediaDescription'] = self._dict_display_text(self.my_osid_object.get_media_description())
        return obj_map

    def get_media_description(self):
        return self.get_matching_language_value('mediaDescriptions')

    media_description = property(fget=get_media_description)


class AssetContentMultiLanguageMediaDescriptionFormRecord(MultiLanguageUtils, osid_records.OsidRecord):
    """form for asset content with media description"""
    _implemented_record_type_identifiers = [
        'asset-content-media-description'
    ]

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(AssetContentMultiLanguageMediaDescriptionFormRecord, self).__init__()

    def _init_metadata(self, **kwargs):
        self._media_descriptions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'media_description'),
            'element_label': 'Media Description',
            'instructions': 'Enter as many media descriptions as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def _init_map(self, **kwargs):
        self.my_osid_object_form._my_map['mediaDescriptions'] = self._media_descriptions_metadata['default_object_values'][0]

    def get_media_descriptions_metadata(self):
        """Gets the metadata for all media descriptions.

        return: (osid.Metadata) - metadata for the media descriptions
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._media_descriptions_metadata)
        metadata.update({'existing_string_values': [t['text'] for t in self.my_osid_object_form._my_map['mediaDescriptions']]})
        return Metadata(**metadata)

    media_descriptions_metadata = property(fget=get_media_descriptions_metadata)

    @utilities.arguments_not_none
    def add_media_description(self, media_description):
        """Adds a media_description.

        arg:    media_description (displayText): the new media_description
        raise:  InvalidArgument - ``media_description`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``media_description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_media_descriptions_metadata().is_read_only():
            raise NoAccess()
        self.add_or_replace_value('mediaDescriptions', media_description)

    def clear_media_descriptions(self):
        """Removes all media_descriptions.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_media_descriptions_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['mediaDescriptions'] = []

    @utilities.arguments_not_none
    def remove_media_description_language(self, language_type):
        """Removes the specified media_description.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_media_descriptions_metadata().is_read_only():
            raise NoAccess()
        self.remove_field_by_language('mediaDescriptions',
                                      language_type)

    @utilities.arguments_not_none
    def edit_media_description(self, new_media_description):
        if self.get_media_descriptions_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_media_description, DisplayText):
            raise InvalidArgument()
        index = self.get_index_of_language_type('altTexts',
                                                new_media_description.language_type)

        self.my_osid_object_form._my_map['mediaDescriptions'][index] = self._dict_display_text(new_media_description)


class AssetContentMultiLanguageVTTRecord(FilesRecord):
    """asset content with video vtt files"""
    _implemented_record_type_identifiers = [
        'asset-content-vtt-files'
    ]

    def get_vtt_locale_label(self):
        # Is there a way to derive this from the default language type?
        locale = self.my_osid_object.get_vtt_locale_identifier()
        if locale == 'HIN':
            return 'Hindi'
        elif locale == 'TEL':
            return 'Telugu'
        return 'English'

    def get_vtt_locale_identifier(self):
        locale = DEFAULT_LANGUAGE_TYPE.identifier
        proxy = self.my_osid_object._proxy
        if proxy.locale is not None:
            locale = proxy.locale.language_type.identifier

        valid_locales = list(self.my_osid_object._my_map['fileIds'].keys())
        if locale in valid_locales:
            return locale
        elif DEFAULT_LANGUAGE_TYPE.identifier in valid_locales:
            return DEFAULT_LANGUAGE_TYPE.identifier

        if len(valid_locales) > 0:
            # by default, return first one
            return valid_locales[0]

        return None

    def get_vtt_url(self):
        # deprecated method -- don't really use tis
        locale = self.my_osid_object.get_vtt_locale_identifier()

        if locale is not None:
            # Don't use the get_url_by_label method, because we actually
            # Need this to stream via this ID
            # Calling self.my_osid_object.get_url() throws IllegalState in this case
            #   because it doesn't have it's own, actual `url` value.
            # So just call ac.get_url() via filesystem_adapter
            return self.my_osid_object.get_url()
            # return self.my_osid_object.get_url_by_label(locale)  # locale here is the label

        return ''

    vtt_url = property(fget=get_vtt_url)

    def get_vtt_text(self):
        locale = self.my_osid_object.get_vtt_locale_identifier()

        if locale is not None:
            return self.my_osid_object.get_file_by_label(locale).read()  # locale is the label

        return ''

    vtt_text = property(fget=get_vtt_text)


class AssetContentMultiLanguageVTTFormRecord(FilesFormRecord):
    """form for asset content with video vtt files
    Assumes VTT files will be added as
    """
    _implemented_record_type_identifiers = [
        'asset-content-vtt-files'
    ]

    @utilities.arguments_not_none
    def add_vtt_file(self, vtt_file, language_type=None):
        """Adds a vtt file tagged as the given language.

        arg:    vtt_file (displayText): the new vtt_file
        raise:  InvalidArgument - ``vtt_file`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``media_description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(vtt_file, DataInputStream):
            raise InvalidArgument('vtt_file')
        # for now, don't bother with genusTypeIds for the newly created
        # asset or assetContent...supposed to be managed via this one, I think
        locale = DEFAULT_LANGUAGE_TYPE.identifier
        if language_type is not None:
            locale = language_type.identifier
        self.my_osid_object_form.add_file(vtt_file,
                                          locale,
                                          asset_name="VTT File Container",
                                          asset_description="Used by an asset content to manage multi-language VTT files")

    def clear_vtt_files(self):
        """Removes all vtt files.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self.my_osid_object_form.clear_files()

    @utilities.arguments_not_none
    def remove_vtt_file_language(self, language_type):
        """Removes the specified vtt file.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self.my_osid_object_form.clear_file(language_type.identifier)

    @utilities.arguments_not_none
    def edit_vtt_file(self, new_vtt_file, language_type):
        if not isinstance(new_vtt_file, DataInputStream):
            raise InvalidArgument('new_vtt_file')
        # for now, don't bother with genusTypeIds for the newly created
        # asset or assetContent...supposed to be managed via this one, I think
        self.my_osid_object_form.clear_file(language_type.identifier)
        self.my_osid_object_form.add_file(new_vtt_file,
                                          language_type.identifier,
                                          asset_name="VTT File Container",
                                          asset_description="Used by an asset content to manage multi-language VTT files")


class AssetContentMultiLanguageTranscriptRecord(FilesRecord):
    """asset content with video / audio transcript files"""
    _implemented_record_type_identifiers = [
        'asset-content-transcript-files'
    ]

    def get_transcript_locale_label(self):
        # Is there a way to derive this from the default language type?
        locale = self.my_osid_object.get_transcript_locale_identifier()
        if locale == 'HIN':
            return 'वीडियो प्रतिलेख'
        elif locale == 'TEL':
            return 'వీడియో ట్రాన్స్క్రిప్ట్'
        return 'Transcript'

    def get_transcript_locale_identifier(self):
        locale = DEFAULT_LANGUAGE_TYPE.identifier
        proxy = self.my_osid_object._proxy
        if proxy.locale is not None:
            locale = proxy.locale.language_type.identifier

        valid_locales = list(self.my_osid_object._my_map['fileIds'].keys())
        if locale in valid_locales:
            return locale
        elif DEFAULT_LANGUAGE_TYPE.identifier in valid_locales:
            return DEFAULT_LANGUAGE_TYPE.identifier

        if len(valid_locales) > 0:
            # by default, return first one
            return valid_locales[0]

        return None

    def get_transcript_text(self):
        locale = self.my_osid_object.get_transcript_locale_identifier()

        if locale is not None:
            return self.my_osid_object.get_file_by_label(locale).read()  # locale is the label

        return ''

    transcript = property(fget=get_transcript_text)


class AssetContentMultiLanguageTranscriptFormRecord(FilesFormRecord):
    """form for asset content with video / audio transcript files
    """
    _implemented_record_type_identifiers = [
        'asset-content-transcript-files'
    ]

    @utilities.arguments_not_none
    def add_transcript_file(self, transcript_file, language_type=None):
        """Adds a transcript file tagged as the given language.

        arg:    transcript_file (displayText): the new transcript_file
        raise:  InvalidArgument - ``transcript_file`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``media_description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if not isinstance(transcript_file, DataInputStream):
            raise InvalidArgument('transcript_file')
        # for now, don't bother with genusTypeIds for the newly created
        # asset or assetContent...supposed to be managed via this one, I think
        locale = DEFAULT_LANGUAGE_TYPE.identifier
        if language_type is not None:
            locale = language_type.identifier
        self.my_osid_object_form.add_file(transcript_file,
                                          locale,
                                          asset_name="Transcript File Container",
                                          asset_description="Used by an asset content to manage multi-language Transcript files")

    def clear_transcript_files(self):
        """Removes all transcript files.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self.my_osid_object_form.clear_files()

    @utilities.arguments_not_none
    def remove_transcript_file_language(self, language_type):
        """Removes the specified transcript file.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        self.my_osid_object_form.clear_file(language_type.identifier)

    @utilities.arguments_not_none
    def edit_transcript_file(self, new_transcript_file, language_type):
        if not isinstance(new_transcript_file, DataInputStream):
            raise InvalidArgument('new_transcript_file')
        # for now, don't bother with genusTypeIds for the newly created
        # asset or assetContent...supposed to be managed via this one, I think
        self.my_osid_object_form.clear_file(language_type.identifier)
        self.my_osid_object_form.add_file(new_transcript_file,
                                          language_type.identifier,
                                          asset_name="Transcript File Container",
                                          asset_description="Used by an asset content to manage multi-language transcript files")
