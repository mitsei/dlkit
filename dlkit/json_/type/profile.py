"""Mongo osid profile elements for type service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by type.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo type'

DESCRIPTION = 'MongoDB based type implementation'

VERSIONCOMPONENTS = [0, 1, 40]

RELEASEDATE = "2018-03-07"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_type_lookup',
    # 'supports_type_admin',
]
