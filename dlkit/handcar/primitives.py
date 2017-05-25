# -*- coding: utf-8 -*-

#
# This module contains primitives and primitive objects required by the
# MIT Core Concept Catalog (MC3) Handcar learning service implementation
import codecs

from . import profile
from . import settings
from .osid import markers
from ..abstract_osid.id.primitives import Id as abc_id
from ..abstract_osid.type.primitives import Type as abc_type
from ..abstract_osid.locale.primitives import DisplayText as abc_displaytext
from .osid.osid_errors import NullArgument, NotFound, OperationFailed
# from .abstract_osid.abc_installation.primitives import Version as abc_version


class Id(abc_id, markers.OsidPrimitive):

    def __init__(self, idstr=None, authority=None, namespace=None, identifier=None):
        self._idstr = idstr
        if idstr is not None:
            idstr = self._unescape(idstr)
            self._authority = self._unescape(idstr.split('@')[-1])
            self._namespace = self._unescape(idstr.split(':')[0])
            self._identifier = self._unescape(idstr.split('@')[0].split(':')[-1])
        elif authority is not None and namespace is not None and identifier is not None:
            self._authority = authority
            self._namespace = namespace
            self._identifier = identifier
        else:
            raise NullArgument()

    def __str__(self):
        if self._idstr is not None:
            return self._idstr
        else:
            return super(Id, self).__str__()

    def get_authority(self):
        return self._authority

    def get_identifier_namespace(self):
        return self._namespace

    def get_identifier(self):
        return self._identifier

    authority = property(get_authority)
    identifier_namespace = property(get_identifier_namespace)
    namespace = property(get_identifier_namespace)
    identifier = property(get_identifier)


class Type(abc_type, markers.OsidPrimitive):

    def __init__(self, type_map):
        self._my_map = type_map

    def get_display_name(self):
        return DisplayText(self._my_map['displayName'])

    def get_display_label(self):
        return DisplayText(self._my_map['displayLabel'])

    def get_description(self):
        return DisplayText(self._my_map['description'])

    def get_domain(self):
        return DisplayText(self._my_map['domain'])

    def get_authority(self):
        return self._my_map['authority']

    def get_identifier_namespace(self):
        return self._my_map['identifierNamespace']

    def get_identifier(self):
        return self._my_map['identifier']

    def get_object_map(self):
        return self._my_map

    display_name = property(get_display_name)
    display_label = property(get_display_label)
    description = property(get_description)
    domain = property(get_domain)
    authority = property(get_authority)
    identifier_namespace = property(get_identifier_namespace)
    namespace = property(get_identifier_namespace)
    identifier = property(get_identifier)
    object_map = property(get_object_map)


class DisplayText(abc_displaytext, markers.OsidPrimitive):

    def __init__(self, display_text_map):
        self._my_map = display_text_map

    def _get_type_map(self, type_identifier):
        try:
            # Python 2
            import urllib2
            urlopen = urllib2.urlopen
            urlerrors = urllib2
        except ImportError:
            # Python 3
            import urllib.request
            import urllib.error
            urlopen = urllib.request.urlopen
            urlerrors = urllib.error

        import json
        from . import settings
        try:
            # url = urllib2.urlopen(settings.HANDCAR +
            #                       '/services/learning/types/' +
            #                       type_identifier).read()
            response = urlopen(settings.HANDCAR +
                               '/services/learning/types')
        except urlerrors.HTTPError:
            raise NotFound('type_identifier not found or bad handcar base URL in settings.py')
        try:
            reader = codecs.getreader('utf8')
            matching_types = [t for t in json.load(reader(response)) if t['id'] == type_identifier]
            if len(matching_types) == 0:
                raise NotFound('type_identifier not found')
            return matching_types[0]
        except Exception:
            raise  # OperationFailed

    def get_language_type(self):
        return Type(self._get_type_map(self._my_map['languageTypeId']))

    def get_script_type(self):
        return Type(self._get_type_map(self._my_map['scriptTypeId']))

    def get_format_type(self):
        return Type(self._get_type_map(self._my_map['formatTypeId']))

    def get_text(self):
        try:
            return self._my_map['text']
        except:
            return ''

    language_type = property(get_language_type)
    script_type = property(get_script_type)
    format_type = property(get_format_type)
    text = property(get_text)


"""
class Version(abc_version, markers.OsidPrimitive):

    def __init__(self, version_map):
        my_vesion

    def get_components(self):
        return self._components

    def get_scheme(self):
        return self._scheme
"""
