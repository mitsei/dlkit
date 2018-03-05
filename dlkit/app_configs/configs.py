import os

from dlkit.runtime.primordium import Type
from .handcar_configs import HANDCAR_MC3

# Some default values for the settings.
HANDCAR_IMPL = 'HANDCAR_MC3'
CLOUDFRONT_PUBLIC_KEY = ''
CLOUDFRONT_PRIVATE_KEY = ''
CLOUDFRONT_SIGNING_KEYPAIR_ID = ''
CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE = ''
CLOUDFRONT_DISTRO = ''
CLOUDFRONT_DISTRO_ID = ''
CLOUDFRONT_TEST_DISTRO = ''
CLOUDFRONT_TEST_DISTRO_ID = ''
S3_PRIVATE_KEY = ''
S3_PUBLIC_KEY = ''
S3_BUCKET = ''
S3_TEST_BUCKET = 'mitodl-repository-test'  # mostly so that the VCR test cassettes work
S3_TEST_PRIVATE_KEY = ''
S3_TEST_PUBLIC_KEY = ''
DLKIT_MONGO_DB_PREFIX = 'test_dlkit_'
DLKIT_AUTHORITY = 'ODL.MIT.EDU'
DLKIT_MONGO_DB_INDEXES = {
    DLKIT_MONGO_DB_PREFIX + 'grading.GradeEntry': ['gradebookColumnId'],
    DLKIT_MONGO_DB_PREFIX + 'assessment.Assessment': ['itemIds'],
    DLKIT_MONGO_DB_PREFIX + 'assessment.Item': ['bankId', 'learningObjectiveIds'],
    DLKIT_MONGO_DB_PREFIX + 'repository.Asset': ['repositoryId']
}

DLKIT_MONGO_KEYWORD_FIELDS = {
    DLKIT_MONGO_DB_PREFIX + 'repository.Asset': ['assetContents.0.text.text'],
    DLKIT_MONGO_DB_PREFIX + 'logging.LogEntry': ['text.text']
}
MONGO_HOST_URI = 'localhost:27017'

try:
    # If you are using Django, you can also configure dlkit from your
    # Django settings.py file.
    from django.conf import settings
except ImportError:
    #   Try to get them from the environment.
    if 'HANDCAR_IMPL' in os.environ:
        HANDCAR_IMPL = os.environ['HANDCAR_IMPL']
    if 'CLOUDFRONT_PUBLIC_KEY' in os.environ:
        CLOUDFRONT_PUBLIC_KEY = os.environ['CLOUDFRONT_PUBLIC_KEY']
    if 'CLOUDFRONT_PRIVATE_KEY' in os.environ:
        CLOUDFRONT_PRIVATE_KEY = os.environ['CLOUDFRONT_PRIVATE_KEY']
    if 'CLOUDFRONT_SIGNING_KEYPAIR_ID' in os.environ:
        CLOUDFRONT_SIGNING_KEYPAIR_ID = os.environ['CLOUDFRONT_SIGNING_KEYPAIR_ID']
    if 'CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE' in os.environ:
        CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE = os.environ['CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE']
    if 'CLOUDFRONT_DISTRO' in os.environ:
        CLOUDFRONT_DISTRO = os.environ['CLOUDFRONT_DISTRO']
    if 'CLOUDFRONT_DISTRO_ID' in os.environ:
        CLOUDFRONT_DISTRO_ID = os.environ['CLOUDFRONT_DISTRO_ID']
    if 'CLOUDFRONT_TEST_DISTRO' in os.environ:
        CLOUDFRONT_TEST_DISTRO = os.environ['CLOUDFRONT_TEST_DISTRO']
    if 'CLOUDFRONT_TEST_DISTRO_ID' in os.environ:
        CLOUDFRONT_TEST_DISTRO_ID = os.environ['CLOUDFRONT_TEST_DISTRO_ID']
    if 'S3_PRIVATE_KEY' in os.environ:
        S3_PRIVATE_KEY = os.environ['S3_PRIVATE_KEY']
    if 'S3_PUBLIC_KEY' in os.environ:
        S3_PUBLIC_KEY = os.environ['S3_PUBLIC_KEY']
    if 'S3_BUCKET' in os.environ:
        S3_BUCKET = os.environ['S3_BUCKET']
    if 'S3_TEST_BUCKET' in os.environ:
        S3_TEST_BUCKET = os.environ['S3_TEST_BUCKET']
    if 'S3_TEST_PRIVATE_KEY' in os.environ:
        S3_TEST_PRIVATE_KEY = os.environ['S3_TEST_PRIVATE_KEY']
    if 'S3_TEST_PUBLIC_KEY' in os.environ:
        S3_TEST_PUBLIC_KEY = os.environ['S3_TEST_PUBLIC_KEY']
    if 'DLKIT_MONGO_DB_PREFIX' in os.environ:
        DLKIT_MONGO_DB_PREFIX = os.environ['DLKIT_MONGO_DB_PREFIX']
    if 'DLKIT_AUTHORITY' in os.environ:
        DLKIT_AUTHORITY = os.environ['DLKIT_AUTHORITY']
    if 'DLKIT_MONGO_DB_INDEXES' in os.environ:
        DLKIT_MONGO_DB_INDEXES = os.environ['DLKIT_MONGO_DB_INDEXES']
    if 'DLKIT_MONGO_KEYWORD_FIELDS' in os.environ:
        DLKIT_MONGO_KEYWORD_FIELDS = os.environ['DLKIT_MONGO_KEYWORD_FIELDS']
    if 'MONGO_HOST_URI' in os.environ:
        MONGO_HOST_URI = os.environ['MONGO_HOST_URI']
else:
    from django.core.exceptions import ImproperlyConfigured
    try:
        settings.configure()
    except RuntimeError:
        pass  # already configured
    else:
        # Should not be called because should happen in handcar_configs.py
        import django
        if django.VERSION < (1, 8):
            settings._setup()
        else:
            django.setup()
    try:
        HANDCAR_IMPL = getattr(settings, 'HANDCAR_IMPL', '')
        CLOUDFRONT_PUBLIC_KEY = getattr(settings, 'CLOUDFRONT_PUBLIC_KEY', '')
        CLOUDFRONT_PRIVATE_KEY = getattr(settings, 'CLOUDFRONT_PRIVATE_KEY', '')
        CLOUDFRONT_SIGNING_KEYPAIR_ID = getattr(settings, 'CLOUDFRONT_SIGNING_KEYPAIR_ID', '')
        CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE = getattr(settings, 'CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE', '')
        CLOUDFRONT_DISTRO = getattr(settings, 'CLOUDFRONT_DISTRO', '')
        CLOUDFRONT_DISTRO_ID = getattr(settings, 'CLOUDFRONT_DISTRO_ID', '')
        CLOUDFRONT_TEST_DISTRO = getattr(settings, 'CLOUDFRONT_TEST_DISTRO', '')
        CLOUDFRONT_TEST_DISTRO_ID = getattr(settings, 'CLOUDFRONT_TEST_DISTRO_ID', '')
        S3_PRIVATE_KEY = getattr(settings, 'S3_PRIVATE_KEY', '')
        S3_PUBLIC_KEY = getattr(settings, 'S3_PUBLIC_KEY', '')
        S3_BUCKET = getattr(settings, 'S3_BUCKET', '')
        S3_TEST_BUCKET = getattr(settings, 'S3_TEST_BUCKET', '')
        S3_TEST_PRIVATE_KEY = getattr(settings, 'S3_TEST_PRIVATE_KEY', '')
        S3_TEST_PUBLIC_KEY = getattr(settings, 'S3_TEST_PUBLIC_KEY', '')
        DLKIT_MONGO_DB_PREFIX = getattr(settings, 'DLKIT_MONGO_DB_PREFIX', '')
        DLKIT_AUTHORITY = getattr(settings, 'DLKIT_AUTHORITY', '')
        DLKIT_MONGO_DB_INDEXES = getattr(settings, 'DLKIT_MONGO_DB_INDEXES', '')
        DLKIT_MONGO_KEYWORD_FIELDS = getattr(settings, 'DLKIT_MONGO_KEYWORD_FIELDS', '')
        MONGO_HOST_URI = getattr(settings, 'MONGO_HOST_URI', '')
    except ImproperlyConfigured:
        pass

# Set up the file path for testing, use filesystem_adapter
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir, '..'))

DATA_STORE_PATH = 'datastore'

TEST_DATA_STORE_PATH = 'test_datastore'


def impl_key_dict(value, priority=1):
    """to reduce duplicate code in configs.py and handcar_configs.py"""
    return {
        'syntax': 'STRING',
        'displayName': 'Implementation Key',
        'description': 'Implementation key used by Runtime for class loading',
        'values': [
            {'value': value, 'priority': priority}
        ]
    }


AWS_ASSET_CONTENT_TYPE = Type(**
                              {
                                  'authority': 'odl.mit.edu',
                                  'namespace': 'asset_content_record_type',
                                  'identifier': 'amazon-web-services'
                              })

FILESYSTEM_ASSET_CONTENT_TYPE = Type(**
                                     {
                                         'authority': 'odl.mit.edu',
                                         'namespace': 'asset_content_record_type',
                                         'identifier': 'filesystem'
                                     })

###################################################
# PRODUCTION SETTINGS
###################################################

AWS_ADAPTER_1 = {
    'id': 'aws_adapter_configuration_1',
    'displayName': 'AWS Adapter Configuration',
    'description': 'Configuration for AWS Adapter',
    'parameters': {
        'implKey': impl_key_dict('aws_adapter'),
        'cloudFrontPublicKey': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Public Key',
            'description': 'Public key for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_PUBLIC_KEY, 'priority': 1}
            ]
        },
        'cloudFrontPrivateKey': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Private Key',
            'description': 'Private key for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_PRIVATE_KEY, 'priority': 1}
            ]
        },
        'cloudFrontSigningKeypairId': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Signing Keypair ID',
            'description': 'Signing keypair id for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_SIGNING_KEYPAIR_ID, 'priority': 1}
            ]
        },
        'cloudFrontSigningPrivateKeyFile': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Signing Private Key File',
            'description': 'Signing Private Key File for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE, 'priority': 1}
            ]
        },
        'cloudFrontDistro': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Distro',
            'description': 'CloudFront Distr-o-bution.',
            'values': [
                {'value': CLOUDFRONT_DISTRO, 'priority': 1}
            ]
        },
        'cloudFrontDistroId': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Distro Id',
            'description': 'CloudFront Distr-o-bution Id.',
            'values': [
                {'value': CLOUDFRONT_DISTRO_ID, 'priority': 1}
            ]
        },
        'S3PrivateKey': {
            'syntax': 'STRING',
            'displayName': 'S3 Private Key',
            'description': 'Private Key for Amazon S3.',
            'values': [
                {'value': S3_PRIVATE_KEY, 'priority': 1}
            ]
        },
        'S3PublicKey': {
            'syntax': 'STRING',
            'displayName': 'S3 Public Key',
            'description': 'Public Key for Amazon S3.',
            'values': [
                {'value': S3_PUBLIC_KEY, 'priority': 1}
            ]
        },
        'S3Bucket': {
            'syntax': 'STRING',
            'displayName': 'S3 Bucket',
            'description': 'Bucket for Amazon S3.',
            'values': [
                {'value': S3_BUCKET, 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
    }
}

FILESYSTEM_ADAPTER_1 = {
    'id': 'filesystem_adapter_configuration_1',
    'displayName': 'Filesystem Adapter Configuration',
    'description': 'Configuration for Filesystem Adapter',
    'parameters': {
        'implKey': impl_key_dict('filesystem_adapter'),
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'dataStorePath': {
            'syntax': 'STRING',
            'displayName': 'Path to local filesystem datastore',
            'description': 'Filesystem path for setting the MongoClient host.',
            'values': [
                {'value': DATA_STORE_PATH, 'priority': 1}  # Mac
            ]
        },
        # 'secondaryDataStorePath': {
        #     'syntax': 'STRING',
        #     'displayName': 'Path to local filesystem datastore',
        #     'description': 'Filesystem path for setting the MongoClient host.',
        #     'values': [
        #         {'value': STUDENT_RESPONSE_DATA_STORE_PATH, 'priority': 1}  # Mac
        #     ]
        # },
        'dataStoreFullPath': {
            'syntax': 'STRING',
            'displayName': 'Full path to local filesystem datastore',
            'description': 'Filesystem path for setting the JSONClient host.',
            'values': [
                {'value': ABS_PATH, 'priority': 1}
            ]
        },
        'urlHostname': {
            'syntax': 'STRING',
            'displayName': 'Hostname config for serving files over the network',
            'description': 'Hostname config for serving files.',
            'values': [
                {'value': 'http://example.com/api/v1', 'priority': 1}  # Mac
            ]
        },
    }
}

JSON_1 = {
    'id': 'json_configuration_1',
    'displayName': 'JSON Configuration',
    'description': 'Configuration for JSON Implementation',
    'parameters': {
        'implKey': impl_key_dict('json'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': DLKIT_MONGO_DB_PREFIX, 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': DLKIT_AUTHORITY, 'priority': 1}
            ]
        },
        'indexes': {
            'syntax': 'OBJECT',
            'displayName': 'Mongo DB Indexes',
            'description': 'Indexes to set in MongoDB',
            'values': [
                {'value': DLKIT_MONGO_DB_INDEXES, 'priority': 1}
            ]
        },
        'mongoHostURI': {
            'syntax': 'STRING',
            'displayName': 'Mongo Host URI',
            'description': 'URI for setting the MongoClient host.',
            'values': [
                {'value': MONGO_HOST_URI, 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'assetContentRecordTypeForFiles': {
            'syntax': 'TYPE',
            'displayName': 'Asset Content Type for Files',
            'description': 'Asset Content Type for Records that store Files in a repository',
            'values': [
                {'value': FILESYSTEM_ASSET_CONTENT_TYPE, 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'dlkit.records.registry', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': HANDCAR_IMPL, 'priority': 1}
            ]
        },
        'keywordFields': {
            'syntax': 'OBJECT',
            'displayName': 'Keyword Fields',
            'description': 'Text fields to include in keyword queries',
            'values': [
                {'value': DLKIT_MONGO_KEYWORD_FIELDS, 'priority': 1}
            ]
        },
        'magicItemLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic item lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
            ]
        },
        'magicAssessmentPartLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic assessment part lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'useCachingForQualifierIds': {
            'syntax': 'BOOLEAN',
            'displayName': 'Flag to use memcached for authz qualifier_ids or not',
            'description': 'Flag to use memcached for authz qualifier_ids or not',
            'values': [
                {'value': True, 'priority': 1}
            ]
        },
        # 'useFilesystem': {
        #     'syntax': 'BOOLEAN',
        #     'displayName': 'Use the filesystem instead of MongoDB',
        #     'description': 'Use the filesystem instead of MongoDB',
        #     'values': [
        #         {'value': True, 'priority': 1}
        #     ]
        # },
        # 'dataStorePath': {
        #     'syntax': 'STRING',
        #     'displayName': 'Path to local filesystem datastore',
        #     'description': 'Filesystem path for setting the MongoClient host.',
        #     'values': [
        #         {'value': DATA_STORE_PATH, 'priority': 1}
        #     ]
        # },
        # 'dataStoreFullPath': {
        #     'syntax': 'STRING',
        #     'displayName': 'Full path to local filesystem datastore',
        #     'description': 'Filesystem path for setting the MongoClient host.',
        #     'values': [
        #         {'value': ABS_PATH, 'priority': 1}
        #     ]
        # },
    }
}

AUTHZ_ADAPTER_1 = {
    'id': 'authz_adapter_configuration_1',
    'displayName': 'AuthZ Adapter Configuration',
    'description': 'Configuration for AuthZ Adapter',
    'parameters': {
        'implKey': impl_key_dict('authz_adapter'),
        'authzAuthorityImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
    }
}

SERVICE = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'JSON_1', 'priority': 1}
            ]
        },
    }
}

BOOTSTRAP = {
    'id': 'bootstrap_configuration',
    'displayName': 'BootStrap Configuration',
    'description': 'Configuration for Bootstrapping',
    'parameters': {
        'implKey': impl_key_dict('service'),
    }
}

###################################################
# TEST SETTINGS
###################################################

TEST_AWS_ADAPTER_1 = {
    'id': 'aws_adapter_configuration_1',
    'displayName': 'AWS Adapter Configuration',
    'description': 'Configuration for AWS Adapter',
    'parameters': {
        'implKey': impl_key_dict('aws_adapter'),
        'cloudFrontPublicKey': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Public Key',
            'description': 'Public key for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_PUBLIC_KEY, 'priority': 1}
            ]
        },
        'cloudFrontPrivateKey': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Private Key',
            'description': 'Private key for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_PRIVATE_KEY, 'priority': 1}
            ]
        },
        'cloudFrontSigningKeypairId': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Signing Keypair ID',
            'description': 'Signing keypair id for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_SIGNING_KEYPAIR_ID, 'priority': 1}
            ]
        },
        'cloudFrontSigningPrivateKeyFile': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Signing Private Key File',
            'description': 'Signing Private Key File for Amazon CloudFront service.',
            'values': [
                {'value': CLOUDFRONT_SIGNING_PRIVATE_KEY_FILE, 'priority': 1}
            ]
        },
        'cloudFrontDistro': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Distro',
            'description': 'CloudFront Distr-o-bution.',
            'values': [
                {'value': CLOUDFRONT_TEST_DISTRO, 'priority': 1}
            ]
        },
        'cloudFrontDistroId': {
            'syntax': 'STRING',
            'displayName': 'CloudFront Distro Id',
            'description': 'CloudFront Distr-o-bution Id.',
            'values': [
                {'value': CLOUDFRONT_TEST_DISTRO_ID, 'priority': 1}
            ]
        },
        'S3PrivateKey': {
            'syntax': 'STRING',
            'displayName': 'S3 Private Key',
            'description': 'Private Key for Amazon S3.',
            'values': [
                {'value': S3_TEST_PRIVATE_KEY, 'priority': 1}
            ]
        },
        'S3PublicKey': {
            'syntax': 'STRING',
            'displayName': 'S3 Public Key',
            'description': 'Public Key for Amazon S3.',
            'values': [
                {'value': S3_TEST_PUBLIC_KEY, 'priority': 1}
            ]
        },
        'S3Bucket': {
            'syntax': 'STRING',
            'displayName': 'S3 Bucket',
            'description': 'Bucket for Amazon S3.',
            'values': [
                {'value': S3_TEST_BUCKET, 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
    }
}

TEST_FILESYSTEM_ADAPTER_1 = {
    'id': 'filesystem_adapter_configuration_1',
    'displayName': 'Filesystem Adapter Configuration',
    'description': 'Configuration for Filesystem Adapter',
    'parameters': {
        'implKey': impl_key_dict('filesystem_adapter'),
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'dataStorePath': {
            'syntax': 'STRING',
            'displayName': 'Path to local filesystem datastore',
            'description': 'Filesystem path for setting the MongoClient host.',
            'values': [
                {'value': TEST_DATA_STORE_PATH, 'priority': 1}  # Mac
            ]
        },
        # 'secondaryDataStorePath': {
        #     'syntax': 'STRING',
        #     'displayName': 'Path to local filesystem datastore',
        #     'description': 'Filesystem path for setting the MongoClient host.',
        #     'values': [
        #         {'value': TEST_STUDENT_RESPONSE_DATA_STORE_PATH, 'priority': 1}  # Mac
        #     ]
        # },
        'dataStoreFullPath': {
            'syntax': 'STRING',
            'displayName': 'Full path to local filesystem datastore',
            'description': 'Filesystem path for setting the JSONClient host.',
            'values': [
                {'value': ABS_PATH, 'priority': 1}
            ]
        },
        'urlHostname': {
            'syntax': 'STRING',
            'displayName': 'Hostname config for serving files over the network',
            'description': 'Hostname config for serving files.',
            'values': [
                {'value': '/api/v1', 'priority': 1}  # Mac
            ]
        },
    }
}

TEST_FILESYSTEM_ADAPTER_2 = {
    'id': 'filesystem_adapter_configuration_2',
    'displayName': 'Filesystem Adapter Configuration',
    'description': 'Configuration for Filesystem Adapter',
    'parameters': {
        'implKey': impl_key_dict('filesystem_adapter'),
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'dataStorePath': {
            'syntax': 'STRING',
            'displayName': 'Path to local filesystem datastore',
            'description': 'Filesystem path for setting the MongoClient host.',
            'values': [
                {'value': TEST_DATA_STORE_PATH, 'priority': 1}  # Mac
            ]
        },
        # 'secondaryDataStorePath': {
        #     'syntax': 'STRING',
        #     'displayName': 'Path to local filesystem datastore',
        #     'description': 'Filesystem path for setting the MongoClient host.',
        #     'values': [
        #         {'value': TEST_STUDENT_RESPONSE_DATA_STORE_PATH, 'priority': 1}  # Mac
        #     ]
        # },
        'dataStoreFullPath': {
            'syntax': 'STRING',
            'displayName': 'Full path to local filesystem datastore',
            'description': 'Filesystem path for setting the JSONClient host.',
            'values': [
                {'value': ABS_PATH, 'priority': 1}
            ]
        },
        'urlHostname': {
            'syntax': 'STRING',
            'displayName': 'Hostname config for serving files over the network',
            'description': 'Hostname config for serving files.',
            'values': [
                {'value': '/api/v1', 'priority': 1}  # Mac
            ]
        },
    }
}

TEST_JSON_1 = {
    'id': 'test_json_configuration_1',
    'displayName': 'Mongo Configuration',
    'description': 'Configuration for Mongo Implementation',
    'parameters': {
        'implKey': impl_key_dict('json'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': 'test_dlkit_', 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': DLKIT_AUTHORITY, 'priority': 1}
            ]
        },
        'mongoHostURI': {
            'syntax': 'STRING',
            'displayName': 'Mongo Host URI',
            'description': 'URI for setting the MongoClient host.',
            'values': [
                {'value': MONGO_HOST_URI, 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'dlkit.records.registry', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'assetContentRecordTypeForFiles': {
            'syntax': 'TYPE',
            'displayName': 'Asset Content Type for Files',
            'description': 'Asset Content Type for Records that store Files in a repository',
            'values': [
                {'value': FILESYSTEM_ASSET_CONTENT_TYPE, 'priority': 1}
            ]
        },
        'magicItemLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic item lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
            ]
        },
        'magicAssessmentPartLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic assessment part lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
    }
}

TEST_JSON_CATALOGING_1 = {
    'id': 'test_json_cataloging_configuration_1',
    'displayName': 'JSON Configuration',
    'description': 'Configuration for JSON Implementation',
    'parameters': {
        'implKey': impl_key_dict('json'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': 'test_dlkit_', 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': DLKIT_AUTHORITY, 'priority': 1}
            ]
        },
        'mongoHostURI': {
            'syntax': 'STRING',
            'displayName': 'Mongo Host URI',
            'description': 'URI for setting the MongoClient host.',
            'values': [
                {'value': MONGO_HOST_URI, 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'dlkit.records.registry', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'assetContentRecordTypeForFiles': {
            'syntax': 'TYPE',
            'displayName': 'Asset Content Type for Files',
            'description': 'Asset Content Type for Records that store Files in a repository',
            'values': [
                {'value': FILESYSTEM_ASSET_CONTENT_TYPE, 'priority': 1}
            ]
        },
        'magicItemLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic item lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
            ]
        },
        'magicAssessmentPartLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic assessment part lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'useCachingForQualifierIds': {
            'syntax': 'BOOLEAN',
            'displayName': 'Flag to use memcached for authz qualifier_ids or not',
            'description': 'Flag to use memcached for authz qualifier_ids or not',
            'values': [
                {'value': True, 'priority': 1}
            ]
        },
        'repositoryCatalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Provider implementation for cataloging service',
            'description': 'Provider implementation for cataloging service',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessmentCatalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Provider implementation for cataloging service',
            'description': 'Provider implementation for cataloging service',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringCatalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Provider implementation for cataloging service',
            'description': 'Provider implementation for cataloging service',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
    }
}

TEST_JSON_AWS_1 = {
    'id': 'test_json_aws_configuration_1',
    'displayName': 'JSON Configuration',
    'description': 'Configuration for JSON Implementation',
    'parameters': {
        'implKey': impl_key_dict('json'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': 'test_dlkit_', 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': DLKIT_AUTHORITY, 'priority': 1}
            ]
        },
        'mongoHostURI': {
            'syntax': 'STRING',
            'displayName': 'Mongo Host URI',
            'description': 'URI for setting the MongoClient host.',
            'values': [
                {'value': MONGO_HOST_URI, 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'dlkit.records.registry', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_AWS_ADAPTER_1', 'priority': 1}
            ]
        },
        'assetContentRecordTypeForFiles': {
            'syntax': 'TYPE',
            'displayName': 'Asset Content Type for Files',
            'description': 'Asset Content Type for Records that store Files in a repository',
            'values': [
                {'value': AWS_ASSET_CONTENT_TYPE, 'priority': 1}
            ]
        },
        'magicItemLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic item lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
            ]
        },
        'magicAssessmentPartLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic assessment part lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
    }
}

TEST_JSON_FILESYSTEM_1 = {
    'id': 'test_json_filesystem_configuration_1',
    'displayName': 'JSON Configuration',
    'description': 'Configuration for JSON Implementation',
    'parameters': {
        'implKey': impl_key_dict('json'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': 'test_dlkit_', 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': DLKIT_AUTHORITY, 'priority': 1}
            ]
        },
        'indexes': {
            'syntax': 'OBJECT',
            'displayName': 'Mongo DB Indexes',
            'description': 'Indexes to set in MongoDB',
            'values': [
                {'value': DLKIT_MONGO_DB_INDEXES, 'priority': 1}
            ]
        },
        'mongoHostURI': {
            'syntax': 'STRING',
            'displayName': 'Mongo Host URI',
            'description': 'URI for setting the MongoClient host.',
            'values': [
                {'value': MONGO_HOST_URI, 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_2', 'priority': 1}
            ]
        },
        'assetContentRecordTypeForFiles': {
            'syntax': 'TYPE',
            'displayName': 'Asset Content Type for Files',
            'description': 'Asset Content Type for Records that store Files in a repository',
            'values': [
                {'value': FILESYSTEM_ASSET_CONTENT_TYPE, 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'dlkit.records.registry', 'priority': 1}
            ]
        },
        'magicItemLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic item lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
            ]
        },
        'magicAssessmentPartLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic assessment part lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'useCachingForQualifierIds': {
            'syntax': 'BOOLEAN',
            'displayName': 'Flag to use memcached for authz qualifier_ids or not',
            'description': 'Flag to use memcached for authz qualifier_ids or not',
            'values': [
                {'value': True, 'priority': 1}
            ]
        },
        'useFilesystem': {
            'syntax': 'BOOLEAN',
            'displayName': 'Use the filesystem instead of MongoDB',
            'description': 'Use the filesystem instead of MongoDB',
            'values': [
                {'value': True, 'priority': 1}
            ]
        },
        'dataStorePath': {
            'syntax': 'STRING',
            'displayName': 'Path to local filesystem datastore',
            'description': 'Filesystem path for setting the MongoClient host.',
            'values': [
                {'value': TEST_DATA_STORE_PATH, 'priority': 1}
            ]
        },
        'dataStoreFullPath': {
            'syntax': 'STRING',
            'displayName': 'Full path to local filesystem datastore',
            'description': 'Filesystem path for setting the MongoClient host.',
            'values': [
                {'value': ABS_PATH, 'priority': 1}
            ]
        },
    }
}


TEST_JSON_MEMCACHE_1 = {
    'id': 'test_json_memcache_configuration_1',
    'displayName': 'Mongo Configuration',
    'description': 'Configuration for Mongo Implementation',
    'parameters': {
        'implKey': impl_key_dict('json'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': 'test_dlkit_', 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': DLKIT_AUTHORITY, 'priority': 1}
            ]
        },
        'mongoHostURI': {
            'syntax': 'STRING',
            'displayName': 'Mongo Host URI',
            'description': 'URI for setting the MongoClient host.',
            'values': [
                {'value': MONGO_HOST_URI, 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'dlkit.records.registry', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'assetContentRecordTypeForFiles': {
            'syntax': 'TYPE',
            'displayName': 'Asset Content Type for Files',
            'description': 'Asset Content Type for Records that store Files in a repository',
            'values': [
                {'value': FILESYSTEM_ASSET_CONTENT_TYPE, 'priority': 1}
            ]
        },
        'magicItemLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic item lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.multi_choice_questions.randomized_questions.RandomizedMCItemLookupSession', 'priority': 1}
            ]
        },
        'magicAssessmentPartLookupSessions': {
            'syntax': 'STRING',
            'displayName': 'Which magic assessment part lookup sessions to try',
            'description': 'To handle magic IDs.',
            'values': [
                {'value': 'dlkit.records.adaptive.magic_parts.assessment_part_records.MagicAssessmentPartLookupSession', 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'useCachingForQualifierIds': {
            'syntax': 'BOOLEAN',
            'displayName': 'Flag to use memcached for authz qualifier_ids or not',
            'description': 'Flag to use memcached for authz qualifier_ids or not',
            'values': [
                {'value': True, 'priority': 1}
            ]
        },
        'cachingEngine': {
            'syntax': 'STRING',
            'displayName': 'Flag to configure the caching engine',
            'description': 'Flag to configure the caching engine',
            'values': [
                {'value': 'memcache', 'priority': 1}
            ]
        },
    }
}


ALWAYS_AUTHZ = {
    'id': 'always_authz_impl',
    'displayName': 'Always Authz Impl Configuration',
    'description': 'Configuration for Always True Authorization Impl',
    'parameters': {
        'implKey': impl_key_dict('always_authz'),
    }
}

NEVER_AUTHZ = {
    'id': 'never_authz_impl',
    'displayName': 'Never Authz Impl Configuration',
    'description': 'Configuration for Never True Authorization Impl',
    'parameters': {
        'implKey': impl_key_dict('never_authz'),
    }
}

TEST_AUTHZ_ADAPTER_1 = {
    'id': 'authz_adapter_configuration_1',
    'displayName': 'AuthZ Adapter Configuration',
    'description': 'Configuration for AuthZ Adapter',
    'parameters': {
        'implKey': impl_key_dict('authz_adapter'),
        'authzAuthorityImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'ALWAYS_AUTHZ', 'priority': 1}
            ]
        },
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
    }
}

TEST_AUTHZ_ADAPTER_2 = {
    'id': 'authz_adapter_configuration_2',
    'displayName': 'AuthZ Adapter Configuration',
    'description': 'Configuration for AuthZ Adapter',
    'parameters': {
        'implKey': impl_key_dict('authz_adapter'),
        'authzAuthorityImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'NEVER_AUTHZ', 'priority': 1}
            ]
        },
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
    }
}

TEST_AUTHZ_ADAPTER_3 = {
    'id': 'authz_adapter_configuration_3',
    'displayName': 'AuthZ Adapter Configuration',
    'description': 'Configuration for AuthZ Adapter',
    'parameters': {
        'implKey': impl_key_dict('authz_adapter'),
        'authzAuthorityImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_1', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_CATALOGING = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_CATALOGING_1', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_ALWAYS_AUTHZ = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_NEVER_AUTHZ = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_2', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_JSON_AUTHZ = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_3', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_FUNCTIONAL = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_AUTHZ_ADAPTER_1', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_AWS = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_AWS_ADAPTER_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_AWS_1', 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_HANDCAR = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': HANDCAR_IMPL, 'priority': 1}
            ]
        },
        'typeProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Type Provider Implementation',
            'description': 'Implementation for type service provider',
            'values': [
                {'value': HANDCAR_IMPL, 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': HANDCAR_IMPL, 'priority': 1}
            ]
        },
    }
}

TEST_SERVICE_FILESYSTEM = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_FILESYSTEM_ADAPTER_2', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_JSON_FILESYSTEM_1', 'priority': 1}
            ]
        },
    }
}


TEST_SERVICE_MEMCACHE = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'learningProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Learning Provider Implementation',
            'description': 'Implementation for learning service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'repositoryProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Repository Provider Implementation',
            'description': 'Implementation for repository service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'commentingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Commenting Provider Implementation',
            'description': 'Implementation for commenting service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'resourceProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Resource Provider Implementation',
            'description': 'Implementation for resource service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'gradingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Grading Provider Implementation',
            'description': 'Implementation for grading provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'loggingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Logging Provider Implementation',
            'description': 'Implementation for logging provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
        'catalogingProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Cataloging Provider Implementation',
            'description': 'Implementation for cataloging service provider',
            'values': [
                {'value': 'TEST_JSON_MEMCACHE_1', 'priority': 1}
            ]
        },
    }
}
