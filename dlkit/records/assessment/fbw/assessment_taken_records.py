"""
records.assessment.fbw.assessment_taken_records.py
"""
from ...osid.base_records import QueryInitRecord,\
    ObjectInitRecord


class AdvancedQueryAssessmentTakenRecord(ObjectInitRecord):
    """No new methods on the taken record"""
    _implemented_record_type_identifiers = [
        'advanced-query'
    ]


class AdvancedQueryAssessmentTakenFormRecord(ObjectInitRecord):
    """No new methods on the form reqcord"""
    _implemented_record_type_identifiers = [
        'advanced-query'
    ]


class AdvancedQueryAssessmentTakenQueryRecord(QueryInitRecord):
    """add some advanced query options"""
    def match_start_time(self, start_time, match):
        if match:
            inin = '$gte'
        else:
            inin = '$lte'

        self._my_osid_query._query_terms['actualStartTime'] = {inin: start_time}

    def clear_match_start_time(self):
        self._my_osid_query._clear_terms('actualStartTime')
