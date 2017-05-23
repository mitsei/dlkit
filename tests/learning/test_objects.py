"""Unit tests of learning objects."""


import unittest


from dlkit.abstract_osid.osid import errors
from dlkit.json_.osid.metadata import Metadata
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

    @classmethod
    def setUpClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        # From test_templates/resource.py::ResourceForm::init_template
        self.form = self.catalog.get_objective_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/resource.py::ResourceForm::init_template
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_assessment_metadata(self):
        """Tests get_assessment_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_assessment_metadata(), Metadata))

    def test_set_assessment(self):
        """Tests set_assessment"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['assessmentId'], '')
        self.form.set_assessment(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['assessmentId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_assessment(self):
        """Tests clear_assessment"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_assessment(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['assessmentId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_assessment()
        self.assertEqual(self.form._my_map['assessmentId'], '')

    def test_get_knowledge_category_metadata(self):
        """Tests get_knowledge_category_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_knowledge_category_metadata(), Metadata))

    def test_set_knowledge_category(self):
        """Tests set_knowledge_category"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['knowledgeCategoryId'], '')
        self.form.set_knowledge_category(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['knowledgeCategoryId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_knowledge_category(self):
        """Tests clear_knowledge_category"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_knowledge_category(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['knowledgeCategoryId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_knowledge_category()
        self.assertEqual(self.form._my_map['knowledgeCategoryId'], '')

    def test_get_cognitive_process_metadata(self):
        """Tests get_cognitive_process_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_cognitive_process_metadata(), Metadata))

    def test_set_cognitive_process(self):
        """Tests set_cognitive_process"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['cognitiveProcessId'], '')
        self.form.set_cognitive_process(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['cognitiveProcessId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_cognitive_process(self):
        """Tests clear_cognitive_process"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_cognitive_process(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['cognitiveProcessId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_cognitive_process()
        self.assertEqual(self.form._my_map['cognitiveProcessId'], '')

    def test_get_objective_form_record(self):
        """Tests get_objective_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_objective_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestObjectiveList(unittest.TestCase):
    """Tests for ObjectiveList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveList tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.learning.objects import ObjectiveList
        self.objective_list = list()
        self.objective_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveList tests'
            obj = self.catalog.create_objective(create_form)
            self.objective_list.append(obj)
            self.objective_ids.append(obj.ident)
        self.objective_list = ObjectiveList(self.objective_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_next_objective(self):
        """Tests get_next_objective"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import Objective
        self.assertTrue(isinstance(self.objective_list.get_next_objective(), Objective))

    def test_get_next_objectives(self):
        """Tests get_next_objectives"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveList, Objective
        new_list = self.objective_list.get_next_objectives(2)
        self.assertTrue(isinstance(new_list, ObjectiveList))
        for item in new_list:
            self.assertTrue(isinstance(item, Objective))


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

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveNodeList tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        cls.objective_node_ids = list()

    def setUp(self):
        from dlkit.json_.learning.objects import ObjectiveNodeList, ObjectiveNode
        self.objective_node_list = list()
        for num in [0, 1]:
            create_form = self.catalog.get_objective_form_for_create([])
            create_form.display_name = 'Test Objective ' + str(num)
            create_form.description = 'Test Objective for ObjectiveNodeList tests'
            obj = self.catalog.create_objective(create_form)
            self.objective_node_list.append(ObjectiveNode(obj.object_map))
            self.objective_node_ids.append(obj.ident)
        # Not put the objectives in a hierarchy
        self.catalog.add_root_objective(self.objective_node_list[0].ident)
        self.catalog.add_child_objective(
            self.objective_node_list[0].ident,
            self.objective_node_list[1].ident)
        self.objective_node_list = ObjectiveNodeList(self.objective_node_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_objectives():
            cls.catalog.delete_objective(obj.ident)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_next_objective_node(self):
        """Tests get_next_objective_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import ObjectiveNode
        self.assertTrue(isinstance(self.objective_node_list.get_next_objective_node(), ObjectiveNode))

    def test_get_next_objective_nodes(self):
        """Tests get_next_objective_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveNodeList, ObjectiveNode
        new_list = self.objective_node_list.get_next_objective_nodes(2)
        self.assertTrue(isinstance(new_list, ObjectiveNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, ObjectiveNode))


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

    @classmethod
    def setUpClass(cls):
        # From test_templates/learning.py::ActivityForm::init_template
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityForm tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityForm tests'
        cls.objective = cls.catalog.create_objective(create_form)

        cls.form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])

    @classmethod
    def tearDownClass(cls):
        # From test_templates/learning.py::ActivityForm::init_template
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_activities():
                catalog.delete_activity(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_assets_metadata(self):
        """Tests get_assets_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        self.assertTrue(isinstance(self.form.get_assets_metadata(), Metadata))

    def test_set_assets(self):
        """Tests set_assets"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_assets([test_id])
        self.assertTrue(len(self.form._my_map['assetIds']), 1)
        self.assertEqual(self.form._my_map['assetIds'][0],
                         str(test_id))
        # reset this for other tests
        self.form._my_map['assetIds'] = list()

    def test_clear_assets(self):
        """Tests clear_assets"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_assets([test_id])
        self.assertTrue(len(self.form._my_map['assetIds']), 1)
        self.assertEqual(self.form._my_map['assetIds'][0],
                         str(test_id))
        self.form.clear_assets()
        self.assertEqual(self.form._my_map['assetIds'], [])

    def test_get_courses_metadata(self):
        """Tests get_courses_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        self.assertTrue(isinstance(self.form.get_courses_metadata(), Metadata))

    def test_set_courses(self):
        """Tests set_courses"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_courses([test_id])
        self.assertTrue(len(self.form._my_map['courseIds']), 1)
        self.assertEqual(self.form._my_map['courseIds'][0],
                         str(test_id))
        # reset this for other tests
        self.form._my_map['courseIds'] = list()

    def test_clear_courses(self):
        """Tests clear_courses"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_courses([test_id])
        self.assertTrue(len(self.form._my_map['courseIds']), 1)
        self.assertEqual(self.form._my_map['courseIds'][0],
                         str(test_id))
        self.form.clear_courses()
        self.assertEqual(self.form._my_map['courseIds'], [])

    def test_get_assessments_metadata(self):
        """Tests get_assessments_metadata"""
        # From test_templates/learning.py::ActivityForm::get_assets_metadata_template
        self.assertTrue(isinstance(self.form.get_assessments_metadata(), Metadata))

    def test_set_assessments(self):
        """Tests set_assessments"""
        # From test_templates/learning.py::ActivityForm::set_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_assessments([test_id])
        self.assertTrue(len(self.form._my_map['assessmentIds']), 1)
        self.assertEqual(self.form._my_map['assessmentIds'][0],
                         str(test_id))
        # reset this for other tests
        self.form._my_map['assessmentIds'] = list()

    def test_clear_assessments(self):
        """Tests clear_assessments"""
        # From test_templates/learning.py::ActivityForm::clear_assets_template
        test_id = Id('osid.Osid%3A1%40ODL.MIT.EDU')
        self.form.set_assessments([test_id])
        self.assertTrue(len(self.form._my_map['assessmentIds']), 1)
        self.assertEqual(self.form._my_map['assessmentIds'][0],
                         str(test_id))
        self.form.clear_assessments()
        self.assertEqual(self.form._my_map['assessmentIds'], [])

    def test_get_activity_form_record(self):
        """Tests get_activity_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_activity_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestActivityList(unittest.TestCase):
    """Tests for ActivityList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ActivityList tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        create_form = cls.catalog.get_objective_form_for_create([])
        create_form.display_name = 'Test Objective for Activity Lookup'
        create_form.description = 'Test Objective for ActivityList tests'
        cls.objective = cls.catalog.create_objective(create_form)

        cls.form = cls.catalog.get_activity_form_for_create(cls.objective.ident, [])

    def setUp(self):
        from dlkit.json_.learning.objects import ActivityList
        self.activity_list = list()
        self.activity_ids = list()
        for num in [0, 1]:
            form = self.catalog.get_activity_form_for_create(self.objective.ident, [])
            form.display_name = 'Test Activity ' + str(num)
            form.description = 'Test Activity for ActivityList tests'
            obj = self.catalog.create_activity(form)

            self.activity_list.append(obj)
            self.activity_ids.append(obj.ident)
        self.activity_list = ActivityList(self.activity_list)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_activities():
                catalog.delete_activity(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_next_activity(self):
        """Tests get_next_activity"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import Activity
        self.assertTrue(isinstance(self.activity_list.get_next_activity(), Activity))

    def test_get_next_activities(self):
        """Tests get_next_activities"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ActivityList, Activity
        new_list = self.activity_list.get_next_activities(2)
        self.assertTrue(isinstance(new_list, ActivityList))
        for item in new_list:
            self.assertTrue(isinstance(item, Activity))


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

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyForm tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        objective = cls.catalog.create_objective(form)

        cls.form = cls.catalog.get_proficiency_form_for_create(objective.ident, AGENT_ID, [])

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_proficiencies():
                catalog.delete_proficiency(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_completion_metadata(self):
        """Tests get_completion_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_completion_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_completion(self):
        """Tests set_completion"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_completion(self):
        """Tests clear_completion"""
        pass

    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_level_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_level(self):
        """Tests set_level"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_level(self):
        """Tests clear_level"""
        pass

    def test_get_proficiency_form_record(self):
        """Tests get_proficiency_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_proficiency_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestProficiencyList(unittest.TestCase):
    """Tests for ProficiencyList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ProficiencyList tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)

        form = cls.catalog.get_objective_form_for_create([])
        form.display_name = "Test LO"
        cls.objective = cls.catalog.create_objective(form)

        cls.form = cls.catalog.get_proficiency_form_for_create(cls.objective.ident, AGENT_ID, [])

    def setUp(self):
        from dlkit.json_.learning.objects import ProficiencyList
        self.proficiency_list = list()
        self.proficiency_ids = list()
        for num in [0, 1]:
            form = self.catalog.get_proficiency_form_for_create(self.objective.ident, AGENT_ID, [])
            form.display_name = 'Test Proficiency ' + str(num)
            form.description = 'Test Proficiency for ProficiencyList tests'
            obj = self.catalog.create_proficiency(form)

            self.proficiency_list.append(obj)
            self.proficiency_ids.append(obj.ident)
        self.proficiency_list = ProficiencyList(self.proficiency_list)

    @classmethod
    def tearDownClass(cls):
        for catalog in cls.svc_mgr.get_objective_banks():
            for obj in catalog.get_proficiencies():
                catalog.delete_proficiency(obj.ident)
            for obj in catalog.get_objectives():
                catalog.delete_objective(obj.ident)
            cls.svc_mgr.delete_objective_bank(catalog.ident)

    def test_get_next_proficiency(self):
        """Tests get_next_proficiency"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import Proficiency
        self.assertTrue(isinstance(self.proficiency_list.get_next_proficiency(), Proficiency))

    def test_get_next_proficiencies(self):
        """Tests get_next_proficiencies"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ProficiencyList, Proficiency
        new_list = self.proficiency_list.get_next_proficiencies(2)
        self.assertTrue(isinstance(new_list, ProficiencyList))
        for item in new_list:
            self.assertTrue(isinstance(item, Proficiency))


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

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankList tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        cls.objective_bank_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.learning.objects import ObjectiveBankList
        self.objective_bank_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for ObjectiveBankList tests'
            obj = self.svc_mgr.create_objective_bank(create_form)
            self.objective_bank_list.append(obj)
            self.objective_bank_ids.append(obj.ident)
        self.objective_bank_list = ObjectiveBankList(self.objective_bank_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.objective_bank_ids:
            cls.svc_mgr.delete_objective_bank(obj)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_next_objective_bank(self):
        """Tests get_next_objective_bank"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBank
        self.assertTrue(isinstance(self.objective_bank_list.get_next_objective_bank(), ObjectiveBank))

    def test_get_next_objective_banks(self):
        """Tests get_next_objective_banks"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankList, ObjectiveBank
        new_list = self.objective_bank_list.get_next_objective_banks(2)
        self.assertTrue(isinstance(new_list, ObjectiveBankList))
        for item in new_list:
            self.assertTrue(isinstance(item, ObjectiveBank))


class TestObjectiveBankNode(unittest.TestCase):
    """Tests for ObjectiveBankNode"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNode
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankNode tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        cls.objective_bank_ids = list()

    def setUp(self):
        # Implemented from init template for BinNode
        from dlkit.json_.learning.objects import ObjectiveBankNode
        self.objective_bank_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBank ' + str(num)
            create_form.description = 'Test ObjectiveBank for ObjectiveBankNode tests'
            obj = self.svc_mgr.create_objective_bank(create_form)
            self.objective_bank_list.append(ObjectiveBankNode(
                obj.object_map,
                runtime=self.svc_mgr._runtime,
                proxy=self.svc_mgr._proxy))
            self.objective_bank_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_objective_bank(self.objective_bank_list[0].ident)
        self.svc_mgr.add_child_objective_bank(
            self.objective_bank_list[0].ident,
            self.objective_bank_list[1].ident)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNode
        for obj in cls.objective_bank_ids:
            cls.svc_mgr.delete_objective_bank(obj)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_objective_bank(self):
        """Tests get_objective_bank"""
        # from test_templates/resource.py::BinNode::get_bin_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBank
        self.assertTrue(isinstance(self.objective_bank_list[0].get_objective_bank(), ObjectiveBank))
        self.assertEqual(str(self.objective_bank_list[0].get_objective_bank().ident),
                         str(self.objective_bank_list[0].ident))

    def test_get_parent_objective_bank_nodes(self):
        """Tests get_parent_objective_bank_nodes"""
        # from test_templates/resource.py::BinNode::get_parent_bin_nodes
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNodeList
        node = self.svc_mgr.get_objective_bank_nodes(
            self.objective_bank_list[1].ident,
            1,
            0,
            False)
        self.assertTrue(isinstance(node.get_parent_objective_bank_nodes(), ObjectiveBankNodeList))
        self.assertEqual(node.get_parent_objective_bank_nodes().available(),
                         1)
        self.assertEqual(str(node.get_parent_objective_bank_nodes().next().ident),
                         str(self.objective_bank_list[0].ident))

    def test_get_child_objective_bank_nodes(self):
        """Tests get_child_objective_bank_nodes"""
        # from test_templates/resource.py::BinNode::get_child_bin_nodes_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNodeList
        node = self.svc_mgr.get_objective_bank_nodes(
            self.objective_bank_list[0].ident,
            0,
            1,
            False)
        self.assertTrue(isinstance(node.get_child_objective_bank_nodes(), ObjectiveBankNodeList))
        self.assertEqual(node.get_child_objective_bank_nodes().available(),
                         1)
        self.assertEqual(str(node.get_child_objective_bank_nodes().next().ident),
                         str(self.objective_bank_list[1].ident))


class TestObjectiveBankNodeList(unittest.TestCase):
    """Tests for ObjectiveBankNodeList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNodeList
        cls.svc_mgr = Runtime().get_service_manager('LEARNING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_objective_bank_form_for_create([])
        create_form.display_name = 'Test ObjectiveBank'
        create_form.description = 'Test ObjectiveBank for ObjectiveBankNodeList tests'
        cls.catalog = cls.svc_mgr.create_objective_bank(create_form)
        cls.objective_bank_node_ids = list()

    def setUp(self):
        # Implemented from init template for BinNodeList
        from dlkit.json_.learning.objects import ObjectiveBankNodeList, ObjectiveBankNode
        self.objective_bank_node_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_objective_bank_form_for_create([])
            create_form.display_name = 'Test ObjectiveBankNode ' + str(num)
            create_form.description = 'Test ObjectiveBankNode for ObjectiveBankNodeList tests'
            obj = self.svc_mgr.create_objective_bank(create_form)
            self.objective_bank_node_list.append(ObjectiveBankNode(obj.object_map))
            self.objective_bank_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_objective_bank(self.objective_bank_node_list[0].ident)
        self.svc_mgr.add_child_objective_bank(
            self.objective_bank_node_list[0].ident,
            self.objective_bank_node_list[1].ident)
        self.objective_bank_node_list = ObjectiveBankNodeList(self.objective_bank_node_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNodeList
        for obj in cls.objective_bank_node_ids:
            cls.svc_mgr.delete_objective_bank(obj)
        cls.svc_mgr.delete_objective_bank(cls.catalog.ident)

    def test_get_next_objective_bank_node(self):
        """Tests get_next_objective_bank_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNode
        self.assertTrue(isinstance(self.objective_bank_node_list.get_next_objective_bank_node(), ObjectiveBankNode))

    def test_get_next_objective_bank_nodes(self):
        """Tests get_next_objective_bank_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.learning.objects import ObjectiveBankNodeList, ObjectiveBankNode
        new_list = self.objective_bank_node_list.get_next_objective_bank_nodes(2)
        self.assertTrue(isinstance(new_list, ObjectiveBankNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, ObjectiveBankNode))
