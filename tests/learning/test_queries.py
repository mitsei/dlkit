"""Unit tests of learning queries."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.primordium.type.primitives import Type
from dlkit.runtime import PROXY_SESSION, proxy_example
from dlkit.runtime.managers import Runtime


REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})


class TestObjectiveQuery(unittest.TestCase):
    """Tests for ObjectiveQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        cls.query = cls.catalog.get_objective_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_knowledge_category_id(self):
        """Tests match_knowledge_category_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_knowledge_category_id_terms(self):
        """Tests clear_knowledge_category_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_knowledge_category_query(self):
        """Tests supports_knowledge_category_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_knowledge_category_query(self):
        """Tests get_knowledge_category_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_knowledge_category(self):
        """Tests match_any_knowledge_category"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_knowledge_category_terms(self):
        """Tests clear_knowledge_category_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_cognitive_process_id(self):
        """Tests match_cognitive_process_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_cognitive_process_id_terms(self):
        """Tests clear_cognitive_process_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_cognitive_process_query(self):
        """Tests supports_cognitive_process_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_cognitive_process_query(self):
        """Tests get_cognitive_process_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_cognitive_process(self):
        """Tests match_any_cognitive_process"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_cognitive_process_terms(self):
        """Tests clear_cognitive_process_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_activity_id(self):
        """Tests match_activity_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_activity_id_terms(self):
        """Tests clear_activity_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_activity_query(self):
        """Tests supports_activity_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_query(self):
        """Tests get_activity_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_activity(self):
        """Tests match_any_activity"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_activity_terms(self):
        """Tests clear_activity_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_requisite_objective_id(self):
        """Tests match_requisite_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_requisite_objective_id_terms(self):
        """Tests clear_requisite_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_requisite_objective_query(self):
        """Tests supports_requisite_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_requisite_objective_query(self):
        """Tests get_requisite_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_requisite_objective(self):
        """Tests match_any_requisite_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_requisite_objective_terms(self):
        """Tests clear_requisite_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_dependent_objective_id(self):
        """Tests match_dependent_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_dependent_objective_id_terms(self):
        """Tests clear_dependent_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_depndent_objective_query(self):
        """Tests supports_depndent_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_dependent_objective_query(self):
        """Tests get_dependent_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_dependent_objective(self):
        """Tests match_any_dependent_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_dependent_objective_terms(self):
        """Tests clear_dependent_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_equivalent_objective_id(self):
        """Tests match_equivalent_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_equivalent_objective_id_terms(self):
        """Tests clear_equivalent_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_equivalent_objective_query(self):
        """Tests supports_equivalent_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_equivalent_objective_query(self):
        """Tests get_equivalent_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_equivalent_objective(self):
        """Tests match_any_equivalent_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_equivalent_objective_terms(self):
        """Tests clear_equivalent_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_objective_id(self):
        """Tests match_ancestor_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_objective_id_terms(self):
        """Tests clear_ancestor_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_objective_query(self):
        """Tests supports_ancestor_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_objective_query(self):
        """Tests get_ancestor_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_objective(self):
        """Tests match_any_ancestor_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_objective_terms(self):
        """Tests clear_ancestor_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_objective_id(self):
        """Tests match_descendant_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_objective_id_terms(self):
        """Tests clear_descendant_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_objective_query(self):
        """Tests supports_descendant_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_objective_query(self):
        """Tests get_descendant_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_objective(self):
        """Tests match_any_descendant_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_objective_terms(self):
        """Tests clear_descendant_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_objective_bank_id(self):
        """Tests match_objective_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_bank_id_terms(self):
        """Tests clear_objective_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_objective_bank_query(self):
        """Tests supports_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_query(self):
        """Tests get_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_bank_terms(self):
        """Tests clear_objective_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_query_record(self):
        """Tests get_objective_query_record"""
        pass


class TestActivityQuery(unittest.TestCase):
    """Tests for ActivityQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityLookupSession tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityLookupSession tests'
        cls.objective = cls.catalog.create_objective(create_form)

        objective_query = cls.catalog.get_objective_query()
        # cls.query = objective_query.get_activity_query()
        # Raises Unimplemented()

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_activities():
                catalog.delete_activity(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_objective_id(self):
        """Tests match_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_id_terms(self):
        """Tests clear_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_query(self):
        """Tests get_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_terms(self):
        """Tests clear_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_asset_id(self):
        """Tests match_asset_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_id_terms(self):
        """Tests clear_asset_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_asset_query(self):
        """Tests supports_asset_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_query(self):
        """Tests get_asset_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_asset(self):
        """Tests match_any_asset"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_asset_terms(self):
        """Tests clear_asset_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_course_id(self):
        """Tests match_course_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_course_id_terms(self):
        """Tests clear_course_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_course_query(self):
        """Tests supports_course_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_course_query(self):
        """Tests get_course_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_course(self):
        """Tests match_any_course"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_course_terms(self):
        """Tests clear_course_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_assessment_id(self):
        """Tests match_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_id_terms(self):
        """Tests clear_assessment_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_assessment_query(self):
        """Tests supports_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_query(self):
        """Tests get_assessment_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_assessment(self):
        """Tests match_any_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment_terms(self):
        """Tests clear_assessment_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_objective_bank_id(self):
        """Tests match_objective_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_bank_id_terms(self):
        """Tests clear_objective_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_objective_bank_query(self):
        """Tests supports_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_query(self):
        """Tests get_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_bank_terms(self):
        """Tests clear_objective_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_query_record(self):
        """Tests get_activity_query_record"""
        pass


class TestProficiencyQuery(unittest.TestCase):
    """Tests for ProficiencyQuery"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        cls.query = cls.catalog.get_proficiency_query()

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_match_resource_id(self):
        """Tests match_resource_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_resource_id_terms(self):
        """Tests clear_resource_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_resource_query(self):
        """Tests supports_resource_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource_query(self):
        """Tests get_resource_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_resource_terms(self):
        """Tests clear_resource_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_objective_id(self):
        """Tests match_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_id_terms(self):
        """Tests clear_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_query(self):
        """Tests get_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_objective(self):
        """Tests match_any_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_terms(self):
        """Tests clear_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_completion(self):
        """Tests match_completion"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_completion_terms(self):
        """Tests clear_completion_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_minimum_completion(self):
        """Tests match_minimum_completion"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_minimum_completion_terms(self):
        """Tests clear_minimum_completion_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_level_id(self):
        """Tests match_level_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level_id_terms(self):
        """Tests clear_level_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_level_query(self):
        """Tests supports_level_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_level_query(self):
        """Tests get_level_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_level(self):
        """Tests match_any_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level_terms(self):
        """Tests clear_level_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_objective_bank_id(self):
        """Tests match_objective_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_bank_id_terms(self):
        """Tests clear_objective_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_objective_bank_query(self):
        """Tests supports_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_query(self):
        """Tests get_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_bank_terms(self):
        """Tests clear_objective_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiency_query_record(self):
        """Tests get_proficiency_query_record"""
        pass


class TestObjectiveBankQuery(unittest.TestCase):
    """Tests for ObjectiveBankQuery"""

    @unittest.skip('unimplemented test')
    def test_match_objective_id(self):
        """Tests match_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_id_terms(self):
        """Tests clear_objective_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_objective_query(self):
        """Tests supports_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_query(self):
        """Tests get_objective_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_objective(self):
        """Tests match_any_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_objective_terms(self):
        """Tests clear_objective_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_activity_id(self):
        """Tests match_activity_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_activity_id_terms(self):
        """Tests clear_activity_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_activity_query(self):
        """Tests supports_activity_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_query(self):
        """Tests get_activity_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_activity(self):
        """Tests match_any_activity"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_activity_terms(self):
        """Tests clear_activity_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_ancestor_objective_bank_id(self):
        """Tests match_ancestor_objective_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_objective_bank_id_terms(self):
        """Tests clear_ancestor_objective_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_ancestor_objective_bank_query(self):
        """Tests supports_ancestor_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_ancestor_objective_bank_query(self):
        """Tests get_ancestor_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_ancestor_objective_bank(self):
        """Tests match_any_ancestor_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_ancestor_objective_bank_terms(self):
        """Tests clear_ancestor_objective_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_descendant_objective_bank_id(self):
        """Tests match_descendant_objective_bank_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_objective_bank_id_terms(self):
        """Tests clear_descendant_objective_bank_id_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_supports_descendant_objective_bank_query(self):
        """Tests supports_descendant_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_descendant_objective_bank_query(self):
        """Tests get_descendant_objective_bank_query"""
        pass

    @unittest.skip('unimplemented test')
    def test_match_any_descendant_objective_bank(self):
        """Tests match_any_descendant_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_descendant_objective_bank_terms(self):
        """Tests clear_descendant_objective_bank_terms"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_query_record(self):
        """Tests get_objective_bank_query_record"""
        pass
