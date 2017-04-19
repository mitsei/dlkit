# -*- coding: utf-8 -*-

from .settings import LANGUAGETYPEID, SCRIPTTYPEID, FORMATTYPEID

# This profile holds most of the information that is accessed through
# the LearningProfile implementation of the MIT Core Concept Catalog (MC3)
# Handcar implementation.

ID = {'authority': 'birdland.mit.edu',
      'namespace': 'learning',
      'identifier': 'MC3'}

# Don't need the ID anymore now that we have the ROOT_BANK.  Delete Soon:
ROOT_BANK_ID = {'authority': 'MIT-OEIT',
                'namespace': 'dlkit-objectivebank',
                'identifier': 'mc3.root'}

ROOT_BANK = {
    'displayName': {
        'text': 'MC3 Root Bank',
        'languageTypeId': LANGUAGETYPEID,
        'scriptTypeId': SCRIPTTYPEID,
        'formatTypeId': FORMATTYPEID
    },
    'description': {
        'text': 'Root level ObjectiveBank to support cross-bank functionality',
        'languageTypeId': LANGUAGETYPEID,
        'scriptTypeId': SCRIPTTYPEID,
        'formatTypeId': FORMATTYPEID
    },
    'genusTypeId': 'dlkit-objectivebank%3Adlkit.learning.objectivebank.mc3root%40MIT-OEIT',
    'type': 'ObjectiveBank',
    'id': 'dlkit-objectivebank%3Amc3.root%40MIT-OEIT'
}


DISPLAYNAME = 'MC3 Learning Service'

DESCRIPTION = 'OSID learning service implementation of the MIT Core Concept Catalog (MC3)'

VERSIONSCHEME = {'authority': 'birdland.mit.edu',
                 'namespace': 'learning',
                 'identifier': '1'}

LOCALES = None  # someday I should deal with this ####

LICENSE = """
<p>This implementation ("Work") and the information contained herein is
provided on an "AS IS" basis. The Massachusetts Institute of Technology.
THE AUTHORS DISCALIM ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OF IN
CONNECTION WITH THE WORK OR THE USE OR OTHER DEALINGS IN THE WORK.
</p><p>Permission to use, copy, modify, adapt and distribute this Work,
for any purpose, without fee or royalty is hereby granted, provided that
you include the above copyright notice and the
terms of this license on ALL copies of the Work of portions thereof.
</p><p>The export of software employing encryption technology may require
a specific license from the United States Government. It is the
responsibility of any person or organization contemplating export to obtain
such a license before exporting this Work.</p>"""

PROVIDERID = {'authority': 'mc3.mit.edu',
              'namespace': 'handcar.learning.service',
              'identifier': 'goulish_tinkering'}

OSIDVERSION = [3, 0, 0]

VERSIONCOMPONENTS = [0, 0, 1]

RELEASEDATE = '2013-08-06'


SUPPORTS = [  # Uncomment the following lines when implementations exist

    # Learning related support statements:
    #
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
    # 'supports_objective_objective_bank',
    'supports_objective_objective_bank_assignment',
    # 'supports_objective_smart_objective_bank',
    'supports_objective_requisite',
    'supports_objective_requisite_assignment',
    'supports_activity_lookup',
    'supports_activity_query',
    # 'supports_activity_search',
    'supports_activity_admin',
    # 'supports_activity_notification',
    # 'supports_activity_objective_bank',
    # 'supports_activity_objective_bank_assignment',
    # 'supports_activity_smart_objective_bank',
    # 'supports_proficiency_lookup',
    # 'supports_proficiency_query',
    # 'supports_proficiency_search',
    # 'supports_proficiency_admin',
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

    # Repository related support statements:
    #
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_asset_lookup',
    # 'supports_asset_query',
    # 'supports_asset_search',
    'supports_asset_admin',
    # 'supports_asset_notification',
    # 'supports_asset_repository',
    # 'supports_asset_repository_assignment',
    # 'supports_asset_smart_repository',
    # 'supports_asset_temporal',
    # 'supports_asset_temporal_assignment',
    # 'supports_asset_spatial',
    # 'supports_asset_spatial_assignment',
    # 'supports_asset_composition',
    # 'supports_asset_composition_design',
    # 'supports_composition_lookup',
    # 'supports_composition_query',
    # 'supports_composition_search',
    # 'supports_composition_admin',
    # 'supports_composition_notification',
    # 'supports_composition_repository',
    # 'supports_composition_repository_assignment',
    # 'supports_composition_smart_repository',
    'supports_repository_lookup',
    # 'supports_repository_query',
    # 'supports_repository_search',
    'supports_repository_admin',
    # 'supports_repository_notification',
    # 'supports_repository_hierarchy',
    # 'supports_repository_hierarchy_design',
    # 'supports_repository_batch',
    # 'supports_repository_rules',

    # Relationship related support statement:
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_relationship_lookup',
    # 'supports_relationship_query',
    # 'supports_relationship_search',
    'supports_relationship_admin',
    # 'supports_relationship_notification',
    # 'supports_relationship_family',
    # 'supports_relationship_family_assignment',
    # 'supports_relationship_smart_family',
    'supports_family_lookup',
    # 'supports_family_query',
    # 'supports_family_search',
    # 'supports_family_admin',
    # 'supports_family_notification',
    # 'supports_family_hierarchy',
    # 'supports_family_hierarchy_design',
    # 'supports_relationship_batch',
    # 'supports_relationship_rules',

    # Type related support statements:
    #
    'supports_type_lookup',
    # 'supports_type_admin',

    # Proxy related support statements:
    #
    'supports_proxy',
]

PROXY_CONDITION_RECORD_TYPES = [{
    "authority": "MIT-OEIT",
    "description": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "A ProxyCondition that can deal with MIT Touchstone requests"
    },
    "displayLabel": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "Touchstone ProxyCondition"
    },
    "displayName": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "Touchstone ProxyCondition Record Type"
    },
    "domain": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "proxy_condition"
    },
    "id": "dlkit-proxy%3Adlkit.proxycondition.touchstone%40MIT-OEIT",
    "identifier": "dlkit.proxycondition.touchstone",
    "identifierNamespace": "dlkit-proxy-condition",
    "module": ""
}]
CREDENTIAL_RECORD_TYPES = [{
    "authority": "MIT-OEIT",
    "description": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "An agent kay provided by the Handcar service"
    },
    "displayLabel": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "Handcar Agent Key"
    },
    "displayName": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "Handcar Agent Key Credential Type"
    },
    "domain": {
        "formatTypeId": FORMATTYPEID,
        "languageTypeId": LANGUAGETYPEID,
        "scriptTypeId": SCRIPTTYPEID,
        "text": "credential"
    },
    "id": "dlkit-proxy%3Adlkit.credential.handcar%40MIT-OEIT",
    "identifier": "dlkit.credential.handcar",
    "identifierNamespace": "dlkit-credential",
}]
