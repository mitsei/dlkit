from ..osid import registry as osid_registry

LOG_ENTRY_RECORD_TYPES = {
    'text-blob': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'logging.LogEntry',
        'identifier': 'text-blob',
        'display_name': 'Text Blob Log Entry',
        'display_label': 'Text Blob Log Entry',
        'description': 'Text Blob Log Entry',
        'domain': 'logging.LogEntry',
        'module_path': 'dlkit.records.logging.clix.text_blob',
        'object_record_class_name': 'TextBlobLogEntryRecord',
        'form_record_class_name': 'TextBlobLogEntryFormRecord'},
}

LOG_ENTRY_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))
