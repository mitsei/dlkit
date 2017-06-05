"""Unit tests of assessment.authoring queries."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAssessmentPartQuery(unittest.TestCase):
    """Tests for AssessmentPartQuery"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_part_list = list()
        cls.assessment_part_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        assessment_form = cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(assessment_form)

    def setUp(self):
        self.query = self.catalog.get_assessment_part_query()

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assessmentId'], {
            '$in': [str(test_id)]
        })

    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_assessment_id(test_id, match=True)
        self.assertIn('assessmentId',
                      self.query._query_terms)
        self.query.clear_assessment_id_terms()
        self.assertNotIn('assessmentId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        pass

    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['assessment'] = 'foo'
        self.query.clear_assessment_terms()
        self.assertNotIn('assessment',
                         self.query._query_terms)

    def test_match_parent_assessment_part_id(self):
        """Tests match_parent_assessment_part_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_parent_assessment_part_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['parentAssessmentPartId'], {
            '$in': [str(test_id)]
        })

    def test_clear_parent_assessment_part_id_terms(self):
        """Tests clear_parent_assessment_part_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_parent_assessment_part_id(test_id, match=True)
        self.assertIn('parentAssessmentPartId',
                      self.query._query_terms)
        self.query.clear_parent_assessment_part_id_terms()
        self.assertNotIn('parentAssessmentPartId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_parent_assessment_part_query(self):
        """Tests supports_parent_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_assessment_part_query(self):
        """Tests get_parent_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_parent_assessment_part(self):
        """Tests match_any_parent_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_parent_assessment_part_terms(self):
        """Tests clear_parent_assessment_part_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_section(self):
        """Tests match_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_section_terms(self):
        """Tests clear_section_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_weight(self):
        """Tests match_weight"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_weight(self):
        """Tests match_any_weight"""
        pass

    def test_clear_weight_terms(self):
        """Tests clear_weight_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['weight'] = 'foo'
        self.query.clear_weight_terms()
        self.assertNotIn('weight',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_match_allocated_time(self):
        """Tests match_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_allocated_time(self):
        """Tests match_any_allocated_time"""
        pass

    def test_clear_allocated_time_terms(self):
        """Tests clear_allocated_time_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['allocatedTime'] = 'foo'
        self.query.clear_allocated_time_terms()
        self.assertNotIn('allocatedTime',
                         self.query._query_terms)

    def test_match_child_assessment_part_id(self):
        """Tests match_child_assessment_part_id"""
        # From test_templates/resource.py::ResourceQuery::match_avatar_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_child_assessment_part_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['childAssessmentPartId'], {
            '$in': [str(test_id)]
        })

    def test_clear_child_assessment_part_id_terms(self):
        """Tests clear_child_assessment_part_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_avatar_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_child_assessment_part_id(test_id, match=True)
        self.assertIn('childAssessmentPartId',
                      self.query._query_terms)
        self.query.clear_child_assessment_part_id_terms()
        self.assertNotIn('childAssessmentPartId',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_child_assessment_part_query(self):
        """Tests supports_child_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_assessment_part_query(self):
        """Tests get_child_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_child_assessment_part(self):
        """Tests match_any_child_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_child_assessment_part_terms(self):
        """Tests clear_child_assessment_part_terms"""
        pass

    def test_match_bank_id(self):
        """Tests match_bank_id"""
        # From test_templates/resource.py::ResourceQuery::match_bin_id_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertEqual(self.query._query_terms['assignedBankIds'], {
            '$in': [str(test_id)]
        })

    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_bin_id_terms_template
        test_id = Id('osid.Osid%3Afake%40ODL.MIT.EDU')
        self.query.match_bank_id(test_id, match=True)
        self.assertIn('assignedBankIds',
                      self.query._query_terms)
        self.query.clear_bank_id_terms()
        self.assertNotIn('assignedBankIds',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        # From test_templates/resource.py::ResourceQuery::clear_group_terms_template
        self.query._query_terms['bank'] = 'foo'
        self.query.clear_bank_terms()
        self.assertNotIn('bank',
                         self.query._query_terms)

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_query_record(self):
        """Tests get_assessment_part_query_record"""
        pass


class TestSequenceRuleQuery(unittest.TestCase):
    """Tests for SequenceRuleQuery"""

    @unittest.skip('unimplemented test')
    def test_match_assessment_part_id(self):
        """Tests match_assessment_part_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_part_id_terms(self):
        """Tests clear_assessment_part_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_part_query(self):
        """Tests supports_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_query(self):
        """Tests get_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_part_terms(self):
        """Tests clear_assessment_part_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_next_assessment_part_id(self):
        """Tests match_next_assessment_part_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_next_assessment_part_id_terms(self):
        """Tests clear_next_assessment_part_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_next_assessment_part_query(self):
        """Tests supports_next_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_part_query(self):
        """Tests get_next_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_next_assessment_part_terms(self):
        """Tests clear_next_assessment_part_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_score(self):
        """Tests match_minimum_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_minimum_score(self):
        """Tests match_any_minimum_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_score_terms(self):
        """Tests clear_minimum_score_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_maximum_score(self):
        """Tests match_maximum_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_maximum_score(self):
        """Tests match_any_maximum_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_maximum_score_terms(self):
        """Tests clear_maximum_score_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_cumulative(self):
        """Tests match_cumulative"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_cumulative_terms(self):
        """Tests clear_cumulative_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_applied_assessment_part_id(self):
        """Tests match_applied_assessment_part_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_applied_assessment_part_id_terms(self):
        """Tests clear_applied_assessment_part_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_applied_assessment_part_query(self):
        """Tests supports_applied_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_applied_assessment_part_query(self):
        """Tests get_applied_assessment_part_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_applied_assessment_part(self):
        """Tests match_any_applied_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_applied_assessment_part_terms(self):
        """Tests clear_applied_assessment_part_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_bank_id(self):
        """Tests match_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_id_terms(self):
        """Tests clear_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_bank_query(self):
        """Tests supports_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_bank_terms(self):
        """Tests clear_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_sequence_rule_query_record(self):
        """Tests get_sequence_rule_query_record"""
        pass
