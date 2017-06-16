"""Unit tests of assessment.authoring searches."""


import unittest


class TestAssessmentPartSearch(unittest.TestCase):
    """Tests for AssessmentPartSearch"""

    def test_search_among_assessment_parts(self):
        """Tests search_among_assessment_parts"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_assessment_parts(True)

    def test_order_assessment_part_results(self):
        """Tests order_assessment_part_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_assessment_part_results(True)

    def test_get_assessment_part_search_record(self):
        """Tests get_assessment_part_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_assessment_part_search_record(True)


class TestAssessmentPartSearchResults(unittest.TestCase):
    """Tests for AssessmentPartSearchResults"""

    def test_get_assessment_parts(self):
        """Tests get_assessment_parts"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_assessment_parts()

    def test_get_assessment_part_query_inspector(self):
        """Tests get_assessment_part_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_assessment_part_query_inspector()

    def test_get_assessment_part_search_results_record(self):
        """Tests get_assessment_part_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_assessment_part_search_results_record(True)


class TestSequenceRuleSearch(unittest.TestCase):
    """Tests for SequenceRuleSearch"""

    def test_search_among_sequence_rules(self):
        """Tests search_among_sequence_rules"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.search_among_sequence_rules(True)

    def test_order_sequence_rule_results(self):
        """Tests order_sequence_rule_results"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.order_sequence_rule_results(True)

    def test_get_sequence_rule_search_record(self):
        """Tests get_sequence_rule_search_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_sequence_rule_search_record(True)


class TestSequenceRuleSearchResults(unittest.TestCase):
    """Tests for SequenceRuleSearchResults"""

    def test_get_sequence_rules(self):
        """Tests get_sequence_rules"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_sequence_rules()

    def test_get_sequence_rule_query_inspector(self):
        """Tests get_sequence_rule_query_inspector"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_sequence_rule_query_inspector()

    def test_get_sequence_rule_search_results_record(self):
        """Tests get_sequence_rule_search_results_record"""
        with self.assertRaises(errors.Unimplemented):
            self.searche.get_sequence_rule_search_results_record(True)
