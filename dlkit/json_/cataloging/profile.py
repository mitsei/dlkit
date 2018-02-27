"""Mongo osid profile elements for cataloging service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by cataloging.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo cataloging'

DESCRIPTION = 'MongoDB based cataloging implementation'

VERSIONCOMPONENTS = [0, 1, 39]

RELEASEDATE = "2018-02-27"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    # 'supports_catalog',
    # 'supports_catalog_assignment',
    # 'supports_catalog_entry_notification',
    'supports_catalog_lookup',
    'supports_catalog_query',
    # 'supports_catalog_search',
    'supports_catalog_admin',
    # 'supports_catalog_notification',
    'supports_catalog_hierarchy',
    'supports_catalog_hierarchy_design',
    # 'supports_cataloging_rules',
]
