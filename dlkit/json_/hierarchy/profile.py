"""Mongo osid profile elements for hierarchy service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by hierarchy.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo hierarchy'

DESCRIPTION = 'MongoDB based hierarchy implementation'

VERSIONCOMPONENTS = [0, 1, 40]

RELEASEDATE = "2018-03-07"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_hierarchy_traversal',
    'supports_hierarchy_design',
    # 'supports_hierarchy_sequencing',
    # 'supports_hierarchy_structure_notification',
    'supports_hierarchy_lookup',
    # 'supports_hierarchy_query',
    # 'supports_hierarchy_search',
    'supports_hierarchy_admin',
    # 'supports_hierarchy_notification',
]
