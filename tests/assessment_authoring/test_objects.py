"""Unit tests of assessment.authoring objects."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAssessmentPart(unittest.TestCase):
    """Tests for AssessmentPart"""

    @unittest.skip('unimplemented test')
    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment(self):
        """Tests get_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_parent_part(self):
        """Tests has_parent_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_id(self):
        """Tests get_assessment_part_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_section(self):
        """Tests is_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_weight(self):
        """Tests get_weight"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_allocated_time(self):
        """Tests get_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_assessment_part_ids(self):
        """Tests get_child_assessment_part_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_assessment_parts(self):
        """Tests get_child_assessment_parts"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_record(self):
        """Tests get_assessment_part_record"""
        pass


class TestAssessmentPartForm(unittest.TestCase):
    """Tests for AssessmentPartForm"""

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

        cls.form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident,
                                                                                  [])

        cls.assessment = cls.catalog.get_assessment(cls.assessment.ident)

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_weight_metadata(self):
        """Tests get_weight_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_weight_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_weight(self):
        """Tests set_weight"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_weight(self):
        """Tests clear_weight"""
        pass

    def test_get_allocated_time_metadata(self):
        """Tests get_allocated_time_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_allocated_time_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_allocated_time(self):
        """Tests set_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_allocated_time(self):
        """Tests clear_allocated_time"""
        pass

    def test_get_assessment_part_form_record(self):
        """Tests get_assessment_part_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_assessment_part_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssessmentPartList(unittest.TestCase):
    """Tests for AssessmentPartList"""

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_part(self):
        """Tests get_next_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_parts(self):
        """Tests get_next_assessment_parts"""
        pass


class TestSequenceRule(unittest.TestCase):
    """Tests for SequenceRule"""

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_id(self):
        """Tests get_assessment_part_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_part_id(self):
        """Tests get_next_assessment_part_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_part(self):
        """Tests get_next_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_minimum_score(self):
        """Tests get_minimum_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_maximum_score(self):
        """Tests get_maximum_score"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_cumulative(self):
        """Tests is_cumulative"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_applied_assessment_part_ids(self):
        """Tests get_applied_assessment_part_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_applied_assessment_parts(self):
        """Tests get_applied_assessment_parts"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_sequence_rule_record(self):
        """Tests get_sequence_rule_record"""
        pass


class TestSequenceRuleForm(unittest.TestCase):
    """Tests for SequenceRuleForm"""

    @classmethod
    def setUpClass(cls):
        cls.sequence_rule_list = list()
        cls.sequence_rule_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleLookupSession tests'
        cls.assessment_part_1 = cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleLookupSession tests'
        cls.assessment_part_2 = cls.catalog.create_assessment_part_for_assessment(create_form)

        cls.form = cls.catalog.get_sequence_rule_form_for_create(cls.assessment_part_1.ident,
                                                                 cls.assessment_part_2.ident,
                                                                 [])

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessment_parts():
                catalog.delete_assessment_part(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_minimum_score_metadata(self):
        """Tests get_minimum_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_minimum_score_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_minimum_score(self):
        """Tests set_minimum_score"""
        pass

    def test_get_maximum_score_metadata(self):
        """Tests get_maximum_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_maximum_score_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_maximum_score(self):
        """Tests set_maximum_score"""
        pass

    def test_get_cumulative_metadata(self):
        """Tests get_cumulative_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_cumulative_metadata(), Metadata))

    def test_set_cumulative(self):
        """Tests set_cumulative"""
        create_form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                     self.assessment_part_2.ident,
                                                                     [])
        create_form.set_cumulative(True)
        self.assertTrue(create_form._my_map['cumulative'])

    @unittest.skip('unimplemented test')
    def test_get_applied_assessment_parts_metadata(self):
        """Tests get_applied_assessment_parts_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_apply_assessment_parts(self):
        """Tests apply_assessment_parts"""
        pass

    def test_get_sequence_rule_form_record(self):
        """Tests get_sequence_rule_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_sequence_rule_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestSequenceRuleList(unittest.TestCase):
    """Tests for SequenceRuleList"""

    @unittest.skip('unimplemented test')
    def test_get_next_sequence_rule(self):
        """Tests get_next_sequence_rule"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_sequence_rules(self):
        """Tests get_next_sequence_rules"""
        pass
