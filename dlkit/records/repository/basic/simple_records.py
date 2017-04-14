"""
records.repository.basic.simple_records.py
"""

from dlkit.abstract_osid.assessment import record_templates as abc_assessment_records

from ...osid.base_records import TextFormRecord, TextRecord


class AssetContentTextRecord(TextRecord, abc_assessment_records.ItemRecord):
    """asset content with text"""
    _implemented_record_type_identifiers = [
        'asset-content-text'
    ]


class AssetContentTextFormRecord(TextFormRecord, abc_assessment_records.ItemFormRecord):
    """form for asset content with text"""
    _implemented_record_type_identifiers = [
        'asset-content-text'
    ]
