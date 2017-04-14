# -*- coding: utf-8 -*-
"""
Generic implementions of osid.locale primitives.

Can be used by implementations and consumer applications alike.

"""
# pylint: disable=too-many-arguments
#    Allowing for multiple initialization profiles

from dlkit.abstract_osid.locale.primitives import DisplayText as abc_displaytext
from dlkit.abstract_osid.osid.errors import NullArgument, InvalidArgument, NotFound
from ..osid.primitives import OsidPrimitive
from ..id.primitives import Id
from .types import language as language_types
from .types import script as script_types
from .types import format as format_types


class DisplayText(abc_displaytext, OsidPrimitive):
    """Text to be displayed."""

    def __init__(self,
                 display_text_map=None,
                 text=None,
                 language_type=None,
                 script_type=None,
                 format_type=None):
        if display_text_map is not None:
            if not isinstance(display_text_map, dict):
                raise InvalidArgument('display_text_map must be a dict')
            self._unfold_map(display_text_map)
        elif (text is not None and language_type is not None and
              script_type is not None and format_type is not None):
            self._text = text
            self._language_type = language_type
            self._script_type = script_type
            self._format_type = format_type
        else:
            raise NullArgument()

    def _unfold_map(self, display_text_map):
        """Parses a display text dictionary map."""
        from ..type.primitives import Type
        lt_identifier = Id(display_text_map['languageTypeId']).get_identifier()
        st_identifier = Id(display_text_map['scriptTypeId']).get_identifier()
        ft_identifier = Id(display_text_map['formatTypeId']).get_identifier()
        try:
            self._language_type = Type(**language_types.get_type_data(lt_identifier))
        except AttributeError:
            raise NotFound('Language Type: ' + lt_identifier)  # or move on to another source
        try:
            self._script_type = Type(**script_types.get_type_data(st_identifier))
        except AttributeError:
            raise NotFound('Script Type: ' + st_identifier)  # or move on to another source
        try:
            self._format_type = Type(**format_types.get_type_data(ft_identifier))
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
