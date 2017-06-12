"""Mongo osid profile elements for repository service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by repository.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo repository'

DESCRIPTION = 'MongoDB based repository implementation'

VERSIONCOMPONENTS = [0, 1, 303]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_asset_lookup',
    'supports_asset_query',
    'supports_asset_search',
    'supports_asset_admin',
    'supports_asset_notification',
    'supports_asset_repository',
    'supports_asset_repository_assignment',
    # 'supports_asset_smart_repository',
    # 'supports_asset_temporal',
    # 'supports_asset_temporal_assignment',
    # 'supports_asset_spatial',
    # 'supports_asset_spatial_assignment',
    'supports_asset_composition',
    'supports_asset_composition_design',
    'supports_composition_lookup',
    'supports_composition_query',
    'supports_composition_search',
    'supports_composition_admin',
    # 'supports_composition_notification',
    'supports_composition_repository',
    'supports_composition_repository_assignment',
    # 'supports_composition_smart_repository',
    'supports_repository_lookup',
    'supports_repository_query',
    # 'supports_repository_search',
    'supports_repository_admin',
    # 'supports_repository_notification',
    'supports_repository_hierarchy',
    'supports_repository_hierarchy_design',
    # 'supports_repository_batch',
    # 'supports_repository_rules',
]
