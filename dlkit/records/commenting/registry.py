from ..osid import registry as osid_registry

COMMENT_RECORD_TYPES = {
    'file-comment': {
        'authority': 'ODL.MIT.EDU',
        'namespace': 'comment-type',
        'identifier': 'file-comment',
        'display_name': 'File Comment',
        'display_label': 'File Comment',
        'description': 'Comment via file',
        'domain': 'commenting.Comment',
        'module_path': 'dlkit.records.commenting.basic.file_comment_records',
        'object_record_class_name': 'FileCommentRecord',
        'form_record_class_name': 'FileCommentFormRecord'
    }
}

COMMENT_RECORD_TYPES.update(osid_registry.__dict__.get('OSID_OBJECT_RECORD_TYPES', {}))
