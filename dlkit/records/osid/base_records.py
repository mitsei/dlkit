from __future__ import unicode_literals

import base64
import datetime
import re
import os
import sys
import codecs

from bs4 import BeautifulSoup
from bson.objectid import ObjectId

from dlkit.json_ import types, utilities
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid import record_templates as osid_records
from dlkit.json_.osid import mdata_conf
from dlkit.json_.osid.metadata import Metadata

from dlkit.abstract_osid.osid.errors import NotFound, IllegalState, \
    InvalidArgument, NoAccess, NullArgument, OperationFailed,\
    Unsupported, Unimplemented
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.primordium.locale.primitives import DisplayText
from dlkit.primordium.calendaring.primitives import DateTime
from dlkit.primordium.mapping.color_primitives import RGBColorCoordinate
from dlkit.primordium.transport.objects import DataInputStream

if getattr(sys, 'frozen', False):
    ABS_PATH = os.path.dirname(sys.executable)
else:
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    ABS_PATH = '{0}'.format(os.path.abspath(os.path.join(PROJECT_PATH, os.pardir)))

DEFAULT_LANGUAGE_TYPE = Type(**types.Language().get_type_data('DEFAULT'))
DEFAULT_SCRIPT_TYPE = Type(**types.Script().get_type_data('DEFAULT'))
DEFAULT_FORMAT_TYPE = Type(**types.Format().get_type_data('DEFAULT'))

# This type definition should go elsewhere:
RGB_COLOR_COORDINATE = Type(identifier='rgb_color',
                            authority='ODL.MIT.EDU',
                            namespace='mapping.Coordinate',
                            display_name='RGB Color Coordinate',
                            display_label='RGB Color',
                            description='Coordinate Type for an RGB Color',
                            domain='mapping.Coordinate')


class AssetUtils(object):
    """Useful methods for getting and managing assets directly from a record"""

    def _get_asset_content(self, asset_id, asset_content_type_str=None, asset_content_id=None):
        """stub"""
        rm = self.my_osid_object._get_provider_manager('REPOSITORY')
        if 'assignedBankIds' in self.my_osid_object._my_map:
            if self.my_osid_object._proxy is not None:
                als = rm.get_asset_lookup_session_for_repository(
                    Id(self.my_osid_object._my_map['assignedBankIds'][0]),
                    self.my_osid_object._proxy)
            else:
                als = rm.get_asset_lookup_session_for_repository(
                    Id(self.my_osid_object._my_map['assignedBankIds'][0]))
        elif 'assignedBookIds' in self.my_osid_object._my_map:
            if self.my_osid_object._proxy is not None:
                als = rm.get_asset_lookup_session_for_repository(
                    Id(self.my_osid_object._my_map['assignedBookIds'][0]),
                    self.my_osid_object._proxy)
            else:
                als = rm.get_asset_lookup_session_for_repository(
                    Id(self.my_osid_object._my_map['assignedBookIds'][0]))
        elif 'assignedRepositoryIds' in self.my_osid_object._my_map:
            if self.my_osid_object._proxy is not None:
                als = rm.get_asset_lookup_session_for_repository(
                    Id(self.my_osid_object._my_map['assignedRepositoryIds'][0]),
                    self.my_osid_object._proxy)
            else:
                als = rm.get_asset_lookup_session_for_repository(
                    Id(self.my_osid_object._my_map['assignedRepositoryIds'][0]))
        else:
            raise KeyError

        if asset_content_id is not None:
            ac_list = als.get_asset(asset_id).get_asset_contents()
            for ac in ac_list:
                if str(ac.ident) == str(asset_content_id):
                    return ac

        if not asset_content_type_str:
            return next(als.get_asset(asset_id).get_asset_contents())  # Just return first one
        else:

            if isinstance(asset_content_type_str, Type):
                asset_content_type_str = str(asset_content_type_str)
            for ac in als.get_asset(asset_id).get_asset_contents():
                if ac.get_genus_type() == Type(asset_content_type_str):
                    return ac
        raise NotFound()

    def create_asset(self,
                     asset_data=None,
                     asset_type=None,
                     asset_content_type=None,
                     asset_content_record_types=None,
                     display_name='',
                     description=''):
        """stub"""
        # This method creates a new Asset in the Repository orchestrated
        # with this AssessmentBank:
        return self._set_asset(asset_data=asset_data,
                               asset_type=asset_type,
                               asset_content_type=asset_content_type,
                               asset_content_record_types=asset_content_record_types,
                               display_name=display_name,
                               description=description)

    def _set_asset(self,
                   asset_data=None,
                   asset_type=None,
                   asset_content_type=None,
                   asset_content_record_types=None,
                   display_name='',
                   description=''):
        """stub"""
        # This method should be deprecated and its code added to the create_asset method:
        rm = self.my_osid_object_form._get_provider_manager('REPOSITORY')
        catalog_id = ''
        try:
            # for create forms
            catalog_id = self.my_osid_object_form._catalog_id
        except AttributeError:
            # for update forms
            if 'assignedBankIds' in self.my_osid_object_form._my_map:
                catalog_id = Id(self.my_osid_object_form._my_map['assignedBankIds'][0])
            elif 'assignedRepositoryIds' in self.my_osid_object_form._my_map:
                catalog_id = Id(self.my_osid_object_form._my_map['assignedRepositoryIds'][0])

        try:
            aas = rm.get_asset_admin_session_for_repository(
                catalog_id,
                self.my_osid_object_form._proxy)
        except (TypeError, NullArgument):  # not a ProxyManager, so don't pass it the proxy
            aas = rm.get_asset_admin_session_for_repository(
                catalog_id)
        afc = aas.get_asset_form_for_create([])
        if asset_type is not None:
            afc.set_genus_type(asset_type)

        afc.set_display_name(display_name)
        afc.set_description(description)
        asset_id = aas.create_asset(afc).get_id()
        ac = None
        if asset_data is not None:
            asset_content_type_list = asset_content_record_types
            if asset_content_type_list is None:
                asset_content_type_list = []

            try:
                config = self.my_osid_object_form._runtime.get_configuration()
                parameter_id = Id('parameter:assetContentRecordTypeForFiles@json')
                asset_content_type_list.append(
                    config.get_value_by_parameter(parameter_id).get_type_value())
            except (AttributeError, KeyError, NotFound):
                pass

            acfc = aas.get_asset_content_form_for_create(asset_id,
                                                         asset_content_type_list)
            if asset_content_type is not None:
                acfc.set_genus_type(asset_content_type)

            acfc.set_data(asset_data)
            ac = aas.create_asset_content(acfc)

            # really stupid, but set the data again, because for filesystem impl
            # the ID above will be off by one-ish -- we need it to match the
            # AssetContent ID, so re-set it.
            # have to set it above so that the filesystem adapter kicks in on update
            # asset_data.seek(0)
            # acfu = aas.get_asset_content_form_for_update(ac.ident)
            # acfu.set_data(asset_data)
            # ac = aas.update_asset_content(acfu)
        if ac is not None:
            return asset_id, ac.ident
        else:
            return asset_id, None

    def add_content_to_asset(self,
                             asset_id,
                             asset_data=None,
                             asset_url=None,
                             asset_content_type=None,
                             asset_label=None):
        """stub"""
        # This method creates a new AssetContent related to the given asset_id:
        return self._add_asset_content(asset_id=asset_id,
                                       asset_data=asset_data,
                                       asset_url=asset_url,
                                       asset_content_type=asset_content_type,
                                       asset_label=asset_label)

    # This is almost the same as _set_asset.  Combine?
    # This method should be deprecated and its code added to the
    # create_asset method:
    def _add_asset_content(self,
                           asset_id,
                           asset_data=None,
                           asset_url=None,
                           asset_content_type=None,
                           asset_label=None):
        """stub"""
        rm = self.my_osid_object_form._get_provider_manager('REPOSITORY')
        try:
            # for create forms
            catalog_id = self.my_osid_object_form._catalog_id
        except AttributeError:
            # for update forms
            catalog_id = Id(self.my_osid_object_form._my_map['assignedBankIds'][0])

        try:
            aas = rm.get_asset_admin_session_for_repository(
                catalog_id,
                self.my_osid_object_form._proxy)
        except (TypeError, NullArgument):  # not a ProxyManager, so don't pass it the proxy
            aas = rm.get_asset_admin_session_for_repository(
                catalog_id)

        asset_content_type_list = []
        try:
            config = self.my_osid_object_form._runtime.get_configuration()
            parameter_id = Id('parameter:assetContentRecordTypeForFiles@json')
            asset_content_type_list.append(
                config.get_value_by_parameter(parameter_id).get_type_value())
        except (AttributeError, KeyError):
            pass

        acfc = aas.get_asset_content_form_for_create(asset_id,
                                                     asset_content_type_list)
        if asset_content_type is not None:
            acfc.set_genus_type(asset_content_type)
        if asset_label is not None:
            acfc.display_name = str(asset_label)
        if asset_data:
            acfc.set_data(asset_data)
        if asset_url:
            acfc.set_url(asset_url)
        ac = aas.create_asset_content(acfc)

        return asset_id, ac.ident


class MultiLanguageUtils(object):
    @staticmethod
    def _empty_display_text():
        return DisplayText(display_text_map={
            'text': '',
            'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
            'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
            'formatTypeId': str(DEFAULT_FORMAT_TYPE)
        })

    def _display_text_dict(self, text_string):
        try:
            proxy = self.my_osid_object._proxy
        except AttributeError:
            proxy = self.my_osid_object_form._proxy
        finally:
            if proxy is None or (proxy is not None and proxy.locale is None):
                return {
                    'text': text_string,
                    'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                    'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                    'formatTypeId': str(DEFAULT_FORMAT_TYPE)
                }
            else:
                return {
                    'text': text_string,
                    'languageTypeId': str(proxy.locale.language_type),
                    'scriptTypeId': str(proxy.locale.script_type),
                    'formatTypeId': str(DEFAULT_FORMAT_TYPE)
                }

    @staticmethod
    def _dict_display_text(display_text):
        if not isinstance(display_text, DisplayText):
            raise InvalidArgument('text must be instance of DisplayText')
        return {
            'text': display_text.text,
            'languageTypeId': str(display_text.language_type),
            'scriptTypeId': str(display_text.script_type),
            'formatTypeId': str(display_text.format_type)
        }

    def _str_display_text(self, text_string):
        try:
            proxy = self.my_osid_object._proxy
        except AttributeError:
            proxy = self.my_osid_object_form._proxy
        finally:
            if proxy is None or proxy.locale is None:
                return DisplayText(**{
                    'text': text_string,
                    'language_type': DEFAULT_LANGUAGE_TYPE,
                    'script_type': DEFAULT_SCRIPT_TYPE,
                    'format_type': DEFAULT_FORMAT_TYPE
                })
            return DisplayText(**{
                'text': text_string,
                'language_type': proxy.locale.language_type,
                'script_type': proxy.locale.script_type,
                'format_type': DEFAULT_FORMAT_TYPE
            })

    def add_or_replace_value(self, field, new_value, dictionary=None):
        try:
            self.my_osid_object
            raise IllegalState('Not a form object -- cannot call this method')
        except AttributeError:
            if dictionary is None:
                dictionary = self.my_osid_object_form._my_map
            if not isinstance(dictionary, dict):
                raise InvalidArgument('dictionary is not a dict')
            if not isinstance(new_value, DisplayText):
                raise InvalidArgument('{0} is not a DisplayText'.format(field))
            if field not in dictionary:
                raise InvalidArgument('{0} is not in dictionary'.format(str(field)))

            # need to check for an existing languageTypeId match. If found, replace that one
            # instead. Otherwise, append.
            current_language_types = [current_value['languageTypeId'] for current_value in dictionary[field]]
            if str(new_value.language_type) in current_language_types:
                dictionary[field][current_language_types.index(str(new_value.language_type))] = self._dict_display_text(new_value)
            else:
                dictionary[field].append(self._dict_display_text(new_value))

    def get_default_language_value(self, field, dictionary):
        if not isinstance(dictionary, dict):
            raise InvalidArgument('dictionary is not a dict')
        if field not in dictionary:
            raise InvalidArgument('{0} is not in the dictionary'.format(str(field)))
        default_texts = [t
                         for t in dictionary[field]
                         if t['languageTypeId'] == str(DEFAULT_LANGUAGE_TYPE)]
        if len(default_texts) == 0:
            return DisplayText(display_text_map=dictionary[field][0])
        else:
            return DisplayText(display_text_map=default_texts[0])

    def get_matching_language_value(self, field, dictionary=None):
        try:
            self.my_osid_object_form
            raise IllegalState('This method cannot be used with form objects')
        except AttributeError:
            if dictionary is None:
                dictionary = self.my_osid_object._my_map
            if not isinstance(dictionary, dict):
                raise InvalidArgument('dictionary is not instance of dict')

            if (field not in dictionary or
                    len(dictionary[field]) == 0):
                return self._empty_display_text()

            proxy = self.my_osid_object._proxy
            if proxy is None or proxy.locale is None:
                return self.get_default_language_value(field, dictionary)
            else:
                matching_texts = [t
                                  for t in dictionary[field]
                                  if t['languageTypeId'] == str(proxy.locale.language_type)]
                if len(matching_texts) == 0:
                    return self.get_default_language_value(field, dictionary)
                else:
                    return DisplayText(display_text_map=matching_texts[0])

    def get_index_of_language_type(self, field, language_type, dictionary=None):
        try:
            self.my_osid_object
            raise IllegalState('This method can only be used with forms')
        except AttributeError:
            if dictionary is None:
                dictionary = self.my_osid_object_form._my_map
            if not isinstance(dictionary, dict):
                raise InvalidArgument('dictionary is not instance of dict')
            if field not in dictionary:
                raise InvalidArgument('{0} is not in dictionary'.format(str(field)))

            index = None
            for ind, display_text_dict in enumerate(dictionary[field]):
                if display_text_dict['languageTypeId'] == str(language_type):
                    index = ind
                    break
            if index is None:
                raise InvalidArgument('that language does not exist yet. Use the "add_{0}" method instead'.format(field))
            return index

    def remove_field_by_language(self, field, language_type, dictionary=None):
        try:
            self.my_osid_object
            raise IllegalState('This method can only be used with forms')
        except AttributeError:
            if dictionary is None:
                dictionary = self.my_osid_object_form._my_map
            if not isinstance(dictionary, dict):
                raise InvalidArgument('dictionary is not dict')
            if field not in dictionary:
                raise InvalidArgument('{0} not in dictionary'.format(str(field)))

            if not isinstance(language_type, Type):
                raise InvalidArgument('language_type is not a Type')
            dictionary[field] = [t
                                 for t in dictionary[field]
                                 if t['languageTypeId'] != str(language_type)]


class ObjectInitRecord(osid_records.OsidRecord):
    """base record class"""

    def __init__(self, osid_object):
        self.my_osid_object = osid_object
        super(ObjectInitRecord, self).__init__()


class ProvenanceRecord(ObjectInitRecord):
    """Provenance == "parent record" of this record...simple way to track
    item inheritance."""

    def get_creator_id(self):
        """stub"""
        return Id(self.my_osid_object._my_map['creatorId'])

    creator_id = property(fget=get_creator_id)

    def get_creation_time(self):
        """stub"""
        ct = self.my_osid_object._my_map['creationTime']
        return DateTime(ct.year,
                        ct.month,
                        ct.day,
                        ct.hour,
                        ct.minute,
                        ct.second,
                        ct.microsecond)

    create_time = property(fget=get_creation_time)

    def has_provenance(self):
        """stub"""
        return bool(self.my_osid_object._my_map['provenanceId'] != '')

    def get_provenance_id(self):
        """stub"""
        if self.has_provenance():
            return self.my_osid_object._my_map['provenanceId']
        raise IllegalState()

    def get_provenance_parent(self):
        """stub"""
        pass  # needs to be over-written

    def has_provenance_children(self):
        """stub"""
        pass  # needs to be over-written

    def get_provenance_children(self):
        """stub"""
        pass  # needs to be over-written

    provenance = property(fget=get_provenance_id)
    provenance_children = property(fget=get_provenance_children)
    provenance_parent = property(fget=get_provenance_parent)

    def _update_object_map(self, obj_map):
        """stub"""
        creation_time = obj_map['creationTime']
        obj_map['creationTime'] = dict()
        obj_map['creationTime']['year'] = creation_time.year
        obj_map['creationTime']['month'] = creation_time.month
        obj_map['creationTime']['day'] = creation_time.day
        obj_map['creationTime']['hour'] = creation_time.hour
        obj_map['creationTime']['minute'] = creation_time.minute
        obj_map['creationTime']['second'] = creation_time.second
        obj_map['creationTime']['microsecond'] = creation_time.microsecond


class ProvenanceFormRecord(osid_records.OsidRecord):
    """form to create / update a record's provenance itemId"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(ProvenanceFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['provenanceId'] = \
            self._provenance_metadata['default_object_values'][0]
        if not self.my_osid_object_form.is_for_update():
            if 'effectiveAgentId' in self.my_osid_object_form._kwargs:
                self.my_osid_object_form._my_map['creatorId'] = \
                    str(self.my_osid_object_form._kwargs['effectiveAgentId'])
            else:
                self.my_osid_object_form._my_map['creatorId'] = ''
            self.my_osid_object_form._my_map['creationTime'] = \
                datetime.datetime.now()

    def _init_metadata(self):
        """stub"""
        self._provenance_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'provenanceId'),
            'element_label': 'provenanceId',
            'instructions': 'The item that "gave birth" to this item.',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [''],
            'syntax': 'STRING',
            'minimum_string_length': None,
            'maximum_string_length': None,
            'string_set': []
        }

    def get_provenance_metadata(self):
        """stub"""
        return Metadata(**self._provenance_metadata)

    def set_provenance(self, provenance_id):
        """stub"""
        if not self.my_osid_object_form._is_valid_string(
                provenance_id, self.get_provenance_metadata()):
            raise InvalidArgument('provenanceId')
        self.my_osid_object_form._my_map['provenanceId'] = provenance_id

    def clear_provenance(self):
        """stub"""
        self.my_osid_object_form._my_map['provenanceId'] = \
            self._provenance_metadata['default_object_values'][0]


class QueryInitRecord(osid_records.OsidRecord):
    """base record for making queries"""

    def __init__(self, osid_query):
        self._my_osid_query = osid_query
        super(QueryInitRecord, self).__init__()


class ResourceIdRecord(ObjectInitRecord):
    """basic extension for something that points to a resource"""

    def has_resource_id(self):
        """stub"""
        return bool(self.my_osid_object._my_map['resourceId'])

    def get_resource_id(self):
        """stub"""
        if self.has_resource_id():
            return Id(self.my_osid_object._my_map['resourceId'])
        raise IllegalState()

    resource_id = property(fget=get_resource_id)


class ResourceFormRecord(osid_records.OsidRecord):
    """basic form record"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(ResourceFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['resourceId'] = \
            self._resource_id_metadata['default_id_values'][0]

    def _init_metadata(self):
        """stub"""
        self._resource_id_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'resource_id'),
            'element_label': 'Resource Id',
            'instructions': 'accepts a valid OSID Id',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def get_resource_id_metadata(self):
        """stub"""
        return Metadata(**self._resource_id_metadata)

    def set_resource_id(self, resource_id=None):
        """stub"""
        if resource_id is None:
            raise NullArgument()
        if self.get_resource_id_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_id(
                resource_id):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['resourceId'] = resource_id

    def clear_resource_id(self):
        """stub"""
        if (self.get_resource_id_metadata().is_read_only() or
                self.get_resource_id_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['resourceId'] = \
            self.get_resource_id_metadata().get_default_id_values()[0]

    resource_id = property(fset=set_resource_id, fdel=clear_resource_id)


class TextRecord(ObjectInitRecord):
    """objects with a single text value"""

    def has_text(self):
        """stub"""
        return bool(self.my_osid_object._my_map['text']['text'])

    def get_text(self):
        """stub"""
        if self.has_text():
            return DisplayText(self.my_osid_object._my_map['text'])
        raise IllegalState('no text available')

    text = property(fget=get_text)


class TextFormRecord(osid_records.OsidRecord):
    """form to create / update the text value"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(TextFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['text'] = \
            dict(self._text_metadata['default_string_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_string_length = None
        self._max_string_length = None
        self._text_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'text'),
            'element_label': 'text',
            'instructions': 'enter some text',
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

    def get_text_metadata(self):
        """stub"""
        return Metadata(**self._text_metadata)

    def set_text(self, text=None):
        """stub"""
        if text is None:
            raise NullArgument()
        if self.get_text_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_string(
                text,
                self.get_text_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['text']['text'] = text

    def clear_text(self):
        """stub"""
        if (self.get_text_metadata().is_read_only() or
                self.get_text_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['text'] = \
            dict(self.get_text_metadata().get_default_string_values()[0])

    text = property(fset=set_text, fdel=clear_text)


class IntegerValueRecord(ObjectInitRecord):
    """records with a single integer value"""

    def has_integer(self):
        """stub"""
        return bool(self.my_osid_object._my_map['integerValue'] is not None)

    def get_integer(self):
        """stub"""
        if self.has_integer():
            return int(self.my_osid_object._my_map['integerValue'])
        raise IllegalState('integerValue')

    integer = property(fget=get_integer)


class IntegerValueFormRecord(osid_records.OsidRecord):
    """form to create / update an integer value"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(IntegerValueFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['integerValue'] = \
            self._integer_value_metadata['default_integer_values'][0]

    def _init_metadata(self):
        """stub"""
        self._min_integer_value = None
        self._max_integer_value = None
        self._integer_value_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'integer_value'),
            'element_label': 'Integer Value',
            'instructions': 'enter an integer value',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_values': [None],
            'syntax': 'INTEGER',
            'minimum_integer': self._min_integer_value,
            'maximum_integer': self._max_integer_value,
            'integer_set': []
        }

    def get_integer_value_metadata(self):
        """stub"""
        return Metadata(**self._integer_value_metadata)

    def set_integer_value(self, value=None):
        """stub"""
        if value is None:
            raise NullArgument()
        if self.get_integer_value_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_integer(
                value,
                self.get_integer_value_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['integerValue'] = int(value)

    def clear_integer_value(self):
        """stub"""
        if (self.get_integer_value_metadata().is_read_only() or
                self.get_integer_value_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['integerValue'] = \
            self.get_integer_value_metadata().get_default_integer_values()[0]

    integer_value = property(fset=set_integer_value, fdel=clear_integer_value)


class DecimalValueRecord(ObjectInitRecord):
    """record with a single decimal value"""

    def has_decimal(self):
        """stub"""
        return bool(self.my_osid_object._my_map['decimalValue'] is not None)

    def get_decimal(self):
        """stub"""
        if self.has_decimal():
            return float(self.my_osid_object._my_map['decimalValue'])
        raise IllegalState('decimalValue')

    decimal = property(fget=get_decimal)


class DecimalValueFormRecord(osid_records.OsidRecord):
    """form to create / update a decimal value"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(DecimalValueFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['decimalValue'] = \
            self._decimal_value_metadata['default_decimal_values'][0]

    def _init_metadata(self):
        """stub"""
        self._min_decimal_value = None
        self._max_decimal_value = None
        self._decimal_value_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'decimal_value'),
            'element_label': 'Decimal Value',
            'instructions': 'enter a decimal value',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_decimal_values': [None],
            'syntax': 'DECIMAL',
            'decimal_scale': None,
            'minimum_decimal': self._min_decimal_value,
            'maximum_decimal': self._max_decimal_value,
            'decimal_set': []
        }

    def get_decimal_value_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def set_decimal_value(self, value=None):
        """stub"""
        if value is None:
            raise NullArgument()
        if self.get_decimal_value_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_decimal(
                value,
                self.get_decimal_value_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['decimalValue'] = float(value)

    def clear_decimal_value(self):
        """stub"""
        if (self.get_decimal_value_metadata().is_read_only() or
                self.get_decimal_value_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['decimalValue'] = \
            self.get_decimal_value_metadata().get_default_decimal_values()[0]

    decimal_value = property(fset=set_decimal_value, fdel=clear_decimal_value)


class TextsRecord(ObjectInitRecord):
    """records with multiple text values, stored in a dict"""

    def has_texts(self):
        """stub"""
        return bool(self.my_osid_object._my_map['texts'])

    def get_texts_map(self):
        """stub"""
        if self.has_texts():
            return self.my_osid_object._my_map['texts']
        raise IllegalState()

    def has_text(self, label):
        """stub"""
        if label in self.my_osid_object._my_map['texts']:
            return True
        return False

    def get_text(self, label):
        """stub"""
        if self.has_text(label):
            # Should this return a DisplayText?
            return DisplayText(self.my_osid_object._my_map['texts'][label])
        raise IllegalState()

    texts_map = property(fget=get_texts_map)


class TextsFormRecord(osid_records.OsidRecord):
    """form to create / update text values"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(TextsFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['texts'] = \
            dict(self._texts_metadata['default_object_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_string_length = None
        self._max_string_length = None
        self._texts_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'texts'),
            'element_label': 'Texts',
            'instructions': 'enter text with optional label',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._text_metadata = {
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
        self._label_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'label'),
            'element_label': 'Label',
            'instructions': 'enter a string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [str(ObjectId())],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 128,
            'string_set': []
        }

    def get_texts_metadata(self):
        """stub"""
        return Metadata(**self._texts_metadata)

    def get_text_metadata(self):
        """stub"""
        return Metadata(**self._text_metadata)

    def get_label_metadata(self):
        """stub"""
        return Metadata(**self._label_metadata)

    def add_text(self, text, label=None):
        """stub"""
        if label is None:
            label = self._label_metadata['default_string_values'][0]
        else:
            if not self.my_osid_object_form._is_valid_string(
                    label, self.get_label_metadata()) or '.' in label:
                raise InvalidArgument('label')
        if text is None:
            raise NullArgument('text cannot be none')
        if not (self.my_osid_object_form._is_valid_string(
                text, self.get_text_metadata()) or isinstance(text, DisplayText)):
            raise InvalidArgument('text')
        if utilities.is_string(text):
            self.my_osid_object_form._my_map['texts'][label] = {
                'text': text,
                'languageTypeId': str(DEFAULT_LANGUAGE_TYPE),
                'scriptTypeId': str(DEFAULT_SCRIPT_TYPE),
                'formatTypeId': str(DEFAULT_FORMAT_TYPE)
            }
        else:
            self.my_osid_object_form._my_map['texts'][label] = {
                'text': text.text,
                'languageTypeId': str(text.language_type),
                'scriptTypeId': str(text.script_type),
                'formatTypeId': str(text.format_type)
            }

    def clear_text(self, label):
        """stub"""
        if label not in self.my_osid_object_form._my_map['texts']:
            raise NotFound()
        del self.my_osid_object_form._my_map['texts'][label]

    def clear_texts(self):
        """stub"""
        if self._texts_metadata['required'] or self._texts_metadata['read_only']:
            raise NoAccess()
        self.my_osid_object_form._my_map['texts'] = \
            dict(self._texts_metadata['default_object_values'][0])


class IntegerValuesRecord(ObjectInitRecord):
    """records with multiple integer values"""

    def has_integer_values(self):
        """stub"""
        return bool(self.my_osid_object._my_map['integerValues'])

    def get_integer_values_map(self):
        """stub"""
        if self.has_integer_values():
            return self.my_osid_object._my_map['integerValues']
        raise IllegalState()

    def has_integer_value(self, label):
        """stub"""
        if label in self.my_osid_object._my_map['integerValues']:
            return True
        return False

    def get_integer_value(self, label):
        """stub"""
        if self.has_integer_value(label):
            return int(self.my_osid_object._my_map['integerValues'][label])
        raise IllegalState()

    integer_values_map = property(fget=get_integer_values_map)


class IntegerValuesFormRecord(osid_records.OsidRecord):
    """form for create / update of multiple integer values"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(IntegerValuesFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['integerValues'] = \
            dict(self._integer_values_metadata['default_object_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_integer_value = None
        self._max_integer_value = None
        self._integer_values_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'integer_values'),
            'element_label': 'Integer Values',
            'instructions': 'enter integer values with optional labels',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._integer_value_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'integer_value'),
            'element_label': 'Integer Value',
            'instructions': 'enter an integer value',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_integer_value': [None],
            'syntax': 'INTEGER',
            'minimum_integer': self._min_integer_value,
            'maximum_integer': self._max_integer_value,
            'integer_set': []
        }
        self._label_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'label'),
            'element_label': 'Label',
            'instructions': 'enter a string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [str(ObjectId())],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 128,
            'string_set': []
        }

    def get_integer_values_metadata(self):
        """stub"""
        return Metadata(**self._integer_values_metadata)

    def get_integer_value_metadata(self):
        """stub"""
        return Metadata(**self._integer_value_metadata)

    def get_label_metadata(self):
        """stub"""
        return Metadata(**self._label_metadata)

    def add_integer_value(self, value, label=None):
        """stub"""
        if value is None:
            raise NullArgument('value cannot be None')
        if label is None:
            label = self._label_metadata['default_string_values'][0]
        else:
            if not self.my_osid_object_form._is_valid_string(
                    label, self.get_label_metadata()) or '.' in label:
                raise InvalidArgument('label')
        if not self.my_osid_object_form._is_valid_integer(
                value, self.get_integer_value_metadata()):
            raise InvalidArgument('value')
        self.my_osid_object_form._my_map['integerValues'][label] = value

    def clear_integer_value(self, label):
        """stub"""
        if label not in self.my_osid_object_form._my_map['integerValues']:
            raise NotFound()
        del self.my_osid_object_form._my_map['integerValues'][label]

    def clear_integer_values(self):
        """stub"""
        if self._integer_values_metadata['required'] or \
                self._integer_values_metadata['read_only']:
            raise NoAccess()
        self.my_osid_object_form._my_map['integerValues'] = \
            dict(self._integer_values_metadata['default_object_values'][0])


class DecimalValuesRecord(ObjectInitRecord):
    """record with multiple decimal values"""

    def has_decimal_values(self):
        """stub"""
        return bool(self.my_osid_object._my_map['decimalValues'])

    def get_decimal_values_map(self):
        """stub"""
        if self.has_decimal_values():
            return self.my_osid_object._my_map['decimalValues']
        raise IllegalState()

    def has_decimal_value(self, label):
        """stub"""
        if label in self.my_osid_object._my_map['decimalValues']:
            return True
        return False

    def get_decimal_value(self, label):
        """stub"""
        if self.has_decimal_value(label):
            return float(self.my_osid_object._my_map['decimalValues'][label])
        raise IllegalState()

    decimal_values_map = property(fget=get_decimal_values_map)


class DecimalValuesFormRecord(osid_records.OsidRecord):
    """form for create / update of multiple decimal values"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(DecimalValuesFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['decimalValues'] = \
            dict(self._decimal_values_metadata['default_object_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_decimal_value = None
        self._max_decimal_value = None
        self._decimal_values_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'decimal_values'),
            'element_label': 'Decimal Values',
            'instructions': 'enter decimal values with optional labels',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._decimal_value_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'decimal_value'),
            'element_label': 'Decimal Value',
            'instructions': 'enter a decimal value',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_decimal_values': [None, 0.0],
            'syntax': 'DECIMAL',
            'decimal_scale': None,
            'minimum_decimal': self._min_decimal_value,
            'maximum_decimal': self._max_decimal_value,
            'decimal_set': []
        }
        self._label_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'label'),
            'element_label': 'Label',
            'instructions': 'enter a string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [str(ObjectId())],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 128,
            'string_set': []
        }

    def get_decimal_values_metadata(self):
        """stub"""
        return Metadata(**self._decimal_values_metadata)

    def get_decimal_value_metadata(self):
        """stub"""
        return Metadata(**self._decimal_value_metadata)

    def get_label_metadata(self):
        """stub"""
        return Metadata(**self._label_metadata)

    def add_decimal_value(self, value, label=None):
        """stub"""
        if label is None:
            label = self._label_metadata['default_string_values'][0]
        else:
            if not self.my_osid_object_form._is_valid_string(
                    label, self.get_label_metadata()) or '.' in label:
                raise InvalidArgument('label')
        if value is None:
            raise NullArgument('value cannot be None')
        if not self.my_osid_object_form._is_valid_decimal(
                value, self.get_decimal_value_metadata()):
            raise InvalidArgument('value')
        self.my_osid_object_form._my_map['decimalValues'][label] = value

    def clear_decimal_value(self, label):
        """stub"""
        if label not in self.my_osid_object_form._my_map['decimalValues']:
            raise NotFound()
        del self.my_osid_object_form._my_map['decimalValues'][label]

    def clear_decimal_values(self):
        """stub"""
        if self._decimal_values_metadata['required'] or \
                self._decimal_values_metadata['read_only']:
            raise NoAccess()
        self.my_osid_object_form._my_map['decimalValues'] = \
            dict(self._decimal_values_metadata['default_object_values'][0])


class edXBaseRecord(ObjectInitRecord):
    """record with edX problem metadata attributes"""

    def has_attempts(self):
        """stub"""
        return bool(self.my_osid_object._my_map['attempts'] is not None)

    def get_attempts(self):
        """stub"""
        if self.has_attempts():
            return int(self.my_osid_object._my_map['attempts'])
        raise IllegalState()

    def has_weight(self):
        """stub"""
        return bool(self.my_osid_object._my_map['weight'] is not None)

    def get_weight(self):
        """stub"""
        if self.has_weight():
            return float(self.my_osid_object._my_map['weight'])
        raise IllegalState()

    # def has_rerandomize(self):
    #     """stub"""
    #     return bool(self.my_osid_object._my_map['rerandomize'] is not None)
    #
    # def get_rerandomize(self):
    #     """stub"""
    #     if self.has_rerandomize():
    #         return self.my_osid_object._my_map['rerandomize']
    #     raise IllegalState()

    def has_showanswer(self):
        """stub"""
        return bool(self.my_osid_object._my_map['showanswer'] is not None)

    def get_showanswer(self):
        """stub"""
        if self.has_showanswer():
            return self.my_osid_object._my_map['showanswer']
        raise IllegalState()

    def has_markdown(self):
        """stub"""
        return bool(self.my_osid_object._my_map['markdown'] != '')

    def get_markdown(self):
        """stub"""
        if self.has_markdown():
            return self.my_osid_object._my_map['markdown']
        raise IllegalState()

    attempts = property(fget=get_attempts)
    weight = property(fget=get_weight)
    # rerandomize = property(fget=get_rerandomize)
    showanswer = property(fget=get_showanswer)
    markdown = property(fget=get_markdown)


class edXBaseFormRecord(osid_records.OsidRecord):
    """form for create / update of edX metadata fields"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(edXBaseFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['attempts'] = \
            int(self._attempts_metadata['default_object_values'][0])
        self.my_osid_object_form._my_map['weight'] = \
            float(self._weight_metadata['default_object_values'][0])
        # self.my_osid_object_form._my_map['rerandomize'] = \
        #     self._rerandomize_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['showanswer'] = \
            str(self._showanswer_metadata['default_object_values'][0])
        self.my_osid_object_form._my_map['markdown'] = \
            str(self._markdown_metadata['default_object_values'][0])

    def _init_metadata(self):
        """stub"""
        self._attempts_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'attempts'),
            'element_label': 'Attempts',
            'instructions': 'Max number of student attempts',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [0],
            'syntax': 'INTEGER',
            'object_set': [],
            'minimum_integer': None,
            'maximum_integer': None,
            'integer_set': []
        }
        self._weight_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'weight'),
            'element_label': 'Weight',
            'instructions': 'Weight of the item when calculating grades',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [1.0],
            'syntax': 'DECIMAL',
            'object_set': [],
            'decimal_scale': None,
            'minimum_decimal': None,
            'maximum_decimal': None,
            'decimal_set': []
        }
        # self._rerandomize_metadata = {
        #     'element_id': Id(self.my_osid_object_form._authority,
        #                      self.my_osid_object_form._namespace,
        #                      'rerandomize'),
        #     'element_label': 'Randomize',
        #     'instructions': 'How to rerandomize the parameters',
        #     'required': False,
        #     'read_only': False,
        #     'linked': False,
        #     'array': False,
        #     'default_object_values': ['never'],
        #     'syntax': 'STRING',
        #     'minimum_string_length': None,
        #     'maximum_string_length': None,
        #     'string_set': []
        # }
        self._showanswer_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'showanswer'),
            'element_label': 'Show answer',
            'instructions': 'When to show the answer to the student',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': ['closed'],
            'syntax': 'STRING',
            'minimum_string_length': None,
            'maximum_string_length': None,
            'string_set': []
        }
        self._markdown_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'markdown'),
            'element_label': 'Studio markdown',
            'instructions': 'Studio markdown representation of the problem',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [''],
            'syntax': 'STRING',
            'minimum_string_length': None,
            'maximum_string_length': None,
            'string_set': []
        }

    def get_attempts_metadata(self):
        """stub"""
        return Metadata(**self._attempts_metadata)

    def get_weight_metadata(self):
        """stub"""
        return Metadata(**self._weight_metadata)

    # def get_rerandomize_metadata(self):
    #     """stub"""
    #     return Metadata(**self._rerandomize_metadata)

    def get_showanswer_metadata(self):
        """stub"""
        return Metadata(**self._showanswer_metadata)

    def get_markdown_metadata(self):
        """stub"""
        return Metadata(**self._markdown_metadata)

    def add_attempts(self, attempts):
        """stub"""
        if attempts is None:
            raise NullArgument('attempts cannot be None')
        if not self.my_osid_object_form._is_valid_integer(
                attempts, self.get_attempts_metadata()):
            raise InvalidArgument('attempts')
        self.my_osid_object_form._my_map['attempts'] = attempts

    def clear_attempts(self):
        """stub"""
        self.my_osid_object_form._my_map['attempts'] = \
            int(self._attempts_metadata['default_object_values'][0])

    def add_weight(self, weight):
        """stub"""
        if weight is None:
            raise NullArgument('weight cannot be None')
        if not self.my_osid_object_form._is_valid_decimal(
                weight, self.get_weight_metadata()):
            raise InvalidArgument('weight')
        self.my_osid_object_form._my_map['weight'] = weight

    def clear_weight(self):
        """stub"""
        self.my_osid_object_form._my_map['weight'] = \
            float(self._weight_metadata['default_object_values'][0])

    # def add_rerandomize(self, rerandomize):
    #     """stub"""
    #     if not self.my_osid_object_form._is_valid_string(
    #             rerandomize, self.get_rerandomize_metadata()):
    #         raise InvalidArgument('rerandomize')
    #     self.my_osid_object_form._my_map['rerandomize'] = rerandomize
    #
    # def clear_rerandomize(self):
    #     """stub"""
    #     self.my_osid_object_form._my_map['rerandomize'] = \
    #         self._rerandomize_metadata['default_object_values'][0]

    def add_showanswer(self, showanswer):
        """stub"""
        if showanswer is None:
            raise NullArgument('showanswer cannot be None')
        if not self.my_osid_object_form._is_valid_string(
                showanswer, self.get_showanswer_metadata()):
            raise InvalidArgument('showanswer')
        self.my_osid_object_form._my_map['showanswer'] = showanswer

    def clear_showanswer(self):
        """stub"""
        self.my_osid_object_form._my_map['showanswer'] = \
            str(self._showanswer_metadata['default_object_values'][0])

    def add_markdown(self, markdown):
        """stub"""
        if markdown is None:
            raise NullArgument('markdown cannot be None')
        if not self.my_osid_object_form._is_valid_string(
                markdown, self.get_markdown_metadata()):
            raise InvalidArgument('markdown')
        self.my_osid_object_form._my_map['markdown'] = markdown

    def clear_markdown(self):
        """stub"""
        self.my_osid_object_form._my_map['markdown'] = \
            str(self._markdown_metadata['default_object_values'][0])


class TimeValueRecord(ObjectInitRecord):
    """records that store a time value"""

    def has_time(self):
        """stub"""
        return bool(self.my_osid_object._my_map['timeValue'] is not None)

    def get_time(self):
        """stub"""
        if self.has_time():
            return self.my_osid_object._my_map['timeValue']
        raise IllegalState()

    def get_time_as_string(self):
        """stub"""
        if self.has_time():
            return (str(self.time['hours']).zfill(2) + ':' +
                    str(self.time['minutes']).zfill(2) + ':' +
                    str(self.time['seconds']).zfill(2))
        raise IllegalState()

    time = property(fget=get_time)
    time_str = property(fget=get_time_as_string)


class TimeValueFormRecord(osid_records.OsidRecord):
    """form to create / update the time value"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(TimeValueFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['timeValue'] = \
            dict(self._time_value_metadata['default_duration_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_time_value = None
        self._max_time_value = None
        self._time_value_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'time_value'),
            'element_label': 'Time Value',
            'instructions': 'enter a time duration string / duration',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_duration_values': [{
                'hours': 0,
                'minutes': 0,
                'seconds': 0
            }],
            'syntax': 'DURATION',
            'minimum_time': self._min_time_value,
            'maximum_time': self._max_time_value
        }

    def _convert_duration_to_hhmmss(self, duration):
        """stub"""
        time_secs = duration.seconds
        min_, sec = divmod(time_secs, 60)
        hour, min_ = divmod(min_, 60)
        results = {
            'hours': hour,
            'minutes': min_,
            'seconds': sec
        }

        return results

    def _convert_string_to_hhmmss(self, string):
        """stub"""
        # assume input string is 'hh:mm:ss'
        components = string.split(':')
        if len(components) != 3:
            raise InvalidArgument('time input string must be hh:mm:ss format')
        return {
            'hours': int(components[0]),
            'minutes': int(components[1]),
            'seconds': int(components[2])
        }

    def get_time_value_metadata(self):
        """stub"""
        return Metadata(**self._time_value_metadata)

    def set_time_value(self, value=None):
        """stub"""
        if value is None:
            raise NullArgument()
        if self.get_time_value_metadata().is_read_only():
            raise NoAccess()
        if self.my_osid_object_form._is_valid_duration(
                value,
                self.get_time_value_metadata()):
            # http://stackoverflow.com/questions/775049/python-time-seconds-to-hms
            time = self._convert_duration_to_hhmmss(value)
        elif utilities.is_string(value):
            # assume something like hh:mm:ss, convert to dict
            time = self._convert_string_to_hhmmss(value)
        else:
            raise InvalidArgument('value must be a string or duration')
        self.my_osid_object_form._my_map['timeValue'] = {
            'hours': time['hours'],
            'minutes': time['minutes'],
            'seconds': time['seconds']
        }

    def clear_time_value(self):
        """stub"""
        if (self.get_time_value_metadata().is_read_only() or
                self.get_time_value_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['timeValue'] = \
            dict(self.get_time_value_metadata().get_default_duration_values()[0])

    time_value = property(fset=set_time_value, fdel=clear_time_value)


class FilesRecord(AssetUtils, ObjectInitRecord):
    """for records that store files"""

    def has_files(self):
        """stub"""
        # I had to add the following check because file record types
        # don't seem to be implemented
        # correctly for raw edx Question objects
        if 'fileIds' not in self.my_osid_object._my_map:
            return False
        return bool(self.my_osid_object._my_map['fileIds'])

    # This impl should probably be deprecated, or updated to use the
    # get_data() method on the AssetContents
    def get_files_map(self):
        """stub"""
        files_map = {}
        if self.has_files():
            for label in self.my_osid_object._my_map['fileIds']:
                asset_content = self._get_asset_content(
                    Id(self.my_osid_object._my_map['fileIds'][label]['assetId']),
                    Type(self.my_osid_object._my_map['fileIds'][label]['assetContentTypeId']))
                try:
                    files_map[label] = asset_content._my_map['base64']
                except KeyError:
                    files_map[label] = base64.b64encode(asset_content.get_data().read())
            return files_map
        raise IllegalState('no files_map')

    files_map = property(fget=get_files_map)

    def get_file_urls_map(self):
        """stub"""
        file_urls_map = {}
        if self.has_files():
            for label in self.my_osid_object._my_map['fileIds']:
                label_map = self.my_osid_object._my_map['fileIds'][label]
                if 'assetContentId' in label_map and bool(label_map['assetContentId']):
                    asset_content = self._get_asset_content(
                        Id(label_map['assetId']),
                        asset_content_id=Id(label_map['assetContentId']))
                else:
                    asset_content = self._get_asset_content(
                        Id(label_map['assetId']),
                        asset_content_type_str=label_map['assetContentTypeId'])
                file_urls_map[label] = asset_content.get_url()
            return file_urls_map
        raise IllegalState('no files_map')

    def get_files(self):
        """stub"""
        try:
            return self.get_file_urls_map()
        except (IllegalState, NotFound):
            return self.get_files_map()

    file_urls_map = property(fget=get_file_urls_map)

    def has_file(self, label):
        """stub"""
        if label in self.my_osid_object._my_map['fileIds']:
            return True
        return False

    def get_asset_ids(self):
        """stub"""
        asset_ids = []
        for f in self.my_osid_object._my_map['fileIds']:
            asset_ids.append(Id(self.my_osid_object._my_map['fileIds'][f]['assetId']))
        return IdList(asset_ids)

    def get_asset_ids_map(self):
        """stub"""
        asset_ids_map = {}
        for label, asset_obj in self.my_osid_object._my_map['fileIds'].items():
            asset_ids_map[label] = asset_obj
        return asset_ids_map

    def get_asset_id_by_label(self, label):
        """stub"""
        if self.has_file(label):
            return Id(self.my_osid_object._my_map['fileIds'][label]['assetId'])
        raise IllegalState()

    def get_file_by_label(self, label, asset_content_type=None):
        """stub"""
        return self._get_asset_content(self.get_asset_id_by_label(label), asset_content_type).get_data()

    def get_url_by_label(self, label, asset_content_type=None):
        """stub"""
        return self._get_asset_content(self.get_asset_id_by_label(label)).get_url()

    def _delete(self):
        pass

    def _update_object_map(self, obj_map):
        """loop through all the keys in self.my_osid_object._my_map, and
        see if any of them contain text like "AssetContent:<label>"
        If so, assume it is markup (?), replace the string with asset_content.get_url()"""
        # TODO: Look for <img> tags to add in alt-text and description
        # TODO: Look for <video> and <audio> tags to add in description, transcripts and vtt files?
        try:
            super(FilesRecord, self)._update_object_map(obj_map)
        except AttributeError:
            pass

        def replace_url_in_display_text(potential_display_text, dict_files_map):
            if ('text' in potential_display_text and
                    potential_display_text['text'] is not None and
                    'AssetContent' in potential_display_text['text']):
                # assume markup? Wrap this in case it's not a valid XML doc
                # with a single parent object
                wrapped_text = '<wrapper>{0}</wrapper'.format(potential_display_text['text'])
                soup = BeautifulSoup(wrapped_text, 'xml')
                media_file_elements = soup.find_all(src=media_regex)
                media_file_elements += soup.find_all(data=media_regex)
                for media_file_element in media_file_elements:
                    if 'src' in media_file_element.attrs:
                        media_key = 'src'
                    else:
                        media_key = 'data'
                    if ':' not in media_file_element[media_key]:
                        continue

                    media_label = media_file_element[media_key].split(':')[-1]

                    if media_label in dict_files_map:
                        ac_id = Id(dict_files_map[media_label]['assetContentId'])
                        ac = acls.get_asset_content(ac_id)

                        if media_file_element.name == 'track':
                            try:
                                if not ac.has_files():
                                    continue
                            except AttributeError:
                                # non-multi-language VTT files
                                media_file_element[media_key] = ac.get_url()
                            else:
                                media_file_element[media_key] = ac.get_url()
                                media_file_element['srclang'] = ac.get_vtt_locale_identifier().lower()[0:2]
                                media_file_element['label'] = ac.get_vtt_locale_label()
                        elif media_file_element.name == 'transcript':
                            if not ac.has_files():
                                continue
                            transcript_template_path = '{0}/osid/transcript_template.xml'.format(ABS_PATH)
                            with codecs.open(transcript_template_path, 'r', encoding='utf-8') as template_file:
                                template = template_file.read().format(media_label,
                                                                       ac.get_transcript_locale_label().lower(),
                                                                       ac.get_transcript_locale_label().title(),
                                                                       ac.get_transcript_text())
                                new_template_tag = BeautifulSoup(template, 'xml').div
                                # media_file_element.replace_with(new_template_tag)
                                p_parent = None
                                for parent in media_file_element.parents:
                                    if parent is not None and parent.name != 'p':
                                        # insert the transcript after the top p tag
                                        # so that we don't create invalid HTML by nesting
                                        # <div> and <aside> inside of a <p> tag
                                        p_parent.insert_after(new_template_tag)
                                        break
                                    p_parent = parent
                                media_file_element.extract()
                        else:
                            media_file_element[media_key] = ac.get_url()

                    # check for alt-tags
                    if 'alt' in media_file_element.attrs:
                        alt_tag_label = media_file_element['alt'].split(':')[-1]
                        if alt_tag_label in dict_files_map:
                            ac_id = Id(dict_files_map[alt_tag_label]['assetContentId'])
                            ac = acls.get_asset_content(ac_id)
                            try:
                                media_file_element['alt'] = ac.get_alt_text().text
                            except AttributeError:
                                pass

                potential_display_text['text'] = soup.wrapper.renderContents().decode('utf-8')
            else:
                for new_key, value in potential_display_text.items():
                    if isinstance(value, list):
                        new_files_map = dict_files_map
                        if 'fileIds' in potential_display_text:
                            new_files_map = potential_display_text['fileIds']
                        potential_display_text[new_key] = check_list_children(value, new_files_map)
            return potential_display_text

        def check_list_children(potential_text_list, list_files_map):
            updated_list = []
            for child in potential_text_list:
                if isinstance(child, dict):
                    files_map = list_files_map
                    if 'fileIds' in child:
                        files_map = child['fileIds']
                    updated_list.append(replace_url_in_display_text(child, files_map))
                elif isinstance(child, list):
                    updated_list.append(check_list_children(child, list_files_map))
                else:
                    updated_list.append(child)
            return updated_list

        # One assumption is that the object's catalogId can be used
        # as the repositoryId
        manager = self.my_osid_object._get_provider_manager('REPOSITORY')
        try:
            if self.my_osid_object._proxy is not None:
                acls = manager.get_asset_content_lookup_session(proxy=self.my_osid_object._proxy)
            else:
                acls = manager.get_asset_content_lookup_session()
        except AttributeError:
            pass
        else:
            acls.use_federated_repository_view()
            media_regex = re.compile('(AssetContent:)')
            original_files_map = {}
            if 'fileIds' in obj_map:
                original_files_map = obj_map['fileIds']

            for key, data in obj_map.items():
                if isinstance(data, dict):
                    obj_map[key] = replace_url_in_display_text(data, original_files_map)
                elif isinstance(data, list):
                    obj_map[key] = check_list_children(data, original_files_map)


class FilesFormRecord(osid_records.OsidRecord, AssetUtils):
    """form to create / update attached files"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(FilesFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['fileIds'] = \
            dict(self._files_metadata['default_object_values'][0])

    def _init_metadata(self):
        """stub"""
        self._files_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'files'),
            'element_label': 'Files',
            'instructions': 'enter a file id with optional label',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._file_metadata = {
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
        self._label_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'label'),
            'element_label': 'Label',
            'instructions': 'enter a string',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_string_values': [str(ObjectId())],
            'syntax': 'STRING',
            'minimum_string_length': 0,
            'maximum_string_length': 128,
            'string_set': []
        }

    def get_file_metadata(self):
        """stub"""
        return Metadata(**self._file_metadata)

    def get_label_metadata(self):
        """stub"""
        return Metadata(**self._label_metadata)

    def add_asset(self, asset_id, asset_content_id=None, label=None, asset_content_type=None):
        """stub"""
        if asset_id is None:
            raise NullArgument('asset_id cannot be None')
        if not isinstance(asset_id, Id):
            raise InvalidArgument('asset_id must be an Id instance')
        if asset_content_id is not None and not isinstance(asset_content_id, Id):
            raise InvalidArgument('asset_content_id must be an Id instance')
        if asset_content_type is not None and not isinstance(asset_content_type, Type):
            raise InvalidArgument('asset_content_type must be a Type instance')
        if label is None:
            label = self._label_metadata['default_string_values'][0]
        else:
            if not self.my_osid_object_form._is_valid_string(
                    label, self.get_label_metadata()) or '.' in label:
                raise InvalidArgument('label')
        if asset_content_type is None:
            asset_content_type = ''

        self.my_osid_object_form._my_map['fileIds'][label] = {
            'assetId': str(asset_id),
            'assetContentTypeId': str(asset_content_type)
        }

        if asset_content_id is not None:
            self.my_osid_object_form._my_map['fileIds'][label].update({
                'assetContentId': str(asset_content_id)
            })

    def add_file(self,
                 asset_data,
                 label=None,
                 asset_type=None,
                 asset_content_type=None,
                 asset_content_record_types=None,
                 asset_name='',
                 asset_description=''):
        """stub"""
        if asset_data is None:
            raise NullArgument('asset_data cannot be None')
        if not isinstance(asset_data, DataInputStream):
            raise InvalidArgument('asset_data must be instance of DataInputStream')
        if asset_type is not None and not isinstance(asset_type, Type):
            raise InvalidArgument('asset_type must be an instance of Type')
        if asset_content_type is not None and not isinstance(asset_content_type, Type):
            raise InvalidArgument('asset_content_type must be an instance of Type')
        if asset_content_record_types is not None and not isinstance(asset_content_record_types, list):
            raise InvalidArgument('asset_content_record_types must be an instance of list')
        if asset_content_record_types is not None:
            for record_type in asset_content_record_types:
                if not isinstance(record_type, Type):
                    raise InvalidArgument('non-Type present in asset_content_record_types')

        if label is None:
            label = self._label_metadata['default_string_values'][0]
        else:
            if not self.my_osid_object_form._is_valid_string(
                    label, self.get_label_metadata()) or '.' in label:
                raise InvalidArgument('label')

        asset_id, asset_content_id = self.create_asset(asset_data=asset_data,
                                                       asset_type=asset_type,
                                                       asset_content_type=asset_content_type,
                                                       asset_content_record_types=asset_content_record_types,
                                                       display_name=asset_name,
                                                       description=asset_description)
        self.add_asset(asset_id,
                       asset_content_id,
                       label,
                       asset_content_type)

    def clear_file(self, label):
        """stub"""
        rm = self.my_osid_object_form._get_provider_manager('REPOSITORY')

        catalog_id_str = ''

        if 'assignedBankIds' in self.my_osid_object_form._my_map:
            catalog_id_str = self.my_osid_object_form._my_map['assignedBankIds'][0]
        elif 'assignedRepositoryIds' in self.my_osid_object_form._my_map:
            catalog_id_str = self.my_osid_object_form._my_map['assignedRepositoryIds'][0]
        try:
            try:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str),
                    self.my_osid_object_form._proxy)
            except NullArgument:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str))
        except AttributeError:
            # for update forms
            try:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str),
                    self.my_osid_object_form._proxy)
            except NullArgument:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str))

        if label not in self.my_osid_object_form._my_map['fileIds']:
            raise NotFound()
        aas.delete_asset(Id(self.my_osid_object_form._my_map['fileIds'][label]['assetId']))
        del self.my_osid_object_form._my_map['fileIds'][label]

    def clear_files(self):
        """stub"""
        # This could also be implemented by iterating over self.clear_file()
        if self._files_metadata['required'] or self._files_metadata['read_only']:
            raise NoAccess()
        rm = self.my_osid_object_form._get_provider_manager('REPOSITORY')

        catalog_id_str = ''

        if 'assignedBankIds' in self.my_osid_object_form._my_map:
            catalog_id_str = self.my_osid_object_form._my_map['assignedBankIds'][0]
        elif 'assignedRepositoryIds' in self.my_osid_object_form._my_map:
            catalog_id_str = self.my_osid_object_form._my_map['assignedRepositoryIds'][0]
        try:
            try:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str),
                    self.my_osid_object_form._proxy)
            except NullArgument:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str))
        except AttributeError:
            # for update forms
            try:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str),
                    self.my_osid_object_form._proxy)
            except NullArgument:
                aas = rm.get_asset_admin_session_for_repository(
                    Id(catalog_id_str))
        for label, asset_data in self.my_osid_object_form._my_map['fileIds'].items():
            aas.delete_asset(Id(asset_data['assetId']))
        self.my_osid_object_form._my_map['fileIds'] = \
            dict(self._files_metadata['default_object_values'][0])


class FileRecord(ObjectInitRecord, AssetUtils):
    """records with a single file"""

    def has_file_asset(self):
        """stub"""
        return bool(self.my_osid_object._my_map['fileId'])

    def has_file_url(self):
        """stub"""
        return bool(self._get_asset_content(
            Id(self.my_osid_object._my_map['fileId']['assetId']),
            self.my_osid_object._my_map['fileId']['assetContentTypeId']).has_url())

    def get_file_asset_id(self):
        """stub"""
        if self.has_file_asset():
            return Id(self.my_osid_object._my_map['fileId']['assetId'])
        raise IllegalState()

    def get_file_url(self):
        """stub"""
        if self.has_file_url():
            return self._get_asset_content(
                Id(self.my_osid_object._my_map['fileId']['assetId']),
                self.my_osid_object._my_map['fileId']['assetContentTypeId']).get_url()
        raise IllegalState()

    def get_file(self):
        """stub"""
        if self.has_file_asset():
            return self._get_asset_content(
                Id(self.my_osid_object._my_map['fileId']['assetId']),
                self.my_osid_object._my_map['fileId']['assetContentTypeId']).get_data()
        raise IllegalState()

    file_asset_id = property(fget=get_file_asset_id)
    file_url = property(fget=get_file_url)
    file_ = property(fget=get_file)


class FileFormRecord(osid_records.OsidRecord, AssetUtils):
    """form for create / update of a single file"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(FileFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['fileId'] = \
            dict(self._file_metadata['default_object_values'][0])

    def _init_metadata(self):
        """stub"""
        self._file_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'file'),
            'element_label': 'File',
            'instructions': 'accepts an asset id and optional asset_content type',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_object_values': [{}],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def get_file_metadata(self):
        """stub"""
        return Metadata(**self._file_metadata)

    def set_file(self,
                 asset_data=None,
                 asset_type=None,
                 asset_content_type=None,
                 asset_name='',
                 asset_description=''):
        """stub"""
        if asset_data is None:
            raise NullArgument()
        if not isinstance(asset_data, DataInputStream):
            raise InvalidArgument('asset_data must be instance of DataInputStream')
        if asset_type is not None and not isinstance(asset_type, Type):
            raise InvalidArgument('asset_type must be instance of Type')
        if asset_content_type is not None and not isinstance(asset_content_type, Type):
            raise InvalidArgument('asset_content_type must be instance of Type')

        asset_id, asset_content_id = self.create_asset(asset_data=asset_data,
                                                       asset_type=asset_type,
                                                       asset_content_type=asset_content_type,
                                                       display_name=asset_name,
                                                       description=asset_description)
        self.set_asset(asset_id,
                       asset_content_type)

    def set_asset(self, asset_id, asset_content_type=None):
        """stub"""
        if asset_id is None:
            raise NullArgument('asset_id cannot be None')
        if not isinstance(asset_id, Id):
            raise InvalidArgument('asset_id must be an instance of Id')
        if asset_content_type is not None and not isinstance(asset_content_type, Type):
            raise InvalidArgument('asset_content_type must be instance of Type')
        if asset_content_type is None:
            asset_content_type = ''
        self.my_osid_object_form._my_map['fileId'] = {
            'assetId': str(asset_id),
            'assetContentTypeId': str(asset_content_type)
        }

    def clear_file(self):
        """stub"""
        if (self.get_file_metadata().is_read_only() or
                self.get_file_metadata().is_required()):
            raise NoAccess()
        if 'assetId' in self.my_osid_object_form._my_map['fileId']:
            rm = self.my_osid_object_form._get_provider_manager('REPOSITORY')

            catalog_id_str = ''

            if 'assignedBankIds' in self.my_osid_object_form._my_map:
                catalog_id_str = self.my_osid_object_form._my_map['assignedBankIds'][0]
            elif 'assignedRepositoryIds' in self.my_osid_object_form._my_map:
                catalog_id_str = self.my_osid_object_form._my_map['assignedRepositoryIds'][0]
            try:
                try:
                    aas = rm.get_asset_admin_session_for_repository(
                        Id(catalog_id_str),
                        self.my_osid_object_form._proxy)
                except NullArgument:
                    aas = rm.get_asset_admin_session_for_repository(
                        Id(catalog_id_str))
            except AttributeError:
                # for update forms
                try:
                    aas = rm.get_asset_admin_session_for_repository(
                        Id(catalog_id_str),
                        self.my_osid_object_form._proxy)
                except NullArgument:
                    aas = rm.get_asset_admin_session_for_repository(
                        Id(catalog_id_str))

            aas.delete_asset(Id(self.my_osid_object_form._my_map['fileId']['assetId']))

        self.my_osid_object_form._my_map['fileId'] = \
            dict(self.get_file_metadata().get_default_object_values()[0])

    file_ = property(fset=set_file, fdel=clear_file)


class ColorCoordinateRecord(ObjectInitRecord):
    """records associated with a single color"""

    def has_color_coordinate(self):
        """stub"""
        return bool(self.my_osid_object._my_map['colorCoordinate'])

    def get_color_coordinate(self):
        """stub"""
        if self.has_color_coordinate():
            color_dict = self.my_osid_object._my_map['colorCoordinate']
            return RGBColorCoordinate(values=color_dict['values'],
                                      uncertainty_minus=color_dict['uncertaintyMinus'],
                                      uncertainty_plus=color_dict['uncertaintyPlus'])
        raise IllegalState('No color coordinate')

    color_coordinate = property(fget=get_color_coordinate)

    def _update_object_map(self, obj_map):
        """stub"""
        if self.has_color_coordinate() and \
                self.get_color_coordinate().get_coordinate_type() == RGB_COLOR_COORDINATE:
            obj_map['colorCoordinate']['hexValue'] = str(self.get_color_coordinate())
        try:
            super(ColorCoordinateRecord, self)._update_object_map(obj_map)
        except AttributeError:
            pass


class ColorCoordinateFormRecord(osid_records.OsidRecord):
    """form to create / update the color of an object"""

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(ColorCoordinateFormRecord, self).__init__()

    def _init_map(self):
        """stub"""
        self.my_osid_object_form._my_map['colorCoordinate'] = \
            dict(self._color_coordinate_metadata['default_coordinate_values'][0])

    def _init_metadata(self):
        """stub"""
        self._min_decimal_value = None
        self._max_decimal_value = None
        self._color_coordinate_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'color_coordinate'),
            'element_label': 'Color Coordinate',
            'instructions': 'enter a color coordinate',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_coordinate_values': [{}],
            'syntax': 'COORDINATE',
            'coordinate_set': []
        }

    def get_color_coordinate_metadata(self):
        """stub"""
        return Metadata(**self._color_coordinate_metadata)

    def set_color_coordinate(self, coordinate=None):
        """stub"""
        if coordinate is None:
            raise NullArgument()
        if self.get_color_coordinate_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(coordinate, RGBColorCoordinate):
            raise InvalidArgument('coordinate must be instance of RGBColorCoordinate')
        self.my_osid_object_form._my_map['colorCoordinate']['values'] = \
            coordinate.get_values()
        self.my_osid_object_form._my_map['colorCoordinate']['uncertaintyPlus'] = \
            coordinate.get_uncertainty_plus()
        self.my_osid_object_form._my_map['colorCoordinate']['uncertaintyMinus'] = \
            coordinate.get_uncertainty_minus()

    def clear_color_coordinate(self):
        """stub"""
        if (self.get_color_coordinate_metadata().is_read_only() or
                self.get_color_coordinate_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['colorCoordinate'] = \
            dict(self.get_color_coordinate_metadata().get_default_coordinate_values()[0])

    color_coordinate = property(fset=set_color_coordinate, fdel=clear_color_coordinate)


class TemporalFormRecord(osid_records.OsidRecord):
    """This form is used to create and update temporals."""
    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(TemporalFormRecord, self).__init__()

    def _init_metadata(self, **kwargs):
        # pylint: disable=attribute-defined-outside-init
        # this method is called from descendent __init__
        self._start_date_metadata = {
            'element_id': Id(authority=self.my_osid_object_form._authority,
                             namespace=self.my_osid_object_form._namespace,
                             identifier='start_date')}
        self._start_date_metadata.update(mdata_conf.START_DATE)
        self._start_date_metadata.update({
            'default_date_time_values': [datetime.datetime.utcnow()],
            'required': False
        })
        self._end_date_metadata = {
            'element_id': Id(authority=self.my_osid_object_form._authority,
                             namespace=self.my_osid_object_form._namespace,
                             identifier='end_date')}
        self._end_date_metadata.update(mdata_conf.END_DATE)
        self._end_date_metadata.update({'required': False})
        try:
            super(TemporalFormRecord, self)._init_metadata()
        except AttributeError:
            pass

    def _init_map(self):
        # pylint: disable=attribute-defined-outside-init
        # this method is called from descendent __init__
        default_start_date = self._start_date_metadata['default_date_time_values'][0]
        self.my_osid_object_form._my_map['startDate'] = DateTime(year=default_start_date.year,
                                                                 month=default_start_date.month,
                                                                 day=default_start_date.day,
                                                                 hour=default_start_date.hour,
                                                                 minute=default_start_date.minute,
                                                                 second=default_start_date.second,
                                                                 microsecond=default_start_date.microsecond)
        self.my_osid_object_form._my_map['endDate'] = DateTime(**self._end_date_metadata['default_date_time_values'][0])
        try:
            super(TemporalFormRecord, self)._init_map()
        except AttributeError:
            pass

    def get_start_date_metadata(self):
        """Gets the metadata for a start date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._start_date_metadata)
        metadata.update({'existing_date_time_values': self.my_osid_object_form._my_map['startDate']})
        return Metadata(**metadata)

    start_date_metadata = property(fget=get_start_date_metadata)

    @utilities.arguments_not_none
    def set_start_date(self, date):
        """Sets the start date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if date is None:
            raise NullArgument('date cannot be None')
        if self.get_start_date_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_date_time(date, self.get_start_date_metadata()):
            raise InvalidArgument('date must be instance of DateTime')
        self.my_osid_object_form._my_map['startDate'] = date

    def clear_start_date(self):
        """Clears the start date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if (self.get_start_date_metadata().is_read_only() or
                self.get_start_date_metadata().is_required()):
            raise NoAccess()
        default_start_date = self._start_date_metadata['default_date_time_values'][0]
        self.my_osid_object_form._my_map['startDate'] = DateTime(year=default_start_date.year,
                                                                 month=default_start_date.month,
                                                                 day=default_start_date.day,
                                                                 hour=default_start_date.hour,
                                                                 minute=default_start_date.minute,
                                                                 second=default_start_date.second,
                                                                 microsecond=default_start_date.microsecond)

    start_date = property(fset=set_start_date, fdel=clear_start_date)

    def get_end_date_metadata(self):
        """Gets the metadata for an end date.

        return: (osid.Metadata) - metadata for the date
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._end_date_metadata)
        metadata.update({'existing_date_time_values': self.my_osid_object_form._my_map['endDate']})
        return Metadata(**metadata)

    end_date_metadata = property(fget=get_end_date_metadata)

    @utilities.arguments_not_none
    def set_end_date(self, date):
        """Sets the end date.

        arg:    date (osid.calendaring.DateTime): the new date
        raise:  InvalidArgument - ``date`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if date is None:
            raise NullArgument('date cannot be None')
        if self.get_end_date_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_date_time(date, self.get_end_date_metadata()):
            raise InvalidArgument('date must be instance of DateTime')
        self.my_osid_object_form._my_map['endDate'] = date

    def clear_end_date(self):
        """Clears the end date.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if (self.get_end_date_metadata().is_read_only() or
                self.get_end_date_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['endDate'] = \
            DateTime(**self._end_date_metadata['default_date_time_values'][0])

    end_date = property(fset=set_end_date, fdel=clear_end_date)


class TemporalRecord(ObjectInitRecord):
    """``Temporal`` is used to indicate the object endures for a period of time."""

    def is_effective(self):
        """Tests if the current date is within the start end end dates inclusive.

        return: (boolean) - ``true`` if this is effective, ``false``
                otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        now = DateTime.utcnow()
        return self.get_start_date() <= now <= self.get_end_date()

    def get_start_date(self):
        """Gets the start date.

        return: (osid.calendaring.DateTime) - the start date
        *compliance: mandatory -- This method must be implemented.*

        """
        sdate = self.my_osid_object._my_map['startDate']
        return DateTime(
            sdate.year,
            sdate.month,
            sdate.day,
            sdate.hour,
            sdate.minute,
            sdate.second,
            sdate.microsecond)

    start_date = property(fget=get_start_date)

    def get_end_date(self):
        """Gets the end date.

        return: (osid.calendaring.DateTime) - the end date
        *compliance: mandatory -- This method must be implemented.*

        """
        edate = self.my_osid_object._my_map['endDate']
        return DateTime(
            edate.year,
            edate.month,
            edate.day,
            edate.hour,
            edate.minute,
            edate.second,
            edate.microsecond)

    end_date = property(fget=get_end_date)


class SourceableFormRecord(osid_records.OsidRecord):
    """this form is used to manage providerId
    Copied from json.osid.objects.OsidSourceableForm
    """

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(SourceableFormRecord, self).__init__()

    def _init_metadata(self, **kwargs):
        self._provider_metadata = {
            'element_id': Id(authority=self.my_osid_object_form._authority,
                             namespace=self.my_osid_object_form._namespace,
                             identifier='provider')}
        self._provider_metadata.update(mdata_conf.PROVIDER)
        self._provider_default = str(self._provider_metadata['default_id_values'][0])

        self._branding_metadata = {
            'element_id': Id(authority=self.my_osid_object_form._authority,
                             namespace=self.my_osid_object_form._namespace,
                             identifier='branding')}
        self._branding_metadata.update(mdata_conf.BRANDING)
        self._branding_default = list(self._branding_metadata['default_id_values'])

        self._license_metadata = {
            'element_id': Id(authority=self.my_osid_object_form._authority,
                             namespace=self.my_osid_object_form._namespace,
                             identifier='license')}
        self._license_metadata.update(mdata_conf.LICENSE)
        self._license_default = dict(self._license_metadata['default_string_values'][0])

    def _init_map(self, **kwargs):
        if 'effective_agent_id' in kwargs:
            try:
                mgr = self.my_osid_object_form._get_provider_manager('RESOURCE', local=True)
                agent_session = mgr.get_resource_agent_session()
                agent_session.use_federated_bin_view()
                resource_idstr = str(agent_session.get_resource_id_by_agent(kwargs['effective_agent_id']))
            except (OperationFailed,
                    Unsupported,
                    Unimplemented,
                    NotFound):
                resource_idstr = self._provider_default
            self.my_osid_object_form._my_map['providerId'] = resource_idstr
        else:
            self.my_osid_object_form._my_map['providerId'] = self._provider_default
        self.my_osid_object_form._my_map['brandingIds'] = self._branding_default
        self.my_osid_object_form._my_map['license'] = self._license_default

    def get_provider_metadata(self):
        """Gets the metadata for a provider.

        return: (osid.Metadata) - metadata for the provider
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._provider_metadata)
        metadata.update({'existing_id_values': self.my_osid_object_form._my_map['providerId']})
        return Metadata(**metadata)

    provider_metadata = property(fget=get_provider_metadata)

    @utilities.arguments_not_none
    def set_provider(self, provider_id):
        """Sets a provider.

        arg:    provider_id (osid.id.Id): the new provider
        raise:  InvalidArgument - ``provider_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``provider_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if provider_id is None:
            raise NullArgument('provider_id cannot be None')
        if self.get_provider_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_id(provider_id):
            raise InvalidArgument('provider_id must be instance of Id')
        self.my_osid_object_form._my_map['providerId'] = str(provider_id)

    def clear_provider(self):
        """Removes the provider.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if (self.get_provider_metadata().is_read_only() or
                self.get_provider_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['providerId'] = self._provider_default

    provider = property(fset=set_provider, fdel=clear_provider)

    def get_branding_metadata(self):
        """Gets the metadata for the asset branding.

        return: (osid.Metadata) - metadata for the asset branding.
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._branding_metadata)
        metadata.update({'existing_id_values': self.my_osid_object_form._my_map['brandingIds']})
        return Metadata(**metadata)

    branding_metadata = property(fget=get_branding_metadata)

    @utilities.arguments_not_none
    def set_branding(self, asset_ids):
        """Sets the branding.

        arg:    asset_ids (osid.id.Id[]): the new assets
        raise:  InvalidArgument - ``asset_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``asset_ids`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if asset_ids is None:
            raise NullArgument('asset_ids cannot be None')
        if self.get_branding_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(asset_ids, list):
            raise InvalidArgument('asset_ids must be a list')
        if not self.my_osid_object_form._is_valid_input(asset_ids,
                                                        self.get_branding_metadata(),
                                                        array=True):
            raise InvalidArgument()
        branding_ids = []
        for asset_id in asset_ids:
            branding_ids.append(str(asset_id))
        self.my_osid_object_form._my_map['brandingIds'] = branding_ids

    def clear_branding(self):
        """Removes the branding.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if (self.get_branding_metadata().is_read_only() or
                self.get_branding_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['brandingIds'] = self._branding_default

    branding = property(fset=set_branding, fdel=clear_branding)

    def get_license_metadata(self):
        """Gets the metadata for the license.

        return: (osid.Metadata) - metadata for the license
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._license_metadata)
        metadata.update({'existing_string_values': self.my_osid_object_form._my_map['license']})
        return Metadata(**metadata)

    license_metadata = property(fget=get_license_metadata)

    @utilities.arguments_not_none
    def set_license(self, license_):
        """Sets the license.

        arg:    license (string): the new license
        raise:  InvalidArgument - ``license`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``license`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if license_ is None:
            raise NullArgument('license cannot be None')
        if not utilities.is_string(license_):
            raise InvalidArgument('license must be a string')
        if self.get_license_metadata().is_read_only():
            raise NoAccess()
        if not self.my_osid_object_form._is_valid_string(license_, self.get_license_metadata()):
            raise InvalidArgument()
        self.my_osid_object_form._my_map['license']['text'] = license_

    def clear_license(self):
        """Removes the license.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if (self.get_license_metadata().is_read_only() or
                self.get_license_metadata().is_required()):
            raise NoAccess()
        self.my_osid_object_form._my_map['license'] = dict(self._license_default)

    license_ = property(fset=set_license, fdel=clear_license)


class SourceableRecord(ObjectInitRecord):
    """to retrieve sourceable objects
    copied from json.osid.markers.Sourceable"""

    def get_provider_id(self):
        """Gets the ``Id`` of the provider.

        return: (osid.id.Id) - the provider ``Id``
        *compliance: mandatory -- This method must be implemented.*

        """
        if ('providerId' not in self.my_osid_object._my_map or
                not self.my_osid_object._my_map['providerId']):
            raise IllegalState('this sourceable object has no provider set')
        return Id(self.my_osid_object._my_map['providerId'])

    provider_id = property(fget=get_provider_id)

    def get_provider(self):
        """Gets the ``Resource`` representing the provider.

        return: (osid.resource.Resource) - the provider
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        if ('providerId' not in self.my_osid_object._my_map or
                not self.my_osid_object._my_map['providerId']):
            raise IllegalState('this sourceable object has no provider set')
        mgr = self.my_osid_object._get_provider_manager('RESOURCE')
        lookup_session = mgr.get_resource_lookup_session()
        lookup_session.use_federated_bin_view()
        return lookup_session.get_resource(self.get_provider_id())

    provider = property(fget=get_provider)

    def get_branding_ids(self):
        """Gets the branding asset ``Ids``.

        return: (osid.id.IdList) - a list of asset ``Ids``
        *compliance: mandatory -- This method must be implemented.*

        """
        if 'brandingIds' not in self.my_osid_object._my_map:
            return IdList([])
        id_list = []
        for idstr in self.my_osid_object._my_map['brandingIds']:
            id_list.append(Id(idstr))
        return IdList(id_list)

    branding_ids = property(fget=get_branding_ids)

    def get_branding(self):
        """Gets a branding, such as an image or logo, expressed using the ``Asset`` interface.

        return: (osid.repository.AssetList) - a list of assets
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        mgr = self.my_osid_object._get_provider_manager('REPOSITORY')
        lookup_session = mgr.get_asset_lookup_session()
        lookup_session.use_federated_repository_view()
        return lookup_session.get_assets_by_ids(self.get_branding_ids())

    branding = property(fget=get_branding)

    def get_license(self):
        """Gets the terms of usage.

        An empty license means the terms are unknown.

        return: (osid.locale.DisplayText) - the license
        *compliance: mandatory -- This method must be implemented.*

        """
        if 'license' in self.my_osid_object._my_map:
            license_text = self.my_osid_object._my_map['license']
            return DisplayText(display_text_map=license_text)
        return DisplayText(text='',
                           language_type=DEFAULT_LANGUAGE_TYPE,
                           format_type=DEFAULT_FORMAT_TYPE,
                           script_type=DEFAULT_SCRIPT_TYPE)

    license_ = property(fget=get_license)


class MultiLanguageFormRecord(MultiLanguageUtils,
                              osid_records.OsidRecord):
    """this form is used to manage multiple languages in the
    displayName and description fields
    """

    def __init__(self, osid_object_form=None):
        if osid_object_form is not None:
            self.my_osid_object_form = osid_object_form
        self._init_metadata()
        if not self.my_osid_object_form.is_for_update():
            self._init_map()
        super(MultiLanguageFormRecord, self).__init__()

    def _init_metadata(self, **kwargs):
        self._display_names_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'display_names'),
            'element_label': 'Display Names',
            'instructions': 'Enter as many display names as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }
        self._descriptions_metadata = {
            'element_id': Id(self.my_osid_object_form._authority,
                             self.my_osid_object_form._namespace,
                             'descriptions'),
            'element_label': 'Descriptions',
            'instructions': 'Enter as many descriptions as you wish',
            'required': True,
            'read_only': False,
            'linked': False,
            'array': True,
            'default_object_values': [[]],
            'syntax': 'OBJECT',
            'object_set': []
        }

    def _init_map(self, **kwargs):
        self.my_osid_object_form._my_map['displayNames'] = self._display_names_metadata['default_object_values'][0]
        self.my_osid_object_form._my_map['descriptions'] = self._descriptions_metadata['default_object_values'][0]

    def get_display_names_metadata(self):
        """Gets the metadata for all display_names.

        return: (osid.Metadata) - metadata for the display_names
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._display_names_metadata)
        metadata.update({'existing_string_values': [t['text'] for t in self.my_osid_object_form._my_map['displayNames']]})
        return Metadata(**metadata)

    display_names_metadata = property(fget=get_display_names_metadata)

    def get_descriptions_metadata(self):
        """Gets the metadata for all descriptions.

        return: (osid.Metadata) - metadata for the descriptions
        *compliance: mandatory -- This method must be implemented.*

        """
        metadata = dict(self._descriptions_metadata)
        metadata.update({'existing_string_values': [t['text'] for t in self.my_osid_object_form._my_map['descriptions']]})
        return Metadata(**metadata)

    descriptions_metadata = property(fget=get_descriptions_metadata)

    @utilities.arguments_not_none
    def add_display_name(self, display_name):
        """Adds a display_name.

        arg:    display_name (displayText): the new display name
        raise:  InvalidArgument - ``display_name`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``display_name`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_display_names_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(display_name, DisplayText):
            raise InvalidArgument('display_name must be instance of DisplayText')
        self.add_or_replace_value('displayNames', display_name)

    def clear_display_names(self):
        """Removes all display_names.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_display_names_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['displayNames'] = []

    @utilities.arguments_not_none
    def remove_display_name_by_language(self, language_type):
        """Removes the specified display_name.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_display_names_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(language_type, Type):
            raise InvalidArgument('language_type must be instance of Type')
        self.my_osid_object_form._my_map['displayNames'] = [t
                                                            for t in self.my_osid_object_form._my_map['displayNames']
                                                            if t['languageTypeId'] != str(language_type)]

    @utilities.arguments_not_none
    def edit_display_name(self, new_display_name):
        if self.get_display_names_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_display_name, DisplayText):
            raise InvalidArgument()

        display_names = [d
                         for d in self.my_osid_object_form._my_map['displayNames']
                         if d['languageTypeId'] == str(new_display_name.language_type)]
        if len(display_names) == 0:
            raise InvalidArgument('That language type display name doesn\'t exist yet. Use add_display_name().')

        self.add_or_replace_value('displayNames', new_display_name)

    @utilities.arguments_not_none
    def add_description(self, description):
        """Adds a description.

        arg:    description (displayText): the new description
        raise:  InvalidArgument - ``description`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        raise:  NullArgument - ``description`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_descriptions_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(description, DisplayText):
            raise InvalidArgument('description must be instance of DisplayText')
        self.add_or_replace_value('descriptions', description)

    def clear_descriptions(self):
        """Removes all descriptions.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_descriptions_metadata().is_read_only():
            raise NoAccess()
        self.my_osid_object_form._my_map['descriptions'] = []

    @utilities.arguments_not_none
    def remove_description_by_language(self, language_type):
        """Removes the specified description.

        raise:  NoAccess - ``Metadata.isRequired()`` is ``true`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        """
        if self.get_descriptions_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(language_type, Type):
            raise InvalidArgument('language_type must be instance of Type')
        self.my_osid_object_form._my_map['descriptions'] = [t
                                                            for t in self.my_osid_object_form._my_map['descriptions']
                                                            if t['languageTypeId'] != str(language_type)]

    @utilities.arguments_not_none
    def edit_description(self, new_description):
        if self.get_descriptions_metadata().is_read_only():
            raise NoAccess()
        if not isinstance(new_description, DisplayText):
            raise InvalidArgument('new description is not a DisplayText object')

        descriptions = [d
                        for d in self.my_osid_object_form._my_map['descriptions']
                        if d['languageTypeId'] == str(new_description.language_type)]
        if len(descriptions) == 0:
            raise InvalidArgument('That language type description doesn\'t exist yet. Use add_description().')

        self.add_or_replace_value('descriptions', new_description)


class MultiLanguageRecord(MultiLanguageUtils,
                          ObjectInitRecord):
    """to retrieve objects with multiple languages in displayName and description"""
    def get_display_name(self):
        """Uses the locale info in the osid object proxy to grab a display name,
        falling back on English as default, then first one available if no English.

        return: (displayText) - the displayText for the given display name
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_matching_language_value('displayNames')

    display_name = property(fget=get_display_name)

    def get_description(self):
        """Uses the locale info in the osid object proxy to grab a description,
        falling back on English as default, then first one available if no English.

        return: (displayText) - the displayText for the given description
        *compliance: mandatory -- This method must be implemented.*

        """
        return self.get_matching_language_value('descriptions')

    description = property(fget=get_description)


class MultiLanguageQueryRecord(QueryInitRecord):
    # do **NOT** override match_display_name and match_description
    # otherwise queries will break for non-multi-language objects

    def match_display_names(self, value, match):
        """stub"""
        if value is None:
            raise NullArgument('value must not be None')
        if not utilities.is_string(value):
            raise InvalidArgument('value must be a string')
        if match is None:
            raise NullArgument('match must not be None')
        if not isinstance(match, bool):
            raise InvalidArgument('match must be a bool')
        self._my_osid_query._add_match('displayNames.text', str(value).lower(), match)

    def clear_match_display_names(self):
        """stub"""
        self._my_osid_query._clear_terms('displayNames.text')

    def match_descriptions(self, value, match):
        """stub"""
        if value is None:
            raise NullArgument('value must not be None')
        if not utilities.is_string(value):
            raise InvalidArgument('value must be a string')
        if match is None:
            raise NullArgument('match must not be None')
        if not isinstance(match, bool):
            raise InvalidArgument('match must be a bool')
        self._my_osid_query._add_match('descriptions.text', str(value).lower(), match)

    def clear_match_descriptions(self):
        """stub"""
        self._my_osid_query._clear_terms('descriptions.text')
