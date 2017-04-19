
# The domain name of the handar host server to use:
# This needs to be set using another mechanism. like the configuration service.
# The Handcar impl should not have this much knowldege about the consuming
# application's runtime environment.
try:
    from django.conf import settings
    HOST = settings.MC3_HOST
except:
    # HOST = 'mc3-demo.mit.edu'
    HOST = 'mc3-dev.mit.edu'
    # HOST = 'mc3.mit.edu'

if HOST == 'mc3-dev.mit.edu':  # use the serialized RC formatted types:
    LANGUAGETYPEID = '639-2%3AENG%40iso.org'
    SCRIPTTYPEID = '15924%3ALATN%40iso.org'
    FORMATTYPEID = 'format.text%3APlain%40okapia.net'
else:                         # use the serialized D6 formatted types:
    LANGUAGETYPEID = '639-2%3AEnglish%40ISO'
    SCRIPTTYPEID = '15924%3ALatin%40ISO'
    FORMATTYPEID = 'Text+Formats%3Aplain%40okapia.net'

try:
    from django.conf import settings
    APP_KEYS = dict(settings.APP_KEYS)
except:
    APP_KEYS = {
        'mc3-demo.mit.edu': 'ACTUAL_KEYS_SHOULD_BE_IN_KEYS_MODULE',
        'mc3-dev.mit.edu': 'ACTUAL_KEYS_SHOULD_BE_IN_KEYS_MODULE',
        'mc3.mit.edu': 'ACTUAL_KEYS_SHOULD_BE_IN_KEYS_MODULE'
    }

# The url of the handcar service application. At some point this will
# likely go away:
HANDCAR = 'https://' + HOST + '/handcar'

# Make up an authority to use for any implementation assembled Osid Ids
AUTHORITY = HOST

# The display text types for this instance of hc_learning:
LANGUAGE_TYPE_ID = '639-2%3AEnglish%40ISO'
SCRIPT_TYPE_ID = '15924%3ALatin%40ISO'
FORMAT_TYPE_ID = 'Text+Formats%3Aplain%40okapia.net'

# Dictionary of the default genusTypeIds for various objects, indexed by
# Id namespace:
DEFAULT_GENUS_TYPES = {
    'learning.Objective': 'mc3-objective%3Amc3.learning.topic%40MIT-OEIT',
    'learning.Activity': 'mc3-activity%3Amc3.learning.activity.asset.based%40MIT-OEIT',
    'learning.ObjectiveBank': 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT',
    'repository.Asset': 'mc3-asset%3Amc3.learning.asset.url%40MIT-OEIT',
    'repository.AssetContent': 'mc3-asset-content%3Amc3.learning.asset.content.unknown%40MIT-OEIT',
    'repository.Repository': 'mc3-objectivebank%3Amc3.learning.objectivebank.sandbox%40MIT-OEIT',
    'relationship.Relationship': 'mc3-relationship%3Amc3.lo.2.lo.related%40MIT-OEIT',
    'authentication.Agent': 'dlkit_authentication%3Adlkit_default_agent%40MIT-OEIT'
}

# The following metadata elements will be used to validate forms prior to
# being posted to handcar. This implementation can assert any metadata
# restrictions it wishes. Just make sure these fall within any parameters
# required by handcar itself. For instance, strings maximum lengths should
# be less than or equal to the max lengths imposed by handcar.
METADATA = {
    'journalComment': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'osid.OsidForm',
            'identifier': 'comment'
        },
        'element_label': 'Comment',
        'instructions': 'Optional form submission comment, 255 character maximum',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 256,
        'string_set': []
    },
    'display_name': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'osid.OsidObjectForm',
            'identifier': 'displayName'
        },
        'element_label': 'Display Name',
        'instructions': 'Optional (default value will be provided by system), 255 character maximum',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 256,
        'string_set': []
    },
    'description': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'osid.OsidObjectForm',
            'identifier': 'description'
        },
        'element_label': 'Description',
        'instructions': 'Optional (default value will be provided by system), 255 character maximum',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 1024,
        'string_set': []
    },
    'genus_type': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'osid.OsidObjectForm',
            'identifier': 'genus_type'
        },
        'element_label': 'Genus Type',
        'instructions': 'Required genus Type of type osid.type.Type',
        'required': True,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'TYPE',
        'array': False,
        'type_set': []
    },
    'genus_type_id': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'osid.OsidObjectForm',
            'identifier': 'genus_type'
        },
        'element_label': 'Genus Type Id',
        'instructions': 'Required genus Type Id of type osid.id.Id',
        'required': True,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': False,
        'id_set': []
    },
    'assessment_id': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'learning.ObjectiveForm',
            'identifier': 'assessment'
        },
        'element_label': 'Assessment',
        'instructions': 'Optional assessment Id of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': False,
        'id_set': []
    },
    'knowledge_category_id': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'learning.ObjectiveForm',
            'identifier': 'knowledge_category'
        },
        'element_label': 'Knowledge Category',
        'instructions': 'Optional knowledge category Id of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': False,
        'id_set': []
    },
    'cognitive_process_id': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'learning.ObjectiveForm',
            'identifier': 'cognitive_process'
        },
        'element_label': 'Cognitive Process',
        'instructions': 'Optional cognitive process Id of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': False,
        'id_set': [],
        'minimum_elements': None,
        'maximum_elements': None
    },
    'asset_ids': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'learning.ActivityForm',
            'identifier': 'assets'
        },
        'element_label': 'Assets',
        'instructions': 'Optional Asset Id list of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': True,
        'id_set': [],
        'minimum_elements': None,
        'maximum_elements': None
    },
    'course_ids': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'learning.ActivityForm',
            'identifier': 'courses'
        },
        'element_label': 'Courses',
        'instructions': 'Optional Course Id list of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': True,
        'id_set': [],
        'minimum_elements': None,
        'maximum_elements': None
    },
    'assessment_ids': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'learning.ActivityForm',
            'identifier': 'assessments'
        },
        'element_label': 'Assessments',
        'instructions': 'Optional Assessment Id list of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': True,
        'id_set': [],
        'minimum_elements': None,
        'maximum_elements': None
    },
    'title': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'title'
        },
        'element_label': 'Title',
        'instructions': 'Optional, 255 character maximum',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 256,
        'string_set': []
    },
    'public_domain': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'public_domain'
        },
        'element_label': 'Is public_domain',
        'instructions': 'Optional, true/false',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'BOOLEAN',
        'array': False,
    },
    'copyright': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'copyright'
        },
        'element_label': 'Copyright',
        'instructions': 'Optional, 1024 character maximum',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 1024,
        'string_set': []
    },
    'distribute_verbatim': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'distribute_verbatim'
        },
        'element_label': 'Can distribute verbatim',
        'instructions': 'Optional, true/false',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'BOOLEAN',
        'array': False,
    },
    'distribute_alterations': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'distribute_alterations'
        },
        'element_label': 'Can distribute alterations',
        'instructions': 'Optional, true/false',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'BOOLEAN',
        'array': False,
    },
    'distribute_compositions': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'distribute_compositions'
        },
        'element_label': 'Can distribute compositions',
        'instructions': 'Optional, true/false',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'BOOLEAN',
        'array': False,
    },
    'source_id': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'source'
        },
        'element_label': 'Source',
        'instructions': 'Optional Source Id of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': False,
        'id_set': []
    },
    'provider_link_ids': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'provider_links'
        },
        'element_label': 'Provider links',
        'instructions': 'Optional provider link Id list of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': True,
        'id_set': [],
        'minimum_elements': None,
        'maximum_elements': None
    },
    'created_date': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'created_date'
        },
        'element_label': 'Created date',
        'instructions': 'Optional date created',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',  # NO, this wants to be a DateTime
        'array': False,
        # also include the date time metadata
    },
    'published': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'published'
        },
        'element_label': 'Is published',
        'instructions': 'Optional, true/false',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'BOOLEAN',
        'array': False,
    },
    'published_date': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'published_date'
        },
        'element_label': 'Published date',
        'instructions': 'Optional date published',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',  # NO, this wants to be a DateTime
        'array': False,
        # also include the date time metadata
    },
    'principal_credit_string': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'principal_credit_string'
        },
        'element_label': 'Principal credit string',
        'instructions': 'Optional, 255 character maximum',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 255,
        'string_set': []
    },
    'composition_id': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetForm',
            'identifier': 'composition'
        },
        'element_label': 'Composition',
        'instructions': 'Optional Composition Id of type osid.id.Id',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'ID',
        'array': False,
        'id_set': []
    },
    'accessibility_type': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetContentForm',
            'identifier': 'accessibility_type'
        },
        'element_label': 'Accessibility Type',
        'instructions': 'Optional accessibility Type of type osid.type.Type',
        'required': True,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'TYPE',
        'array': False,
        'type_set': []
    },
    'data': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetContentForm',
            'identifier': 'data'
        },
        'element_label': 'Data',
        'instructions': 'Optional data',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',  # NO, this wants to be a DataStream
        'array': False,
        # also include the datastream metadata
    },
    'url': {
        'element_id': {
            'authority': AUTHORITY,
            'namespace': 'repository.AssetContentForm',
            'identifier': 'url'
        },
        'element_label': 'URL',
        'instructions': 'Optional URL',
        'required': False,
        'value': False,
        'read_only': False,
        'linked': False,
        'syntax': 'STRING',
        'array': False,
        'minimum_string_length': 0,
        'maximum_string_length': 255,
        'string_set': []
    },
}
