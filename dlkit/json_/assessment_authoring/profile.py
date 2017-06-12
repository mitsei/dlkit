"""Mongo osid profile elements for assessment.authoring service packages"""
# -*- coding: utf-8 -*-
# pylint: disable=unused-import
#    importing common values to be used by assessment.authoring.ProfileManger implementation

from ..profile import ID
from ..profile import LANGUAGETYPE
from ..profile import SCRIPTTYPE
from ..profile import FORMATTYPE
from ..profile import VERSIONSCHEME
from ..profile import LOCALES
from ..profile import LICENSE
from ..profile import PROVIDERID
from ..profile import OSIDVERSION

DISPLAYNAME = 'Mongo assessment.authoring'

DESCRIPTION = 'MongoDB based assessment.authoring implementation'

VERSIONCOMPONENTS = [0, 1, 304]

RELEASEDATE = "2017-06-12"

SUPPORTS = [  # 'Remove the # when implementations exist:'
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_assessment_part_lookup',
    'supports_assessment_part_query',
    # 'supports_assessment_part_search',
    'supports_assessment_part_admin',
    # 'supports_assessment_part_notification',
    # 'supports_assessment_part_bank',
    # 'supports_assessment_part_bank_assignment',
    # 'supports_assessment_part_smart_bank',
    'supports_assessment_part_item',
    'supports_assessment_part_item_design',
    'supports_sequence_rule_lookup',
    # 'supports_sequence_rule_query',
    # 'supports_sequence_rule_search',
    'supports_sequence_rule_admin',
    # 'supports_sequence_rule_notification',
    # 'supports_sequence_rule_bank',
    # 'supports_sequence_rule_bank_assignment',
    # 'supports_sequence_rule_smart_bank',
    # 'supports_sequence_rule_enabler_lookup',
    # 'supports_sequence_rule_enabler_query',
    # 'supports_sequence_rule_enabler_search',
    # 'supports_sequence_rule_enabler_admin',
    # 'supports_sequence_rule_enabler_notification',
    # 'supports_sequence_rule_enabler_bank',
    # 'supports_sequence_rule_enabler_bank_assignment',
    # 'supports_sequence_rule_enabler_smart_bank',
    # 'supports_sequence_rule_enabler_rule_lookup',
    # 'supports_sequence_rule_enabler_rule_application',
]
