"""Mongo osid profile elements for authorization service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by authorization.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo authorization'

DESCRIPTION = 'MongoDB based authorization implementation'

VERSIONCOMPONENTS = [0, 1, 39]

RELEASEDATE = "2018-02-27"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_authorization',
    'supports_authorization_lookup',
    'supports_authorization_query',
    # 'supports_authorization_search',
    'supports_authorization_admin',
    # 'supports_authorization_notification',
    'supports_authorization_vault',
    'supports_authorization_vault_assignment',
    # 'supports_authorization_smart_vault',
    # 'supports_function_lookup',
    # 'supports_function_query',
    # 'supports_function_search',
    # 'supports_function_admin',
    # 'supports_function_notification',
    # 'supports_function_vault',
    # 'supports_function_vault_assignment',
    # 'supports_function_smart_vault',
    # 'supports_qualifier_lookup',
    # 'supports_qualifier_query',
    # 'supports_qualifier_search',
    # 'supports_qualifier_admin',
    # 'supports_qualifier_notification',
    # 'supports_qualifier_hierarchy',
    # 'supports_qualifier_hierarchy_design',
    # 'supports_qualifier_vault',
    # 'supports_qualifier_vault_assignment',
    # 'supports_qualifier_smart_vault',
    'supports_vault_lookup',
    'supports_vault_query',
    # 'supports_vault_search',
    'supports_vault_admin',
    # 'supports_vault_notification',
    'supports_vault_hierarchy',
    'supports_vault_hierarchy_design',
    # 'supports_authorization_batch',
    # 'supports_authorization_rules',
]
