"""Unit tests of assessment.authoring objects."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
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
        create_form.description = 'Test Bank for AssessmentPartForm tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        assessment_form = cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartForm tests'
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

    def test_set_allocated_time(self):
        """Tests set_allocated_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_duration_template
        test_duration = Duration(hours=1)
        self.assertIsNone(self.form._my_map['allocatedTime'])
        self.form.set_allocated_time(test_duration)
        self.assertEqual(self.form._my_map['allocatedTime']['seconds'], 3600)
        self.assertEqual(self.form._my_map['allocatedTime']['days'], 0)
        self.assertEqual(self.form._my_map['allocatedTime']['microseconds'], 0)
        # reset this for other tests
        self.form._my_map['allocatedTime'] = None

    def test_clear_allocated_time(self):
        """Tests clear_allocated_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::clear_duration_template
        test_duration = Duration(hours=1)
        self.assertIsNone(self.form._my_map['allocatedTime'])
        self.form.set_allocated_time(test_duration)
        self.assertEqual(self.form._my_map['allocatedTime']['seconds'], 3600)
        self.assertEqual(self.form._my_map['allocatedTime']['days'], 0)
        self.assertEqual(self.form._my_map['allocatedTime']['microseconds'], 0)
        self.form.clear_allocated_time()
        self.assertIsNone(self.form._my_map['allocatedTime'])

    def test_get_assessment_part_form_record(self):
        """Tests get_assessment_part_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_assessment_part_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssessmentPartList(unittest.TestCase):
    """Tests for AssessmentPartList"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_part_list = list()
        cls.assessment_part_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        assessment_form = cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartList tests'
        cls.assessment = cls.catalog.create_assessment(assessment_form)

        cls.form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident,
                                                                                  [])

    def setUp(self):
        from dlkit.json_.assessment_authoring.objects import AssessmentPartList
        self.assessment_part_list = list()
        self.assessment_part_ids = list()

        for num in [0, 1]:
            form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident, [])

            obj = self.catalog.create_assessment_part_for_assessment(form)

            self.assessment_part_list.append(obj)
            self.assessment_part_ids.append(obj.ident)
        self.assessment_part_list = AssessmentPartList(self.assessment_part_list)

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_assessment_part(self):
        """Tests get_next_assessment_part"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        self.assertTrue(isinstance(self.assessment_part_list.get_next_assessment_part(), AssessmentPart))

    def test_get_next_assessment_parts(self):
        """Tests get_next_assessment_parts"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList, AssessmentPart
        new_list = self.assessment_part_list.get_next_assessment_parts(2)
        self.assertTrue(isinstance(new_list, AssessmentPartList))
        for item in new_list:
            self.assertTrue(isinstance(item, AssessmentPart))


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
        create_form.description = 'Test Bank for SequenceRuleForm tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleForm tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleForm tests'
        cls.assessment_part_1 = cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleForm tests'
        cls.assessment_part_2 = cls.catalog.create_assessment_part_for_assessment(create_form)

        cls.form = cls.catalog.get_sequence_rule_form_for_create(cls.assessment_part_1.ident,
                                                                 cls.assessment_part_2.ident,
                                                                 [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessment_parts():
            cls.catalog.delete_assessment_part(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

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

    @classmethod
    def setUpClass(cls):
        cls.sequence_rule_list = list()
        cls.sequence_rule_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRuleList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRuleList tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRuleList tests'
        cls.assessment_part_1 = cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleList tests'
        cls.assessment_part_2 = cls.catalog.create_assessment_part_for_assessment(create_form)

        cls.form = cls.catalog.get_sequence_rule_form_for_create(cls.assessment_part_1.ident,
                                                                 cls.assessment_part_2.ident,
                                                                 [])

    def setUp(self):
        from dlkit.json_.assessment_authoring.objects import SequenceRuleList
        self.sequence_rule_list = list()
        self.sequence_rule_ids = list()

        for num in [0, 1]:
            form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                  self.assessment_part_2.ident,
                                                                  [])
            obj = self.catalog.create_sequence_rule(form)

            self.sequence_rule_list.append(obj)
            self.sequence_rule_ids.append(obj.ident)
        self.sequence_rule_list = SequenceRuleList(self.sequence_rule_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_sequence_rules():
            cls.catalog.delete_sequence_rule(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_sequence_rule(self):
        """Tests get_next_sequence_rule"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRule
        self.assertTrue(isinstance(self.sequence_rule_list.get_next_sequence_rule(), SequenceRule))

    def test_get_next_sequence_rules(self):
        """Tests get_next_sequence_rules"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList, SequenceRule
        new_list = self.sequence_rule_list.get_next_sequence_rules(2)
        self.assertTrue(isinstance(new_list, SequenceRuleList))
        for item in new_list:
            self.assertTrue(isinstance(item, SequenceRule))
