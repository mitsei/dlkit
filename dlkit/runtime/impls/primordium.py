# -*- coding: utf-8 -*-

# This module contains primitives required by the MIT Core Concept
# Catalog (MC3) Handcar learning service implementation

from dlkit.abstract_osid.id.primitives import Id as abc_id
from dlkit.abstract_osid.osid import markers as abc_osid_markers
from dlkit.abstract_osid.type.primitives import Type as abc_type
from dlkit.abstract_osid.locale.primitives import DisplayText as abc_displaytext
from .osid.osid_errors import NullArgument, NotFound, OperationFailed
from . import types

# from .abstract_osid.abc_installation.primitives import Version as abc_version


class OsidPrimitive(abc_osid_markers.OsidPrimitive):
    """A marker interface for an interface that behaves like a language primitive.

    Primitive types, such as numbers and strings, do not encapsulate
    behaviors supplied by an OSID Provider. More complex primitives are
    expressed through interface definitions but are treated in a similar
    fashion as a language primitive. OSID Primitives supplied by an OSID
    Consumer must be consumable by any OSID Provider.

    """

    def _test_escape(self):
        print(self._unescape(self._escape("here:there@okapia.net")) == "here:there@okapia.net")
        print(self._unescape(self._escape("here:there/somewhere@okapia.net")) == "here:there/somewhere@okapia.net")
        print(self._unescape(self._escape("here:there%3asomewhere@okapia.net")) == "here:there%3asomewhere@okapia.net")
        print(self._unescape(self._escape("almost%3ahere:there%3asomewhere@okapia.net")) == "almost%3ahere:there%3asomewhere@okapia.net")
        print(self._unescape(self._escape("almost%3ahere:there%3asomewhere@okapia.net")) == "almost%3ahere:there%3asomewhere@okapia.net")
        print(self._unescape(self._escape("almost%3ahere:there%3asomewhere%40else@okapia.net")) == "almost%3ahere:there%3asomewhere%40else@okapia.net")
        print(self._unescape(self._escape("almost%3ahere:there%3asomewhere%40else@site%40okapia.net")) == "almost%3ahere:there%3asomewhere%40else@site%40okapia.net")
        print(self._unescape(self._escape("almost%3ahere:there%3asomewhere%40else@our%3asite%40okapia.net")) == "almost%3ahere:there%3asomewhere%40else@our%3asite%40okapia.net")
        print(self._unescape(self._escape("al!#$<>;^&*()_+|}{?//-=most%3ahere:there%3asome!#$<>;^&*()_+|}{?//-=where%40else@our%3asite%40ok!#$<>;^&*()_+|}{?//-=apia")) == "al!#$<>;^&*()_+|}{?//-=most%3ahere:there%3asome!#$<>;^&*()_+|}{?//-=where%40else@our%3asite%40ok!#$<>;^&*()_+|}{?//-=apia")


class Id(abc_id, OsidPrimitive):

    def __init__(self, idstr=None, authority=None, namespace=None, identifier=None, **kwargs):
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


class Type(abc_type, OsidPrimitive):

    def __init__(self,
                 identifier=None,
                 authority=None,
                 namespace=None,
                 display_name=None,
                 display_label=None,
                 description=None,
                 domain=None):
        if (authority is not None and namespace is not None and identifier is not None and
                display_name is not None and description is not None and domain is not None):
            self._authority = authority
            self._namespace = namespace
            self._identifier = identifier
            self._display_name = display_name
            self._display_label = display_label
            self._description = description
            self._domain = domain
        else:
            raise NullArgument()

    def get_display_name(self):
        return DisplayText(text=self._display_name,
                           language_type=Type(**types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**types.Format().get_type_data('DEFAULT')))

    def get_display_label(self):
        return DisplayText(text=self._display_label,
                           language_type=Type(**types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**types.Format().get_type_data('DEFAULT')))

    def get_description(self):
        return DisplayText(text=self._description,
                           language_type=Type(**types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**types.Format().get_type_data('DEFAULT')))

    def get_domain(self):
        return DisplayText(text=self._domain,
                           language_type=Type(**types.Language().get_type_data('DEFAULT')),
                           script_type=Type(**types.Script().get_type_data('DEFAULT')),
                           format_type=Type(**types.Format().get_type_data('DEFAULT')))

    def get_authority(self):
        return self._authority

    def get_identifier_namespace(self):
        return self._namespace

    def get_identifier(self):
        return self._identifier

    display_name = property(get_display_name)
    display_label = property(get_display_label)
    description = property(get_description)
    domain = property(get_domain)
    authority = property(get_authority)
    identifier_namespace = property(get_identifier_namespace)
    namespace = property(get_identifier_namespace)
    identifier = property(get_identifier)


class DisplayText(abc_displaytext, OsidPrimitive):

    def __init__(self, display_text_map=None, text=None, language_type=None, script_type=None, format_type=None):
        if display_text_map is not None:
            self._unfold_map(display_text_map)
        elif (text is not None and language_type is not None and
                script_type is not None and format_type is not None):
            self._text = text
            self._language_type = language_type
            self._script_type = script_type
            self._format_type = format_type
        else:
            raise NotFound()

    def _unfold_map(self, display_text_map):
        from .locale import types as locale_types
        lt_identifier = Id(display_text_map['languageTypeId']).get_identifier()
        st_identifier = Id(display_text_map['scriptTypeId']).get_identifier()
        ft_identifier = Id(display_text_map['formatTypeId']).get_identifier()
        try:
            self._language_type = Type(**locale_types.Language().get_type_data(lt_identifier))
        except AttributeError:
            raise NotFound('Language Type: ' + lt_identifier)  # or move on to another source
        try:
            self._script_type = Type(**locale_types.Script().get_type_data(st_identifier))
        except AttributeError:
            raise NotFound('Script Type: ' + st_identifier)  # or move on to another source
        try:
            self._format_type = Type(**locale_types.Format().get_type_data(ft_identifier))
        except AttributeError:
            raise NotFound('Format Type: ' + ft_identifier)  # or move on to another source
        self._text = display_text_map['text']

    def get_language_type(self):
        return self._language_type

    def get_script_type(self):
        return self._script_type

    def get_format_type(self):
        return self._format_type

    def get_text(self):
        return self._text

    language_type = property(get_language_type)
    script_type = property(get_script_type)
    format_type = property(get_format_type)
    text = property(get_text)


"""
class Version(abc_version, OsidPrimitive):

    def __init__(self, version_map):
        my_vesion

    def get_components(self):
        return self._components

    def get_scheme(self):
        return self._scheme
"""
