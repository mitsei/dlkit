from ...osid.base_records import FileRecord, FileFormRecord


class FileCommentRecord(FileRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'file-comment'
    ]


class FileCommentFormRecord(FileFormRecord):
    """
    # This is really only a marker implementation to indicate that a
    # file submission response will be required
    """
    _implemented_record_type_identifiers = [
        'file-comment'
    ]
