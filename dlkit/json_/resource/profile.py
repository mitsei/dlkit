"""Mongo osid profile elements for resource service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by resource.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo resource'

DESCRIPTION = 'MongoDB based resource implementation'

VERSIONCOMPONENTS = [0, 1, 39]

RELEASEDATE = "2018-02-27"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_resource_lookup',
    'supports_resource_query',
    'supports_resource_search',
    'supports_resource_admin',
    'supports_resource_notification',
    'supports_resource_bin',
    'supports_resource_bin_assignment',
    # 'supports_resource_smart_bin',
    # 'supports_membership',
    # 'supports_group',
    # 'supports_group_assignment',
    # 'supports_group_notification',
    # 'supports_group_hierarchy',
    'supports_resource_agent',
    'supports_resource_agent_assignment',
    # 'supports_resource_relationship_lookup',
    # 'supports_resource_relationship_query',
    # 'supports_resource_relationship_search',
    # 'supports_resource_relationship_admin',
    # 'supports_resource_relationship_notification',
    # 'supports_resource_relationship_bin',
    # 'supports_resource_relationship_bin_assignment',
    # 'supports_resource_relationship_smart_bin',
    'supports_bin_lookup',
    'supports_bin_query',
    # 'supports_bin_search',
    'supports_bin_admin',
    # 'supports_bin_notification',
    'supports_bin_hierarchy',
    'supports_bin_hierarchy_design',
    # 'supports_resource_batch',
    # 'supports_resource_demographic',
]
