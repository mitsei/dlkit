"""Unit tests of assessment.authoring objects."""


import unittest


from dlkit.abstract_osid.assessment.objects import Assessment
from dlkit.abstract_osid.assessment_authoring import objects as ABCObjects
from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
from dlkit.abstract_osid.id.primitives import Id as ABC_Id
from dlkit.abstract_osid.locale.primitives import DisplayText as ABC_DisplayText
from dlkit.abstract_osid.osid import errors
from dlkit.json_.id.objects import IdList
from dlkit.json_.osid.metadata import Metadata
from dlkit.primordium.calendaring.primitives import DateTime, Duration
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


SIMPLE_SEQUENCE_RECORD_TYPE = Type(**{"authority": "ODL.MIT.EDU", "namespace": "osid-object", "identifier": "simple-child-sequencing"})
REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestAssessmentPart(unittest.TestCase):
    """Tests for AssessmentPart"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_part_list = list()
        cls.assessment_part_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPart tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        assessment_form = cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPart tests'
        cls.assessment = cls.catalog.create_assessment(assessment_form)

    def setUp(self):
        form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                               [])
        self.object = self.catalog.create_assessment_part_for_assessment(form)
        self.assessment = self.catalog.get_assessment(self.assessment.ident)

    def tearDown(self):
        for assessment_part in self.catalog.get_assessment_parts_for_assessment(self.assessment.ident):
            if assessment_part.has_children():
                for child_id in assessment_part.get_child_ids():
                    try:
                        self.catalog.delete_assessment_part(child_id)
                    except errors.NotFound:
                        pass
            self.catalog.delete_assessment_part(assessment_part.ident)

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        result_id = self.object.get_assessment_id()
        self.assertTrue(isinstance(result_id, Id))
        self.assertEqual(str(result_id),
                         str(self.assessment.ident))

    def test_get_assessment(self):
        """Tests get_assessment"""
        result = self.object.get_assessment()
        self.assertTrue(isinstance(result, Assessment))
        self.assertEqual(str(result.ident),
                         str(self.assessment.ident))

    def test_has_parent_part(self):
        """Tests has_parent_part"""
        self.assertTrue(isinstance(self.object.has_parent_part(), bool))

    def test_get_assessment_part_id(self):
        """Tests get_assessment_part_id"""
        with self.assertRaises(errors.IllegalState):
            self.object.get_assessment_part_id()

    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        with self.assertRaises(errors.IllegalState):
            self.object.get_assessment_part()

    def test_is_section(self):
        """Tests is_section"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_section(), bool))

    def test_get_weight(self):
        """Tests get_weight"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_weight()

    def test_get_allocated_time(self):
        """Tests get_allocated_time"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_allocated_time()

    def test_get_child_assessment_part_ids(self):
        """Tests get_child_assessment_part_ids"""
        with self.assertRaises(errors.IllegalState):
            self.object.get_child_assessment_part_ids()

        # to get these back, need to have a simple sequencing part as the parent
        form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                               [SIMPLE_SEQUENCE_RECORD_TYPE])
        form.set_children([Id('assessment.Part%3A000000000000000000000000%40ODL.MIT.EDU')])
        parent_part = self.catalog.create_assessment_part_for_assessment(form)

        results = parent_part.get_child_assessment_part_ids()
        self.assertTrue(isinstance(results, IdList))
        self.assertEqual(results.available(), 1)
        self.assertEqual(str(results.next()),
                         'assessment.Part%3A000000000000000000000000%40ODL.MIT.EDU')

    def test_get_child_assessment_parts(self):
        """Tests get_child_assessment_parts"""
        with self.assertRaises(errors.IllegalState):
            self.object.get_child_assessment_parts()

        # to get these back, need to have a simple sequencing part as the parent

        form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                               [SIMPLE_SEQUENCE_RECORD_TYPE])
        parent_part = self.catalog.create_assessment_part_for_assessment(form)

        form = self.catalog.get_assessment_part_form_for_create_for_assessment_part(parent_part.ident,
                                                                                    [])
        child_part = self.catalog.create_assessment_part_for_assessment(form)

        parent_part = self.catalog.get_assessment_part(parent_part.ident)

        results = parent_part.get_child_assessment_part_ids()
        self.assertTrue(isinstance(results, IdList))
        self.assertEqual(results.available(), 1)
        self.assertEqual(str(results.next()),
                         str(child_part.ident))

    def test_get_assessment_part_record(self):
        """Tests get_assessment_part_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_assessment_part_record(True)


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

    def setUp(self):
        self.form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident,
                                                                                    [])
        self.object = self.form
        self.assessment = self.catalog.get_assessment(self.assessment.ident)

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_weight_metadata(self):
        """Tests get_weight_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_weight_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'CARDINAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_weight(self):
        """Tests set_weight"""
        with self.assertRaises(errors.Unimplemented):
            self.object.set_weight(True)

    def test_clear_weight(self):
        """Tests clear_weight"""
        with self.assertRaises(errors.Unimplemented):
            self.object.clear_weight()

    def test_get_allocated_time_metadata(self):
        """Tests get_allocated_time_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_allocated_time_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'DURATION')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_allocated_time(self):
        """Tests set_allocated_time"""
        # From test_templates/assessment.py::AssessmentOfferedForm::set_duration_template
        test_duration = Duration(hours=1)
        self.assertIsNone(self.form._my_map['allocatedTime'])
        self.form.set_allocated_time(test_duration)
        self.assertEqual(self.form._my_map['allocatedTime']['seconds'], 3600)
        self.assertEqual(self.form._my_map['allocatedTime']['days'], 0)
        self.assertEqual(self.form._my_map['allocatedTime']['microseconds'], 0)
        with self.assertRaises(errors.InvalidArgument):
            self.form.set_allocated_time(1.05)
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
        self.assertEqual(self.form._my_map['allocatedTime'], self.form.get_allocated_time_metadata().get_default_duration_values()[0])

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

    @classmethod
    def setUpClass(cls):
        cls.sequence_rule_list = list()
        cls.sequence_rule_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for SequenceRule tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for SequenceRule tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 1'
        create_form.description = 'Test Assessment Part for SequenceRule tests'
        cls.assessment_part_1 = cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRule tests'
        cls.assessment_part_2 = cls.catalog.create_assessment_part_for_assessment(create_form)

    def setUp(self):
        form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                              self.assessment_part_2.ident,
                                                              [])
        self.object = self.catalog.create_sequence_rule(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessment_parts():
            cls.catalog.delete_assessment_part(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_assessment_part_id(self):
        """Tests get_assessment_part_id"""
        part_id = self.object.get_assessment_part_id()
        self.assertTrue(isinstance(part_id, Id))
        self.assertEqual(str(part_id),
                         str(self.assessment_part_1.ident))

    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        part = self.object.get_assessment_part()
        self.assertTrue(isinstance(part, AssessmentPart))
        self.assertEqual(str(part.ident),
                         str(self.assessment_part_1.ident))

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_part_id(self):
        """Tests get_next_assessment_part_id"""
        pass

    def test_get_next_assessment_part(self):
        """Tests get_next_assessment_part"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_next_assessment_part()

    def test_get_minimum_score(self):
        """Tests get_minimum_score"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_minimum_score()

    def test_get_maximum_score(self):
        """Tests get_maximum_score"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_maximum_score()

    def test_is_cumulative(self):
        """Tests is_cumulative"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.is_cumulative(), bool))

    def test_get_applied_assessment_part_ids(self):
        """Tests get_applied_assessment_part_ids"""
        result = self.object.get_applied_assessment_part_ids()
        self.assertTrue(isinstance(result, IdList))
        self.assertEqual(result.available(), 0)

    def test_get_applied_assessment_parts(self):
        """Tests get_applied_assessment_parts"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_applied_assessment_parts()

    def test_get_sequence_rule_record(self):
        """Tests get_sequence_rule_record"""
        with self.assertRaises(errors.Unsupported):
            self.object.get_sequence_rule_record(True)


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

    def setUp(self):
        self.form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                   self.assessment_part_2.ident,
                                                                   [])
        self.object = self.form

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
        mdata = self.form.get_minimum_score_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'CARDINAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_minimum_score(self):
        """Tests set_minimum_score"""
        with self.assertRaises(errors.Unimplemented):
            self.object.set_minimum_score(True)

    def test_get_maximum_score_metadata(self):
        """Tests get_maximum_score_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_maximum_score_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'CARDINAL')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_maximum_score(self):
        """Tests set_maximum_score"""
        with self.assertRaises(errors.Unimplemented):
            self.object.set_maximum_score(True)

    def test_get_cumulative_metadata(self):
        """Tests get_cumulative_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        mdata = self.form.get_cumulative_metadata()
        self.assertTrue(isinstance(mdata, Metadata))
        self.assertTrue(isinstance(mdata.get_element_id(), ABC_Id))
        self.assertTrue(isinstance(mdata.get_element_label(), ABC_DisplayText))
        self.assertTrue(isinstance(mdata.get_instructions(), ABC_DisplayText))
        self.assertEquals(mdata.get_syntax(), 'BOOLEAN')
        self.assertFalse(mdata.is_array())
        self.assertTrue(isinstance(mdata.is_required(), bool))
        self.assertTrue(isinstance(mdata.is_read_only(), bool))
        self.assertTrue(isinstance(mdata.is_linked(), bool))

    def test_set_cumulative(self):
        """Tests set_cumulative"""
        create_form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                     self.assessment_part_2.ident,
                                                                     [])
        create_form.set_cumulative(True)
        self.assertTrue(create_form._my_map['cumulative'])

    def test_get_applied_assessment_parts_metadata(self):
        """Tests get_applied_assessment_parts_metadata"""
        with self.assertRaises(errors.Unimplemented):
            self.object.get_applied_assessment_parts_metadata()

    def test_apply_assessment_parts(self):
        """Tests apply_assessment_parts"""
        with self.assertRaises(errors.Unimplemented):
            self.object.apply_assessment_parts(True)

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
