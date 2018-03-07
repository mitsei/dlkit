"""Mongo osid profile elements for logging service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by logging.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo logging'

DESCRIPTION = 'MongoDB based logging implementation'

VERSIONCOMPONENTS = [0, 1, 40]

RELEASEDATE = "2018-03-07"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_logging',
    'supports_log_entry_lookup',
    'supports_log_entry_query',
    # 'supports_log_entry_search',
    # 'supports_log_entry_notification',
    'supports_log_entry_log',
    'supports_log_entry_log_assignment',
    # 'supports_log_entry_smart_log',
    'supports_log_lookup',
    # 'supports_log_query',
    # 'supports_log_search',
    'supports_log_admin',
    # 'supports_log_notification',
    'supports_log_hierarchy',
    'supports_log_hierarchy_design',
    # 'supports_logging_batch',
    'supports_log_entry_admin',
]
