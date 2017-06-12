"""Mongo osid profile elements for authentication service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by authentication.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo authentication'

DESCRIPTION = 'MongoDB based authentication implementation'

VERSIONCOMPONENTS = [0, 1, 303]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    # 'supports_authentication_acquisition',
    # 'supports_authentication_validation',
    'supports_agent_lookup',
    # 'supports_agent_query',
    # 'supports_agent_search',
    # 'supports_agent_admin',
    # 'supports_agent_notification',
    # 'supports_agent_agency',
    # 'supports_agent_agency_assignment',
    # 'supports_agent_smart_agency',
    # 'supports_agency_lookup',
    # 'supports_agency_query',
    # 'supports_agency_search',
    # 'supports_agency_admin',
    # 'supports_agency_notification',
    # 'supports_agency_hierarchy',
    # 'supports_agency_hierarchy_design',
    # 'supports_authentication_keys',
    # 'supports_authentication_process',
]
