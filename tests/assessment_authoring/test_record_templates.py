"""Unit tests of assessment.authoring records."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz, uses_cataloging, uses_filesystem_only


@pytest.mark.usefixtures("assessment_part_record_class_fixture", "assessment_part_record_test_fixture")
class TestAssessmentPartRecord(object):
    """Tests for AssessmentPartRecord"""


@pytest.mark.usefixtures("assessment_part_query_record_class_fixture", "assessment_part_query_record_test_fixture")
class TestAssessmentPartQueryRecord(object):
    """Tests for AssessmentPartQueryRecord"""


@pytest.mark.usefixtures("assessment_part_form_record_class_fixture", "assessment_part_form_record_test_fixture")
class TestAssessmentPartFormRecord(object):
    """Tests for AssessmentPartFormRecord"""


@pytest.mark.usefixtures("assessment_part_search_record_class_fixture", "assessment_part_search_record_test_fixture")
class TestAssessmentPartSearchRecord(object):
    """Tests for AssessmentPartSearchRecord"""


@pytest.mark.usefixtures("sequence_rule_record_class_fixture", "sequence_rule_record_test_fixture")
class TestSequenceRuleRecord(object):
    """Tests for SequenceRuleRecord"""


@pytest.mark.usefixtures("sequence_rule_query_record_class_fixture", "sequence_rule_query_record_test_fixture")
class TestSequenceRuleQueryRecord(object):
    """Tests for SequenceRuleQueryRecord"""


@pytest.mark.usefixtures("sequence_rule_form_record_class_fixture", "sequence_rule_form_record_test_fixture")
class TestSequenceRuleFormRecord(object):
    """Tests for SequenceRuleFormRecord"""


@pytest.mark.usefixtures("sequence_rule_search_record_class_fixture", "sequence_rule_search_record_test_fixture")
class TestSequenceRuleSearchRecord(object):
    """Tests for SequenceRuleSearchRecord"""
