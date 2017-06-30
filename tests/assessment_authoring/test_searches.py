"""Unit tests of assessment.authoring searches."""


import pytest


from ..utilities.general import is_never_authz, is_no_authz


@pytest.mark.usefixtures("assessment_part_search_class_fixture", "assessment_part_search_test_fixture")
class TestAssessmentPartSearch(object):
    """Tests for AssessmentPartSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_assessment_parts(self):
        """Tests search_among_assessment_parts"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_assessment_part_results(self):
        """Tests order_assessment_part_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_part_search_record(self):
        """Tests get_assessment_part_search_record"""
        pass


@pytest.mark.usefixtures("assessment_part_search_results_class_fixture", "assessment_part_search_results_test_fixture")
class TestAssessmentPartSearchResults(object):
    """Tests for AssessmentPartSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_parts(self):
        """Tests get_assessment_parts"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_part_query_inspector(self):
        """Tests get_assessment_part_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_assessment_part_search_results_record(self):
        """Tests get_assessment_part_search_results_record"""
        pass


@pytest.mark.usefixtures("sequence_rule_search_class_fixture", "sequence_rule_search_test_fixture")
class TestSequenceRuleSearch(object):
    """Tests for SequenceRuleSearch"""
    @pytest.mark.skip('unimplemented test')
    def test_search_among_sequence_rules(self):
        """Tests search_among_sequence_rules"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_order_sequence_rule_results(self):
        """Tests order_sequence_rule_results"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rule_search_record(self):
        """Tests get_sequence_rule_search_record"""
        pass


@pytest.mark.usefixtures("sequence_rule_search_results_class_fixture", "sequence_rule_search_results_test_fixture")
class TestSequenceRuleSearchResults(object):
    """Tests for SequenceRuleSearchResults"""
    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rules(self):
        """Tests get_sequence_rules"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rule_query_inspector(self):
        """Tests get_sequence_rule_query_inspector"""
        pass

    @pytest.mark.skip('unimplemented test')
    def test_get_sequence_rule_search_results_record(self):
        """Tests get_sequence_rule_search_results_record"""
        pass
