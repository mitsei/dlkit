"""Mongo osid profile elements for relationship service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by relationship.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo relationship'

DESCRIPTION = 'MongoDB based relationship implementation'

VERSIONCOMPONENTS = [0, 1, 303]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_relationship_lookup',
    'supports_relationship_query',
    # 'supports_relationship_search',
    'supports_relationship_admin',
    # 'supports_relationship_notification',
    # 'supports_relationship_family',
    # 'supports_relationship_family_assignment',
    # 'supports_relationship_smart_family',
    'supports_family_lookup',
    # 'supports_family_query',
    # 'supports_family_search',
    'supports_family_admin',
    # 'supports_family_notification',
    'supports_family_hierarchy',
    'supports_family_hierarchy_design',
    # 'supports_relationship_batch',
    # 'supports_relationship_rules',
]
