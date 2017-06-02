"""Unit tests of assessment.authoring sessions."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.abstract_osid.osid.objects import OsidForm
from dlkit.primordium.id.primitives import Id
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


class TestAssessmentPartLookupSession(unittest.TestCase):
    """Tests for AssessmentPartLookupSession"""

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

        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident,
                                                                                         [])
            create_form.display_name = 'Test AssessmentPart ' + str(num)
            create_form.description = 'Test AssessmentPart for AssessmentPartLookupSession tests'
            if num > 1:
                create_form.sequestered = True
            obj = cls.catalog.create_assessment_part_for_assessment(create_form)
            cls.assessment_part_list.append(obj)
            cls.assessment_part_ids.append(obj.ident)

        cls.assessment = cls.catalog.get_assessment(cls.assessment.ident)

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        for obj in cls.catalog.get_assessment_parts():
            cls.catalog.delete_assessment_part(obj.ident)
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_assessment_id(self):
        """tests get_assessment_id"""
        self.assertEqual(str(self.assessment_part_list[0].get_assessment_id()),
                         str(self.assessment.ident))

    def test_get_assessment(self):
        """tests get_assessment"""
        def check_equal(val1, val2):
            self.assertEqual(val1, val2)

        def check_dict_equal(dict1, dict2):
            for item in dict1.items():
                key = item[0]
                value = item[1]
                if isinstance(value, dict):
                    check_dict_equal(value, dict2[key])
                else:
                    check_equal(value, dict2[key])

        check_dict_equal(self.assessment_part_list[0].get_assessment().object_map,
                         self.assessment.object_map)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        # this should not be here...
        pass

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_assessment_parts(self):
        """Tests can_lookup_assessment_parts"""
        self.assertTrue(isinstance(self.catalog.can_lookup_assessment_parts(), bool))

    def test_use_comparative_assessment_part_view(self):
        """Tests use_comparative_assessment_part_view"""
        self.catalog.use_comparative_assessment_part_view()

    def test_use_plenary_assessment_part_view(self):
        """Tests use_plenary_assessment_part_view"""
        self.catalog.use_plenary_assessment_part_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    @unittest.skip('unimplemented test')
    def test_use_active_assessment_part_view(self):
        """Tests use_active_assessment_part_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_any_status_assessment_part_view(self):
        """Tests use_any_status_assessment_part_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_sequestered_assessment_part_view(self):
        """Tests use_sequestered_assessment_part_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_unsequestered_assessment_part_view(self):
        """Tests use_unsequestered_assessment_part_view"""
        pass

    def test_get_assessment_part(self):
        """Tests get_assessment_part"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment_part(self.assessment_part_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_part_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment_part(self.assessment_part_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_part_list[0].ident)

    def test_get_assessment_parts_by_ids(self):
        """Tests get_assessment_parts_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_ids(self.assessment_part_ids)
        self.assertTrue(isinstance(objects, AssessmentPartList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_ids(self.assessment_part_ids)

    def test_get_assessment_parts_by_genus_type(self):
        """Tests get_assessment_parts_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentPartList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_genus_type(DEFAULT_TYPE)

    def test_get_assessment_parts_by_parent_genus_type(self):
        """Tests get_assessment_parts_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentPartList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_assessment_parts_by_record_type(self):
        """Tests get_assessment_parts_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentPartList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_assessment_parts_for_assessment(self):
        """Tests get_assessment_parts_for_assessment"""
        pass

    def test_get_assessment_parts(self):
        """Tests get_assessment_parts"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartList
        objects = self.catalog.get_assessment_parts()
        self.assertTrue(isinstance(objects, AssessmentPartList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessment_parts()

    def test_get_assessment_part_with_alias(self):
        self.catalog.alias_assessment_part(self.assessment_part_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment_part(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_part_ids[0])


class TestAssessmentPartQuerySession(unittest.TestCase):
    """Tests for AssessmentPartQuerySession"""

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

        colors = ['Orange', 'Blue', 'Green', 'orange']

        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident,
                                                                                         [])
            create_form.display_name = 'Test AssessmentPart ' + str(num) + colors[num]
            create_form.description = 'Test AssessmentPart for AssessmentPartLookupSession tests'
            obj = cls.catalog.create_assessment_part_for_assessment(create_form)
            cls.assessment_part_list.append(obj)
            cls.assessment_part_ids.append(obj.ident)

        cls.assessment = cls.catalog.get_assessment(cls.assessment.ident)

    @classmethod
    def tearDownClass(cls):
        cls.catalog.use_unsequestered_assessment_part_view()
        for obj in cls.catalog.get_assessment_parts():
            cls.catalog.delete_assessment_part(obj.ident)
        cls.catalog.delete_assessment(cls.assessment.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_search_assessment_parts(self):
        """Tests can_search_assessment_parts"""
        pass

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    @unittest.skip('unimplemented test')
    def test_use_sequestered_assessment_part_view(self):
        """Tests use_sequestered_assessment_part_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_unsequestered_assessment_part_view(self):
        """Tests use_unsequestered_assessment_part_view"""
        pass

    def test_get_assessment_part_query(self):
        """Tests get_assessment_part_query"""
        query = self.catalog.get_assessment_part_query()

    def test_get_assessment_parts_by_query(self):
        """Tests get_assessment_parts_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_assessment_part_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessment_parts_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_assessment_parts_by_query(query).available(), 3)


class TestAssessmentPartAdminSession(unittest.TestCase):
    """Tests for AssessmentPartAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        assessment_form = cls.catalog.get_assessment_form_for_create([])
        assessment_form.display_name = 'Test Assessment'
        assessment_form.description = 'Test Assessment for AssessmentPartAdminSession tests'
        cls.assessment = cls.catalog.create_assessment(assessment_form)

        form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        form.display_name = 'new AssessmentPart'
        form.description = 'description of AssessmentPart'
        form.set_genus_type(NEW_TYPE)
        cls.osid_object = cls.catalog.create_assessment_part_for_assessment(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessment_parts():
            cls.catalog.delete_assessment_part(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_assessment_parts(self):
        """Tests can_create_assessment_parts"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_assessment_parts(), bool))

    def test_can_create_assessment_part_with_record_types(self):
        """Tests can_create_assessment_part_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_assessment_part_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_form_for_create_for_assessment(self):
        """Tests get_assessment_part_form_for_create_for_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_assessment_part_for_assessment(self):
        """Tests create_assessment_part_for_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_part_form_for_create_for_assessment_part(self):
        """Tests get_assessment_part_form_for_create_for_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_assessment_part_for_assessment_part(self):
        """Tests create_assessment_part_for_assessment_part"""
        pass

    def test_can_update_assessment_parts(self):
        """Tests can_update_assessment_parts"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_assessment_parts(), bool))

    def test_get_assessment_part_form_for_update(self):
        """Tests get_assessment_part_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_assessment_part_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    @unittest.skip('unimplemented test')
    def test_update_assessment_part(self):
        """Tests update_assessment_part"""
        pass

    def test_can_delete_assessment_parts(self):
        """Tests can_delete_assessment_parts"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_assessment_parts(), bool))

    @unittest.skip('unimplemented test')
    def test_delete_assessment_part(self):
        """Tests delete_assessment_part"""
        pass

    def test_can_manage_assessment_part_aliases(self):
        """Tests can_manage_assessment_part_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_assessment_part_aliases(), bool))

    def test_alias_assessment_part(self):
        """Tests alias_assessment_part"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_assessment_part(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_assessment_part(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)


class TestAssessmentPartItemSession(unittest.TestCase):
    """Tests for AssessmentPartItemSession"""

    @classmethod
    def setUpClass(cls):
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT_AUTHORING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartItemSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssetCompositionSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part'
        create_form.description = 'Test Assessment Part for AssetCompositionSession tests'
        cls.assessment_part = cls.catalog.create_assessment_part_for_assessment(create_form)
        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for AssessmentPartItemSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)
            cls.catalog.add_item(obj.ident, cls.assessment_part.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessment_parts():
                catalog.delete_assessment_part(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_access_assessment_part_items(self):
        """Tests can_access_assessment_part_items"""
        pass

    def test_use_comparative_asseessment_part_item_view(self):
        """Tests use_comparative_asseessment_part_item_view"""
        self.catalog.use_comparative_asseessment_part_item_view()

    def test_use_plenary_assessment_part_item_view(self):
        """Tests use_plenary_assessment_part_item_view"""
        self.catalog.use_plenary_assessment_part_item_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_part_items(self):
        """Tests get_assessment_part_items"""
        self.assertEqual(self.catalog.get_assessment_part_items(self.assessment_part.ident).available(), 4)

    def test_get_assessment_parts_by_item(self):
        """Tests get_assessment_parts_by_item"""
        self.assertEqual(self.catalog.get_assessment_parts_by_item(self.item_ids[0]).available(), 1)
        self.assertEqual(self.catalog.get_assessment_parts_by_item(self.item_ids[0]).next().ident, self.assessment_part.ident)


class TestAssessmentPartItemDesignSession(unittest.TestCase):
    """Tests for AssessmentPartItemDesignSession"""

    @classmethod
    def setUpClass(cls):
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT_AUTHORING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentPartItemDesignSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssetCompositionSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part'
        create_form.description = 'Test Assessment Part for AssetCompositionSession tests'
        cls.assessment_part = cls.catalog.create_assessment_part_for_assessment(create_form)
        for num in [0, 1, 2, 3]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for AssessmentPartItemSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)
            cls.catalog.add_item(obj.ident, cls.assessment_part.ident)

        cls.assessment = cls.catalog.get_assessment(cls.assessment.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessment_parts():
                catalog.delete_assessment_part(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    @unittest.skip('unimplemented test')
    def test_can_design_assessment_parts(self):
        """Tests can_design_assessment_parts"""
        pass

    @unittest.skip('unimplemented test')
    def test_add_item(self):
        """Tests add_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_move_item_ahead(self):
        """Tests move_item_ahead"""
        pass

    @unittest.skip('unimplemented test')
    def test_move_item_behind(self):
        """Tests move_item_behind"""
        pass

    @unittest.skip('unimplemented test')
    def test_order_items(self):
        """Tests order_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_remove_item(self):
        """Tests remove_item"""
        pass


class TestSequenceRuleLookupSession(unittest.TestCase):
    """Tests for SequenceRuleLookupSession"""

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
        assessment_part_1 = cls.catalog.create_assessment_part_for_assessment(create_form)

        create_form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident, [])
        create_form.display_name = 'Test Assessment Part 2'
        create_form.description = 'Test Assessment Part for SequenceRuleLookupSession tests'
        assessment_part_2 = cls.catalog.create_assessment_part_for_assessment(create_form)

        for num in [0, 1]:
            create_form = cls.catalog.get_sequence_rule_form_for_create(assessment_part_1.ident,
                                                                        assessment_part_2.ident,
                                                                        [])
            create_form.display_name = 'Test Sequence Rule ' + str(num)
            create_form.description = 'Test Sequence Rule for SequenceRuleLookupSession tests'
            obj = cls.catalog.create_sequence_rule(create_form)
            cls.sequence_rule_list.append(obj)
            cls.sequence_rule_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_sequence_rules():
                catalog.delete_sequence_rule(obj.ident)
            for obj in catalog.get_assessment_parts():
                catalog.delete_assessment_part(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_lookup_sequence_rules(self):
        """Tests can_lookup_sequence_rules"""
        self.assertTrue(isinstance(self.catalog.can_lookup_sequence_rules(), bool))

    def test_use_comparative_sequence_rule_view(self):
        """Tests use_comparative_sequence_rule_view"""
        self.catalog.use_comparative_sequence_rule_view()

    def test_use_plenary_sequence_rule_view(self):
        """Tests use_plenary_sequence_rule_view"""
        self.catalog.use_plenary_sequence_rule_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    @unittest.skip('unimplemented test')
    def test_use_active_sequence_rule_view(self):
        """Tests use_active_sequence_rule_view"""
        pass

    @unittest.skip('unimplemented test')
    def test_use_any_status_sequence_rule_view(self):
        """Tests use_any_status_sequence_rule_view"""
        pass

    def test_get_sequence_rule(self):
        """Tests get_sequence_rule"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_sequence_rule(self.sequence_rule_list[0].ident)
        self.assertEqual(obj.ident, self.sequence_rule_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_sequence_rule(self.sequence_rule_list[0].ident)
        self.assertEqual(obj.ident, self.sequence_rule_list[0].ident)

    def test_get_sequence_rules_by_ids(self):
        """Tests get_sequence_rules_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        objects = self.catalog.get_sequence_rules_by_ids(self.sequence_rule_ids)
        self.assertTrue(isinstance(objects, SequenceRuleList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_sequence_rules_by_ids(self.sequence_rule_ids)

    def test_get_sequence_rules_by_genus_type(self):
        """Tests get_sequence_rules_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        objects = self.catalog.get_sequence_rules_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, SequenceRuleList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_sequence_rules_by_genus_type(DEFAULT_TYPE)

    def test_get_sequence_rules_by_parent_genus_type(self):
        """Tests get_sequence_rules_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        objects = self.catalog.get_sequence_rules_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, SequenceRuleList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_sequence_rules_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_sequence_rules_by_record_type(self):
        """Tests get_sequence_rules_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        objects = self.catalog.get_sequence_rules_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, SequenceRuleList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_sequence_rules_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_sequence_rules_for_assessment_part(self):
        """Tests get_sequence_rules_for_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_sequence_rules_for_next_assessment_part(self):
        """Tests get_sequence_rules_for_next_assessment_part"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_sequence_rules_for_assessment_parts(self):
        """Tests get_sequence_rules_for_assessment_parts"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_sequence_rules_for_assessment(self):
        """Tests get_sequence_rules_for_assessment"""
        pass

    def test_get_sequence_rules(self):
        """Tests get_sequence_rules"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRuleList
        objects = self.catalog.get_sequence_rules()
        self.assertTrue(isinstance(objects, SequenceRuleList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_sequence_rules()

    def test_get_sequence_rule_with_alias(self):
        self.catalog.alias_sequence_rule(self.sequence_rule_ids[0], ALIAS_ID)
        obj = self.catalog.get_sequence_rule(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.sequence_rule_ids[0])


class TestSequenceRuleAdminSession(unittest.TestCase):
    """Tests for SequenceRuleAdminSession"""

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

        for num in [0, 1]:
            create_form = cls.catalog.get_sequence_rule_form_for_create(cls.assessment_part_1.ident,
                                                                        cls.assessment_part_2.ident,
                                                                        [])
            create_form.display_name = 'Test Sequence Rule ' + str(num)
            create_form.description = 'Test Sequence Rule for SequenceRuleLookupSession tests'
            obj = cls.catalog.create_sequence_rule(create_form)
            cls.sequence_rule_list.append(obj)
            cls.sequence_rule_ids.append(obj.ident)

        create_form = cls.catalog.get_sequence_rule_form_for_create(cls.assessment_part_1.ident,
                                                                    cls.assessment_part_2.ident,
                                                                    [])
        create_form.display_name = 'new SequenceRule'
        create_form.description = 'description of SequenceRule'
        create_form.genus_type = NEW_TYPE
        cls.osid_object = cls.catalog.create_sequence_rule(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_sequence_rules():
                catalog.delete_sequence_rule(obj.ident)
            for obj in catalog.get_assessment_parts():
                catalog.delete_assessment_part(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    def test_get_bank(self):
        """Tests get_bank"""
        # is this test really needed?
        # From test_templates/resource.py::ResourceLookupSession::get_bin_template
        self.assertIsNotNone(self.catalog)

    def test_can_create_sequence_rule(self):
        """Tests can_create_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resources_template
        self.assertTrue(isinstance(self.catalog.can_create_sequence_rule(), bool))

    def test_can_create_sequence_rule_with_record_types(self):
        """Tests can_create_sequence_rule_with_record_types"""
        # From test_templates/resource.py::ResourceAdminSession::can_create_resource_with_record_types_template
        self.assertTrue(isinstance(self.catalog.can_create_sequence_rule_with_record_types(DEFAULT_TYPE), bool))

    def test_get_sequence_rule_form_for_create(self):
        """Tests get_sequence_rule_form_for_create"""
        form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                              self.assessment_part_2.ident,
                                                              [])
        self.assertTrue(isinstance(form, OsidForm))
        self.assertFalse(form.is_for_update())

    def test_create_sequence_rule(self):
        """Tests create_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::create_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRule
        self.assertTrue(isinstance(self.osid_object, SequenceRule))
        self.assertEqual(self.osid_object.display_name.text, 'new SequenceRule')
        self.assertEqual(self.osid_object.description.text, 'description of SequenceRule')
        self.assertEqual(self.osid_object.genus_type, NEW_TYPE)

    def test_can_update_sequence_rules(self):
        """Tests can_update_sequence_rules"""
        # From test_templates/resource.py::ResourceAdminSession::can_update_resources_template
        self.assertTrue(isinstance(self.catalog.can_update_sequence_rules(), bool))

    def test_get_sequence_rule_form_for_update(self):
        """Tests get_sequence_rule_form_for_update"""
        # From test_templates/resource.py::ResourceAdminSession::get_resource_form_for_update_template
        form = self.catalog.get_sequence_rule_form_for_update(self.osid_object.ident)
        self.assertTrue(isinstance(form, OsidForm))
        self.assertTrue(form.is_for_update())

    def test_update_sequence_rule(self):
        """Tests update_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::update_resource_template
        from dlkit.abstract_osid.assessment_authoring.objects import SequenceRule
        form = self.catalog.get_sequence_rule_form_for_update(self.osid_object.ident)
        form.display_name = 'new name'
        form.description = 'new description'
        form.set_genus_type(NEW_TYPE_2)
        updated_object = self.catalog.update_sequence_rule(form)
        self.assertTrue(isinstance(updated_object, SequenceRule))
        self.assertEqual(updated_object.ident, self.osid_object.ident)
        self.assertEqual(updated_object.display_name.text, 'new name')
        self.assertEqual(updated_object.description.text, 'new description')
        self.assertEqual(updated_object.genus_type, NEW_TYPE_2)

    def test_can_delete_sequence_rules(self):
        """Tests can_delete_sequence_rules"""
        # From test_templates/resource.py::ResourceAdminSession::can_delete_resources_template
        self.assertTrue(isinstance(self.catalog.can_delete_sequence_rules(), bool))

    def test_delete_sequence_rule(self):
        """Tests delete_sequence_rule"""
        create_form = self.catalog.get_sequence_rule_form_for_create(self.assessment_part_1.ident,
                                                                     self.assessment_part_2.ident,
                                                                     [])
        create_form.display_name = 'new SequenceRule'
        create_form.description = 'description of SequenceRule'
        create_form.genus_type = NEW_TYPE
        osid_object = self.catalog.create_sequence_rule(create_form)
        self.catalog.delete_sequence_rule(osid_object.ident)
        with self.assertRaises(errors.NotFound):
            self.catalog.get_sequence_rule(osid_object.ident)

    def test_can_manage_sequence_rule_aliases(self):
        """Tests can_manage_sequence_rule_aliases"""
        # From test_templates/resource.py::ResourceAdminSession::can_manage_resource_aliases_template
        self.assertTrue(isinstance(self.catalog.can_manage_sequence_rule_aliases(), bool))

    def test_alias_sequence_rule(self):
        """Tests alias_sequence_rule"""
        # From test_templates/resource.py::ResourceAdminSession::alias_resource_template
        alias_id = Id(self.catalog.ident.namespace + '%3Amy-alias%40ODL.MIT.EDU')
        self.catalog.alias_sequence_rule(self.osid_object.ident, alias_id)
        aliased_object = self.catalog.get_sequence_rule(alias_id)
        self.assertEqual(aliased_object.ident, self.osid_object.ident)

    @unittest.skip('unimplemented test')
    def test_can_sequence_sequence_rules(self):
        """Tests can_sequence_sequence_rules"""
        pass

    @unittest.skip('unimplemented test')
    def test_move_sequence_rule_ahead(self):
        """Tests move_sequence_rule_ahead"""
        pass

    @unittest.skip('unimplemented test')
    def test_move_sequence_rule_behind(self):
        """Tests move_sequence_rule_behind"""
        pass

    @unittest.skip('unimplemented test')
    def test_order_sequence_rules(self):
        """Tests order_sequence_rules"""
        pass
