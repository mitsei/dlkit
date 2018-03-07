"""Mongo osid profile elements for assessment service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by assessment.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo assessment'

DESCRIPTION = 'MongoDB based assessment implementation'

VERSIONCOMPONENTS = [0, 1, 40]

RELEASEDATE = "2018-03-07"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    # 'supports_my_assessment_taken',
    'supports_assessment',
    'supports_assessment_results',
    'supports_item_lookup',
    'supports_item_query',
    'supports_item_search',
    'supports_item_admin',
    'supports_item_notification',
    'supports_item_bank',
    'supports_item_bank_assignment',
    # 'supports_item_smart_bank',
    'supports_assessment_lookup',
    'supports_assessment_query',
    # 'supports_assessment_search',
    'supports_assessment_admin',
    # 'supports_assessment_notification',
    'supports_assessment_bank',
    'supports_assessment_bank_assignment',
    # 'supports_assessment_smart_bank',
    'supports_assessment_basic_authoring',
    'supports_assessment_offered_lookup',
    'supports_assessment_offered_query',
    # 'supports_assessment_offered_search',
    'supports_assessment_offered_admin',
    # 'supports_assessment_offered_notification',
    'supports_assessment_offered_bank',
    'supports_assessment_offered_bank_assignment',
    # 'supports_assessment_offered_smart_bank',
    'supports_assessment_taken_lookup',
    'supports_assessment_taken_query',
    # 'supports_assessment_taken_search',
    'supports_assessment_taken_admin',
    # 'supports_assessment_taken_notification',
    'supports_assessment_taken_bank',
    'supports_assessment_taken_bank_assignment',
    # 'supports_assessment_taken_smart_bank',
    'supports_bank_lookup',
    'supports_bank_query',
    # 'supports_bank_search',
    'supports_bank_admin',
    # 'supports_bank_notification',
    'supports_bank_hierarchy',
    'supports_bank_hierarchy_design',
    # 'supports_assessment_authoring',
    # 'supports_assessment_batch',
]
