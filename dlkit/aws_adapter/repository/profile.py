"""
# -*- coding: utf-8 -*-
# This profile.py has been constructed from
# resource/ResourceProfile/profile_template.txt
"""
ID = {'authority': 'birdland.mit.edu',
      'namespace': 'repository',
      'identifier': 'aws_adapter'}

LANGUAGETYPE = {
    'identifier': 'ENG',
    'namespace': '639-2',
    'authority': 'ISO',
    # The following may be optional. Time will tell.
    'domain': 'DisplayText Languages',
    'display_name': 'English Text Language',
    'display_label': 'English',
    'description': 'The display text language type for the English language.'
}

SCRIPTTYPE = {
    'identifier': 'LATN',
    'namespace': '15924',
    'authority': 'ISO',
    # The following may be optional. Time will tell.
    'domain': 'ISO Script Types',
    'display_name': 'Latin Text Script',
    'display_label': 'Latin',
    'description': 'The display text script type for the Latin script.'
}

FORMATTYPE = {
    'identifier': 'PLAIN',
    'namespace': 'TextFormats',
    'authority': 'okapia.net',
    # The following may be optional. Time will tell.
    'domain': 'DisplayText Formats',
    'display_name': 'Plain Text Format',
    'display_label': 'Plain',
    'description': 'The display text format type for the Plain format.'
}

DISPLAYNAME = 'AWS Adapter repository'

DESCRIPTION = 'repository adapter for Amazon Web Services support'

VERSIONSCHEME = {'authority': 'birdland.mit.edu',
                 'namespace': 'repository',
                 'identifier': '1'}

LOCALES = None  # someday I'll deal with this ####

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

PROVIDERID = {'authority': 'odl.mit.edu',
              'namespace': 'weaselworks',
              'identifier': 'goulish_tinkering'}

OSIDVERSION = [3, 0, 0]

VERSIONCOMPONENTS = [0, 0, 71]

RELEASEDATE = '2015-05-03'


SUPPORTS = [  # Uncomment the following lines when implementations exist:
    # 'supports_journal_rollback',
    # 'supports_journal_branching',
    # 'supports_visible_federation',
    'supports_asset_lookup',
    'supports_asset_query',
    'supports_asset_search',
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
    # 'supports_repository_lookup',
    # 'supports_repository_query',
    # 'supports_repository_search',
    # 'supports_repository_admin',
    # 'supports_repository_notification',
    # 'supports_repository_hierarchy',
    # 'supports_repository_hierarchy_design',
    # 'supports_repository_batch',
    # 'supports_repository_rules'
]
