from ...osid.base_records import TextFormRecord, TextRecord


class TextBlobLogEntryRecord(TextRecord):
    """log entries that consist of a text blob only"""
    _implemented_record_type_identifiers = [
        'text-blob'
    ]


class TextBlobLogEntryFormRecord(TextFormRecord):
    """log entries that consist of a text blob only"""
    _implemented_record_type_identifiers = [
        'text-blob'
    ]
