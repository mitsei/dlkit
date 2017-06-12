"""Mongo osid profile elements for learning service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by learning.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo learning'

DESCRIPTION = 'MongoDB based learning implementation'

VERSIONCOMPONENTS = [0, 1, 303]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_objective_lookup',
    'supports_objective_query',
    # 'supports_objective_search',
    'supports_objective_admin',
    # 'supports_objective_notification',
    'supports_objective_hierarchy',
    'supports_objective_hierarchy_design',
    'supports_objective_sequencing',
    'supports_objective_objective_bank',
    'supports_objective_objective_bank_assignment',
    # 'supports_objective_smart_objective_bank',
    'supports_objective_requisite',
    'supports_objective_requisite_assignment',
    'supports_activity_lookup',
    # 'supports_activity_query',
    # 'supports_activity_search',
    'supports_activity_admin',
    # 'supports_activity_notification',
    'supports_activity_objective_bank',
    'supports_activity_objective_bank_assignment',
    # 'supports_activity_smart_objective_bank',
    'supports_proficiency_lookup',
    'supports_proficiency_query',
    # 'supports_proficiency_search',
    'supports_proficiency_admin',
    # 'supports_proficiency_notification',
    # 'supports_proficiency_objective_bank',
    # 'supports_proficiency_objective_bank_assignment',
    # 'supports_proficiency_smart_objective_bank',
    # 'supports_my_learning_path',
    # 'supports_learning_path',
    'supports_objective_bank_lookup',
    # 'supports_objective_bank_query',
    # 'supports_objective_bank_search',
    'supports_objective_bank_admin',
    # 'supports_objective_bank_notification',
    'supports_objective_bank_hierarchy',
    'supports_objective_bank_hierarchy_design',
    # 'supports_learning_batch',
]
