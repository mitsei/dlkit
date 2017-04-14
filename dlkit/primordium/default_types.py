"""
Gets types.

Probably needs a complete re-design, as functions only.

"""
# -*- coding: utf-8 -*-
from dlkit.abstract_osid.osid.errors import NotFound
from .locale.display_text_default_types import LANGUAGETYPE, SCRIPTTYPE, FORMATTYPE


class Language(object):
    """Language type default"""

    def get_type_data(self, name):
        """gets language type default data dictionary"""
        if name == 'DEFAULT':
            return LANGUAGETYPE
        else:
            raise NotFound(name + 'Language Type')


class Script(object):
    """Language type default"""

    def get_type_data(self, name):
        """gets script type default data dictionary"""
        if name == 'DEFAULT':
            return SCRIPTTYPE
        else:
            raise NotFound(name + 'Script Type')


class Format(object):
    """Language type default"""

    def get_type_data(self, name):
        """gets format type default data dictionary"""
        if name == 'DEFAULT':
            return FORMATTYPE
        else:
            raise NotFound(name + 'Format Type')
