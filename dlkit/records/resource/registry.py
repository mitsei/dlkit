from ..osid import registry as osid_registry

RESOURCE_RECORD_TYPES = {
}

RESOURCE_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))

BIN_RECORD_TYPES = {
}

BIN_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))
