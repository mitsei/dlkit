"""Unit tests of assessment objects."""


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


class TestQuestion(unittest.TestCase):
    """Tests for Question"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_form = cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        cls.item = cls.catalog.create_item(item_form)

        form = cls.catalog.get_question_form_for_create(cls.item.ident, [])
        form.display_name = 'Test question'
        cls.question = cls.catalog.create_question(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_question_record(self):
        """Tests get_question_record"""
        pass


class TestQuestionForm(unittest.TestCase):
    """Tests for QuestionForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_form = cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        cls.item = cls.catalog.create_item(item_form)

        cls.form = cls.catalog.get_question_form_for_create(cls.item.ident, [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_question_form_record(self):
        """Tests get_question_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_question_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestQuestionList(unittest.TestCase):
    """Tests for QuestionList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for QuestionList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        from dlkit.json_.assessment.objects import QuestionList
        self.question_list = list()
        self.question_ids = list()
        for num in [0, 1]:
            item_form = self.catalog.get_item_form_for_create([])
            item_form.display_name = 'Item'
            item = self.catalog.create_item(item_form)

            create_form = self.catalog.get_question_form_for_create(item.ident, [])
            create_form.display_name = 'Test Question ' + str(num)
            create_form.description = 'Test Question for QuestionList tests'
            obj = self.catalog.create_question(create_form)
            self.question_list.append(obj)
            self.question_ids.append(obj.ident)
        self.question_list = QuestionList(self.question_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_question(self):
        """Tests get_next_question"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Question
        self.assertTrue(isinstance(self.question_list.get_next_question(), Question))

    def test_get_next_questions(self):
        """Tests get_next_questions"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import QuestionList, Question
        new_list = self.question_list.get_next_questions(2)
        self.assertTrue(isinstance(new_list, QuestionList))
        for item in new_list:
            self.assertTrue(isinstance(item, Question))


class TestAnswer(unittest.TestCase):
    """Tests for Answer"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_form = cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        cls.item = cls.catalog.create_item(item_form)

        form = cls.catalog.get_answer_form_for_create(cls.item.ident, [])
        form.display_name = 'Test answer'
        cls.answer = cls.catalog.create_answer(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_answer_record(self):
        """Tests get_answer_record"""
        pass


class TestAnswerForm(unittest.TestCase):
    """Tests for AnswerForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        item_form = cls.catalog.get_item_form_for_create([])
        item_form.display_name = 'Item'
        cls.item = cls.catalog.create_item(item_form)

        cls.form = cls.catalog.get_answer_form_for_create(cls.item.ident, [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_answer_form_record(self):
        """Tests get_answer_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_answer_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAnswerList(unittest.TestCase):
    """Tests for AnswerList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AnswerList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        from dlkit.json_.assessment.objects import AnswerList
        self.answer_list = list()
        self.answer_ids = list()
        for num in [0, 1]:
            item_form = self.catalog.get_item_form_for_create([])
            item_form.display_name = 'Item'
            item = self.catalog.create_item(item_form)

            create_form = self.catalog.get_answer_form_for_create(item.ident, [])
            create_form.display_name = 'Test Answer ' + str(num)
            create_form.description = 'Test Answer for AnswerList tests'
            obj = self.catalog.create_answer(create_form)
            self.answer_list.append(obj)
            self.answer_ids.append(obj.ident)
        self.answer_list = AnswerList(self.answer_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_answer(self):
        """Tests get_next_answer"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Answer
        self.assertTrue(isinstance(self.answer_list.get_next_answer(), Answer))

    def test_get_next_answers(self):
        """Tests get_next_answers"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AnswerList, Answer
        new_list = self.answer_list.get_next_answers(2)
        self.assertTrue(isinstance(new_list, AnswerList))
        for item in new_list:
            self.assertTrue(isinstance(item, Answer))


class TestItem(unittest.TestCase):
    """Tests for Item"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_item_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_item(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_learning_objective_ids(self):
        """Tests get_learning_objective_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_learning_objectives(self):
        """Tests get_learning_objectives"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question_id(self):
        """Tests get_question_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_question(self):
        """Tests get_question"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answer_ids(self):
        """Tests get_answer_ids"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_answers(self):
        """Tests get_answers"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_item_record(self):
        """Tests get_item_record"""
        pass

        pass


class TestItemForm(unittest.TestCase):
    """Tests for ItemForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        self.form = self.catalog.get_item_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_learning_objectives_metadata(self):
        """Tests get_learning_objectives_metadata"""
        pass

    @unittest.skip('unimplemented test')
    def test_set_learning_objectives(self):
        """Tests set_learning_objectives"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_learning_objectives(self):
        """Tests clear_learning_objectives"""
        pass

    def test_get_item_form_record(self):
        """Tests get_item_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_item_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestItemList(unittest.TestCase):
    """Tests for ItemList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for ItemList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.assessment.objects import ItemList
        self.item_list = list()
        self.item_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_item_form_for_create([])
            create_form.display_name = 'Test Item ' + str(num)
            create_form.description = 'Test Item for ItemList tests'
            obj = self.catalog.create_item(create_form)
            self.item_list.append(obj)
            self.item_ids.append(obj.ident)
        self.item_list = ItemList(self.item_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_items():
            cls.catalog.delete_item(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_item(self):
        """Tests get_next_item"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Item
        self.assertTrue(isinstance(self.item_list.get_next_item(), Item))

    def test_get_next_items(self):
        """Tests get_next_items"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import ItemList, Item
        new_list = self.item_list.get_next_items(2)
        self.assertTrue(isinstance(new_list, ItemList))
        for item in new_list:
            self.assertTrue(isinstance(item, Item))


class TestAssessment(unittest.TestCase):
    """Tests for Assessment"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Test object'
        cls.object = cls.catalog.create_assessment(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_level_id(self):
        """Tests get_level_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level_id)

    def test_get_level(self):
        """Tests get_level"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # From test_templates/resources.py::Resource::has_avatar_template
        self.assertTrue(isinstance(self.object.has_rubric(), bool))
        self.assertFalse(self.object.has_rubric())

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_rubric)

    @unittest.skip('unimplemented test')
    def test_get_assessment_record(self):
        """Tests get_assessment_record"""
        pass


class TestAssessmentForm(unittest.TestCase):
    """Tests for AssessmentForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        self.form = self.catalog.get_assessment_form_for_create([])

    @classmethod
    def tearDownClass(cls):
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_level_metadata(), Metadata))

    def test_set_level(self):
        """Tests set_level"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['levelId'], '')
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['levelId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_level(self):
        """Tests clear_level"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['levelId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_level()
        self.assertEqual(self.form._my_map['levelId'], '')

    def test_get_rubric_metadata(self):
        """Tests get_rubric_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_rubric_metadata(), Metadata))

    def test_set_rubric(self):
        """Tests set_rubric"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['rubricId'], '')
        self.form.set_rubric(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['rubricId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_rubric(self):
        """Tests clear_rubric"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_rubric(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['rubricId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_rubric()
        self.assertEqual(self.form._my_map['rubricId'], '')

    def test_get_assessment_form_record(self):
        """Tests get_assessment_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_assessment_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssessmentList(unittest.TestCase):
    """Tests for AssessmentList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for ResourceList
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

    def setUp(self):
        # Implemented from init template for ResourceList
        from dlkit.json_.assessment.objects import AssessmentList
        self.assessment_list = list()
        self.assessment_ids = list()
        for num in [0, 1]:
            create_form = self.catalog.get_assessment_form_for_create([])
            create_form.display_name = 'Test Assessment ' + str(num)
            create_form.description = 'Test Assessment for AssessmentList tests'
            obj = self.catalog.create_assessment(create_form)
            self.assessment_list.append(obj)
            self.assessment_ids.append(obj.ident)
        self.assessment_list = AssessmentList(self.assessment_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for ResourceList
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_assessment(self):
        """Tests get_next_assessment"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Assessment
        self.assertTrue(isinstance(self.assessment_list.get_next_assessment(), Assessment))

    def test_get_next_assessments(self):
        """Tests get_next_assessments"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentList, Assessment
        new_list = self.assessment_list.get_next_assessments(2)
        self.assertTrue(isinstance(new_list, AssessmentList))
        for item in new_list:
            self.assertTrue(isinstance(item, Assessment))


class TestAssessmentOffered(unittest.TestCase):
    """Tests for AssessmentOffered"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Assessment'
        cls.assessment = cls.catalog.create_assessment(form)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        cls.object = cls.catalog.create_assessment_offered(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_assessment_id(self):
        """Tests get_assessment_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment(self):
        """Tests get_assessment"""
        pass

    def test_get_level_id(self):
        """Tests get_level_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level_id)

    def test_get_level(self):
        """Tests get_level"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_level)

    def test_are_items_sequential(self):
        """Tests are_items_sequential"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.are_items_sequential(), bool))
        self.assertFalse(self.object.are_items_sequential())

    def test_are_items_shuffled(self):
        """Tests are_items_shuffled"""
        # From test_templates/resources.py::Resource::is_group_template
        self.assertTrue(isinstance(self.object.are_items_shuffled(), bool))
        self.assertFalse(self.object.are_items_shuffled())

    @unittest.skip('unimplemented test')
    def test_has_start_time(self):
        """Tests has_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_start_time(self):
        """Tests get_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_deadline(self):
        """Tests has_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_deadline(self):
        """Tests get_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_duration(self):
        """Tests has_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_duration(self):
        """Tests get_duration"""
        pass

    def test_is_scored(self):
        """Tests is_scored"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scored?
        self.assertRaises(KeyError,
                          self.object.is_scored)

    def test_get_score_system_id(self):
        """Tests get_score_system_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_score_system_id)

    def test_get_score_system(self):
        """Tests get_score_system"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_score_system)

    def test_is_graded(self):
        """Tests is_graded"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set graded?
        self.assertRaises(KeyError,
                          self.object.is_graded)

    def test_get_grade_system_id(self):
        """Tests get_grade_system_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade_system_id)

    def test_get_grade_system(self):
        """Tests get_grade_system"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade_system)

    def test_has_rubric(self):
        """Tests has_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.has_rubric)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric)

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_record(self):
        """Tests get_assessment_offered_record"""
        pass

        pass


class TestAssessmentOfferedForm(unittest.TestCase):
    """Tests for AssessmentOfferedForm"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedLookupSession tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedLookupSession tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

        cls.form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident,
                                                                      [])

    def setUp(self):
        self.form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident,
                                                                        [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_level_metadata(self):
        """Tests get_level_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_level_metadata(), Metadata))

    def test_set_level(self):
        """Tests set_level"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['levelId'], '')
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['levelId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_level(self):
        """Tests clear_level"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_level(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['levelId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_level()
        self.assertEqual(self.form._my_map['levelId'], '')

    def test_get_items_sequential_metadata(self):
        """Tests get_items_sequential_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_items_sequential_metadata(), Metadata))

    def test_set_items_sequential(self):
        """Tests set_items_sequential"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_items_sequential(True)
        self.assertTrue(self.form._my_map['itemsSequential'])

    def test_clear_items_sequential(self):
        """Tests clear_items_sequential"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_items_sequential(True)
        self.assertTrue(self.form._my_map['itemsSequential'])
        self.form.clear_items_sequential()
        self.assertIsNone(self.form._my_map['itemsSequential'])

    def test_get_items_shuffled_metadata(self):
        """Tests get_items_shuffled_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_items_shuffled_metadata(), Metadata))

    def test_set_items_shuffled(self):
        """Tests set_items_shuffled"""
        # From test_templates/resource.py::ResourceForm::set_group_template
        self.form.set_items_shuffled(True)
        self.assertTrue(self.form._my_map['itemsShuffled'])

    def test_clear_items_shuffled(self):
        """Tests clear_items_shuffled"""
        # From test_templates/resource.py::ResourceForm::clear_group_template
        self.form.set_items_shuffled(True)
        self.assertTrue(self.form._my_map['itemsShuffled'])
        self.form.clear_items_shuffled()
        self.assertIsNone(self.form._my_map['itemsShuffled'])

    def test_get_start_time_metadata(self):
        """Tests get_start_time_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_start_time_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_start_time(self):
        """Tests set_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_start_time(self):
        """Tests clear_start_time"""
        pass

    def test_get_deadline_metadata(self):
        """Tests get_deadline_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_deadline_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_deadline(self):
        """Tests set_deadline"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_deadline(self):
        """Tests clear_deadline"""
        pass

    def test_get_duration_metadata(self):
        """Tests get_duration_metadata"""
        # From test_templates/resource.py::ResourceForm::get_group_metadata_template
        self.assertTrue(isinstance(self.form.get_duration_metadata(), Metadata))

    @unittest.skip('unimplemented test')
    def test_set_duration(self):
        """Tests set_duration"""
        pass

    @unittest.skip('unimplemented test')
    def test_clear_duration(self):
        """Tests clear_duration"""
        pass

    def test_get_score_system_metadata(self):
        """Tests get_score_system_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_score_system_metadata(), Metadata))

    def test_set_score_system(self):
        """Tests set_score_system"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['scoreSystemId'], '')
        self.form.set_score_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['scoreSystemId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_score_system(self):
        """Tests clear_score_system"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_score_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['scoreSystemId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_score_system()
        self.assertEqual(self.form._my_map['scoreSystemId'], '')

    def test_get_grade_system_metadata(self):
        """Tests get_grade_system_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_grade_system_metadata(), Metadata))

    def test_set_grade_system(self):
        """Tests set_grade_system"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['gradeSystemId'], '')
        self.form.set_grade_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['gradeSystemId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_grade_system(self):
        """Tests clear_grade_system"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_grade_system(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['gradeSystemId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_grade_system()
        self.assertEqual(self.form._my_map['gradeSystemId'], '')

    def test_get_assessment_offered_form_record(self):
        """Tests get_assessment_offered_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_assessment_offered_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssessmentOfferedList(unittest.TestCase):
    """Tests for AssessmentOfferedList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentOfferedList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentOfferedList tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

        cls.form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident,
                                                                      [])

    def setUp(self):
        from dlkit.json_.assessment.objects import AssessmentOfferedList
        self.assessment_offered_list = list()
        self.assessment_offered_ids = list()
        for num in [0, 1]:
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident,
                                                                       [])
            form.display_name = 'Test AssessmentOffered ' + str(num)
            form.description = 'Test AssessmentOffered for AssessmentOfferedList tests'
            obj = self.catalog.create_assessment_offered(form)
            self.assessment_offered_list.append(obj)
            self.assessment_offered_ids.append(obj.ident)
        self.assessment_offered_list = AssessmentOfferedList(self.assessment_offered_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_assessment_offered(self):
        """Tests get_next_assessment_offered"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOffered
        self.assertTrue(isinstance(self.assessment_offered_list.get_next_assessment_offered(), AssessmentOffered))

    def test_get_next_assessments_offered(self):
        """Tests get_next_assessments_offered"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentOfferedList, AssessmentOffered
        new_list = self.assessment_offered_list.get_next_assessments_offered(2)
        self.assertTrue(isinstance(new_list, AssessmentOfferedList))
        for item in new_list:
            self.assertTrue(isinstance(item, AssessmentOffered))


class TestAssessmentTaken(unittest.TestCase):
    """Tests for AssessmentTaken"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test catalog'
        create_form.description = 'Test catalog description'
        cls.catalog = cls.svc_mgr.create_bank(create_form)

        form = cls.catalog.get_assessment_form_for_create([])
        form.display_name = 'Assessment'
        cls.assessment = cls.catalog.create_assessment(form)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident, [])
        form.display_name = 'Test assessment offered'
        cls.offered = cls.catalog.create_assessment_offered(form)

        form = cls.catalog.get_assessment_taken_form_for_create(cls.offered.ident,
                                                                [])
        cls.object = cls.catalog.create_assessment_taken(form)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            for offered in cls.catalog.get_assessments_offered_for_assessment(obj.ident):
                for taken in cls.catalog.get_assessments_taken_for_assessment_offered(offered.ident):
                    cls.catalog.delete_assessment_taken(taken.ident)
                cls.catalog.delete_assessment_offered(offered.ident)
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered_id(self):
        """Tests get_assessment_offered_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_offered(self):
        """Tests get_assessment_offered"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taker_id(self):
        """Tests get_taker_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taker(self):
        """Tests get_taker"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taking_agent_id(self):
        """Tests get_taking_agent_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_taking_agent(self):
        """Tests get_taking_agent"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_started(self):
        """Tests has_started"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_actual_start_time(self):
        """Tests get_actual_start_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_ended(self):
        """Tests has_ended"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_completion_time(self):
        """Tests get_completion_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_time_spent(self):
        """Tests get_time_spent"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_completion(self):
        """Tests get_completion"""
        pass

    def test_is_scored(self):
        """Tests is_scored"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scored?
        self.assertRaises(KeyError,
                          self.object.is_scored)

    def test_get_score_system_id(self):
        """Tests get_score_system_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scoreSystemId?
        self.assertRaises(KeyError,
                          self.object.get_score_system_id)

    def test_get_score_system(self):
        """Tests get_score_system"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set scoreSystemId?
        self.assertRaises(KeyError,
                          self.object.get_score_system)

    @unittest.skip('unimplemented test')
    def test_get_score(self):
        """Tests get_score"""
        pass

    def test_is_graded(self):
        """Tests is_graded"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set graded?
        self.assertRaises(KeyError,
                          self.object.is_graded)

    def test_get_grade_id(self):
        """Tests get_grade_id"""
        # From test_templates/resources.py::Resource::get_avatar_id_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade_id)

    def test_get_grade(self):
        """Tests get_grade"""
        # From test_templates/resources.py::Resource::get_avatar_template
        self.assertRaises(errors.IllegalState,
                          self.object.get_grade)

    @unittest.skip('unimplemented test')
    def test_get_feedback(self):
        """Tests get_feedback"""
        pass

    def test_has_rubric(self):
        """Tests has_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.has_rubric)

    def test_get_rubric_id(self):
        """Tests get_rubric_id"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric_id)

    def test_get_rubric(self):
        """Tests get_rubric"""
        # This may be an error in the spec -- not in _my_map
        # since there are no form methods to set rubricId?
        self.assertRaises(KeyError,
                          self.object.get_rubric)

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_record(self):
        """Tests get_assessment_taken_record"""
        pass


class TestAssessmentTakenForm(unittest.TestCase):
    """Tests for AssessmentTakenForm"""

    @classmethod
    def setUpClass(cls):
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

        cls.form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident, [])

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_taker_metadata(self):
        """Tests get_taker_metadata"""
        # From test_templates/resource.py::ResourceForm::get_avatar_metadata_template
        self.assertTrue(isinstance(self.form.get_taker_metadata(), Metadata))

    def test_set_taker(self):
        """Tests set_taker"""
        # From test_templates/resource.py::ResourceForm::set_avatar_template
        self.assertEqual(self.form._my_map['takerId'], '')
        self.form.set_taker(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['takerId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')

    def test_clear_taker(self):
        """Tests clear_taker"""
        # From test_templates/resource.py::ResourceForm::clear_avatar_template
        self.form.set_taker(Id('repository.Asset%3Afake-id%40ODL.MIT.EDU'))
        self.assertEqual(self.form._my_map['takerId'],
                         'repository.Asset%3Afake-id%40ODL.MIT.EDU')
        self.form.clear_taker()
        self.assertEqual(self.form._my_map['takerId'], '')

    def test_get_assessment_taken_form_record(self):
        """Tests get_assessment_taken_form_record"""
        with self.assertRaises(errors.Unsupported):
            self.form.get_assessment_taken_form_record(Type('osid.Osid%3Afake-record%40ODL.MIT.EDU'))
        # Here check for a real record?


class TestAssessmentTakenList(unittest.TestCase):
    """Tests for AssessmentTakenList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentTakenList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentTakenList tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

        form = cls.catalog.get_assessment_offered_form_for_create(cls.assessment.ident,
                                                                  [])
        cls.assessment_offered = cls.catalog.create_assessment_offered(form)

        cls.form = cls.catalog.get_assessment_taken_form_for_create(cls.assessment_offered.ident,
                                                                    [])

    def setUp(self):
        from dlkit.json_.assessment.objects import AssessmentTakenList
        self.assessment_taken_list = list()
        self.assessment_taken_ids = list()
        for num in [0, 1]:
            form = self.catalog.get_assessment_offered_form_for_create(self.assessment.ident,
                                                                       [])
            form.display_name = 'Test AssessmentOffered ' + str(num)
            form.description = 'Test AssessmentOffered for AssessmentTakenList tests'
            obj = self.catalog.create_assessment_offered(form)

            form = self.catalog.get_assessment_taken_form_for_create(obj.ident, [])
            obj = self.catalog.create_assessment_taken(form)
            self.assessment_taken_list.append(obj)
            self.assessment_taken_ids.append(obj.ident)
        self.assessment_taken_list = AssessmentTakenList(self.assessment_taken_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments_taken():
            cls.catalog.delete_assessment_taken(obj.ident)
        for obj in cls.catalog.get_assessments_offered():
            cls.catalog.delete_assessment_offered(obj.ident)
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_assessment_taken(self):
        """Tests get_next_assessment_taken"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTaken
        self.assertTrue(isinstance(self.assessment_taken_list.get_next_assessment_taken(), AssessmentTaken))

    def test_get_next_assessments_taken(self):
        """Tests get_next_assessments_taken"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import AssessmentTakenList, AssessmentTaken
        new_list = self.assessment_taken_list.get_next_assessments_taken(2)
        self.assertTrue(isinstance(new_list, AssessmentTakenList))
        for item in new_list:
            self.assertTrue(isinstance(item, AssessmentTaken))


class TestAssessmentSection(unittest.TestCase):
    """Tests for AssessmentSection"""

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken_id(self):
        """Tests get_assessment_taken_id"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_taken(self):
        """Tests get_assessment_taken"""
        pass

    @unittest.skip('unimplemented test')
    def test_has_allocated_time(self):
        """Tests has_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_allocated_time(self):
        """Tests get_allocated_time"""
        pass

    @unittest.skip('unimplemented test')
    def test_are_items_sequential(self):
        """Tests are_items_sequential"""
        pass

    @unittest.skip('unimplemented test')
    def test_are_items_shuffled(self):
        """Tests are_items_shuffled"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_assessment_section_record(self):
        """Tests get_assessment_section_record"""
        pass


class TestAssessmentSectionList(unittest.TestCase):
    """Tests for AssessmentSectionList"""

    @classmethod
    def setUpClass(cls):
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for AssessmentSectionList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        create_form = cls.catalog.get_assessment_form_for_create([])
        create_form.display_name = 'Test Assessment'
        create_form.description = 'Test Assessment for AssessmentSectionList tests'
        cls.assessment = cls.catalog.create_assessment(create_form)

        cls.form = cls.catalog.get_assessment_part_form_for_create_for_assessment(cls.assessment.ident,
                                                                                  [])

    def setUp(self):
        from dlkit.json_.assessment.objects import AssessmentSectionList
        self.assessment_section_list = list()
        self.assessment_section_ids = list()

        for num in [0, 1]:
            form = self.catalog.get_assessment_part_form_for_create_for_assessment(self.assessment.ident, [])

            obj = self.catalog.create_assessment_part_for_assessment(form)

            self.assessment_section_list.append(obj)
            self.assessment_section_ids.append(obj.ident)
        self.assessment_section_list = AssessmentSectionList(self.assessment_section_list)

    @classmethod
    def tearDownClass(cls):
        for obj in cls.catalog.get_assessments():
            cls.catalog.delete_assessment(obj.ident)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_assessment_section(self):
        """Tests get_next_assessment_section"""
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        self.assertTrue(isinstance(self.assessment_section_list.get_next_assessment_section(), AssessmentPart))

    def test_get_next_assessment_sections(self):
        """Tests get_next_assessment_sections"""
        from dlkit.abstract_osid.assessment.objects import AssessmentSectionList
        from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPart
        new_list = self.assessment_section_list.get_next_assessment_sections(2)
        self.assertTrue(isinstance(new_list, AssessmentSectionList))
        for item in new_list:
            self.assertTrue(isinstance(item, AssessmentPart))


class TestBank(unittest.TestCase):
    """Tests for Bank"""

    @unittest.skip('unimplemented test')
    def test_get_bank_record(self):
        """Tests get_bank_record"""
        pass


class TestBankForm(unittest.TestCase):
    """Tests for BankForm"""

    @unittest.skip('unimplemented test')
    def test_get_bank_form_record(self):
        """Tests get_bank_form_record"""
        pass


class TestBankList(unittest.TestCase):
    """Tests for BankList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinList
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        cls.bank_ids = list()

    def setUp(self):
        # Implemented from init template for BinList
        from dlkit.json_.assessment.objects import BankList
        self.bank_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test Bank ' + str(num)
            create_form.description = 'Test Bank for BankList tests'
            obj = self.svc_mgr.create_bank(create_form)
            self.bank_list.append(obj)
            self.bank_ids.append(obj.ident)
        self.bank_list = BankList(self.bank_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinList
        for obj in cls.bank_ids:
            cls.svc_mgr.delete_bank(obj)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_bank(self):
        """Tests get_next_bank"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import Bank
        self.assertTrue(isinstance(self.bank_list.get_next_bank(), Bank))

    def test_get_next_banks(self):
        """Tests get_next_banks"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import BankList, Bank
        new_list = self.bank_list.get_next_banks(2)
        self.assertTrue(isinstance(new_list, BankList))
        for item in new_list:
            self.assertTrue(isinstance(item, Bank))


class TestBankNode(unittest.TestCase):
    """Tests for BankNode"""

    @unittest.skip('unimplemented test')
    def test_get_bank(self):
        """Tests get_bank"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_parent_bank_nodes(self):
        """Tests get_parent_bank_nodes"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_child_bank_nodes(self):
        """Tests get_child_bank_nodes"""
        pass


class TestBankNodeList(unittest.TestCase):
    """Tests for BankNodeList"""

    @classmethod
    def setUpClass(cls):
        # Implemented from init template for BinNodeList
        cls.svc_mgr = Runtime().get_service_manager('ASSESSMENT', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_bank_form_for_create([])
        create_form.display_name = 'Test Bank'
        create_form.description = 'Test Bank for BankNodeList tests'
        cls.catalog = cls.svc_mgr.create_bank(create_form)
        cls.bank_node_ids = list()

    def setUp(self):
        # Implemented from init template for BinNodeList
        from dlkit.json_.assessment.objects import BankNodeList, BankNode
        self.bank_node_list = list()
        for num in [0, 1]:
            create_form = self.svc_mgr.get_bank_form_for_create([])
            create_form.display_name = 'Test BankNode ' + str(num)
            create_form.description = 'Test BankNode for BankNodeList tests'
            obj = self.svc_mgr.create_bank(create_form)
            self.bank_node_list.append(BankNode(obj.object_map))
            self.bank_node_ids.append(obj.ident)
        # Not put the catalogs in a hierarchy
        self.svc_mgr.add_root_bank(self.bank_node_list[0].ident)
        self.svc_mgr.add_child_bank(
            self.bank_node_list[0].ident,
            self.bank_node_list[1].ident)
        self.bank_node_list = BankNodeList(self.bank_node_list)

    @classmethod
    def tearDownClass(cls):
        # Implemented from init template for BinNodeList
        for obj in cls.bank_node_ids:
            cls.svc_mgr.delete_bank(obj)
        cls.svc_mgr.delete_bank(cls.catalog.ident)

    def test_get_next_bank_node(self):
        """Tests get_next_bank_node"""
        # From test_templates/resource.py::ResourceList::get_next_resource_template
        from dlkit.abstract_osid.assessment.objects import BankNode
        self.assertTrue(isinstance(self.bank_node_list.get_next_bank_node(), BankNode))

    def test_get_next_bank_nodes(self):
        """Tests get_next_bank_nodes"""
        # From test_templates/resource.py::ResourceList::get_next_resources_template
        from dlkit.abstract_osid.assessment.objects import BankNodeList, BankNode
        new_list = self.bank_node_list.get_next_bank_nodes(2)
        self.assertTrue(isinstance(new_list, BankNodeList))
        for item in new_list:
            self.assertTrue(isinstance(item, BankNode))


class TestResponseList(unittest.TestCase):
    """Tests for ResponseList"""

    @unittest.skip('unimplemented test')
    def test_get_next_response(self):
        """Tests get_next_response"""
        pass

    @unittest.skip('unimplemented test')
    def test_get_next_responses(self):
        """Tests get_next_responses"""
        pass
