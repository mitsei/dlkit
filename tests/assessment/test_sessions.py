"""Unit tests of assessment sessions."""


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
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})


class TestAssessmentSession(unittest.TestCase):
    """Tests for AssessmentSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_take_assessments(self):
        """Tests can_take_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_assessment_begun(self):
        """Tests has_assessment_begun"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_assessment_over(self):
        """Tests is_assessment_over"""
        pass

    @unittest.skip('unimplemented test')
    def test_requires_synchronous_sections(self):
        """Tests requires_synchronous_sections"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_first_assessment_section(self):
        """Tests get_first_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_next_assessment_section(self):
        """Tests has_next_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_assessment_section(self):
        """Tests get_next_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_previous_assessment_section(self):
        """Tests has_previous_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_previous_assessment_section(self):
        """Tests get_previous_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_section(self):
        """Tests get_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_sections(self):
        """Tests get_assessment_sections"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_assessment_section_complete(self):
        """Tests is_assessment_section_complete"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_incomplete_assessment_sections(self):
        """Tests get_incomplete_assessment_sections"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_assessment_section_begun(self):
        """Tests has_assessment_section_begun"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_assessment_section_over(self):
        """Tests is_assessment_section_over"""
        pass

    @unittest.skip('unimplemented test')
    def test_requires_synchronous_responses(self):
        """Tests requires_synchronous_responses"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_first_question(self):
        """Tests get_first_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_next_question(self):
        """Tests has_next_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_question(self):
        """Tests get_next_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_previous_question(self):
        """Tests has_previous_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_previous_question(self):
        """Tests get_previous_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question(self):
        """Tests get_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_questions(self):
        """Tests get_questions"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_response_form(self):
        """Tests get_response_form"""
        pass

    @unittest.skip('unimplemented test')
    def test_submit_response(self):
        """Tests submit_response"""
        pass

    @unittest.skip('unimplemented test')
    def test_skip_item(self):
        """Tests skip_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_question_answered(self):
        """Tests is_question_answered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_unanswered_questions(self):
        """Tests get_unanswered_questions"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_unanswered_questions(self):
        """Tests has_unanswered_questions"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_first_unanswered_question(self):
        """Tests get_first_unanswered_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_next_unanswered_question(self):
        """Tests has_next_unanswered_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_unanswered_question(self):
        """Tests get_next_unanswered_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_previous_unanswered_question(self):
        """Tests has_previous_unanswered_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_previous_unanswered_question(self):
        """Tests get_previous_unanswered_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_response(self):
        """Tests get_response"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_responses(self):
        """Tests get_responses"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_response(self):
        """Tests clear_response"""
        pass

    @unittest.skip('unimplemented test')
    def test_finish_assessment_section(self):
        """Tests finish_assessment_section"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_answer_available(self):
        """Tests is_answer_available"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answers(self):
        """Tests get_answers"""
        pass

    @unittest.skip('unimplemented test')
    def test_finish_assessment(self):
        """Tests finish_assessment"""
        pass


class TestAssessmentResultsSession(unittest.TestCase):
    """Tests for AssessmentResultsSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_access_assessment_results(self):
        """Tests can_access_assessment_results"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items(self):
        """Tests get_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_responses(self):
        """Tests get_responses"""
        pass

    @unittest.skip('unimplemented test')
    def test_are_results_available(self):
        """Tests are_results_available"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_grade_entries(self):
        """Tests get_grade_entries"""
        pass


class TestItemLookupSession(unittest.TestCase):
    """Tests for ItemLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemLookupSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_lookup_items(self):
        """Tests can_lookup_items"""
        self.assertTrue(isinstance(self.catalog.can_lookup_items(), bool))

    def test_use_comparative_item_view(self):
        """Tests use_comparative_item_view"""
        self.catalog.use_comparative_item_view()

    def test_use_plenary_item_view(self):
        """Tests use_plenary_item_view"""
        self.catalog.use_plenary_item_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_item(self):
        """Tests get_item"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_item(self.item_list[0].ident)
        self.assertEqual(obj.ident, self.item_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_item(self.item_list[0].ident)
        self.assertEqual(obj.ident, self.item_list[0].ident)

    def test_get_items_by_ids(self):
        """Tests get_items_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_ids(self.item_ids)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_ids(self.item_ids)

    def test_get_items_by_genus_type(self):
        """Tests get_items_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_genus_type(DEFAULT_TYPE)

    def test_get_items_by_parent_genus_type(self):
        """Tests get_items_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_items_by_record_type(self):
        """Tests get_items_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_items_by_question(self):
        """Tests get_items_by_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_by_answer(self):
        """Tests get_items_by_answer"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_by_learning_objective(self):
        """Tests get_items_by_learning_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_by_learning_objectives(self):
        """Tests get_items_by_learning_objectives"""
        pass

    def test_get_items(self):
        """Tests get_items"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import ItemList
        objects = self.catalog.get_items()
        self.assertTrue(isinstance(objects, ItemList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_items()

    def test_get_item_with_alias(self):
        self.catalog.alias_item(self.item_ids[0], ALIAS_ID)
        obj = self.catalog.get_item(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.item_ids[0])


class TestItemQuerySession(unittest.TestCase):
    """Tests for ItemQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemQuerySession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + color
            create_form.description = (
                'Test Item for ItemQuerySession tests, did I mention green')
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_search_items(self):
        """Tests can_search_items"""
        pass

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_item_query(self):
        """Tests get_item_query"""
        query = self.catalog.get_item_query()

    def test_get_items_by_query(self):
        """Tests get_items_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_item_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_items_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_items_by_query(query).available(), 3)


class TestItemSearchSession(unittest.TestCase):
    """Tests for ItemSearchSession"""

    @unittest.skip('unimplemented test')
    def test_get_item_search(self):
        """Tests get_item_search"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_search_order(self):
        """Tests get_item_search_order"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_by_search(self):
        """Tests get_items_by_search"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_query_from_inspector(self):
        """Tests get_item_query_from_inspector"""
        pass


class TestItemAdminSession(unittest.TestCase):
    """Tests for ItemAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_create_items(self):
        """Tests can_create_items"""
        self.assertTrue(isinstance(self.catalog.can_create_items(), bool))

    def test_can_create_item_with_record_types(self):
        """Tests can_create_item_with_record_types"""
        self.assertTrue(isinstance(self.catalog.can_create_item_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_item_form_for_create(self):
        """Tests get_item_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_item(self):
        """Tests create_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_items(self):
        """Tests can_update_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_form_for_update(self):
        """Tests get_item_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_item(self):
        """Tests update_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_items(self):
        """Tests can_delete_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_item(self):
        """Tests delete_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_manage_item_aliases(self):
        """Tests can_manage_item_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_item(self):
        """Tests alias_item"""
        pass

    def test_can_create_questions(self):
        """Tests can_create_questions"""
        self.assertTrue(isinstance(self.catalog.can_create_questions(), bool))

    def test_can_create_question_with_record_types(self):
        """Tests can_create_question_with_record_types"""
        self.assertTrue(isinstance(self.catalog.can_create_question_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_question_form_for_create(self):
        """Tests get_question_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_question(self):
        """Tests create_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_questions(self):
        """Tests can_update_questions"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question_form_for_update(self):
        """Tests get_question_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_question(self):
        """Tests update_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_questions(self):
        """Tests can_delete_questions"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_question(self):
        """Tests delete_question"""
        pass

    def test_can_create_answers(self):
        """Tests can_create_answers"""
        self.assertTrue(isinstance(self.catalog.can_create_answers(), bool))

    def test_can_create_answers_with_record_types(self):
        """Tests can_create_answers_with_record_types"""
        self.assertTrue(isinstance(self.catalog.can_create_answers_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_answer_form_for_create(self):
        """Tests get_answer_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_answer(self):
        """Tests create_answer"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_answers(self):
        """Tests can_update_answers"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answer_form_for_update(self):
        """Tests get_answer_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_answer(self):
        """Tests update_answer"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_answers(self):
        """Tests can_delete_answers"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_answer(self):
        """Tests delete_answer"""
        pass


class TestItemNotificationSession(unittest.TestCase):
    """Tests for ItemNotificationSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemNotificationSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemNotificationSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_register_for_item_notifications(self):
        """Tests can_register_for_item_notifications"""
        pass

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    @unittest.skip('unimplemented test')
    def test_reliable_item_notifications(self):
        """Tests reliable_item_notifications"""
        pass

    @unittest.skip('unimplemented test')
    def test_unreliable_item_notifications(self):
        """Tests unreliable_item_notifications"""
        pass

    @unittest.skip('unimplemented test')
    def test_acknowledge_item_notification(self):
        """Tests acknowledge_item_notification"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_new_items(self):
        """Tests register_for_new_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_changed_items(self):
        """Tests register_for_changed_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_changed_item(self):
        """Tests register_for_changed_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_deleted_items(self):
        """Tests register_for_deleted_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_register_for_deleted_item(self):
        """Tests register_for_deleted_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_reliable_item_notifications(self):
        """Tests reliable_item_notifications"""
        pass

    @unittest.skip('unimplemented test')
    def test_unreliable_item_notifications(self):
        """Tests unreliable_item_notifications"""
        pass

    @unittest.skip('unimplemented test')
    def test_acknowledge_item_notification(self):
        """Tests acknowledge_item_notification"""
        pass


class TestItemBankSession(unittest.TestCase):
    """Tests for ItemBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.item_list = list()
        cls.item_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for ItemBankSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemBankSession tests'
            obj = cls.catalog.create_item(create_form)
            cls.item_list.append(obj)
            cls.item_ids.append(obj.ident)
        cls.svc_mgr.assign_item_to_bank(
            cls.item_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_item_to_bank(
            cls.item_ids[2], cls.assigned_catalog.ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_item_from_bank(
            cls.item_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_item_from_bank(
            cls.item_ids[2], cls.assigned_catalog.ident)
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_item_bank_mappings(self):
        """Tests can_lookup_item_bank_mappings"""
        pass

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        self.svc_mgr.use_plenary_bank_view()

    def test_get_item_ids_by_bank(self):
        """Tests get_item_ids_by_bank"""
        objects = self.svc_mgr.get_item_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_items_by_bank(self):
        """Tests get_items_by_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_ids_by_banks(self):
        """Tests get_item_ids_by_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_items_by_banks(self):
        """Tests get_items_by_banks"""
        pass

    def test_get_bank_ids_by_item(self):
        """Tests get_bank_ids_by_item"""
        cats = self.svc_mgr.get_bank_ids_by_item(self.item_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_item(self):
        """Tests get_banks_by_item"""
        cats = self.svc_mgr.get_banks_by_item(self.item_ids[1])
        self.assertEqual(cats.available(), 2)


class TestItemBankAssignmentSession(unittest.TestCase):
    """Tests for ItemBankAssignmentSession"""

    @unittest.skip('unimplemented test')
    def test_can_assign_items(self):
        """Tests can_assign_items"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_assign_items_to_bank(self):
        """Tests can_assign_items_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids_for_item(self):
        """Tests get_assignable_bank_ids_for_item"""
        pass

    @unittest.skip('unimplemented test')
    def test_assign_item_to_bank(self):
        """Tests assign_item_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_unassign_item_from_bank(self):
        """Tests unassign_item_from_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_reassign_item_to_billing(self):
        """Tests reassign_item_to_billing"""
        pass


class TestAssessmentLookupSession(unittest.TestCase):
    """Tests for AssessmentLookupSession"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceLookupSession
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentLookupSession tests'
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceLookupSession
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_lookup_assessments(self):
        """Tests can_lookup_assessments"""
        self.assertTrue(isinstance(self.catalog.can_lookup_assessments(), bool))

    def test_use_comparative_assessment_view(self):
        """Tests use_comparative_assessment_view"""
        self.catalog.use_comparative_assessment_view()

    def test_use_plenary_assessment_view(self):
        """Tests use_plenary_assessment_view"""
        self.catalog.use_plenary_assessment_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment(self):
        """Tests get_assessment"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment(self.assessment_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment(self.assessment_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_list[0].ident)

    def test_get_assessments_by_ids(self):
        """Tests get_assessments_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_ids(self.assessment_ids)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_ids(self.assessment_ids)

    def test_get_assessments_by_genus_type(self):
        """Tests get_assessments_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_genus_type(DEFAULT_TYPE)

    def test_get_assessments_by_parent_genus_type(self):
        """Tests get_assessments_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_assessments_by_record_type(self):
        """Tests get_assessments_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_by_record_type(DEFAULT_TYPE)

    def test_get_assessments(self):
        """Tests get_assessments"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList
        objects = self.catalog.get_assessments()
        self.assertTrue(isinstance(objects, AssessmentList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments()

    def test_get_assessment_with_alias(self):
        self.catalog.alias_assessment(self.assessment_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_ids[0])


class TestAssessmentQuerySession(unittest.TestCase):
    """Tests for AssessmentQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentQuerySession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + color
            create_form.description = (
                'Test Assessment for AssessmentQuerySession tests, did I mention green')
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_search_assessments(self):
        """Tests can_search_assessments"""
        pass

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        query = self.catalog.get_assessment_query()

    def test_get_assessments_by_query(self):
        """Tests get_assessments_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_assessment_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessments_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_assessments_by_query(query).available(), 3)


class TestAssessmentAdminSession(unittest.TestCase):
    """Tests for AssessmentAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_create_assessments(self):
        """Tests can_create_assessments"""
        self.assertTrue(isinstance(self.catalog.can_create_assessments(), bool))

    def test_can_create_assessment_with_record_types(self):
        """Tests can_create_assessment_with_record_types"""
        self.assertTrue(isinstance(self.catalog.can_create_assessment_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_assessment_form_for_create(self):
        """Tests get_assessment_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_assessment(self):
        """Tests create_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_assessments(self):
        """Tests can_update_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_form_for_update(self):
        """Tests get_assessment_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_assessment(self):
        """Tests update_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_assessments(self):
        """Tests can_delete_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_assessment(self):
        """Tests delete_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_manage_assessment_aliases(self):
        """Tests can_manage_assessment_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_assessment(self):
        """Tests alias_assessment"""
        pass


class TestAssessmentBankSession(unittest.TestCase):
    """Tests for AssessmentBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_list = list()
        cls.assessment_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank for Assignment'
        create_form.description = 'Test Bank for AssessmentBankSession tests assignment'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentBankSession tests'
            obj = cls.catalog.create_assessment(create_form)
            cls.assessment_list.append(obj)
            cls.assessment_ids.append(obj.ident)
        cls.svc_mgr.assign_assessment_to_bank(
            cls.assessment_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_assessment_to_bank(
            cls.assessment_ids[2], cls.assigned_catalog.ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_assessment_from_bank(
            cls.assessment_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_assessment_from_bank(
            cls.assessment_ids[2], cls.assigned_catalog.ident)
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_assessment_bank_mappings(self):
        """Tests can_lookup_assessment_bank_mappings"""
        pass

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_ids_by_bank(self):
        """Tests get_assessment_ids_by_bank"""
        objects = self.svc_mgr.get_assessment_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_assessments_by_bank(self):
        """Tests get_assessments_by_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_ids_by_banks(self):
        """Tests get_assessment_ids_by_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_by_banks(self):
        """Tests get_assessments_by_banks"""
        pass

    def test_get_bank_ids_by_assessment(self):
        """Tests get_bank_ids_by_assessment"""
        cats = self.svc_mgr.get_bank_ids_by_assessment(self.assessment_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_assessment(self):
        """Tests get_banks_by_assessment"""
        cats = self.svc_mgr.get_banks_by_assessment(self.assessment_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssessmentBankAssignmentSession(unittest.TestCase):
    """Tests for AssessmentBankAssignmentSession"""

    @unittest.skip('unimplemented test')
    def test_can_assign_assessments(self):
        """Tests can_assign_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_assign_assessments_to_bank(self):
        """Tests can_assign_assessments_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids_for_assessment(self):
        """Tests get_assignable_bank_ids_for_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_assign_assessment_to_bank(self):
        """Tests assign_assessment_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_unassign_assessment_from_bank(self):
        """Tests unassign_assessment_from_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_reassign_assessment_to_billing(self):
        """Tests reassign_assessment_to_billing"""
        pass


class TestAssessmentBasicAuthoringSession(unittest.TestCase):
    """Tests for AssessmentBasicAuthoringSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        simple_sequence_record_type = Type(**{
            'authority': 'ODL.MIT.EDU',
            'namespace': 'osid-object',
            'identifier': 'simple-child-sequencing'})
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        # cls.auth_svc_mgr = Runtime().get_service_manager('ASSESSMENT_AUTHORING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentBasicAuthoringSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([simple_sequence_record_type])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentBasicAuthoringSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        cls.test_items = list()
        cls.test_item_ids = list()
        for number in ['One', 'Two', 'Three', 'Four']:
            ifc = cls.catalog.get_item_form_for_create([])
            ifc.set_display_name('Test Assessment Item ' + number)
            ifc.set_description('This is a Test Item Called Number ' + number)
            test_item = cls.catalog.create_item(ifc)
            cls.test_items.append(test_item)
            cls.test_item_ids.append(test_item.ident)
            cls.catalog.add_item(cls.assessment.ident, test_item.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            for obj in catalog.get_items():
                catalog.delete_item(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_author_assessments(self):
        """Tests can_author_assessments"""
        pass

    def test_get_items(self):
        """Tests get_items"""
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).available(), 4)

    def test_add_item(self):
        """Tests add_item"""
        self._reorder_items()
        ifc = self.catalog.get_item_form_for_create([])
        ifc.set_display_name('Test Assessment Additional Item')
        ifc.set_description('This is an addtional Test Item')
        additional_item = self.catalog.create_item(ifc)
        self.catalog.add_item(self.assessment.ident, additional_item.ident)
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).available(), 5)
        self.catalog.remove_item(self.assessment.ident, additional_item.ident)

    def test_remove_item(self):
        """Tests remove_item"""
        self._reorder_items()
        self.catalog.remove_item(self.assessment.ident, self.test_item_ids[1])
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).available(), 3)
        self.catalog.add_item(self.assessment.ident, self.test_item_ids[1])
        items = self.catalog.get_assessment_items(self.assessment.ident)
        self.assertEqual(items.next().ident, self.test_item_ids[0])
        self.assertEqual(items.next().ident, self.test_item_ids[2])
        self.assertEqual(items.next().ident, self.test_item_ids[3])
        self.assertEqual(items.next().ident, self.test_item_ids[1])

    def test_move_item(self):
        """Tests move_item"""
        self._reorder_items()
        self.catalog.move_item(self.assessment.ident, self.test_item_ids[0], self.test_item_ids[3])
        items = self.catalog.get_assessment_items(self.assessment.ident)
        self.assertEqual(items.next().ident, self.test_item_ids[1])
        self.assertEqual(items.next().ident, self.test_item_ids[2])
        self.assertEqual(items.next().ident, self.test_item_ids[3])
        self.assertEqual(items.next().ident, self.test_item_ids[0])

    def test_order_items(self):
        """Tests order_items"""
        self.catalog.order_items([
            self.test_item_ids[3],
            self.test_item_ids[2],
            self.test_item_ids[1],
            self.test_item_ids[0]],
            self.assessment.ident)
        self.assertEqual(self.catalog.get_assessment_items(self.assessment.ident).next().ident, self.test_item_ids[3])

    def _reorder_items(self):
        self.catalog.order_items([
            self.test_item_ids[0],
            self.test_item_ids[1],
            self.test_item_ids[2],
            self.test_item_ids[3]],
            self.assessment.ident)


class TestAssessmentOfferedLookupSession(unittest.TestCase):
    """Tests for AssessmentOfferedLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedLookupSession tests'
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_lookup_assessments_offered(self):
        """Tests can_lookup_assessments_offered"""
        self.assertTrue(isinstance(self.catalog.can_lookup_assessments_offered(), bool))

    def test_use_comparative_assessment_offered_view(self):
        """Tests use_comparative_assessment_offered_view"""
        self.catalog.use_comparative_assessment_offered_view()

    def test_use_plenary_assessment_offered_view(self):
        """Tests use_plenary_assessment_offered_view"""
        self.catalog.use_plenary_assessment_offered_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_offered(self):
        """Tests get_assessment_offered"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_offered_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment_offered(self.assessment_offered_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_offered_list[0].ident)

    def test_get_assessments_offered_by_ids(self):
        """Tests get_assessments_offered_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_ids(self.assessment_offered_ids)

    def test_get_assessments_offered_by_genus_type(self):
        """Tests get_assessments_offered_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_genus_type(DEFAULT_TYPE)

    def test_get_assessments_offered_by_parent_genus_type(self):
        """Tests get_assessments_offered_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_assessments_offered_by_record_type(self):
        """Tests get_assessments_offered_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_assessments_offered_by_date(self):
        """Tests get_assessments_offered_by_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_offered_for_assessment(self):
        """Tests get_assessments_offered_for_assessment"""
        pass

    def test_get_assessments_offered(self):
        """Tests get_assessments_offered"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList
        objects = self.catalog.get_assessments_offered()
        self.assertTrue(isinstance(objects, AssessmentOfferedList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_offered()

    def test_get_assessment_offered_with_alias(self):
        self.catalog.alias_assessment_offered(self.assessment_offered_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment_offered(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_offered_ids[0])


class TestAssessmentOfferedQuerySession(unittest.TestCase):
    """Tests for AssessmentOfferedQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + color
            create_form.description = (
                'Test AssessmentOffered for AssessmentOfferedQuerySession tests, did I mention green')
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_search_assessments_offered(self):
        """Tests can_search_assessments_offered"""
        pass

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_offered_query(self):
        """Tests get_assessment_offered_query"""
        query = self.catalog.get_assessment_offered_query()

    def test_get_assessments_offered_by_query(self):
        """Tests get_assessments_offered_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_assessment_offered_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessments_offered_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_assessments_offered_by_query(query).available(), 3)


class TestAssessmentOfferedAdminSession(unittest.TestCase):
    """Tests for AssessmentOfferedAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_create_assessments_offered(self):
        """Tests can_create_assessments_offered"""
        self.assertTrue(isinstance(self.catalog.can_create_assessments_offered(), bool))

    def test_can_create_assessment_offered_with_record_types(self):
        """Tests can_create_assessment_offered_with_record_types"""
        self.assertTrue(isinstance(self.catalog.can_create_assessment_offered_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_form_for_create(self):
        """Tests get_assessment_offered_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_assessment_offered(self):
        """Tests create_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_assessments_offered(self):
        """Tests can_update_assessments_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_form_for_update(self):
        """Tests get_assessment_offered_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_assessment_offered(self):
        """Tests update_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_assessments_offered(self):
        """Tests can_delete_assessments_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_assessment_offered(self):
        """Tests delete_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_manage_assessment_offered_aliases(self):
        """Tests can_manage_assessment_offered_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_assessment_offered(self):
        """Tests alias_assessment_offered"""
        pass


class TestAssessmentOfferedBankSession(unittest.TestCase):
    """Tests for AssessmentOfferedBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_offered_list = list()
        cls.assessment_offered_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentOfferedBankSession tests'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedBankSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
            create_form.display_name = 'Test AssessmentOffered ' + str(num)
            create_form.description = 'Test AssessmentOffered for AssessmentOfferedBankSession tests'
            obj = cls.catalog.create_assessment_offered(create_form)
            cls.assessment_offered_list.append(obj)
            cls.assessment_offered_ids.append(obj.ident)
        cls.svc_mgr.assign_assessment_offered_to_bank(
            cls.assessment_offered_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_assessment_offered_to_bank(
            cls.assessment_offered_ids[2], cls.assigned_catalog.ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_assessment_offered_from_bank(
            cls.assessment_offered_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_assessment_offered_from_bank(
            cls.assessment_offered_ids[2], cls.assigned_catalog.ident)
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_assessment_offered_bank_mappings(self):
        """Tests can_lookup_assessment_offered_bank_mappings"""
        pass

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_offered_ids_by_bank(self):
        """Tests get_assessment_offered_ids_by_bank"""
        objects = self.svc_mgr.get_assessment_offered_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_assessments_offered_by_bank(self):
        """Tests get_assessments_offered_by_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_ids_by_banks(self):
        """Tests get_assessment_offered_ids_by_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_offered_by_banks(self):
        """Tests get_assessments_offered_by_banks"""
        pass

    def test_get_bank_ids_by_assessment_offered(self):
        """Tests get_bank_ids_by_assessment_offered"""
        cats = self.svc_mgr.get_bank_ids_by_assessment_offered(self.assessment_offered_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_assessment_offered(self):
        """Tests get_banks_by_assessment_offered"""
        cats = self.svc_mgr.get_banks_by_assessment_offered(self.assessment_offered_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssessmentOfferedBankAssignmentSession(unittest.TestCase):
    """Tests for AssessmentOfferedBankAssignmentSession"""

    @unittest.skip('unimplemented test')
    def test_can_assign_assessments_offered(self):
        """Tests can_assign_assessments_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_assign_assessments_offered_to_bank(self):
        """Tests can_assign_assessments_offered_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids_for_assessment_offered(self):
        """Tests get_assignable_bank_ids_for_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_assign_assessment_offered_to_bank(self):
        """Tests assign_assessment_offered_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_unassign_assessment_offered_from_bank(self):
        """Tests unassign_assessment_offered_from_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_reassign_assessment_offered_to_billing(self):
        """Tests reassign_assessment_offered_to_billing"""
        pass


class TestAssessmentTakenLookupSession(unittest.TestCase):
    """Tests for AssessmentTakenLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentOfferedLookupSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenLookupSession tests'
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_taken():
                catalog.delete_assessment_taken(obj.ident)
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_lookup_assessments_taken(self):
        """Tests can_lookup_assessments_taken"""
        self.assertTrue(isinstance(self.catalog.can_lookup_assessments_taken(), bool))

    def test_use_comparative_assessment_taken_view(self):
        """Tests use_comparative_assessment_taken_view"""
        self.catalog.use_comparative_assessment_taken_view()

    def test_use_plenary_assessment_taken_view(self):
        """Tests use_plenary_assessment_taken_view"""
        self.catalog.use_plenary_assessment_taken_view()

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_taken(self):
        """Tests get_assessment_taken"""
        # From test_templates/resource.py ResourceLookupSession.get_resource_template
        self.catalog.use_isolated_bank_view()
        obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_taken_list[0].ident)
        self.catalog.use_federated_bank_view()
        obj = self.catalog.get_assessment_taken(self.assessment_taken_list[0].ident)
        self.assertEqual(obj.ident, self.assessment_taken_list[0].ident)

    def test_get_assessments_taken_by_ids(self):
        """Tests get_assessments_taken_by_ids"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_ids_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_ids(self.assessment_taken_ids)

    def test_get_assessments_taken_by_genus_type(self):
        """Tests get_assessments_taken_by_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_genus_type(DEFAULT_TYPE)

    def test_get_assessments_taken_by_parent_genus_type(self):
        """Tests get_assessments_taken_by_parent_genus_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_parent_genus_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_parent_genus_type(DEFAULT_TYPE)

    def test_get_assessments_taken_by_record_type(self):
        """Tests get_assessments_taken_by_record_type"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_by_record_type_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken_by_record_type(DEFAULT_TYPE)

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_date(self):
        """Tests get_assessments_taken_by_date"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_for_taker(self):
        """Tests get_assessments_taken_for_taker"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_date_for_taker(self):
        """Tests get_assessments_taken_by_date_for_taker"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_for_assessment(self):
        """Tests get_assessments_taken_for_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_date_for_assessment(self):
        """Tests get_assessments_taken_by_date_for_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_for_taker_and_assessment(self):
        """Tests get_assessments_taken_for_taker_and_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_date_for_taker_and_assessment(self):
        """Tests get_assessments_taken_by_date_for_taker_and_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_for_assessment_offered(self):
        """Tests get_assessments_taken_for_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_date_for_assessment_offered(self):
        """Tests get_assessments_taken_by_date_for_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_for_taker_and_assessment_offered(self):
        """Tests get_assessments_taken_for_taker_and_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_date_for_taker_and_assessment_offered(self):
        """Tests get_assessments_taken_by_date_for_taker_and_assessment_offered"""
        pass

    def test_get_assessments_taken(self):
        """Tests get_assessments_taken"""
        # From test_templates/resource.py ResourceLookupSession.get_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList
        objects = self.catalog.get_assessments_taken()
        self.assertTrue(isinstance(objects, AssessmentTakenList))
        self.catalog.use_federated_bank_view()
        objects = self.catalog.get_assessments_taken()

    def test_get_assessment_taken_with_alias(self):
        self.catalog.alias_assessment_taken(self.assessment_taken_ids[0], ALIAS_ID)
        obj = self.catalog.get_assessment_taken(ALIAS_ID)
        self.assertEqual(obj.get_id(), self.assessment_taken_ids[0])


class TestAssessmentTakenQuerySession(unittest.TestCase):
    """Tests for AssessmentTakenQuerySession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentOfferedLookupSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for color in ['Orange', 'Blue', 'Green', 'orange']:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + color
            create_form.description = (
                'Test AssessmentTaken for AssessmentTakenQuerySession tests, did I mention green')
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_taken():
                catalog.delete_assessment_taken(obj.ident)
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_search_assessments_taken(self):
        """Tests can_search_assessments_taken"""
        pass

    def test_use_federated_bank_view(self):
        """Tests use_federated_bank_view"""
        self.catalog.use_federated_bank_view()

    def test_use_isolated_bank_view(self):
        """Tests use_isolated_bank_view"""
        self.catalog.use_isolated_bank_view()

    def test_get_assessment_taken_query(self):
        """Tests get_assessment_taken_query"""
        query = self.catalog.get_assessment_taken_query()

    def test_get_assessments_taken_by_query(self):
        """Tests get_assessments_taken_by_query"""
        # From test_templates/resource.py ResourceQuerySession::get_resources_by_query_template
        # Need to add some tests with string types
        query = self.catalog.get_assessment_taken_query()
        query.match_display_name('orange')
        self.assertEqual(self.catalog.get_assessments_taken_by_query(query).available(), 2)
        query.clear_display_name_terms()
        query.match_display_name('blue', match=False)
        self.assertEqual(self.catalog.get_assessments_taken_by_query(query).available(), 3)


class TestAssessmentTakenAdminSession(unittest.TestCase):
    """Tests for AssessmentTakenAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_taken():
            cls.catalog.delete_assessment_taken(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_bank_id(self):
        """Tests get_bank_id"""
        self.assertEqual(self.catalog.get_bank_id(), self.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    def test_can_create_assessments_taken(self):
        """Tests can_create_assessments_taken"""
        self.assertTrue(isinstance(self.catalog.can_create_assessments_taken(), bool))

    def test_can_create_assessment_taken_with_record_types(self):
        """Tests can_create_assessment_taken_with_record_types"""
        self.assertTrue(isinstance(self.catalog.can_create_assessment_taken_with_record_types(DEFAULT_TYPE), bool))

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_form_for_create(self):
        """Tests get_assessment_taken_form_for_create"""
        pass

    @unittest.skip('unimplemented test')
    def test_create_assessment_taken(self):
        """Tests create_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_update_assessments_taken(self):
        """Tests can_update_assessments_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_form_for_update(self):
        """Tests get_assessment_taken_form_for_update"""
        pass

    @unittest.skip('unimplemented test')
    def test_update_assessment_taken(self):
        """Tests update_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_delete_assessments_taken(self):
        """Tests can_delete_assessments_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_delete_assessment_taken(self):
        """Tests delete_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_manage_assessment_taken_aliases(self):
        """Tests can_manage_assessment_taken_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_assessment_taken(self):
        """Tests alias_assessment_taken"""
        pass


class TestAssessmentTakenBankSession(unittest.TestCase):
    """Tests for AssessmentTakenBankSession"""

    @classmethod
    def setUpClass(cls):
        cls.assessment_taken_list = list()
        cls.assessment_taken_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenBankSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank Assigned'
        create_form.description = 'Test Bank for AssessmentTakenBankSession tests'
        cls.assigned_catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenBankSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)
        create_form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        create_form.display_name = 'Test AssessmentOffered'
        create_form.description = 'Test AssessmentOffered for AssessmentTakenLBankSession tests'
        cls.assessment_offered = cls.catalog.create_assessment_offered(create_form)
        for num in [0, 1, 2]:
            create_form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])
            create_form.display_name = 'Test AssessmentTaken ' + str(num)
            create_form.description = 'Test AssessmentTaken for AssessmentTakenLookupSession tests'
            obj = cls.catalog.create_assessment_taken(create_form)
            cls.assessment_taken_list.append(obj)
            cls.assessment_taken_ids.append(obj.ident)
        cls.svc_mgr.assign_assessment_taken_to_bank(
            cls.assessment_taken_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.assign_assessment_taken_to_bank(
            cls.assessment_taken_ids[2], cls.assigned_catalog.ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.unassign_assessment_taken_from_bank(
            cls.assessment_taken_ids[1], cls.assigned_catalog.ident)
        cls.svc_mgr.unassign_assessment_taken_from_bank(
            cls.assessment_taken_ids[2], cls.assigned_catalog.ident)
        for catalog in cls.svc_mgr.get_banks():
            for obj in catalog.get_assessments_taken():
                catalog.delete_assessment_taken(obj.ident)
            for obj in catalog.get_assessments_offered():
                catalog.delete_assessment_offered(obj.ident)
            for obj in catalog.get_assessments():
                catalog.delete_assessment(obj.ident)
            cls.svc_mgr.delete_bank(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_assessment_taken_bank_mappings(self):
        """Tests can_lookup_assessment_taken_bank_mappings"""
        pass

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        self.svc_mgr.use_plenary_bank_view()

    def test_get_assessment_taken_ids_by_bank(self):
        """Tests get_assessment_taken_ids_by_bank"""
        objects = self.svc_mgr.get_assessment_taken_ids_by_bank(self.assigned_catalog.ident)
        self.assertEqual(objects.available(), 2)

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_bank(self):
        """Tests get_assessments_taken_by_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_ids_by_banks(self):
        """Tests get_assessment_taken_ids_by_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_taken_by_banks(self):
        """Tests get_assessments_taken_by_banks"""
        pass

    def test_get_bank_ids_by_assessment_taken(self):
        """Tests get_bank_ids_by_assessment_taken"""
        cats = self.svc_mgr.get_bank_ids_by_assessment_taken(self.assessment_taken_ids[1])
        self.assertEqual(cats.available(), 2)

    def test_get_banks_by_assessment_taken(self):
        """Tests get_banks_by_assessment_taken"""
        cats = self.svc_mgr.get_banks_by_assessment_taken(self.assessment_taken_ids[1])
        self.assertEqual(cats.available(), 2)


class TestAssessmentTakenBankAssignmentSession(unittest.TestCase):
    """Tests for AssessmentTakenBankAssignmentSession"""

    @unittest.skip('unimplemented test')
    def test_can_assign_assessments_taken(self):
        """Tests can_assign_assessments_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_can_assign_assessments_taken_to_bank(self):
        """Tests can_assign_assessments_taken_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids(self):
        """Tests get_assignable_bank_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assignable_bank_ids_for_assessment_taken(self):
        """Tests get_assignable_bank_ids_for_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_assign_assessment_taken_to_bank(self):
        """Tests assign_assessment_taken_to_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_unassign_assessment_taken_from_bank(self):
        """Tests unassign_assessment_taken_from_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_reassign_assessment_taken_to_billing(self):
        """Tests reassign_assessment_taken_to_billing"""
        pass


class TestBankLookupSession(unittest.TestCase):
    """Tests for BankLookupSession"""

    @classmethod
    def setUpClass(cls):
        cls.catalogs = list()
        cls.catalog_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        for num in [0, 1]:
            create_form = cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for assessment proxy manager tests'
            catalog = cls.svc_mgr.create_bank(create_form)
            cls.catalogs.append(catalog)
            cls.catalog_ids.append(catalog.ident)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            cls.svc_mgr.delete_bank(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_can_lookup_banks(self):
        """Tests can_lookup_banks"""
        pass

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        self.svc_mgr.use_plenary_bank_view()

    def test_get_bank(self):
        """Tests get_bank"""
        catalog = self.svc_mgr.get_bank(self.catalogs[0].ident)
        self.assertEqual(catalog.ident, self.catalogs[0].ident)

    def test_get_banks_by_ids(self):
        """Tests get_banks_by_ids"""
        catalogs = self.svc_mgr.get_banks_by_ids(self.catalog_ids)

    @unittest.skip('unimplemented test')
    def test_get_banks_by_genus_type(self):
        """Tests get_banks_by_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_banks_by_parent_genus_type(self):
        """Tests get_banks_by_parent_genus_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_banks_by_record_type(self):
        """Tests get_banks_by_record_type"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_banks_by_provider(self):
        """Tests get_banks_by_provider"""
        pass

    def test_get_banks(self):
        """Tests get_banks"""
        catalogs = self.svc_mgr.get_banks()


class TestBankQuerySession(unittest.TestCase):
    """Tests for BankQuerySession"""

    @unittest.skip('unimplemented test')
    def test_can_search_banks(self):
        """Tests can_search_banks"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_bank_query(self):
        """Tests get_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_banks_by_query(self):
        """Tests get_banks_by_query"""
        pass


class TestBankAdminSession(unittest.TestCase):
    """Tests for BankAdminSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        # Initialize test catalog:
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankAdminSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        # Initialize catalog to be deleted:
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank For Deletion'
        create_form.description = 'Test Bank for BankAdminSession deletion test'
        cls.catalog_to_delete = cls.svc_mgr.create_bank(create_form)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_banks():
            cls.svc_mgr.delete_bank(catalog.ident)

    def test_can_create_banks(self):
        """Tests can_create_banks"""
        # From test_templates/resource.py BinAdminSession.can_create_bins_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_banks(), bool))

    def test_can_create_bank_with_record_types(self):
        """Tests can_create_bank_with_record_types"""
        # From test_templates/resource.py BinAdminSession.can_create_bin_with_record_types_template
        self.assertTrue(isinstance(self.svc_mgr.can_create_bank_with_record_types(DEFAULT_TYPE), bool))

    def test_get_bank_form_for_create(self):
        """Tests get_bank_form_for_create"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_create_template
        from dlkit.abstract_osid.assessment.objects import BankForm
        catalog_form = self.svc_mgr.get_bank_form_for_create([])
        self.assertTrue(isinstance(catalog_form, BankForm))
        self.assertFalse(catalog_form.is_for_update())

    def test_create_bank(self):
        """Tests create_bank"""
        # From test_templates/resource.py BinAdminSession.create_bin_template
        from dlkit.abstract_osid.assessment.objects import Bank
        catalog_form = self.svc_mgr.get_bank_form_for_create([])
        catalog_form.display_name = 'Test Bank'
        catalog_form.description = 'Test Bank for BankAdminSession.create_bank tests'
        new_catalog = self.svc_mgr.create_bank(catalog_form)
        self.assertTrue(isinstance(new_catalog, Bank))

    @unittest.skip('unimplemented test')
    def test_can_update_banks(self):
        """Tests can_update_banks"""
        pass

    def test_get_bank_form_for_update(self):
        """Tests get_bank_form_for_update"""
        # From test_templates/resource.py BinAdminSession.get_bin_form_for_update_template
        from dlkit.abstract_osid.assessment.objects import BankForm
        catalog_form = self.svc_mgr.get_bank_form_for_update(self.catalog.ident)
        self.assertTrue(isinstance(catalog_form, BankForm))
        self.assertTrue(catalog_form.is_for_update())

    def test_update_bank(self):
        """Tests update_bank"""
        # From test_templates/resource.py BinAdminSession.update_bin_template
        catalog_form = self.svc_mgr.get_bank_form_for_update(self.catalog.ident)
        # Update some elements here?
        self.svc_mgr.update_bank(catalog_form)

    @unittest.skip('unimplemented test')
    def test_can_delete_banks(self):
        """Tests can_delete_banks"""
        pass

    def test_delete_bank(self):
        """Tests delete_bank"""
        # From test_templates/resource.py BinAdminSession.delete_bin_template
        cat_id = self.catalog_to_delete.ident
        self.svc_mgr.delete_bank(cat_id)
        with self.assertRaises(errors.NotFound):
            self.svc_mgr.get_bank(cat_id)

    @unittest.skip('unimplemented test')
    def test_can_manage_bank_aliases(self):
        """Tests can_manage_bank_aliases"""
        pass

    @unittest.skip('unimplemented test')
    def test_alias_bank(self):
        """Tests alias_bank"""
        pass


class TestBankHierarchySession(unittest.TestCase):
    """Tests for BankHierarchySession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bank ' + name
            cls.catalogs[name] = cls.svc_mgr.create_bank(create_form)
        cls.svc_mgr.add_root_bank(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.remove_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_banks(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_bank(cls.catalogs[cat_name].ident)

    def test_get_bank_hierarchy_id(self):
        """Tests get_bank_hierarchy_id"""
        hierarchy_id = self.svc_mgr.get_bank_hierarchy_id()

    def test_get_bank_hierarchy(self):
        """Tests get_bank_hierarchy"""
        hierarchy = self.svc_mgr.get_bank_hierarchy()

    @unittest.skip('unimplemented test')
    def test_can_access_bank_hierarchy(self):
        """Tests can_access_bank_hierarchy"""
        pass

    def test_use_comparative_bank_view(self):
        """Tests use_comparative_bank_view"""
        self.svc_mgr.use_comparative_bank_view()

    def test_use_plenary_bank_view(self):
        """Tests use_plenary_bank_view"""
        self.svc_mgr.use_plenary_bank_view()

    def test_get_root_bank_ids(self):
        """Tests get_root_bank_ids"""
        root_ids = self.svc_mgr.get_root_bank_ids()

    def test_get_root_banks(self):
        """Tests get_root_banks"""
        roots = self.svc_mgr.get_root_banks()

    def test_has_parent_banks(self):
        """Tests has_parent_banks"""
        self.assertTrue(isinstance(self.svc_mgr.has_parent_banks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_parent_banks(self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.has_parent_banks(self.catalogs['Child 2'].ident))
        self.assertTrue(self.svc_mgr.has_parent_banks(self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.has_parent_banks(self.catalogs['Root'].ident))

    def test_is_parent_of_bank(self):
        """Tests is_parent_of_bank"""
        self.assertTrue(isinstance(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_parent_of_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))
        self.assertTrue(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Grandchild 1'].ident))
        self.assertFalse(self.svc_mgr.is_parent_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))

    def test_get_parent_bank_ids(self):
        """Tests get_parent_bank_ids"""
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_parent_bank_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_parent_banks(self):
        """Tests get_parent_banks"""
        from dlkit.abstract_osid.assessment.objects import BankList
        catalog_list = self.svc_mgr.get_parent_banks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BankList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Root')

    @unittest.skip('unimplemented test')
    def test_is_ancestor_of_bank(self):
        """Tests is_ancestor_of_bank"""
        pass

    def test_has_child_banks(self):
        """Tests has_child_banks"""
        self.assertTrue(isinstance(self.svc_mgr.has_child_banks(self.catalogs['Child 1'].ident), bool))
        self.assertTrue(self.svc_mgr.has_child_banks(self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.has_child_banks(self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.has_child_banks(self.catalogs['Child 2'].ident))
        self.assertFalse(self.svc_mgr.has_child_banks(self.catalogs['Grandchild 1'].ident))

    def test_is_child_of_bank(self):
        """Tests is_child_of_bank"""
        self.assertTrue(isinstance(self.svc_mgr.is_child_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident), bool))
        self.assertTrue(self.svc_mgr.is_child_of_bank(self.catalogs['Child 1'].ident, self.catalogs['Root'].ident))
        self.assertTrue(self.svc_mgr.is_child_of_bank(self.catalogs['Grandchild 1'].ident, self.catalogs['Child 1'].ident))
        self.assertFalse(self.svc_mgr.is_child_of_bank(self.catalogs['Root'].ident, self.catalogs['Child 1'].ident))

    def test_get_child_bank_ids(self):
        """Tests get_child_bank_ids"""
        from dlkit.abstract_osid.id.objects import IdList
        catalog_list = self.svc_mgr.get_child_bank_ids(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, IdList))
        self.assertEqual(catalog_list.available(), 1)

    def test_get_child_banks(self):
        """Tests get_child_banks"""
        from dlkit.abstract_osid.assessment.objects import BankList
        catalog_list = self.svc_mgr.get_child_banks(self.catalogs['Child 1'].ident)
        self.assertTrue(isinstance(catalog_list, BankList))
        self.assertEqual(catalog_list.available(), 1)
        self.assertEqual(catalog_list.next().display_name.text, 'Grandchild 1')

    @unittest.skip('unimplemented test')
    def test_is_descendant_of_bank(self):
        """Tests is_descendant_of_bank"""
        pass

    def test_get_bank_node_ids(self):
        """Tests get_bank_node_ids"""
        node_ids = self.svc_mgr.get_bank_node_ids(self.catalogs['Child 1'].ident, 1, 2, False)
        # add some tests on the returned node

    def test_get_bank_nodes(self):
        """Tests get_bank_nodes"""
        nodes = self.svc_mgr.get_bank_nodes(self.catalogs['Child 1'].ident, 1, 2, False)
        # add some tests on the returned node


class TestBankHierarchyDesignSession(unittest.TestCase):
    """Tests for BankHierarchyDesignSession"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        cls.catalogs = dict()
        for name in ['Root', 'Child 1', 'Child 2', 'Grandchild 1']:
            create_form = cls.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = name
            create_form.description = 'Test Bank ' + name
            cls.catalogs[name] = cls.svc_mgr.create_bank(create_form)
        cls.svc_mgr.add_root_bank(cls.catalogs['Root'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 1'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Root'].ident, cls.catalogs['Child 2'].ident)
        cls.svc_mgr.add_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.remove_child_bank(cls.catalogs['Child 1'].ident, cls.catalogs['Grandchild 1'].ident)
        cls.svc_mgr.remove_child_banks(cls.catalogs['Root'].ident)
        for cat_name in cls.catalogs:
            cls.svc_mgr.delete_bank(cls.catalogs[cat_name].ident)

    def test_get_bank_hierarchy_id(self):
        """Tests get_bank_hierarchy_id"""
        hierarchy_id = self.svc_mgr.get_bank_hierarchy_id()

    def test_get_bank_hierarchy(self):
        """Tests get_bank_hierarchy"""
        hierarchy = self.svc_mgr.get_bank_hierarchy()

    @unittest.skip('unimplemented test')
    def test_can_modify_bank_hierarchy(self):
        """Tests can_modify_bank_hierarchy"""
        pass

    @unittest.skip('unimplemented test')
    def test_add_root_bank(self):
        """Tests add_root_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_remove_root_bank(self):
        """Tests remove_root_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_add_child_bank(self):
        """Tests add_child_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_remove_child_bank(self):
        """Tests remove_child_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_remove_child_banks(self):
        """Tests remove_child_banks"""
        pass
