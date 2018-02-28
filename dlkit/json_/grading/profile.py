"""Mongo osid profile elements for grading service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by grading.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo grading'

DESCRIPTION = 'MongoDB based grading implementation'

VERSIONCOMPONENTS = [0, 1, 39]

RELEASEDATE = "2018-02-27"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_grade_system_lookup',
    'supports_grade_system_query',
    # 'supports_grade_system_search',
    'supports_grade_system_admin',
    # 'supports_grade_system_notification',
    'supports_grade_system_gradebook',
    'supports_grade_system_gradebook_assignment',
    # 'supports_grade_system_smart_gradebook',
    'supports_grade_entry_lookup',
    'supports_grade_entry_query',
    # 'supports_grade_entry_search',
    'supports_grade_entry_admin',
    # 'supports_grade_entry_notification',
    'supports_gradebook_column_lookup',
    'supports_gradebook_column_query',
    # 'supports_gradebook_column_search',
    'supports_gradebook_column_admin',
    # 'supports_gradebook_column_notification',
    'supports_gradebook_column_gradebook',
    'supports_gradebook_column_gradebook_assignment',
    # 'supports_gradebook_column_smart_gradebook',
    'supports_gradebook_lookup',
    # 'supports_gradebook_query',
    # 'supports_gradebook_search',
    'supports_gradebook_admin',
    # 'supports_gradebook_notification',
    'supports_gradebook_hierarchy',
    'supports_gradebook_hierarchy_design',
    # 'supports_grading_batch',
    # 'supports_grading_calculation',
    # 'supports_grading_transform',
]
