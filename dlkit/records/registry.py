from .assessment import registry as assessment_registry
from .commenting import registry as commenting_registry
from .adaptive import registry as adaptive_registry
from .logging import registry as logging_registry
from .osid import registry as osid_registry
from .repository import registry as repository_registry
from .resource import registry as resource_registry

# ASSESSMENT
ANSWER_GENUS_TYPES = assessment_registry.__dict__.get('ANSWER_GENUS_TYPES', {})
ANSWER_RECORD_TYPES = assessment_registry.__dict__.get('ANSWER_RECORD_TYPES', {})
ASSESSMENT_GENUS_TYPES = assessment_registry.__dict__.get('ASSESSMENT_GENUS_TYPES', {})
ASSESSMENT_RECORD_TYPES = assessment_registry.__dict__.get('ASSESSMENT_RECORD_TYPES', {})
ASSESSMENT_OFFERED_GENUS_TYPES = assessment_registry.__dict__.get('ASSESSMENT_OFFERED_GENUS_TYPES', {})
ASSESSMENT_OFFERED_RECORD_TYPES = assessment_registry.__dict__.get('ASSESSMENT_OFFERED_RECORD_TYPES', {})
ASSESSMENT_PART_GENUS_TYPES = assessment_registry.__dict__.get('ASSESSMENT_PART_GENUS_TYPES', {})
ASSESSMENT_PART_GENUS_TYPES.update(adaptive_registry.__dict__.get('ASSESSMENT_PART_GENUS_TYPES', {}))
ASSESSMENT_PART_RECORD_TYPES = assessment_registry.__dict__.get('ASSESSMENT_PART_RECORD_TYPES', {})
ASSESSMENT_PART_RECORD_TYPES.update(adaptive_registry.__dict__.get('ASSESSMENT_PART_RECORD_TYPES', {}))
ASSESSMENT_SECTION_RECORD_TYPES = assessment_registry.__dict__.get('ASSESSMENT_SECTION_RECORD_TYPES', {})
ASSESSMENT_TAKEN_GENUS_TYPES = assessment_registry.__dict__.get('ASSESSMENT_TAKEN_GENUS_TYPES', {})
ASSESSMENT_TAKEN_RECORD_TYPES = assessment_registry.__dict__.get('ASSESSMENT_TAKEN_RECORD_TYPES', {})
BANK_GENUS_TYPES = assessment_registry.__dict__.get('BANK_GENUS_TYPES', {})
BANK_RECORD_TYPES = assessment_registry.__dict__.get('BANK_RECORD_TYPES', {})
ITEM_GENUS_TYPES = assessment_registry.__dict__.get('ITEM_GENUS_TYPES', {})
ITEM_RECORD_TYPES = assessment_registry.__dict__.get('ITEM_RECORD_TYPES', {})
ITEM_RECORD_TYPES.update(adaptive_registry.__dict__.get('ITEM_RECORD_TYPES', {}))
QUESTION_GENUS_TYPES = assessment_registry.__dict__.get('QUESTION_GENUS_TYPES', {})
QUESTION_RECORD_TYPES = assessment_registry.__dict__.get('QUESTION_RECORD_TYPES', {})
QUESTION_RECORD_TYPES.update(adaptive_registry.__dict__.get('QUESTION_RECORD_TYPES', {}))
RESPONSE_GENUS_TYPES = assessment_registry.__dict__.get('RESPONSE_GENUS_TYPES', {})
RESPONSE_RECORD_TYPES = assessment_registry.__dict__.get('RESPONSE_RECORD_TYPES', {})


# COMMENTING
COMMENT_GENUS_TYPES = commenting_registry.__dict__.get('COMMENT_GENUS_TYPES', {})
COMMENT_RECORD_TYPES = commenting_registry.__dict__.get('COMMENT_RECORD_TYPES', {})

# LOGGING
LOG_ENTRY_RECORD_TYPES = logging_registry.__dict__.get('LOG_ENTRY_RECORD_TYPES', {})

# OSID
OSID_OBJECT_GENUS_TYPES = osid_registry.__dict__.get('OSID_OBJECT_GENUS_TYPES', {})
OSID_OBJECT_RECORD_TYPES = osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {})

# REPOSITORY
ASSET_CONTENT_GENUS_TYPES = repository_registry.__dict__.get('ASSET_CONTENT_GENUS_TYPES', {})
ASSET_CONTENT_RECORD_TYPES = repository_registry.__dict__.get('ASSET_CONTENT_RECORD_TYPES', {})
ASSET_GENUS_TYPES = repository_registry.__dict__.get('ASSET_GENUS_TYPES', {})
ASSET_RECORD_TYPES = repository_registry.__dict__.get('ASSET_RECORD_TYPES', {})
COMPOSITION_GENUS_TYPES = repository_registry.__dict__.get('COMPOSITION_GENUS_TYPES', {})
COMPOSITION_RECORD_TYPES = repository_registry.__dict__.get('COMPOSITION_RECORD_TYPES', {})
REPOSITORY_GENUS_TYPES = repository_registry.__dict__.get('REPOSITORY_GENUS_TYPES', {})
REPOSITORY_RECORD_TYPES = repository_registry.__dict__.get('REPOSITORY_RECORD_TYPES', {})

# RESOURCE
BIN_RECORD_TYPES = resource_registry.__dict__.get('BIN_RECORD_TYPES', {})
RESOURCE_RECORD_TYPES = resource_registry.__dict__.get('RESOURCE_RECORD_TYPES', {})
