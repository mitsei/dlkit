"""Mongo osid profile elements for locale service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by locale.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo locale'

DESCRIPTION = 'MongoDB based locale implementation'

VERSIONCOMPONENTS = [0, 1, 303]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    # 'supports_translation',
    # 'supports_translation_admin',
    # 'supports_numeric_formatting',
    # 'supports_calendar_formatting',
    # 'supports_currency_formatting',
    # 'supports_coordinate_formatting',
    # 'supports_unit_conversion',
    # 'supports_currency_conversion',
    # 'supports_calendar_conversion',
    # 'supports_coordinate_conversion',
    # 'supports_spatial_unit_conversion',
    # 'supports_format_conversion',
    # 'supports_calendar_info',
]
