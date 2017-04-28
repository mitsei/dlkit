"""Unit tests of learning objects."""


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
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})


class TestObjective(unittest.TestCase):
    """Tests for Objective"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_objective(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_has_assessment(self):
        """Tests has_assessment"""
        # From test_templates/resources.py::Resource::has_avatar_template
        self.assertTrue(isinstance(self.object.has_assessment(), bool))
        self.assertFalse(self.object.has_assessment())

    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_assessment_id)

    def test_get_assessment(self):
        """Tests get_assessment"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_assessment)

    def test_has_knowledge_category(self):
        """Tests has_knowledge_category"""
        # From test_templates/resources.py::Resource::has_avatar_template
        self.assertTrue(isinstance(self.object.has_knowledge_category(), bool))
        self.assertFalse(self.object.has_knowledge_category())

    def test_get_knowledge_category_id(self):
        """Tests get_knowledge_category_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_knowledge_category_id)

    def test_get_knowledge_category(self):
        """Tests get_knowledge_category"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_knowledge_category)

    def test_has_cognitive_process(self):
        """Tests has_cognitive_process"""
        # From test_templates/resources.py::Resource::has_avatar_template
        self.assertTrue(isinstance(self.object.has_cognitive_process(), bool))
        self.assertFalse(self.object.has_cognitive_process())

    def test_get_cognitive_process_id(self):
        """Tests get_cognitive_process_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_cognitive_process_id)

    def test_get_cognitive_process(self):
        """Tests get_cognitive_process"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_cognitive_process)

    @unittest.skip('unimplemented test')
    def test_get_objective_record(self):
        """Tests get_objective_record"""
        pass


class TestObjectiveForm(unittest.TestCase):
    """Tests for ObjectiveForm"""

    @unittest.skip('unimplemented test')
    def test_get_assessment_metadata(self):
        """Tests get_assessment_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_assessment(self):
        """Tests set_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessment(self):
        """Tests clear_assessment"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_knowledge_category_metadata(self):
        """Tests get_knowledge_category_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_knowledge_category(self):
        """Tests set_knowledge_category"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_knowledge_category(self):
        """Tests clear_knowledge_category"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_cognitive_process_metadata(self):
        """Tests get_cognitive_process_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_cognitive_process(self):
        """Tests set_cognitive_process"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_cognitive_process(self):
        """Tests clear_cognitive_process"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_form_record(self):
        """Tests get_objective_form_record"""
        pass


class TestObjectiveList(unittest.TestCase):
    """Tests for ObjectiveList"""

    @unittest.skip('unimplemented test')
    def test_get_next_objective(self):
        """Tests get_next_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_objectives(self):
        """Tests get_next_objectives"""
        pass


class TestObjectiveNode(unittest.TestCase):
    """Tests for ObjectiveNode"""

    @unittest.skip('unimplemented test')
    def test_get_objective(self):
        """Tests get_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_objective_nodes(self):
        """Tests get_parent_objective_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_objective_nodes(self):
        """Tests get_child_objective_nodes"""
        pass


class TestObjectiveNodeList(unittest.TestCase):
    """Tests for ObjectiveNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_objective_node(self):
        """Tests get_next_objective_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_objective_nodes(self):
        """Tests get_next_objective_nodes"""
        pass


class TestActivity(unittest.TestCase):
    """Tests for Activity"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = 'Objective'
        cls.objective = cls.catalog.create_objective(form)

        form = cls.catalog.get_activity_form_for_create(cls.objective.ident,
                                                        [])
        form.display_name = 'Test activity'
        cls.object = cls.catalog.create_activity(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_activities():
            cls.catalog.delete_activity(obj.ident)
        cls.catalog.delete_objective(cls.objective.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_objective_id(self):
        """Tests get_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective(self):
        """Tests get_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_asset_based_activity(self):
        """Tests is_asset_based_activity"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_asset_ids(self):
        """Tests get_asset_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assets(self):
        """Tests get_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_course_based_activity(self):
        """Tests is_course_based_activity"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_course_ids(self):
        """Tests get_course_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_courses(self):
        """Tests get_courses"""
        pass

    @unittest.skip('unimplemented test')
    def test_is_assessment_based_activity(self):
        """Tests is_assessment_based_activity"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_ids(self):
        """Tests get_assessment_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments(self):
        """Tests get_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_record(self):
        """Tests get_activity_record"""
        pass


class TestActivityForm(unittest.TestCase):
    """Tests for ActivityForm"""

    @unittest.skip('unimplemented test')
    def test_get_assets_metadata(self):
        """Tests get_assets_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_assets(self):
        """Tests set_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assets(self):
        """Tests clear_assets"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_courses_metadata(self):
        """Tests get_courses_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_courses(self):
        """Tests set_courses"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_courses(self):
        """Tests clear_courses"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessments_metadata(self):
        """Tests get_assessments_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_assessments(self):
        """Tests set_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_assessments(self):
        """Tests clear_assessments"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_activity_form_record(self):
        """Tests get_activity_form_record"""
        pass


class TestActivityList(unittest.TestCase):
    """Tests for ActivityList"""

    @unittest.skip('unimplemented test')
    def test_get_next_activity(self):
        """Tests get_next_activity"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_activities(self):
        """Tests get_next_activities"""
        pass


class TestProficiency(unittest.TestCase):
    """Tests for Proficiency"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = 'Objective'
        cls.objective = cls.catalog.create_objective(form)

        form = cls.catalog.get_proficiency_form_for_create(cls.objective.ident,
                                                           AGENT_ID,
                                                           [])
        form.display_name = 'Test proficiency'
        cls.object = cls.catalog.create_proficiency(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_proficiencies():
            cls.catalog.delete_proficiency(obj.ident)
        cls.catalog.delete_objective(cls.objective.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_resource_id(self):
        """Tests get_resource_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_resource(self):
        """Tests get_resource"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective_id(self):
        """Tests get_objective_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_objective(self):
        """Tests get_objective"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_completion(self):
        """Tests get_completion"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_level(self):
        """Tests has_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_level_id(self):
        """Tests get_level_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_level(self):
        """Tests get_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiency_record(self):
        """Tests get_proficiency_record"""
        pass


class TestProficiencyForm(unittest.TestCase):
    """Tests for ProficiencyForm"""

    @unittest.skip('unimplemented test')
    def test_get_completion_metadata(self):
        """Tests get_completion_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_completion(self):
        """Tests set_completion"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_completion(self):
        """Tests clear_completion"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_level(self):
        """Tests set_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level(self):
        """Tests clear_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_proficiency_form_record(self):
        """Tests get_proficiency_form_record"""
        pass


class TestProficiencyList(unittest.TestCase):
    """Tests for ProficiencyList"""

    @unittest.skip('unimplemented test')
    def test_get_next_proficiency(self):
        """Tests get_next_proficiency"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_proficiencies(self):
        """Tests get_next_proficiencies"""
        pass


class TestObjectiveBank(unittest.TestCase):
    """Tests for ObjectiveBank"""

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_record(self):
        """Tests get_objective_bank_record"""
        pass


class TestObjectiveBankForm(unittest.TestCase):
    """Tests for ObjectiveBankForm"""

    @unittest.skip('unimplemented test')
    def test_get_objective_bank_form_record(self):
        """Tests get_objective_bank_form_record"""
        pass


class TestObjectiveBankList(unittest.TestCase):
    """Tests for ObjectiveBankList"""

    @unittest.skip('unimplemented test')
    def test_get_next_objective_bank(self):
        """Tests get_next_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_objective_banks(self):
        """Tests get_next_objective_banks"""
        pass


class TestObjectiveBankNode(unittest.TestCase):
    """Tests for ObjectiveBankNode"""

    @unittest.skip('unimplemented test')
    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_objective_bank_nodes(self):
        """Tests get_parent_objective_bank_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_objective_bank_nodes(self):
        """Tests get_child_objective_bank_nodes"""
        pass


class TestObjectiveBankNodeList(unittest.TestCase):
    """Tests for ObjectiveBankNodeList"""

    @unittest.skip('unimplemented test')
    def test_get_next_objective_bank_node(self):
        """Tests get_next_objective_bank_node"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_objective_bank_nodes(self):
        """Tests get_next_objective_bank_nodes"""
        pass
